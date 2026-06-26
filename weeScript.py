 #to load this tool from GitHub, paste this into Maya's Python script editor:
#import urllib.request, __main__; exec(urllib.request.urlopen('https://raw.githubusercontent.com/ersizzle/weeScript/master/weeScript.py').read().decode('utf-8'), __main__.__dict__)
import maya.cmds as mc
import maya.mel as mel

def _guard(cmd):
	#Run a button command, turning an empty/wrong selection into a friendly
	#warning instead of a raw traceback in the script editor.
	try:
		eval(cmd)
	except IndexError:
		mc.warning('weeTools: select the right object(s) for this action first.')
	except Exception as e:
		mc.warning('weeTools: ' + str(e))

ui='weeTools'
title = ui

if mc.workspaceControl(ui, q=True, exists=True):
	mc.deleteUI(ui, control=True)
if mc.window(ui, exists=True):
	mc.deleteUI(ui)

def weeToolsUI():
	global field1
	global field2
	global animMin, animMax, animX, animY, animZ
	W = 230
	col = {
		'gray':   [0.29, 0.29, 0.28],
		'coral':  [0.40, 0.24, 0.21],
		'purple': [0.31, 0.26, 0.42],
		'amber':  [0.42, 0.34, 0.16],
		'blue':   [0.18, 0.27, 0.42],
		'teal':   [0.13, 0.34, 0.29],
		'indigo': [0.25, 0.25, 0.46],
	}
	def addRow(parent, items):
		n = len(items)
		h = 34 if any('\n' in l for l, c, k in items) else 26
		fl = mc.formLayout(parent=parent, numberOfDivisions=100, height=h + 2)
		bs = []
		for label, cmd, c in items:
			bs.append(mc.button(parent=fl, label=label, height=h, bgc=col[c], command='_guard("%s")' % cmd))
		for i, b in enumerate(bs):
			lp = int(round(i * 100.0 / n))
			rp = int(round((i + 1) * 100.0 / n))
			mc.formLayout(fl, e=True, attachPosition=[(b, 'left', 1, lp), (b, 'right', 1, rp)], attachForm=[(b, 'top', 1), (b, 'bottom', 1)])
		return fl
	def addField(parent):
		fl = mc.formLayout(parent=parent, height=24)
		t = mc.textField(parent=fl)
		mc.formLayout(fl, e=True, attachForm=[(t, 'left', 2), (t, 'right', 2), (t, 'top', 1), (t, 'bottom', 1)])
		return t
	def addLabel(parent, text):
		mc.text(parent=parent, label=text, height=14, align='left', font='smallObliqueLabelFont')
	def addMinMax(parent):
		global animMin, animMax
		fl = mc.formLayout(parent=parent, numberOfDivisions=100, height=24)
		l1 = mc.text(parent=fl, label='Min', align='right')
		animMin = mc.textField(parent=fl, text='-1')
		l2 = mc.text(parent=fl, label='Max', align='right')
		animMax = mc.textField(parent=fl, text='1')
		mc.formLayout(fl, e=True, attachPosition=[(l1, 'left', 2, 0), (l1, 'right', 2, 16), (animMin, 'left', 0, 16), (animMin, 'right', 3, 50), (l2, 'left', 2, 50), (l2, 'right', 2, 66), (animMax, 'left', 0, 66), (animMax, 'right', 2, 100)], attachForm=[(l1, 'top', 4), (l1, 'bottom', 2), (animMin, 'top', 1), (animMin, 'bottom', 1), (l2, 'top', 4), (l2, 'bottom', 2), (animMax, 'top', 1), (animMax, 'bottom', 1)])
	def addAxis(parent):
		global animX, animY, animZ
		fl = mc.formLayout(parent=parent, numberOfDivisions=100, height=22)
		animX = mc.checkBox(parent=fl, label='X', value=True)
		animY = mc.checkBox(parent=fl, label='Y', value=True)
		animZ = mc.checkBox(parent=fl, label='Z', value=True)
		mc.formLayout(fl, e=True, attachPosition=[(animX, 'left', 4, 4), (animX, 'right', 0, 33), (animY, 'left', 4, 36), (animY, 'right', 0, 66), (animZ, 'left', 4, 69), (animZ, 'right', 0, 100)], attachForm=[(animX, 'top', 2), (animX, 'bottom', 2), (animY, 'top', 2), (animY, 'bottom', 2), (animZ, 'top', 2), (animZ, 'bottom', 2)])
	def section(label, collapse=False):
		return mc.frameLayout(parent=main, label='  ' + label, collapsable=True, collapse=collapse, marginHeight=2, backgroundColor=[0.2, 0.2, 0.2])
	main = mc.columnLayout(adjustableColumn=True, rowSpacing=1, width=W)
	f = section('Modeling', collapse=False)
	addRow(f, [('Freeze\nTransform', 'fTrans()', 'gray'), ('Delete\nHistory', 'dHis()', 'coral'), ('Delete\nNon-Def', 'dnondefHis()', 'coral'), ('Center\nPivot', 'cPiv()', 'gray')])
	addRow(f, [('Send to\nOrigin', 'zero()', 'gray'), ('Build\nTile', 'buildTiles()', 'gray'), ('Tile\nSquare', 'gridTiles()', 'gray'), ('Tile\nRectangle', 'bondTiles()', 'gray'), ('Group', 'group()', 'gray'), ('Auto UV', 'autoUV()', 'amber')])
	addRow(f, [('UV\nCopy', 'UVcopy()', 'amber'), ('BBox\nOn', 'box()', 'teal'), ('BBox\nOff', 'unbox()', 'teal'), ('Lock\nAttrs', 'lock()', 'blue'), ('Unlock\nAttrs', 'unlock()', 'blue')])
	f = section('Name', collapse=False)
	field1 = addField(f)
	field2 = addField(f)
	addRow(f, [('Rename', 'changeName()', 'gray'), ('Shader', 'shaderName()', 'gray'), ('Prefix', 'prefix()', 'gray'), ('Suffix', 'sufix()', 'gray'), ('Replace', 'search()', 'gray')])
	f = section('Pre-name', collapse=True)
	addRow(f, [('+geo', 'addgeo()', 'gray'), ('+grp', 'addgrp()', 'gray'), ('+low', 'addlow()', 'gray'), ('+high', 'addhigh()', 'gray'), ('+lgt', 'addlgt()', 'gray'), ('+off', 'addoff()', 'gray')])
	addRow(f, [('+S', 'addS()', 'gray'), ('+SG', 'addSG()', 'gray'), ('+L', 'addL()', 'gray'), ('+R', 'addR()', 'gray'), ('+top', 'addtop()', 'gray'), ('+mid', 'addmid()', 'gray'), ('+bot', 'addbot()', 'gray')])
	addRow(f, [('+A', 'addA()', 'gray'), ('+B', 'addB()', 'gray'), ('+C', 'addC()', 'gray'), ('+D', 'addD()', 'gray'), ('+E', 'addE()', 'gray'), ('+F', 'addF()', 'gray'), ('+G', 'addG()', 'gray'), ('+H', 'addH()', 'gray')])
	f = section('Shading', collapse=False)
	addRow(f, [('Tess 2', 'tess2()', 'purple'), ('Tess 3', 'tess3()', 'purple'), ('Tess Off', 'untess()', 'purple')])
	addRow(f, [('Displace\nOn', 'disp()', 'teal'), ('Displace\nOff', 'undisp()', 'teal'), ('Backface', 'backface()', 'teal')])
	addRow(f, [('PBR\nB_D', 'pbrBD()', 'purple'), ('PBR\nB_M', 'pbrBM()', 'purple'), ('PBR\nD_D', 'pbrDD()', 'purple'), ('PBR\nD_M', 'pbrDM()', 'purple'), ('PBR\nTile', 'pbrTile()', 'purple')])
	addRow(f, [('PrimVis\nOn', 'primvis()', 'teal'), ('PrimVis\nOff', 'unprimvis()', 'teal')])
	addRow(f, [('sRGB', 'setsrgb()', 'purple'), ('Linear', 'setlin()', 'purple'), ('TexConn', 'texcon()', 'purple'), ('TexChnge', 'replaceTextures()', 'purple'), ('Phong', 'matphong()', 'gray')])
	f = section('Render', collapse=False)
	addLabel(f, '  Output')
	addRow(f, [('RS', 'redshift()', 'blue'), ('Final', 'fnrender()', 'blue'), ('Pre', 'prerender()', 'blue'), ('Atmos', 'atmos()', 'purple'), ('Un-\nAtmos', 'unatmos()', 'purple')])
	addLabel(f, '  Lights')
	addRow(f, [('Dome', 'domelgt()', 'amber'), ('Area', 'arealgt()', 'amber'), ('Point', 'pointlgt()', 'amber')])
	addRow(f, [('Spot', 'spotlgt()', 'amber'), ('Direct.', 'directlgt()', 'amber'), ('Mesh\nLight', 'meshlgt()', 'amber')])
	addLabel(f, '  Resolution')
	addRow(f, [('1280\n720', 'x720x1280()', 'gray'), ('1080\n1080', 'x1080x1080()', 'gray'), ('1920\n1080', 'x1080x1920()', 'gray'), ('1080\n1920', 'x1920x1080()', 'gray'), ('2560\n1440', 'x1440x2560()', 'gray'), ('1440\n2560', 'x2560x1440()', 'gray'), ('3840\n2160', 'x2148x3840()', 'gray'), ('2160\n3840', 'x3840x2160()', 'gray')])
	addLabel(f, '  Scene tools')
	addRow(f, [('Preserve\nEdge', 'preserveedge()', 'gray'), ('Bokeh', 'bokeh()', 'blue'), ('Locator', 'targetselect()', 'gray'), ('Render\nCam', 'rendercam()', 'blue')])
	addRow(f, [('Checker', 'checkerfield()', 'gray'), ('Node\nType', 'nodetype()', 'gray'), ('Snap &\nBake', 'snp()', 'gray')])
	addLabel(f, '  Matte / output')
	addRow(f, [('Light\nBlocker', 'lightblocker()', 'blue'), ('Matte\nAll', 'matteAll()', 'blue'), ('Matte 1', 'matteOne()', 'blue'), ('Matte\nIsolate', 'isolateObject()', 'blue'), ('Save\nIncr.', 'incsave()', 'gray')])
	f = section('Display', collapse=True)
	addRow(f, [('Joints', 'showjoint()', 'teal'), ('Polys', 'showpoly()', 'teal'), ('Curves', 'showcurve()', 'teal')])
	addRow(f, [('Lights', 'showlight()', 'teal'), ('Cameras', 'showcam()', 'teal'), ('All', 'showallobjects()', 'teal')])
	addRow(f, [('Cam\nSetup', 'camset()', 'teal'), ('Focus', 'focussett()', 'teal')])
	f = section('Animation', collapse=True)
	addLabel(f, '  Random range')
	addMinMax(f)
	addLabel(f, '  Axes')
	addAxis(f)
	addRow(f, [('Translate', 'translate()', 'gray'), ('Scale', 'scale()', 'gray'), ('Rotate', 'rotate()', 'gray'), ('Bake Sim', 'bakesimulation()', 'gray')])
	f = section('Windows', collapse=False)
	addRow(f, [('Render\nView', 'renderview()', 'indigo'), ('Hyper-\nshade', 'hyper()', 'indigo'), ('UV\nEditor', 'uveditor()', 'indigo'), ('Script\nEditor', 'scripteditor()', 'indigo')])
	addRow(f, [('Render\nSettings', 'rendersettings()', 'indigo'), ('Graph\nEditor', 'grapheditor()', 'indigo'), ('Node\nEditor', 'nodeeditor()', 'indigo'), ('Attr\nSpread', 'attspread()', 'indigo')])
	addRow(f, [('Light\nLink', 'lightlink()', 'indigo'), ('RS\nFeedback', 'rsfeedback()', 'indigo')])

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

