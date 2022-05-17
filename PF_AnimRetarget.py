import json
import maya.cmds as cmds
import os

global scriptname; scriptname = "PF_AnimRetarget"
global Toes_Fixed; ToesFixed = False
global Toes_or_digit

CtrlJointPairs = {
        "Head_M":"", "Neck2_M":"", "Neck1_M":"", "Root_M":"", "Spine1_M":"", "Spine2_M":"", "Spine3_M":"", "Spine4_M":"", "Chest_M":"",
    "Scapula_R":"", "Shoulder_R":"",   "Elbow_R":"",   "Armtwist_R":"",   "Wrist_R":"",
    "Scapula_L":"",   "Shoulder_L":"",   "Elbow_L":"",   "Armtwist_L":"",   "Wrist_L":"",
    "Hip_R":"",   "Knee_R":"",   "Ankle_R":"",   "Toe_R":"",
    "Hip_L":"",   "Knee_L":"",   "Ankle_L":"",   "Toe_L":"",
    "ThumbFinger1_R":"",   "ThumbFinger2_R":"",   "ThumbFinger3_R":"",
    "IndexFinger1_R":"",   "IndexFinger2_R":"",   "IndexFinger3_R":"",
    "MiddleFinger1_R":"",   "MiddleFinger2_R":"",   "MiddleFinger3_R":"",
    "RingFinger1_R":"",   "RingFinger2_R":"",   "RingFinger3_R":"",
    "PinkyFinger1_R":"",   "PinkyFinger2_R":"",   "PinkyFinger3_R":"",
    "ThumbFinger1_L":"",   "ThumbFinger2_L":"",   "ThumbFinger3_L":"",
    "IndexFinger1_L":"",   "IndexFinger2_L":"",   "IndexFinger3_L":"",
    "MiddleFinger1_L":"",   "MiddleFinger2_L":"",   "MiddleFinger3_L":"",
    "RingFinger1_L":"",   "RingFinger2_L":"",   "RingFinger3_L":"",
    "PinkyFinger1_L":"",   "PinkyFinger2_L":"",   "PinkyFinger3_L":"",}
def getfiles(*args) -> list:
    global icon; global banner; global presetfolder; global FKicon; global pickerfolder
    mayascriptpaths = os.getenv("MAYA_SCRIPT_PATH").split(";")
    for each in mayascriptpaths:
        if each.endswith("maya/scripts"):
            scriptsfolder = each
            break
    icon = scriptsfolder + "/" + scriptname + "/data/img/PF_Anim_ico.png"
    banner = scriptsfolder + "/" + scriptname + "/data/img/PF_Anim_banner.png"
    presetfolder = scriptsfolder + "/" + scriptname + "/data/presets/"
    pickerfolder = scriptsfolder + "/" + scriptname + "/data/img/picker/"
    get_preset_list()
    return [icon, banner, presetfolder]

def PresetMaker():
    window_main = cmds.window(title="Preset Maker", le=600, widthHeight=(450, 500), s=False)
    cmds.columnLayout(adj = True, h = 100)
    cmds.separator(style = "none", h = 5)
    cmds.text("starttext", label ="Select bone and press on corresponding button", fn = "boldLabelFont")
    cmds.rowLayout(numberOfColumns=2, cw2=(200, 30), ct2=("both", "both"), adj=True)
    cmds.textField("newPreset_input")
    cmds.iconTextButton(style='iconOnly', image1='save.png', label='btn_presetMaker_win', c = savePreset)
    cmds.setParent("..")

    cmds.showWindow(window_main)
    cmds.setFocus("starttext")
    PresetMaker_UI()
