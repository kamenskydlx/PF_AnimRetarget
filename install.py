import sys
import maya.cmds as cmds
import maya.mel as mel
import os
def getfolder(*args):
    syspath = sys.path
    mayascriptspaths = os.getenv("MAYA_SCRIPT_PATH").split(";")
    for each in mayascriptspaths:
        if each.endswith("maya/scripts"):
            scriptsfolder = each
            break

    AnimRetargetScriptPath = scriptsfolder + "/PF_AnimRetarget"
    AnimRetarget_icon = AnimRetargetScriptPath+"/data/img/PF_Anim_ico.png"
    return [syspath, AnimRetargetScriptPath, AnimRetarget_icon]
def runscript(*args):
     print(scriptpath)

command = '''
import sys
syspath = sys.path
mayascriptspaths = os.getenv("MAYA_SCRIPT_PATH").split(";")
for each in mayascriptspaths:
    if each.endswith("maya/scripts"):
        scriptsfolder = each
        break
AnimRetargetScriptPath = scriptsfolder+"/PF_AnimRetarget"
if AnimRetargetScriptPath in syspath:
    import PF_AnimRetarget
    PF_AnimRetarget.PF_AnimRetarget_Main()
else:
    syspath.append(AnimRetargetScriptPath)
    import PF_AnimRetarget
    PF_AnimRetarget.PF_AnimRetarget_Main()

'''
def onMayaDroppedPythonFile(*args):
    AnimRetargetScriptPath = getfolder()[1]
    syspath = getfolder()[0]
    AnimRetarget_icon = getfolder()[2]
    gShelfTopLevel = mel.eval("global string $gShelfTopLevel; $temp = $gShelfTopLevel;")
    currentShelf = cmds.tabLayout(gShelfTopLevel, q=True, st=True)
    cmds.setParent(currentShelf)
    cmds.shelfButton(command=command, sourceType="python", image=AnimRetarget_icon)

