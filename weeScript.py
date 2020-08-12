#to execute from another location, enter code below in to MEL :
#python("execfile(r'Z:/HomurGumur/Trash/erbay/weeScript.py')");
#python("execfile('C:/Users/er/Downloads/weeScript.py')")
import maya.cmds as mc
import maya.mel as mel

ui='weeTools'
title = ui

if mc.workspaceControl(ui, q=True, exists=True):
	mc.workspaceControl(ui, e=True, close=True)
	mc.deleteUI(ui, control=True)

def weeToolsUI():
	global field1
	global field2
	mainLayout = mc.columnLayout(
				width = 246,
				height = 790,
				rowSpacing= 0,
				columnOffset=('both', 0) )
	modelfLayout = mc.frameLayout(l = "  MODELING", parent = mainLayout, cll =1, cl =0, bgc= [0.21, 0.21, 0.21])
	rowLayoutA1 = mc.rowColumnLayout(
						parent = modelfLayout,
						numberOfColumns = 5,
						h=38,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2)],
						columnWidth = [(1,52), (2,51), (3,50), (4,49), (5,50)]
						)
	rowLayoutA2 = mc.rowColumnLayout(
						parent = modelfLayout,
						numberOfColumns = 4,
						h=38,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2)],
						columnWidth = [(1,60), (2,60), (3,60), (4,60)]
						)
	rowLayoutA3 = mc.rowColumnLayout(
						parent = modelfLayout,
						numberOfColumns = 4,
						h=38,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2)],
						columnWidth = [(1,60), (2,60), (3,60), (4,60)]
						)
	shadingfLayout = mc.frameLayout(l = "  SHADING", parent = mainLayout, cll =1, cl =0, bgc= [0.21, 0.21, 0.21])
	rowLayoutB1 = mc.rowColumnLayout(
						parent = shadingfLayout,
						numberOfColumns = 6,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2), (6,'both',2)],
						columnWidth = [(1,32), (2,32), (3,34), (4,48), (5,48), (6,38)]
						)
	rowLayoutB2 = mc.rowColumnLayout(
						parent = shadingfLayout,
						numberOfColumns = 7,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2), (6,'both',2), (7,'both',2)],
						columnWidth = [(1,30), (2,30), (3,30), (4,30), (5,30), (6,36), (7,36)]
						)
	rowLayoutB21 = mc.rowColumnLayout(
						parent = shadingfLayout,
						numberOfColumns = 7,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2), (6,'both',2), (7,'both',2)],
						columnWidth = [(1,30), (2,30), (3,30), (4,30), (5,30), (6,44), (7,40)]
						)
	shadingffLayout = mc.frameLayout(l = "  PRE-SHADING", parent = shadingfLayout, cll =1, cl =1, bgc= [0.21, 0.21, 0.21])
	rowLayoutB3 = mc.rowColumnLayout(
						parent = shadingffLayout,
						numberOfColumns = 5,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2)],
						columnWidth = [(1,44), (2,44), (3,44), (4,54), (5,50)]
						)
	rowLayoutB4 = mc.rowColumnLayout(
						parent = shadingffLayout,
						numberOfColumns = 5,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2)],
						columnWidth = [(1,46), (2,36), (3,36), (4,44), (5,44)]
						)
	rowLayoutB5 = mc.rowColumnLayout(
						parent = shadingffLayout,
						numberOfColumns = 4,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2)],
						columnWidth = [(1,46), (2,36), (3,36), (4,44)]
						)
	namingfLayout = mc.frameLayout(l = "  NAME", parent = mainLayout, cll =1, cl =0, bgc= [0.21, 0.21, 0.21])
	rowLayoutC1 = mc.rowColumnLayout(
						parent = namingfLayout,
						numberOfColumns = 1,
						columnOffset = [(1,'both',2)],
						columnWidth = [(1,235)]
						)
	rowLayoutC1A = mc.rowColumnLayout(
						parent = namingfLayout,
						numberOfColumns = 1,
						columnOffset = [(1,'both',2)],
						columnWidth = [(1,235)]
						)
	rowLayoutC1B = mc.rowColumnLayout(
						parent = namingfLayout,
						numberOfColumns = 5,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2)],
						columnWidth = [(1,48),(2,48),(3,48),(4,48),(5,48)]
						)
	namingffLayout = mc.frameLayout(l = "  PRE-NAME", parent = namingfLayout, cll =1, cl =1, bgc= [0.21, 0.21, 0.21])
	rowLayoutC2 = mc.rowColumnLayout(
						parent = namingffLayout,
						numberOfColumns = 6,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2), (6,'both',2)],
						columnWidth = [(1,41), (2,41), (3,41), (4,43), (5,37), (6,37)]
						)
	rowLayoutC5 = mc.rowColumnLayout(
						parent = namingffLayout,
						numberOfColumns = 8,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2), (6,'both',2), (7,'both',2)],
						columnWidth = [(1,28), (2,32), (3,28), (4,28), (5,36), (6,38), (7,36)]
						)
	rowLayoutC6 = mc.rowColumnLayout(
						parent = namingffLayout,
						numberOfColumns = 8,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2), (6,'both',2), (7,'both',2), (8,'both',2)],
						columnWidth = [(1,29), (2,29), (3,29), (4,29), (5,29), (6,29), (7,29), (8,29)]
						)
	renderfLayout = mc.frameLayout(l = "  RENDER", parent = mainLayout, cll =1, cl =0, bgc= [0.21, 0.21, 0.21])
	rowLayoutD1 = mc.rowColumnLayout(
						parent = renderfLayout,
						numberOfColumns = 6,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2), (6,'both',2)],
						columnWidth = [(1,24), (2,34), (3,30), (4,35), (5,42), (6,54)]
						)
	rowLayoutD2 = mc.rowColumnLayout(
						parent = renderfLayout,
						numberOfColumns = 4,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2)],
						columnWidth = [(1,52), (2,52), (3,41), (4,52)]
						)
	rowLayoutD3 = mc.rowColumnLayout(
						parent = renderfLayout,
						numberOfColumns = 5,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2)],
						columnWidth = [(1,51), (2,46), (3,48), (4,44), (5,51)]
						)
	rowLayoutD4 = mc.rowColumnLayout(
						parent = renderfLayout,
						numberOfColumns = 6,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2), (6,'both',2)],
						columnWidth = [(1,40), (2,40), (3,40), (4,40), (5,40), (6,40)]
						)
	rowLayoutD5 = mc.rowColumnLayout(
						parent = renderfLayout,
						numberOfColumns = 4,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2)],
						columnWidth = [(1,64), (2,76), (3,56), (4,45)]
						)
	rowLayoutD6 = mc.rowColumnLayout(
						parent = renderfLayout,
						numberOfColumns = 8,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2), (6,'both',2), (7,'both',2), (8,'both',2)],
						columnWidth = [(1,27), (2,27), (3,27), (4,27), (5,27), (6,27), (7,30), (8,38)]
						)
	rowLayoutD7 = mc.rowColumnLayout(
						parent = renderfLayout,
						numberOfColumns = 5,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2)],
						columnWidth = [(1,68), (2,40), (3,33), (4,42),(5,40)]
						)
	animationfLayout = mc.frameLayout(l = "  ANIMATION", parent = mainLayout, cll =1, cl =1, bgc= [0.21, 0.21, 0.21])
	rowLayoutE1 = mc.rowColumnLayout(
						parent = animationfLayout,
						numberOfColumns = 5,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2)],
						columnWidth = [(1,48), (2,54), (3,35), (4,54), (5,50)]
						)
	windowfLayout = mc.frameLayout(l = "  WINDOWS", parent = mainLayout, cll =1, cl =0, bgc= [0.21, 0.21, 0.21])
	rowLayoutF1 = mc.rowColumnLayout(
						parent = windowfLayout,
						numberOfColumns = 5,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2)],
						columnWidth = [(1,48), (2,45), (3,45), (4,48), (5,50)]
						)
	rowLayoutF2 = mc.rowColumnLayout(
						parent = windowfLayout,
						numberOfColumns = 6,
						columnOffset = [(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2), (5,'both',2), (6,'both',2)],
						columnWidth = [(1,41), (2,41), (3,46), (4,37), (5,42), (6,41)]
						)
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
########################################################## BUTTONS ###########################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

	mc.button(parent = rowLayoutA1, label = 'Freeze\nTransfo..', bgc= [0.35, 0.228, 0.228], command = 'fTrans()')
	mc.button(parent = rowLayoutA1, label = 'Delete\nHistory', bgc= [0.35, 0.228, 0.228], command = 'dHis()')
	mc.button(parent = rowLayoutA1, label = 'Delete\nN.Hist.', bgc= [0.35, 0.228, 0.228], command = 'dnondefHis()')
	mc.button(parent = rowLayoutA1, label = 'Center\nPivot', bgc= [0.35, 0.228, 0.228], command = 'cPiv()')
	mc.button(parent = rowLayoutA1, label = 'Bottom\nPivot', bgc= [0.35, 0.228, 0.228], command = 'bPiv()')
	############################################################################################
	mc.button(parent = rowLayoutA2, label = 'Send to\n0 0 0', bgc= [0.35, 0.228, 0.228], command = 'zero()')
	mc.button(parent = rowLayoutA2, label = 'Copy\nAttributes', bgc= [0.35, 0.228, 0.228], command = 'cpyAtt()')
	mc.button(parent = rowLayoutA2, label = 'Group', command = 'group()')
	mc.button(parent = rowLayoutA2, label = 'Auto UV', bgc= [0.35, 0.35, 0.222], command = 'autoUV()')