def PresetMaker_UI():
    FL = cmds.formLayout("FL")
    cmds.picture(i=pickerfolder + "body.png", h=450, w=450)
    cmds.text("lastbone_tx", label = "last bone here")
    # __________________________________________________________________________________________________________________#
    cmds.iconTextButton("btn_Head_M", i=pickerfolder + "head.png", iol="", hi=pickerfolder + "head_hi.png", ann="Head", c=lambda *_: pickerbtn_pressed("Head_M"))  # Head
    cmds.iconTextButton("btn_Neck2_M", i=pickerfolder + "neck2.png", iol="", hi=pickerfolder + "neck2_hi.png", ann="Neck2", c=lambda *_: pickerbtn_pressed("Neck2_M"))  # Neck2
    cmds.iconTextButton("btn_Neck1_M", i=pickerfolder + "neck1.png", iol="", hi=pickerfolder + "neck1_hi.png", ann="Neck1", c=lambda *_: pickerbtn_pressed("Neck1_M"))  # Neck1
    cmds.iconTextButton("btn_Root_M", i=pickerfolder + "root.png", hi=pickerfolder + "root_hi.png", iol="", ann="Root", c=lambda *_: pickerbtn_pressed("Root_M"))  # Root
    cmds.iconTextButton("btn_Spine1_M", i=pickerfolder + "spine1.png", hi=pickerfolder + "Spine1_hi.png", iol="", ann="Spine1", c=lambda *_: pickerbtn_pressed("Spine1_M"))  # Spine1
    cmds.iconTextButton("btn_Spine2_M", i=pickerfolder + "spine2.png", hi=pickerfolder + "Spine2_hi.png", iol="", ann="Spine2", c=lambda *_: pickerbtn_pressed("Spine2_M"))  # Spine2
    cmds.iconTextButton("btn_Spine3_M", i=pickerfolder + "spine3.png", hi=pickerfolder + "Spine3_hi.png", iol="", ann="Spine3", c=lambda *_: pickerbtn_pressed("Spine3_M"))  # Spine3
    cmds.iconTextButton("btn_Spine4_M", i=pickerfolder + "spine4.png", hi=pickerfolder + "Spine4_hi.png", iol="", ann="Spine4", c=lambda *_: pickerbtn_pressed("Spine4_M"))  # Spine4
    cmds.iconTextButton("btn_Chest_M", i=pickerfolder + "chest.png", hi=pickerfolder + "chest_hi.png", iol="", ann="Chest", c=lambda *_: pickerbtn_pressed("Chest_M"))  # Chest
    # _______________________________________________________________________RIGHT ARM_____________________________________________________________________________________________________________#
    cmds.iconTextButton("btn_Scapula_R", i=pickerfolder + "scapula.png", hi=pickerfolder + "scapula_hi.png", iol="", ann="Scapula", c=lambda *_: pickerbtn_pressed("Scapula_R"))  # Scapula
    cmds.iconTextButton("btn_Shoulder_R", i=pickerfolder + "shoulder.png", hi=pickerfolder + "shoulder_hi.png", iol="", ann="Shoulder", c=lambda *_: pickerbtn_pressed("Shoulder_R"))  # Shoulder
    cmds.iconTextButton("btn_Elbow_R", i=pickerfolder + "shoulder.png", hi=pickerfolder + "shoulder_hi.png", iol="", ann="Elbow", c=lambda *_: pickerbtn_pressed("Elbow_R"))  # Elbow
    cmds.iconTextButton("btn_Armtwist_R", i=pickerfolder + "armtwist.png", hi=pickerfolder + "armtwist_hi.png", iol="", ann="Twist", c=lambda *_: pickerbtn_pressed("Armtwist_R"))  # Twist
    cmds.iconTextButton("btn_Wrist_R", i=pickerfolder + "wrist.png", hi=pickerfolder + "wrist_hi.png", iol="", ann="Hand", c=lambda *_: pickerbtn_pressed("Wrist_R"))  # Hand
    # _______________________________________________________________________LEFT ARM_____________________________________________________________________________________________________________#
    cmds.iconTextButton("btn_Scapula_L", i=pickerfolder + "scapula.png", hi=pickerfolder + "scapula_hi.png", iol="", ann="Scapula", c=lambda *_: pickerbtn_pressed("Scapula_L"))  # Scapula
    cmds.iconTextButton("btn_Shoulder_L", i=pickerfolder + "shoulder.png", hi=pickerfolder + "shoulder_hi.png", iol="",  ann="Shoulder", c=lambda *_: pickerbtn_pressed("Shoulder_L"))  # Shoulder
    cmds.iconTextButton("btn_Elbow_L", i=pickerfolder + "shoulder.png", hi=pickerfolder + "shoulder_hi.png", iol="", ann="Elbow", c=lambda *_: pickerbtn_pressed("Elbow_L"))  # Elbow
    cmds.iconTextButton("btn_Armtwist_L", i=pickerfolder + "armtwist.png", hi=pickerfolder + "armtwist_hi.png", iol="", ann="Twist", c=lambda *_: pickerbtn_pressed("Armtwist_L"))  # Twist
    cmds.iconTextButton("btn_Wrist_L", i=pickerfolder + "wrist.png", hi=pickerfolder + "wrist_hi.png", iol="", ann="Hand", c=lambda *_: pickerbtn_pressed("Wrist_L"))  # Hand
    # _______________________________________________________________________RIGHT LEG_____________________________________________________________________________________________________________#
    cmds.iconTextButton("btn_Hip_R", i=pickerfolder + "hip.png", hi=pickerfolder + "hip_hi.png", iol="", ann="Hip", c=lambda *_: pickerbtn_pressed("Hip_R"))  # Hip
    cmds.iconTextButton("btn_Knee_R", i=pickerfolder + "knee.png", hi=pickerfolder + "knee_hi.png", iol="", ann="Knee", c=lambda *_: pickerbtn_pressed("Knee_R"))  # Knee
    cmds.iconTextButton("btn_Ankle_R", i=pickerfolder + "Ankle.png", hi=pickerfolder + "Ankle.png", iol="", ann="Foot", c=lambda *_: pickerbtn_pressed("Ankle_R"))  # Foot
    cmds.iconTextButton("btn_Toes_R", i=pickerfolder + "Toes.png", hi=pickerfolder + "Toes_hi.png", iol="", ann="Toes", c=lambda *_: pickerbtn_pressed("Toes_R"))  # Toes
    # _______________________________________________________________________LEFT LEG_____________________________________________________________________________________________________________#
    cmds.iconTextButton("btn_Hip_L", i=pickerfolder + "hip.png", hi=pickerfolder + "hip_hi.png", iol="", ann="Hip", c=lambda *_: pickerbtn_pressed("Hip_L"))  # Hip
    cmds.iconTextButton("btn_Knee_L", i=pickerfolder + "knee.png", hi=pickerfolder + "knee_hi.png", iol="", ann="Knee", c=lambda *_: pickerbtn_pressed("Knee_L"))  # Knee
    cmds.iconTextButton("btn_Ankle_L", i=pickerfolder + "Ankle.png", hi=pickerfolder + "Ankle_hi.png", iol="", ann="Foot",  c=lambda *_: pickerbtn_pressed("Ankle_L"))  # Foot
    cmds.iconTextButton("btn_Toes_L", i=pickerfolder + "Toes.png", hi=pickerfolder + "Toes_hi.png", iol="", ann="Toes", c=lambda *_: pickerbtn_pressed("Toes_L"))  # Toes
    # _______________________________________________________________________RIGHT FINGER_____________________________________________________________________________________________________________#
    cmds.iconTextButton("btn_ThumbFinger1_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Thumb Finger 1", c=lambda *_: pickerbtn_pressed("ThumbFinger1_R"))  # ThumbFinger1_R
    cmds.iconTextButton("btn_ThumbFinger2_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Thumb Finger 2", c=lambda *_: pickerbtn_pressed("ThumbFinger2_R"))  # ThumbFinger2_R
    cmds.iconTextButton("btn_ThumbFinger3_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Thumb Finger 3", c=lambda *_: pickerbtn_pressed("ThumbFinger3_R"))  # ThumbFinger3_R
    cmds.iconTextButton("btn_IndexFinger1_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Index Finger 1", c=lambda *_: pickerbtn_pressed("IndexFinger1_R"))  # IndexFinger1_R
    cmds.iconTextButton("btn_IndexFinger2_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Index Finger 2", c=lambda *_: pickerbtn_pressed("IndexFinger2_R"))  # IndexFinger2_R
    cmds.iconTextButton("btn_IndexFinger3_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Index Finger 3", c=lambda *_: pickerbtn_pressed("IndexFinger3_R"))  # IndexFinger3_R
    cmds.iconTextButton("btn_MiddleFinger1_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Middle Finger 1", c=lambda *_: pickerbtn_pressed("MiddleFinger1_R"))  # MiddleFinger1_R
    cmds.iconTextButton("btn_MiddleFinger2_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Middle Finger 2", c=lambda *_: pickerbtn_pressed("MiddleFinger2_R"))  # MiddleFinger2_R
    cmds.iconTextButton("btn_MiddleFinger3_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Middle Finger 3", c=lambda *_: pickerbtn_pressed("MiddleFinger3_R"))  # MiddleFinger3_R
    cmds.iconTextButton("btn_RingFinger1_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Ring Finger 1", c=lambda *_: pickerbtn_pressed("RingFinger1_R"))  # RingFinger1_R
    cmds.iconTextButton("btn_RingFinger2_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Ring Finger 2", c=lambda *_: pickerbtn_pressed("RingFinger2_R"))  # RingFinger2_R
    cmds.iconTextButton("btn_RingFinger3_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Ring Finger 3", c=lambda *_: pickerbtn_pressed("RingFinger3_R"))  # RingFinger3_R
    cmds.iconTextButton("btn_PinkyFinger1_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Pinky Finger 1", c=lambda *_: pickerbtn_pressed("PinkyFinger1_R"))  # PinkyFinger3_R
    cmds.iconTextButton("btn_PinkyFinger2_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Pinky Finger 2", c=lambda *_: pickerbtn_pressed("PinkyFinger2_R"))  # PinkyFinger3_R
    cmds.iconTextButton("btn_PinkyFinger3_R", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Pinky Finger 3", c=lambda *_: pickerbtn_pressed("PinkyFinger3_R"))  # PinkyFinger3_R
    # _______________________________________________________________________LEFT FINGER_____________________________________________________________________________________________________________#
    cmds.iconTextButton("btn_ThumbFinger1_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Thumb Finger 1", c=lambda *_: pickerbtn_pressed("ThumbFinger1_L"))  # ThumbFinger1_L
    cmds.iconTextButton("btn_ThumbFinger2_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Thumb Finger 2", c=lambda *_: pickerbtn_pressed("ThumbFinger2_L"))  # ThumbFinger2_L
    cmds.iconTextButton("btn_ThumbFinger3_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Thumb Finger 3", c=lambda *_: pickerbtn_pressed("ThumbFinger3_L"))  # ThumbFinger3_L
    cmds.iconTextButton("btn_IndexFinger1_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Index Finger 1", c=lambda *_: pickerbtn_pressed("IndexFinger1_L"))  # IndexFinger1_L
    cmds.iconTextButton("btn_IndexFinger2_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Index Finger 2", c=lambda *_: pickerbtn_pressed("IndexFinger2_L"))  # IndexFinger2_L
    cmds.iconTextButton("btn_IndexFinger3_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Index Finger 3", c=lambda *_: pickerbtn_pressed("IndexFinger3_L"))  # IndexFinger3_L
    cmds.iconTextButton("btn_MiddleFinger1_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Middle Finger 1", c=lambda *_: pickerbtn_pressed("MiddleFinger1_L"))  # MiddleFinger1_L
    cmds.iconTextButton("btn_MiddleFinger2_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Middle Finger 2", c=lambda *_: pickerbtn_pressed("MiddleFinger2_L"))  # MiddleFinger2_L
    cmds.iconTextButton("btn_MiddleFinger3_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Middle Finger 3", c=lambda *_: pickerbtn_pressed("MiddleFinger3_L"))  # MiddleFinger3_L
    cmds.iconTextButton("btn_RingFinger1_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Ring Finger 1", c=lambda *_: pickerbtn_pressed("RingFinger1_L"))  # RingFinger1_L
    cmds.iconTextButton("btn_RingFinger2_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Ring Finger 2", c=lambda *_: pickerbtn_pressed("RingFinger2_L"))  # RingFinger2_L
    cmds.iconTextButton("btn_RingFinger3_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Ring Finger 3", c=lambda *_: pickerbtn_pressed("RingFinger3_L"))  # RingFinger3_L
    cmds.iconTextButton("btn_PinkyFinger1_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Pinky Finger 1", c=lambda *_: pickerbtn_pressed("PinkyFinger1_L"))  # PinkyFinger3_L
    cmds.iconTextButton("btn_PinkyFinger2_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Pinky Finger 2", c=lambda *_: pickerbtn_pressed("PinkyFinger2_L"))  # PinkyFinger3_L
    cmds.iconTextButton("btn_PinkyFinger3_L", i=pickerfolder + "finger.png", hi=pickerfolder + "finger_hi.png", iol="", ann="Pinky Finger 3", c=lambda *_: pickerbtn_pressed("PinkyFinger3_L"))  # PinkyFinger3_L
    # _______________________________________________________________________________________________________________________________________________________________________________________________________________#
    cmds.formLayout(FL, e=True, af=["lastbone_tx", "left", 10]); cmds.formLayout(FL, e=True, af=["lastbone_tx", "top", 10])
    cmds.formLayout(FL, e=True, af=["btn_Head_M", "left", 201]); cmds.formLayout(FL, e=True, af=["btn_Head_M", "top", 3])  # Head
    cmds.formLayout(FL, e=True, af=["btn_Neck2_M", "left", 206]); cmds.formLayout(FL, e=True, af=["btn_Neck2_M", "top", 43])  # Neck2
    cmds.formLayout(FL, e=True, af=["btn_Neck1_M", "left", 202]); cmds.formLayout(FL, e=True, af=["btn_Neck1_M", "top", 58])  # Neck1
    cmds.formLayout(FL, e=True, af=["btn_Root_M", "left", 167]); cmds.formLayout(FL, e=True, af=["btn_Root_M", "top", 199])  # Root
    cmds.formLayout(FL, e=True, af=["btn_Spine1_M", "left", 182]); cmds.formLayout(FL, e=True, af=["btn_Spine1_M", "top", 177])  # Spine1
    cmds.formLayout(FL, e=True, af=["btn_Spine2_M", "left", 183]); cmds.formLayout(FL, e=True, af=["btn_Spine2_M", "top", 155])  # Spine2
    cmds.formLayout(FL, e=True, af=["btn_Spine3_M", "left", 183]); cmds.formLayout(FL, e=True, af=["btn_Spine3_M", "top", 135])  # Spine3
    cmds.formLayout(FL, e=True, af=["btn_Spine4_M", "left", 183]); cmds.formLayout(FL, e=True, af=["btn_Spine4_M", "top", 116])  # Spine4
    cmds.formLayout(FL, e=True, af=["btn_Chest_M", "left", 213]); cmds.formLayout(FL, e=True, af=["btn_Chest_M", "top", 74])  # Spine4
    # ________________________________________________________________RIGHT ARM_________________________________________________________________________________#
    cmds.formLayout(FL, e=True, af=["btn_Scapula_R", "left", 179]); cmds.formLayout(FL, e=True, af=["btn_Scapula_R", "top", 51])  # Scapula
    cmds.formLayout(FL, e=True, af=["btn_Shoulder_R", "left", 147]); cmds.formLayout(FL, e=True, af=["btn_Shoulder_R", "top", 68])  # Shoulder
    cmds.formLayout(FL, e=True, af=["btn_Elbow_R", "left", 102]); cmds.formLayout(FL, e=True, af=["btn_Elbow_R", "top", 68])  # Elbow
    cmds.formLayout(FL, e=True, af=["btn_Armtwist_R", "left", 70]); cmds.formLayout(FL, e=True, af=["btn_Armtwist_R", "top", 80])  # Elbow
    cmds.formLayout(FL, e=True, af=["btn_Wrist_R", "left", 17]); cmds.formLayout(FL, e=True, af=["btn_Wrist_R", "top", 68])  # Hand
    # ________________________________________________________________LEFT ARM_________________________________________________________________________________#
    cmds.formLayout(FL, e=True, af=["btn_Scapula_L", "right", 174]); cmds.formLayout(FL, e=True, af=["btn_Scapula_L", "top", 51])  # Scapula
    cmds.formLayout(FL, e=True, af=["btn_Shoulder_L", "right", 142]); cmds.formLayout(FL, e=True, af=["btn_Shoulder_L", "top", 68])  # Shoulder
    cmds.formLayout(FL, e=True, af=["btn_Elbow_L", "right", 97]); cmds.formLayout(FL, e=True, af=["btn_Elbow_L", "top", 68])  # Elbow
    cmds.formLayout(FL, e=True, af=["btn_Armtwist_L", "right", 65]); cmds.formLayout(FL, e=True, af=["btn_Armtwist_L", "top", 80])  # Elbow
    cmds.formLayout(FL, e=True, af=["btn_Wrist_L", "right", 12]); cmds.formLayout(FL, e=True, af=["btn_Wrist_L", "top", 68])  # Hand
    # ________________________________________________________________RIGHT LEG_________________________________________________________________________________#
    cmds.formLayout(FL, e=True, af=["btn_Hip_R", "left", 181]); cmds.formLayout(FL, e=True, af=["btn_Hip_R", "top", 228])  # Hip
    cmds.formLayout(FL, e=True, af=["btn_Knee_R", "left", 179]); cmds.formLayout(FL, e=True, af=["btn_Knee_R", "top", 303])  # Knee
    cmds.formLayout(FL, e=True, af=["btn_Ankle_R", "left", 178]); cmds.formLayout(FL, e=True, af=["btn_Ankle_R", "top", 375])  # Foot
    cmds.formLayout(FL, e=True, af=["btn_Toes_R", "left", 176]); cmds.formLayout(FL, e=True, af=["btn_Toes_R", "top", 427])  # Toes
    # ________________________________________________________________LEFT LEG__________________________________________________________________________________#
    cmds.formLayout(FL, e=True, af=["btn_Hip_L", "right", 178]); cmds.formLayout(FL, e=True, af=["btn_Hip_L", "top", 228])  # Hip
    cmds.formLayout(FL, e=True, af=["btn_Knee_L", "right", 176]); cmds.formLayout(FL, e=True, af=["btn_Knee_L", "top", 303])  # Knee
    cmds.formLayout(FL, e=True, af=["btn_Ankle_L", "right", 176]); cmds.formLayout(FL, e=True, af=["btn_Ankle_L", "top", 375])  # Foot
    cmds.formLayout(FL, e=True, af=["btn_Toes_L", "right", 174]); cmds.formLayout(FL, e=True, af=["btn_Toes_L", "top", 427])  # Toes
    # ________________________________________________________________RIGHT FINGERS_________________________________________________________________________________#
    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger1_R", "left", 105]);    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger1_R", "top", 313])  # ThumbFinger1
    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger2_R", "left", 129]);    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger2_R", "top", 298])  # ThumbFinger2
    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger3_R", "left", 153]);    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger3_R", "top", 290])  # ThumbFinger3
    cmds.formLayout(FL, e=True, af=["btn_IndexFinger1_R", "left", 91]);    cmds.formLayout(FL, e=True, af=["btn_IndexFinger1_R", "top", 277])  # IndexFinger1
    cmds.formLayout(FL, e=True, af=["btn_IndexFinger2_R", "left", 98]);    cmds.formLayout(FL, e=True, af=["btn_IndexFinger2_R", "top", 250])  # IndexFinger2
    cmds.formLayout(FL, e=True, af=["btn_IndexFinger3_R", "left", 104]);    cmds.formLayout(FL, e=True, af=["btn_IndexFinger3_R", "top", 223])  # IndexFinger3
    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger1_R", "left", 69]);    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger1_R", "top", 273])  # MiddleFinger1
    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger2_R", "left", 68]);    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger2_R", "top", 243])  # MiddleFinger1
    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger3_R", "left", 66]);    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger3_R", "top", 215])  # MiddleFinger2
    cmds.formLayout(FL, e=True, af=["btn_RingFinger1_R", "left", 50]);    cmds.formLayout(FL, e=True, af=["btn_RingFinger1_R", "top", 277])  # RingFinger1
    cmds.formLayout(FL, e=True, af=["btn_RingFinger2_R", "left", 43]);    cmds.formLayout(FL, e=True, af=["btn_RingFinger2_R", "top", 252])  # RingFinger1
    cmds.formLayout(FL, e=True, af=["btn_RingFinger3_R", "left", 35]);    cmds.formLayout(FL, e=True, af=["btn_RingFinger3_R", "top", 226])  # RingFinger2
    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger1_R", "left", 34]);    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger1_R", "top", 293])  # PinkyFinger1
    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger2_R", "left", 20]);    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger2_R", "top", 274])  # PinkyFinger1
    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger3_R", "left", 10]);    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger3_R", "top", 254])  # PinkyFinger2
    # __________________________________________________________________LEFT FINGERS__________________________________________________________________________________#
    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger1_L", "right", 102]);    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger1_L", "top", 313])  # ThumbFinger1
    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger2_L", "right", 127]);    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger2_L", "top", 298])  # ThumbFinger2
    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger3_L", "right", 151]);    cmds.formLayout(FL, e=True, af=["btn_ThumbFinger3_L", "top", 290])  # ThumbFinger3
    cmds.formLayout(FL, e=True, af=["btn_IndexFinger1_L", "right", 88]);    cmds.formLayout(FL, e=True, af=["btn_IndexFinger1_L", "top", 277])  # IndexFinger1
    cmds.formLayout(FL, e=True, af=["btn_IndexFinger2_L", "right", 96]);    cmds.formLayout(FL, e=True, af=["btn_IndexFinger2_L", "top", 250])  # IndexFinger2
    cmds.formLayout(FL, e=True, af=["btn_IndexFinger3_L", "right", 101]);    cmds.formLayout(FL, e=True, af=["btn_IndexFinger3_L", "top", 223])  # IndexFinger3
    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger1_L", "right", 66]);    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger1_L", "top", 273])  # MiddleFinger1
    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger2_L", "right", 65]);    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger2_L", "top", 243])  # MiddleFinger1
    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger3_L", "right", 63]);    cmds.formLayout(FL, e=True, af=["btn_MiddleFinger3_L", "top", 215])  # MiddleFinger2
    cmds.formLayout(FL, e=True, af=["btn_RingFinger1_L", "right", 47]);    cmds.formLayout(FL, e=True, af=["btn_RingFinger1_L", "top", 277])  # RingFinger1
    cmds.formLayout(FL, e=True, af=["btn_RingFinger2_L", "right", 40]);    cmds.formLayout(FL, e=True, af=["btn_RingFinger2_L", "top", 252])  # RingFinger1
    cmds.formLayout(FL, e=True, af=["btn_RingFinger3_L", "right", 32]);    cmds.formLayout(FL, e=True, af=["btn_RingFinger3_L", "top", 226])  # RingFinger2
    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger1_L", "right", 31]);    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger1_L", "top", 293])  # PinkyFinger1
    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger2_L", "right", 17]);    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger2_L", "top", 274])  # PinkyFinger1
    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger3_L", "right", 7]);    cmds.formLayout(FL, e=True, af=["btn_PinkyFinger3_L", "top", 254])  # PinkyFinger2
