

layeredimage SCG_01 :
    yalign 0.1
    group outfit:
        attribute always default:
            'char/ch_01_pl/0default.png'

    group express:
        attribute 0:
            "none.png"
        attribute idle:
            "none.png"

        attribute 1:
            'char/ch_01_pl/1smile.png'

        attribute 2:
            'char/ch_01_pl/2anger.png'

        attribute 3:
            'char/ch_01_pl/3sad.png'

        attribute 4:
            'char/ch_01_pl/4.png'


layeredimage SCG_02 :
    yalign 0.2
    group outfit:
        attribute always default:
            'char/ch_02_my/0default.png'
        attribute A:
            'char/ch_02_my/1default.png'
        attribute B:
            ConditionSwitch(
            
                "persistent.call_CG", ConditionSwitch (
                    "persistent.update",'char/ch_02_my/2default.png',
                    "True", 'char/ch_02_my/2defaultR.png'
                ),
        
        
                "True", 'char/ch_02_my/2defaultR.png'
            )

    group express:
        attribute 0:
            "none.png"
        attribute idle:
            "none.png"

        attribute 1:
            'char/ch_02_my/1smile.png'

        attribute 2:
            'char/ch_02_my/2anger.png'

        attribute 3:
            'char/ch_02_my/3sad.png'

        attribute 4:
            'char/ch_02_my/4joy.png'

        attribute 5:
            'char/ch_02_my/5alarmed.png'

        attribute 6:
            'char/ch_02_my/6shy.png'

        attribute 7:
            'char/ch_02_my/7panic.png'

        attribute 8:
            'char/ch_02_my/8chilly.png'

        attribute 00:
            'char/ch_02_my/9chilly.png'

        attribute 10:
            'char/ch_02_my/10.png'

    group dm:
        attribute always default:
            "none.png"
        attribute 100:
            'char/ch_02_my/0_dm.png'



layeredimage SCG_03 :
    yalign 0.1
    always:
        'char/ch_03_sc/0default.png'

    group express:
        attribute 0:
            "none.png"
        attribute idle:
            "none.png"

        attribute 1:
            'char/ch_03_sc/1smile.png'

        attribute 2:
            'char/ch_03_sc/2angry.png'

        attribute 3:
            'char/ch_03_sc/3sad.png'

        attribute 4:
            'char/ch_03_sc/4joy.png'

        attribute 5:
            'char/ch_03_sc/5surprisal.png'

        attribute 6:
            'char/ch_03_sc/6shy.png'

        attribute 7:
            'char/ch_03_sc/7.png'

        attribute 72:
            'char/ch_03_sc/72.png'

        attribute 8:
            'char/ch_03_sc/8.png'

        attribute 9:
            'char/ch_03_sc/9.png'


        attribute 100:
            'char/ch_03_sc/100.png'



layeredimage SCG_04 :
    yalign -0.2
    group outfit:
        attribute always default:
            'char/ch_04_cr/0default.png'
        attribute W:
            'char/ch_04_cr/1default.png'
        attribute A:
            'char/ch_04_cr/A.png'

    group express:
        attribute idle:
            "none.png"

        attribute 0:
            "none.png"

        attribute 1:
            'char/ch_04_cr/1smile.png'

        attribute 2:
            'char/ch_04_cr/2anger.png'

        attribute 3:
            'char/ch_04_cr/3sad.png'

        attribute 4:
            'char/ch_04_cr/4joy.png'

        attribute 5:
            'char/ch_04_cr/5alarmed.png'

        attribute 6:
            'char/ch_04_cr/6shy.png'

        attribute 7:
            'char/ch_04_cr/7.png'

        attribute 8:
            'char/ch_04_cr/8.png'

        attribute 9:
            'char/ch_04_cr/9.png'

        attribute 10:
            'char/ch_04_cr/10.png'

        attribute 100:
            'char/ch_04_cr/100.png'
    group me:
        attribute always default:
            "none.png"
        attribute B:
            'char/ch_04_cr/B.png'

