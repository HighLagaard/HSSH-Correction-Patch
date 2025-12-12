



define config.steam_appid = 2093610

init -2:
    $ achievement.register("hss_ending")
    $ achievement.register("cr_end")
    $ achievement.register("ar_end")
    $ achievement.register("rs_end")
    $ achievement.register("gr_end")
    $ achievement.register("sc_end")
    $ achievement.register("hk_end")
    $ achievement.register("all_end")
    $ achievement.register("maya_love")
    $ achievement.register("outsider")

label love:
    $ love_my = 0
    $ love_ar = 0
    $ love_hk = 0
    $ love_gr = 0
    $ love_rs = 0
    $ love_cr = 0
    return

define meet_my = False
define meet_hk = False
define meet_ar = False
define meet_rs = False
define meet_gr = False
define meet_crea = False
define love_hkb = False
define meet_hkb = False
define hkA = False
define hardmode = False
define hssh_rkn = False
define hssh_end = False

default persistent.lovelovemaya = False
default persistent.dmy = 0
default persistent.hssh12end = False
default persistent.hssh_end_2 = False
default persistent.sc_end = False
default persistent.ar_end = False
default persistent.rs_end = False
default persistent.cr_end = False
default persistent.gr_end = False
default persistent.hk_end = False
default persistent.mylove_end = False
default persistent.no_girls = False

define sc_happy = False
define ar_happy = False
define rs_happy = False
define gr_happy = False
define cr_happy = False

default love_my = 0
default love_ar = 0
default love_hk = 0
default love_gr = 0
default love_rs = 0
default love_cr = 0

default meet_my = False
default meet_hk = False
default meet_ar = False
default meet_rs = False
default meet_gr = False

default day_my = False
default day_ar = False
default day_hk = False
default day_gr = False
default day_rs = False
default day_cr = False

label meet_girl:
    $ meet_my = False
    $ meet_hk = False
    $ meet_ar = False
    $ meet_rs = False
    $ meet_gr = False
    return



label placemenu:
    stop music fadeout 2
    pause 1
    nvl clear
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with slowdissolve
    else:
        scene bg02_1 with slowdissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    pause 2
    $ day_time = 0
    $ day_my = False
    $ day_ar = False
    $ day_hk = False
    $ day_gr = False
    $ day_rs = False
    $ day_cr = False
    show screen nvlbox with dissolve
    $ _history = False
    et "\nさて…{w}どこへ行こうか？"
    $ _history = True
    hide screen nvlbox with dissolve
    nvl clear
    jump day_time


screen place_my:
    if hssh_rkn == True:
        add 'main_menu_myR.png'
    else:
        add 'main_menu_my.png'

screen place_ar:
    if hssh_rkn == True:
        add 'main_menu_arR.png'
    else:
        add 'main_menu_ar.png'

screen place_hk:
    if hssh_rkn == True:
        add 'main_menu_hkR.png'
    else:
        add 'main_menu_hk.png'

screen place_hkB:
    if hssh_rkn == True:
        add 'main_menu_hkBR.png'
    else:
        add 'main_menu_hkB.png'

screen place_hkBR:
    add 'main_menu_hkBRR.png'

screen place_rs:
    add 'main_menu_rs.png'

screen place_gr:
    if hssh_rkn == True:
        add 'main_menu_grR.png'
    else:
        add 'main_menu_gr.png'

screen place_cr:
    if hssh_rkn == True:
        add 'main_menu_crR.png'
    else:
        add 'main_menu_cr.png'