def ToeFixer_Preset():
    ToeChecker = False
    ToesWrongVars = ["*Foot", "*foot", "*ankle", "*Ankle"] #Возможные названия кости ступней
    for each in ToesWrongVars:
        presence = cmds.ls(each, l = True, r = True)
        if len(presence) > 0:
            wrongToeParent = presence
            wrongToeChildFull = cmds.listRelatives(wrongToeParent, f = True)
            wrongToeChildShort = cmds.listRelatives(wrongToeParent)
            if wrongToeChildFull :
                ToeChecker = True
            else:
                ToeChecker = False
            break
    if ToeChecker:
        for index, item in enumerate(wrongToeChildFull):
            if "Digit" in item:
                pass
            else:
                globals()["ToesFixed"] = True
            NewName = wrongToeChildShort[index].replace("Digit", "Toes")
            cmds.rename(item, NewName)
            global Toes_Fixed
            Toes_Fixed= True
def pickerbtn_pressed(btn_name = ""):
    picker_selbone = cmds.ls(sl=True, type = "joint") #получаем выделение, в список вносим только джоинты
    if len(picker_selbone) == 1: #если выбран только 1 объект
        if not globals()["ToesFixed"]:
            print(globals()["ToesFixed"])
            ToeFixer_Preset()
            print(globals()["ToesFixed"])
        picker_selbone = picker_selbone[0] #picker_selbone - выбранный 1 объект
        pickerbtn_changecolor(btn_name) #меняем цвет на основе названия контроллера (поместить в конец)
        recognizerResult = recognizer(picker_selbone, btn_name) #запускаем рекогнайзер на неймспейсы и название кости, он возвращает список из 2 элементов - неймспейс, кость
        namespace = recognizerResult[0]
        bone_name = recognizerResult[1]
        cmds.iconTextButton("btn_"+btn_name, e = True, ann = bone_name)
        cmds.text("lastbone_tx", e = True, label = bone_name)
        add_to_writelist(btn_name, bone_name, namespace) #Запускаем записыватель в файл
    else:
        cmds.confirmDialog(title = "error", m="Select 1 bone that matches button!", bgc=(0.49, 0.2, 0.2), button="OK, sorry")
