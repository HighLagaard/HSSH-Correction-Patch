default persistent.titlename = "def"

define right = Position(xalign = 1.0)
define left = Position(xalign = 0.0)
define center = Position(xalign = 0.5)
define truecenter = Position(xalign = 0.5, yalign = 0.5)
define offcenter = Position(xoffset=524,yoffset=394)

transform ding:
    alpha 1
    linear 0.3 alpha 0


define day3_10_ctc = Position(xalign = 0.55, yalign = 0.5)

define hkright = Position(xalign = 1.9)
define bigleft = Position(xalign = -1.0)
define arleft = Position(xalign = -0.2)
define bigright = Position(xalign = 2.5)
define mycent = Position(xoffset=210,yoffset=-120)

transform blur_1(child):
    contains:
        child
    contains:
        child
        alpha 0.1 xoffset -3
    contains:
        child
        alpha 0.1 xoffset 3
    contains:
        child
        alpha 0.1 yoffset -3
    contains:
        child
        alpha 0.1 yoffset 4
    contains:
        child
        alpha 0.1 xoffset -4
    contains:
        child
        alpha 0.1 xoffset 4
    contains:
        child
        alpha 0.1 yoffset -4
    contains:
        child
        alpha 0.1 yoffset 4
    contains:
        child
        alpha 0.1 zoom 1.015
    contains:
        child
        alpha 0.1 zoom 1.10
    contains:
        child
        alpha 0.1 zoom 0.995
    contains:
        child
        alpha 0.1 zoom 0.990
    contains:
        child
        alpha 0.1 yoffset 5
    contains:
        child
        alpha 0.1 zoom 1.05
    contains:
        child
        alpha 0.1 yzoom 2
    contains:
        child
        alpha 0.1 yzoom 3
    contains:
        child
        alpha 0.1 yzoom 1.5
    contains:
        child
        alpha 0.1 zoom 0.8
    contains:
        child
        alpha 0.1 zoom 0.9
    contains:
        child

transform blur_char(child):
    contains:
        child
    contains:
        child
        alpha 0.1 xoffset -3
    contains:
        child
        alpha 0.1 xoffset 3
    contains:
        child
        alpha 0.1 yoffset -3
    contains:
        child
        alpha 0.1 yoffset 4
    contains:
        child
        alpha 0.1 xoffset -4
    contains:
        child
        alpha 0.1 xoffset 4
    contains:
        child
        alpha 0.1 yoffset -4
    contains:
        child
        alpha 0.1 yoffset 4
    contains:
        child
        alpha 0.1 zoom 1.015
    contains:
        child
        alpha 0.1 zoom 1.10
    contains:
        child
        alpha 0.1 zoom 0.995
    contains:
        child
        alpha 0.1 zoom 0.990
    contains:
        child
        alpha 0.1 yoffset 5
    contains:
        child
        alpha 0.1 zoom 1.05
    contains:
        child
        alpha 0.1 yzoom 2
    contains:
        child
        alpha 0.1 yzoom 3
    contains:
        child
        alpha 0.1 yzoom 1.5
    contains:
        child
        alpha 0.1 zoom 0.8
    contains:
        child
        alpha 0.1 zoom 0.9
    contains:
        child
        alpha 0.5

transform blur(child):
    blur 10
    contains:
        child

transform blur_0(child):
    contains:
        child


transform bounce:
    subpixel True
    yoffset 0
    easein 0.2 yoffset 5
    easeout 0.2 yoffset -7
    easein 0.15 yoffset 3
    easein 0.15 yoffset 0


transform in_right:
    subpixel True
    xalign 4.6
    easein 0.8 xalign 2.5

transform in_right2:
    subpixel True
    xpos 1000
    easein 0.8 xpos 600

transform out_right:
    subpixel True
    xalign 2.5
    easeout 0.8 xalign 4.6

transform out_right2:
    subpixel True
    xpos 600
    easein 0.8 xpos 1000

transform er_stand:
    subpixel True
    yoffset 0
    ease 2.5 yoffset 10
    ease 2.5 yoffset -10
    ease 2.5 yoffset 5
    ease 2.5 yoffset 0



transform bt:
    ypos 768
transform bg_down:
    easein 0.5 yoffset -50
    ease 1 yoffset -50
    easein 0.5 yoffset 0

transform ch_down:
    easein 0.5 yoffset -60
    ease 1 yoffset -60
    easein 0.5 yoffset 0




transform huruhuru:
    subpixel True
    easeout 0.07 xoffset 6
    easeout 0.07 xoffset -6
    easeout 0.07 xoffset 5
    easeout 0.07 xoffset -5
    easeout 0.1 xoffset 2
    easeout 0.1 xoffset 0

init:
    python:
        def slowdown(t):
            return 1 - (1 - t) * (1 - t)

    $ config.keymap['toggle_skip'].remove('K_TAB')

define Auto_screen = False

screen keymap_screen:
    if Auto_screen == True:
        key "K_TAB" action [Preference("auto-forward", "toggle"), ToggleScreen("auto_indicator")]
    else:
        key "K_TAB" action [Preference("auto-forward", "toggle"), ToggleScreen("auto_indicator")]

init python:
    player_name = 'FlaSh'
    p = Character('player_name', dynamic = True)


init:
    transform shaking:
        linear 0.01 xoffset -0 yoffset 2
        linear 0.01 xoffset 1 yoffset -0
        linear 0.01 xoffset 0 yoffset -2
        linear 0.01 xoffset -1 yoffset 1
        linear 0.01 xoffset 0 yoffset 0
        repeat


"Shown"
$ show_quick_menu = False
"Hidden"
$ show_quick_menu = True


screen disable_Lmouse():
    key "mouseup_1" action NullAction()


init python:
    style.say_thought.line_leading = 12 
    style.ruby_style = Style(style.default)
    style.ruby_style.size = 16 
    style.ruby_style.yoffset = -40 
    style.default.ruby_style = style.ruby_style






init:

    transform ping:
        yalign 1
        ypos 0
        linear 0.1 ypos 20
        linear 0.1 ypos 0

    transform say:
        alpha 0.5
        linear 0.2 alpha 1

    transform saynot:
        alpha 1
        linear 0.2 alpha 0.5

    transform ding:
        alpha 1
        linear 0.2 alpha 0


define facedissolve = Dissolve ( 0.2 )
define fastdissolve = ImageDissolve ( "gui/trans.png" ,  0.2 )
define newfastdissolve = { "master" : ImageDissolve ( "gui/trans.png" ,  0.2 ) }
define exfastdissolve = ImageDissolve("gui/trans.png", 0.2, reverse=False, layers=["master"])



transform slowname:
    xalign 0.0
    yalign 0.0
    xpos 123
    ypos 503

transform slowsay:
    xalign 0.0
    yalign 1.0
    xpos 138
    ypos 549



init python:
    
    from renpy.text.text import Text
    from renpy.display.layout import Composite
    
    
    NAME_INFO = {
        "pl": ("[na]", "#E06666"),

        "my": ("マヤ", "#ff9587"), "my2": ("天使", "#ff9587"),
        "my_q": ("淨化部A", "#ff9587"), "my_q2": ("？？？", "#ff9587"),

        "sc": ("シーキュレット", "#d9d2E9"),
        "cr": ("クリオネ", "#c9daf8"),

        "hk": ("ハク", "#ffe594"), "hk_q": ("？？？", "#ffe594"),
        "hk_qns": ("？？？", "#ffe594"), "hkn": ("ハク", "#ffe594"),
        "hk_A": ("白髪の男性", "#ffe594"),
        "hk_b": ("ハク", "#cfe2f3"), "hk_bq": ("ハク？", "#cfe2f3"),

        "ar": ("アルネ", "#a4c2f4"), "ar_q": ("気高い女性", "#a4c2f4"),

        "en": ("エノク", "#a2c4c9"), "en_q": ("背の高い男性", "#a2c4c9"),

        "er": ("エルジェーベト", "#6d9eeb"),

        "ev": ("イヴリン", "#b4a7d6"), "ev_q": ("司書の姉さん", "#b4a7d6"),

        "rv": ("ラヴィアン", "#ead1dc"), "rv_q": ("ローズ？", "#ead1dc"),

        "rs": ("ローズ", "#d0a6bd"),

        "gg": ("グレゴール", "#93c47d"),

        "gr": ("グレーテ", "#d9ead3"), "gr_w": ("優しいお姉さん", "#d9ead3"),

        "qus": ("？？？", "#ffffff"),

        "lz_q1": ("小さい女性", "#ce8349"), "lz1": ("委員長", "#ce8349"),
        "lz_q2": ("金髪の女性", "#fce5cd"), "lz2": ("金髪女", "#fce5cd"),

        "ex1": ("淨化部A", "#ffffff"), "ex2": ("淨化部B", "#ffffff"),
        "ex3": ("淨化部C", "#ffffff"), "ex5": ("神殿の司祭", "#ffffff"),
        "ex6": ("魔導部の司祭", "#ffffff"), "ex7": ("学術部の司祭", "#ffffff"),
        "ex8": ("学術部A", "#ffffff"), "ex9": ("学術部B", "#ffffff"),
        "ex10": ("学術部C", "#ffffff"), "ex11": ("学術部D", "#ffffff"),
        "ex12": ("通りすがりの人", "#ffffff"),

        "nar": ("", "#ffffff"), "narrator": ("", "#ffffff"),
        "et": ("", "#ffffff"), "am": ("", "#ffffff"),
        "br": ("", "#ffffff"), "br2": ("", "#000000"),
    }
    
    def clone_say():
        w, h = renpy.config.screen_width, renpy.config.screen_height
        who_var = getattr(renpy.store, "_last_say_who", None)
        what = getattr(renpy.store, "_last_say_what", "") or ""
        
        
        who_name = ""
        color = "#ffffff"
        
        if isinstance(who_var, basestring):
            
            entry = NAME_INFO.get(who_var, (who_var, "#ffffff"))
            who_name, color = entry
        elif who_var is not None:
            
            var_name = None
            for name, val in renpy.store.__dict__.items():
                if val is who_var:
                    var_name = name
                    break
            entry = NAME_INFO.get(var_name, ("", "#ffffff"))
            who_name, color = entry
        
        return Composite(
            (w, h),
            (123, 503), Text(who_name, style="say_label", size=36, color=color),
            (138, 538), Text("{k=1}%s{/1}" % what, style="say_dialogue", size=36)
        )