def cPiv():
	mc.xform (ws=True, p=True, cp=True) #CenterPivot
def fTrans():
	mc.makeIdentity( apply=True )
def dHis():
	mc.delete (ch=True) #DeleteHistory
def dnondefHis():
	mel.eval('BakeNonDefHistory')
def bPiv():
	#set pivot of objects to it's center and bottom
	#this script must be edited for the exact point where at it's bottom at x-y-z
	sel_n = mc.ls(selection=True, type='transform')
	for obj in sel_n:
		bbox = mc.xform (obj, q=True, ws=True, bb=True)
		mc.xform (obj, ws=True, p=True, cp=True)
		centerPos = mc.xform (obj, q=True, ws=True, sp=True)
		mc.xform (obj, ws=True, piv=(centerPos[0], bbox[1], centerPos[2]))
def UVcopy():
	#grab all the selected objects
	selectedObjects = mc.ls(sl=True)
	#save first one into variable
	#pop first one out of the selected objects list
	driver = selectedObjects.pop(0)
	#for each object in the selected objects list
	for object in selectedObjects:
		mc.select([driver,object])
		mc.transferAttributes(sampleSpace=4,transferUVs=2,transferColors=2)
def zeropiv():
	sel_n = mc.ls(selection=True, type='transform')
	for obj in sel_n:
		mc.xform (obj, ws=True, piv=(0, 0, 0))
def box():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.overrideEnabled', 1)
		mc.setAttr (i+'.overrideLevelOfDetail', 1)
def unbox():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.overrideEnabled', 0)
		mc.setAttr (i+'.overrideLevelOfDetail', 0)
def lock():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.tx', lock=True)
		mc.setAttr (i+'.ty', lock=True)
		mc.setAttr (i+'.tz', lock=True)
		mc.setAttr (i+'.rx', lock=True)
		mc.setAttr (i+'.ry', lock=True)
		mc.setAttr (i+'.rz', lock=True)
		mc.setAttr (i+'.sx', lock=True)
		mc.setAttr (i+'.sy', lock=True)
		mc.setAttr (i+'.sz', lock=True)
def unlock():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.tx', lock=False)
		mc.setAttr (i+'.ty', lock=False)
		mc.setAttr (i+'.tz', lock=False)
		mc.setAttr (i+'.rx', lock=False)
		mc.setAttr (i+'.ry', lock=False)
		mc.setAttr (i+'.rz', lock=False)
		mc.setAttr (i+'.sx', lock=False)
		mc.setAttr (i+'.sy', lock=False)
		mc.setAttr (i+'.sz', lock=False)
def _face_center_y(f):
	verts = mc.ls(mc.polyListComponentConversion(f, ff=True, tv=True), flatten=True)
	ys = [mc.pointPosition(v, world=True)[1] for v in verts]
	return sum(ys) / len(ys)
def _buildTile(x, z, name, offset_x):
	#one master tile: box -> top-edge grout chamfer -> drop bottom face ->
	#UV from top (planar Y) -> pivot to base.  thickness 0.76cm, grout 0.15.
	cube = mc.polyCube(w=x, h=0.76, d=z, name=name)[0]
	faces = mc.ls(cube + '.f[*]', flatten=True)
	top_face = max(faces, key=_face_center_y)
	top_edges = mc.ls(mc.polyListComponentConversion(top_face, ff=True, te=True), flatten=True)
	mc.polyBevel3(top_edges, offset=0.15, offsetAsFraction=False, segments=1, depth=1, worldSpace=True, autoFit=True, mergeVertices=True, smoothingAngle=30)
	mc.delete(cube, constructionHistory=True)
	faces = mc.ls(cube + '.f[*]', flatten=True)
	mc.delete(min(faces, key=_face_center_y))
	tf = mc.polyListComponentConversion(cube, tf=True)
	mc.polyProjection(tf, type='Planar', md='y')
	#rotate UVs 90deg so the texture matches the tile long/short ratio
	bb2 = mc.polyEvaluate(cube, boundingBox2d=True)
	mc.polyEditUV(mc.polyListComponentConversion(cube, tuv=True), pivotU=(bb2[0][0] + bb2[0][1]) / 2.0, pivotV=(bb2[1][0] + bb2[1][1]) / 2.0, angle=90)
	mc.delete(cube, constructionHistory=True)
	mc.move(offset_x, 0, 0, cube)
	bb = mc.xform(cube, q=True, ws=True, bb=True)
	mc.xform(cube, ws=True, piv=((bb[0] + bb[3]) / 2.0, bb[1], (bb[2] + bb[5]) / 2.0))
	return cube