layeredimage SCG_05 :
    yalign 0.1
    group outfit:
        attribute always default:
            'char/ch_05_hk/0default.png'
        attribute B:
            'char/ch_05_hk/hkB.png'

        attribute A:
            'char/ch_05_hk/hkA.png'

    group express:
        attribute 0:
            "none.png"
        attribute idle:
            "none.png"

        attribute 00:
            'char/ch_05_hk/hkB_0.png'

        attribute 000:
            'char/ch_05_hk/hkB_0_.png'

        attribute 1:
            'char/ch_05_hk/1smile.png'

        attribute 2:
            'char/ch_05_hk/2anger.png'

        attribute 3:
            'char/ch_05_hk/3sad.png'

        attribute 4:
            'char/ch_05_hk/4joy.png'

        attribute 5:
            'char/ch_05_hk/5surprisal.png'

        attribute 6:
            'char/ch_05_hk/6shy.png'

        attribute 7:
            'char/ch_05_hk/7panic.png'

        attribute 8:
            'char/ch_05_hk/8chilly.png'

        attribute 9:
            'char/ch_05_hk/9chilly2.png'

        attribute 10:
            'char/ch_05_hk/10.png'

        attribute 11:
            'char/ch_05_hk/11.png'

        attribute 90:
            'char/ch_05_hk/9chilly2_B.png'

        attribute 100:
            'char/ch_05_hk/hkA_0.png'

        attribute 101:
            'char/ch_05_hk/100.png'




layeredimage SCG_06 :
    yalign 0.1
    zoom 0.95
    group outfit:
        attribute always default:
            'char/ch_06_hk/0default.png'

    group express:
        attribute 0:
            "none.png"
        attribute idle:
            "none.png"

        attribute 00:
            'char/ch_06_hk/hkB_0.png'

        attribute 000:
            'char/ch_06_hk/hkB_0_.png'

        attribute 1:
            'char/ch_06_hk/1smile.png'

        attribute 2:
            'char/ch_06_hk/2anger.png'

        attribute 3:
            'char/ch_06_hk/3sad.png'

        attribute 4:
            'char/ch_06_hk/4joy.png'

        attribute 5:
            'char/ch_06_hk/5surprisal.png'

        attribute 6:
            'char/ch_06_hk/6shy.png'

        attribute 7:
            'char/ch_06_hk/7panic.png'

        attribute 8:
            'char/ch_06_hk/8chilly.png'

        attribute 9:
            'char/ch_06_hk/9chilly2.png'

        attribute 10:
            'char/ch_06_hk/10.png'

        attribute 11:
            'char/ch_06_hk/11.png'

        attribute 12:
            'char/ch_06_hk/12.png'
        attribute 13:
            'char/ch_06_hk/13.png'


layeredimage SCG_07 :
    yalign -0.05
    always:
        'char/ch_07_ar/0default.png'

    group express:
        attribute 0:
            "none.png"
        attribute idle:
            "none.png"

        attribute 1:
            'char/ch_07_ar/1smile.png'

        attribute 2:
            'char/ch_07_ar/2angry.png'

        attribute 4:
            'char/ch_07_ar/4joy.png'

        attribute 5:    
            'char/ch_07_ar/5surprisal.png'

        attribute 7:    
            'char/ch_07_ar/7.png'

        attribute 9:
            'char/ch_07_ar/9.png'

        attribute 10:    
            'char/ch_07_ar/10.png'

        attribute 11:    
            'char/ch_07_ar/11.png'

        attribute 100:    
            'char/ch_07_ar/100.png'


layeredimage SCG_08 :
    yalign 0.05
    always:
        'char/ch_08_en/0default.png'

    group express:
        attribute 0:
            "none.png"
        attribute idle:
            "none.png"
        attribute 1:
            'char/ch_08_en/1smile.png'
        attribute 2:
            'char/ch_08_en/2.png'
        attribute 3:
            'char/ch_08_en/3.png'
        attribute 4:
            'char/ch_08_en/4.png'
        attribute 5:
            'char/ch_08_en/5.png'
        attribute 6:
            'char/ch_08_en/6.png'
        attribute 7:
            'char/ch_08_en/7.png'
        attribute 8:
            'char/ch_08_en/8.png'
        attribute 9:
            'char/ch_08_en/9.png'
        attribute 10:
            'char/ch_08_en/10.png'
        attribute 11:
            'char/ch_08_en/11.png'
        attribute 12:
            'char/ch_08_en/12.png'
        attribute 13:
            'char/ch_08_en/13.png'
        attribute 14:
            'char/ch_08_en/14.png'
    group shy:
        attribute always default:
            "none.png"
        attribute S:
            'char/ch_08_en/s.png'