init python:

    def show_say_ex():
        renpy.show("say_clone", what=clone_say(), layer="screens")


    def hide_say_ex():
        renpy.hide("say_clone", layer="screens")


define slowdissolve = ImageDissolve ( "gui/trans.png" ,  2.0 )


define gjdissolve = Dissolve(2.0)

define veryslowdissolve = Dissolve(12.0)


label bgw:
    show bgw onlayer screens
    hide bgw onlayer screens with dissolve
    return

transform ctc:
    xoffset 0
    pause 0.5
    xoffset 2
    pause 0.5
    xoffset 5
    pause 0.5
    xoffset 2
    pause 0.5
    repeat

transform ctc_ent:
    yoffset 0
    pause 0.5
    yoffset 2
    pause 0.5
    yoffset 5
    pause 0.5
    yoffset 2
    pause 0.5
    repeat


init:

    python:
        import math
        class Shaker(object):
            
            anchors = {
        'top' : 0.0,
        'center' : 0.5,
        'bottom' : 1.0,
        'left' : 0.0,
        'right' : 1.0,
        }
            
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                
                self.start = [ self.anchors.get(i, i) for i in start ]  
                self.dist = dist    
                self.child = child
            
            def __call__(self, t, sizes):
                
                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                
                return (int(nx), int(ny), 0, 0)
        def _Shake(start, time, child=None, dist=100.0, **properties):
            
            move = Shaker(start, child, dist=dist)
            
            return renpy.display.layout.Motion(move,
                time,
                child,
                add_sizes=True,
                **properties)
        Shake = renpy.curry(_Shake)






init:

    python:
        import math
        class char_Shaker(object):
            
            anchors = {
        'top' : 0.0,
        'center' : 0.5,
        'left' : 0.0,
        }
            
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                
                self.start = [ self.anchors.get(i, i) for i in start ]  
                self.dist = dist    
                self.child = child
            
            def __call__(self, t, sizes):
                
                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                
                xalign, yalign, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                
                xalign = xalign
                yalign = yalign
                
                nx = xalign + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = yalign + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                
                return (int(nx), int(ny), 0, 0)
        def char_Shake(start, time, child=None, dist=100.0, **properties):
            
            move = char_Shaker(start, child, dist=dist)
            
            return renpy.display.layout.Motion(move,
                time,
                child,
                add_sizes=True,
                **properties)
        char_Shake = renpy.curry(char_Shake)






init:
    $ sshake = Shake((0, 0, 0, 0), 0.5, dist=15)
    $ sshake_C = char_Shake((0.208, -0.149, 00, 0), 10000, dist=2)





define slowname = Position(xalign = 0, yalign = 0, xpos = 123, ypos = 503)
define slowsay = Position(xalign = 0, yalign = 1, xpos = 138, ypos = 549)
define blur_nvl = Position(xpos = 113, ypos = 63)
init python:
    day = 0
init:
    transform notice:
        xalign 0.5
        yalign 0.52

    transform notice_T:
        xalign 0.5
        yalign 0.3

    transform day00:
        xalign 0.9
        yalign 0.9

image char_hkq = Text("？？？",antialias=False, size=36)
image char_my = Text('マヤ', color="#ff9587", size=36)
image char_hk = Text('ハク', color="#ffe594", size=36)
image char_hk_b = Text('ハク', color="#cfe2f3", size=36)
image char_sc = Text('シーキュレット', color="#d9d2E9", size=36)
image char_en = Text('エノク', color="#a2c4c9",size=36)
image char_er = Text('エルジェーベト', color="#6d9eeb", size=36)
image hk1 = Text("みなさぁ～ん、お元気ですかあ？ここ最近、{vspace=10}季節に沿わずずう～…っと寒い日が続いてまぁ{vspace=10}す…～", slow=True, slow_cps=4, size=36, antialias=False)
image hk2 = Text("みなさんのだあいじなお身体はですねえ、す{vspace=10}べて神様がお貸出しになったものなのですよ{vspace=10}お？ですので、", slow=True, slow_cps=4, size=36)
image hk3 = Text("{k=1}どうか病気にだけはならないよう～ご自愛く{vspace=10}ださいませえ…♪{/k}", slow=True, slow_cps=4, size=36)


image hk1_en = Text("みなさぁ～ん、お元気ですかあ？ここ最近、{vspace=10}季節に沿わずずう～…っと寒い日が続いてまぁ{vspace=10}す…～", slow=True, slow_cps=4, size=27, antialias=False)
image hk2_en = Text("みなさんのだあいじなお身体はですねえ、す{vspace=10}べて神様がお貸出しになったものなのですよ{vspace=10}お？ですので、", slow=True, slow_cps=4, size=27)
image hk3_en = Text("{k=1}どうか病気にだけはならないよう～ご自愛く{vspace=10}ださいませえ…♪{/k}", slow=True, slow_cps=4, size=27)


image hk1_cn = Text("{cps=*0.7}各位～还好吗？最近这天啊，不分季节一直冷得不行呢～{/cps}", slow=True, slow_cps=4, size=28, antialias=False)
image hk2_cn = Text("{cps=*0.7}大家那宝贵的身体呢，可都是神借给你们的哦？所以呀，{/cps}", slow=True, slow_cps=4, size=28)
image hk3_cn = Text("{cps=*0.7}一定要保重身体～不要生病哦……♪{/cps}", slow=True, slow_cps=4, size=28)


image notice = Text("このゲームはフィクションです。\n実在の人物、団体、事件、宗教などとは一切関係ありません。\n作品中にたびたび用いられる「ちいさい」または「おさない」等の表現は、\nキャラクターの身体的特徴を表すものであり、\n決して年齢のことを表しているものではございません。\n本ゲームに登場するキャラクターの年齢は、全て１８歳以上と設定しております。", size=25, text_align=0.5, line_leading=10)
image notice_Title = Text("注      意", color="#ff0000",size=48, text_align=0.5, line_leading=10)
image day12_1 = Text("{color=#000000}自分を変えるのは自分だけ。\nどんなに大きな変化も、全てあなたの一歩から。{/color}", slow=True, slow_cps=5 ,size=36, text_align=0.5)

screen tut_key:

    add "tut_key.png"
    add "ctc" at ctc:
        xalign 0.95
        yalign 0.95
    text "ヘルプ":
        size 48
        xalign 0.5
        yalign 0.08
    text "Esc\n ゲームメニュー":
        size 28
        xpos 60
        ypos 190

    text "Tab\n オートモード":
        size 28
        xpos 25
        ypos 330

    text "Ctrl\n 押し続けている間\n 既読スキップする":
        size 28
        xpos 85
        ypos 530

    text "Space\n 台詞を読み進める":
        size 28
        xpos 380
        ypos 555

    text "方向キー\n インターフェースを移動する":
        size 28
        xpos 380
        ypos 660

    text "Enter\n 選択する":
        size 28
        xalign 0.95
        ypos 380
        text_align 1.0

    text "S\n スクリーンショット":
        size 28
        xpos 510
        ypos 150

    text "H\n インターフェースを隠す":
        size 28
        xpos 510
        ypos 230

screen tut_key2:
    add "tut_key2.png"
    add "ctc" at ctc:
        xalign 0.95
        yalign 0.95
    text "ヘルプ":
        size 48
        xalign 0.5
        yalign 0.08

    text "左クリック\n 選択または会話を進める":
        size 28
        xpos 55
        ypos 370

    text " 右クリック\nメニューを閉じる ":
        size 28
        xalign 0.9
        ypos 405
        text_align 1.0

    text "ホイール\n ヒストリーを表示":
        size 28
        xpos 510
        ypos 250

screen tut_key3:
    add "black"

    text "セーブの途中にゲームを閉じるなど異常な操作でプレイすると、\nエラーが発生する場合があります。":
        size 25
        xalign 0.5
        yalign 0.5
        text_align 0.5
        line_leading 10












define no = Dissolve(0.0)


screen set_name(title, init_name):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 20
        text title xalign 0.5
        input default init_name allow None length 10 xalign 0.5

screen dis_Lag:
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 20
        textbutton "English" action Language("English"), SetVariable("persistent.current_lang", "English"), SetVariable("persistent.control", "1"), Hide('dis_Lag'), Jump("tut")
        textbutton "Japanese" action Language("Japanese"), SetVariable("persistent.current_lang", "Japanese"), SetVariable("persistent.control", "1"), Hide('dis_Lag'), Jump("tut")
        textbutton "Korean" action Language("Korean"), SetVariable("persistent.current_lang", "Korean"), SetVariable("persistent.control", "1"), Hide('dis_Lag'), Jump("tut")

screen set_name2(title, init_name2):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 20
        text title xalign 0.5
        input default init_name2 length 10 xalign 0.5




