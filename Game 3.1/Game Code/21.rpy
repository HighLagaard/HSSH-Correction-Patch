

label day1_my:
    show screen place_day1
    show screen place_my
    with None
    hide screen place_my
    hide screen place_day1
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg05 with dissolve
    else:
        scene bg05_1 with dissolve
    call place05 from _call_place05
    play music 'audio/bgm/maya.ogg' fadein 3
    show screen textbox with dissolve
    nar "部署の外をウロウロとしていると、ふとマヤが足を止める。"
    nar "薔薇の管が空高く巻かれた粗末な花壇。特に管理している人はいないのか、花は萎れている。"
    hide screen textbox with dissolve
    show SCG_02 0 with dissolve
    show screen textbox with dissolve
    my "勝手に入っちゃっていいのかな…"
    pl "周りにベンチもあるんだし、いいんじゃね？"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    show screen textbox with dissolve
    nar "マヤは座り込んでレンガの壁の中に詰まれた花壇の土を見つめる。 "
    my "あっ…！"
    nar "そんなマヤを隣から見守っていた俺は、唐突に声を上げる彼女にびっくりしてしまった。"
    pl "ど、どうした？"
    hide screen textbox with dissolve
    show SCG_02 4 with dissolve
    show screen textbox with dissolve
    my "ここ、芽が生えてきてる。"
    pl "本当だ…{w}勝手に生えてきたのか？"
    pl "こんな荒れ地なのに。エラいなぁ。"
    pl "花、好きなのか？"

    show SCG_02 6 with fastdissolve

    my "すき…だと思う、多分…"
    pl "じゃあこれからも辛くなったら息抜きにでもここに来たらどうだ？"
    pl "たまに水やりもしたりさ。"

    show SCG_02 0 with fastdissolve

    my "…そんなことしちゃっていいのかなぁ…"
    pl "大丈夫だって、俺も手伝うから、な！"

    show SCG_02 6 with fastdissolve

    my "…うん。"
    stop music fadeout 3

    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    pause 2
    $ day_my = True
    $ day_time = day_time +1
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with slowdissolve
    else:
        scene bg02_1 with slowdissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_1
    return