############################################################################################
	mc.button(parent = rowLayoutA3, label = 'Bounding\nBox On', bgc= [0.15, 0.228, 0.228], command = 'box()')
	mc.button(parent = rowLayoutA3, label = 'Bounding\nBox Off', bgc= [0.15, 0.228, 0.228], command = 'unbox()')
	mc.button(parent = rowLayoutA3, label = 'Lock\nAttributes', bgc= [0.228, 0.228, 0.35], command = 'lock()')
	mc.button(parent = rowLayoutA3, label = 'UnLock\nAttributes', bgc= [0.228, 0.228, 0.35], command = 'unlock()')
############################################################################################
	mc.button(parent = rowLayoutB1, label = 'Tess\n2', bgc= [0.305, 0.222, 0.35], command = 'tess2()')
	mc.button(parent = rowLayoutB1, label = 'Tess\n3', bgc= [0.305, 0.222, 0.35], command = 'tess3()')
	mc.button(parent = rowLayoutB1, label = 'Tess\n Off', bgc= [0.305, 0.222, 0.35], command = 'untess()')
	mc.button(parent = rowLayoutB1, label = 'Displ-\nace On', bgc= [0.15, 0.228, 0.228], command = 'disp()')
	mc.button(parent = rowLayoutB1, label = 'Displ-\nace Off', bgc= [0.15, 0.228, 0.228], command = 'undisp()')
	mc.button(parent = rowLayoutB1, label = 'Back\nFace', bgc= [0.15, 0.228, 0.228], command = 'backface()')
############################################################################################
	mc.button(parent = rowLayoutB2, label = 'Mat\n1', command = 'mat1()')
	mc.button(parent = rowLayoutB2, label = 'Mat\n2', command = 'mat2()')
	mc.button(parent = rowLayoutB2, label = 'Mat\n3', command = 'mat3()')
	mc.button(parent = rowLayoutB2, label = 'Mat\n4', command = 'mat4()')
	mc.button(parent = rowLayoutB2, label = 'Mat\n5', command = 'mat5()')
	mc.button(parent = rowLayoutB2, label = 'Prim.\nvis 1', bgc= [0.305, 0.222, 0.35], command = 'primvis()')
	mc.button(parent = rowLayoutB2, label = 'Prim.\nvis 0', bgc= [0.305, 0.222, 0.35], command = 'unprimvis()')
############################################################################################
	mc.button(parent = rowLayoutB21, label = 'PBR\nD', command = 'pbrd()')
	mc.button(parent = rowLayoutB21, label = 'PBR\nM', command = 'pbrm()')
	mc.button(parent = rowLayoutB21, label = 'S\nRGB', command = 'setsrgb()')
	mc.button(parent = rowLayoutB21, label = 'Lin\near', command = 'setlin()')
	mc.button(parent = rowLayoutB21, label = 'AC\nES', command = 'aces()')
	mc.button(parent = rowLayoutB21, label = 'texCon', command = 'texcon()')
	mc.button(parent = rowLayoutB21, label = 'Lam\nbert', bgc= [0.3, 0.3, 0.3], command = 'matlambert()')
############################################################################################
	mc.button(parent = rowLayoutB3, label = 'Glass', bgc= [0.3, 0.5, 0.5], command = 'matglass()')
	mc.button(parent = rowLayoutB3, label = 'Water', bgc= [0.3, 0.5, 0.5], command = 'matwater()')
	mc.button(parent = rowLayoutB3, label = 'Plastic', bgc= [0.3, 0.5, 0.5], command = 'matplastic()')
	mc.button(parent = rowLayoutB3, label = 'Aluminium', bgc= [0.3, 0.5, 0.5], command = 'mataluminium()')
	mc.button(parent = rowLayoutB3, label = 'Copper', bgc= [0.3, 0.5, 0.5], command = 'matcopper()')
############################################################################################
	mc.button(parent = rowLayoutB4, label = 'Gold', bgc= [0.3, 0.5, 0.5], command = 'matgold()')
	mc.button(parent = rowLayoutB4, label = 'Iron', bgc= [0.3, 0.5, 0.5], command = 'matiron()')
	mc.button(parent = rowLayoutB4, label = 'Lead', bgc= [0.3, 0.5, 0.5], command = 'matlead()')
	mc.button(parent = rowLayoutB4, label = 'Platinum', bgc= [0.3, 0.5, 0.5], command = 'matplatinum()')
	mc.button(parent = rowLayoutB4, label = 'Silver', bgc= [0.3, 0.5, 0.5], command = 'matsilver()')
############################################################################################
	mc.button(parent = rowLayoutB5, label = 'Milky\nCoffee', bgc= [0.3, 0.5, 0.5], command = 'matmilky()')
	mc.button(parent = rowLayoutB5, label = 'Jade', bgc= [0.3, 0.5, 0.5], command = 'matjade()')
	mc.button(parent = rowLayoutB5, label = 'Paper', bgc= [0.3, 0.5, 0.5], command = 'matpaper()')
	mc.button(parent = rowLayoutB5, label = 'Tinted\nGlass', bgc= [0.3, 0.5, 0.5], command = 'mattinted()')
############################################################################################
############################################################################################
	field1 = mc.textField(parent = rowLayoutC1)
	field2 = mc.textField(parent = rowLayoutC1A)
	mc.button(parent = rowLayoutC1B, label = 'Rename', command = 'changeName()')
	mc.button(parent = rowLayoutC1B, label = 'Shader', command = 'shaderName()')
	mc.button(parent = rowLayoutC1B, label = 'Prefix', command = 'prefix()')
	mc.button(parent = rowLayoutC1B, label = 'Sufix', command = 'sufix()')
	mc.button(parent = rowLayoutC1B, label = 'Replace', command = 'search()')
############################################################################################
	mc.button(parent = rowLayoutC2, label = '+_geo',  bgc= [0.95, 0.95, 0.95], command = 'addgeo()')
	mc.button(parent = rowLayoutC2, label = '+_grp', bgc= [0.75, 0.75, 0.75], command = 'addgrp()')
	mc.button(parent = rowLayoutC2, label = '+_low', bgc= [0.95, 0.95, 0.95], command = 'addlow()')
	mc.button(parent = rowLayoutC2, label = '+_high', bgc= [0.75, 0.75, 0.75], command = 'addhigh()')
	mc.button(parent = rowLayoutC2, label = '+_lgt', bgc= [0.95, 0.95, 0.95], command = 'addlgt()')
	mc.button(parent = rowLayoutC2, label = '+_off', bgc= [0.75, 0.75, 0.75], command = 'addoff()')
############################################################################################
	mc.button(parent = rowLayoutC5, label = '+_S', bgc= [0.95, 0.95, 0.95], command = 'addS()')
	mc.button(parent = rowLayoutC5, label = '+_SG', bgc= [0.75, 0.75, 0.75], command = 'addSG()')
	mc.button(parent = rowLayoutC5, label = '+_L', bgc= [0.95, 0.95, 0.95], command = 'addL()')
	mc.button(parent = rowLayoutC5, label = '+_R', bgc= [0.75, 0.75, 0.75], command = 'addR()')
	mc.button(parent = rowLayoutC5, label = '+_top', bgc= [0.95, 0.95, 0.95], command = 'addtop()')
	mc.button(parent = rowLayoutC5, label = '+_mid', bgc= [0.75, 0.75, 0.75], command = 'addmid()')
	mc.button(parent = rowLayoutC5, label = '+_bot', bgc= [0.95, 0.95, 0.95], command = 'addbot()')
############################################################################################
	mc.button(parent = rowLayoutC6, label = '+_A', bgc= [0.75, 0.75, 0.75], command = 'addA()')
	mc.button(parent = rowLayoutC6, label = '+_B', bgc= [0.95, 0.95, 0.95], command = 'addB()')
	mc.button(parent = rowLayoutC6, label = '+_C', bgc= [0.75, 0.75, 0.75], command = 'addC()')
	mc.button(parent = rowLayoutC6, label = '+_D', bgc= [0.95, 0.95, 0.95], command = 'addD()')
	mc.button(parent = rowLayoutC6, label = '+_E', bgc= [0.75, 0.75, 0.75], command = 'addE()')
	mc.button(parent = rowLayoutC6, label = '+_F', bgc= [0.95, 0.95, 0.95], command = 'addF()')
	mc.button(parent = rowLayoutC6, label = '+_G', bgc= [0.75, 0.75, 0.75], command = 'addG()')
	mc.button(parent = rowLayoutC6, label = '+_H', bgc= [0.95, 0.95, 0.95], command = 'addH()')
############################################################################################
	mc.button(parent = rowLayoutD1, label = 'RS', bgc= [0.3, 0.25, 0.55], command = 'redshift()')
	mc.button(parent = rowLayoutD1, label = 'Final', bgc= [0.305, 0.222, 0.45], command = 'fnrender()')
	mc.button(parent = rowLayoutD1, label = 'Pre', bgc= [0.305, 0.222, 0.40], command = 'prerender()')
	mc.button(parent = rowLayoutD1, label = 'oneF.', bgc= [0.305, 0.222, 0.35], command = 'oneframerender()')
	mc.button(parent = rowLayoutD1, label = 'Atmos.', bgc= [0.305, 0.222, 0.35], command = 'atmos()')
	mc.button(parent = rowLayoutD1, label = 'UnAtmos', bgc= [0.305, 0.222, 0.35], command = 'unatmos()')