label time_out:
    pause 1
    show screen textbox with dissolve
    if hssh_rkn == True:
        if (day == 1):
            $ save_name = "day 1, 夕, 楽園"
        elif (day == 2):
            $ save_name = "day 2, 夕, 楽園"
        elif (day == 3):
            $ save_name = "day 3, 夕, 楽園"
        elif (day == 4):
            $ save_name = "day 4, 夕, 楽園"
        elif (day == 5):
            $ save_name = "day 5, 夕, 楽園"
    else:
        if (day == 1):
            $ save_name = "day 1, 夕"
        elif (day == 2):
            $ save_name = "day 2, 夕"
        elif (day == 3):
            $ save_name = "day 3, 夕"
        elif (day == 4):
            $ save_name = "day 4, 夕"
        elif (day == 5):
            $ save_name = "day 5, 夕"
    if hssh_rkn == True:
        nar "…そそろそろ戻る時間だ。"
    else:
        nar "…そろそろ暗くなる時間だ。"
    nar "あと一か所済ませて部屋に戻らないとそろそろマズいな。"
    hide screen textbox with dissolve
    pause 1
    return


label day_time:
    if (day == 1):
        if (day_time >= 3):
            jump day1_hakuB
        else:
            show screen place_day1 with fastdissolve
            $ place = renpy.call_screen("place_day1")
    if (day == 2):
        show screen place_day2 with fastdissolve
        $ place = renpy.call_screen("place_day2")

    if (day == 3):
        show screen place_day3 with fastdissolve
        $ place = renpy.call_screen("place_day3")

    if (day == 4):
        show screen place_day4 with fastdissolve
        $ place = renpy.call_screen("place_day4")

    if (day == 5):
        show screen place_day5 with fastdissolve
        $ place = renpy.call_screen("place_day5")

    if (day == 6):
        show screen place_day6 with fastdissolve
        $ place = renpy.call_screen("place_day6")

    if (day == 8):
        show screen place_day8 with fastdissolve
        $ place = renpy.call_screen("place_day8")

    if (day == 62):
        show screen place_day6_rkn with fastdissolve
        $ place = renpy.call_screen("place_day6_rkn")
    else:


        $ place = renpy.call_screen("place")

label day_time_1:
    $ show_quick_menu = False
    if (day_time >= 3):
        jump day1_hakuB
    else:

        if (day == 1):
            show screen place_day1 with fastdissolve
            $ place = renpy.call_screen("place_day1")
        else:
            $ place = renpy.call_screen("place")

label day_time_2:
    $ show_quick_menu = False
    if (day_time == 4):
        call time_out from _call_time_out
        if (day == 2):
            show screen place_day2 with fastdissolve
            $ place = renpy.call_screen("place_day2")
    elif (day_time >= 5):
        jump day2_night
    else:
        if (day == 2):
            show screen place_day2 with fastdissolve
            $ place = renpy.call_screen("place_day2")


label day_time_3:
    $ show_quick_menu = False
    if (day_time >= 3):
        jump day3_night
    elif (day_time == 2):
        call time_out from _call_time_out_1
        if (day == 3):
            show screen place_day3 with fastdissolve
            $ place = renpy.call_screen("place_day3")
    else:
        if (day == 3):
            show screen place_day3 with fastdissolve
            $ place = renpy.call_screen("place_day3")
        else:
            $ place = renpy.call_screen("place")

label day_time_4:
    $ show_quick_menu = False
    if (day_time == 2):
        call time_out from _call_time_out_2
        if (day == 4):
            show screen place_day4 with fastdissolve
            $ place = renpy.call_screen("place_day4")
    elif (day_time >= 3):
        jump day4_night
    else:
        if (day == 4):
            show screen place_day4 with fastdissolve
            $ place = renpy.call_screen("place_day4")

label day_time_5:
    $ show_quick_menu = False
    if (day_time == 1):
        if (love_my==0):
            if (love_ar==0):
                if (love_cr==0):
                    if (love_rs==0):
                        if (love_gr==0):
                            if (love_hk==0):
                                if hssh_rkn == True:
                                    pause 0.001
                                else:
                                    $ hkA = True
        call time_out from _call_time_out_3
        if (day == 5):
            show screen place_day5 with fastdissolve
            $ place = renpy.call_screen("place_day5")
    elif (day_time == 2):
        if (hkA == True):
            jump day5_ev
        else:
            jump day5_night
    else:
        if (day == 5):
            show screen place_day5 with fastdissolve
            $ place = renpy.call_screen("place_day5")