def buildTiles():
	import re
	presets = {'33 x 66': (66.0, 33.0), '33 x 33': (33.0, 33.0), '15 x 15': (15.0, 15.0)}
	size = mc.confirmDialog(title='Tile size', message='Choose tile dimensions (cm):', button=['33 x 66', '33 x 33', '15 x 15', 'Custom', 'Cancel'], defaultButton='33 x 66', cancelButton='Cancel', dismissString='Cancel')
	if size in (None, 'Cancel', ''):
		return
	if size == 'Custom':
		r = mc.promptDialog(title='Custom size', message='Short x Long in cm (e.g. 20x40):', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
		if r != 'OK':
			return
		nums = re.findall(r'[\d.]+', mc.promptDialog(q=True, text=True))
		if len(nums) < 2:
			mc.warning('weeTools: enter two numbers, e.g. 20x40.')
			return
		short, long_ = float(nums[0]), float(nums[1])
		x, z = long_, short
		token = '%gx%g' % (short, long_)
	else:
		x, z = presets[size]
		token = size.replace(' ', '')
	r = mc.promptDialog(title='Tile count', message='How many tiles do you need?', text='4', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
	if r != 'OK':
		return
	try:
		count = int(float(mc.promptDialog(q=True, text=True)))
	except ValueError:
		mc.warning('weeTools: tile count must be a number.')
		return
	if count < 1:
		mc.warning('weeTools: need at least 1 tile.')
		return
	made = []
	for i in range(count):
		nm = 'tile_%s_%02d_geo' % (token, i + 1)
		made.append(_buildTile(x, z, nm, i * (x + 5.0)))
	mc.select(made)
	print('weeTools: created %d x %scm tile(s).' % (count, token))
def _trimTileScatter(made, area_w, area_l):
	#1 instances->objects | 2 delete history+freeze, group, duplicate, hide first
	#3 combine the second group | 4 box at the area size | 5 intersection boolean
	#(box first, then mesh) | 6 group box+mesh so the live boolean follows.
	if not made:
		return
	# 1) scattered instances -> objects
	mc.select(made)
	mel.eval('ConvertInstanceToObject;')
	# 2) those same tiles: delete history, freeze, group, duplicate, hide first
	tiles = [t for t in made if mc.objExists(t)]
	mc.delete(tiles, constructionHistory=True)
	mc.makeIdentity(tiles, apply=True, translate=True, rotate=True, scale=True)
	grp = mc.group(tiles, name='tiles_grp#')
	dup = mc.duplicate(grp)[0]
	mc.hide(grp)
	# 3) combine the duplicated group
	kids = mc.listRelatives(dup, children=True, fullPath=True)
	combined = mc.polyUnite(kids, constructionHistory=False, name='tiles_combined#')[0]
	# 4) box at the area size, bottom aligned to the tiles' actual bottom level
	tb = mc.xform(combined, q=True, ws=True, bb=True)   # tiles bbox -> tb[1] = bottom
	box = mc.polyCube(w=area_w, h=10.0, d=area_l, name='tile_trim_box#')[0]
	mc.move(area_w / 2.0, tb[1] + 5.0, area_l / 2.0, box, absolute=True)   # center+5 -> bottom on tiles
	bb = mc.xform(box, q=True, ws=True, bb=True)
	mc.xform(box, ws=True, piv=((bb[0] + bb[3]) / 2.0, bb[1], (bb[2] + bb[5]) / 2.0))
	# 5) box first, then the combined mesh; intersection boolean
	mc.select(box)
	mc.select(combined, add=True)
	mel.eval('polyPerformBooleanAction 3 o 0;')
	# 6) group box + mesh so moving the group carries the live boolean result
	keep = [n for n in (box, combined) if mc.objExists(n)]
	if keep:
		mc.select(mc.group(keep, name='tile_trim_grp#'))
def gridTiles():
	#square-tile grid fill: instance the selected tile(s) across an area with
	#random 0/90/180/270 rotation.  asks for the (single) square tile size.
	import random
	sel = mc.ls(selection=True)
	if not sel:
		mc.warning('weeTools: select one or more square tile object(s) first.')
		return
	r = mc.promptDialog(title='Square tile size', message='Tile size in cm (square - one value):', text='15', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
	if r != 'OK':
		return
	try:
		size = float(mc.promptDialog(q=True, text=True))
	except ValueError:
		mc.warning('weeTools: tile size must be a number.')
		return
	if size <= 0:
		mc.warning('weeTools: tile size must be greater than 0.')
		return
	a = mc.promptDialog(title='Total area', message='Total area W x L in cm (e.g. 600x600, one value = square):', text='600x600', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
	if a != 'OK':
		return
	import re
	nums = re.findall(r'[\d.]+', mc.promptDialog(q=True, text=True))
	if not nums:
		mc.warning('weeTools: enter the area size, e.g. 600x600.')
		return
	AREA_W = float(nums[0])
	AREA_H = float(nums[1]) if len(nums) > 1 else AREA_W
	cols = int(AREA_W // size)
	rows = int(AREA_H // size)
	used = set()
	made = []
	for row in range(rows):
		for col in range(cols):
			avail = [t for t in sel if t not in used]
			if not avail:
				used.clear()
				avail = sel
			tile = random.choice(avail)
			used.add(tile)
			inst = mc.instance(tile, name='%s_%d_%d' % (tile, row, col))
			mc.move(col * size, 0, row * size, inst)
			mc.rotate(0, random.choice([0, 90, 180, 270]), 0, inst)
			made += inst
			if len(used) >= len(sel):
				used.clear()
	print('weeTools: generated %dx%d square tile grid at %gcm.' % (cols, rows, size))
	_trimTileScatter(made, AREA_W, AREA_H)
def bondTiles():
	#running-bond fill for rectangular tiles: instance the selected tile(s) in a
	#half-offset brick pattern with random 0/180 rotation and a grout gap.
	#asks for the tile size (short x long) and the total area.
	import random, math, re
	sel = mc.ls(selection=True)
	if not sel:
		mc.warning('weeTools: select one or more rectangular tile object(s) first.')
		return
	t = mc.promptDialog(title='Tile size', message='Tile short x long in cm (e.g. 33x66):', text='33x66', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
	if t != 'OK':
		return
	tn = re.findall(r'[\d.]+', mc.promptDialog(q=True, text=True))
	if len(tn) < 2:
		mc.warning('weeTools: enter two numbers, e.g. 33x66.')
		return
	tile_z, tile_x = float(tn[0]), float(tn[1])   # short -> Z, long -> X
	a = mc.promptDialog(title='Total area', message='Total area W x L in cm (e.g. 600x600, one value = square):', text='600x600', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
	if a != 'OK':
		return
	an = re.findall(r'[\d.]+', mc.promptDialog(q=True, text=True))
	if not an:
		mc.warning('weeTools: enter the area size, e.g. 600x600.')
		return
	area_w = float(an[0])
	area_l = float(an[1]) if len(an) > 1 else area_w
	step_x = tile_x
	step_z = tile_z
	cols = int(math.ceil(area_w / step_x)) + 1
	rows = int(math.ceil(area_l / step_z))
	used = set()
	made = []
	for row in range(rows):
		x_off = (step_x / 2.0) if (row % 2) else 0.0
		for col in range(cols):
			avail = [o for o in sel if o not in used]
			if not avail:
				used.clear()
				avail = sel
			tile = random.choice(avail)
			used.add(tile)
			inst = mc.instance(tile, name='%s_r%d_c%d' % (tile, row, col))
			mc.move(col * step_x - x_off, 0, row * step_z, inst)
			mc.rotate(0, random.choice([0, 180]), 0, inst)
			made += inst
			if len(used) >= len(sel):
				used.clear()
	print('weeTools: generated %dx%d running-bond grid (tile %gx%g).' % (cols, rows, tile_z, tile_x))
	_trimTileScatter(made, area_w, area_l)
def tess2():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.rsEnableSubdivision', 1)
		mc.setAttr (i+'.rsMaxTessellationSubdivs', 2)
		mc.setAttr (i+'.rsMinTessellationLength', 2)
def tess3():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.rsEnableSubdivision', 1)
		mc.setAttr (i+'.rsMaxTessellationSubdivs', 3)
		mc.setAttr (i+'.rsMinTessellationLength', 2)
def untess():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.rsEnableSubdivision', 0)
		mc.setAttr (i+'.rsMaxTessellationSubdivs', 0)
		mc.setAttr (i+'.rsMinTessellationLength', 4)
def disp():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.rsEnableDisplacement', 1)
def undisp():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.rsEnableDisplacement', 0)
def backface():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.select (sel[i], r=True)
		query=mc.displayCull(q=True)
		if query == True:
			mc.displayCull( bfc=False )
		else:
			mc.displayCull( bfc=True )
		mc.select(sel)
def matphong():
	#Create Material and assign on selected objects with their names on material
	import random as random
	from random import uniform as rand
	rand1 = rand(0.0,1.0)
	rand2 = rand(0.01,0.99)
	ranD4 = rand(0.02,0.98)
	draw_list = [0.35, 0.30, 0.25, 0.20, 0.15, -0.35, -0.30, -0.25, -0.20, -0.15,]
	randlist = random.choice(draw_list)
	sel_geo = mc.ls(selection=True)
	nam1 = sel_geo[0].replace('_geo', '')
	nam2 = nam1.replace('|', '')
	mc.shadingNode ('phong', asShader=True, n=nam2 + '_#')
	sel_s = mc.ls(selection=True)
	mc.rename (sel_s[0], sel_s[0] + '_S')
	sel_inp = mc.ls(selection=True)
	inputs = sel_inp[0]
	mc.setAttr(inputs + '.color', rand1+randlist, rand2+randlist, ranD4+randlist)
	mc.setAttr(inputs + '.transparency', 0,0,0)
	mc.setAttr(inputs + '.diffuse', 1)
	mc.setAttr(inputs + '.specularColor', 0, 0, 0)
	mc.setAttr(inputs + '.reflectivity', 0)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=inputs + 'G')
	mc.connectAttr(inputs + '.outColor', inputs + 'G.surfaceShader')
	mc.sets(sel_geo, edit=True, forceElement=inputs + 'G')
	mc.select (sel_geo[0])
def _pbrMat(metal, detail, colorlayer=False, noise_type=None, noise_scale=None):
	#metal True=metallic / False=dielectric(IOR 1.5). detail='bump' or 'displace' (noise-driven). One shared material for the whole selection.
	#colorlayer=True also builds a Maxon-noise + AO + Curvature network through a RedshiftColorLayer into base_color (layers 1 & 2 enabled).
	import random
	import colorsys
	sel_geo = mc.ls(selection=True)
	if not sel_geo:
		mc.warning('weeTools: select object(s) first.')
		return
	name = sel_geo[0].split('|')[-1].replace('_geo', '')
	r, g, b = colorsys.hsv_to_rgb(random.random(), random.uniform(0.35, 0.85), random.uniform(0.25, 0.85))
	mat = mc.shadingNode('RedshiftStandardMaterial', asShader=True, name=name + '_S')
	mc.setAttr(mat + '.base_color', r, g, b, type='double3')
	mc.setAttr(mat + '.refl_weight', 1)
	mc.setAttr(mat + '.refl_roughness', 0)
	if metal:
		mc.setAttr(mat + '.metalness', 1)
	else:
		try:
			mc.setAttr(mat + '.refl_ior', 1.5)
		except:
			pass
	sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=name + '_SG')
	mc.connectAttr(mat + '.outColor', sg + '.surfaceShader', force=True)
	mc.sets(sel_geo, edit=True, forceElement=sg)
	noise = mc.shadingNode('RedshiftMaxonNoise', asTexture=True, name=name + '_rsMaxon')
	if noise_type is not None:
		try:
			mc.setAttr(noise + '.noise_type', noise_type)
		except:
			pass
	if noise_scale is not None:
		try:
			mc.setAttr(noise + '.coord_scale_global', noise_scale)
		except:
			pass
	if detail == 'bump':
		bump = mc.shadingNode('RedshiftBumpMap', asShader=True, name=name + '_rsBump')
		mc.connectAttr(noise + '.outColor', bump + '.input', force=True)
		try:
			mc.setAttr(bump + '.factorInObjScale', 0)
		except:
			pass
		try:
			mc.setAttr(bump + '.scale', 0.2)
		except:
			pass
		mc.connectAttr(bump + '.out', mat + '.bump_input', force=True)
	else:
		disp = mc.shadingNode('RedshiftDisplacement', asShader=True, name=name + '_rsDispl')
		mc.connectAttr(noise + '.outColor', disp + '.texMap', force=True)
		try:
			mc.setAttr(disp + '.scale', 0.5)
		except:
			pass
		mc.connectAttr(disp + '.out', sg + '.displacementShader', force=True)
		shapes = mc.listRelatives(sel_geo, shapes=True, fullPath=True) or []
		for shp in shapes:
			for a, v in [('.rsEnableSubdivision', 1), ('.rsMaxTessellationSubdivs', 2), ('.rsEnableDisplacement', 1)]:
				try:
					mc.setAttr(shp + a, v)
				except:
					pass
	if colorlayer:
		#Flat random base colour on the Color Layer; AO -> layer-1 mask, Curvature -> layer-2 mask (its output max driven by Maxon noise). Color Layer -> material base_color.
		clr = mc.shadingNode('RedshiftColorLayer', asTexture=True, name=name + '_rsClrLyr')
		try:
			mc.setAttr(clr + '.base_color', r, g, b, type='double3')
		except:
			pass
		mc.connectAttr(clr + '.outColor', mat + '.base_color', force=True)
		#Layer 1 = Ambient Occlusion (inverted: white<->black) feeding the layer mask
		ao = mc.shadingNode('RedshiftAmbientOcclusion', asTexture=True, name=name + '_rsAO')
		try:
			mc.setAttr(ao + '.bright', 0, 0, 0, type='double3')
		except:
			pass
		try:
			mc.setAttr(ao + '.dark', 1, 1, 1, type='double3')
		except:
			pass
		try:
			mc.setAttr(ao + '.maxDistance', 50)
		except:
			pass
		try:
			mc.setAttr(ao + '.spread', 0.4)
		except:
			pass
		try:
			mc.setAttr(clr + '.layer1_enable', 1)
		except:
			pass
		try:
			mc.connectAttr(ao + '.outColorR', clr + '.layer1_mask', force=True)
		except:
			pass
		#Layer 2 = Curvature (output max modulated by Maxon noise) feeding the layer mask
		cnoise = mc.shadingNode('RedshiftMaxonNoise', asTexture=True, name=name + '_rsMaxonClr')
		curv = mc.shadingNode('RedshiftCurvature', asTexture=True, name=name + '_rsCurv')
		for _cattr in ['.outputMax', '.output_max']:
			try:
				mc.connectAttr(cnoise + '.outColorR', curv + _cattr, force=True)
				break
			except:
				pass
		try:
			mc.setAttr(clr + '.layer2_enable', 1)
		except:
			pass
		try:
			mc.connectAttr(curv + '.out', clr + '.layer2_mask', force=True)
		except:
			pass
	mc.select(sel_geo)
def pbrBD(): _pbrMat(False, 'bump', colorlayer=True)
def pbrTile(): _pbrMat(False, 'bump', colorlayer=True, noise_type=10, noise_scale=0.93)  # 10 = Luka

def mat1():
	import random as random
	from random import uniform as rand
	rand1 = rand(0.0,1.0)
	rand2 = rand(0.01,0.99)
	ranD4 = rand(0.02,0.98)
	draw_list = [0.35, 0.30, 0.25, 0.20, 0.15, -0.35, -0.30, -0.25, -0.20, -0.15,]
	randlist = random.choice(draw_list)
	sel_geo = mc.ls(selection=True)
	nam1 = sel_geo[0].replace('_geo', '')
	nam2 = nam1.replace('|', '')
	mc.shadingNode ('RedshiftStandardMaterial', asShader=True, n=nam2 + '_#')
	sel_s = mc.ls(selection=True)
	mc.rename (sel_s[0], sel_s[0] + '_S')
	sel_inp = mc.ls(selection=True)
	inputs = sel_inp[0]
	mc.setAttr(inputs + '.base_color', rand1+randlist, rand2+randlist, ranD4+randlist)
	mc.setAttr(inputs + '.refl_weight', 0)
	mc.setAttr(inputs + '.refl_roughness', 0)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=inputs + 'G')
	mc.connectAttr(inputs + '.outColor', inputs + 'G.surfaceShader')
	mc.sets(sel_geo, edit=True, forceElement=inputs + 'G')

	mc.shadingNode ('RedshiftFresnel', asUtility=True, n=inputs + '_fresnel')
	sel_fres = mc.ls(selection=True)
	mc.setAttr (sel_fres[0] + '.correct_intensity', 0)

	mc.shadingNode ('floatMath', asUtility=True, n=inputs + 'floatMath')
	sel_math1 = mc.ls(selection=True)
	mc.setAttr(sel_math1[0] + '.floatA', 1)
	mc.setAttr(sel_math1[0] + '.operation', 1)

	mc.shadingNode ('floatMath', asUtility=True, n=inputs + 'floatMath')
	sel_math2 = mc.ls(selection=True)
	mc.setAttr(sel_math2[0] + '.floatA', 1)
	mc.setAttr(sel_math2[0] + '.operation', 1)
	mc.connectAttr(sel_math2[0] + '.outFloat', sel_fres[0] + '.perp_colorR')
	mc.connectAttr(sel_math2[0] + '.outFloat', sel_fres[0] + '.perp_colorG')
	mc.connectAttr(sel_math2[0] + '.outFloat', sel_fres[0] + '.perp_colorB')
	mc.connectAttr(inputs + '.refl_roughness', sel_math2[0] + '.floatB')

	mc.shadingNode ('floatMath', asUtility=True, n=inputs + 'floatMath')
	sel_math3 = mc.ls(selection=True)
	mc.connectAttr(inputs + '.refl_weight', sel_math3[0] + '.floatA')
	mc.connectAttr(sel_fres[0] + '.outColorR', sel_math3[0] + '.floatB')
	mc.connectAttr(sel_math3[0] + '.outFloat', inputs + '.refl_weight')

	mc.connectAttr(sel_math3[0] + '.outFloat', sel_math1[0] + '.floatB')
	mc.connectAttr(sel_math1[0] + '.outFloat', inputs + '.diffuse_weight')

	mc.connectAttr(inputs + '.refl_roughness', inputs + '.diffuse_roughness')

	rsbump = mc.shadingNode ('RedshiftBumpMap', asShader=True, n=sel_geo[0] + '_rsBump')
	diffuse = mc.shadingNode ('file', asTexture=True, name=sel_geo[0]+'_diffuse')
	roughness = mc.shadingNode ('file', asTexture=True, name=sel_geo[0]+'_roughness')
	bump = mc.shadingNode ('file', asTexture=True, name=sel_geo[0]+'_bump')
	#transmittance = mc.shadingNode ('file', asTexture=True, name=sel_geo[0]+'_transmittance')
	#displacement = mc.shadingNode ('file', asTexture=True, name=sel_geo[0]+'_displacement')
	texture = mc.shadingNode ('place2dTexture', asUtility=True, name=sel_geo[0]+'_place2dTexture')

	mc.select(clear=True)
	mc.select(texture, add=True)
	mc.select(diffuse, add=True)
	mc.select(roughness, add=True)
	mc.select(bump, add=True)
	#mc.select(displacement, add=True)
	#mc.select(transmittance, add=True)
	#-----------------------------------------------------------
	selnode = mc.ls(selection=True)
	#if selnode[0] type='place2dTexture'
	for x in range(len(selnode)):
		try:
			mc.connectAttr(selnode[0] +'.outUV', selnode[x+1] + '.uvCoord')
			mc.connectAttr(selnode[0] +'.outUvFilterSize', selnode[x+1] + '.uvFilterSize')
			mc.connectAttr(selnode[0] +'.coverage', selnode[x+1] + '.coverage')
			mc.connectAttr(selnode[0] +'.mirrorU', selnode[x+1] + '.mirrorU')
			mc.connectAttr(selnode[0] +'.mirrorV', selnode[x+1] + '.mirrorV')
			mc.connectAttr(selnode[0] +'.noiseUV', selnode[x+1] + '.noiseUV')
			mc.connectAttr(selnode[0] +'.offset', selnode[x+1] + '.offset')
			mc.connectAttr(selnode[0] +'.repeatUV', selnode[x+1] + '.repeatUV')
			mc.connectAttr(selnode[0] +'.rotateFrame', selnode[x+1] + '.rotateFrame')
			mc.connectAttr(selnode[0] +'.rotateUV', selnode[x+1] + '.rotateUV')
			mc.connectAttr(selnode[0] +'.stagger', selnode[x+1] + '.stagger')
			mc.connectAttr(selnode[0] +'.translateFrame', selnode[x+1] + '.translateFrame')
			mc.connectAttr(selnode[0] +'.vertexCameraOne', selnode[x+1] + '.vertexCameraOne')
			mc.connectAttr(selnode[0] +'.vertexUvOne', selnode[x+1] + '.vertexUvOne')
			mc.connectAttr(selnode[0] +'.vertexUvThree', selnode[x+1] + '.vertexUvThree')
			mc.connectAttr(selnode[0] +'.vertexUvTwo', selnode[x+1] + '.vertexUvTwo')
			mc.connectAttr(selnode[0] +'.wrapU', selnode[x+1] + '.wrapU')
			mc.connectAttr(selnode[0] +'.wrapV', selnode[x+1] + '.wrapV')
		except:
			pass
	#------------------------------------------------------------
	mc.connectAttr (bump+'.outColor', rsbump+'.input.')
	mc.connectAttr (rsbump+'.out', inputs+'.bump_input')
	mc.setAttr(rsbump+'.factorInObjScale', 0)
	mc.setAttr(rsbump+'.scale', 0.1)
	mc.connectAttr (roughness+'.outColor.outColorG', inputs+'.refl_roughness')
	mc.connectAttr (diffuse+'.outColor', inputs+'.base_color')

	#mc.connectAttr (transmittance +'.outColor', inputs+'.refr_transmittance')
	#mc.setAttr(inputs + '.ss_amount', 1)

	mc.setAttr (nam2+'.rsEnableDisplacement', 1)
	mc.setAttr (nam2+'.rsEnableSubdivision', 1)
	mc.setAttr (nam2+'.rsMaxTessellationSubdivs', 2)
	mc.setAttr (nam2+'.rsMinTessellationLength', 2)

	#mc.shadingNode ('RedshiftDisplacement', asShader=True, n=inputs + '_displ')
	#mc.connectAttr (inputs+'_displ.out', inputs+'G.displacementShader')
	#mc.connectAttr (displacement +'.outColor', inputs+'_displ.texMap')

	mc.select (sel_geo[0])
def pbrBM(): _pbrMat(True, 'bump')
def pbrDD(): _pbrMat(False, 'displace')
def pbrDM(): _pbrMat(True, 'displace')

def texcon():
	selnode = mc.ls(selection=True)
	#if selnode[0] type='place2dTexture'
	for x in range(len(selnode)):
		mc.connectAttr(selnode[0] +'.outUV', selnode[x+1] + '.uvCoord')
		mc.connectAttr(selnode[0] +'.outUvFilterSize', selnode[x+1] + '.uvFilterSize')
		mc.connectAttr(selnode[0] +'.coverage', selnode[x+1] + '.coverage')
		mc.connectAttr(selnode[0] +'.mirrorU', selnode[x+1] + '.mirrorU')
		mc.connectAttr(selnode[0] +'.mirrorV', selnode[x+1] + '.mirrorV')
		mc.connectAttr(selnode[0] +'.noiseUV', selnode[x+1] + '.noiseUV')
		mc.connectAttr(selnode[0] +'.offset', selnode[x+1] + '.offset')
		mc.connectAttr(selnode[0] +'.repeatUV', selnode[x+1] + '.repeatUV')
		mc.connectAttr(selnode[0] +'.rotateFrame', selnode[x+1] + '.rotateFrame')
		mc.connectAttr(selnode[0] +'.rotateUV', selnode[x+1] + '.rotateUV')
		mc.connectAttr(selnode[0] +'.stagger', selnode[x+1] + '.stagger')
		mc.connectAttr(selnode[0] +'.translateFrame', selnode[x+1] + '.translateFrame')
		mc.connectAttr(selnode[0] +'.vertexCameraOne', selnode[x+1] + '.vertexCameraOne')
		mc.connectAttr(selnode[0] +'.vertexUvOne', selnode[x+1] + '.vertexUvOne')
		mc.connectAttr(selnode[0] +'.vertexUvThree', selnode[x+1] + '.vertexUvThree')
		mc.connectAttr(selnode[0] +'.vertexUvTwo', selnode[x+1] + '.vertexUvTwo')
		mc.connectAttr(selnode[0] +'.wrapU', selnode[x+1] + '.wrapU')
		mc.connectAttr(selnode[0] +'.wrapV', selnode[x+1] + '.wrapV')
def replaceTextures():
	#1) count the selected texture (file) nodes
	sel = mc.ls(selection=True) or []
	fileNodes = [n for n in sel if mc.nodeType(n) == 'file']
	if not fileNodes:
		mc.warning('weeTools: select one or more file (texture) nodes first.')
		return
	#2) open a window to pick that many replacement textures from a folder
	picked = mc.fileDialog2(
		fileMode=4,  # one or more existing files
		caption='Select %d replacement texture(s)' % len(fileNodes),
		okCaption='Replace',
		fileFilter='Images (*.jpg *.jpeg *.png *.tif *.tiff *.exr *.tga *.tx *.bmp);;All Files (*.*)')
	if not picked:
		return
	if len(picked) != len(fileNodes):
		mc.warning('weeTools: %d node(s) selected but %d file(s) picked - replacing %d (paired in order).'
			% (len(fileNodes), len(picked), min(len(fileNodes), len(picked))))
	#3) replace each selected file node's texture, paired in order
	count = 0
	for node, path in zip(fileNodes, picked):
		try:
			mc.setAttr(node + '.fileTextureName', path, type='string')
			count += 1
		except Exception as e:
			mc.warning('weeTools: could not set %s -> %s (%s)' % (node, path, e))
	mc.select(fileNodes)
	print('weeTools: replaced %d texture(s).' % count)
def unprimvis():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.primaryVisibility', 0)
def primvis():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.primaryVisibility', 1)

def setsrgb():
	sel_txt = mc.ls(selection=True, type='file')
	for i in range(len(sel_txt)):
		mc.setAttr(sel_txt[i] + '.ignoreColorSpaceFileRules', 1)
		mc.setAttr(sel_txt[i] + '.cs', 'Utility - sRGB - Texture', type='string')
def setlin():
	sel_txt = mc.ls(selection=True, type='file')
	for i in range(len(sel_txt)):
		mc.setAttr(sel_txt[i] + '.ignoreColorSpaceFileRules', 1)
		mc.setAttr(sel_txt[i] + '.cs', 'Utility - Linear - sRGB', type='string')
def group():
	sel = mc.ls(selection=True)
	mc.group (sel, name=sel[0] + '_grp')
	sel = mc.ls(selection=True)
	temp = sel[0].replace('_geo', '')
	mc.rename (sel[0], temp)
	temp2 = sel[0].replace('_1', '')
	mc.rename (sel[0], temp2)

def autoUV():
	sel = mc.ls(sl = True, fl = True, dag = True, type= 'mesh')
	for i in range(len(sel)):
		mc.select (sel[i])
		mc.DeleteHistory()
		mc.polyAutoProjection(lm= 0, pb= 0, ibd= 1, sc= 1, o= 1, p= 3, ps= 0.1, ws= 0)
		mc.polyEditUV(pu= 0.5, pv= 0.5, su= 0.99, sv= 0.99, u= -0.0, v= 0.0)
		mc.select (sel[i])
		mc.DeleteHistory()
def zero():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.move (0, i, xyz=True, absolute=True, spr=True)
def changeName():
	sel = mc.ls(selection=True)
	input = mc.textField(field2, text = True, query = True)
	for i in range(len(sel)):
		mc.rename (sel[i], input + '_' + str (i + 1))
def shaderName():
	input = mc.textField(field2, text=True, query=True)
	types = [
		('shadingEngine', '_sg', False),
		('RedshiftStandardMaterial', '_s', False),
		('RedshiftStandardMaterialBlender', '_rsMatBlend', True),
		('RedshiftDisplacement', '_rsDispl', True),
		('RedshiftDisplacementBlender', '_rsDisplBlend', True),
		('RedshiftBumpMap', '_rsBump', True),
		('RedshiftBumpBlender', '_rsBumpBlend', True),
		('RedshiftFresnel', '_fresnel', True),
		('RedshiftColorLayer', '_rsClrLyr', True),
		('RedshiftColorCorrection', '_rsCC', True),
		('cloth', '_cloth', True),
		('place2dTexture', '_place2dTexture', True),
		('RedshiftAmbientOcclusion', '_rsAO', True),
		('RedshiftCurvature', '_rsCurv', True),
		('RedshiftTriPlanar', '_rsTripl', True),
		('file', '_file', True),
		('RedshiftNoise', '_rsNoi', True),
		('remapHsv', '_rmphsv', True),
		('ramp', '_ramp', True),
		('fractal', '_fractal', True),
		('noise', '_noi', True),
		('layeredTexture', '_layTex', True),
		('checker', '_checker', True),
		('blendColors', '_blClr', True),
		('reverse', '_rvrs', True),
		('remapColor', '_rmpclr', True),
		('floatConstant', '_fltConst', True),
		('RedshiftRaySwitch', '_rsRaySwt', True),
		('RedshiftSprite', '_rsSprite', True),
		('substanceNode', '_substance', True),
		('substanceOutputNode', '_substanceOutput', True),
		('multiplyDivide', '_multiplyDivide', True),
		('projection', '_projection', True),
		('RedshiftRoundCorners', '_rsRoundCrnr', True),
		('lambert', '_lambert_S', False),
		('phong', '_PH_S', False),
		('samplerInfo', '_SInfo', True),
		('floatMath', '_floatMath', True),
		('RedshiftIncandescent', '_rsIncd', True),
		('RedshiftMaxonNoise', '_rsMaxon', True),
	]
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		for ntype, suffix, numbered in types:
			selnode = mc.ls(selection=True, type=ntype)
			for y in range(len(selnode)):
				if numbered:
					mc.rename(selnode[y], input + '_' + str(y + 1) + suffix)
				else:
					mc.rename(selnode[y], input + suffix)
def prefix():
	input = mc.textField(field2, text = True, query = True)
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], input + sel[i])
def sufix():
	input = mc.textField(field2, text = True, query = True)
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i] + input)
def search():
	search = mc.textField(field1, text = True, query = True)
	input = mc.textField(field2, text = True, query = True)
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		temp = sel[i].replace(search, input)
		mc.rename (sel[i], temp)
def _addSuffix(suffix):
	for obj in mc.ls(selection=True):
		mc.rename(obj, obj.split('|', 1)[-1] + suffix)
def addgeo(): _addSuffix('_geo')
def addgrp(): _addSuffix('_grp')
def addlow(): _addSuffix('_low')
def addhigh(): _addSuffix('_high')
def addlgt(): _addSuffix('_lgt')
def addoff(): _addSuffix('_off')
def adddiff(): _addSuffix('_diff')
def addemis(): _addSuffix('_emis')
def addrefl(): _addSuffix('_refl')
def addrefr(): _addSuffix('_refr')
def addopa(): _addSuffix('_opa')
def addloc(): _addSuffix('_loc')
def addcolor(): _addSuffix('Color')
def addwght(): _addSuffix('Wght')
def addrghn(): _addSuffix('Rghn')
def addcoat(): _addSuffix('Coat')
def addsdk(): _addSuffix('_sdk')
def addS(): _addSuffix('_S')
def addSG(): _addSuffix('_SG')
def addL(): _addSuffix('_L')
def addR(): _addSuffix('_R')
def addtop(): _addSuffix('_top')
def addmid(): _addSuffix('_mid')
def addbot(): _addSuffix('_bot')
def addA(): _addSuffix('_A')
def addB(): _addSuffix('_B')
def addC(): _addSuffix('_C')
def addD(): _addSuffix('_D')
def addE(): _addSuffix('_E')
def addF(): _addSuffix('_F')
def addG(): _addSuffix('_G')
def addH(): _addSuffix('_H')
def redshift():
	mc.loadPlugin( 'redshift4maya.mll')
	mc.setAttr("defaultRenderGlobals.currentRenderer", "redshift", type="string")
def fnrender():
	width =float(1440)
	height = float(2560)
	deviceAspect = width / height
	mc.setAttr('defaultResolution.height', height)
	mc.setAttr('defaultResolution.width', width)
	mc.setAttr('defaultResolution.pixelAspect', 1)
	mc.setAttr('defaultResolution.deviceAspectRatio',deviceAspect)
	rpath = '<scene>/beauty'
	mc.setAttr('defaultRenderGlobals.imageFilePrefix', rpath, type='string')
	mc.setAttr("defaultRenderGlobals.animation", 1)
	mc.setAttr("redshiftOptions.imageFormat", 1)
	mc.setAttr('redshiftOptions.unifiedMinSamples', 8)
	mc.setAttr('redshiftOptions.unifiedMaxSamples', 1024)
	mc.setAttr('redshiftOptions.unifiedAdaptiveErrorThreshold', 0.02)
	mc.setAttr('redshiftOptions.primaryGIEngine', 4)
	mc.setAttr("redshiftOptions.secondaryGIEngine", 2)
	mc.setAttr("redshiftOptions.numGIBounces", 3)
	mc.setAttr('redshiftOptions.bruteForceGINumRays', 256)
	mc.setAttr('redshiftOptions.denoiseEngine', 3)
	minTime = mc.playbackOptions(q=True, minTime=True)
	maxTime = mc.playbackOptions(q=True, maxTime=True)
	mc.setAttr('defaultRenderGlobals.startFrame', minTime)
	mc.setAttr('defaultRenderGlobals.endFrame', maxTime)
	mc.setAttr('defaultRenderGlobals.byFrameStep', 1)

def prerender():
	width =float(540)
	height = float(540)
	deviceAspect = width / height
	mc.setAttr('defaultResolution.height', height)
	mc.setAttr('defaultResolution.width', width)
	mc.setAttr('defaultResolution.pixelAspect', 1)
	mc.setAttr('defaultResolution.deviceAspectRatio',deviceAspect)
	rpath = '<scene>/Previsual/prev'
	mc.setAttr('defaultRenderGlobals.imageFilePrefix', rpath, type='string')
	mc.setAttr("defaultRenderGlobals.animation", 1)
	mc.setAttr("redshiftOptions.imageFormat", 2)
	mc.setAttr('redshiftOptions.unifiedMinSamples', 4)
	mc.setAttr('redshiftOptions.unifiedMaxSamples', 1024)
	mc.setAttr('redshiftOptions.unifiedAdaptiveErrorThreshold', 3)
	mc.setAttr('redshiftOptions.primaryGIEngine', 0)
	mc.setAttr("redshiftOptions.secondaryGIEngine", 0)
	mc.setAttr("redshiftOptions.numGIBounces", 0)
	mc.setAttr('redshiftOptions.bruteForceGINumRays', 0)
	mc.setAttr('redshiftOptions.denoiseEngine', 0)

def domelgt(): ##################################### Dome light creation
	mel.eval('redshiftCreateDomeLight;')
	list=mc.ls(selection=True)
	mc.rename (list[0], 'domelgt_#')
	list2=mc.ls(selection=True)
	mc.setAttr(list2[0]+'.scaleX', 30)
	mc.setAttr(list2[0]+'.scaleY', 30)
	mc.setAttr(list2[0]+'.scaleZ', 30)
	mc.setAttr(list2[0]+'.volumeRayContributionScale', 0)
	mc.setAttr(list2[0]+'.volumeNumSamples', 64)
	mc.setAttr(list2[0]+'.background_enable', 0)
	hdrDir = 'C:/Users/erbay/Documents/archiveFiles/hdr'
	picked = mc.fileDialog2(fileMode=1, dialogStyle=2, caption='Select HDR for Dome Light', startingDirectory=hdrDir)
	if picked:
		mc.setAttr(list2[0]+'.tex0', picked[0], type='string')
def arealgt(): ##################################### Area light creation
	mel.eval('redshiftCreateLight "RedshiftPhysicalLight";')
	list=mc.ls(selection=True)
	mc.rename (list[0], 'arealgt_#')
	list2=mc.ls(selection=True)
	mc.setAttr(list2[0]+'.lightType', 0)
	mc.setAttr(list2[0]+'.scaleX', 10)
	mc.setAttr(list2[0]+'.scaleY', 10)
	mc.setAttr(list2[0]+'.scaleZ', 10)
	mc.setAttr(list2[0]+'.rotateX', -90)
	mc.setAttr(list2[0]+'.intensity', 10)
	mc.setAttr(list2[0]+'.volumeRayContributionScale', 0.01)
	mc.setAttr(list2[0]+'.volumeNumSamples', 256)
	mc.setAttr(list2[0]+'.areaVisibleInRender', 0)
	mc.setAttr(list2[0]+'.colorMode', 1)
	mc.setAttr(list2[0]+'.temperature', 4500)
	mc.setAttr(list2[0]+'.unitsType', 3)
	mc.setAttr(list2[0]+'.lumensperwatt', 11)
	mc.setAttr(list2[0]+'.intensity', 1)
	mc.setAttr(list2[0]+'.exposure', 12)
def pointlgt(): ##################################### Point light creation
	mel.eval('redshiftCreateLight "RedshiftPhysicalLight";')
	list=mc.ls(selection=True)
	mc.rename (list[0], 'pointlgt_#')
	list2=mc.ls(selection=True)
	mc.setAttr(list2[0]+'.scaleX', 5)
	mc.setAttr(list2[0]+'.scaleY', 5)
	mc.setAttr(list2[0]+'.scaleZ', 5)
	mc.setAttr(list2[0]+'.lightType', 1)
	mc.setAttr(list2[0]+'.volumeRayContributionScale', 0.01)
	mc.setAttr(list2[0]+'.volumeNumSamples', 256)
	mc.setAttr(list2[0]+'.colorMode', 1)
	mc.setAttr(list2[0]+'.temperature', 4500)
	mc.setAttr(list2[0]+'.unitsType', 3)
	mc.setAttr(list2[0]+'.lumensperwatt', 11)
	mc.setAttr(list2[0]+'.intensity', 1)
	mc.setAttr(list2[0]+'.exposure', 12)
def spotlgt(): ##################################### Spot light creation
	mel.eval('redshiftCreateLight "RedshiftPhysicalLight";')
	list=mc.ls(selection=True)
	mc.rename (list[0], 'spotlgt_#')
	list2=mc.ls(selection=True)
	mc.setAttr(list2[0]+'.lightType', 2)
	mc.setAttr(list2[0]+'.scaleX', 5)
	mc.setAttr(list2[0]+'.scaleY', 5)
	mc.setAttr(list2[0]+'.scaleZ', 5)
	mc.setAttr(list2[0]+'.rotateX', -90)
	mc.setAttr(list2[0]+'.volumeRayContributionScale', 0.01)
	mc.setAttr(list2[0]+'.volumeNumSamples', 256)
	mc.setAttr(list2[0]+'.areaVisibleInRender', 0)
	mc.setAttr(list2[0]+'.colorMode', 1)
	mc.setAttr(list2[0]+'.temperature', 4500)
	mc.setAttr(list2[0]+'.unitsType', 3)
	mc.setAttr(list2[0]+'.lumensperwatt', 11)
	mc.setAttr(list2[0]+'.intensity', 1)
	mc.setAttr(list2[0]+'.exposure', 12)
def directlgt(): ##################################### Direct light creation
	mel.eval('redshiftCreateLight "RedshiftPhysicalLight";')
	list=mc.ls(selection=True)
	mc.rename (list[0], 'direct_#')
	list2=mc.ls(selection=True)
	mc.setAttr(list2[0]+'.lightType', 3)
	mc.setAttr(list2[0]+'.scaleX', 50)
	mc.setAttr(list2[0]+'.scaleY', 50)
	mc.setAttr(list2[0]+'.scaleZ', 50)
	mc.setAttr(list2[0]+'.rotateX', -90)
	mc.setAttr(list2[0]+'.volumeRayContributionScale', 0.00)
	mc.setAttr(list2[0]+'.volumeNumSamples', 256)
	mc.setAttr(list2[0]+'.areaVisibleInRender', 0)
	mc.setAttr(list2[0]+'.intensity', 1)
	mc.setAttr(list2[0]+'.colorMode', 1)
	mc.setAttr(list2[0]+'.temperature', 4500)
	mc.setAttr(list2[0]+'.unitsType', 3)
	mc.setAttr(list2[0]+'.lumensperwatt', 11)
	mc.setAttr(list2[0]+'.intensity', 0.5)
def meshlgt():
	listtransform=mc.ls(selection=True)
	listmesh=mc.ls(type='mesh')
	mel.eval('redshiftCreateLight "RedshiftPhysicalLight";')
	list=mc.ls(selection=True)
#	mc.rename (list[0], listtransform[0]+'_lgt_#')
#	list=mc.ls(selection=True)
	mc.setAttr(list[0]+'.areaShape', 4)
	mc.setAttr(list[0]+'.areaVisibleInRender', 1)
	mc.setAttr(list[0]+'.volumeRayContributionScale', 0.01)
	mc.setAttr(list[0]+'.volumeRayContributionScale', 0.01)
	mc.setAttr(list[0]+'.volumeNumSamples', 256)
	mc.setAttr(list[0]+'.unitsType', 3)
	mc.setAttr(list[0]+'.lumensperwatt', 11)
	mc.setAttr(list[0]+'.intensity', 1)
	mc.setAttr(list[0]+'.exposure', 12)
	mc.select(listmesh[0])
	mc.select(list[0], add=True)
	mc.connectAttr(listtransform[0]+'|'+listmesh[0]+'.message', list[0]+'.areaShapeObject')
	mc.setAttr (listtransform[0]+'.overrideEnabled', 1)
	mc.setAttr (listtransform[0]+'.overrideLevelOfDetail', 1)
	mc.setAttr (listtransform[0]+'.primaryVisibility', 0)
	mc.setAttr (listtransform[0]+'.visibleInReflections', 0)
	mc.setAttr (listtransform[0]+'.visibleInRefractions', 0)
	mc.parent (list[0], listtransform[0])
	mc.select(listtransform[0])
def _setRes(w, h):
	w = float(w)
	h = float(h)
	mc.setAttr('defaultResolution.height', h)
	mc.setAttr('defaultResolution.width', w)
	mc.setAttr('defaultResolution.pixelAspect', 1)
	mc.setAttr('defaultResolution.deviceAspectRatio', w / h)
def x1080x1920(): _setRes(1920, 1080)
def x720x1280(): _setRes(1280, 720)
def x1440x2560(): _setRes(2560, 1440)
def x1080x1080(): _setRes(1080, 1080)
def x1920x1080(): _setRes(1080, 1920)
def x2148x3840(): _setRes(3840, 2160)
def x2560x1440(): _setRes(1440, 2560)
def x3840x2160(): _setRes(2160, 3840)
def _togglePanels(flag):
	for i in range(1, 9):
		p = 'modelPanel' + str(i)
		try:
			cur = mc.modelEditor(p, query=True, **{flag: 1})
			mc.modelEditor(p, edit=True, **{flag: 0 if cur else 1})
		except:
			print(p + ' not found')
def showjoint(): _togglePanels('joints')
def showpoly(): _togglePanels('polymeshes')
def showcurve(): _togglePanels('nurbsCurves')
def showlight(): _togglePanels('lights')
def showcam(): _togglePanels('cameras')
def showallobjects():
	for i in range(1, 9):
		try:
			queryp = mc.modelEditor('modelPanel'+str(i), query=True, polymeshes=1)
			queryj = mc.modelEditor('modelPanel'+str(i), query=True, joints=1)
			queryc = mc.modelEditor('modelPanel'+str(i), query=True, nurbsCurves=1)
			if queryp==True or queryj==True or queryc==True:
				mc.modelEditor('modelPanel'+str(i), edit=True, allObjects=0)
			else:
				mc.modelEditor('modelPanel'+str(i), edit=True, allObjects=1)
		except:
			print ('modelPanel' + str(i) + ' not found')

#try except pass example:#	for i in ref:
#try except pass example:#		mc.select(clear=True)
#try except pass example:#		try:
#try except pass example:#			mc.select (i+'dumper_r_f_tire_part_11_loGeo1.f[0:17777]', r=True)
#try except pass example:#		except:pass

def preserveedge():
	sel = mc.ls(selection=True)
	for i in sel:
  		mc.setAttr (i+'Shape.osdFvarBoundary', 1)
def bokeh():
	import maya.cmds as mc
	locator1 = ('cameraLocator')
	locator2 = ('targetLocator')

	cmr= mc.ls(selection=True)
	if mc.objExists('*Boke*'):
		mc.select ("*Boke*")
		mel.eval('doDelete;')
		print("Bokeh nodes deleted")
	else:
		print("No Bokeh object detected")
	#mel.eval('unifiedRenderGlobalsWindow')
	#mel.eval('redshiftCreateGlobalShader RedshiftBokeh "rendernode/redshift/shader/lens" "bokeh";')
	#mc.setAttr ('rsBokeh1.dofDeriveFocusDistanceFromCamera', 0)
	if mc.objExists('*distanceD*'):
		mc.select ("*distanceD*")
		mel.eval('doDelete;')
		print("Distance Dimension deleted")
	else:
		print ("No Distance Dimension detected")
	if mc.objExists('*targetLoc*'):
		mc.select ("*targetLoc*")
		mel.eval('doDelete;')
		print("BokehLocators deleted")
	else:
		print("No BokehLocators detected")
	if mc.objExists('*cameraLoc*'):
		mc.select ("*cameraLoc*")
		mel.eval('doDelete;')
		print("BokehLocators deleted")
	else:
		print("No BokehLocators detected")
	mc.createNode  ('distanceDimShape') #instead of creating distanceDimension directly, this one doesn't create extra locators.
	mc.spaceLocator( p=(0, 0, 0), name=locator1)
	mc.spaceLocator( p=(0, 0, 0), name=locator2)
	mc.addAttr( shortName='fstop', ln='Fstop', k=1, dv=5.6, min=0.001, max=5000)
	mc.addAttr( shortName='fregscale', ln='FocusRegionScale', k=1, dv=1, min=0.001, max=10)
	mc.connectAttr (locator1+'Shape.worldPosition', 'distanceDimensionShape1.startPoint', f=True)
	mc.connectAttr (locator2+'Shape.worldPosition', 'distanceDimensionShape1.endPoint', f=True)
	mc.connectAttr (locator2+'.Fstop', cmr[0]+'.fStop', f=True)
	mc.connectAttr (locator2+'.FocusRegionScale', cmr[0]+'.focusRegionScale', f=True)
	mc.connectAttr (cmr[0]+'.translate', locator1+'.translate', f=True)
	mc.connectAttr (cmr[0]+'.rotate', locator1+'.rotate', f=True)
	mc.connectAttr (cmr[0]+'.scale', locator1+'.scale', f=True)
	camTX=mc.getAttr(cmr[0]+'.translateX')
	camTY=mc.getAttr(cmr[0]+'.translateY')
	camTZ=mc.getAttr(cmr[0]+'.translateZ')
	camRX=mc.getAttr(cmr[0]+'.rotateX')
	camRY=mc.getAttr(cmr[0]+'.rotateY')
	camRZ=mc.getAttr(cmr[0]+'.rotateZ')
	camSX=mc.getAttr(cmr[0]+'.scaleX')
	camSY=mc.getAttr(cmr[0]+'.scaleY')
	camSZ=mc.getAttr(cmr[0]+'.scaleZ')
	mc.setAttr(locator2+'.translate', camTX, camTY, camTZ, type="double3")
	mc.setAttr(locator2+'.rotate', camRX, camRY, camRZ, type="double3")
	mc.setAttr(locator2+'.scale', camSX, camSY, camSZ, type="double3")
	mc.parent (locator2, cmr[0])
	mc.move (0, 0, -50, locator2, r=True, wd=True, os=True)
	mc.setAttr(cmr[0]+'.depthOfField', 1)
	mc.connectAttr ('distanceDimensionShape1.distance', cmr[0]+'.focusDistance', f=True)
def atmos():
	global atmoname
	atmoname='VolumetricATM'
	mc.shadingNode ('RedshiftVolumeScattering', asUtility=True, name=atmoname)
	mel.eval('redshiftChangeGlobalShader (python("atmoname")) "atmosphere";')
def unatmos():
	listatm=mc.listConnections ("redshiftOptions.atmosphere")
	mc.disconnectAttr ((listatm[0]+".message"), "redshiftOptions.atmosphere")
	print (listatm[0])
	mc.delete (listatm[0])
def rendercam():
	mc.camera (centerOfInterest=1,
				focalLength=35,
				lensSqueezeRatio=1,
				cameraScale=1,
				displayFilmGate=True,
				displayGateMask=True,
				horizontalFilmAperture=1.41732,
				horizontalFilmOffset=0,
				verticalFilmAperture=0.94488,
				verticalFilmOffset=0,
				overscan=2,
				motionBlur=0,
				shutterAngle=144,
				nearClipPlane=0.05,
				farClipPlane=1000000,
				orthographic=0,
				orthographicWidth=30,
				panZoomEnabled=0,
				horizontalPan=0,
				verticalPan=0,
				zoom=1)
	cam=mc.ls(selection=True)
	mc.rename (cam[0], 'renderCam_#')
	cam=mc.ls(selection=True)
	mc.lookThru(cam)

def checkerfield():
	mc.shadingNode('checker', asTexture=True)
	checker=mc.ls(selection=True)
	mc.setAttr(checker[0]+'.color1', 0.5,0.5,0.5)
	mc.setAttr(checker[0]+'.color2', 0.18,0.18,0.18)
	mc.shadingNode('place2dTexture', asUtility=True)
	checkUV=mc.ls(selection=True)
	mc.connectAttr(checkUV[0]+'.outUV', checker[0]+'.uvCoord')
	mc.connectAttr(checkUV[0]+'.outUvFilterSize', checker[0]+'.uvFilterSize')
	mc.setAttr(checkUV[0]+'.repeatU', 50)
	mc.setAttr(checkUV[0]+'.repeatV', 50)
	#createPlane
	mc.polyPlane(w=1000, h=1000, sx=10, sy=10, cuv=2, ch=1)
	plane=mc.ls(selection=True)
	#createRedshiftStandardMaterial
	mc.shadingNode ('RedshiftStandardMaterial', asShader=True, name=checker[0]+'_S')
	mc.setAttr(checker[0] + '_S.refl_weight', 0.0)
	mc.setAttr(checker[0] + '_S.refl_roughness', 0.0)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=checker[0]+ '_SG')
	mc.connectAttr(checker[0]+'_S.outColor', checker[0]+'_SG.surfaceShader')
	mc.connectAttr(checker[0]+'.outColor', checker[0]+'_S.base_color')
	mc.select(plane[0])
	mc.sets(plane[0], edit=True, forceElement=checker[0]+'_SG')