############################################################################################
	mc.button(parent = rowLayoutD2, label = 'CleanUp', bgc= [0.305, 0.222, 0.35], command = 'optscene()')
	mc.button(parent = rowLayoutD2, label = 'TurtleKill', bgc= [0.305, 0.222, 0.35], command = 'turtlekill()')
	mc.button(parent = rowLayoutD2, label = 'Bokeh', bgc= [0.300, 0.262, 0.40], command = 'bokeh()')
	mc.button(parent = rowLayoutD2, label = 'Locator', bgc= [0.22, 0.22, 0.22], command = 'targetselect()')
############################################################################################
	mc.button(parent = rowLayoutD3, label = 'Domelgt', bgc= [0.35, 0.35, 0.25], command = 'domelgt()')
	mc.button(parent = rowLayoutD3, label = 'Arealgt', bgc= [0.35, 0.35, 0.3], command = 'arealgt()')
	mc.button(parent = rowLayoutD3, label = 'Pointlgt', bgc= [0.35, 0.35, 0.25], command = 'pointlgt()')
	mc.button(parent = rowLayoutD3, label = 'Spotlgt', bgc= [0.35, 0.35, 0.3], command = 'spotlgt()')
	mc.button(parent = rowLayoutD3, label = 'Directlgt', bgc= [0.35, 0.35, 0.25], command = 'directlgt()')
############################################################################################
	mc.button(parent = rowLayoutD4, label = '1080\n1920', command = 'x1080x1920()')
	mc.button(parent = rowLayoutD4, label = '720\n1280', bgc= [0.40, 0.40, 0.40], command = 'x720x1280()')
	mc.button(parent = rowLayoutD4, label = '540\n948', command = 'x540x948()')
	mc.button(parent = rowLayoutD4, label = '1080\n1080', bgc= [0.40, 0.40, 0.40], command = 'x1080x1080()')
	mc.button(parent = rowLayoutD4, label = '1080\n1350', command = 'x1080x1350()')
	mc.button(parent = rowLayoutD4, label = '2148\n3840', bgc= [0.40, 0.40, 0.40], command = 'x2148x3840()')
############################################################################################
	mc.button(parent = rowLayoutD5, label = 'RenderCam', bgc= [0.49, 0.49, 0.49], command = 'rendercam()')
	mc.button(parent = rowLayoutD5, label = 'Checker Field', bgc= [0.49, 0.49, 0.49], command = 'checkerfield()')
	mc.button(parent = rowLayoutD5, label = 'nodetype', bgc= [0.49, 0.49, 0.49], command = 'nodetype()')
	mc.button(parent = rowLayoutD5, label = 'Snap&Bake', bgc= [0.18, 0.18, 0.18], command = 'snp()')
############################################################################################
	mc.button(parent = rowLayoutD6, label = 'Joi', bgc= [0.49, 0.49, 0.49], command = 'showjoint()')
	mc.button(parent = rowLayoutD6, label = 'Pol', bgc= [0.49, 0.49, 0.49], command = 'showpoly()')
	mc.button(parent = rowLayoutD6, label = 'Cur', bgc= [0.49, 0.49, 0.49], command = 'showcurve()')
	mc.button(parent = rowLayoutD6, label = 'Lgt', bgc= [0.49, 0.49, 0.49], command = 'showlight()')
	mc.button(parent = rowLayoutD6, label = 'Cam', bgc= [0.49, 0.49, 0.49], command = 'showcam()')
	mc.button(parent = rowLayoutD6, label = 'All', bgc= [0.49, 0.49, 0.49], command = 'showallobjects()')
	mc.button(parent = rowLayoutD6, label = 'Cam', bgc= [0.3, 0.6, 0.5], command = 'camset()')
	mc.button(parent = rowLayoutD6, label = 'Focus', bgc= [0.32, 0.32, 0.32], command = 'focussett()')
############################################################################################
	mc.button(parent = rowLayoutD7, label = 'LightBlocker', bgc= [0.24, 0.27, 0.69], command = 'lightblocker()')
	mc.button(parent = rowLayoutD7, label = 'MatAll', bgc= [0.24, 0.27, 0.69], command = 'matteAll()')
	mc.button(parent = rowLayoutD7, label = 'Mat1', bgc= [0.24, 0.27, 0.69], command = 'matteOne()')
	mc.button(parent = rowLayoutD7, label = 'MatIso', bgc= [0.24, 0.27, 0.69], command = 'isolateObject()')
	mc.button(parent = rowLayoutD7, label = 'SaveI', bgc= [0.24, 0.27, 0.69], command = 'incsave()')
############################################################################################
	mc.button(parent = rowLayoutE1, label = 'Random', bgc= [0.65, 0.65, 0.75], command = '()')
	mc.button(parent = rowLayoutE1, label = 'Translate', bgc= [0.65, 0.65, 0.85], command = 'translate()')
	mc.button(parent = rowLayoutE1, label = 'Scale', bgc= [0.65, 0.65, 0.75], command = 'scale()')
	mc.button(parent = rowLayoutE1, label = 'Rotation', bgc= [0.65, 0.65, 0.85], command = 'rotate()')
	mc.button(parent = rowLayoutE1, label = 'BakeSim', bgc= [0.65, 0.65, 0.75], command = 'bakesimulation()')
############################################################################################
	mc.button(parent = rowLayoutF1, label = 'Render\nView', bgc= [0.3, 0.25, 0.55], command = 'renderview()')
	mc.button(parent = rowLayoutF1, label = 'Hyper\nshade', bgc= [0.3, 0.25, 0.55], command = 'hyper()')
	mc.button(parent = rowLayoutF1, label = 'UV\nEditor', bgc= [0.3, 0.25, 0.55], command = 'uveditor()')
	mc.button(parent = rowLayoutF1, label = 'Script\nEditor', bgc= [0.3, 0.25, 0.55], command = 'scripteditor()')
	mc.button(parent = rowLayoutF1, label = 'Rend.\nSett.', bgc= [0.55, 0.28, 0.62], command = 'rendersettings()')
############################################################################################
	mc.button(parent = rowLayoutF2, label = 'Graph\nEditor', bgc= [0.27, 0.25, 0.65], command = 'grapheditor()')
	mc.button(parent = rowLayoutF2, label = 'Node\nEditor', bgc= [0.27, 0.25, 0.65], command = 'nodeeditor()')
	mc.button(parent = rowLayoutF2, label = 'Attri..\nSpread..', bgc= [0.27, 0.25, 0.65], command = 'attspread()')
	mc.button(parent = rowLayoutF2, label = 'Light\nLink', bgc= [0.27, 0.25, 0.65], command = 'lightlink()')
	mc.button(parent = rowLayoutF2, label = 'Refer..\nEditor', bgc= [0.27, 0.25, 0.65], command = 'refeditor()')
	mc.button(parent = rowLayoutF2, label = 'RS Feed\nBack', bgc= [0.27, 0.25, 0.65], command = 'rsfeedback()')
############################################################################################
###############################################################################################################
###############################################################################################################
	mc.showWindow()

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
def cpyAtt():
	sel_b = mc.ls(selection=True)
	mc.copyAttr(sel_b[0],sel_b[1],values=True)
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
def matglass(): #Create Glass Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'glass_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 0)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matwater(): #Create Water Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'water_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 1)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matplastic(): #Create Plastic Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'plastic_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 2)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def mataluminium(): #Create Aluminium Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'aluminium_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 3)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matcopper(): #Create Copper Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'copper_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 4)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matgold(): #Create Gold Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'gold_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 5)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matiron(): #Create Iron Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'iron_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 6)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matlead(): #Create Lead Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'lead_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 7)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matplatinum(): #Create Platinum Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'platinum_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 8)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matsilver(): #Create Silver Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'silver_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 9)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matmilky(): #Create Milky Coffe Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'milkyCoffee_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 10)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matjade(): #Create Jade Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'jade_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 11)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matpaper(): #Create Paper Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'paper_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 12)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def mattinted(): #Create Tinder Glass Material and add it to selected object
	sel_a = mc.ls(selection=True)
	presetname = 'tintedglass_'
	input=presetname + sel_a[0]
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=input + '_S')
	mc.setAttr(input + '_S.refl_brdf', 1) #not working somehow
	mc.setAttr (input + '_S.preset', 13)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=input + '_SG')
	mc.connectAttr(input +'_S.outColor', input + '_SG.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=input + '_SG')
def matlambert():
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
	mc.shadingNode ('lambert', asShader=True, n=nam2 + '_#')
	sel_s = mc.ls(selection=True)
	mc.rename (sel_s[0], sel_s[0] + '_S')
	sel_inp = mc.ls(selection=True)
	inputs = sel_inp[0]
	mc.setAttr(inputs + '.color', rand1+randlist, rand2+randlist, ranD4+randlist)
	mc.setAttr(inputs + '.transparency', 0,0,0)
	mc.setAttr(inputs + '.diffuse', 1)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=inputs + 'G')
	mc.connectAttr(inputs + '.outColor', inputs + 'G.surfaceShader')
	mc.sets(sel_geo, edit=True, forceElement=inputs + 'G')
	mc.select (sel_geo[0])