init python:
    g = Gallery()

    g.locked_button = "gal/gal-locked.png"

    g.transition = dissolve

    g.hover_border = "gal/gal-hover.png"



    g.button("story01"); 
    g.unlock_image("story01")

    g.button("story02"); 
    g.unlock_image("story02")

    g.button("story03"); 
    g.unlock_image("story03")

    g.button("story04"); 
    g.unlock_image("story04")

    g.button("story05"); 
    g.unlock_image("story05")

    g.button("story06"); 
    g.unlock_image("story06"); 
    g.unlock_image("story06R")

    g.button("story07"); 
    g.unlock_image("story07")

    g.button("story08"); 
    g.unlock_image("story08"); 
    g.unlock_image("story08R")

    g.button("story09"); 
    g.unlock_image("story09")

    g.button("story10"); 
    g.unlock_image("story10")


    g.button("story11"); 
    g.unlock_image("story11")

    g.button("story12"); 
    g.unlock_image("story12")

    g.button("story13"); 
    g.unlock_image("story13")

    g.button("story14"); 
    g.unlock_image("story14")

    g.button("story15"); 
    g.unlock_image("story15")

    g.button("story16"); 
    g.unlock_image("story16")

    g.button("story17"); 
    g.unlock_image("story17")

    g.button("story19"); 
    g.unlock_image("story19")

    g.button("story20"); 
    g.unlock_image("story20")

    g.button("story21"); 
    g.unlock_image("story21"); 
    g.unlock_image("story21R")

    g.button("story22"); 
    g.unlock_image("story22")



    g.button("dmy1"); 
    g.unlock_image("dmy1")

    g.button("dmy2"); 
    g.unlock_image("dmy2")

    g.button("dmy3"); 
    g.unlock_image("dmy3")

    g.button("dmy4"); 
    g.unlock_image("dmy4")

    g.button("dmy5"); 
    g.unlock_image("dmy5")



    g.button("cgmy01"); 
    g.unlock_image("cgmy01")

    g.button("cgmy03"); 
    g.unlock_image("cgmy03")

    g.unlock_image("cgmy03_1"); 
    g.unlock_image("cgmy03_2")



    g.button("cgsc01"); 
    g.unlock_image("cgsc01")

    g.button("cgsc02"); 
    g.unlock_image("cgsc02")

    g.button("cgsc03"); 
    g.unlock_image("cgsc03")

    g.button("cgsc04"); 
    g.unlock_image("cgsc04")

    g.button("cgsc05"); 
    g.unlock_image("cgsc05")



    g.button("cgar01"); 
    g.unlock_image("cgar01")

    g.button("cgar02"); 
    g.unlock_image("cgar02")

    g.button("cgar03"); 
    g.unlock_image("cgar03")

    g.button("cgar03R"); 
    g.unlock_image("cgar03R")

    g.button("cgar04"); 
    g.unlock_image("cgar04")

    g.button("cgar05"); 
    g.unlock_image("cgar05")

    g.button("cgar06"); 
    g.unlock_image("cgar06")



    g.button("cgrs01"); 
    g.unlock_image("cgrs01")

    g.button("cgrs02"); 
    g.unlock_image("cgrs02")

    g.button("cgrs03"); 
    g.unlock_image("cgrs03")

    g.button("cgrs03R"); 
    g.unlock_image("cgrs03R")

    g.button("cgrs04"); 
    g.unlock_image("cgrs04")

    g.button("cgrs05"); 
    g.unlock_image("cgrs05")

    g.button("cgrs06"); 
    g.unlock_image("cgrs06")



    g.button("cghk01"); 
    g.unlock_image("cghk01"); 
    g.unlock_image("cghk01R")

    g.button("cghk02"); 
    g.unlock_image("cghk02")

    g.button("cghk03"); 
    g.unlock_image("cghk03")

    g.button("cghk04"); 
    g.unlock_image("cghk04")

    g.button("cghk05"); 
    g.unlock_image("cghk05")

    g.button("cghk06"); 
    g.unlock_image("cghk06")



    g.button("cggr01"); 
    g.unlock_image("cggr01")

    g.button("cggr02"); 
    g.unlock_image("cggr02")

    g.button("cggr02R"); 
    g.unlock_image("cggr02R")

    g.button("cggr03"); 
    g.unlock_image("cggr03")

    g.button("cggr04"); 
    g.unlock_image("cggr04")

    g.button("cggr05"); 
    g.unlock_image("cggr05")

    g.button("cggr06"); 
    g.unlock_image("cggr06")



    g.button("cgcr01"); 
    g.unlock_image("cgcr01")

    g.button("cgcr02"); 
    g.unlock_image("cgcr02")

    g.button("cgcr03"); 
    g.unlock_image("cgcr03")

    g.button("cgcr04"); 
    g.unlock_image("cgcr04")

    g.button("cgcr05"); 
    g.unlock_image("cgcr05"); 
    g.unlock_image("cgcr05R")

    g.button("cgcr06"); 
    g.unlock_image("cgcr06")

    g.button("cgcr07"); 
    g.unlock_image("cgcr07")

    g.button("title_gallery") 

    g.image("titledef")


    if persistent.title_my or persistent.cheat_title: 
        g.image("title_my")
    if persistent.title_sc or persistent.cheat_title: 
        g.image("title_sc")
    if persistent.title_ar or persistent.cheat_title: 
        g.image("title_ar")
    if persistent.title_rs or persistent.cheat_title: 
        g.image("title_rs")
    if persistent.title_gr or persistent.cheat_title: 
        g.image("title_gr")
    if persistent.title_cr or persistent.cheat_title: 
        g.image("title_cr")
    if persistent.title_hk or persistent.cheat_title: 
        g.image("title_hk")



    if not persistent.cheat_title:
        
        if not persistent.title_my:
            g.image("title_my")
            g.condition("persistent.title_my == True")
        
        if not persistent.title_sc:
            g.image("title_sc")
            g.condition("persistent.title_sc == True")
        
        if not persistent.title_ar:
            g.image("title_ar")
            g.condition("persistent.title_ar == True")
        
        if not persistent.title_rs:
            g.image("title_rs")
            g.condition("persistent.title_rs == True")
        
        if not persistent.title_gr:
            g.image("title_gr")
            g.condition("persistent.title_gr == True")
        
        if not persistent.title_cr:
            g.image("title_cr")
            g.condition("persistent.title_cr == True")
        
        if not persistent.title_hk:
            g.image("title_hk")
            g.condition("persistent.title_hk == True")



    g.transition = dissolve

    g.hover_border = "gal/gal-hover.png"


transform sha:
    alpha 0
    linear 5 alpha 0.3




style galbutton:
    hover_sound "audio/SE/mouse over.ogg"
    activate_sound "audio/SE/mouse click.wav"