def recognizer(picker_selbone = "", btn_name = ""): #узнать неймспейс и название кости
    toRecognizeChecker = picker_selbone.split(":") #делим первый входной аргумент (т.е. picker_selbone) на части по ":", чтобы найти неймспейс
    if len(toRecognizeChecker) > 1: #если в списке больше 1 значения - то нейспейс есть
        namespace = toRecognizeChecker[0]+":"
        bone_name = toRecognizeChecker[1]
    else:
        namespace = ""
        bone_name = toRecognizeChecker[0]
    return [namespace, bone_name]
def add_to_writelist(controller = "", bone_name = "", namespace = ""):
    rx = cmds.getAttr(namespace+bone_name + ".rx")
    ry = cmds.getAttr(namespace+bone_name + ".ry")
    rz = cmds.getAttr(namespace+bone_name + ".rz")
    CtrlJointPairs[controller] = [bone_name, rx, ry, rz]
def savePreset(*args):
    print (CtrlJointPairs)
    newPresetName = cmds.textField("newPreset_input", q = True, tx = True)
    CtrlJointPairs_json = json.dumps(CtrlJointPairs, indent=4)
    with open(presetfolder + newPresetName + ".json", "w+") as newPresetName:
        newPresetName.write(CtrlJointPairs_json)