def mat1():
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
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=nam2 + '_#')
	sel_s = mc.ls(selection=True)
	mc.rename (sel_s[0], sel_s[0] + '_S')
	sel_inp = mc.ls(selection=True)
	inputs = sel_inp[0]
	mc.setAttr(inputs + '.diffuse_color', rand1+randlist, rand2+randlist, ranD4+randlist)
	mc.setAttr(inputs + '.refl_brdf', 1)
	mc.setAttr(inputs + '.refl_weight', 0.1)
	mc.setAttr(inputs + '.refl_roughness', 0.20)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=inputs + 'G')
	mc.connectAttr(inputs + '.outColor', inputs + 'G.surfaceShader')
	mc.sets(sel_geo, edit=True, forceElement=inputs + 'G')
	mc.select (sel_geo[0])
def mat2():
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
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=nam2 + '_#')
	sel_s = mc.ls(selection=True)
	mc.rename (sel_s[0], sel_s[0] + '_S')
	sel_inp = mc.ls(selection=True)
	inputs = sel_inp[0]
	mc.setAttr(inputs + '.refl_brdf', 1)
	mc.setAttr(inputs + '.refl_weight', 0.15)
	mc.setAttr(inputs + '.refl_roughness', 0.15)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=inputs + 'G')
	mc.connectAttr(inputs + '.outColor', inputs + 'G.surfaceShader')
	#Create Fresnel Node and connect it to the material
	mc.shadingNode ('RedshiftFresnel', asUtility=True, n=sel_s[0])
	sel_f = mc.ls(selection=True)
	mc.rename (sel_f[0], sel_f[0] + '_fresnel')
	sel_fre = mc.ls(selection=True)
	mc.setAttr (sel_fre[0] + '.fresnel_useior', 0)
	mc.setAttr (sel_fre[0] + '.facing_color', rand1+randlist, rand2+randlist, ranD4+randlist)
	mc.setAttr (sel_fre[0] + '.perp_color', rand1-randlist, rand2-randlist, ranD4-randlist)
	mc.connectAttr( sel_fre[0] + '.outColor', inputs + '.diffuse_color' )
	mc.sets(sel_geo, edit=True, forceElement=inputs + 'G')
	mc.select (sel_geo[0])
def mat3():
	import random as random
	from random import uniform as rand
	sel_a = mc.ls(selection=True)
	input = sel_a[0]
	namo = input.replace('_geo', '')
	name = namo.replace('|', '')
	#DiffuseSettings
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=name + '_#')
	sel_s = mc.ls(selection=True)
	mc.rename (sel_s[0], sel_s[0] + '_S')
	sel_inp = mc.ls(selection=True)
	inputs = sel_inp[0]
	mc.setAttr (inputs + '.diffuse_weight', 0)
	mc.setAttr (inputs + '.refl_brdf', 1)
	mc.setAttr (inputs + '.refl_weight', 1)
	#reflRoughnessMapSettings
	mc.shadingNode( 'RedshiftNoise', asTexture=True, n=sel_s[0])
	sel_n = mc.ls(selection=True)
	mc.rename (sel_n[0], sel_n[0] + '_rsNoise')
	sel_noi = mc.ls(selection=True)
	mc.setAttr (sel_noi[0] + '.noise_type', 3)
	mc.setAttr (sel_noi[0] + '.noise_complexity', 5)
	mc.setAttr (sel_noi[0] + '.coord_scale_global', 20)
	mc.setAttr (sel_noi[0] + '.coord_scale0', 40)
	mc.setAttr (sel_noi[0] + '.coord_scale1', 1)
	mc.setAttr (sel_noi[0] + '.coord_scale2', 1)
	mc.connectAttr(sel_noi[0] + '.outColorR', inputs + '.refl_roughness' )
	#IORSettings
	mc.setAttr (inputs + '.refl_fresnel_mode', 1)
	mc.setAttr (inputs + '.refl_reflectivity', 0.005, 0.005, 0.005)
	#subsurfaceSettings
	mc.setAttr (inputs + '.ss_unitsMode', 1)
	mc.setAttr (inputs + '.ss_extinction_coeff', 0.33, 1.1, 0.93)
	mc.setAttr (inputs + '.ss_extinction_scale', 16)
	mc.setAttr (inputs + '.ss_scatter_coeff', 1.2, 0.51, 0.72)
	mc.setAttr (inputs + '.ss_amount', 16)
	mc.setAttr (inputs + '.ss_phase', 0.05)
	mc.setAttr (inputs + '.ss_samples', 64)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=inputs + 'G')
	mc.connectAttr(inputs + '.outColor', inputs + 'G.surfaceShader')
	mc.sets(sel_a, edit=True, forceElement=inputs + 'G')
def mat4():
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
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=nam2 + '_#')
	sel_s = mc.ls(selection=True)
	mc.rename (sel_s[0], sel_s[0] + '_S')
	sel_inp = mc.ls(selection=True)
	inputs = sel_inp[0]
	mc.setAttr(inputs + '.refl_brdf', 1)
	mc.setAttr(inputs + '.refl_weight', 0.15)
	mc.setAttr(inputs + '.refl_roughness', 0.15)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=inputs + 'G')
	mc.connectAttr(inputs + '.outColor', inputs + 'G.surfaceShader')
	#Create Fresnel Node and connect it to the material
	mc.shadingNode ('RedshiftFresnel', asUtility=True, n=sel_s[0])
	sel_f = mc.ls(selection=True)
	mc.rename (sel_f[0], sel_f[0] + '_fresnel')
	sel_fre = mc.ls(selection=True)
	mc.setAttr (sel_fre[0] + '.fresnel_useior', 0)
	mc.setAttr (sel_fre[0] + '.facing_color', rand1+randlist, rand2+randlist, ranD4+randlist)
	mc.setAttr (sel_fre[0] + '.perp_color', rand1-randlist, rand2-randlist, ranD4-randlist)
	mc.connectAttr( sel_fre[0] + '.outColor', inputs + '.diffuse_color' )
	mc.sets(sel_geo, edit=True, forceElement=inputs + 'G')
	mc.select (sel_geo[0])

	mc.setAttr (inputs + '.refl_fresnel_mode', 2)
	mc.shadingNode ('RedshiftRoundCorners', asShader=True, n=inputs + '_rsRoundCrnr')
	mc.shadingNode ('RedshiftBumpMap', asShader=True, n=inputs + '_rsBump')
	mc.shadingNode ('RedshiftBumpBlender', asShader=True, n=inputs + '_rsBumpBlend')
	mc.connectAttr(inputs + '_rsBump.out', inputs + '_rsBumpBlend.bumpInput0')
	mc.setAttr (inputs + '_rsBumpBlend.bumpWeight0', 1)
	mc.setAttr (inputs + '_rsBumpBlend.additive', 1)
	mc.connectAttr(inputs + '_rsRoundCrnr.out', inputs + '_rsBumpBlend.baseInput')
	mc.setAttr (inputs + '_rsBump.newrange_min', -0.4)
	mc.setAttr (inputs + '_rsBump.newrange_max', 0.4)
	mc.setAttr (inputs + '_rsBump.scale', 0.01)

	mc.connectAttr (inputs + '_rsBumpBlend.outColor', inputs + '.bump_input')

	mc.shadingNode('noise', asTexture=True)
	noise=mc.ls(selection=True)
	mc.shadingNode('place2dTexture', asUtility=True)
	noiseUV=mc.ls(selection=True)
	mc.connectAttr(noiseUV[0]+'.outUV', noise[0]+'.uvCoord')
	mc.connectAttr(noiseUV[0]+'.outUvFilterSize', noise[0]+'.uvFilterSize')
	mc.shadingNode ('RedshiftTriPlanar', asShader=True, n=inputs + '_rsTripl')
	mc.connectAttr(noise[0] + '.outColor', inputs + '_rsTripl.imageX')
	mc.connectAttr(inputs + '_rsTripl.outColor', inputs + '_rsBump.input')
	mc.setAttr(inputs + '_rsTripl.scale0', 0.1)
	mc.setAttr(inputs + '_rsTripl.scale1', 0.1)
	mc.setAttr(inputs + '_rsTripl.scale2', 0.1)

def mat5():
	#Create matte Shadow catcher for toonShader purposes
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
	mc.shadingNode ('RedshiftMatteShadowCatcher', asShader=True, n=nam2 + 'matte' + '_#')
	sel_shader = mc.ls(selection=True)
	mc.setAttr(sel_shader[0] + '.background', rand1+randlist, rand2+randlist, ranD4+randlist)
	mc.setAttr(sel_shader[0] + '.catch_shadows', 1)
	mc.setAttr(sel_shader[0] + '.ambient', 1,1,1)
	mc.setAttr(sel_shader[0] + '.shadows', rand1+randlist, rand2+randlist, ranD4+randlist)
	mc.setAttr(sel_shader[0] + '.ao_on', 1)
	mc.setAttr(sel_shader[0] + '.ao_distance', 2)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=sel_shader[0] + 'G')
	mc.connectAttr(sel_shader[0] + '.outColor', sel_shader[0] + 'G.surfaceShader')
	for i in range(len(sel_geo)):
		mc.sets(sel_geo[i], edit=True, forceElement=sel_shader[0] + 'G')

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
def unprimvis():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.primaryVisibility', 0)
def primvis():
	sel = mc.ls(selection=True)
	for i in sel:
		mc.setAttr (i+'.primaryVisibility', 1)

