default called_from_menu = False

label splashscreen:
    if persistent.first_start == True:
        pause 0.1
    else:
        $ renpy.set_physical_size((640, 480))
        $ persistent.first_start = True
        $ persistent.tut = True
        call tut
        $ renpy.restart_interaction()
    $ _dismiss_pause = False
    if persistent.dead_maya == True:
        $ na = persistent.na
        $ na2 = persistent.na2
        jump day11_my
        return
    if persistent.dmy >= 2:
        $ na = persistent.na
        $ na2 = persistent.na2
        jump dmy_end
        return
    pause 1


    if (persistent.hssh_end and persistent.hssh12end):
        if not achievement.has("hss_ending"):
            $ achievement.grant("hss_ending")
            $ achievement.sync()
    if persistent.cr_end:
        if not achievement.has("cr_end"):
            $ achievement.grant("cr_end")
            $ achievement.sync()
    if persistent.ar_end:
        if not achievement.has("ar_end"):
            $ achievement.grant("ar_end")
            $ achievement.sync()
    if persistent.rs_end:
        if not achievement.has("rs_end"):
            $ achievement.grant("rs_end")
            $ achievement.sync()
    if persistent.gr_end:
        if not achievement.has("gr_end"):
            $ achievement.grant("gr_end")
            $ achievement.sync()
    if persistent.sc_end:
        if not achievement.has("sc_end"):
            $ achievement.grant("sc_end")
            $ achievement.sync()
    if persistent.hk_end:
        if not achievement.has("hk_end"):
            $ achievement.grant("hk_end")
            $ achievement.sync()


    if persistent.mylove_end:
        if not achievement.has("maya_love"):
            $ achievement.grant("maya_love")
            $ achievement.sync()
    if persistent.no_girls:
        if not achievement.has("outsider"):
            $ achievement.grant("outsider")
            $ achievement.sync()


    if all([persistent.cr_end, persistent.ar_end, persistent.rs_end, persistent.gr_end, persistent.sc_end, persistent.hk_end]):
        if not achievement.has("all_end"):
            $ achievement.grant("all_end")
            $ achievement.sync()

    scene black
    $ skipping = True
    show splash with dissolve
    pause(3)
    hide splash with dissolve
    show notice_Title at notice_T
    show notice at notice
    with dissolve
    pause(7)    
    hide notice_Title
    hide notice
    with dissolve
    return

label tut_menu:
    $ called_from_menu = True
    call tut
    $ called_from_menu = False
    $ renpy.call_screen("preferences")

label tut:
    play sound "audio/se/tut.ogg"

    show screen tut_key with dissolve
    $ _dismiss_pause = True
    $ renpy.pause()
    $ _dismiss_pause = False
    $ preferences.transitions = 2
    hide screen tut_key with dissolve
    show screen tut_key2 with dissolve
    $ _dismiss_pause = True
    $ renpy.pause()
    $ _dismiss_pause = False
    $ preferences.transitions = 2
    hide screen tut_key2 with dissolve
    show screen tut_key3 with dissolve
    $ renpy.pause(3.0)
    hide screen tut_key3 with dissolve

    $ persistent.tut = False

    if called_from_menu:
        return
    else:
        return


label start:

    $ persistent.dmy = 0;
    if persistent.hssh_end == True:
        jump start_rkn
    elif persistent.cheat_hssh_end == True:
        jump start_rkn
    else:
        jump prr_name