screen place_day1:
    add 'main_menu.png'

    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    text "{font=amii.otf}熱の月 1日    昼{/font}":
        size 16
        xpos 0.04
        yalign 0.25

    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        if (day_my == False):
            textbutton _("{size=28}花壇{/size}"):
                hovered Show('place_my')
                unhovered Hide('place_my')
                action Hide('place_my'), Jump('day1_my')

        if (day_hk == False):
            textbutton _("{size=28}作業場{/size}"):
                hovered Show('place_hk')
                unhovered Hide('place_hk')
                action Hide('place_hk'), Jump('day1_hk')

        if (day_gr == False):
            textbutton _("{size=28}医務室{/size}"):
                hovered Show('place_gr')
                unhovered Hide('place_gr')
                action Hide('place_gr'), Jump('day1_gr')


screen place_day1_hkB:
    add 'main_menu.png'

    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    text "{font=amii.otf}熱の月 1日    夜{/font}":
        size 16
        xpos 0.05
        yalign 0.25
    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        textbutton _("{size=28}？？？{/size}"):
            hovered Show('place_hkB')
            unhovered Hide('place_hkB')
            action Hide('place_hkB'), Jump('day1_hakuB_')

screen place_day5_hkA:
    add 'main_menu.png'

    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    text "{font=amii.otf}熱の月 5日    夜{/font}":
        size 16
        xpos 0.05
        yalign 0.25
    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        if (day_rs == False):
            textbutton _("{size=28}図書館{/size}"):
                hovered Show('place_rs')
                unhovered Hide('place_rs')
                action Hide('place_rs'), Jump('day5_hkA')

screen place_day8_hkB:
    add 'main_menu.png'

    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    text "{font=amii.otf}熱の月 8日    夜{/font}":
        size 16
        xpos 0.05
        yalign 0.25
    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        textbutton _("{size=28}野外礼拝堂{/size}"):
            hovered Show('place_hkB')
            unhovered Hide('place_hkB')
            action Hide('place_hkB'), Jump('day8_hakuB')


screen place_day12_my:
    add 'main_menu.png'

    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    text "{font=amii.otf}熱の月 ？？日    夜{/font}":
        size 16
        xpos 0.05
        yalign 0.25
    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        textbutton _("{size=28}野外礼拝堂{/size}"):
            hovered Show('place_hkB')
            unhovered Hide('place_hkB')
            action Hide('place_hkB'), Jump('day12_my')

screen place_day12_sc:
    add 'main_menu.png'

    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    text "{font=amii.otf}熱の月 ？？日    夜{/font}":
        size 16
        xpos 0.05
        yalign 0.25
    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        textbutton _("{size=28}野外礼拝堂{/size}"):
            hovered Show('place_hkB')
            unhovered Hide('place_hkB')
            action Hide('place_hkB'), Jump('sc_end_1_1')

screen place_day7_hk:
    add 'main_menu.png'

    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    text "{font=amii.otf}熱の月 7日    夜{/font}":
        size 16
        xpos 0.05
        yalign 0.25
    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        textbutton _("{size=28}野外礼拝堂{/size}"):
            hovered Show('place_hkB')
            unhovered Hide('place_hkB')
            action Hide('place_hkB'), Jump('day7_hkR')

screen place_day12_hk:
    add 'main_menu.png'

    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    text "{font=amii.otf}熱の月 12日    夜{/font}":
        size 16
        xpos 0.05
        yalign 0.25
    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        textbutton _("{size=28}野外礼拝堂{/size}"):
            hovered Show('place_hkBR')
            unhovered Hide('place_hkBR')
            action Hide('place_hkBR'), Jump('day12_hk_end')