def pbrd():
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
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=nam2 + '_#')
	sel_s = mc.ls(selection=True)
	mc.rename (sel_s[0], sel_s[0] + '_S')
	sel_inp = mc.ls(selection=True)
	inputs = sel_inp[0]
	mc.setAttr(inputs + '.diffuse_color', rand1+randlist, rand2+randlist, ranD4+randlist)
	mc.setAttr(inputs + '.refl_brdf', 1)
	mc.setAttr(inputs + '.refl_weight', 0)
	mc.setAttr(inputs + '.refl_roughness', 0)
	mc.setAttr(inputs + '.refl_fresnel_mode', 2)
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
	mc.connectAttr(sel_math3[0] + '.outFloat', inputs + '.refl_reflectivityR')
	mc.connectAttr(sel_math3[0] + '.outFloat', inputs + '.refl_reflectivityG')
	mc.connectAttr(sel_math3[0] + '.outFloat', inputs + '.refl_reflectivityB')

	mc.connectAttr(sel_math3[0] + '.outFloat', sel_math1[0] + '.floatB')
	mc.connectAttr(sel_math1[0] + '.outFloat', inputs + '.diffuse_weight')

	mc.connectAttr(inputs + '.refl_roughness', inputs + '.diffuse_roughness')

	mc.select (sel_geo[0])

def pbrm():
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
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=nam2 + '_#')
	sel_s = mc.ls(selection=True)
	mc.rename (sel_s[0], sel_s[0] + '_S')
	sel_inp = mc.ls(selection=True)
	inputs = sel_inp[0]
	mc.setAttr(inputs + '.diffuse_color', rand1+randlist, rand2+randlist, ranD4+randlist)
	mc.setAttr(inputs + '.refl_brdf', 1)
	mc.setAttr(inputs + '.refl_weight', 0)
	mc.setAttr(inputs + '.refl_roughness', 0)
	mc.setAttr(inputs + '.refl_fresnel_mode', 2)
	mc.setAttr(inputs + '.refl_metalness', 1)
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
	mc.connectAttr(sel_math3[0] + '.outFloat', inputs + '.refl_reflectivityR')
	mc.connectAttr(sel_math3[0] + '.outFloat', inputs + '.refl_reflectivityG')
	mc.connectAttr(sel_math3[0] + '.outFloat', inputs + '.refl_reflectivityB')

	mc.connectAttr(sel_math3[0] + '.outFloat', sel_math1[0] + '.floatB')
	mc.connectAttr(sel_math1[0] + '.outFloat', inputs + '.diffuse_weight')

	mc.connectAttr(inputs + '.refl_roughness', inputs + '.diffuse_roughness')

	mc.shadingNode ('RedshiftFresnel', asUtility=True, n=inputs + '_fresnel')
	sel_fres2 = mc.ls(selection=True)
	mc.setAttr (sel_fres2[0] + '.correct_intensity', 0)
	mc.setAttr (sel_fres2[0] + '.facing_color', 1, 0.766, 0.366)
	mc.setAttr (sel_fres2[0] + '.perp_color', 1, 0.135, 0.135)
	mc.connectAttr(sel_fres2[0] + '.outColor', inputs + '.diffuse_color')
	mc.select (sel_geo[0])

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
def aces():
	ws = mc.colorManagementPrefs(q=True, renderingSpaceName=True)
	mc.colorManagementPrefs(e=True, viewTransformName="Log")
	renderingSpaces = mc.colorManagementPrefs(q=True, renderingSpaceNames=True)
	viewingTransforms = mc.colorManagementPrefs(q=True, viewTransformNames=True)
	mc.colorManagementPrefs(e=True, configFilePath="C:/Users/er/Documents/OpenColorIO-Configs-feature-aces-1.2-config/aces_1.2/config.ocio")
	mc.colorManagementPrefs(e=True, cmConfigFileEnabled=True)
def group():
	sel = mc.ls(selection=True)
	mc.group (sel, name=sel[0] + '_grp')
	sel = mc.ls(selection=True)
	temp = sel[0].replace('_geo', '')
	mc.rename (sel[0], temp)

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
	input = mc.textField(field2, text = True, query = True)
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		selnode = mc.ls(selection=True, type='shadingEngine')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_sg')
		selnode = mc.ls(selection=True, type='RedshiftMaterial')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_s')
		selnode = mc.ls(selection=True, type='RedshiftMaterialBlender')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsMatBlend')
		selnode = mc.ls(selection=True, type='RedshiftDisplacement')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsDispl')
		selnode = mc.ls(selection=True, type='RedshiftDisplacementBlender')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsDisplBlend')
		selnode = mc.ls(selection=True, type='RedshiftBumpMap')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsBump')
		selnode = mc.ls(selection=True, type='RedshiftBumpBlender')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsBumpBlend')
		selnode = mc.ls(selection=True, type='RedshiftFresnel')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_fresnel')
		selnode = mc.ls(selection=True, type='RedshiftColorLayer')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsClrLyr')
		selnode = mc.ls(selection=True, type='RedshiftColorCorrection')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsCC')
		selnode = mc.ls(selection=True, type='cloth')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_cloth')
		selnode = mc.ls(selection=True, type='place2dTexture')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_place2dTexture')
		selnode = mc.ls(selection=True, type='RedshiftAmbientOcclusion')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsAO')
		selnode = mc.ls(selection=True, type='RedshiftCurvature')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsCurv')
		selnode = mc.ls(selection=True, type='RedshiftTriPlanar')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsTripl')
		selnode = mc.ls(selection=True, type='file')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_file')
		selnode = mc.ls(selection=True, type='RedshiftNoise')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsNoi')
		selnode = mc.ls(selection=True, type='remapHsv')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rmphsv')
		selnode = mc.ls(selection=True, type='ramp')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_ramp')
		selnode = mc.ls(selection=True, type='fractal')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_fractal')
		selnode = mc.ls(selection=True, type='noise')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_noi')
		selnode = mc.ls(selection=True, type='layeredTexture')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_layTex')
		selnode = mc.ls(selection=True, type='checker')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_checker')
		selnode = mc.ls(selection=True, type='blendColors')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_blClr')
		selnode = mc.ls(selection=True, type='reverse')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rvrs')
		selnode = mc.ls(selection=True, type='remapColor')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rmpclr')
		selnode = mc.ls(selection=True, type='floatConstant')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_fltConst')
		selnode = mc.ls(selection=True, type='RedshiftRaySwitch')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsRaySwt')
		selnode = mc.ls(selection=True, type='RedshiftSprite')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsSprite')
		selnode = mc.ls(selection=True, type='substanceNode')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_substance')
		selnode = mc.ls(selection=True, type='substanceOutputNode')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_substanceOutput')
		selnode = mc.ls(selection=True, type='multiplyDivide')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_multiplyDivide')
		selnode = mc.ls(selection=True, type='projection')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_projection')
		selnode = mc.ls(selection=True, type='RedshiftRoundCorners')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsRoundCrnr')
		selnode = mc.ls(selection=True, type='lambert')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_lambert_S')
		selnode = mc.ls(selection=True, type='samplerInfo')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_SInfo')
		selnode = mc.ls(selection=True, type='floatMath')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_floatMath')
		selnode = mc.ls(selection=True, type='RedshiftIncandescent')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsIncd')
		selnode = mc.ls(selection=True, type='RedshiftMaxonNoise')
		for y in range(len(selnode)):
			mc.rename (selnode[y], input + '_' + str(y+1) + '_rsMaxon')
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
def addgeo():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_geo')
def addgrp():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_grp')
def addlow():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_low')
def addhigh():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_high')
def addlgt():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_lgt')
def addoff():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_off')
def adddiff():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_diff')
def addemis():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_emis')
def addrefl():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_refl')
def addrefr():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_refr')
def addopa():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_opa')
def addloc():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_loc')
def addcolor():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + 'Color')
def addwght():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + 'Wght')
def addrghn():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + 'Rghn')
def addcoat():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + 'Coat')
def addsdk():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_sdk')
def addS():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_S')
def addSG():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_SG')
def addL():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_L')
def addR():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_R')
def addtop():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_top')
def addmid():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_mid')
def addbot():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_bot')
def addA():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_A')
def addB():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_B')
def addC():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_C')
def addD():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_D')
def addE():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_E')
def addF():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_F')
def addG():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_G')
def addH():
	sel = mc.ls(selection=True)
	for i in range(len(sel)):
		mc.rename (sel[i], sel[i].split('|', 1)[-1] + '_H')
def redshift():
	mc.loadPlugin( 'redshift4maya.mll')
	mc.setAttr("defaultRenderGlobals.currentRenderer", "redshift", type="string")