def pickerbtn_changecolor(btn_name):
    if "Finger" in btn_name: #Если палец, то не собираем путь, а ставим конкретный, на картинку пальца
        img_ok = "finger_ok.png"
    else:
        img_ok = btn_name[:-2]+"_ok.png"
    cmds.iconTextButton("btn_"+btn_name, i = pickerfolder+img_ok, e = True)

def get_preset_list():
    global presetlist
    presetlist = os.listdir(presetfolder)

def getNS_Rig(*args):
    global RigNS
    RigObj = cmds.ls(sl = True)
    RigNS = RigObj[0].split(":")
    if len(RigNS) > 1:
        RigNS = RigNS[0]+":"
    else:
        RigNS = ""
    cmds.textField("RigNS", e = True, tx = RigNS)
def getNS_Anim(*args):
    global AnimNS
    global AnimPelvisName
    AnimObj = cmds.ls(sl=True)
    AnimNS = AnimObj[0].split(":")
    if len(AnimNS) > 1:
        AnimPelvisName = AnimNS[1]
        AnimNS = AnimNS[0] + ":"
        AnimPelvisName = AnimNS+AnimPelvisName
    else:
        AnimNS = ""
        AnimPelvisName = AnimObj[0]
    cmds.textField("AnimNS", e=True, tx=AnimNS)
    cmds.button(btn_match, edit = True, enable = True)