def nodetype():
#______nodeType for 1 object(edit for more than one)________________________________________________________
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		node = mc.nodeType (sel[i])
		obj =  mc.objectType (sel[i])
		mc.confirmDialog( title='Warning: Nodetype', message='NodeType is : '+node+'\nObjectType is : '+obj, button=['Ok'], defaultButton='Ok', cancelButton='Ok')
def bakesimulation():
	mel.eval('BakeSimulationOptions')
def snp():
		sel = mc.ls(selection=True)
		for i in range(len(sel)):
			posF=mc.xform(sel[0],q=1,ws=1,translation=True)
			mc.xform(sel[1], ws=1, translation=posF)
			mc.parentConstraint(sel[0], sel[1])
			mel.eval('BakeSimulationOptions')
			mc.select('*camera')
def camset():
	cams=mc.ls(cameras=True)
	ref=['*','*:','*:*:','*:*:*:']
	for x in ref:
		for i in range (1,7):
			try:
				print (cams[i])
			except:pass
			try:
				mc.setAttr(x + cams[i]+'.overscan', 1.15)
			except:pass
			try:
				mc.setAttr(x + cams[i]+'.nearClipPlane', 0.03)
			except:pass
			try:
				mc.setAttr(x + cams[i]+'.farClipPlane', 10000000)
			except:pass
			try:
				mc.setAttr(x + cams[i]+'.renderable', 0)
			except:pass
			try:
				mc.setAttr(x + '*:cameraShape1.renderable', 1)
			except:pass
			try:
				mc.setAttr(x + '*:cameraShape1.renderable', 1)
			except:pass
			try:
				mc.setAttr(x + '*:cameraShape1.overscan', 1.15)
			except:pass
			try:
				mc.setAttr(x + '*:cameraShape1.nearClipPlane', 0.03)
			except:pass
			try:
				mc.setAttr(x + 'cameraShape1.renderable', 1)
			except:pass
			try:
				mc.setAttr(x + 'cameraShape1.renderable', 1)
			except:pass
			try:
				mc.setAttr(x + 'cameraShape1.overscan', 1.15)
			except:pass
			try:
				mc.setAttr(x + 'cameraShape1.nearClipPlane', 0.03)
			except:pass