def fnrender():
	mc.currentUnit(time='pal')#(25 fps)
	mc.setAttr("redshiftOptions.exrForceMultilayer", 1)
	mc.setAttr("redshiftOptions.autocrop", 0)
	mc.setAttr("redshiftOptions.imageFormat", 1)
	mc.setAttr("redshiftOptions.exrCompression", 4)
	mc.setAttr("defaultRenderGlobals.animation", 1)
	mc.setAttr('redshiftOptions.unifiedMinSamples', 16)
	mc.setAttr('redshiftOptions.unifiedMaxSamples', 128)
	mc.setAttr('redshiftOptions.unifiedAdaptiveErrorThreshold', 0.01)
	minTime = mc.playbackOptions (q=True, minTime=True)
	maxTime = mc.playbackOptions (q=True, maxTime=True)
	mc.setAttr ('defaultRenderGlobals.startFrame', minTime)
	mc.setAttr ('defaultRenderGlobals.endFrame', maxTime)
	filename=mc.file(q=1,sn=1,shn=1)
	buffer = filename.split('_')
	rpath = buffer[0] + '\\''render3d''\\' + buffer[0] + '_' + buffer[1] + '\\' + buffer[0] + '_' + buffer[1] + '_render3d'
	mc.setAttr('defaultRenderGlobals.imageFilePrefix', rpath, type='string')
	mc.setAttr("redshiftOptions.unifiedFilterType", 2)
	mc.setAttr("redshiftOptions.unifiedFilterSize", 2)
	mc.setAttr("redshiftOptions.unifiedMaxOverbright", 1)
	mc.setAttr("redshiftOptions.glossyRayMaxOverbright", 1)
	mc.setAttr("defaultRenderGlobals.byFrameStep", 1)
	mc.setAttr('defaultResolution.height', 1080)
	mc.setAttr('defaultResolution.width', 1920)
	mc.setAttr('defaultResolution.lockDeviceAspectRatio', 0)
	mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
	mc.setAttr('defaultResolution.pixelAspect', 1)
	mc.setAttr('redshiftOptions.reflectionMaxTraceDepth', 2)
	mc.setAttr('redshiftOptions.refractionMaxTraceDepth', 4)
	mc.setAttr('redshiftOptions.combinedMaxTraceDepth', 3)
	mc.setAttr('redshiftOptions.primaryGIEngine', 4)
	mc.setAttr("redshiftOptions.secondaryGIEngine", 2)
	mc.setAttr("redshiftOptions.numGIBounces", 4)
	mc.setAttr('redshiftOptions.bruteForceGINumRays', 256)
	mc.setAttr('redshiftOptions.subsurfaceScatteringRate', -2)
	mc.setAttr('redshiftOptions.bucketSize', 256)
	##### AOV DISABLER START #####
	mc.select (clear=True)
	aov4=mc.ls('*:*:*:*:rsAov*')
	aov3=mc.ls('*:*:*:rsAov*')
	aov2=mc.ls('*:*:rsAov*')
	aov1=mc.ls('*:rsAov*')
	aov=mc.ls('*rsAov*')
	mc.select (clear=True)
	mc.select (aov, add=True)
	mc.select (aov1, add=True)
	mc.select (aov2, add=True)
	mc.select (aov3, add=True)
	mc.select (aov4, add=True)
	fullaov=mc.ls(selection=True)
	for i in range(len(fullaov)):
		try:
			mc.disconnectAttr(fullaov[i] + '_enabled.output', fullaov[i] + '.enabled')
		except:pass
		try:
			   mc.setAttr(fullaov[i] + '.enabled', 0)
		except:pass
		try:
			   mc.setKeyframe( fullaov[i]+'.enabled' )
		except:pass
		try:
			   mc.delete(fullaov[i])
		except:pass
	mc.select (clear=True) ##### AOV DISABLER END #####
def fn4render():
	mc.currentUnit(time='pal')#(25 fps)
	mc.setAttr("redshiftOptions.exrForceMultilayer", 1)
	mc.setAttr("redshiftOptions.autocrop", 0)
	mc.setAttr("redshiftOptions.imageFormat", 1)
	mc.setAttr("redshiftOptions.exrCompression", 4)
	mc.setAttr("defaultRenderGlobals.animation", 1)
	mc.setAttr('redshiftOptions.unifiedMinSamples', 16)
	mc.setAttr('redshiftOptions.unifiedMaxSamples', 128)
	mc.setAttr('redshiftOptions.unifiedAdaptiveErrorThreshold', 0.01)
	minTime = mc.playbackOptions (q=True, minTime=True)
	maxTime = mc.playbackOptions (q=True, maxTime=True)
	mc.setAttr ('defaultRenderGlobals.startFrame', minTime)
	mc.setAttr ('defaultRenderGlobals.endFrame', maxTime)
	filename=mc.file(q=1,sn=1,shn=1)
	buffer = filename.split('_')
	rpath = '..\\..\\' 'season04\\render\\' + buffer[0] + '\\''render3d''\\' + buffer[0] + '_' + buffer[1] + '\\' + buffer[0] + '_' + buffer[1] + '_render3d'
	mc.setAttr('defaultRenderGlobals.imageFilePrefix', rpath, type='string')
	mc.setAttr("redshiftOptions.unifiedFilterType", 2)
	mc.setAttr("redshiftOptions.unifiedFilterSize", 2)
	mc.setAttr("redshiftOptions.unifiedMaxOverbright", 1)
	mc.setAttr("redshiftOptions.glossyRayMaxOverbright", 1)
	mc.setAttr("defaultRenderGlobals.byFrameStep", 1)
	mc.setAttr('defaultResolution.height', 1080)
	mc.setAttr('defaultResolution.width', 1920)
	mc.setAttr('defaultResolution.lockDeviceAspectRatio', 0)
	mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
	mc.setAttr('defaultResolution.pixelAspect', 1)
	mc.setAttr('redshiftOptions.reflectionMaxTraceDepth', 2)
	mc.setAttr('redshiftOptions.refractionMaxTraceDepth', 4)
	mc.setAttr('redshiftOptions.combinedMaxTraceDepth', 3)
	mc.setAttr('redshiftOptions.primaryGIEngine', 4)
	mc.setAttr("redshiftOptions.secondaryGIEngine", 2)
	mc.setAttr("redshiftOptions.numGIBounces", 4)
	mc.setAttr('redshiftOptions.bruteForceGINumRays', 256)
	mc.setAttr('redshiftOptions.subsurfaceScatteringRate', -2)
	mc.setAttr('redshiftOptions.bucketSize', 256)
	##### AOV DISABLER START #####
	mc.select (clear=True)
	aov4=mc.ls('*:*:*:*:rsAov*')
	aov3=mc.ls('*:*:*:rsAov*')
	aov2=mc.ls('*:*:rsAov*')
	aov1=mc.ls('*:rsAov*')
	aov=mc.ls('*rsAov*')
	mc.select (clear=True)
	mc.select (aov, add=True)
	mc.select (aov1, add=True)
	mc.select (aov2, add=True)
	mc.select (aov3, add=True)
	mc.select (aov4, add=True)
	fullaov=mc.ls(selection=True)
	for i in range(len(fullaov)):
		try:
			mc.disconnectAttr(fullaov[i] + '_enabled.output', fullaov[i] + '.enabled')
		except:pass
		try:
			   mc.setAttr(fullaov[i] + '.enabled', 0)
		except:pass
		try:
			   mc.setKeyframe( fullaov[i]+'.enabled' )
		except:pass
		try:
			   mc.delete(fullaov[i])
		except:pass
	mc.select (clear=True) ##### AOV DISABLER END #####
def prerender():
	mc.currentUnit(time='pal')#(25 fps)
	mc.setAttr("redshiftOptions.exrForceMultilayer", 1)
	mc.setAttr("redshiftOptions.autocrop", 0)
	mc.setAttr("redshiftOptions.imageFormat", 1)
	mc.setAttr("redshiftOptions.exrCompression", 4)
	mc.setAttr("defaultRenderGlobals.animation", 1)
	mc.setAttr('redshiftOptions.unifiedMinSamples', 8)
	mc.setAttr('redshiftOptions.unifiedMaxSamples', 64)
	mc.setAttr('redshiftOptions.unifiedAdaptiveErrorThreshold', 0.01)
	minTime = mc.playbackOptions (q=True, minTime=True)
	maxTime = mc.playbackOptions (q=True, maxTime=True)
	mc.setAttr ('defaultRenderGlobals.startFrame', minTime)
	mc.setAttr ('defaultRenderGlobals.endFrame', maxTime)
	filename=mc.file(q=1,sn=1,shn=1)
	buffer = filename.split('_')
	rpath = buffer[0] + '\\''render3d''\\' + buffer[0] + '_' + buffer[1] + '\\' + buffer[0] + '_' + buffer[1] + '_render3d'
	mc.setAttr('defaultRenderGlobals.imageFilePrefix', rpath, type='string')
	mc.setAttr("redshiftOptions.unifiedFilterType", 2)
	mc.setAttr("redshiftOptions.unifiedFilterSize", 2)
	mc.setAttr("redshiftOptions.unifiedMaxOverbright", 1)
	mc.setAttr("redshiftOptions.glossyRayMaxOverbright", 1)
	mc.setAttr("defaultRenderGlobals.byFrameStep", 10)
	mc.setAttr('defaultResolution.height', 720)
	mc.setAttr('defaultResolution.width', 1280)
	mc.setAttr('defaultResolution.lockDeviceAspectRatio', 0)
	mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
	mc.setAttr('defaultResolution.pixelAspect', 1)
	mc.setAttr('redshiftOptions.reflectionMaxTraceDepth', 2)
	mc.setAttr('redshiftOptions.refractionMaxTraceDepth', 4)
	mc.setAttr('redshiftOptions.combinedMaxTraceDepth', 3)
	mc.setAttr('redshiftOptions.primaryGIEngine', 4)
	mc.setAttr("redshiftOptions.secondaryGIEngine", 2)
	mc.setAttr("redshiftOptions.numGIBounces", 4)
	mc.setAttr('redshiftOptions.bruteForceGINumRays', 64)
	mc.setAttr('redshiftOptions.subsurfaceScatteringRate', -2)
	mc.setAttr('redshiftOptions.bucketSize', 256)
	##### AOV DISABLER START #####
	mc.select (clear=True)
	aov4=mc.ls('*:*:*:*:rsAov*')
	aov3=mc.ls('*:*:*:rsAov*')
	aov2=mc.ls('*:*:rsAov*')
	aov1=mc.ls('*:rsAov*')
	aov=mc.ls('*rsAov*')
	mc.select (clear=True)
	mc.select (aov, add=True)
	mc.select (aov1, add=True)
	mc.select (aov2, add=True)
	mc.select (aov3, add=True)
	mc.select (aov4, add=True)
	fullaov=mc.ls(selection=True)
	for i in range(len(fullaov)):
		try:
			mc.disconnectAttr(fullaov[i] + '_enabled.output', fullaov[i] + '.enabled')
		except:pass
		try:
			   mc.setAttr(fullaov[i] + '.enabled', 0)
		except:pass
		try:
			   mc.setKeyframe( fullaov[i]+'.enabled' )
		except:pass
		try:
			   mc.delete(fullaov[i])
		except:pass
	mc.select (clear=True) ##### AOV DISABLER END #####