layeredimage SCG_09 :
    yalign -0.4
    xoffset 80
    always:
        'char/ch_09_er/0default.png'

    group express:
        attribute idle:
            "none.png"

        attribute 0:
            "none.png"
        attribute 2:
            'char/ch_09_er/2.png'
        attribute 4:
            'char/ch_09_er/4joy.png'

        attribute 7:
            'char/ch_09_er/7.png'

        attribute 8:
            'char/ch_09_er/8.png'

        attribute 9:
            'char/ch_09_er/9.png'

        attribute 10:
            'char/ch_09_er/10.png'

        attribute 11:
            'char/ch_09_er/11.png'


layeredimage SCG_10 :
    yalign 0.16
    always:
        'char/ch_10_ev/0default.png'

    group outfit:
        attribute test:
            'char/ch_10_ev/0default.png'

    group express:
        attribute idle:
            "none.png"
        attribute 0:
            "none.png"
        attribute 1:
            'char/ch_10_ev/1.png'

        attribute 2:
            'char/ch_10_ev/2.png'

        attribute 3:
            'char/ch_10_ev/3.png'

        attribute 4:
            'char/ch_10_ev/4.png'

        attribute 5:
            'char/ch_10_ev/5alarmed.png'

        attribute 6:
            'char/ch_10_ev/6shy.png'

        attribute 7:
            'char/ch_10_ev/7panic.png'

        attribute 8:
            'char/ch_10_ev/8chilly.png'


layeredimage SCG_11 :
    yalign 0.07

    group outfit:
        attribute always default:
            'char/ch_11_rv/0default.png'
        attribute ns:
            'char/ch_11_rv/outfit.png'

    group express:
        attribute idle:
            "none.png"

        attribute 0:
            "none.png"

        attribute 1:
            'char/ch_11_rv/1.png'

        attribute 2:
            'char/ch_11_rv/2.png'

        attribute 3:
            'char/ch_11_rv/3.png'

        attribute 4:
            'char/ch_11_rv/4.png'

        attribute 5:
            'char/ch_11_rv/5.png'

        attribute 6:
            'char/ch_11_rv/6.png'

        attribute 7:
            'char/ch_11_rv/7.png'

        attribute 8:
            'char/ch_11_rv/8.png'

        attribute 9:
            'char/ch_11_rv/9.png'


layeredimage SCG_12 :
    yalign 0.07
    always:
        'char/ch_12_rs/0default.png'

    group outfit:
        attribute always default:
            'char/ch_12_rs/0default.png'
        attribute A:
            'char/ch_12_rs/A.png'

    group express:
        attribute idle:
            "none.png"

        attribute 0:
            "none.png"

        attribute 1:
            'char/ch_12_rs/1.png'

        attribute 2:
            'char/ch_12_rs/2.png'

        attribute 3:
            'char/ch_12_rs/3.png'

        attribute 4:
            'char/ch_12_rs/4.png'

        attribute 5:
            'char/ch_12_rs/5.png'

        attribute 6:
            'char/ch_12_rs/6.png'

        attribute 7:
            'char/ch_12_rs/7.png'

        attribute 8:
            'char/ch_12_rs/8.png'

        attribute 9:
            'char/ch_12_rs/9.png'

        attribute 10:
            'char/ch_12_rs/10.png'
        attribute 11:
            'char/ch_12_rs/11.png'
    group pin:
        attribute always default:
            "none.png"
        attribute B:
            'char/ch_12_rs/B.png'