def lightblocker():
	lightb='lightblock_#'
	mc.polyPlane (n=lightb, w=25, h=25, sx=4, sy=4)
	lightblock = mc.ls(selection=True)
	mc.setAttr (lightblock[0] + 'Shape.rsEnableVisibilityOverrides', 1)
	mc.setAttr (lightblock[0] + 'Shape.rsPrimaryRayVisible', 0)
	mc.setAttr (lightblock[0] + 'Shape.rsSecondaryRayVisible', 0)
	mc.setAttr (lightblock[0] + 'Shape.rsSecondaryRayVisible', 0)
	mc.setAttr (lightblock[0] + 'Shape.rsShadowReceiver', 0)
	mc.setAttr (lightblock[0] + 'Shape.rsSelfShadows', 0)
	mc.setAttr (lightblock[0] + 'Shape.rsAOCaster', 0)
	mc.shadingNode ('RedshiftStandardMaterial', asShader=True, n=lightblock[0] + '_S')
	sel_shader = mc.ls(selection=True)
	mc.setAttr(sel_shader[0] + '.diffuse_weight', 0)
	mc.setAttr(sel_shader[0] + '.refl_weight', 0)
	mc.setAttr (sel_shader[0]+ '.opacity_color', 0.4, 0.4, 0.4, type='double3')
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=sel_shader[0] + 'G')
	mc.connectAttr(sel_shader[0] + '.outColor', sel_shader[0] + 'G.surfaceShader')
	mc.sets(lightblock[0], edit=True, forceElement=sel_shader[0] + 'G')
	mc.select (lightblock[0])

