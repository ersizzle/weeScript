# WeeScript — project context for Claude Code

A single-file Maya tool (`weeScript.py`, Python, Redshift renderer) that builds a docked
shelf-style panel (`weeTools`) of modeling / shading / naming / render / animation / window
buttons. Long-running personal tool by the user (ersizzle). This file is the handoff from a
Cowork session that redesigned the UI and refactored a lot of the code.

## How it loads / runs

- Repo: https://github.com/ersizzle/weeScript  (public, default branch `master`, file at root).
- Load into Maya (Python script editor):
  ```python
  import urllib.request, __main__
  exec(urllib.request.urlopen('https://raw.githubusercontent.com/ersizzle/weeScript/master/weeScript.py').read().decode('utf-8'), __main__.__dict__)
  ```
- **Alt+1** hotkey re-pulls the script from that GitHub raw URL and rebuilds (so a pushed commit
  is picked up automatically; GitHub raw CDN caches ~5 min).
- Must `exec` into `__main__.__dict__` — button/hotkey command strings (e.g. `'fTrans()'`) are
  evaluated in Maya's `__main__` namespace, so all functions must live there.
- Bottom of the file: loads redshift4maya, builds the `workspaceControl`, and registers
  `nameCommand`/`hotkey` bindings. The panel is dockable (`workspaceControl`, responsive width).

## Conventions (IMPORTANT — keep these)

- **Indentation is TABS** throughout. Do not introduce spaces (one past offender, `refEnable`,
  was fixed). Mixing breaks Python 3.
- **Button commands are STRING literals** like `command='fTrans()'`, routed through a `_guard()`
  wrapper (see below). The named functions must stay global and keep their names, or bindings break.
- After ANY edit, sanity-check in a shell:
  - `python3 -c "import ast; ast.parse(open('weeScript.py').read())"` (parse)
  - confirm every `'name()'` button command maps to a `def name(`.
- **Null-byte gotcha:** this file has repeatedly picked up stray NUL bytes (in the trailing
  comment divider / via round-trips). If `grep` says "binary file" or parsing fails with
  "source code string cannot contain null bytes", strip them:
  `python3 -c "p='weeScript.py';b=open(p,'rb').read();open(p,'wb').write(b.replace(b'\x00',b''))"`
- Target Maya 2022+ (Python 3). `execfile`/old `reload` were removed; `exec(open().read())` and
  `importlib.reload` are used instead.

## Architecture

- `weeToolsUI()` is a **data-driven UI builder**. Helpers inside it:
  - `addRow(parent, items)` — a `formLayout` row; buttons fill width equally (responsive).
    `items` = list of `(label, command, colorKey)`. Auto height: 34 for two-line labels (contain
    `\n`), else 26.
  - `addField(parent)` — full-width text field (returns the control; used for `field1`/`field2`).
  - `addLabel(parent, text)` — small italic sub-label.
  - `addMinMax(parent)` / `addAxis(parent)` — Animation section Min/Max entry boxes and X/Y/Z
    checkboxes (globals `animMin/animMax/animX/animY/animZ`).
  - `section(label, collapse)` — collapsible `frameLayout`.
  - Semantic color palette `col`: gray=general, coral=destructive, purple=shading, amber=lights/UV,
    blue=render/attrs, teal=display, indigo=windows.
- `_guard(cmd)` (module level, near top): `eval`s a button command in try/except; turns an empty/
  wrong selection (IndexError) or any error into an `mc.warning` instead of a raw traceback. All
  buttons are wired as `command='_guard("the_real_call()")'`. Hotkeys still call functions directly.
- De-duplicated helpers (each with thin one-line wrappers that keep the original names):
  - `_addSuffix(suffix)` → `addgeo/addgrp/.../addH` (renaming buttons).
  - `_setRes(w, h)` → `x1080x1920/...` (resolution buttons; labels show the ACTUAL output res).
  - `_togglePanels(flag)` → `showjoint/showpoly/showcurve/showlight/showcam` (display toggles).
  - `shaderName()` uses a `(nodeType, suffix, numbered)` table instead of ~120 repeated blocks.

## Material system ("SHADING" tab)

Four buttons, all driven by one helper `_pbrMat(metal, detail, colorlayer=False)`:

| Button | Function | metal | detail |
|--------|----------|-------|--------|
| PBR B_D | `pbrBD()` | dielectric (IOR 1.5) | bump  |
| PBR B_M | `pbrBM()` | metallic (metalness 1) | bump |
| PBR D_D | `pbrDD()` | dielectric | displacement |
| PBR D_M | `pbrDM()` | metallic | displacement |