init:

    screen cggallery1:
        tag menu

        add "bgw"
        add gui.main_menu_background
        add "main_gallery.png"

        text "ギャラリー":
            xpos 40
            ypos 33
            xalign 0
            style "main_menu_title"

        grid 4 4:

            xspacing 10
            yspacing 10
            xalign 0.8
            yalign 0.5
            xfill False
            yfill False

            add g.make_button("story01", "gal/gal-story01.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story02", "gal/gal-story02.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story03", "gal/gal-story03.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story04", "gal/gal-story04.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("story05", "gal/gal-story05.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story06", "gal/gal-story06.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story07", "gal/gal-story07.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story08", "gal/gal-story08.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("story09", "gal/gal-story09.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story10", "gal/gal-story10.png", xalign=0.5, yalign=0.5, style='galbutton')


            if persistent.call_CG == True:
                add g.make_button("story11", "gal/gal-story11.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("story12", "gal/gal-story12.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story13", "gal/gal-story13.png", xalign=0.5, yalign=0.5, style='galbutton')


            if persistent.call_CG == True:
                add g.make_button("story14", "gal/gal-story14.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("story15", "gal/gal-story15.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story16", "gal/gal-story16.png", xalign=0.5, yalign=0.5, style='galbutton')


        vbox:
            style_prefix "place"

            xpos 0.05
            yalign 0.5
            spacing gui.navigation_spacing
            textbutton '1' action ShowMenu("cggallery1") xalign 0.05 yalign 0.4
            textbutton '2' action ShowMenu("cggallery2") xalign 0.05 yalign 0.5
            textbutton '3' action ShowMenu("cggallery3") xalign 0.05 yalign 0.5
            textbutton '4' action ShowMenu("cggallery4") xalign 0.05 yalign 0.5
            textbutton 'ノート' action ShowMenu("cggallery_memo") yoffset 20
            if persistent.hssh_end_2 or persistent.cheat_rosary:
                textbutton 'ロザリオ' action ShowMenu("cggallery_rozario") yoffset 20
            if persistent.titlename == "def":
                add None
            else:
                textbutton "背景画像" action ShowMenu("title_select") yalign 0.5 yoffset 20
        textbutton '戻る' action Return() xalign 0.05 yalign 0.95


    screen cggallery2:
        tag menu

        add "bgw"
        add gui.main_menu_background
        add "main_gallery.png"

        text "ギャラリー":
            xpos 40
            ypos 33
            xalign 0
            style "main_menu_title"

        grid 4 4:

            xspacing 10
            yspacing 10
            xalign 0.8
            yalign 0.5
            xfill False
            yfill False

            if persistent.call_CG == True:
                add g.make_button("story19", "gal/gal-story19.png", xalign=0.5, yalign=0.5, style='galbutton')
            else:
                add g.make_button("story17", "gal/gal-story17.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story20", "gal/gal-story20.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story21", "gal/gal-story21.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("story22", "gal/gal-story22.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("dmy1", "gal/gal-dmy1.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("dmy2", "gal/gal-dmy2.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("dmy3", "gal/gal-dmy3.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("dmy4", "gal/gal-dmy4.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("dmy5", "gal/gal-dmy5.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgmy01", "gal/gal-my01.png", xalign=0.5, yalign=0.5, style='galbutton')


            if persistent.call_CG == True:
                add g.make_button("cgmy03", "gal/gal-my03.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("cgsc01", "gal/gal-sc01.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("cgsc02", "gal/gal-sc02.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgsc05", "gal/gal-sc05.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgsc03", "gal/gal-sc03.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgsc04", "gal/gal-sc04.png", xalign=0.5, yalign=0.5, style='galbutton')


        vbox:
            style_prefix "place"

            xpos 0.05
            yalign 0.5
            spacing gui.navigation_spacing
            textbutton '1' action ShowMenu("cggallery1") xalign 0.05 yalign 0.4
            textbutton '2' action ShowMenu("cggallery2") xalign 0.05 yalign 0.5
            textbutton '3' action ShowMenu("cggallery3") xalign 0.05 yalign 0.5
            textbutton '4' action ShowMenu("cggallery4") xalign 0.05 yalign 0.5

            textbutton 'ノート' action ShowMenu("cggallery_memo") yoffset 20
            if persistent.hssh_end_2 or persistent.cheat_rosary:
                textbutton 'ロザリオ' action ShowMenu("cggallery_rozario") yoffset 20
            if persistent.titlename == "def":
                add None
            else:
                textbutton "背景画像" action ShowMenu("title_select") yalign 0.5 yoffset 20
        textbutton '戻る' action Return() xalign 0.05 yalign 0.95


init:
    screen cggallery3:
        tag menu

        add "bgw"
        add gui.main_menu_background
        add "main_gallery.png"

        text "ギャラリー":
            xpos 40
            ypos 33
            xalign 0
            style "main_menu_title"

        grid 4 4:

            xspacing 10
            yspacing 10
            xalign 0.8
            yalign 0.5
            xfill False
            yfill False

            add g.make_button("cgar01", "gal/gal-ar01.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgar02", "gal/gal-ar02.png", xalign=0.5, yalign=0.5, style='galbutton')


            if persistent.call_CG == True:
                add g.make_button("cgar03", "gal/gal-ar03.png", xalign=0.5, yalign=0.5, style='galbutton')
            else:
                add g.make_button("cgar03R", "gal/gal-ar03R.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("cgar04", "gal/gal-ar04.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgar05", "gal/gal-ar05.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgar06", "gal/gal-ar06.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgrs01", "gal/gal-rs01.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgrs02", "gal/gal-rs02.png", xalign=0.5, yalign=0.5, style='galbutton')


            if persistent.call_CG == True:
                add g.make_button("cgrs03", "gal/gal-rs03.png", xalign=0.5, yalign=0.5, style='galbutton')
            else:
                add g.make_button("cgrs03R", "gal/gal-rs03R.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("cgrs04", "gal/gal-rs04.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgrs06", "gal/gal-rs06.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgrs05", "gal/gal-rs05.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("cggr01", "gal/gal-gr01.png", xalign=0.5, yalign=0.5, style='galbutton')
            if persistent.call_CG == True:
                add g.make_button("cggr02", "gal/gal-gr02.png", xalign=0.5, yalign=0.5, style='galbutton')
            else:
                add g.make_button("cggr02R", "gal/gal-gr02R.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cggr03", "gal/gal-gr03.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cggr04", "gal/gal-gr04.png", xalign=0.5, yalign=0.5, style='galbutton')

        vbox:
            style_prefix "place"
            xpos 0.05
            yalign 0.5
            spacing gui.navigation_spacing
            textbutton '1' action ShowMenu("cggallery1") xalign 0.05 yalign 0.4
            textbutton '2' action ShowMenu("cggallery2") xalign 0.05 yalign 0.5
            textbutton '3' action ShowMenu("cggallery3") xalign 0.05 yalign 0.5
            textbutton '4' action ShowMenu("cggallery4") xalign 0.05 yalign 0.5

            textbutton 'ノート' action ShowMenu("cggallery_memo") yoffset 20
            if persistent.hssh_end_2 or persistent.cheat_rosary:
                textbutton 'ロザリオ' action ShowMenu("cggallery_rozario") yoffset 20
            if persistent.titlename == "def":
                add None
            else:
                textbutton "背景画像" action ShowMenu("title_select") yalign 0.5 yoffset 20
        textbutton '戻る' action Return() xalign 0.05 yalign 0.95

init:
    screen cggallery4:
        tag menu

        add "bgw"
        add gui.main_menu_background
        add "main_gallery.png"

        text "ギャラリー":
            xpos 40
            ypos 33
            xalign 0
            style "main_menu_title"

        grid 4 4:
            xspacing 10
            yspacing 10
            xalign 0.8
            yalign 0.5
            xfill False
            yfill False

            add g.make_button("cggr05", "gal/gal-gr05.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cggr06", "gal/gal-gr06.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgcr01", "gal/gal-cr01.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("cgcr02", "gal/gal-cr02.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgcr07", "gal/gal-cr07.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgcr03", "gal/gal-cr03.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgcr04", "gal/gal-cr04.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("cgcr05", "gal/gal-cr05.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cgcr06", "gal/gal-cr06.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cghk01", "gal/gal-hk01.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cghk02", "gal/gal-hk02.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("cghk03", "gal/gal-hk03.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cghk06", "gal/gal-hk06.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cghk04", "gal/gal-hk04.png", xalign=0.5, yalign=0.5, style='galbutton')
            add g.make_button("cghk05", "gal/gal-hk05.png", xalign=0.5, yalign=0.5, style='galbutton')

            add g.make_button("title_gallery", "gal/gal-title.png", xalign=0.5, yalign=0.5, style='galbutton')
        vbox:
            style_prefix "place"
            xpos 0.05
            yalign 0.5
            spacing gui.navigation_spacing
            textbutton '1' action ShowMenu("cggallery1") xalign 0.05 yalign 0.4
            textbutton '2' action ShowMenu("cggallery2") xalign 0.05 yalign 0.5
            textbutton '3' action ShowMenu("cggallery3") xalign 0.05 yalign 0.5
            textbutton '4' action ShowMenu("cggallery4") xalign 0.05 yalign 0.5
            textbutton 'ノート' action ShowMenu("cggallery_memo") yoffset 20
            if persistent.hssh_end_2 or persistent.cheat_rosary:
                textbutton 'ロザリオ' action ShowMenu("cggallery_rozario") yoffset 20
            if persistent.titlename == "def":
                add None
            else:
                textbutton "背景画像" action ShowMenu("title_select") yalign 0.5 yoffset 20
        textbutton '戻る' action Return() xalign 0.05 yalign 0.95





image memo0 = Text("「今からおよそ二千年前、\n天地がひっくり返る程の大災害があった。」\n「禍の後、男は神からのお告げを受け、\n国を立て直せる程の力と知恵を手に入れた。」\n\n\nキミはおつむは残念だけど、\n物覚えは早いんだし暗記でもしておくといいよ。\n - キミのセンパイ", size=25, text_align=0.5, line_leading=10)

screen memo1:
    add "main_memo2.png"
    text "{rb}禍  {/rb}{rt}ペスティス{/rt}":
        xpos 270
        ypos 330
    text "大災難以来、所々で起きている異常現象。\n人間の力では断じて対抗できない絶対的な力。\n現代科学で説明できない全ての怪現象を称する。\n地と人が死にゆく主な原因。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo4:
    add "main_memo2.png"
    text "州都":
        xpos 270
        ypos 320
    text "人の住めない土地になってしまった大陸で唯一\n人が住めるように浄化された地。\n魔導部の結界によって保護されている。\n交流はないが、州都の外にも禍に抗いながら生きている\n少数の人が存在すると言い伝えられている。\n狭い意味ではセイント・シェオル周辺繁華街の事を\n指している場合もある。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo3:
    add "main_memo2.png"
    text "力場":
        xpos 270
        ypos 320
    text "禍が起こる区域。種類は時によって異なり、\n一か所にに停まることはない。\n力場の流れに逆らわない為には「規則」を知るべきであり、\nそれを充実に守れば誰でも力場から無事出られるだろう。\n充実に守れれば、だが。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo5:
    add "main_memo2.png"
    text "神聖力":
        xpos 270
        ypos 320
    text "大新人類の身体に流れる魔力。\n現人類はこの力を駆使することで「力場」を探知し、\n「禍」から生き残る事が出来る。\n個人の持つ神聖力の強さは生まれる時から決まっていて、\n後天的に変化した例はまだない。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo6:
    add "main_memo2.png"
    text "神聖術":
        xpos 270
        ypos 320
    text "神聖力を駆使する術。\n生まれ持つ能力は人それぞれであり、\n駆使する方法がわからなければ扱うことが出来ないため\n魔導師でない者の中で神聖術を使う者は極僅か。\n\n※義務教育を終えなかった者が神聖術を使うことは\n法律にて禁じられている。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo7:
    add "main_memo2.png"
    text "聖痕":
        xpos 270
        ypos 320
    text "身身体に流れる「神聖力」の力量を測れる十字型の傷。\n人によって個数や現る箇所が違い、\n通常傷同士が繋がった形で現れる。\n遅くても七歳前までには発現する傾向にある。\nあくまでも「傷痕」であるため、必ず個人の神聖力に\n比例するとは限らない。\n※聖痕を真似た刺青やタトゥーは違法":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo8:
    add "main_memo2.png"
    text "神殿":
        xpos 270
        ypos 320
    text "人々を「禍」から護り、彼らの世話をするために\n設立された機関。神殿は中央教皇庁を中心に、\n六つの大陸にそれぞれ一つずつ存在する。\n我々が所属している場所は、エカルラン現枢機卿が\n管理している北大陸の「セイント・シェオル」\n神殿と距離が遠い州都の外側では小さな教会が\nその役割を果たしている。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo9:
    add "main_memo2.png"
    text "亡者":
        xpos 270
        ypos 320
    text "人間が死んだ後にもその身体を流れる「神聖力」は\n消えない為、「処理」を怠るとその神聖力を\n使い尽くすまで動き続ける。\n逆に魂だけが彷徨う状態は「亡霊」と呼ぶ。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo10:
    add "main_memo2.png"
    text "枢機卿":
        xpos 270
        ypos 320
    text "神殿を管理するため「神託」によって選ばれる人間。\n神託を得た者はその瞬間から歳老わず、傷の癒しが早まり、\n空腹を感じない存在となり祀られる事となる。\n枢機卿の仕事は主に「神託」を受ける事であり、\nこの仕事は次期枢機卿が決定されるまで続く。":
        size 25
        line_leading 10
        xpos 270
        ypos 380


screen memo11:
    add "main_memo2.png"
    text "主教":
        xpos 270
        ypos 320
    text "枢機卿によって選ばれる部署の総責任者。\n通常は正式司祭の中から選ばれる。\n彼らが一任される部署は通常魔導師、学術部、保健部の\n三つに分かれるが、セイント・シェオルには\n「浄化部」という第4の部署が存在する。\n他にも主教が存在せず、枢機卿自らの指揮によって神殿の\n行政業務のみを行う「行政府」も存在している。":
        size 25
        line_leading 10
        xpos 270
        ypos 380


screen memo12:
    add "main_memo2.png"
    text "補佐教":
        xpos 270
        ypos 320
    text "主教を補佐する司祭の名称。\n一年以上勤務した正式司祭の中から主教によって選ばれる。\n特別な「職位」としての権力が得られるわけではないが、\n現在としては主教よりも補佐教の影響力によって\n部署の雰囲気が決定されるところがある。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo13:
    add "main_memo2.png"
    text "聖夜祭":
        xpos 270
        ypos 320
    text "神の祝福と新たな命の誕生を祝う祭典。\nこの日、魔導士たちは州都の結界を補強し、\n来たる一年を迎えるための準備を行う。\n人々は互いの誕生を祝いながら、\nこの日をもってまた一つ歳を老う。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo14:
    add "main_memo2.png"
    text "魔導部":
        xpos 270
        ypos 320
    text "「神聖術」を教育し、禍から人々を護るための\n魔導師を育成する部署。\nその力だけでも相当な影響力を持つ。\n遺伝による神聖力に依存する傾向があるため、\n血縁関係が重視される。\n\n※魔導師を真似る様な黒髪に染める事は禁じられている。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo15:
    add "main_memo2.png"
    text "学術部":
        xpos 270
        ypos 320
    text "旧人類の痕跡を発掘し実生活で利用できるように\n研究したり禍の力場を観察しその法則を研究する部署。\n年に一度行う試験の結果によって\n入社出来るかどうかが関わる。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo16:
    add "main_memo2.png"
    text "保健部":
        xpos 270
        ypos 320
    text "禍によって怪我を負った人々を癒し、神殿で働く司祭達の\nケアをするための部署。\nこの部署の司祭たちは指定の衣装を着る事はあまりなく、\n日夜を問わず常に忙しい。\n主に「治癒術」と呼ばれる神聖術を駆使する。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo17:
    add "main_memo2.png"
    text "{rb}浄化部{/rb}{rt}せいかぶ{/rt}":
        xpos 270
        ypos 320
    text "3年前、現枢機卿によって設立された特別部署。\n本来魔導師の後に付き様々な後始末を行う\n「処理班」という名の集団であったが、\nいつしか部署として成立するようになった。\n個人が処理するに手が余るような後始末のお手伝いが\n仕事だ。過酷な作業環境のせいで定期的に\n新入社員を募集しているが、常に人不足。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo18:
    add "main_memo2.png"
    text "季節歴":
        xpos 270
        ypos 320
    text "北大陸で使用される公式の暦。\n神の誕生日を称える聖夜祭を基点とし、\n季節に基づいて日付を計算する。\n古代人が用いていた日付の基準は「数字暦」と呼ばれ、\n古代に関する研究や呪術などに用いられている。":
        size 25
        line_leading 10
        xpos 270
        ypos 380

screen memo2:
    add "main_memo2.png"


init:
    screen cggallery_memo:
        tag menu




        add "bgw"
        add gui.main_menu_background
        add "main_gallery.png"
        add "main_memo.png"
        add "main_memo2.png"
        if config.language == "English":
            add "memo0":
                xpos 335
                ypos 310
        elif config.language == "SimplifiedChinese":
            add "memo0":
                xpos 305
                ypos 310

        elif config.language == "Korean":
            add "memo0":
                xpos 285
                ypos 310
        else:
            add "memo0":
                xpos 330
                ypos 310

        text "ギャラリー":
            xpos 40
            ypos 33
            xalign 0
            style "main_menu_title"
        vbox:
            style_prefix "place"

            xpos 0.05
            yalign 0.5
            spacing gui.navigation_spacing
            textbutton '1' action ShowMenu("cggallery1") xalign 0.05 yalign 0.4
            textbutton '2' action ShowMenu("cggallery2") xalign 0.05 yalign 0.5
            textbutton '3' action ShowMenu("cggallery3") xalign 0.05 yalign 0.5
            textbutton '4' action ShowMenu("cggallery4") xalign 0.05 yalign 0.5
            textbutton 'ノート' action ShowMenu("cggallery_memo") yoffset 20
            if persistent.hssh_end_2 or persistent.cheat_rosary:
                textbutton 'ロザリオ' action ShowMenu("cggallery_rozario") yoffset 20
            if persistent.titlename == "def":
                add None
            else:
                textbutton "背景画像" action ShowMenu("title_select") yalign 0.5 yoffset 20
        textbutton '戻る' action Return() xalign 0.05 yalign 0.95

        if config.language == "English":
            hbox:
                style_prefix "place"

                textbutton _("{size=28}禍{/size}"):
                    hovered Show('memo1')
                    unhovered Hide('memo1')
                    action Show('memo1')

                textbutton _("{size=28}州都{/size}"):
                    hovered Show('memo4')
                    unhovered Hide('memo4')
                    action Show('memo4')

                textbutton _("{size=28}力場{/size}"):
                    hovered Show('memo3')
                    unhovered Hide('memo3')
                    action Show('memo3')

                textbutton _("{size=28}神聖力{/size}"):
                    hovered Show('memo5')
                    unhovered Hide('memo5')
                    action Show('memo5')

                textbutton _("{size=28}神聖術{/size}"):
                    hovered Show('memo6')
                    unhovered Hide('memo6')
                    action Show('memo6')

                textbutton _("{size=28}聖痕{/size}"):
                    hovered Show('memo7')
                    unhovered Hide('memo7')
                    action Show('memo7')

                xpos 250
                ypos 120
                spacing 14

            hbox:
                style_prefix "place"

                textbutton _("{size=28}神殿{/size}"):
                    hovered Show('memo8')
                    unhovered Hide('memo8')
                    action Show('memo8')

                textbutton _("{size=28}亡者{/size}"):
                    hovered Show('memo9')
                    unhovered Hide('memo9')
                    action Show('memo9')

                textbutton _("{size=28}枢機卿{/size}"):
                    hovered Show('memo10')
                    unhovered Hide('memo10')
                    action Show('memo10')

                textbutton _("{size=28}主教{/size}"):
                    hovered Show('memo11')
                    unhovered Hide('memo11')
                    action Show('memo11')

                textbutton _("{size=28}補佐教{/size}"):
                    hovered Show('memo12')
                    unhovered Hide('memo12')
                    action Show('memo12')

                xpos 260
                ypos 150
                spacing 46

            hbox:
                style_prefix "place"

                textbutton _("{size=28}聖夜祭{/size}"):
                    hovered Show('memo13')
                    unhovered Hide('memo13')
                    action Show('memo13')

                textbutton _("{size=28}季節歴{/size}"):
                    hovered Show('memo18')
                    unhovered Hide('memo18')
                    action Show('memo18')

                textbutton _("{size=28}魔導部{/size}"):
                    hovered Show('memo14')
                    unhovered Hide('memo14')
                    action Show('memo14')

                xpos 260
                ypos 180
                spacing 56

            hbox:
                style_prefix "place"

                textbutton _("{size=28}学術部{/size}"):
                    hovered Show('memo15')
                    unhovered Hide('memo15')
                    action Show('memo15')

                textbutton _("{size=28}保健部{/size}"):
                    hovered Show('memo16')
                    unhovered Hide('memo16')
                    action Show('memo16')

                textbutton _("{size=28}浄化部{/size}"):
                    hovered Show('memo17')
                    unhovered Hide('memo17')
                    action Show('memo17')

                xpos 250
                ypos 210
                spacing 34
        elif config.language == "Korean":
            hbox:
                style_prefix "place"

                textbutton _("{size=28}禍{/size}"):
                    hovered Show('memo1')
                    unhovered Hide('memo1')
                    action Show('memo1')

                textbutton _("{size=28}州都{/size}"):
                    hovered Show('memo4')
                    unhovered Hide('memo4')
                    action Show('memo4')

                textbutton _("{size=28}力場{/size}"):
                    hovered Show('memo3')
                    unhovered Hide('memo3')
                    action Show('memo3')

                textbutton _("{size=28}神聖力{/size}"):
                    hovered Show('memo5')
                    unhovered Hide('memo5')
                    action Show('memo5')

                textbutton _("{size=28}神聖術{/size}"):
                    hovered Show('memo6')
                    unhovered Hide('memo6')
                    action Show('memo6')

                textbutton _("{size=28}聖痕{/size}"):
                    hovered Show('memo7')
                    unhovered Hide('memo7')
                    action Show('memo7')

                xpos 260
                ypos 120
                spacing 35

            hbox:
                style_prefix "place"

                textbutton _("{size=28}神殿{/size}"):
                    hovered Show('memo8')
                    unhovered Hide('memo8')
                    action Show('memo8')

                textbutton _("{size=28}亡者{/size}"):
                    hovered Show('memo9')
                    unhovered Hide('memo9')
                    action Show('memo9')

                textbutton _("{size=28}枢機卿{/size}"):
                    hovered Show('memo10')
                    unhovered Hide('memo10')
                    action Show('memo10')

                textbutton _("{size=28}主教{/size}"):
                    hovered Show('memo11')
                    unhovered Hide('memo11')
                    action Show('memo11')

                textbutton _("{size=28}補佐教{/size}"):
                    hovered Show('memo12')
                    unhovered Hide('memo12')
                    action Show('memo12')

                textbutton _("{size=28}聖夜祭{/size}"):
                    hovered Show('memo13')
                    unhovered Hide('memo13')
                    action Show('memo13')

                xpos 260
                ypos 160
                spacing 30

            hbox:
                style_prefix "place"

                textbutton _("{size=28}季節歴{/size}"):
                    hovered Show('memo18')
                    unhovered Hide('memo18')
                    action Show('memo18')

                textbutton _("{size=28}魔導部{/size}"):
                    hovered Show('memo14')
                    unhovered Hide('memo14')
                    action Show('memo14')

                textbutton _("{size=28}学術部{/size}"):
                    hovered Show('memo15')
                    unhovered Hide('memo15')
                    action Show('memo15')

                textbutton _("{size=28}保健部{/size}"):
                    hovered Show('memo16')
                    unhovered Hide('memo16')
                    action Show('memo16')

                textbutton _("{size=28}浄化部{/size}"):
                    hovered Show('memo17')
                    unhovered Hide('memo17')
                    action Show('memo17')

                xpos 260
                ypos 200
                spacing 40

        else:
            hbox:
                style_prefix "place"

                textbutton _("{size=28}禍{/size}"):
                    hovered Show('memo1')
                    unhovered Hide('memo1')
                    action Show('memo1')

                textbutton _("{size=28}州都{/size}"):
                    hovered Show('memo4')
                    unhovered Hide('memo4')
                    action Show('memo4')

                textbutton _("{size=28}力場{/size}"):
                    hovered Show('memo3')
                    unhovered Hide('memo3')
                    action Show('memo3')

                textbutton _("{size=28}神聖力{/size}"):
                    hovered Show('memo5')
                    unhovered Hide('memo5')
                    action Show('memo5')

                textbutton _("{size=28}神聖術{/size}"):
                    hovered Show('memo6')
                    unhovered Hide('memo6')
                    action Show('memo6')

                textbutton _("{size=28}聖痕{/size}"):
                    hovered Show('memo7')
                    unhovered Hide('memo7')
                    action Show('memo7')

                xpos 260
                ypos 120
                spacing 40

            hbox:
                style_prefix "place"

                textbutton _("{size=28}神殿{/size}"):
                    hovered Show('memo8')
                    unhovered Hide('memo8')
                    action Show('memo8')

                textbutton _("{size=28}亡者{/size}"):
                    hovered Show('memo9')
                    unhovered Hide('memo9')
                    action Show('memo9')

                textbutton _("{size=28}枢機卿{/size}"):
                    hovered Show('memo10')
                    unhovered Hide('memo10')
                    action Show('memo10')

                textbutton _("{size=28}主教{/size}"):
                    hovered Show('memo11')
                    unhovered Hide('memo11')
                    action Show('memo11')

                textbutton _("{size=28}補佐教{/size}"):
                    hovered Show('memo12')
                    unhovered Hide('memo12')
                    action Show('memo12')

                textbutton _("{size=28}聖夜祭{/size}"):
                    hovered Show('memo13')
                    unhovered Hide('memo13')
                    action Show('memo13')

                xpos 260
                ypos 160
                spacing 40

            hbox:
                style_prefix "place"

                textbutton _("{size=28}季節歴{/size}"):
                    hovered Show('memo18')
                    unhovered Hide('memo18')
                    action Show('memo18')

                textbutton _("{size=28}魔導部{/size}"):
                    hovered Show('memo14')
                    unhovered Hide('memo14')
                    action Show('memo14')

                textbutton _("{size=28}学術部{/size}"):
                    hovered Show('memo15')
                    unhovered Hide('memo15')
                    action Show('memo15')

                textbutton _("{size=28}保健部{/size}"):
                    hovered Show('memo16')
                    unhovered Hide('memo16')
                    action Show('memo16')

                textbutton _("{size=28}浄化部{/size}"):
                    hovered Show('memo17')
                    unhovered Hide('memo17')
                    action Show('memo17')

                xpos 260
                ypos 200
                spacing 40

























































































































































































































































































































































































































































screen cggallery_rozario:
    tag menu

    add "bgw"
    add gui.main_menu_background
    add "main_gallery.png"
    add "main_memo.png"
    add "main_memo2.png"

    text "ギャラリー":
        xpos 40
        ypos 33
        xalign 0
        style "main_menu_title"
    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing
        textbutton '1' action ShowMenu("cggallery1") xalign 0.05 yalign 0.4
        textbutton '2' action ShowMenu("cggallery2") xalign 0.05 yalign 0.5
        textbutton '3' action ShowMenu("cggallery3") xalign 0.05 yalign 0.5
        textbutton '4' action ShowMenu("cggallery4") xalign 0.05 yalign 0.5
        textbutton 'ノート' action ShowMenu("cggallery_memo") yoffset 20
        if persistent.hssh_end_2 or persistent.cheat_rosary:
            textbutton 'ロザリオ' action ShowMenu("cggallery_rozario") yoffset 20
        if persistent.titlename == "def":
            add None
        else:
            textbutton "背景画像" action ShowMenu("title_select") yalign 0.5 yoffset 20
    textbutton '戻る' action Return() xalign 0.05 yalign 0.95

    if config.language == "English":
        hbox:
            style_prefix "place"

            if persistent.sc_end or persistent.cheat_rosary:
                textbutton _("{size=28}マヤ{/size}"):
                    hovered Show('rzro_my')
                    unhovered Hide('rzro_my')
                    action Show('rzro_my')
            else:
                textbutton _("{size=28}マヤ{/size}"):
                    action None

            if persistent.sc_end or persistent.cheat_rosary:
                textbutton _("{size=28}シーキュレット{/size}"):
                    hovered Show('rzro_sc')
                    unhovered Hide('rzro_sc')
                    action Show('rzro_sc')
            else:
                textbutton _("{size=28}シーキュレット{/size}"):
                    action None

            if persistent.hk_end or persistent.cheat_rosary:
                textbutton _("{size=28}ハク{/size}"):
                    hovered Show('rzro_hk')
                    unhovered Hide('rzro_hk')
                    action Show('rzro_hk')
            else:
                textbutton _("{size=28}ハク{/size}"):
                    action None

            if persistent.ar_end or persistent.cheat_rosary:
                textbutton _("{size=28}アルネ{/size}"):
                    hovered Show('rzro_ar')
                    unhovered Hide('rzro_ar')
                    action Show('rzro_ar')
            else:
                textbutton _("{size=28}アルネ{/size}"):
                    action None

            if persistent.ar_end or persistent.cheat_rosary:
                textbutton _("{size=28}エノク{/size}"):
                    hovered Show('rzro_en')
                    unhovered Hide('rzro_en')
                    action Show('rzro_en')
            else:
                textbutton _("{size=28}エノク{/size}"):
                    action None

            if persistent.ar_end or persistent.cheat_rosary:
                textbutton _("{size=28}エルジェーベト{/size}"):
                    hovered Show('rzro_er')
                    unhovered Hide('rzro_er')
                    action Show('rzro_er')
            else:
                textbutton _("{size=28}エルジェーベト{/size}"):
                    action None
            xpos 260
            ypos 140
            spacing 25

        hbox:
            style_prefix "place"

            if persistent.rs_end or persistent.cheat_rosary:
                textbutton _("{size=28}ラヴィアン{/size}"):
                    hovered Show('rzro_rv')
                    unhovered Hide('rzro_rv')
                    action Show('rzro_rv')
            else:
                textbutton _("{size=28}ラヴィアン{/size}"):
                    action None

            if persistent.rs_end or persistent.cheat_rosary:
                textbutton _("{size=28}ローズ{/size}"):
                    hovered Show('rzro_rs')
                    unhovered Hide('rzro_rs')
                    action Show('rzro_rs')
            else:
                textbutton _("{size=28}ローズ{/size}"):
                    action None

            if persistent.rs_end or persistent.cheat_rosary:
                textbutton _("{size=28}イヴリン{/size}"):
                    hovered Show('rzro_ev')
                    unhovered Hide('rzro_ev')
                    action Show('rzro_ev')
            else:
                textbutton _("{size=28}イヴリン{/size}"):
                    action None

            if persistent.gr_end or persistent.cheat_rosary:
                textbutton _("{size=28}グレーテ{/size}"):
                    hovered Show('rzro_gr')
                    unhovered Hide('rzro_gr')
                    action Show('rzro_gr')
            else:
                textbutton _("{size=28}グレーテ{/size}"):
                    action None

            if persistent.gr_end or persistent.cheat_rosary:
                textbutton _("{size=28}グレゴール{/size}"):
                    hovered Show('rzro_gg')
                    unhovered Hide('rzro_gg')
                    action Show('rzro_gg')
            else:
                textbutton _("{size=28}グレゴール{/size}"):
                    action None

            if persistent.cr_end or persistent.cheat_rosary:
                textbutton _("{size=28}クリオネ{/size}"):
                    hovered Show('rzro_cr')
                    unhovered Hide('rzro_cr')
                    action Show('rzro_cr')
            else:
                textbutton _("{size=28}クリオネ{/size}"):
                    action None

            textbutton _("{size=28}[persistent.na]{/size}"):
                hovered Show('rzro_ore')
                unhovered Hide('rzro_ore')
                action Show('rzro_ore')

            xpos 260
            ypos 180
            spacing 15

    elif config.language == "Korean":
        hbox:
            style_prefix "place"

            if persistent.sc_end or persistent.cheat_rosary:
                textbutton _("{size=28}マヤ{/size}"):
                    hovered Show('rzro_my')
                    unhovered Hide('rzro_my')
                    action Show('rzro_my')
            else:
                textbutton _("{size=28}マヤ{/size}"):
                    action None

            if persistent.sc_end or persistent.cheat_rosary:
                textbutton _("{size=28}シーキュレット{/size}"):
                    hovered Show('rzro_sc')
                    unhovered Hide('rzro_sc')
                    action Show('rzro_sc')
            else:
                textbutton _("{size=28}シーキュレット{/size}"):
                    action None

            if persistent.hk_end or persistent.cheat_rosary:
                textbutton _("{size=28}ハク{/size}"):
                    hovered Show('rzro_hk')
                    unhovered Hide('rzro_hk')
                    action Show('rzro_hk')
            else:
                textbutton _("{size=28}ハク{/size}"):
                    action None

            if persistent.ar_end or persistent.cheat_rosary:
                textbutton _("{size=28}アルネ{/size}"):
                    hovered Show('rzro_ar')
                    unhovered Hide('rzro_ar')
                    action Show('rzro_ar')
            else:
                textbutton _("{size=28}アルネ{/size}"):
                    action None

            if persistent.ar_end or persistent.cheat_rosary:
                textbutton _("{size=28}エノク{/size}"):
                    hovered Show('rzro_en')
                    unhovered Hide('rzro_en')
                    action Show('rzro_en')
            else:
                textbutton _("{size=28}エノク{/size}"):
                    action None

            if persistent.ar_end or persistent.cheat_rosary:
                textbutton _("{size=28}エルジェーベト{/size}"):
                    hovered Show('rzro_er')
                    unhovered Hide('rzro_er')
                    action Show('rzro_er')
            else:
                textbutton _("{size=28}エルジェーベト{/size}"):
                    action None
            xpos 260
            ypos 120
            spacing 25

        hbox:
            style_prefix "place"

            if persistent.rs_end or persistent.cheat_rosary:
                textbutton _("{size=28}ラヴィアン{/size}"):
                    hovered Show('rzro_rv')
                    unhovered Hide('rzro_rv')
                    action Show('rzro_rv')
            else:
                textbutton _("{size=28}ラヴィアン{/size}"):
                    action None

            if persistent.rs_end or persistent.cheat_rosary:
                textbutton _("{size=28}ローズ{/size}"):
                    hovered Show('rzro_rs')
                    unhovered Hide('rzro_rs')
                    action Show('rzro_rs')
            else:
                textbutton _("{size=28}ローズ{/size}"):
                    action None

            if persistent.rs_end or persistent.cheat_rosary:
                textbutton _("{size=28}イヴリン{/size}"):
                    hovered Show('rzro_ev')
                    unhovered Hide('rzro_ev')
                    action Show('rzro_ev')
            else:
                textbutton _("{size=28}イヴリン{/size}"):
                    action None

            if persistent.gr_end or persistent.cheat_rosary:
                textbutton _("{size=28}グレーテ{/size}"):
                    hovered Show('rzro_gr')
                    unhovered Hide('rzro_gr')
                    action Show('rzro_gr')
            else:
                textbutton _("{size=28}グレーテ{/size}"):
                    action None

            if persistent.gr_end or persistent.cheat_rosary:
                textbutton _("{size=28}グレゴール{/size}"):
                    hovered Show('rzro_gg')
                    unhovered Hide('rzro_gg')
                    action Show('rzro_gg')
            else:
                textbutton _("{size=28}グレゴール{/size}"):
                    action None

            if persistent.cr_end or persistent.cheat_rosary:
                textbutton _("{size=28}クリオネ{/size}"):
                    hovered Show('rzro_cr')
                    unhovered Hide('rzro_cr')
                    action Show('rzro_cr')
            else:
                textbutton _("{size=28}クリオネ{/size}"):
                    action None

            xpos 260
            ypos 160
            spacing 15

        hbox:
            style_prefix "place"

            textbutton _("{size=28}[persistent.na]{/size}"):
                hovered Show('rzro_ore')
                unhovered Hide('rzro_ore')
                action Show('rzro_ore')

            xpos 260
            ypos 200
            spacing 35

    else:
        hbox:
            style_prefix "place"

            if persistent.sc_end or persistent.cheat_rosary:
                textbutton _("{size=28}マヤ{/size}"):
                    hovered Show('rzro_my')
                    unhovered Hide('rzro_my')
                    action Show('rzro_my')
            else:
                textbutton _("{size=28}マヤ{/size}"):
                    action None

            if persistent.sc_end or persistent.cheat_rosary:
                textbutton _("{size=28}シーキュレット{/size}"):
                    hovered Show('rzro_sc')
                    unhovered Hide('rzro_sc')
                    action Show('rzro_sc')
            else:
                textbutton _("{size=28}シーキュレット{/size}"):
                    action None

            if persistent.hk_end or persistent.cheat_rosary:
                textbutton _("{size=28}ハク{/size}"):
                    hovered Show('rzro_hk')
                    unhovered Hide('rzro_hk')
                    action Show('rzro_hk')
            else:
                textbutton _("{size=28}ハク{/size}"):
                    action None

            if persistent.ar_end or persistent.cheat_rosary:
                textbutton _("{size=28}アルネ{/size}"):
                    hovered Show('rzro_ar')
                    unhovered Hide('rzro_ar')
                    action Show('rzro_ar')
            else:
                textbutton _("{size=28}アルネ{/size}"):
                    action None

            if persistent.ar_end or persistent.cheat_rosary:
                textbutton _("{size=28}エノク{/size}"):
                    hovered Show('rzro_en')
                    unhovered Hide('rzro_en')
                    action Show('rzro_en')
            else:
                textbutton _("{size=28}エノク{/size}"):
                    action None

            xpos 260
            ypos 120
            spacing 35

        hbox:
            style_prefix "place"

            if persistent.ar_end or persistent.cheat_rosary:
                textbutton _("{size=28}エルジェーベト{/size}"):
                    hovered Show('rzro_er')
                    unhovered Hide('rzro_er')
                    action Show('rzro_er')
            else:
                textbutton _("{size=28}エルジェーベト{/size}"):
                    action None

            if persistent.rs_end or persistent.cheat_rosary:
                textbutton _("{size=28}ラヴィアン{/size}"):
                    hovered Show('rzro_rv')
                    unhovered Hide('rzro_rv')
                    action Show('rzro_rv')
            else:
                textbutton _("{size=28}ラヴィアン{/size}"):
                    action None

            if persistent.rs_end or persistent.cheat_rosary:
                textbutton _("{size=28}ローズ{/size}"):
                    hovered Show('rzro_rs')
                    unhovered Hide('rzro_rs')
                    action Show('rzro_rs')
            else:
                textbutton _("{size=28}ローズ{/size}"):
                    action None

            if persistent.rs_end or persistent.cheat_rosary:
                textbutton _("{size=28}イヴリン{/size}"):
                    hovered Show('rzro_ev')
                    unhovered Hide('rzro_ev')
                    action Show('rzro_ev')
            else:
                textbutton _("{size=28}イヴリン{/size}"):
                    action None

            xpos 260
            ypos 160
            spacing 35

        hbox:
            style_prefix "place"

            if persistent.gr_end or persistent.cheat_rosary:
                textbutton _("{size=28}グレーテ{/size}"):
                    hovered Show('rzro_gr')
                    unhovered Hide('rzro_gr')
                    action Show('rzro_gr')
            else:
                textbutton _("{size=28}グレーテ{/size}"):
                    action None

            if persistent.gr_end or persistent.cheat_rosary:
                textbutton _("{size=28}グレゴール{/size}"):
                    hovered Show('rzro_gg')
                    unhovered Hide('rzro_gg')
                    action Show('rzro_gg')
            else:
                textbutton _("{size=28}グレゴール{/size}"):
                    action None

            if persistent.cr_end or persistent.cheat_rosary:
                textbutton _("{size=28}クリオネ{/size}"):
                    hovered Show('rzro_cr')
                    unhovered Hide('rzro_cr')
                    action Show('rzro_cr')
            else:
                textbutton _("{size=28}クリオネ{/size}"):
                    action None

            textbutton _("{size=28}[persistent.na]{/size}"):
                hovered Show('rzro_ore')
                unhovered Hide('rzro_ore')
                action Show('rzro_ore')

            xpos 260
            ypos 200
            spacing 35
screen rzro_ore:
    add "main_memo2.png"
    text "[persistent.na]":
        xpos 270
        ypos 310
    text "身長：173cm\n血液型：A\n所属部署：浄化部\n聖痕：◆◆\n人事評価：勤務実績は無難だが、仮病を装う傾向有。\n職務怠慢。態度不良。容姿不良。\nまずは遅刻を無くすように。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350
screen rzro_my:
    add "main_memo2.png"
    text "マヤ・エルベット":
        xpos 270
        ypos 310
    text "身長：144cm\n血液型：B\n所属部署：浄化部\n聖痕：◆◆\n人事評価：場合によっての乱調が酷い司祭です。\nしかし仕事ぶりが丁寧なため、ミスが少ないという\n長所があります。\n本人が努力を継続できる様、持続的な指導が必要です。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350
screen rzro_sc:
    add "main_memo2.png"
    text "シーキュレット・レイフ":
        xpos 270
        ypos 310
    text "身長：154cm\n血液型：O\n所属部署：浄化部\n聖痕：◆◆◆\n人事評価：仕事効率がとても良く、\n優秀ですが臨機応変に弱い傾向がある司祭です。\n特に負傷が多いため、本人の格別な注意が必要です。\nこれからの成長に期待しています":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

screen rzro_hk:
    add "main_memo2.png"
    text "ハク・エカルラン":
        xpos 270
        ypos 310
    text "身長：177cm\n血液型：A\n所属部署：浄化部\n聖痕：確認できず\n人事評価：個人の能力は優れているも、\n本人指揮下の司祭を取り締まる能力が不足しています。\n神殿に被害が及ぶ事のない様精進願います。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

screen rzro_ar:
    add "main_memo2.png"
    text "アルネ・アルタナータ":
        xpos 270
        ypos 310
    text "身長：176cm\n血液型：A\n所属部署：魔導部\n聖痕：◆◆◆◆◆\n人事評価：優秀な技量と、\nこれ以上にない態度で魔導部司祭達の鑑となっています。\n現状維持だけで充分なので、常時本人の安全に気を付け\n健康で居て頂きたい。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

screen rzro_er:
    add "main_memo2.png"
    text "エルジェーベト・アルタナータ":
        xpos 270
        ypos 310
    text "身長：127cm\n血液型：A\n所属部署：魔導部\n聖痕：◆◆◆◆◆◆◆\n人事評価：優秀な実績に依存している為、\n怠り易い傾向にあります。傲慢な態度のせいで交友関係の\n欠乏が特に部署の位相を落とす原因となっています。\nどうか精進願います。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

screen rzro_en:
    add "main_memo2.png"
    text "エノク・アピス":
        xpos 270
        ypos 310
    text "身長：188cm\n血液型：A\n所属部署：魔導部\n聖痕：◆◆◆◆\n人事評価：勤務態度や技量自体は優秀ですが、\n締めが甘い傾向にある為、それらが時折大きいミスへと\n発展する場合があります。誠実なのは良い事だが、\nだからといって周りに気を配る事を怠らない様に。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

screen rzro_rv:
    add "main_memo2.png"
    text "ラヴィアン・ローズ":
        xpos 270
        ypos 310
    text "身長：161.1cm\n血液型：O\n所属部署：学術部\n聖痕：◆◆\n人事評価：私が優秀に育て上げた究極の少年です。\n貴方が神殿で生活為さる上にあたって、\n此の愛しい司祭の力は必然的です。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

screen rzro_rs:
    add "main_memo2.png"
    text "ローズ":
        xpos 270
        ypos 310
    text "身長：161.1cm\n血液型：O\n所属部署：学術部\n聖痕：◆◆◆\nロザリオ型の木で出来た首飾り。\n精巧に仕上げられており、銀色に塗色してある。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

screen rzro_ev:
    add "main_memo2.png"
    text "イヴリン・ヴィオレッタ":
        xpos 270
        ypos 310
    text "身長：168cm\n血液型：AB\n所属部署：学術部\n聖痕：◆◆◆◆\n人事評価：容貌端正で優秀な主教です。\nこれからも傑出した知識で神殿の位相を高めてください。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

screen rzro_gr:
    add "main_memo2.png"
    text "グレーテ・コーニッシュ":
        xpos 270
        ypos 310
    text "身長：150cm\n血液型：AB\n所属部署：保健部\n聖痕：◆\n人事評価：勤務時間が長いだけあって、\n神殿の精神的な支えとなってくれている\n熟練した司祭である。\nしかしあまり私的な雑談を業務時間内にしない事！":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

screen rzro_gg:
    add "main_memo2.png"
    text "グレゴール・コーニッシュ":
        xpos 270
        ypos 310
    text "身長：185cm\n血液型：B\n所属部署：保健部\n聖痕：◆◆◆◆\n人事評価：真面目な司祭です。\n１階お手洗いの電球が切れておりましたので、\nご確認をお願いいたします。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

screen rzro_cr:
    add "main_memo2.png"
    text "クリオネ・ミオソティス":
        xpos 270
        ypos 310
    text "身長：132cm\n血液型：AB\n聖痕：◆\n周りの評価：\n司祭A：かわい～～好き！\n司祭B：この前ボールペンを貸して貰った事があるんだ。\n司祭C：ウサギに餌をやることを手伝ってもらった。\n本当にいい子だよ。":
        size 25
        if config.language == "English":
            line_leading 5
        else:
            line_leading 8
        xpos 270
        ypos 350

init:
    screen title_select:
        tag menu

        add "bgw"
        add gui.main_menu_background
        add "main_gallery.png"

        text "ギャラリー":
            xpos 40
            ypos 33
            xalign 0
            style "main_menu_title"
        vbox:
            style_prefix "place"

            xpos 0.05
            yalign 0.5
            spacing gui.navigation_spacing
            textbutton '1' action ShowMenu("cggallery1") xalign 0.05 yalign 0.4
            textbutton '2' action ShowMenu("cggallery2") xalign 0.05 yalign 0.5
            textbutton '3' action ShowMenu("cggallery3") xalign 0.05 yalign 0.5
            textbutton '4' action ShowMenu("cggallery4") xalign 0.05 yalign 0.5
            textbutton 'ノート' action ShowMenu("cggallery_memo") yoffset 20
            if persistent.hssh_end_2 or persistent.cheat_rosary:
                textbutton 'ロザリオ' action ShowMenu("cggallery_rozario") yoffset 20
            if persistent.titlename == "def":
                add None
            else:
                textbutton "背景画像" action ShowMenu("title_select") yalign 0.5 yoffset 20
        textbutton '戻る' action Return() xalign 0.05 yalign 0.95

        vbox:
            style_prefix "place"
            frame:
                xpadding 50
                ypadding 50
                xalign 0.5
                yalign 0.5
                has vbox
                spacing gui.navigation_spacing
                if persistent.title_hk == False and persistent.cheat_title == False:
                    textbutton "デフォルト" action [SetVariable("persistent.titlename", "def2"), renpy.save_persistent()]

                if persistent.title_my or persistent.cheat_title:
                    textbutton "{size=28}マヤ{/size}" action [SetVariable("persistent.titlename", "my"), renpy.save_persistent()]

                if persistent.title_sc or persistent.cheat_title:
                    textbutton "{size=28}シーキュレット{/size}" action [SetVariable("persistent.titlename", "sc"), renpy.save_persistent()]

                if persistent.title_ar or persistent.cheat_title:
                    textbutton "{size=28}アルネ{/size}" action [SetVariable("persistent.titlename", "ar"), renpy.save_persistent()]

                if persistent.title_rs or persistent.cheat_title:
                    textbutton "{size=28}ローズ{/size}" action [SetVariable("persistent.titlename", "rs"), renpy.save_persistent()]

                if persistent.title_gr or persistent.cheat_title:
                    textbutton "{size=28}グレーテ{/size}" action [SetVariable("persistent.titlename", "gr"), renpy.save_persistent()]

                if persistent.title_cr or persistent.cheat_title:
                    textbutton "{size=28}クリオネ{/size}" action [SetVariable("persistent.titlename", "cr"), renpy.save_persistent()]

                if persistent.title_hk or persistent.cheat_title:
                    textbutton "{size=28}ハク{/size}" action [SetVariable("persistent.titlename", "hk"), renpy.save_persistent()]
            xpos 260
            yalign 0.5

init:



    image BG05 = Image("bg05_1.png")
    image BG12 = Image("bg12.png")

    transform transpa:
        alpha 0.1

    transform transpa2:
        alpha 0.5

    python hide:

        def gen_randmotion(count, dist, delay):
            
            import random
            
            args = [ ]
            
            for i in range(0, count):
                args.append(anim.State(i, None,
                               Position(xpos=random.randrange(-dist, dist),
                                        ypos=random.randrange(-dist, dist),
                                        xanchor='left',
                                        yanchor='top',
                                        )))
            
            for i in range(0, count):
                for j in range(0, count):
                    
                    if i == j:
                        continue
                    
                    args.append(anim.Edge(i, delay, j, MoveTransition(delay)))
            
            return anim.SMAnimation(0, *args)

        store.randmotion = gen_randmotion(5, 5, 1.0)




init python:
    def double_vision_on(picture):
        
        
        
        renpy.show(picture)
        
        renpy.show(picture, at_list=[transpa,randmotion], tag="blur_image")
        
        renpy.with_statement(dissolve)
    def double_vision_on2(picture):
        
        
        
        renpy.show(picture)
        
        renpy.show(picture, at_list=[transpa,randmotion], tag="blur_image2")
        
        renpy.with_statement(dissolve)
    def double_vision_off():
        
        renpy.hide("blur_image")
        
        renpy.with_statement(dissolve)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