def matteAll():
	pmesh=mc.ls(type='mesh')
	mc.select (pmesh)
	sel_geo = mc.ls(selection=True)
	matte=('matteBG_')
	mc.shadingNode ('RedshiftMatteShadowCatcher', asShader=True, n=matte + '_S')
	sel_shader = mc.ls(selection=True)
	mc.setAttr(sel_shader[0] + '.catch_shadows', 0)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=sel_shader[0] + 'G')
	mc.connectAttr(sel_shader[0] + '.outColor', sel_shader[0] + 'G.surfaceShader')
	for i in range(len(sel_geo)):
		mc.sets(sel_geo[i], edit=True, forceElement=sel_shader[0] + 'G')
	mc.select (clear=True)
	try:
		mc.select ('*:mash_assets_grp', add=True)
	except:pass
	try:
		mc.select ('*:*:mash_assets_grp', add=True)
	except:pass
	try:
		mc.select ('*:*:*:mash_assets_grp', add=True)
	except:pass
	sel_mash=mc.ls(selection=True)
	mc.hide (sel_mash)

def matteOne():
	import random as random
	from random import uniform as rand
	rand1 = rand(0.0,1.0)
	rand2 = rand(0.01,0.99)
	ranD4 = rand(0.02,0.98)
	draw_list = [0.35, 0.30, 0.25, 0.20, 0.15, -0.35, -0.30, -0.25, -0.20, -0.15,]
	randlist = random.choice(draw_list)
	sel_geo = mc.ls(selection=True)
	matte=('matte_')
	mc.shadingNode ('RedshiftMatteShadowCatcher', asShader=True, n=matte + '_S')
	sel_shader = mc.ls(selection=True)
	mc.setAttr(sel_shader[0] + '.catch_shadows', 0)
	mc.setAttr(sel_shader[0] + '.catch_diffuse', 1)
	mc.setAttr(sel_shader[0] + '.background', rand1+randlist, rand2+randlist, ranD4+randlist, type="double3")
	mc.setAttr(sel_shader[0] + '.diffuse', rand1+randlist, rand2+randlist, ranD4+randlist, type="double3")
	mc.setAttr(sel_shader[0] + '.background_alpha', 1)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=sel_shader[0] + 'G')
	mc.connectAttr(sel_shader[0] + '.outColor', sel_shader[0] + 'G.surfaceShader')
	for i in range(len(sel_geo)):
		mc.sets(sel_geo[i], edit=True, forceElement=sel_shader[0] + 'G')
	mc.select (clear=True)