def openPreset(*args):
    selected_preset = cmds.optionMenu("Main_presetMenu", q=True, v=True)
    with open(presetfolder+selected_preset+".json") as preset:
        presetfile = json.load(preset)
    return presetfile
def Match(*args):
    Match_ToeFixer()
    presetfile = openPreset()
    for each in presetfile:
        line = presetfile[each]
        if len(line)>0:
            match_controller = each
            match_joint = line[0]
            match_rx = line[1]
            match_ry = line[2]
            match_rz = line[3]
        checker = cmds.ls(AnimNS+match_joint)
        if len(checker) > 0:
            cmds.setAttr(AnimNS+match_joint+".rx", match_rx)
            cmds.setAttr(AnimNS+match_joint + ".ry", match_ry)
            cmds.setAttr(AnimNS+match_joint + ".rz", match_rz)
        else:
            pass
def Match_ToeFixer(*args):
    ToesWrongVars = ["*Foot", "*foot", "*ankle", "*Ankle"]  # Возможные названия кости ступней
    for each in ToesWrongVars:
        presence = cmds.ls(each, l=True, r=True)
        if len(presence) > 0:
            wrongToeParent = presence
            wrongToeChildFull = cmds.listRelatives(wrongToeParent, f=True)
            wrongToeChildShort = cmds.listRelatives(wrongToeParent)
            if wrongToeChildFull:
                ToeChecker = True
            else:
                ToeChecker = False
            break
    if ToeChecker:
        for index, item in enumerate(wrongToeChildFull):
            NewName = wrongToeChildShort[index].replace("Digit", "Toe")
            cmds.rename(item, NewName)