label day1_hk:
    show screen place_day1 
    show screen place_hk
    with None
    hide screen place_hk
    hide screen place_day1
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg04 with slowdissolve
    else:
        scene bg04_1 with slowdissolve
    call place04 from _call_place04
    play music 'audio/bgm/dialogue.ogg' fadein 3
    show screen textbox with dissolve
    nar "人が沢山流れ出ていく道の方を何となくでわざと遡っていくと、{w}そこは焦げた臭いと煙の充満した場所だった。"
    hide screen textbox with dissolve
    show SCG_02 0 with dissolve
    show screen textbox with dissolve
    pl "なあ、向こうでなんか燃えてないか？"
    my "浄化部は、その…{w}\nゴミ拾いとかもしたりするから、それの処理場じゃないかなあ…"
    pl "へえ、じゃあ言うならこれも仕事場みたいなもんなんだな。"
    my "う～ん…たぶんそうかも…"

    show SCG_02 5 with fastdissolve

    my "…え、行っちゃうの…？"
    pl "ああ、うん。マヤは？あんま行きたくねぇのか？"

    show SCG_02 7 with fastdissolve

    my "わ…わたしは…ここにいるだけで鼻がツーンとしちゃって…"

    show SCG_02 0 with fastdissolve

    my "進んで行きたくはない、っていうか……\nうん、[na2]くんだけでお願いしてもいいかな…"
    my "わたし、他のとこ見てくるね…"
    pl "そっか…{w}\nじゃあしょうがないか。また後でな！"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    pause 1
    show screen textbox with dissolve  
    nar "彼女だけ一人置いて行くのは少しばかり引っ掛かるが、{w}今日は俺もなるべく色んな所を目に留めておきたい。"
    nar "こればかりは仕方がないか。"
    hide screen textbox with dissolve
    show screen nvlbox with dissolve
    "\n ぱっと見十数人ぐらいは入れそうな広い空間なのにも関わらず、皆仕事を終えるなりさっさと出て行ってしまうのか誰もいなくて静まり返っていた。"
    "錆びたコンテナのみが並ぶ場所で、周りを見渡せばふと聞き慣れた音とともに見慣れた顔が目に入る。"
    "少し離れた場所に、昼最後に見た時と同じく片手で荷車を引くシーキュレット。"
    hide screen nvlbox with dissolve
    nvl clear
    show SCG_03 7 with dissolve
    show screen textbox with dissolve
    pl "おい！"

    show SCG_03 8 with fastdissolve

    sc "……"
    pl "無視すんなって。{w}まだ仕事終わってないのか？"
    pl "見かけによらず誠実なんだな！"

    show SCG_03 7 with fastdissolve

    nar "近寄れば近寄るほど焦げた臭いが濃くなっていく。"
    nar "獣臭さが溶け込んだカビっぽい臭い。{w}\nたまに故郷でも嗅いだことがあった。"
    pl "ここって…火葬場か？"

    show SCG_03 8 with fastdissolve

    sc "…それに近いだろうね。"
    nar "もっとちゃんと説明してくれたっていいじゃないか。{w}彼はまたそのまま口を閉じてしまう。"
    nar "これからまた仕事に戻るらしい。{w}とんだ優等生サマだ。"
    nar "彼を見ていると昼のことを思い返す。{w}\nただでさえやせ細ってる奴なのに、食事は結局どうしたんだろう。"

    show SCG_03 0 with fastdissolve

    nar "そんなしょうもないことを考えていたら、彼のうなじの薄い髪の中うっすらと青黒い痕みたいなものが見える。"
    nar "聖痕か？{w}妙に分かりにくいところにあるんだな。"
    pl "ここ、ゴミ付いてるぜ。"

    show SCG_03 5 with fastdissolve

    sc "…！"
    nar "首筋に付いていた白い埃のような物を取り除いてやると、シーキュレットは一瞬肩を震わせ俺の手から逃れようとするように"
    nar "身を小さく丸める。"
    nar "彼はかなり吃驚してしまったのか目を丸くして俺の方を振り向くも、すぐまた顔を逸らした。"
    nar "うちの鶏でもここまで俺を警戒したりはしなかったぞ。{w}彼の敏感な反応に俺は少しだけ気まずくなってしまう。"

    show SCG_03 0 with fastdissolve

    sc "……やることないなら早く寮に戻りなよ。"
    pl "ちょっ…話しようって言ってるじゃねーか！{w}さっきからシカトしやがって。"

    show SCG_03 2 with fastdissolve

    sc "ボクがキミと？一体何を？"
    pl "ああハイハイ、お前の性格が悪いのはもう充分わかったから…"
    pl "けどさ、俺にならわかるけど、マヤには優しくしてやれよ。"
    sc "……"
    pl "お前だってみりゃあ分かるだろ、あの子は女の子なんだし…"

    show SCG_03 0 with fastdissolve

    sc "彼女が女なのと仕事ができないのには何の関係があるんだい。"
    nar "コイツ、バッサリ仕事ができないとか言いやがりましたよ。"
    pl "おい、マヤが聞いたらどうするつもりだよ！"

    show SCG_03 9 with fastdissolve

    sc "……"

    show SCG_03 0 with fastdissolve

    sc "あと…もうちょっとお願いする時の態度っていうのがあるものだろ。"

    show SCG_03 8 with fastdissolve

    sc "特採で来た癖に仕事もせず初日から女ばっか追いかけてるとか、本当に底が知れるね。"
    pl "黙って聞いてりゃテメェ、さっきからずっと生意気な口ばっか叩きやがって…何様だ？"

    show SCG_03 7 with fastdissolve

    sc "黙って聞いてあげたのはこっちだろ。{w}生意気ばっか言うのもそっちだし。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    show screen textbox with dissolve
    nar "ガン！コンテナが叩かれる鈍い音が響く。{w}驚く間も与えられず今までずっとこちらに背を向けたままだった彼と目が合った。"
    nar "怒りを抑えているかのようにこちらを真っ直ぐ睨み付けている。"
    nar "奴は神経質混じりの溜息を吐いてはゆっくりこちらに向かって歩き始めた。"
    hide screen textbox with dissolve
    show SCG_03 2 with dissolve
    show screen textbox with dissolve 
    sc "オマエさ、"
    sc "人の仕事に一々首突っ込んでいいくらい自分が何か特別だとでも思ってるの？"
    pl "な、何だって…"
    sc "ボクが今何を言ってるのか理解すら出来てないだろ。{w}オマエがこの処理班で、「冥土」で何が出来るのかって聞いてるんだよ。"
    nar "思いも寄らなかった状況で逆に冴えきってしまった頭で違和感だけがぐるぐると廻る。"
    nar "処理班？冥土？セイント・シェオルの浄化部の話なのか？"

    show SCG_03 0 with fastdissolve

    sc "キミの尻拭いは他を当たってくれ。"

    show SCG_03 72 with fastdissolve

    sc "じゃあ、お疲れ様です。{w}また寝坊したくなかったら早く帰った方がいいよ。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    show screen textbox with dissolve
    nar "口に出すほど整理することはできなかった言の葉たちを喉元で突っかからせている間、とっくに彼は俺を通り過ぎて帰っていく。"
    nar "俺はまた何も言えないままただポツンと残されただけだった。"
    nar "一人取り残された俺はこのどうしようもない静寂に耐えきれずまたトボトボと歩き始めた。"
    nar "あの態度と冷たい警告のせいで逆に反抗心が湧いてきたからであった。"
    nar "とにもかくにもイヤなヤツだぜ。"
    nar "どっかで聞いた言葉じゃ初印象がその人の全てを語るとあったはずで、{w}それが事実なら彼は最悪だった。"
    nar "周りからの評判が悪いのもそれとなくわかった気がする。"
    nar "初対面の人間に対してあの敵対心いっぱいの顔、わざとなのかちんぷんかんぷんな言葉選び。"
    nar "お陰様で頭の中がぐちゃぐちゃだ！"
    pl "やれやれ、初日から散々だぜ。"
    stop music fadeout 3

    hide screen textbox with dissolve
    $ day_hk = True
    $ day_time = day_time +1
    pause 2
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with slowdissolve
    else:
        scene bg02_1 with slowdissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_1
    return