def isolateObject():
	sel_f=mc.ls(selection=True)
	sel_fshape= mc.listRelatives(sel_f, shapes=True)
	mc.select (clear=True)
	pmesh=mc.ls(type='mesh')
	mc.select (pmesh)
	for i in range(len(sel_f)):
		mc.select (sel_f[i], deselect=True)
		mc.select (sel_fshape[i], deselect=True)
	sel_geo = mc.ls(selection=True)
	matte=('matte_')
	mc.shadingNode ('RedshiftMatteShadowCatcher', asShader=True, n=matte + '_S')
	sel_shader = mc.ls(selection=True)
	mc.setAttr(sel_shader[0] + '.catch_shadows', 0)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=sel_shader[0] + 'G')
	mc.connectAttr(sel_shader[0] + '.outColor', sel_shader[0] + 'G.surfaceShader')
	for i in range(len(sel_geo)):
		mc.sets(sel_geo[i], edit=True, forceElement=sel_shader[0] + 'G')
	mc.select (clear=True)

def incsave():
	mel.eval('incrementAndSaveScene 1;')
def _animRand(attrs):
	#Add a fresh random offset (within the Min/Max fields) to each checked axis
	import random
	try:
		mn = float(mc.textField(animMin, q=True, text=True))
	except:
		mn = 0.0
	try:
		mx = float(mc.textField(animMax, q=True, text=True))
	except:
		mx = 0.0
	use = [mc.checkBox(animX, q=True, value=True),
		mc.checkBox(animY, q=True, value=True),
		mc.checkBox(animZ, q=True, value=True)]
	sel = mc.ls(selection=True)
	for obj in sel:
		for u, a in zip(use, attrs):
			if u:
				try:
					cur = mc.getAttr(obj + a)
					mc.setAttr(obj + a, cur + random.uniform(mn, mx))
				except:
					pass