layeredimage SCG_13 :
    yalign 0.08
    always:
        'char/ch_13_gg/0default.png'

    group express:
        attribute 0:
            "none.png"
        attribute idle:
            "none.png"
        attribute 1:
            'char/ch_13_gg/1.png'
        attribute 2:
            'char/ch_13_gg/2.png'
        attribute 3:
            'char/ch_13_gg/3.png'
        attribute 4:
            'char/ch_13_gg/4.png'
        attribute 5:
            'char/ch_13_gg/5.png'
        attribute 6:
            'char/ch_13_gg/6.png'
        attribute 7:
            'char/ch_13_gg/7.png'
        attribute 8:
            'char/ch_13_gg/8.png'
        attribute 9:
            'char/ch_13_gg/9.png'
        attribute 10:
            'char/ch_13_gg/10.png'
        attribute 11:
            'char/ch_13_gg/11.png'
        attribute 12:
            'char/ch_13_gg/12.png'



layeredimage SCG_14 :
    yalign 0.2
    always:
        'char/ch_14_gr/0default.png'

    group express:
        attribute 0:
            "none.png"
        attribute idle:
            "none.png"

        attribute 1:
            'char/ch_14_gr/1smile.png'

        attribute 2:
            'char/ch_14_gr/2angry.png'

        attribute 3:
            'char/ch_14_gr/3sad.png'

        attribute 4:
            'char/ch_14_gr/4joy.png'

        attribute 5:
            'char/ch_14_gr/5surprisal.png'

        attribute 6:
            'char/ch_14_gr/6shy.png'

        attribute 7:
            'char/ch_14_gr/7alarmed.png'

        attribute 8:
            'char/ch_14_gr/8smile.png'

        attribute 9:
            'char/ch_14_gr/9.png'

        attribute 10:
            'char/ch_14_gr/10.png'

        attribute 11:
            'char/ch_14_gr/11.png'

        attribute 12:
            'char/ch_14_gr/12.png'





layeredimage SCG_101 :
    yalign 0.2
    always:
        'char/ch_101_lz/0default.png'

    group express:
        attribute 0:
            'char/ch_101_lz/0default.png'
        attribute 1:
            'char/ch_101_lz/1.png'

        attribute 2:
            'char/ch_101_lz/2panic.png'

        attribute 3:
            'char/ch_101_lz/3smile.png'

        attribute 4:
            'char/ch_101_lz/4angry.png'



layeredimage SCG_102 :
    yalign 0.1
    group outfit:
        attribute always default:
            'char/ch_102_lz/0default.png'
        attribute outfit:
            'char/ch_102_lz/outfit1.png'

    group express:
        attribute 0:
            "none.png"

        attribute 1:
            'char/ch_102_lz/1smile.png'

        attribute 2:
            'char/ch_102_lz/2pero.png'

        attribute 3:
            'char/ch_102_lz/3.png'

        attribute 4:
            'char/ch_102_lz/4chilly.png'

        attribute 5:
            'char/ch_102_lz/5chilly.png'


image bg_06_rkn:
    "bg06"
    function WaveShader(period=5, amp=2.0, speed=0.05, direction='x', double="x")

image bg107_rkn:
    "bg107"
    function WaveShader(period=5, amp=2.0, speed=0.05, direction='x', double="x")


image cggr3_rkn:
    "cggr3"
    function WaveShader(period=10, amp=0.4, speed=0.1, direction='x', double="x")



image story01 = 'cg_01.png'
image story02 = 'cg02.png'
image story03 = 'cg03.png'
image story04 = 'cg04.png'
image story05 = 'cg05.png'
image story06 = 'cg06.png'
image story06R = 'cg06_1.png'
image story07 = 'cg07.png'
image story08 = 'cg08.png'
image story08R = 'cg08_1.png'
image story09 = 'cg09.png'
image story10 = 'cg10.png'
image story11 = 'cg11.png'
image story12 = 'cg12.png'
image story13 = 'cg13.png'
image story14 = 'cg14.png'
image story15 = 'cg15.png'
image story16 = 'cg16.png'
image story17 = 'cg17.png'
image story19 = 'cg19.png'
image story20 = 'cg20.png'
image story21 = 'cg21.png'
image story21R = 'cg21_1.png'
image story22 = 'cg22.png'
image dmy1 = 'dmy1.png'
image dmy2 = 'dmy2.png'
image dmy3 = 'dmy3.png'
image dmy4 = 'dmy4.png'
image dmy5 = 'dmy5.png'
image cgmy01 = 'cgmy1.png'
image cgmy03 = 'cgmy3.png'
image cgmy03_1 = 'cgmy3_1.png'
image cgmy03_2 = 'cgmy3_2.png'