label day1_gr:
    show screen place_day1
    show screen place_gr
    with None
    hide screen place_gr
    hide screen place_day1
    with dissolve
    pause 1
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg03 with slowdissolve
    else:
        scene bg03_1 with slowdissolve
    call place03 from _call_place03_2
    show screen textbox with dissolve
    if hssh_rkn == True:
        nar "ロビー中央の大きな噴水を通り廊下を進んでいく。"
        nar "光をそのまま受けた埃が窓の辺りできらきらと漂っている。"
    else:
        nar "ロビー中央の大きな噴水を通り暗い廊下を進んでいく。"
        nar "あちこちから人の声が聞こえてくるのに空は真っ暗だなんて、おかしなもんだ。"
    nar "道中ずっと鼻先に残っていた大理石の冷たい匂いが、角を回るとガラッと変わってくる。"
    nar "バター込みの生地を焼いたような香ばしく甘い香り。{w}ここからかなり近い。"
    hide screen textbox with dissolve
    show SCG_02 0 with dissolve
    show screen textbox with dissolve
    my "は、入っちゃダメ…なんじゃないかな…？"
    pl "新入りって言ったら見逃してくれるんじゃないか？"
    my "でもぉ…"
    hide screen textbox with dissolve
    hide SCG_02 0 with dissolve
    show screen textbox with dissolve  
    nar "揉めている間、ドアが先に開いてしまいマヤの悲鳴が高々と耳元に響く。"

    hide screen textbox with dissolve
    stop music fadeout 1
    show SCG_02 5 at right
    show SCG_14 7 at left
    with dissolve
    pause 1
    show screen textbox with dissolve
    gr_w "あらあら…"
    pl "あっ！"

    show SCG_02 0 with fastdissolve

    my "あ…"
    play music 'audio/bgm/daily.ogg'

    show SCG_14 1 with fastdissolve

    gr_w "あなたたちだったのね！{w}今は休憩中かしら？"
    gr_w "さあさあ、そこに立ってないで入っておいで？"

    show SCG_02 7 with fastdissolve

    my "それが、そのぉ…"
    pl "おう！じゃあ失礼するぜ！"

    show SCG_02 0 with fastdissolve

    my "あうう…"

    hide screen textbox with dissolve
    hide SCG_02
    hide SCG_14
    with dissolve
    stop music fadeout 1
    pause 1
    if hssh_rkn == True:
        scene bg06 with slowdissolve
    else:
        scene bg06_1 with slowdissolve
    call place06 from _call_place06
    play music 'audio/bgm/Grette.ogg'
    show screen textbox with dissolve
    nar "入ると部屋は真っ白で温かく、廊下からも香っていたふわふわした匂いでいっぱいだった。"
    nar "先ほどの光景なんて忘れてしまいそうになるぐらい。{w}こんな殺伐とした建物にこんな場所があるなんて。"
    nar "静かなカタカタ音に目を向けると、パーテーションの向こう側で薄暗い印象の男がタイプライターを打っている姿が見える。"
    nar "来客にすら気付いていないのか目線はずっと紙と睨めっこしたまんまだ。"
    hide screen textbox with dissolve
    show SCG_02 0 at right
    show SCG_14 0 at left
    with dissolve
    show screen textbox with dissolve    
    gr_w "あら！{w}丁度菓子が切れちゃってるわ…{w}\n二人とも紅茶でいいかしら？"
    my "えと、大丈夫、です…"
    pl "牛乳はないですか～？"

    show SCG_14 1 with fastdissolve

    gr_w "ありますよ～{w}じゃあ[na2]くんは牛乳ね。"
    hide screen textbox with dissolve
    hide SCG_02 0 at right
    hide SCG_14
    with dissolve
    pause 0.5
    show SCG_14 0 at center with dissolve
    show screen textbox with dissolve  
    nar "彼女は俺が神殿に来て初めて会話を交わした人だった。{w}ふわふわとした口調に優しい声。{w}何だか気持ちが穏やかになる。"
    nar "しかしやはり何度見ても司祭の服装ではなく、{w}白衣を羽織っているためどちらかというとお医者さん、という印象だった。"
    nar "その代わりか、胸のポケットには他の司祭たちのものと似たようなロザリオのネックレスがブローチの様に掛かったまま光っていた。"
    hide screen textbox with dissolve
    show SCG_02 0 at right
    show SCG_14 0 at left
    with dissolve
    show screen textbox with dissolve 
    gr_w "熱いから気を付けてね。"
    my "ありがとうございます…"
    pl "あんがとさん！{w}てか、姉さんって本当は何してる人なんだよ？"

    show SCG_14 7 with fastdissolve

    gr_w "あらま、わたしとしたことが…{w}\nそういえばちゃんと紹介してないわね。"
    hide SCG_02 0 at right
    show SCG_14 1 at center
    with dissolve
    gr "わたしは{color=#d9ead3}グレーテ{/color}。{w}保健部で働いているわ。"
    gr "保健部の説明も多分まだかしら？{w}神殿の人々を治療したり、診てあげるところなの。"
    pl "おお、何だか先生みたいだな！"

    show SCG_14 0 with fastdissolve

    gr "うふふ、じゃあ先生って呼んでくれる？{w}そう呼ばれるのが実は好きなの。"
    gr "もし困った時や相談したい時はいつでも\nいらっしゃい？"

    show SCG_14 1 with fastdissolve

    gr "紅茶とクッキーが食べたくなった時でもいいけど！"
    show SCG_02 0 at right
    show SCG_14 1 at left
    with dissolve
    my "ありがとうございます…色々と…"
    pl "へぇ…神殿にもこんな人情のある人っているんだな。"

    show SCG_14 8 with fastdissolve

    gr "勿論！神殿にはいい人ばかりよ？"

    show SCG_14 0 with fastdissolve

    gr "そうだ、浄化部の主教様にはもう会った？"
    my "それが、今日は忙しいって…"

    show SCG_14 7 with fastdissolve

    gr "あら、そう…"
    pl "そういえば気になってたけど、その人ってどんな人なんだ？"

    show SCG_14 1 with fastdissolve

    gr "{color=#cfe2f3}ハク・エカルラン{/color}。{w}あの子はねえ、凄い子なのよ！"

    show SCG_14 0 with fastdissolve

    gr "尋常じゃないわ、あなたたちよりも少しだけ年上だった頃神殿に就職してもう主教様になっちゃったもの。"

    show SCG_14 8 with fastdissolve

    gr "とても強くて、誰よりも優しくて、いつも努力を惜しまない素敵な人だからね、"

    show SCG_14 1 with fastdissolve

    gr "あなたたちもきっと好きになってくれると思うわ。"
    pl "やっぱ聞いてるだけじゃなーんもわかんねぇや。先生とは長い付き合いなのか？"

    show SCG_14 8 with fastdissolve

    gr "そうねぇ…随分長いわ。"
    gr "人の価値というものは見届けた時間が長ければ長いほどわたしの中でちゃんと形になっていくの。"

    show SCG_14 0 with fastdissolve

    gr "あなたたちともそういった関係に是非なってみたいわ。"

    show SCG_14 1 with fastdissolve

    gr "これからも色々大変だろうけど頑張って頂戴ね。{w}先生、応援してるわ！"

    show SCG_02 7 with fastdissolve

    my "はい…"
    pl "また来るぜ！"
    stop music fadeout 3

    hide screen textbox with dissolve
    hide SCG_02
    hide SCG_14
    with dissolve
    $ day_gr = True
    $ day_time = day_time +1
    pause 2
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with slowdissolve
    else:
        scene bg02_1 with slowdissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_1
    return