`_pbrMat` makes ONE shared `RedshiftStandardMaterial` for the whole selection: random in-gamut
color via `colorsys.hsv_to_rgb`, `refl_weight=1`, `refl_roughness=0.4`, metalness/IOR per `metal`.
It relies on the material's built-in Fresnel (no external Fresnel rig — that was removed as
redundant/non-physical). Detail = a `RedshiftMaxonNoise` (Maxon noise, not RedshiftNoise) →
`RedshiftBumpMap`→`bump_input`, or `RedshiftDisplacement`→ shading group `displacementShader`
(+ enables `rsEnableSubdivision`/`rsMaxTessellationSubdivs`/`rsEnableDisplacement` on each shape).

`colorlayer=True` (only `pbrBD` uses it) adds a `RedshiftColorLayer` driving base color:
- Color Layer `base_color` = the random color; Color Layer `outColor` → material `base_color`.
- Layer 1 = `RedshiftAmbientOcclusion`: bright/dark swapped (bright=0,0,0 / dark=1,1,1),
  maxDistance=50, spread=0.4; `ao.outColorR` → `layer1_mask`; `layer1_enable=1`.
- Layer 2 = `RedshiftCurvature`: `curv.out` (scalar) → `layer2_mask`; `layer2_enable=1`;
  a second Maxon noise `outColorR` → curvature output max.
- Redshift-specific setAttr/connectAttr are individually wrapped in try/except so a wrong attr
  name warns for that one line instead of aborting the whole build.

`pbrTile()` ("PBR Tile" button) = `_pbrMat(False, None, colorlayer=True, ss_weight=0.08, roughlayer=True)`:
- `detail=None` → NO bump/displacement branch and no `_rsMaxon` node at all (the bump rig was
  removed on purpose; `_pbrMat` guards node creation with `if detail:` / `elif detail:`).
- `ss_weight=0.08` → subsurface weight on the standard material (tries `.ss_weight`,
  `.subsurface_weight`, `.ms_amount` in order).
- `roughlayer=True` → a SECOND `RedshiftColorLayer` (`*_rsRoughLyr`), separate from the base_color
  one: `layer2_enable=1` (layer 1 is on by default), layer1 mask ← Maxon noise **Stupl** with
  `coord_scale_global` 1.5, layer2 mask ← Maxon noise **Turbulence** with `coord_scale_global` 10,
  then `rsRoughLyr.outColorR` → material `refl_roughness`.
- `_setNoiseType(node, 'Stupl')` (module level) resolves a Maxon noise type by its UI NAME via
  `mc.attributeQuery(..., listEnum=True)` instead of a hard-coded index — enum order differs
  between Redshift builds, which is what made the old `noise_type=10  # Luka` fragile. `_pbrMat`'s
  `noise_type` arg now accepts a string name or an int.

`mat1()` (hotkey Ctrl+Shift+Q) and `matphong()` still exist and were NOT part of the matrix.
Deleted earlier: `mat5`, `pbrd`, `pbrm`, and the 14 PRE-SHADING material presets + OCIO `aces()`.

## Render settings (`fnrender` etc.)

User maintains these. Research notes given (Redshift): `imageFormat 1`=EXR (good for final);
GI enums `primaryGIEngine 4`=Brute Force, `secondaryGIEngine 2`=Irradiance Point Cloud,
`denoiseEngine 3`=OptiX. Flagged as worth improving (user may or may not have applied):
`bruteForceGINumRays 2048` too high (→~64), `unifiedMaxSamples 8192` too high (→~512),
IPC secondary flickers in animation (use Brute Force secondary), and `animation=1` with no frame
range set (snippet provided to pull start/end from `playbackOptions`). User does NOT currently use
OptiX. Don't change render functions without asking.

## Open TODOs / verify in Maya (couldn't test live from Cowork)

- Confirm these Redshift attribute names on the user's version; some are wrapped in try/except:
  `RedshiftMaxonNoise` scale (tried `.scale` / `.globalScale`), `RedshiftCurvature` output-max
  (tried `outputMax` / `output_max`), AO `maxDistance` / `spread`, Color Layer `layer1_mask` /
  `layer2_mask` / `layer1_enable` / `layer2_enable` / `base_color`. (`refl_ior` also try/excepted.)
- Optional: cache-buster `?t=<time>` on the GitHub raw URL (Alt+1) to skip the ~5 min CDN cache.
- Optional: a "Reload" button in the WINDOWS section that runs the GitHub fetch.
- Optional niceties discussed but not done: button tooltips (`annotation`), routing hotkeys through
  `_guard` too, exposing roughness/noise-scale via fields, blend modes on the Color Layer.
- `exportdeskma()` logic is quirky (exports whole selection per name) but no longer crashes.

## Git

Cowork could not push (no credentials). Claude Code CAN push using the user's local git auth:
```
git add weeScript.py CLAUDE.md
git commit -m "..."
git push        # to origin master
```