image cgsc01 = 'cgsc1.png'
image cgsc02 = 'cgsc2.png'
image cgsc03 = 'cgsc3.png'
image cgsc04 = 'cgsc4.png'
image cgsc05 = 'cgsc5.png'

image cgar01 = 'cgar1.png'
image cgar02 = 'cgar2.png'
image cgar03 = 'cgar3.png'
image cgar03R = 'cgar3R.png'
image cgar04 = 'cgar4.png'
image cgar05 = 'cgar5.png'
image cgar06 = 'cgar6.png'

image cgrs01 = 'cgrs1.png'
image cgrs02 = 'cgrs2.png'
image cgrs03 = 'cgrs3.png'
image cgrs03R = 'cgrs3R.png'
image cgrs04 = 'cgrs4.png'
image cgrs05 = 'cgrs5.png'
image cgrs06 = 'cgrs6.png'

image cghk01 = 'cghk1.png'
image cghk01R = 'cghk1R.png'
image cghk02 = 'cghk2.png'
image cghk03 = 'cghk3.png'
image cghk04 = 'cghk4.png'
image cghk05 = 'cghk5.png'
image cghk06 = 'cghk6.png'

image cggr01 = 'cggr1.png'
image cggr02 = 'cggr2.png'
image cggr02R = 'cggr2R.png'
image cggr03 = 'cggr3.png'
image cggr04 = 'cggr4.png'
image cggr05 = 'cggr5.png'
image cggr06 = 'cggr6.png'

image cgcr01 = 'cgcr1.png'
image cgcr02 = 'cgcr2.png'
image cgcr03 = 'cgcr3.png'
image cgcr04 = 'cgcr4.png'
image cgcr05 = 'cgcr5.png'
image cgcr05R = 'cgcr5R.png'
image cgcr06 = 'cgcr6.png'
image cgcr07 = 'cgcr7.png'


image titledef = 'title1.png'
image title_my = 'title2.png'
image title_sc = 'title3.png'
image title_ar = 'title4.png'
image title_rs = 'title5.png'
image title_gr = 'title6.png'
image title_cr = 'title7.png'
image title_hk = 'title8.png'



init -999 python:
    def unlock_all_gallery():
        images = [
        "story01","story02","story03","story04","story05","story06","story06R",
        "story07","story08","story08R", "story09","story10","story11","story12","story13",
        "story14","story15","story16","story17","story19","story20","story21",
        "story21R","story22",
        "dmy1","dmy2","dmy3","dmy4","dmy5",
        "cgmy01","cgmy03","cgmy03_1","cgmy03_2",
        "cgsc01","cgsc02","cgsc03","cgsc04","cgsc05",
        "cgar01","cgar02","cgar03","cgar03R","cgar04","cgar05","cgar06",
        "cgrs01","cgrs02","cgrs03","cgrs03R","cgrs04","cgrs05","cgrs06",
        "cghk01","cghk01R","cghk02","cghk03","cghk04","cghk05","cghk06",
        "cggr01","cggr02","cggr02R","cggr03","cggr04","cggr05","cggr06",
        "cgcr01","cgcr02","cgcr03","cgcr04","cgcr05","cgcr05R","cgcr06","cgcr07",
        "titledef","title_my","title_sc","title_ar","title_rs","title_gr","title_cr","title_hk"
    ]
        
        renpy.notify("コレクション解放を開始します… 少々お待ちください。")
        
        for img in images:
            try:
                renpy.show(img)
                renpy.pause(0.1, hard=True)
                renpy.hide(img)
            except Exception as e:
                renpy.log("skip %s: %s" % (img, e))
        
        
        if persistent.titlename == "def" or persistent.titlename == "def2":
            persistent.titlename = "my"
        
        persistent.cheat_title = True
        persistent.cheat_rosary = True
        persistent.cheat_gal = True
        
        renpy.save_persistent()
        renpy.notify("全てのコレクションがアンロックされました！")
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