screen place_day2:
    add 'main_menu.png'

    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    if (day_time >= 4):
        text "{font=amii.otf}熱の月 2日    夕{/font}":
            size 16
            xpos 0.04
            yalign 0.25
    else:
        text "{font=amii.otf}熱の月 2日    昼{/font}":
            size 16
            xpos 0.04
            yalign 0.25

    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        if (day_my == False):
            textbutton _("{size=28}花壇{/size}"):
                hovered Show('place_my')
                unhovered Hide('place_my')
                action Hide('place_my'), Jump('day2_my')
        if (day_ar == False):
            textbutton _("{size=28}訓練場{/size}"):
                hovered Show('place_ar')
                unhovered Hide('place_ar')
                action Hide('place_ar'), Jump('day2_ar')
        if (day_hk == False):
            textbutton _("{size=28}作業場{/size}"):
                hovered Show('place_hk')
                unhovered Hide('place_hk')
                action Hide('place_hk'), Jump('day2_hk')
        if (day_rs == False):
            textbutton _("{size=28}図書館{/size}"):
                hovered Show('place_rs')
                unhovered Hide('place_rs')
                action Hide('place_rs'), Jump('day2_rs')
        if (day_gr == False):
            textbutton _("{size=28}医務室{/size}"):
                hovered Show('place_gr')
                unhovered Hide('place_gr')
                action Hide('place_gr'), Jump('day2_gr')


screen place_day3:
    add 'main_menu.png'

    if (day_time >= 2):
        text "{font=amii.otf}熱の月 3日    夕{/font}":
            size 16
            xpos 0.04
            yalign 0.25
    else:
        text "{font=amii.otf}熱の月 3日    昼{/font}":
            size 16
            xpos 0.04
            yalign 0.25


    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        if (day_my == False):
            textbutton _("{size=28}花壇{/size}"):
                hovered Show('place_my')
                unhovered Hide('place_my')
                action Hide('place_my'), Jump('day3_my')
        if (day_ar == False):
            if (meet_ar == True):
                textbutton _("{size=28}訓練場{/size}"):
                    hovered Show('place_ar')
                    unhovered Hide('place_ar')
                    action Hide('place_ar'), Jump('day3_ar')
        if (day_hk == False):
            textbutton _("{size=28}作業場{/size}"):
                hovered Show('place_hk')
                unhovered Hide('place_hk')
                action Hide('place_hk'), Jump('day3_hk')
        if (day_rs == False):
            if (meet_rs == True):
                textbutton _("{size=28}図書館{/size}"):
                    hovered Show('place_rs')
                    unhovered Hide('place_rs')
                    action Hide('place_rs'), Jump('day3_rs')
        if (day_gr == False):
            if (meet_gr == True):
                textbutton _("{size=28}医務室{/size}"):
                    hovered Show('place_gr')
                    unhovered Hide('place_gr')
                    action Hide('place_gr'), Jump('day3_gr')
        if (day_cr == False):
            textbutton _("{size=28}階段{/size}"):
                hovered Show('place_cr')
                unhovered Hide('place_cr')
                action Hide('place_cr'), Jump('day3_cr')

screen place_day4:
    add 'main_menu.png'

    if (day_time >= 2):
        text "{font=amii.otf}熱の月 4日    夕{/font}":
            size 16
            xpos 0.04
            yalign 0.25
    else:
        text "{font=amii.otf}熱の月 4日    昼{/font}":
            size 16
            xpos 0.04
            yalign 0.25


    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        if (day_my == False):
            textbutton _("{size=28}花壇{/size}"):
                hovered Show('place_my')
                unhovered Hide('place_my')
                action Hide('place_my'), Jump('day4_my')
        if (day_ar == False):
            if (meet_ar == True):
                textbutton _("{size=28}訓練場{/size}"):
                    hovered Show('place_ar')
                    unhovered Hide('place_ar')
                    action Hide('place_ar'), Jump('day4_ar')
        if (day_hk == False):
            if (meet_hk == True):
                textbutton _("{size=28}作業場{/size}"):
                    hovered Show('place_hk')
                    unhovered Hide('place_hk')
                    action Hide('place_hk'), Jump('day4_hk')
        if (day_rs == False):
            if (meet_rs == True):
                textbutton _("{size=28}図書館{/size}"):
                    hovered Show('place_rs')
                    unhovered Hide('place_rs')
                    action Hide('place_rs'), Jump('day4_rs')
        if (day_gr == False):
            if (meet_gr == True):
                textbutton _("{size=28}医務室{/size}"):
                    hovered Show('place_gr')
                    unhovered Hide('place_gr')
                    action Hide('place_gr'), Jump('day4_gr')
        if (day_cr == False):
            if (meet_crea == True):
                textbutton _("{size=28}階段{/size}"):
                    hovered Show('place_cr')
                    unhovered Hide('place_cr')
                    action Hide('place_cr'), Jump('day4_cr')
            else:
                textbutton _("{size=28}階段{/size}"):
                    hovered Show('place_cr')
                    unhovered Hide('place_cr')
                    action Hide('place_cr'), Jump('day_cr_FF')