def ConnectFK(*args):
    global ConstraintNodes
    ConstraintNodes = []
    presetfile = openPreset()
    for key in presetfile:
        line = presetfile[key]
        if len(line) > 0:  # Проверка, есть ли вообще какие-то значения в файле у ключа (контроллера)
            controllchecker = cmds.ls(RigNS + "FK" + key)  # Проверялка контроллов это попытка выбрать неймспейс плюс ключ
            if len(controllchecker) > 0:  # Если чета выбралось, то идём дальше
                jointchecker = cmds.ls(AnimNS + line[0])  # Проверялка пытающаяся выбрать нулевой элемент списка контроллера в сцене (который точно есть в файле)
                if len(jointchecker) > 0:  # Если чета выбралось в сцене, то идём дальше
                    # __________Теперь можно начинать заменять названия контроллеров_________#
                    if "Root" in key:
                        connect_controll = RigNS+"RootX_M"
                        connect_joint = AnimNS + line[0]
                        ControllArray.append(connect_controll)
                        cmds.matchTransform(connect_controll, connect_joint, pos=True)
                        ConstraintNodes.append(cmds.pointConstraint(connect_joint, connect_controll, mo=True))
                        ConstraintNodes.append(cmds.orientConstraint(connect_joint, connect_controll, mo=True))
                    else:
                        connect_controll = RigNS + "FK"+key
                        connect_joint = AnimNS + line[0]
                        ControllArray.append(connect_controll)
                        print(connect_controll+"____"+connect_joint)
                        ConstraintNodes.append(cmds.orientConstraint(connect_joint, connect_controll, mo=True))
    print(ConstraintNodes)

def ConnectIK(*args):
    global ConstraintNodes
    ConstraintNodes = []
    presetfile = openPreset()
    for key in presetfile:
        line = presetfile[key]
        if len(line) > 0: #Проверка, есть ли вообще какие-то значения в файле у ключа (контроллера)
            controllchecker = cmds.ls(RigNS+"FK"+key) #Проверялка контроллов это попытка выбрать неймспейс плюс ключ
            if len(controllchecker) > 0: #Если чета выбралось, то идём дальше
                jointchecker = cmds.ls(AnimNS + line[0]) #Проверялка пытающаяся выбрать нулевой элемент списка контроллера в сцене (который точно есть в файле)
                if len(jointchecker) > 0: #Если чета выбралось в сцене, то идём дальше
                    #__________Теперь можно начинать заменять названия контроллеров_________#
                    if "Wrist" in key: #Заменили запястье на руку IK
                        connect_controll = RigNS+"IK"+key.replace("Wrist", "Arm")
                        connect_joint = AnimNS+line[0]
                        ControllArray.append(connect_controll)
                        ConstraintNodes.append(cmds.parentConstraint(connect_joint, connect_controll, mo=True))
                    elif "Ankle" in key:
                        connect_controll = RigNS+"IK"+key.replace("Ankle", "Leg")
                        connect_joint = AnimNS+line[0]
                        ControllArray.append(connect_controll)
                        ConstraintNodes.append(cmds.parentConstraint(connect_joint, connect_controll, mo=True))
                    elif "Chest" in key:
                        connect_controll = RigNS+"IK"+key.replace("Chest", "Spine3")
                        connect_joint = AnimNS+line[0]
                        ControllArray.append(connect_controll)
                        ConstraintNodes.append(cmds.parentConstraint(connect_joint, connect_controll, mo=True))
                    elif "Elbow" in key or "Shoulder" in key or "Hip" in key or "Knee" in key or "Spine1" in key or "Spine2" in key or "Spine3" in key or "Spine4" in key:
                        print("propuskaem = " +key)
                        pass
                    elif "Root" in key:
                        connect_controll = RigNS+"RootX_M"
                        connect_joint = AnimNS+line[0]
                        cmds.matchTransform(connect_controll, connect_joint, pos=True)
                        ControllArray.append(connect_controll)
                        ConstraintNodes.append(cmds.pointConstraint(connect_joint, connect_controll, mo=True))
                        ConstraintNodes.append(cmds.orientConstraint(connect_joint, connect_controll, mo=True))
                    else:
                        connect_controll = RigNS+"FK"+key
                        connect_joint = AnimNS+line[0]
                        ControllArray.append(connect_controll)
                        ConstraintNodes.append(cmds.orientConstraint(connect_joint, connect_controll, mo=True))