label prr_name:
    define init_name = "ベリアル"
    define init_name2 = "ベル"
    if config.language == "Korean":
        $ init_name = "벨리알"
    elif config.language == "English":
        $ init_name = "Belial"
    elif config.language == "SimplifiedChinese":
        $ init_name = "彼列"
    else:
        $ init_name = "ベリアル"
    window hide
    $ _dismiss_pause = False
    stop music fadeout 1
    $ day = 0
    $ _game_menu_screen = None
    $ show_quick_menu = False
    $ _history = False
    scene black with dissolve
    scene bgw with dissolve
    $ name = renpy.call_screen("set_name",title=" {font=KH-Dot-Dougenzaka-16.ttf}俺の名前は...{/font} ",init_name=init_name)
    $ na = (name)
    $ persistent.na = (name)
    $ na = na.strip()
    if not na:
        if config.language == "Korean":
            $ na = "벨리알"
        elif config.language == "English":
            $ na = "Belial"
        elif config.language == "SimplifiedChinese":
            $ na = "彼列"
        else:
            $ na = "ベリアル"
    if (na == 'アミー・エカルラン'):
        show screen nvlbox with dissolve
        am "\n※貴方の行う選択にはそれ相応の責任と云う物が付く事になるでしょう。{w}\n貴方に、その煩悩と艱苦を耐え抜く覚悟はありますか?"
        "{size=0} {/size}{nw}"
        "{size=0} {/size}{nw}"
        menu(nvl=True):
            "{font=KH-Dot-Dougenzaka-16.ttf}はい{/font}":
                show nvlb
                nvl clear
                $ hardmode = True
                hide screen nvlbox
                jump day_0
            "{font=KH-Dot-Dougenzaka-16.ttf}いいえ{/font}":
                nvl clear
                hide screen nvlbox with dissolve
                jump name
    else:
        show screen nvlbox with dissolve
        et "\n※[na]で宜しいですか?"
    "{size=0} {/size}{nw}"
    "{size=0} {/size}{nw}"
    menu(nvl=True):
        "{font=KH-Dot-Dougenzaka-16.ttf}はい{/font}":
            show nvlb
            nvl clear
            hide screen nvlbox
            jump day_0
        "{font=KH-Dot-Dougenzaka-16.ttf}いいえ{/font}":
            nvl clear
            hide screen nvlbox with dissolve
            jump name
            label name:

                $ name = renpy.call_screen("set_name",title=" {font=KH-Dot-Dougenzaka-16.ttf}俺の名前は...{/font} ",init_name="")
                $ na = (name)
                $ persistent.na = (name)
                $ na = na.strip()
                if not na:
                    if config.language == "Korean":
                        $ na = "벨리알"
                    if config.language == "English":
                        $ na = "Belial"
                    if config.language == "SimplifiedChinese":
                        $ na = "彼列"
                    else:
                        $ na = "ベリアル"
                if (na == 'アミー・エカルラン'):
                    show screen nvlbox with dissolve
                    am "\n※貴方の行う選択にはそれ相応の責任と云う物が付く事になるでしょう。{w}\n貴方に、その煩悩と艱苦を耐え抜く覚悟はありますか？"
                    "{size=0} {/size}{nw}"
                    "{size=0} {/size}{nw}"
                    menu(nvl=True):
                        "{font=KH-Dot-Dougenzaka-16.ttf}はい{/font}":
                            show nvlb
                            nvl clear
                            hide screen nvlbox
                            $ hardmode = True
                            jump day_0
                        "{font=KH-Dot-Dougenzaka-16.ttf}いいえ{/font}":
                            nvl clear
                            hide screen nvlbox with dissolve
                            jump name
            show screen nvlbox with dissolve
            et "\n※[na]で宜しいですか?"
            "{size=0} {/size}{nw}"
            "{size=0} {/size}{nw}"
            menu(nvl=True):
                "{font=KH-Dot-Dougenzaka-16.ttf}はい{/font}":
                    show nvlb
                    nvl clear
                    hide screen nvlbox
                    jump day_0
                "{font=KH-Dot-Dougenzaka-16.ttf}いいえ{/font}":
                    nvl clear
                    hide screen nvlbox with dissolve
                    jump name


    return
label start_rkn:
    window hide
    $ _dismiss_pause = False
    stop music fadeout 1
    $ day = 0
    $ _game_menu_screen = None
    $ show_quick_menu = False
    $ _history = False
    scene black with dissolve
    pause 1
    br "\n「楽園へ行こう。」"
    "{nw}"
    menu(nvl=True):
        "はい":
            nvl clear
            $ na = persistent.na
            $ na2 = persistent.na2
            $ hssh_rkn = True
            jump day_0
        "いいえ":
            nvl clear
            pause 0.1
            jump prr_name
    nvl clear
    return