label day1_hakuB:
    if hssh_rkn == True:
        $ save_name = "day 1, 夜, 楽園"
    else:
        $ save_name = "day 1, 夜"
    pause 1
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg02_1 with dissolve
    else:
        scene bg02_2 with dissolve
    stop music fadeout 3
    call place02 from _call_place02
    show screen textbox with dissolve
    if hssh_rkn == True:
        nar "…もう夕暮れ時だ。"
    else:
        nar "…もう空が真っ暗だ。"
    hide screen textbox with dissolve
    show SCG_02 7 with dissolve
    show screen textbox with dissolve
    my "そろそろおねえちゃんたち戻ってるかも…"
    pl "じゃあマヤは先に寮に戻っとくか？"

    show SCG_02 0 with fastdissolve

    my "え、[na2]くんは…？"
    pl "俺はもうちょいだけ見回ってからいくぜ。"

    show SCG_02 7 with dissolve

    my "ほ、ほんとに迷っちゃったらどうするの…"
    pl "大丈夫だって！俺は道探しだけは大の得意だぜ！"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    show screen textbox with dissolve
    nar "肩を落としてとぼとぼと帰るマヤを見送ってから俺は一度身体をグッと伸ばす。{w}まずはこの近辺の道をちゃんと把握しておこう。"

    hide screen textbox with dissolve
    $ show_quick_menu = False
    show screen place_day1_hkB with fastdissolve
    $ place = renpy.call_screen("place_day1_hkB")
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
