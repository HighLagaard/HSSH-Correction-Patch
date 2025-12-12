define credit = "nomal"

label creditscreen:
    pause 1 
    show end with dissolve:
        yalign 0.0
    pause 2
    show end:
        yalign 0.0
        linear 70 yalign 1.0
    pause 77
    stop music fadeout 2
    scene black with dissolve
    return

label end:
    $ credit = "nomal"
    if persistent.hssh_end == True:
        pause 1 
        show end with dissolve:
            yalign 0.0
        show screen creditskip
        call creditscreen
        jump end222
    elif persistent.mylove_end == True:
        pause 1 
        show end with dissolve:
            yalign 0.0
        show screen creditskip
        call creditscreen
        jump end222
    else:
        if preferences.skip_unseen == True:
            pause 1 
            show end with dissolve:
                yalign 0.0
            show screen creditskip
            call creditscreen
            jump end222
        else:
            jump end222

label end222:
    if persistent.hssh12end or persistent.mylove_end == False:
        jump end12
    else:
        $ MainMenu(confirm=False)()

label end_sc:
    $ credit = "sc"
    pause 1 
    show end with dissolve:
        yalign 0.0
    show screen creditskip
    call creditscreen
    jump end_sc2

label end_sc2:
    if persistent.sc_end == False:
        $ persistent.sc_end = True
        "\n クリア報償として浄化部のロザリオがアンロックされました。"
        if not achievement.has("sc_end"):
            $ achievement.grant("sc_end")
            $ achievement.sync()


    if all([persistent.cr_end, persistent.ar_end, persistent.rs_end, persistent.gr_end, persistent.sc_end, persistent.hk_end]):
        if not achievement.has("all_end"):
            $ achievement.grant("all_end")
            $ achievement.sync()

        $ renpy.reload_script
    elif sc_happy == True:
        $ persistent.titlename = "sc"
        $ persistent.title_sc = True
        $ persistent.title_my = True
        $ renpy.reload_script
    else:
        $ renpy.reload_script
    $ MainMenu(confirm=False)()
    return

label end_ar:
    $ credit = "ar"
    pause 1 
    show end with dissolve:
        yalign 0.0
    show screen creditskip
    call creditscreen
    jump end_ar2

label end_ar2:
    hide screen creditskip
    $ _skipping = False
    if persistent.ar_end == False:
        $ persistent.ar_end = True
        $ persistent.titlename = "ar"
        $ persistent.title_ar = True
        "\n クリア報償として魔導部のロザリオがアンロックされました。"

        if not achievement.has("ar_end"):
            $ achievement.grant("ar_end")
            $ achievement.sync()


    if all([persistent.cr_end, persistent.ar_end, persistent.rs_end, persistent.gr_end, persistent.sc_end, persistent.hk_end]):
        if not achievement.has("all_end"):
            $ achievement.grant("all_end")
            $ achievement.sync()

        $ renpy.reload_script
    else:
        $ renpy.reload_script
    $ MainMenu(confirm=False)()
    return

label end_rs:
    $ credit = "rs"
    pause 1 
    show end with dissolve:
        yalign 0.0
    show screen creditskip
    call creditscreen
    jump end_rs2

label end_rs2:
    hide screen creditskip
    if persistent.rs_end == False:
        $ persistent.rs_end = True
        $ persistent.titlename = "rs"
        $ persistent.title_rs = True
        "\n クリア報償として学術部のロザリオがアンロックされました。"

        if not achievement.has("rs_end"):
            $ achievement.grant("rs_end")
            $ achievement.sync()


    if all([persistent.cr_end, persistent.ar_end, persistent.rs_end, persistent.gr_end, persistent.sc_end, persistent.hk_end]):
        if not achievement.has("all_end"):
            $ achievement.grant("all_end")
            $ achievement.sync()

        $ renpy.reload_script
    else:
        $ renpy.reload_script
    $ MainMenu(confirm=False)()
    return

label end_gr:
    $ credit = "gr"
    pause 1 
    show end with dissolve:
        yalign 0.0
    show screen creditskip
    call creditscreen
    jump end_gr2

label end_gr2:
    hide screen creditskip
    if persistent.gr_end == False:
        $ persistent.gr_end = True
        $ persistent.titlename = "gr"
        $ persistent.title_gr = True
        "\n クリア報償として保健部のロザリオがアンロックされました。"

        if not achievement.has("gr_end"):
            $ achievement.grant("gr_end")
            $ achievement.sync()


    if all([persistent.cr_end, persistent.ar_end, persistent.rs_end, persistent.gr_end, persistent.sc_end, persistent.hk_end]):
        if not achievement.has("all_end"):
            $ achievement.grant("all_end")
            $ achievement.sync()

        $ renpy.reload_script
    else:
        $ renpy.reload_script
    $ MainMenu(confirm=False)()
    return

label end_cr:
    $ credit = "cr"
    pause 1 
    show end with dissolve:
        yalign 0.0
    show screen creditskip
    call creditscreen
    jump end_cr2

label end_cr2:
    hide screen creditskip
    if persistent.cr_end == False:
        $ persistent.cr_end = True
        $ persistent.titlename = "cr"
        $ persistent.title_cr = True
        "\n クリア報償としてクリオネのプロフィールがアンロックされました。"

        if not achievement.has("cr_end"):
            $ achievement.grant("cr_end")
            $ achievement.sync()


    if all([persistent.cr_end, persistent.ar_end, persistent.rs_end, persistent.gr_end, persistent.sc_end, persistent.hk_end]):
        if not achievement.has("all_end"):
            $ achievement.grant("all_end")
            $ achievement.sync()

        $ renpy.reload_script
    else:
        $ renpy.reload_script
    $ MainMenu(confirm=False)()
    return

label end_hk2:
    $ credit = "nomal"
    pause 1 
    show end with dissolve:
        yalign 0.0
    show screen creditskip
    call creditscreen
    $ MainMenu(confirm=False)()
    return

label end_hk:
    $ credit = "hk"
    pause 1 
    show end with dissolve:
        yalign 0.0
    show screen creditskip
    call creditscreen
    jump end_hk22

label end_hk22:
    hide screen creditskip
    if persistent.hk_end == False:
        $ persistent.hk_end = True
        $ persistent.titlename = "hk"
        $ persistent.title_hk = True
        "\n クリア報償としてハクのロザリオがアンロックされました。"

        if not achievement.has("hk_end"):
            $ achievement.grant("hk_end")
            $ achievement.sync()


    if all([persistent.cr_end, persistent.ar_end, persistent.rs_end, persistent.gr_end, persistent.sc_end, persistent.hk_end]):
        if not achievement.has("all_end"):
            $ achievement.grant("all_end")
            $ achievement.sync()

    jump day12_hk_end2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