def pre4render():
	mc.currentUnit(time='pal')#(25 fps)
	mc.setAttr("redshiftOptions.exrForceMultilayer", 1)
	mc.setAttr("redshiftOptions.autocrop", 0)
	mc.setAttr("redshiftOptions.imageFormat", 1)
	mc.setAttr("redshiftOptions.exrCompression", 4)
	mc.setAttr("defaultRenderGlobals.animation", 1)
	mc.setAttr('redshiftOptions.unifiedMinSamples', 8)
	mc.setAttr('redshiftOptions.unifiedMaxSamples', 64)
	mc.setAttr('redshiftOptions.unifiedAdaptiveErrorThreshold', 0.01)
	minTime = mc.playbackOptions (q=True, minTime=True)
	maxTime = mc.playbackOptions (q=True, maxTime=True)
	mc.setAttr ('defaultRenderGlobals.startFrame', minTime)
	mc.setAttr ('defaultRenderGlobals.endFrame', maxTime)
	filename=mc.file(q=1,sn=1,shn=1)
	buffer = filename.split('_')
	rpath = '..\\..\\' 'season04\\render\\' + buffer[0] + '\\''render3d''\\' + buffer[0] + '_' + buffer[1] + '\\' + buffer[0] + '_' + buffer[1] + '_render3d'
	mc.setAttr('defaultRenderGlobals.imageFilePrefix', rpath, type='string')
	mc.setAttr("redshiftOptions.unifiedFilterType", 2)
	mc.setAttr("redshiftOptions.unifiedFilterSize", 2)
	mc.setAttr("redshiftOptions.unifiedMaxOverbright", 1)
	mc.setAttr("redshiftOptions.glossyRayMaxOverbright", 1)
	mc.setAttr("defaultRenderGlobals.byFrameStep", 10)
	mc.setAttr('defaultResolution.height', 720)
	mc.setAttr('defaultResolution.width', 1280)
	mc.setAttr('defaultResolution.lockDeviceAspectRatio', 0)
	mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
	mc.setAttr('defaultResolution.pixelAspect', 1)
	mc.setAttr('redshiftOptions.reflectionMaxTraceDepth', 2)
	mc.setAttr('redshiftOptions.refractionMaxTraceDepth', 4)
	mc.setAttr('redshiftOptions.combinedMaxTraceDepth', 3)
	mc.setAttr('redshiftOptions.primaryGIEngine', 4)
	mc.setAttr("redshiftOptions.secondaryGIEngine", 2)
	mc.setAttr("redshiftOptions.numGIBounces", 4)
	mc.setAttr('redshiftOptions.bruteForceGINumRays', 64)
	mc.setAttr('redshiftOptions.subsurfaceScatteringRate', -2)
	mc.setAttr('redshiftOptions.bucketSize', 256)
	##### AOV DISABLER START #####
	mc.select (clear=True)
	aov4=mc.ls('*:*:*:*:rsAov*')
	aov3=mc.ls('*:*:*:rsAov*')
	aov2=mc.ls('*:*:rsAov*')
	aov1=mc.ls('*:rsAov*')
	aov=mc.ls('*rsAov*')
	mc.select (clear=True)
	mc.select (aov, add=True)
	mc.select (aov1, add=True)
	mc.select (aov2, add=True)
	mc.select (aov3, add=True)
	mc.select (aov4, add=True)
	fullaov=mc.ls(selection=True)
	for i in range(len(fullaov)):
		try:
			mc.disconnectAttr(fullaov[i] + '_enabled.output', fullaov[i] + '.enabled')
		except:pass
		try:
			   mc.setAttr(fullaov[i] + '.enabled', 0)
		except:pass
		try:
			   mc.setKeyframe( fullaov[i]+'.enabled' )
		except:pass
		try:
			   mc.delete(fullaov[i])
		except:pass
	mc.select (clear=True) ##### AOV DISABLER END #####
def oneframerender():
	mc.currentUnit(time='pal')#(25 fps)
	mc.setAttr("redshiftOptions.exrForceMultilayer", 1)
	mc.setAttr("redshiftOptions.autocrop", 0)
	mc.setAttr("redshiftOptions.imageFormat", 1)
	mc.setAttr("redshiftOptions.exrCompression", 4)
	mc.setAttr("defaultRenderGlobals.animation", 1)
	mc.setAttr('redshiftOptions.unifiedMinSamples', 16)
	mc.setAttr('redshiftOptions.unifiedMaxSamples', 128)
	mc.setAttr('redshiftOptions.unifiedAdaptiveErrorThreshold', 0.01)
	minTime = mc.playbackOptions (q=True, minTime=True)
	maxTime = mc.playbackOptions (q=True, maxTime=True)
	mc.setAttr ('defaultRenderGlobals.startFrame', minTime)
	mc.setAttr ('defaultRenderGlobals.endFrame', maxTime)
	filename=mc.file(q=1,sn=1,shn=1)
	buffer = filename.split('_')
	rpath = buffer[0] + '\\''render3d''\\' + buffer[0] + '_' + buffer[1] + '\\' + buffer[0] + '_' + buffer[1] + '_render3d'
	mc.setAttr('defaultRenderGlobals.imageFilePrefix', rpath, type='string')
	mc.setAttr("redshiftOptions.unifiedFilterType", 2)
	mc.setAttr("redshiftOptions.unifiedFilterSize", 2)
	mc.setAttr("redshiftOptions.unifiedMaxOverbright", 1)
	mc.setAttr("redshiftOptions.glossyRayMaxOverbright", 1)
	mc.setAttr("defaultRenderGlobals.byFrameStep", 1)
	mc.setAttr('defaultResolution.height', 540)
	mc.setAttr('defaultResolution.width', 960)
	mc.setAttr('defaultResolution.lockDeviceAspectRatio', 0)
	mc.setAttr('defaultResolution.deviceAspectRatio', 1.777)
	mc.setAttr('defaultResolution.pixelAspect', 1)
	mc.setAttr('redshiftOptions.reflectionMaxTraceDepth', 2)
	mc.setAttr('redshiftOptions.refractionMaxTraceDepth', 4)
	mc.setAttr('redshiftOptions.combinedMaxTraceDepth', 3)
	mc.setAttr('redshiftOptions.primaryGIEngine', 4)
	mc.setAttr("redshiftOptions.secondaryGIEngine", 2)
	mc.setAttr("redshiftOptions.numGIBounces", 4)
	mc.setAttr('redshiftOptions.bruteForceGINumRays', 256)
	mc.setAttr('redshiftOptions.subsurfaceScatteringRate', -2)
	mc.setAttr('redshiftOptions.bucketSize', 256)
	##### AOV DISABLER START #####
	mc.select (clear=True)
	aov4=mc.ls('*:*:*:*:rsAov*')
	aov3=mc.ls('*:*:*:rsAov*')
	aov2=mc.ls('*:*:rsAov*')
	aov1=mc.ls('*:rsAov*')
	aov=mc.ls('*rsAov*')
	mc.select (clear=True)
	mc.select (aov, add=True)
	mc.select (aov1, add=True)
	mc.select (aov2, add=True)
	mc.select (aov3, add=True)
	mc.select (aov4, add=True)
	fullaov=mc.ls(selection=True)
	for i in range(len(fullaov)):
		try:
			mc.disconnectAttr(fullaov[i] + '_enabled.output', fullaov[i] + '.enabled')
		except:pass
		try:
			   mc.setAttr(fullaov[i] + '.enabled', 0)
		except:pass
		try:
			   mc.setKeyframe( fullaov[i]+'.enabled' )
		except:pass
		try:
			   mc.delete(fullaov[i])
		except:pass
	mc.select (clear=True) ##### AOV DISABLER END #####
def domelgt(): ##################################### Dome light creation
	mel.eval('redshiftCreateDomeLight;')
	list=mc.ls(selection=True)
	mc.rename (list[0], 'dome_#')
	list2=mc.ls(selection=True)
	mc.setAttr(list2[0]+'.scaleX', 30)
	mc.setAttr(list2[0]+'.scaleY', 30)
	mc.setAttr(list2[0]+'.scaleZ', 30)
	mc.setAttr(list2[0]+'.volumeRayContributionScale', 0)
	mc.setAttr(list2[0]+'.volumeNumSamples', 64)
	mc.setAttr(list2[0]+'.background_enable', 0)
	mc.setAttr(list2[0]+'.tex0', 'D:/zorttirik', type='string')
def arealgt(): ##################################### Area light creation
	mel.eval('redshiftCreateLight "RedshiftPhysicalLight";')
	list=mc.ls(selection=True)
	mc.rename (list[0], 'area_#')
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
	mc.setAttr(list2[0]+'.intensity', 1500)
def pointlgt(): ##################################### Point light creation
	mel.eval('redshiftCreateLight "RedshiftPhysicalLight";')
	list=mc.ls(selection=True)
	mc.rename (list[0], 'point_#')
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
	mc.setAttr(list2[0]+'.intensity', 1500)
