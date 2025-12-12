

style amii:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
    antialias True

style amii2:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    antialias True


init:

    style glow_say is say_dialogue:
        color "#FFFFFF"
        outlines [
            (10, "#ffffff07", 0, 0),
            (8,  "#ffffff07", 0, 0),
            (6,  "#ffffff10", 0, 0),
            (4,  "#ffffff10", 0, 0),
            (3,  "#ffffff10", 0, 0),
            (2,  "#ffffff15", 0, 0),
            (1,  "#ffffff15", 0, 0),
            (0,  "#ffffff20", 0, 0)
        ]
        yoffset -10






define narrator = Character(None, kind=nvl, ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define et = Character(None, kind=nvl, ctc="ctc_ent", ctc_pause="ctc_blink", ctc_position="nestled")
define am = Character(None, kind=nvl, ctc="ctc_ent", ctc_pause="ctc_blink", ctc_position="nestled",what_prefix ='{size=24}{font=amii.otf}',what_style='amii')
define br = Character(None, kind=nvl, ctc="ctc_ent", ctc_pause="ctc_br", ctc_position="nestled", what_outlines=[ (10, "#ffffff07"),(8, "#ffffff07"),(6, "#ffffff10"),(4, "#ffffff10"), (3, "ffffff10"),  (2, "ffffff15"),(1, "ffffff15"),(0.5, "ffffff15") ])
define br2 = Character(None, kind=nvl, ctc="ctc_ent", ctc_pause="ctc_br", ctc_position="nestled", what_outlines=[ (10, "#00000007"),(8, "#00000007"),(6, "#00000010"),(4, "#00000010"), (3, "00000010"),  (2, "00000015"),(1, "00000015"),(0.5, "00000015") ])
define nar = Character(None, ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")



define pl = Character('[na]', color="#E06666", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")

define my = Character('マヤ', color="#ff9587", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define my2 = Character('天使', color="#ff9587", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define my_q = Character('淨化部A', color="#ff9587", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define my_q2 = Character('？？？', color="#ff9587", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")

define sc = Character('シーキュレット', color="#d9d2E9", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")


define cr = Character('クリオネ',what_prefix = '{cps=*1.7}', color="#c9daf8", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")


define hk = Character('ハク',what_prefix = '{cps=*0.3}', color="#ffe594", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define hk_q = Character('？？？',what_prefix = '{cps=*0.3}', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define hk_qns = Character('？？？',what_prefix = '{cps=0}', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define hkn = Character('ハク', color="#ffe594", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define hk_A = Character('白髪の男性', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled",what_prefix ='{font=amii.otf}',what_style='amii2')


define hk_b = Character('ハク', color="#cfe2f3", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define hk_bq = Character('ハク？', color="#cfe2f3", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")


define ar = Character('アルネ', color="#a4c2f4", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define ar_q = Character('気高い女性', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")


define en = Character('エノク', color="#a2c4c9", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define en_q = Character('背の高い男性', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")


define er = Character('エルジェーベト', color="#6d9eeb", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")


define ev = Character('イヴリン', color="#b4a7d6", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define ev_q = Character('司書の姉さん', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")


define rv = Character('ラヴィアン', color="#ead1dc", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define rv_q = Character('ローズ？', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")


define rs = Character('ローズ', color="#d0a6bd", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")


define gg = Character('グレゴール', color="#93c47d", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")


define gr = Character('グレーテ', color="#d9ead3", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define gr_w = Character('優しいお姉さん', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")




define qus = Character('？？？', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")

define lz_q1 = Character('小さい女性', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define lz1 = Character('委員長', color="#ce8349", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")

define lz_q2 = Character('金髪の女性', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define lz2 = Character('金髪女', color="#fce5cd", ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")

define ex1 = Character('淨化部A', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")

define ex2 = Character('淨化部B', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")

define ex3 = Character('淨化部C', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")

define ex5 = Character('神殿の司祭', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")

define ex6 = Character('魔導部の司祭', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define ex7 = Character('学術部の司祭', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")

define ex8 = Character('学術部A', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define ex9 = Character('学術部B', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define ex10 = Character('学術部C', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define ex11 = Character('学術部D', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")
define ex12 = Character('通りすがりの人', ctc="ctc_blink", ctc_pause="ctc_blink", ctc_position="nestled")



define ui_place_name = Image("ui_place_name.png")
transform place_name:
    yalign 0.905



label place00:
    image place00 = Text("？？？", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place00
    with dissolve
    pause 2
    hide ui_place_name
    hide place00
    with dissolve
    pause 1
    return


label place01:
    image place01 = Text("神殿ロビー", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place01
    with dissolve
    pause 2
    hide ui_place_name
    hide place01
    with dissolve
    pause 1
    return



label place02:
    image place02 = Text("神殿正門", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place02
    with dissolve
    pause 2
    hide ui_place_name
    hide place02
    with dissolve
    pause 1
    return



label place03:
    image place03 = Text("神殿廊下", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place03
    with dissolve
    pause 2
    hide ui_place_name
    hide place03
    with dissolve
    pause 1
    return





label place04:
    image place04 = Text("作業場", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place04
    with dissolve
    pause 2
    hide ui_place_name
    hide place04
    with dissolve
    pause 1
    return


label place05:
    image place05 = Text("花壇", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place05
    with dissolve
    pause 2
    hide ui_place_name
    hide place05
    with dissolve
    pause 1
    return



label place06:
    image place06 = Text("医務室", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place06
    with dissolve
    pause 2
    hide ui_place_name
    hide place06
    with dissolve
    pause 1
    return


label place10:
    image place10 = Text("寮", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place10
    with dissolve
    pause 2
    hide ui_place_name
    hide place10
    with dissolve
    pause 1
    return


label place10_1:
    image place10_1 = Text("先輩の部屋", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place10_1
    with dissolve
    pause 2
    hide ui_place_name
    hide place10_1
    with dissolve
    pause 1
    return


label place10_2:
    image place10_2 = Text("マヤの部屋", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place10_2
    with dissolve
    pause 2
    hide ui_place_name
    hide place10_2
    with dissolve
    pause 1
    return



label place12:
    image place12 = Text("天使の夢", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place12
    with dissolve
    pause 2
    hide ui_place_name
    hide place12
    with dissolve
    pause 1
    return


label place13:
    image place13 = Text("民家", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place13
    with dissolve
    pause 2
    hide ui_place_name
    hide place13
    with dissolve
    pause 1
    return


label place14:
    image place14 = Text("浄化部事務室", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place14
    with dissolve
    pause 2
    hide ui_place_name
    hide place14
    with dissolve
    pause 1
    return


label place15:
    image place15 = Text("寮の廊下", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place15
    with dissolve
    pause 2
    hide ui_place_name
    hide place15
    with dissolve
    pause 1
    return


label place16:
    image place16 = Text("街", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place16
    with dissolve
    pause 2
    hide ui_place_name
    hide place16
    with dissolve
    pause 1
    return


label place17:
    image place17 = Text("森の中", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place17
    with dissolve
    pause 2
    hide ui_place_name
    hide place17
    with dissolve
    pause 1
    return

label place18:
    image place18 = Text("洞窟", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place18
    with dissolve
    pause 2
    hide ui_place_name
    hide place18
    with dissolve
    pause 1
    return

label place19:
    image place19 = Text("アルネの部屋", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place19
    with dissolve
    pause 2
    hide ui_place_name
    hide place19
    with dissolve
    pause 1
    return




label place100:
    image place100 = Text("野外礼拝堂", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place100
    with dissolve
    pause 2
    hide ui_place_name
    hide place100
    with dissolve
    pause 1
    return


label place101:
    image place101 = Text("神殿裏庭", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place101
    with dissolve
    pause 2
    hide ui_place_name
    hide place101
    with dissolve
    pause 1
    return


label place102:
    image place102 = Text("訓練場", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place102
    with dissolve
    pause 2
    hide ui_place_name
    hide place102
    with dissolve
    pause 1
    return


label place104:
    image place104 = Text("図書館", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place104
    with dissolve
    pause 2
    hide ui_place_name
    hide place104
    with dissolve
    pause 1
    return


label place105:
    image place105 = Text("ローズの部屋", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place105
    with dissolve
    pause 2
    hide ui_place_name
    hide place105
    with dissolve
    pause 1
    return


label place106:
    image place106 = Text("階段", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place106
    with dissolve
    pause 2
    hide ui_place_name
    hide place106
    with dissolve
    pause 1
    return


label place107:
    image place107 = Text("魔導部事務室", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place107
    with dissolve
    pause 2
    hide ui_place_name
    hide place107
    with dissolve
    pause 1
    return

label place108:
    image place108 = Text("ハクの部屋", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place108
    with dissolve
    pause 2
    hide ui_place_name
    hide place108
    with dissolve
    pause 1
    return

label place114:
    image place114 = Text("書斎", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place114
    with dissolve
    pause 2
    hide ui_place_name
    hide place114
    with dissolve
    pause 1
    return

label place116:
    image place116 = Text("宿屋", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show place116
    with dissolve
    pause 2
    hide ui_place_name
    hide place116
    with dissolve
    pause 1
    return

label place_t_9:
    image placet9 = Text("9ヶ月前", size=32, xalign=0.9, yalign=0.9)
    pause 1
    show ui_place_name at place_name
    show placet9
    with dissolve
    pause 2
    hide ui_place_name
    hide placet9
    with dissolve
    pause 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