screen place_day5:
    add 'main_menu.png'

    if (day_time >= 1):
        text "{font=amii.otf}熱の月 5日    夕{/font}":
            size 16
            xpos 0.04
            yalign 0.25
    else:
        text "{font=amii.otf}熱の月 5日    昼{/font}":
            size 16
            xpos 0.04
            yalign 0.25


    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        if (day_my == False):
            textbutton _("{size=28}花壇{/size}"):
                hovered Show('place_my')
                unhovered Hide('place_my')
                action Hide('place_my'), Jump('day5_my')
        if (day_ar == False):
            if (meet_ar == True):
                textbutton _("{size=28}訓練場{/size}"):
                    hovered Show('place_ar')
                    unhovered Hide('place_ar')
                    action Hide('place_ar'), Jump('day5_ar')
        if (day_hk == False):
            if (meet_hk == True):
                textbutton _("{size=28}作業場{/size}"):
                    hovered Show('place_hk')
                    unhovered Hide('place_hk')
                    action Hide('place_hk'), Jump('day5_hk')
        if (day_rs == False):
            if (meet_rs == True):
                textbutton _("{size=28}図書館{/size}"):
                    hovered Show('place_rs')
                    unhovered Hide('place_rs')
                    action Hide('place_rs'), Jump('day5_rs')
        if (day_gr == False):
            if (meet_gr == True):
                textbutton _("{size=28}医務室{/size}"):
                    hovered Show('place_gr')
                    unhovered Hide('place_gr')
                    action Hide('place_gr'), Jump('day5_gr')
        if (day_cr == False):
            if (meet_crea == 2):
                textbutton _("{size=28}階段{/size}"):
                    hovered Show('place_cr')
                    unhovered Hide('place_cr')
                    action Hide('place_cr'), Jump('day5_cr')
            else:
                textbutton _("{size=28}階段{/size}"):
                    hovered Show('place_cr')
                    unhovered Hide('place_cr')
                    action Hide('place_cr'), Jump('day_cr_FF')

screen place_day6:
    add 'main_menu.png'

    text "{font=amii.otf}熱の月 6日    昼{/font}":
        size 16
        xpos 0.04
        yalign 0.25


    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        if (day_my == False):
            if (love_ar == 3):
                add None
            elif (love_rs == 3):
                add None
            elif (love_hk == 3):
                add None
            elif (love_gr == 3):
                add None
            elif (love_cr == 3):
                add None
            else:
                textbutton _("{size=28}花壇{/size}"):
                    hovered Show('place_my')
                    unhovered Hide('place_my')
                    action Hide('place_my'), Jump('day6_my')
        if (day_ar == False):
            if (love_ar == 3):
                textbutton _("{size=28}訓練場{/size}"):
                    hovered Show('place_ar')
                    unhovered Hide('place_ar')
                    action Hide('place_ar'), Jump('day6_ar')
        if (day_hk == False):
            if (love_hk == 3):
                textbutton _("{size=28}作業場{/size}"):
                    hovered Show('place_hk')
                    unhovered Hide('place_hk')
                    action Hide('place_hk'), Jump('day6_hk')
        if (day_rs == False):
            if (love_rs == 3):
                textbutton _("{size=28}図書館{/size}"):
                    hovered Show('place_rs')
                    unhovered Hide('place_rs')
                    action Hide('place_rs'), Jump('day6_rs')
        if (day_gr == False):
            if (love_gr == 3):
                textbutton _("{size=28}医務室{/size}"):
                    hovered Show('place_gr')
                    unhovered Hide('place_gr')
                    action Hide('place_gr'), Jump('day6_gr')
        if (day_cr == False):
            if (love_cr == 3):
                textbutton _("{size=28}階段{/size}"):
                    hovered Show('place_cr')
                    unhovered Hide('place_cr')
                    action Hide('place_cr'), Jump('day6_cr')