def spotlgt(): ##################################### Spot light creation
	mel.eval('redshiftCreateLight "RedshiftPhysicalLight";')
	list=mc.ls(selection=True)
	mc.rename (list[0], 'spot_#')
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
	mc.setAttr(list2[0]+'.intensity', 1500)
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
def x1080x1920():
	mc.setAttr("defaultResolution.height", 1080)
	mc.setAttr("defaultResolution.width", 1920)
def x720x1280():
	mc.setAttr("defaultResolution.height", 720)
	mc.setAttr("defaultResolution.width", 1280)
def x540x948():
	mc.setAttr("defaultResolution.height", 540)
	mc.setAttr("defaultResolution.width", 948)
def x1080x1080():
	mc.setAttr("defaultResolution.height", 1080)
	mc.setAttr("defaultResolution.width", 1080)
def x1080x1350():
	mc.setAttr("defaultResolution.height", 1350)
	mc.setAttr("defaultResolution.width", 1080)
def x2148x3840():
	mc.setAttr("defaultResolution.height", 2148)
	mc.setAttr("defaultResolution.width", 3840)
def showjoint():
	for i in range(1, 9):
		try:
			query = mc.modelEditor('modelPanel'+str(i), query=True, joints=1)
			if query==True:
				mc.modelEditor('modelPanel'+str(i), edit=True, joints=0)
			else:
				mc.modelEditor('modelPanel'+str(i), edit=True, joints=1)
		except:
			print 'modelPanel' + str(i) + ' not found'
def showpoly():
	for i in range(1, 9):
		try:
			query = mc.modelEditor('modelPanel'+str(i), query=True, polymeshes=1)
			if query==True:
				mc.modelEditor('modelPanel'+str(i), edit=True, polymeshes=0)
			else:
				mc.modelEditor('modelPanel'+str(i), edit=True, polymeshes=1)
		except:
			print 'modelPanel' + str(i) + ' not found'
def showcurve():
	for i in range(1, 9):
		try:
			query = mc.modelEditor('modelPanel'+str(i), query=True, nurbsCurves=1)
			if query==True:
				mc.modelEditor('modelPanel'+str(i), edit=True, nurbsCurves=0)
			else:
				mc.modelEditor('modelPanel'+str(i), edit=True, nurbsCurves=1)
		except:
			print 'modelPanel' + str(i) + ' not found'
def showlight():
	for i in range(1, 9):
		try:
			query = mc.modelEditor('modelPanel'+str(i), query=True, lights=1)
			if query==True:
				mc.modelEditor('modelPanel'+str(i), edit=True, lights=0)
			else:
				mc.modelEditor('modelPanel'+str(i), edit=True, lights=1)
		except:
			print 'modelPanel' + str(i) + ' not found'
def showcam():
	for i in range(1, 9):
		try:
			query = mc.modelEditor('modelPanel'+str(i), query=True, cameras=1)
			if query==True:
				mc.modelEditor('modelPanel'+str(i), edit=True, cameras=0)
			else:
				mc.modelEditor('modelPanel'+str(i), edit=True, cameras=1)
		except:
			print 'modelPanel' + str(i) + ' not found'
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
			print 'modelPanel' + str(i) + ' not found'

#try except pass example:#	for i in ref:
#try except pass example:#		mc.select(clear=True)
#try except pass example:#		try:
#try except pass example:#			mc.select (i+'dumper_r_f_tire_part_11_loGeo1.f[0:17777]', r=True)
#try except pass example:#		except:pass

def optscene():
	# Source cleanUpScene.mel
	# to make scOpt_performOneCleanup available
	import pymel.core as pm
	pm.mel.source('cleanUpScene')
	pm.mel.scOpt_performOneCleanup({'setsOption','partitionOption','transformOption',
	'displayLayerOption','renderLayerOption','animationCurveOption','clipOption',
	'poseOption','nurbsSrfOption','deformerOption','unusedSkinInfsOption','groupIDnOption',
	'ptConOption','pbOption','snapshotOption','unitConversionOption','referencedOption',
	'brushOption','shaderOption','unknownNodesOption','shadingNetworksOption'})
	#______cleanup custom python_____________________
	geometry = mc.ls(geometry=True)
	#transforms = mc.listRelatives(geometry, p=True, path=True)
	#mc.select(geometry, r=True)
	if range(len(geometry)) > 0:
		mc.loadPlugin( 'redshift4maya.mll')
		mc.setAttr("defaultRenderGlobals.currentRenderer", "redshift", type="string")
		sel1 = mc.ls('*rnold*')
		for i in sel1:
			mc.delete(sel1)
		sel2 = mc.ls('*urtle*')
		for i in sel2:
			mc.delete(sel2)
		sel3 = mc.ls('*brush*', type='brush')
		for i in sel3:
			mc.delete(sel3)
		mc.select(clear=True)
		sel4 = mc.ls('*poly*')
		sel5 = mc.ls('place2*')
		sel6 = mc.ls('ramp*')
		sel7 = mc.ls('file*')
		mc.select(sel4)
		mc.select(sel5, add=True)
		mc.select(sel6, add=True)
		mc.select(sel7, add=True)
		print(sel)
		mc.bakePartialHistory(geometry)#nonDeformerBake
	else:
		mc.bakePartialHistory(geometry)#nonDeformerBake
def turtlekill():
	unlockError = False
	nodes = mc.ls()
	for node in nodes:
		lockStatus = mc.lockNode( node, q=True )
		for response in lockStatus:
			if response != False:
				try:
					mc.lockNode( node, lock=False )
					print 'Unlocked: ' + node
					mc.delete(nodes)
				except:
					print 'Error: Could not unlock ' + node
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
	print listatm[0]
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
	#createRedshiftMaterial
	mc.shadingNode ('RedshiftMaterial', asShader=True, name=checker[0]+'_S')
	mc.setAttr(checker[0] + '_S.refl_brdf', 1)
	mc.setAttr(checker[0] + '_S.refl_weight', 0.0)
	mc.setAttr(checker[0] + '_S.refl_roughness', 0.0)
	mc.sets( renderable=True, noSurfaceShader=True, empty=True, name=checker[0]+ '_SG')
	mc.connectAttr(checker[0]+'_S.outColor', checker[0]+'_SG.surfaceShader')
	mc.connectAttr(checker[0]+'.outColor', checker[0]+'_S.diffuse_color')
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
				print cams[i]
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
	mc.shadingNode ('RedshiftMaterial', asShader=True, n=lightblock[0] + '_S')
	sel_shader = mc.ls(selection=True)
	mc.setAttr(sel_shader[0] + '.diffuse_weight', 0)
	mc.setAttr(sel_shader[0] + '.refl_brdf', 1)
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
def translate():
	import random as random
	from random import uniform as rand
	sel = mc.ls(selection=True)
	for i in sel:
		randomvalue = rand(-0.3,0.3)
		getx = mc.getAttr(i+".tx")
		gety = mc.getAttr(i+".ty")
		getz = mc.getAttr(i+".tz")
		mc.setAttr(i+".tx", getx + randomvalue)
		mc.setAttr(i+".ty", gety + randomvalue)
		mc.setAttr(i+".tz", getz + randomvalue)
def scale():
	import random as random
	from random import uniform as rand
	sel = mc.ls(selection=True)
	for i in sel:
		randomvalue = rand(-0.2,0.2)
		getx = mc.getAttr(i+".sx")
		gety = mc.getAttr(i+".sy")
		getz = mc.getAttr(i+".sz")
		mc.setAttr(i+".sx", getx + randomvalue)
		mc.setAttr(i+".sy", gety + randomvalue)
		mc.setAttr(i+".sz", getz + randomvalue)
def rotate():
	import random as random
	from random import uniform as rand
	sel = mc.ls(selection=True)
	for i in sel:
		randomvalue = rand(-15,15)
		getx = mc.getAttr(i+".rx")
		gety = mc.getAttr(i+".ry")
		getz = mc.getAttr(i+".rz")
		mc.setAttr(i+".rx", getx + randomvalue)
		#mc.setAttr(i+".ry", gety + randomvalue)
		#mc.setAttr(i+".rz", getz + randomvalue)
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
def refeditor():
	mel.eval('ReferenceEditor')
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


mc.loadPlugin( 'redshift4maya.mll')
mc.setAttr("defaultRenderGlobals.currentRenderer", "redshift", type="string")

##############################################################################################################################################
######################################################################   HOTKEYS  ############################################################
##############################################################################################################################################

mc.nameCommand( 'weeToools', annotation='weeToools', command="python(\"execfile('C:/Users/er/Downloads/weeScript.py')\")")
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

mc.nameCommand( 'fTrans', annotation='FreezeTransformations', command='python("mc.makeIdentity( apply=True )")', stp='python')
mc.hotkey( k='q', sht=True, name='fTrans')
mc.nameCommand( 'dHis', annotation='DeleteHistory', command='python("mc.delete (ch=True)")', stp='python')
mc.hotkey( k="w", sht=True, name='dHis')
mc.nameCommand( 'dnondefHis', annotation='DeleteNonDeformerHistory', command='BakeNonDefHistory')
mc.hotkey( k='e', sht=True, name='dnondefHis')
incrsave = mc.nameCommand('incrsave', annotation='incrsave', command='python("incsave()")', stp='python')
mc.hotkey(k='Space', ctl=True, sht=True, name='incrsave')

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
mc.workspaceControl(ui, retain=True, floating=True, uiScript='weeToolsUI()')

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################