label day_0:
    $ persistent.na = na
    if hssh_rkn == True:
        $ save_name = "day 0, プロローグ, 楽園"
    else:
        $ save_name = "day 0, プロローグ"
    scene black
    pause 1.0
    play music 'audio/SE/prologue wind.ogg' fadein 2
    pause 5.0
    show screen at_frame

    scene bg00
    with slowdissolve
    $ _skipping = True
    $ _game_menu_screen = 'preferences'
    $ show_quick_menu = True
    $ _history = True
    show screen keymap_screen

    show screen nvlbox with dissolve
    "\n 薄暗い空、重金属の塵が散り舞う濁った空気。足を踏み入れる船内には数多の人々が行来していた。"
    "どれぐらい経っただろうか、朝出発する頃真っ白に目の前を覆っていた霧も晴れかけていた。{w}真夏のはずなのにずっと曇っているばかりだからか通りすがりの人々は皆厚く着込んでいる。"
    "お陰様で俺は予想外の寒さに列車の待ち時間の間ずっと薄着のまま寒さに震えるしかなかった。"
    et "周りの沈んだ空気にも関わらず、近くで出発を知らせる機関士の声が聞こえてくる。"
    nvl clear
    "\n 州都の駅は流石に長居出来そうな場所ではない。{w}石炭の埃に喉はやられ、冷たい旋風にどんどん体は冷えてくる。"
    et "しかもまた人の多いことやら、気を張っていないとすぐ列車を逃してしまいそうになる。{w}そうならないよう俺は自分の足を急かした。"
    hide screen nvlbox with dissolve
    scene black with dissolve
    nvl clear
    show screen nvlbox with dissolve
    "\n 今からおよそ二千年前、天地がひっくり返る程の大災害があった。"
    "瞬く間に世界に広がる災害と疫病、即ち{rb}禍{/rb}{rt}ペスティス{/ rt}と呼ばれる現象によってあらゆる土地が腐り、その影響で未だ人は長生き出来ないような環境に置かれている。"
    "禍の後、一人の生存者の男の身体に奇妙な傷痕のようなものが現れた。{w}その痕のお陰かは知らないが、男は神からのお告げを受け、国を立て直せる程の力と知恵を手に入れた。"
    "それからの人類は皆身体のどこかしらに傷痕を持ったまま生まれるようになり、それは「聖痕」と呼ばれるようになったと言う。"
    et "今じゃその聖痕の数で魔力の強さが分かるんだとか…{w}まあ、ぶっちゃけ里の大人の話は適当に流しちゃったし、詳しくは知らない。"
    nvl clear
    "\n とにもかくにも俺はそうやって再建された六つの大陸のうち、北の奥地にある小さな共同体の集落で育ってきた。"
    "昼と夜の区別すらつかない程ずっと真っ暗な州都とは違い、俺の里はずっと太陽が燦々と照り続けていた。"
    "普通の人なら生き残る事さえ困難な荒れ地の主、{w}または忘れ去られし文化の最後の継承者、{w}または……"
    et "そんな大陸のそこら辺にあるそこら辺の小さい民族集団の宗孫、{w}それが俺。{w}俺は今、ウンザリする程馴染んできた故郷を離れ、ずっと憧れ続けた州都へと向かっている。"
    hide screen nvlbox with dissolve 
    scene bg11 with dissolve
    nvl clear 
    show screen nvlbox with dissolve
    "\n 同じ顔で、同じ考え方ばっかのつまらない人間がわんさかと居る俺の故郷じゃ、軽く駄弁れるような友達すら作ることも出来なかった。"
    "兄弟や姉妹がいなかった訳ではないが、やっぱりお互い年が離れすぎてて、既に子供が出来てるぐらいのオジサンオバサンかまだ乳離れも出来てない赤ん坊ぐらい。"
    "婚期の年頃の男子なんか俺ぐらいで、それ以外はイカれちまったか四肢温存のできていない病人ばかりでこの共同体を導けるような能力はなかった。"
    et "だから大人達が誰もが俺にこの集落の未来を託そうとしていて、{w}まあそれが理解出来ない訳でもなかったけど、それでもやっぱりこんなところでジジイ共の説教なんかを聞きながら腐ってくしかない理由にはならなかった。"
    nvl clear
    "\n 周りに目を向ければ爺さんや婆さん、叔父や叔母に姉か弟、どこもかしこも家族、家族……{w}新しさを受け入れるつもりが全くなく、ずっと過去に留まったまま井戸の水のように腐っていくばかりの集団。"
    "俺はその中で大人に成るまでずっと育ってきた。もうずっと同じ顔ばっか拝むことにもウンザリしてきた。"
    "毎日来るか来ないかも知らない「あの御方」なんかに怯えて狭い倉庫で誰彼もが息を殺しながら朝を迎える生活に飽き飽きしてきたってことだ。"
    "俺は、州都へ行く。"
    et "そう想い続けて七年、目に見えるような成果は特になかった。{w}やる事もなくただ「北大陸の歴史」の本なんかを角が磨り減るぐらい読み返すなどしながら意味もない月日ばかりを送っていった。"
    nvl clear
    "\n 州都で働いてたらもうとっくに家を買って結婚して幸せな家庭を紡げていたはず…{w}そう、集落の大人に決められた俺と同じ顔のお隣のお姉ちゃんとかじゃなくて、俺が俺の意思でちゃんと選んだ人生のパートナーと！"
    "死に際、朦朧としながらも俺を呼ぶ爺さんの皺くちゃの手を握る度に、{w}ああ、俺はこんなところで一生夢も青春も味わえないまま腐っていくんだなと思うと息が詰まるようだった。"
    et "死んですら他の兄弟や姉妹と一緒に火に放り投げられて、挙句には同じ墓で人生を終えてしまうんだろうな！"
    scene black with dissolve
    nvl clear
    hide screen nvlbox with dissolve
    "\n そんなある日、俺にもやっと奇跡は訪れた。"
    "陽射しと湿気が酷くて農作物の栽培が厳しいとても忙しい時期に、外部から急に一人の「お客さん」が訪れたのだ。"
    "頬に沢山の聖痕が刻まれた蒼い瞳の真っ黒の男だった。{w}何故だかはわからなかったが俺は彼に神殿で働いてみてはどうかと提案を受ける事になった。"
    "俺は嬉しさで跳ね上がりそうになった。これこそチャンスだ。{w}こんな狭く小さい里で腐り行き死にたくだけはないと願った俺に訪れた最初で最後のチャンス。"
    et "そうやって俺は意味もない月日ばかりを送っていった。"
    $ _dismiss_pause = False
    hide screen nvlbox with dissolve
    stop music fadeout 3
    pause 4
    play sound 'audio/SE/luggage down.ogg'
    pause 2
    play sound 'audio/SE/train ongoing.ogg' 
    pause 7
    stop sound fadeout 3
    scene cg_01
    show story01
    with slowdissolve
    pause 1
    play music 'audio/bgm/train meet.ogg'
    pause 1
    nvl clear
    pause(0.7)
    show screen nvlbox with dissolve
    $ persistent.CG01 = True
    "\n 州都へと向かう列車はとても混みあっている。"
    "運良く空いた席へ咄嗟に自分の荷物を降ろした…が、ほぼ同時に誰かが降ろした荷物とぶつかってしまう。"
    "吃驚したのはお互い様のようで、小さく息を呑む音が聞こえてくる。俺よりずっと小さい体格の女の子だ。{w}荷物を持っているだけでも充分不安になるぐらいの。"
    "俺は反射的に自分の荷物を持ち上げて、そこから何歩か退く。{w}少女は小さく肩を丸めては俺と空いた席を交互に見つめてからやがて席に着く。"
    et "薄い桃色の髪のその女の子は妙に目の下が赤く、その目線はずっと下を向いたままだった。{w}まだ俺に気を遣ってたらどうしようか、それだけが気がかりで列車の喧騒の中でもずっと彼女に目線が行ってしまう。"
    scene black with dissolve
    hide screen nvlbox
    $ renpy.music.set_volume(2, channel="sound")
    play sound 'audio/SE/train moving.ogg'
    pause 4
    stop sound fadeout 3
    pause 3.5
    $ renpy.music.set_volume(1, channel="sound")
    play sound 'audio/SE/train door open.ogg'
    pause 4
    stop sound fadeout 2
    scene cg_01 with dissolve
    pause 1
    nvl clear
    show screen nvlbox with dissolve
    "\n 会話もないまま駅への到着を告げる信号が向こうから聞こえてきて、沢山の人の波が外へと流れていく。"
    "その波に押し寄せられ外に出る直前、一瞬彼女と目が遇った。軽く目礼された後、少しだけ唇が動く。{w}多分、感謝をされたんだと思う。"
    et "忙しく行き交う人々に背中を押されていくその少しの間、俺はちょっとだけ呆けていた。"
    hide screen nvlbox with dissolve
    stop music fadeout 3
    pause 1
    scene bg00 with slowdissolve
    nvl clear
    play music 'audio/SE/tutorial walking.ogg'
    pause 1
    scene bg02 with slowdissolve
    pause 1
    show screen nvlbox with dissolve
    "\n 辿り着いた建物の入り口にはちょっとした行列があった。"
    "そこは検問所らしい。{w}狭苦しい空間の窓向こうの人が修道服を着ているものだから、ぱっと見「ゆるしの秘跡」に見えなくもない妙な光景だった。{w}俺が検問所の前に立つとその人は俺を一度まじまじと見つめてから軽く待機を命令した。"
    "審査官が狭い空間の向こう側へと去り、少し後から印象が物柔らかな女性が替り席に着く。"
    et "茶髪のその女性は、さっきの人とは違って修道服の姿ではなかった。"
    hide screen nvlbox with dissolve
    stop music fadeout 2
    pause 2.0
    show SCG_14 0 with dissolve
    pause 1.0
    play music 'audio/bgm/name select.ogg'
    show screen textbox with dissolve
    gr_w "初めましてね、お名前は？"
    show SCG_14 1 with fastdissolve
    gr_w "{color=#E06666}[na]{/color}って言うのね…とても素敵な名前だわ！"
    show SCG_14 0 with fastdissolve
    if (hardmode == True):
        $ na2 = "アミー"
    elif (hssh_rkn == True):
        gr_w "「{color=#E06666}[na2]{/color}」くんって呼べばいいのかしら？"
    else:
        gr_w "わたしが何て呼んであげたらいいかしら？"
        if config.language == "Korean":
            $ init_name2 = "벨"
        elif config.language == "English":
            $ init_name2 = "Bel"
        elif config.language == "SimplifiedChinese":
            $ init_name2 = "小彼"
        else:
            $ init_name2 = "ベル"
        $ _game_menu_screen = None
        hide screen textbox with dissolve
        $ show_quick_menu = False

        $ name = renpy.call_screen("set_name2",title=" {font=KH-Dot-Dougenzaka-16.ttf}あだ名は？{/font} ",init_name2=init_name2)
        $ na2 = (name)
        $ persistent.na2 = (name)
        $ na2 = na2.strip()
        if not na2:
            if config.language == "Korean":
                $ na2 = "벨"
            elif config.language == "English":
                $ na2 = "Bel"
            elif config.language == "SimplifiedChinese":
                $ na2 = "小彼"
            else:
                $ na2 = "ベル"
        $ _history = False
        $ _game_menu_screen = 'preferences'
        $ show_quick_menu = True
        show screen textbox with dissolve
        gr_w "「{color=#E06666}[na2]{/color}」くんって呼べばいいのかしら？"
        hide screen textbox with dissolve
        nvl clear
        menu:
            "そうだ":
                show screen textbox with dissolve
                nvl clear
            "ちょっと違う":
                nvl clear
                jump name2
                label name2:
                    show SCG_14 1 with fastdissolve
                    show screen textbox with dissolve
                    gr_w "あら、ごめんなさいね。じゃあもう一度いいかしら？"
                    hide screen textbox with dissolve
                    show SCG_14 0 with fastdissolve
                    $ _game_menu_screen = None
                    $ show_quick_menu = False

                    $ name = renpy.call_screen("set_name2",title=" {font=KH-Dot-Dougenzaka-16.ttf}あだ名は？{/font} ",init_name2="")
                    $ na2 = (name)
                    $ persistent.na2 = (name)
                    $ na2 = na2.strip()
                    if not na2:
                        if config.language == "Korean":
                            $ na2 = "벨"
                        else:
                            $ na2 = "ベル"
                    $ _game_menu_screen = 'preferences'
                    $ show_quick_menu = True
                    show screen textbox with dissolve
                    gr_w "「{color=#E06666}[na2]{/color}」くんって呼べばいいのかしら？"
                    hide screen textbox with dissolve
                menu:
                    "そうだ":
                        show screen textbox with dissolve
                        nvl clear
                    "ちょっと違う":
                        nvl clear
                        jump name2
        $ _history = True
        $ _game_menu_screen = 'preferences'
        hide nvlb
    nvl clear
    $ persistent.na2 = na2
    gr_w "どれどれ……{w=0.7}うん、確かに本日の新入者名簿にあなたの名前があるわ。"
    nar "優しい声の彼女は手慣れた様子で紙を渡してくる。"
    nar "ペンを持つ手の袖奥に一つの聖痕がチラっと見えた。{w}どんな仕事をしてる人なんだろうか…"
    gr_w "聖痕はどれぐらいあるのか見せて貰ってもいい？"
    nar "俺が自信満々に両手の平を見せつけると受付窓向こうの姉さんが小さく笑う。"
    show SCG_14 1 with fastdissolve

    gr_w "ふふふ、自信いっぱいなのね。{w}とってもいいことだわ！"

    show SCG_14 0 with fastdissolve

    gr_w "でも髪は真っ黒なのに聖痕は二つしかないのね、ちょっと不思議。"
    pl "二つって少ないのか？"
    gr_w "この州都じゃあなたのような黒い髪の子はとても神聖力が強いという認識があるの。"
    gr_w "その割には少ない傾向にはあるわ。"
    pl "へえ、今までの生涯ずっと黒髪で生きてきたけどそんなことは初めて聞くな。"
    gr_w "ただの偏見よ？州都の人は噂話と偏見がとっても好きだもの。"
    show SCG_14 1 with fastdissolve
    gr_w "あなたも一晩ぐらいで有名人になってしまうかもね！"
    show SCG_14 1 at bounce
    gr_w "それじゃあ、浄化部署所属の[na]くん、中へどうぞ～"
    show SCG_14 0 with fastdissolve
    pl "浄化とやら部署とやらは何なんだ？"
    show SCG_14 1 with fastdissolve
    gr_w "あなたとっても面白い子なのね！"
    show SCG_14 0 with fastdissolve
    gr_w "何をすべきかは初日にわかると思うわ。"
    gr_w "ここまで苦労して来ちゃって疲れたでしょう？{w}今日はまずゆっくりお休みなさい。"
    gr_w "寮はこの建物の裏側にあるわ。そんな迷うほどではないとは思うけど…{w}一人で行けそう？"
    pl "こう見えて道探しは大の得意だぜ、{w}ともかくありがとな！"
    pl "姉さんってここの管理者さんなのか？"
    gr_w "ふふ、ただのおばさんよ。"
    show SCG_14 1 with fastdissolve
    gr_w "じゃあね、[na2]くん。あなたの行く道に幸運があらんことを。"
    hide screen textbox with dissolve
    hide SCG_14 with dissolve
    stop music fadeout 5
    pause 1
    $ _game_menu_screen = None
    $ show_quick_menu = False
    $ _dismiss_pause = False
    scene black with dissolve
    pause 1
    $ _skipping = False
    "\n この日、俺は冥土に足を踏み入れてしまったのだ。"
    hide screen at_frame with slowdissolve
    pause 2
    scene bgtitle with slowdissolve
    pause 5
    scene black with slowdissolve
    $ renpy.movie_cutscene("op.webm")

    nvl clear

    pause 2
    jump day1
return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