screen place_day8:
    add 'main_menu.png'

    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    if (day_time >= 4):
        text "{font=amii.otf}熱の月 8日    夕{/font}":
            size 16
            xpos 0.04
            yalign 0.25
    else:
        text "{font=amii.otf}熱の月 8日    昼{/font}":
            size 16
            xpos 0.04
            yalign 0.25

    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        if (day_my == False):
            textbutton _("{size=28}花壇{/size}"):
                hovered Show('place_my')
                unhovered Hide('place_my')
                action Hide('place_my'), Jump('day8_my')
        if (day_ar == False):
            textbutton _("{size=28}訓練場{/size}"):
                hovered Show('place_ar')
                unhovered Hide('place_ar')
                action Hide('place_ar'), Jump('day8_ar')

screen place_day6_rkn:
    add 'main_menu.png'

    text "{font=amii.otf}熱の月 6日    昼{/font}":
        size 16
        xpos 0.04
        yalign 0.25


    text "どこに向かう？":
        size 28
        xpos 0.04
        yalign 0.35

    vbox:
        style_prefix "place"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing

        if (day_my == False):
            if (love_ar == 3):
                add None
            elif (love_rs == 3):
                add None
            elif (love_hk == 3):
                add None
            elif (love_gr == 3):
                add None
            elif (love_cr == 3):
                add None
            else:
                textbutton _("{size=28}花壇{/size}"):
                    hovered Show('place_my')
                    unhovered Hide('place_my')
                    action Hide('place_my'), Jump('day6_my_rkn')
        if (day_ar == False):
            if (love_ar == 3):
                textbutton _("{size=28}訓練場{/size}"):
                    hovered Show('place_ar')
                    unhovered Hide('place_ar')
                    action Hide('place_ar'), Jump('day6_ar')
        if (day_hk == False):
            if (love_hk == 3):
                textbutton _("{size=28}作業場{/size}"):
                    hovered Show('place_hk')
                    unhovered Hide('place_hk')
                    action Hide('place_hk'), Jump('day6_hk')
        if (day_rs == False):
            if (love_rs == 3):
                textbutton _("{size=28}図書館{/size}"):
                    hovered Show('place_rs')
                    unhovered Hide('place_rs')
                    action Hide('place_rs'), Jump('day6_rs')
        if (day_gr == False):
            if (love_gr == 3):
                textbutton _("{size=28}医務室{/size}"):
                    hovered Show('place_gr')
                    unhovered Hide('place_gr')
                    action Hide('place_gr'), Jump('day6_gr')
        if (day_cr == False):
            if (love_cr == 3):
                textbutton _("{size=28}階段{/size}"):
                    hovered Show('place_cr')
                    unhovered Hide('place_cr')
                    action Hide('place_cr'), Jump('day6_cr')

screen place:
    add 'main_menu.png'

    text "どこに向かう？":
        size 20
        xpos 0.04
        yalign 0.35

    vbox:
        style_prefix "place"

        xpos 0.2
        yalign 0.5
        spacing gui.navigation_spacing
        textbutton _("花壇"):
            hovered Show('place_my')
            unhovered Hide('place_my')
            if (day == 1):
                action Jump('day1_my')
            if (day == 2):
                action Jump('day2_my')

        textbutton _("訓練場") action Jump("on_punch_1")
        textbutton _("作業場") action Jump("on_punch_1")
        textbutton _("医務室") action Jump("on_punch_1")
        textbutton _("図書館") action Jump("on_punch_1")
        textbutton _("階段") action Jump("on_punch_1")
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