def translate():
	_animRand(['.tx', '.ty', '.tz'])
def scale():
	_animRand(['.sx', '.sy', '.sz'])
def rotate():
	_animRand(['.rx', '.ry', '.rz'])
def renderview():
	mel.eval('redshiftRvShow')
def hyper():
	mel.eval('HypershadeWindow')
def uveditor():
	mel.eval('TextureViewWindow')
def scripteditor():
	mel.eval('ScriptEditor')
def rendersettings():
	mel.eval('unifiedRenderGlobalsWindow')
def grapheditor():
	mel.eval('GraphEditor')
def nodeeditor():
	mel.eval('NodeEditorWindow')
def attspread():
	mel.eval('SpreadSheetEditor')
def lightlink():
	mel.eval('LightCentricLightLinkingEditor')
def rsfeedback():
	mc.rsRender (showFeedbackDisplay=True)

def targetselect():
	try:
		selectdumper=mc.select('*targetLocator', add=True)
	except:pass
	try:
		selectdumper=mc.select('*:targetLocator', add=True)
	except:pass

def focussett():
	import maya.api.OpenMaya as om
	mel.eval('CBdeleteConnection "targetLocator.fstop"')
	mel.eval('CBdeleteConnection "targetLocator.fregscale"')
	mc.setAttr('targetLocator.Fstop', 8.6)
	mc.setAttr('targetLocator.FocusRegionScale', 3)

def faceselect():
	mc.selectMode (component=True)
	mel.eval('setComponentPickMask "Facet" true;')
	mel.eval('setComponentPickMask "Line" false;')
	mel.eval('setComponentPickMask "Point" false;')
def edgeselect():
	mc.selectMode (component=True)
	mel.eval('setComponentPickMask "Facet" false;')
	mel.eval('setComponentPickMask "Line" true;')
	mel.eval('setComponentPickMask "Point" false;')
def vertexselect():
	mc.selectMode (component=True)
	mel.eval('setComponentPickMask "Facet" false;')
	mel.eval('setComponentPickMask "Line" false;')
	mel.eval('setComponentPickMask "Point" true;')
def objselect():
	mc.selectMode (object=True)

def duplicateshader():
	sel = mc.ls(selection=True)
	mc.hyperShade(sel[0], duplicate=True)

def exportdesk():
	import os
	desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.select (sel, deselect=True)
		mc.select (sel[i])
		mc.file(os.path.join(desktop, sel[i]), force = True, options = "v = 0", type = "FBX export", exportSelected = True)
		mc.select (sel[i], deselect=True)
	#if not working, reOpen maya

def exportdeskma():
	import os
	desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		temp = sel[i].replace('_grp', '')
		zeropiv()
		zero()
		fTrans()
		dHis()
		mc.file(os.path.join(desktop, temp), force = True, options = "v = 0", type = "mayaAscii", exportSelected = True)
	#if not working, reOpen maya
def planarX():
	sel = mc.ls(selection=True)
	list = mc.polyListComponentConversion(sel, tf=True)
	mc.polyProjection(list, type='Planar', md='x')
	mc.select(list)
def planarY():
	sel = mc.ls(selection=True)
	list = mc.polyListComponentConversion(sel, tf=True)
	mc.polyProjection(list, type='Planar', md='y')
	mc.select(list)
def planarZ():
	sel = mc.ls(selection=True)
	list = mc.polyListComponentConversion(sel, tf=True)
	mc.polyProjection(list, type='Planar', md='z')
	mc.select(list)


mc.loadPlugin( 'redshift4maya.mll')
mc.setAttr("defaultRenderGlobals.currentRenderer", "redshift", type="string")

##############################################################################################################################################
######################################################################   HOTKEYS  ############################################################
##############################################################################################################################################

mc.nameCommand( 'weeToools', annotation='weeToools', command="python(\"import urllib.request,__main__; exec(urllib.request.urlopen('https://raw.githubusercontent.com/ersizzle/weeScript/master/weeScript.py').read().decode('utf-8'), __main__.__dict__)\")")
mc.hotkey( k='1', alt=True, name='weeToools')
mc.nameCommand( 'hyper', annotation='hypershade', command='HypershadeWindow')
mc.hotkey( k='2', alt=True, name='hyper')
mc.nameCommand( 'rsrenderview', annotation='rsrenderview', command='redshiftRvShow')
mc.hotkey( k='^', alt=True, name='rsrenderview')
mc.nameCommand( 'scripteditor', annotation='scripteditor', command='ScriptEditor')
mc.hotkey( k='4', alt=True, name='scripteditor')
mc.nameCommand( 'uveditor', annotation='uveditor', command='TextureViewWindow')
mc.hotkey( k='5', alt=True, name='uveditor')
mc.nameCommand( 'nodeeditor', annotation='nodeeditor', command='NodeEditorWindow')
mc.hotkey( k='6', alt=True, name='nodeeditor')
mc.nameCommand('grapheditor', annotation='grapheditor', command='GraphEditor')
mc.hotkey( k='7', alt=True, name='grapheditor')
mc.nameCommand('renderSettings', annotation='rendersettings', command='unifiedRenderGlobalsWindow;')
mc.hotkey( k='a', sht=True, ctl=True, name='renderSettings')
mc.nameCommand('nameSpaceeditor', annotation='NamespaceEditor', command='NamespaceEditor')
mc.hotkey( k='x', alt=True, sht=True, name='nameSpaceeditor')
mc.nameCommand('filePatheditor', annotation='FilePathEditor', command='FilePathEditor')
mc.hotkey( k='z', alt=True, sht=True, name='filePatheditor')

mc.nameCommand( 'fTrans', annotation='FreezeTransformations', command='python("mc.makeIdentity( apply=True )")', stp='python')
mc.hotkey( k='q', sht=True, name='fTrans')
mc.nameCommand( 'dHis', annotation='DeleteHistory', command='python("mc.delete (ch=True)")', stp='python')
mc.hotkey( k="w", sht=True, name='dHis')
mc.nameCommand( 'cpivot', annotation='CenterPivot', command='python("cPiv()")', stp='python')
mc.hotkey( k='e', sht=True, name='cpivot')
mc.nameCommand( 'bpivot', annotation='BottomPivot', command='python("bPiv()")', stp='python')
mc.hotkey( k='e', ctl=True, name='bpivot')
mc.nameCommand( 'sendzero', annotation='sendZero', command='python("zero()")', stp='python')
mc.hotkey( k='r', sht=True, name='sendzero')
mc.nameCommand( 'planarx', annotation='pLanarx', command='python("planarX()")', stp='python')
mc.hotkey( k='a', sht=True, alt=True, name='planarx')
mc.nameCommand( 'planary', annotation='pLanary', command='python("planarY()")', stp='python')
mc.hotkey( k='s', sht=True, alt=True, name='planary')
mc.nameCommand( 'planarz', annotation='pLanarz', command='python("planarZ()")', stp='python')
mc.hotkey( k='d', sht=True, alt=True, name='planarz')
mc.nameCommand( 'exportdesktop', annotation='Exportdeskt', command='python("exportdesk()")', stp='python')
mc.hotkey( k='t', sht=True, name='exportdesktop')
mc.nameCommand( 'exportdesktopma', annotation='Exportdesktma', command='python("exportdeskma()")', stp='python')
mc.hotkey( k='y', sht=True, name='exportdesktopma')
mc.nameCommand( 'extractf', annotation='ExtractFaces', command='ExtractFace')
mc.hotkey( k='c', sht=True, name='extractf')
incrsave = mc.nameCommand('incrsave', annotation='incrsave', command='python("incsave()")', stp='python')
mc.hotkey(k='Space', ctl=True, sht=True, name='incrsave')
mc.nameCommand('importt', annotation='import', command='Import', stp='python')
mc.hotkey(k='I', sht=True, name='importt')



fselect = mc.nameCommand('fselect', annotation='fselect', command='python("faceselect()")', stp='python')
mc.hotkey(k='F2', sht=True, name='fselect')
edselect = mc.nameCommand('edselect', annotation='edselect', command='python("edgeselect()")', stp='python')
mc.hotkey(k='F3', sht=True, name='edselect')
vtxselect = mc.nameCommand('vtxselect', annotation='vtxselect', command='python("vertexselect()")', stp='python')
mc.hotkey(k='F4', sht=True, name='vtxselect')
obselect = mc.nameCommand('obselect', annotation='obselect', command='python("objselect()")', stp='python')
mc.hotkey(k='F1', sht=True, name='obselect')
dpshader = mc.nameCommand('dpshader', annotation='dpshader', command='python("duplicateshader()")', stp='python')
mc.hotkey(k='G', sht=True, name='dpshader')


mat111 = mc.nameCommand( 'mat111', annotation='mat1', command='python("mat1()")', stp='python')
mc.hotkey( k='q', sht=True, ctl=True, name='mat111')

##############################################################################################################################################
######################################################################  HOTKEYS END  ############################################################
##############################################################################################################################################

mel.eval('SavePreferences')
mel.eval('savePrefs')
mel.eval('saveToolSettings')
mel.eval('saveViewportSettings')
mc.workspaceControl(ui, retain=True, floating=True, uiScript='weeToolsUI()',
	initialWidth=230, initialHeight=900)
mc.workspaceControl(ui, e=True, resizeWidth=230)


#unknownPlugin -q -l;
#unknownPlugin -r "rpmaya"
#unknownPlugin -r "stereoCamera"
#unknownPlugin -r "Mayatomr"
#select -r `ls -type unknown`;
#
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
###############################################################################################################################################