def disconnect(*args):
    for each in ConstraintNodes:
        cmds.delete(each)
def bake(*args):
    toBakeArray = ControllArray
    cmds.select(toBakeArray)
    cmds.bakeResults(sm=True, ral=True, pok=True, t=(cmds.playbackOptions(q=True, min=True), cmds.playbackOptions(q=True, max=True)))
    for each in ConstraintNodes:
        cmds.delete(each)

global AnimNS; global RigNS
def PF_AnimRetarget_Main():
    global ConstraintNodes
    ConstraintNodes = []
    global ControllArray
    ControllArray = []
    global Toes_Fixed
    Toes_Fixed = False
    getfiles()
    window_main = cmds.window(title="PF Animation Retarget", le=600, widthHeight=(250, 420), s=False)
    cmds.columnLayout(adj=True)
    cmds.separator(style = "in") ; cmds.separator(style="none", h=5)
    cmds.image(image = banner, width=250, bgc=(0.2667, 0.2667, 0.2667))
    cmds.separator(style="none", h=5) ; cmds.separator(style = "out") ;    cmds.separator(style="none", h=3)
    cmds.text("Select T-Pose preset that matches animation :", fn = "smallBoldLabelFont")
    cmds.separator(style="none", h=5)
    cmds.rowLayout(numberOfColumns=2, cw2=(207, 30), ct2=("left", "left"))
    cmds.optionMenu("Main_presetMenu", h = 22, w = 200)
    for each in presetlist:
        item = cmds.menuItem(each.split(".")[0])
    cmds.iconTextButton(style='iconOnly', image1='HIKCharacterToolFullBody.png', label='btn_presetMaker_win', bgc = (0.2, 0.4, 0.5), h = 21, w = 30, c = PresetMaker)
    cmds.setParent('..')
    cmds.optionMenu("Main_presetMenu", q = True, v = True)
    cmds.separator(style = "none", h = 5)
    cmds.separator(style = "out")
    cmds.separator(style = "none", h = 1)
    cmds.rowLayout(numberOfColumns=2, cw2=(125, 125), ct2=("both", "both"), adj=True)
    cmds.text("select RIG", fn = "smallBoldLabelFont")
    cmds.text("select ANIMATION",fn = "smallBoldLabelFont")
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=2, cw2=(50, 50), ct2=("both", "both"), adj=True)
    cmds.button(label="RIG", width=120, bgc=(0.3, 0.45, 0.3), c = getNS_Rig)
    cmds.button(label="ANIM", width=120, bgc=(0.45, 0.4, 0.35), c = getNS_Anim)
    cmds.setParent("..")
    cmds.separator(style="none", h=5)
    cmds.rowLayout(numberOfColumns=2, cw2=(50, 50,), ct2=("both", "both"), adj=True)
    cmds.text("RIG NAMESPACE", w=120, fn="smallPlainLabelFont")
    cmds.text("ANIM NAMESPACE", w=120, fn="smallPlainLabelFont")
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=2, cw2=(50,50), ct2=("both", "both"), adj=True)
    RigNS = cmds.textField("RigNS", editable=False, tx="", width=120)
    AnimNS = cmds.textField("AnimNS", editable=False, tx=" ", width=120)
    cmds.setParent("..")
    cmds.separator(style = "none", h =7); cmds.separator(style = "out");
    cmds.separator(style = "none", h = 5)
    cmds.text("Press on frame 0 to MATCH animation to rig :", fn = "smallBoldLabelFont")
    cmds.separator(style = "none", h = 7)
    global btn_match;
    btn_match = cmds.button(label = "Match", bgc = (0.3,0.3,0.2), enable = False, c = Match)
    cmds.separator(style = "none", h = 7)
    cmds.separator(style = "in")
    cmds.separator(style = "none", h = 3)
    cmds.text("Press to CONNECT rig to animation :", fn = "smallBoldLabelFont")
    cmds.separator(style = "none", h = 3)
    cmds.rowLayout(numberOfColumns=2, cw2=(120, 120), ct2=("both", "both"), adj=True)
    cmds.button(label="Connect FK", width=120, h = 30, bgc=(0.3, 0.4, 0.45), c = ConnectFK)
    cmds.button(label="Connect IK", width=120, h = 30, bgc=(0.45, 0.3, 0.3), c = ConnectIK)
    cmds.setParent("..")
    cmds.separator(style = "none", h = 5)
    cmds.text("Press to DISCONNECT rig from animation :", fn = "smallBoldLabelFont")
    cmds.separator(style = "none", h = 5)
    cmds.columnLayout(cal = "center", cat = ("both", 65))

    cmds.button(label="Disconnect", width = 120, h = 15, bgc = (0.30,0.21,0.40), c = disconnect)
    cmds.setParent("..")
    cmds.separator(style = "none", h =5)
    cmds.separator(style = "out")
    cmds.separator(style = "none", h = 10)
    cmds.columnLayout(cal = "center", cat = ("both", 30))
    cmds.button(label = "BAKE", width = 200, h = 30, bgc = (0.2,0.5,0.5), c = bake)
    cmds.showWindow(window_main)