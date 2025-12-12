label day4:
    $ day = 4
    if hssh_rkn == True:
        $ save_name = "day 4, 朝, 楽園"
    else:
        $ save_name = "day 4, 朝"
    play sound 'audio/SE/bell 1.ogg' fadein 2.0
    image 4day = Text("day 4",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '4day' at day00 with slowdissolve
    pause 5
    hide expression '4day' with slowdissolve
    stop sound fadeout 1.0
    pause 3.0
    show screen at_frame  with dissolve
    play music 'audio/bgm/dream.ogg'fadein 5.0
    pause 4.0
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    $ _game_menu_screen = 'preferences'
    show screen keymap_screen
    $ renpy.music.set_volume(1, channel="music")
    scene bg12
    show screen TrackCursor
    show screen grumbleBG12
    with slowdissolve
    pause 1
    show screen nvlbox with dissolve
    if hssh_rkn == True:
        br "\n 十分固まって冷たい盛り土。{w}俺はその上に立っている。{w}周りを見回る為に動いた足下にとろっとした泥がくっつく。{w}{nw}"
        extend "\n足を上げて確認してみれば、それは泥ではなかった。{w}動物の内臓だ。{w}崩れた腸から、膿汁のような粘液質が噴き出していた。{w}{nw}"
        extend "\n床に散らばった死体。頭の上に零れるぬるい血。まるで誰かの墓穴の中にいるみたいだ。{w}ここは俺の知っている世界だ。"
        nvl clear
        br "\n ……ぶんぶんと、奇妙な音が耳元に響く。黒い影が目の前で揺らぐ。{w}温かい湿気に触れた体がくすぐったい。{w}{nw}"
        extend "\n蠅。無数の蠅の群れが腕に付いている。{w}蠅の付いた腕は真っ黒だ。{w}{nw}"
        extend "まるで死にゆく俺から生命力を吸い取るように、小さな生物たちが休まず羽搏いている。"
        hide screen nvlbox with dissolve
        pause 1
        hide screen grumbleBG12
        show cg08 onlayer screens:
            yoffset -600
            ease 5 yoffset -500
        with slowdissolve
        pause 2.5
        nvl clear
        hide cg08 onlayer screens
        show screen grumble_cg08
        show screen nvlbox
        with dissolve
        br "\n ふと、耳と頭の中に染みた感じ慣れた悍ましさに顔を上げる。{w}暗い天井から、天使の輪郭が見える。{w}{nw}"
        extend "\nその形体は俺に向けて手を伸ばしているように見えた。{w}圧倒的といえるほどに美しかった。{w}{nw}"
        extend "\n人として持つべき敬拝。{w}然るべき恐怖。全ての感情があの燦爛な存在にあった。{w}{nw}"
        extend "\nいつの間にか俺を抱きついた天使は俺の下腹に白い手を置いた。徐々に冷や汗をかく。{w}{nw}"
        extend "\nしかし俺はその手を受け入れる。{w}彼女は俺の抵抗できない存在、敢えて振り払えない存在だからだ。"
        nvl clear
        br "\n 優雅な、汚さを知らない手の上を、真っ黒の虫が汚い足を付けたままで這う。{w}{nw}"
        extend "\n彼女は嫌がる気配はなく、寧ろ微笑んでは優しく囁いた。{w}{nw}"
        extend "\n\n「また必要な物があったら言ってね…わたしに。」{w}{nw}"
        extend "\n\nやがて天使の顔が目に入る。{w}{nw}"
        extend "\n彼女の顔。{w}{nw}"
        extend "\n俺は確かに彼女と会ったことがある。"
    else:
        br "\n 気が付けば見慣れた空の下。{w}足元を引き摺るべっとりした泥。腐った腸の臭いに頭が割れそうだ。{w}{nw}"
        extend "\n誰のものかも分からない血肉が頭上に降り掛かる。{w}夢だ。{w}あの夢だ。{w}{nw}"
        extend "\n天使の夢だ。{w}か細い腕が俺を連れ去ろうとするかのよう強く抱きしめる。{w}{nw}"
        extend "今にでも落ちてしまいそうな崖っぷちを俺の足先が危うく指している。{w}{nw}"
        extend "\n何故こうなってしまったのか、なんて覚えてすらいない。{w}荒い息を呑めば背後から気配を感じる。{w}{nw}"
        extend "頬を擽る髪の毛、この空間に全くそぐわない柔い息の音。{w}{nw}"
        extend "\n天使様、だ。"
        hide screen nvlbox with dissolve
        pause 1
        hide screen grumbleBG12
        show cg08 onlayer screens:
            yoffset -600
            ease 5 yoffset -500
        with slowdissolve
        pause 2.5
        nvl clear
        hide cg08 onlayer screens
        show screen grumble_cg08
        show screen nvlbox
        with dissolve
        br "\n 天使は俺を抱いたまま離さない。{w}首が回らない、手には力が入らない。{w}{nw}"
        extend "\n力を振り絞って地面を蹴り腕を振り払おうとするも靴や服に付いた血と内臓を潰し返す様になるのみだった。{w}{nw}"
        extend "\n目眩がするぐらい降り注がれる光、真っ白な空。{w}天使の翼が広がり俺の頭上に影が差す。{w}{nw}"
        extend "\n天使は俺の身体を更に強く抱き締める。内臓が押し潰される様な感覚だった。{w}天使の温もりが伝わってくるが同時に背筋の凍る様な悪寒すら感じる。{w}{nw}"
        extend "\n天使は俺の怯え切った顔を見下ろしながら優しく微笑んだ。"
        nvl clear
        br "\n 「放せっ…！」{w}{nw}"
        extend "\nその御許から逃れようと足掻くとやっと天使を振りほどいた。{w}{nw}"
        extend "\nやがて天使の顔が目に入る。{w}{nw}"
        extend "\n彼女の顔。{w}{nw}"
        extend "\n俺は確か、彼女と出会った事があるのではないだろうか？"
    nvl clear
    hide screen grumble_cg08
    hide screen nvlbox
    show cg08 onlayer screens:
        yoffset -500
        ease 4.5 yoffset -440
    stop music fadeout 2
    with dissolve
    pause 2
    hide cg08 onlayer screens
    hide screen TrackCursor
    scene black
    with slowdissolve
    pause 2
    with dissolve
    if hssh_rkn:
        scene bg10 with dissolve
    else:
        scene bg10_1 with dissolve
    call place10 from _call_place10_2
    $ show_quick_menu = False
    show screen morning with fastdissolve
    $ renpy.call_screen("morning")
    if hssh_rkn:
        scene bg14 with dissolve
    else:
        scene bg14_1 with dissolve
    call place14 from _call_place14_1
    pause 1.0
    show screen textbox with dissolve
    show SCG_05 1 with dissolve
    play music "audio/bgm/daily.ogg"
    hk "ではみなさ～ん、今日も互いに愛し合い、頑張りましょう～♪"
    hide SCG_05 with dissolve
    nar "騒ぎの中で一人か二人だけが答える。"
    nar "主教の挨拶が終わるとシーキュレットが黙礼をする。{w}いつものような朝の始まりだ。"
    show SCG_03 idle with dissolve
    sc "ボクが帰るまで移動せずに待機。{w}今日の仕事は新入りには難しいだろうから、しっかりした方がいいよ。"
    hide SCG_03 with dissolve
    nar "シーキュレットがハク主教の後に付いて出る前に一言を言う。"
    nar "何かを聞こうとする間もなく、シーキュレットは廊下の突き当りへ消える。{w}アイツはいつもそうだ。"
    nar "仕方なく、俺はお互い様のマヤと一緒に部室に座り、彼を待とうとした。"
    show SCG_02 idle with dissolve
    my "キューくん、いつも主教様と共に何してるのかな……"
    pl "書類の片づけとか？"
    show SCG_02 7 with fastdissolve
    my "キューくん、大変そう……{w}主教様の仕事を手伝いながら浄化部の仕事もしないとならないでしょう？"
    pl "うん、そりゃあいつがここの補佐教？らしいから。"
    pl "あいつが何でわざわざそんなめんどくさい仕事を引き受けるのかは俺もよく分からんけど…"
    nar "正直、補佐教については何も知らない。{w}昨日グレーテ先生に簡単にいくつかを教えてもらったが、それだけだ。"
    nar "それでも俺はひとまず頭に浮かぶ単語をそのまま吐き、言葉を繋いだ。{w}多分マヤとの対話を断ちたくなかっただろう。"
    my "うーん、そんなんじゃなくて…{w}何と言うか、キューくんはいつも主教様と一緒にいるんだよね。"
    my "うちの主教様って、少し馴染み難いって言うか……"
    pl "え、マヤもそう思った？"
    show SCG_02 0 with fastdissolve
    my "うん？"
    pl "主教様ってさ、時々調子がおかしくね？その…会話中にいきなり真顔になるって言うか……"
    pl "本当に見た事あるってワケじゃないんだけど、雰囲気がさ。"
    my "うん……"
    pl "なんか……忌まわしいような……"
    my "うん……そうかな……"
    pl "……こんなこと、むやみに言っちゃだめだがな。"
    show SCG_02 8 with fastdissolve
    my "でも、主教様ってちょっと……話すのが緩いだけで、嫌な感じとか……忌まわしい感じではないというか……"
    pl "そ、そうよな。"
    show SCG_02 0 with fastdissolve
    my "[na2]くんが敏感なだけじゃないかな……"
    pl "……"
    show SCG_02 at bounce
    my "……[na2]くん、なにかあったの？"
    play sound "audio/SE/ding.ogg"
    pl "あ、うん？"
    nar "正直、金髪女のことを考えてなかったと言ったら嘘になる。"
    nar "違うと言えば良いものだが、何故か口が開けなかった。"
    nar "気まずい静寂が続き、マヤから先に話をかけた。"
    show SCG_02 8 with fastdissolve
    my "……何でもないなら、それでいいよ……"
    nar "その言葉とは違って、マヤはまだ何か言いたいように周りを見回した。"
    show SCG_02 0 with fastdissolve
    my "あの、[na2]くん。その…{w}金髪のお姉ちゃんとどんな関係？"
    stop music 
    pl "何？"
    nar "心臓が凍り付く。" with sshake
    play music "audio/bgm/r18.ogg" fadein 5
    pl "何でそんなことを聞くんだ？"
    my "何でって…わたし、[na2]くんがその―{space=-3}―{space=-3}―に、―{space=-3}―のを見て……"
    nar "俺が大声を出したせいで驚いたのか、マヤは頭を下げてむにゃむにゃ言う。"
    nar "州都の言語に慣れていないせいか、俺は彼女が今何を言っているのかよく分からない。"
    show SCG_02 5
    play sound "audio/SE/hit.ogg"
    pl "何を？" with sshake
    extend "何を見たってんだ、マヤ！" with sshake
    nar "狼狽した俺は彼女に聞き返した。{w}が、俺のこういう行動が彼女を怖がらせたことに気付いて、言い訳の為に深呼吸をした。"
    hide SCG_02 with dissolve
    nar "単なる偶然か、同時に後ろから何かが飛んできた。" with hpunch
    nar "べちゃべちゃして冷たい感覚のあれは、俺の背中に触れてはあっけない音をして地面に落ちた。"
    nar "自然に口を止めて、音のした方に視線を向ける。"
    $ renpy.music.set_volume(0, channel="music")
    hide screen textbox
    play sound "audio/se/noise.ogg"
    show BG12_ns at ns
    pause 0.1
    stop sound
    hide BG12_ns
    show screen textbox
    $ renpy.music.set_volume(1, channel="music")
    nar "{cps=*2.0}そこには鮮紅の塊が、黄色い塊と青黒い血管が纏わりついたまま落ちている。にじみ出た血が木の床を汚している。{/cps}"
    $ renpy.music.set_volume(0, channel="music")
    hide screen textbox
    play sound "audio/se/noise.ogg"
    show BG12_ns
    pause 0.1
    stop sound
    hide BG12_ns
    show screen textbox
    $ renpy.music.set_volume(1, channel="music")
    pause 0.05
    $ renpy.music.set_volume(0, channel="music")
    hide screen textbox
    play sound "audio/se/noise.ogg"
    show screen grumbleBG12
    pause 0.2
    stop sound
    show screen textbox
    $ renpy.music.set_volume(1, channel="music")
    nar "{cps=*2.0}ふと夢のある場面が頭をよぎる。{/cps}"
    nar "{cps=*2.0}ふざけた話だが、困惑という感情は行き過ぎると逆に何も感じなくなるみたいだ。{/cps}"
    hide screen grumbleBG12
    stop music
    play sound "audio/se/pii.ogg" loop 
    pause 0.1
    stop sound fadeout 6
    nar "やがて鉄を掻くような、醜い男の悲鳴が聞こえた。" with sshake
    nar "俺の喉からの声だ。{w}それに気付くには、そんなに長くはかからなかった。"
    nar "俺の驚きを楽しんでいるように、周りで何人かが嗤い出す。"
    play music "audio/bgm/dialogue.ogg" fadein 5
    nar "顔を上げると、行き来して何度か見たような浄化部の司祭のやつらがいた。見慣れた顔ではない。"
    show SCG_02 5 with dissolve
    my "[na2]くん…"
    nar "厚いおしろいを付けた女たちと、わざとだぶだぶした服を着た男たちでできている、不良の群れ。"
    nar "彼らがニヤニヤしながらこっちを見ていた。"
    hide SCG_02 with dissolve
    nar "記憶をたどると、確かにどこかで見たことがある。{w}あの金髪女の周辺にいた人たちだった。"
    nar "その中の一人は俺と目が合うと、わざと大げさな声と仕草で剽軽な真似をした。"
    ex1 "はっ…バ、バレた！"
    nar "それを聞いて、笑いを堪えるように肩を叩く横の人。"
    ex2 "こら、何そんなとこに投げてんだ！ちゃんと照準しなよ！"
    nar "軽薄な笑い声。"
    ex1 "……―{space=-3}―…悪いって、おい、怒ってんの？"
    ex2 "惚けてんじゃん？うわ…こいつネズミ見るの初めてかよ。"
    nar "騒がしく飛び交う言葉の中で、誰かの言葉が耳に当たった。"
    nar "ネズミ？俺は「あれ」を見直した。{w}床には、毛が強くもつれて、瞳孔が濁ってる、死んだネズミの死体。"
    nar "確かに、先に見たのはせいぜいこんなものじゃなかった。"
    pl "い、いや、でも、さっき…"
    nar "慌てて当たった所を擦ってみた。{w}その手には、当然、血など付いてない。"
    nar "その時、群れに割り込んできた声がボケてる俺の耳を更に叩いた。{w}高く、弾むような、あの汚らわしい鼻声。"
    show SCG_102 1 with dissolve
    lz2 "ああん、もう、きみたち、なんでうちの後輩ちゃんいじめてんのよ～"
    show SCG_102 4 with fastdissolve
    lz2 "[na2]ちゃん、気が弱いから、驚いちゃったじゃん～"
    nar "ずいぶんとニヤニヤしていた女は、群れに混ざってたやつらと一緒に喉を鳴らしながら笑う。"
    nar "どんな話が行き交ったのか知りたくもない。"
    hide SCG_102 with dissolve
    ex2 "また一緒にいるな、そばかす女の妹ちゃん！お前たち付き合ってんの？"
    ex1 "おい！そんなこと言ったら首がぶっ飛んじゃうぞ、あいつあれだろう、魔導部の…"
    ex1 "アルネ・アルタナータの、{rb}ア{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}レ{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}…"
    nar "小指一本を出して振る仕草。{w}俺はあのジェスチャーを初めて見たが、奴らが言いたいことはすぐにでも分かってしまった。"
    ex2 "羨ましいな、おい。何をどうすればド田舎出身がそうなれるんだ？{w}姫の御前でパンツでも脱いだのか？"
    ex1 "うわ、じゃあもう乳繰り合っただけじゃねーんだよなぁ？"
    lz2 "つよいね～"
    nar "飽きもせずに笑いが弾き、睨みつく視線を一身に受けたマヤはどこにも隠れずに立ったまま固まっている。"
    nar "軽薄に飛び交う言葉に気が遠くなる。全部、全部知ってるんだろうか。" with sshake
    scene bgw with fastdissolve
    nar "いつから？{w}知らなかったのは、張本人の俺だけ？{w}このことをどれだけ多くの人が知ってるんだろう？"
    nar "頭の中に浮かんでくる数々の混乱の中の一つを問い出すために、口を開けた瞬間。"
    play sound 'audio/se/wake up.ogg'
    stop music
    if hssh_rkn:
        scene bg14 with dissolve
    else:
        scene bg14_1 with dissolve
    show screen textbox 
    sc "仕事に向かわずに何をやっているんだ。" with hpunch
    ex2 "うわっ、補佐教様じゃん！こっわ～"
    ex1 "ネズミが死んだから、母親かと思って来たんだ！"
    hide screen textbox with dissolve
    show SCG_03 2 with dissolve
    show screen textbox with dissolve
    nar "運よく入ってきた彼の一言で群れは瞬時に散らばった。"
    nar "彼らが部屋を完全に出ようとする最中、シーキュレットが金髪の女性一人だけを呼び止めた。"
    show SCG_03 0 at left
    show SCG_102 5 at right
    with dissolve
    sc "キミは主教室に行きなさい。主教様からの御呼びだよ。"
    lz2 "は～い。"
    hide screen textbox with dissolve
    hide SCG_102 with dissolve
    hide SCG_03 with dissolve
    pause 1.0
    play sound "audio/se/door slide.ogg"
    pause 2.0
    show screen textbox with dissolve
    nar "彼女を最後に、さっきまでの大騒ぎがまるで嘘のように静まった部屋には、俺たち三人だけが残った。"
    pl "……"
    show SCG_03 7 with dissolve
    play music "audio/bgm/daily.ogg"
    sc "いつまでそうしてるつもりだ。準備しろ。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    nvl clear
    pause 2
    if hssh_rkn:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03_5
    show screen textbox with dissolve
    pl "あの、魔導部のことだが…"
    show SCG_03 0 at left
    show SCG_02 idle at right
    with dissolve
    "{nw}"
    show SCG_03 at bounce
    sc "…魔導部が何？"
    nar "二人は驚く気配も、何かを聞いてくる気配もない。"
    nar "俺が編入してきた理由、アル姉との婚約…知らなかったのは本当に俺だけだった。"
    show SCG_02 at bounce
    my "[na2]くん…大丈夫…？ネズミ見るの、本当に初めて？"
    pl "そ、そんなワケじゃ。"
    pl "さっきはちょっと…うん、ちょっと疲れてるのか…"
    show SCG_03 8 with fastdissolve
    sc "仕事もしないくせに夜に出回るからそうなるんだよ。"
    pl "よく知ってるね。"
    pl "俺のこと、好きになられても困るんだぞ～"
    show SCG_03 0 with fastdissolve
    sc "…それ本気で言ってるの？"
    pl "またマジになって食い付いちゃって。"
    pl "でもお前って、口ではそんなこと言いながら、何かあった時にはいつも助けに来てくれるんだな。"
    sc "助けに来てるわけじゃないんだけど。"
    show SCG_02 4 with fastdissolve
    my "でも、キューくんが来てくれて本当に嬉しいよ…ありがとう、キューくん。"
    sc "はあ…{w}あんな奴ら、一々相手する必要ないさ。どうせあんな奴らは一か月程度仕事してはもう来ないから。"
    show SCG_02 0 with fastdissolve
    my "辞めれるんだ、浄化部って…"
    pl "え？マジか。部署を移る奴らって他にもいるんだ。"
    sc "……"
    nar "また気まずい瞬間に奴が口を閉ざしたせいで、マヤが顔色を窺っては先に口を開く。"
    nar "沈黙を破る彼女の一言がありがたく、俺も口を挟む。"
    show SCG_02 at bounce
    my "あの、キューくんって、浄化部で働いてからどれぐらい経ったの？"
    pl "そうだ！お前って、そんなに熱心に働いてるくせに処理班で何年腐ってるんだ？もっと上を目指さないとな。"
    hide SCG_03
    hide SCG_02
    with dissolve
    nar "俺は相変わらず口を閉じている彼の細い背中をパンパンと叩く。優しいマヤは指をぐずぐずしながら小声で言った。"
    show SCG_02 6 with dissolve
    my "キューくんは頭がいいから、学術部とか似合いそう…"
    my "あの…{w}わたしはね、後にでも部署を移せるなら、保健部に入りたいよ。"
    my "わたし、人の世話をするのが好きで…"
    pl "何っ！マヤ、似合うじゃないか！天使みたいだぜ！"
    pl "マヤが保健部所属になったら、俺は毎日リンゴをもって遊びに行くからな～"
    show SCG_02 8 with fastdissolve
    my "うん、ありがとう、[na2]くん。[na2]くんも魔導部で頑張ってね？"
    hide SCG_02 with dissolve
    pl "ま、魔導部な…"
    nar "またさっきの混乱が揺らいでくる。気まずい反応に、マヤの表情がくもってきた。"
    show SCG_03 7 at left
    show SCG_02 5 at right
    with dissolve
    my "あっ…ご、ごめん…"
    pl "いやいや、ちょっと考えていただけ。{w}魔導部…そう、そこは一体何する所なんだ？"
    show SCG_02 0 with fastdissolve
    my "あれだよ…エクソシズムみたいな…"
    pl "え、くそ？"
    my "違うよ…"
    pl "ハッハ、なんてな！"
    my "もう…"
    pl "エクソシストと聖職者が違う存在とは思わなかったな。"
    pl "その、俺らだって、街の外では神父様と呼ばれてるだろ？"
    my "浄化部って、聖職者でも、エクソシストでもないよ、[na2]くん。わたしたちって、ただの…"
    show SCG_03 8 with dissolve
    sc "…ただの掃除人さ。"
    hide SCG_03
    hide SCG_02
    with dissolve
    nar "シーキュレットが何気なく投げてきた言葉に、マヤの肩がぎくりとした。"
    nar "だがそれだけ。それ以上なんの反応もなく、やつは俺が触れた所を自分の手で払いながら廊下を歩いて行った。"
    nar "ただの掃除人と思う程度なら、なんでこんなところで続々と働いているんだろう。"
    nar "もしあの弱々しい主教様が今の話を聞いたら、絶対痛嘆にたえないだろう。"
    nar "一方的に途切れた会話がもたらす気まずい空気の中で、俺とマヤはシーキュレットの後に付いて仕事へ向かった。"
    stop music fadeout 2
    hide screen textbox with dissolve
    nvl clear
    pause 2
    scene bg17 with dissolve
    call place17 from _call_place17
    show screen nvlbox with dissolve
    play music "audio/bgm/dialogue.ogg"
    "\n シーキュレットに付いて歩いて来た道は、今まで見た神殿や民家とかははっきりと違う雰囲気だった。"
    "空気が違うというか、そもそもそこは、普段考えられる「作業場」ではなかった。"
    "木々の間にかかった分厚い霧が目の前を隠し、険しい獣道は足を踏む度に石の角や木の根が引っかかって、何度も転びそうになった。"
    et "シーキュレットは森の中に向かっていた。{w}朝っぱらとは言っても、おかしく思われるほどに雲が低くかかっていた。"
    nvl clear
    "\n 彼の後ろに付いて行く俺たち二人は一寸先も見られずに手足をふらふらと振ってるだけなのに、彼は上手く足場を見つけて前に進んで行った。"
    "こんな所で迷ってしまったら、本当に迷子になるに決まっているため、俺とマヤは約束でもしたように"
    "口を固く閉じて、シーキュレットの腕と肩にくっついて、ようやく進んでいるところだった。"
    et "そうしてる間には、これが人間にできる仕事かよ、という不満に満ちながらも、目の前の男がここを頻繁に出入りしているってことを推測できる。"
    nvl clear
    "\n 人気がなくなってからおよそ２０分以上を歩き、俺たち三人は小さい小屋の前で足を止めた。"
    "小屋周辺の空気は、歩いて来た道よりは澄んでいた。{w}こんな場合に使う表現で合ってるのか知らないが、台風の目と表現するあれと似たような印象だ。"
    et "シーキュレットは懐中から鍵束を出して、それを数えては中から一つを選んでドアを開けた。"
    nvl clear
    "\n 小屋の中は、大分よく管理されているらしい。{w}特に調度品などはなく、色んなサイズの木箱が置かれてるだけで、"
    "せめて濡れた木材がにおわすカビ臭に息が詰まったり、床に押しつぶされた腐った肉片を踏んで滑ることはなかった。"
    "シーキュレットは結構大きいサイズの箱を選び、中身を手探っては重たい金具を持ってきて俺とマヤに一個ずつ差し出した。"
    et "一つは掌よりちょっと長めな短剣、もう一つは銃だ。"
    hide screen nvlbox with dissolve
    show screen textbox with dissolve
    show SCG_03 7 with dissolve
    sc "これ、持って。"
    pl "ここはなんだ？"
    sc "戦闘基地。{w}ここ以外にもいくつかあるよ。"
    pl "作業場に既に倉庫があるのに、なんで戦闘基地なんかが浄化部に要るってんだ？しかも一つじゃないなんて…"
    show SCG_03 8 with fastdissolve
    sc "……それは…ボクにも分からない。"
    pl "ハァ？"
    sc "多分「資格を持つ司祭」にのみ個人的に伝わる内容なんだろうね……{w}ボクはまだその資格を満たせてないから。"
    nar "何かいるんだな。{w}凶器などを差し出されながら戦闘基地って言葉を聞いていると、改めて神殿に就職したことを実感する。"
    pl "じゃあこれはなんで渡すんだ？"
    show SCG_03 0 with fastdissolve
    sc "ここから先はキミたち新入りには危ないからね。{w}元々「掃除」に行く際にはこれくらいは支給されるんだ。"
    pl "頂くがままにありがとうごぜえます～って受け取るには凶悪すぎるだろう。"
    show SCG_03 0 at left
    show SCG_02 idle at right
    with dissolve
    my "わあ…わたし、銃は初めて見た。"
    nar "シーキュレットは話が長引くのが気に入らない様、眉根をひそめては小さくため息をついた。"
    sc "二度は言わないから、集中して聞いて。"
    sc "今からボクたちは、「禍の力場」に入る。"
    pl "禍？"
    my "力場？"
    show SCG_03 9 with fastdissolve
    sc "…キミってさ、いくら州都の外出身とは言え、禍が何なのかも知らないの。"
    pl "…うっ…"
    sc "はあ…"
    hide SCG_02
    hide SCG_03
    with dissolve
    hide screen textbox with dissolve
    nvl clear
    show screen nvlbox with dissolve
    "\n 「禍」。人間の力では対抗できない、絶対的な力。"
    "現代の科学では説明し切れない、怪現象の総称。"
    "―「今からおよそ二千年前、天地がひっくり返る程の大災害があった。」"
    "「禍の後、奇妙な傷痕のようなものを持つ男が現れた。彼は神からのお告げを受け、国を立て直せる程の力と知恵を手に入れた。」"
    et "それは確か、村の大人たちから聞いたことがある内容だった。"
    nvl clear
    "\n シーキュレットは、手では持ってる刃物を手入れしながら、口では話を語り始める。"
    "俺は聞いたことのない話だった。{w}いや、聞いたことのない話じゃなかった。"
    "故郷の人たちは、時々空を仰ぎ、儀式を行った。{w}それは日付は規則的ではなく、いきなりやってきたが、それが近づく頃には"
    "村の大人たちに強制的に連れられて、狭い祭壇の中で、寝ることもできず、染みを数えながら夜を過ごさなければならなかった。"
    et "そして日が昇ると、皆で集まって、昨日まで一緒におしゃべりしていた友達や、いつもおはようと言ってくれた隣のおばさんの葬儀を行った。"
    nvl clear
    "\n 俺だけの話ではない。{w}大人になるまでもその日が何なのか、何のために儀式を行うのかは知らなかったが、"
    "大人たちが上気になって叫んでいた「あの方が来られる！」という言葉だけは、妙に鮮明に覚えていた。"
    "シーキュレットの話は、その事件と似た様相をしていた。"
    et "禍、聖痕…これらは、ただ慣れてない「表現」に過ぎなかった。多分これが州都の常識だろう。"
    hide screen nvlbox with dissolve
    pause 1
    show SCG_03 idle at left
    show SCG_02 idle at right
    with dissolve
    show screen textbox with dissolve
    sc "さっきから視野を妨げるこれが禍の「力場」だよ。{w}もっと簡単に言うと、禍が起こる区域みたいなものなんだ。"
    sc "…いくらキミたちでも、通ってきた道にかかった霧くらいは見えただろう？"
    nar "やっぱり、堂々と人を無視してんな。"
    my "でも、霧はずっと流れていたよ…"
    sc "それは力場も数々の外部要因によって流れ続けるからさ。"
    nar "俺は気に食わない表情で彼をにらみつけた。{w}目が合っても、彼は俺の態度には気にせず話を続ける。"
    show SCG_03 7 with fastdissolve
    sc "キミたち、釣り針の原理は知ってるかい？"
    my "うぅん…{w}針が刺されると、逆方向にあるかえしに引っ掛かって、抜け出せなくなるんだよね？"
    sc "よく知ってるね。{w}針が刺されること自体は大したことないけど、"
    sc "それを抜く時にかえしに引っかかって、肉片が千切り取られる痛みを感じる。"
    sc "禍の原理もそれと同じさ。力場が流れる方向を逆らうと、その分の痛みを感じるんだ。"
    pl "じゃあ、その方向を先に読むと、禍も起こらないんじゃ？"
    sc "理論的には、ね。{w}だから学術部とかで禍の流れを研究し続けてるわけさ。"
    sc "…でもキミたちには無理だから。"
    pl "……"
    sc "軽いめまいと吐き気。キミたちも今まで働きながら感じたことあるだろう？"
    sc "更には全身から血を吹いたり、五感の永久的損失、精神異常、数々の傷害などなど。"
    show SCG_02 at huruhuru
    my "ひいぃ…"
    nar "酷いことを、顔色も変えずによくもまあ言う。"
    sc "まあ、それくらいは普通。"
    sc "「本物」の禍がやってくると、疫病が広がって村ごと全滅したり、地がそのまま腐ってしまう例もよくある。"
    sc "だから神殿はそれに備えてるんだ。"
    my "学術部が研究した禍に、魔導部が立ち向かって、保健部が負傷者をサポートするんだね。"
    show SCG_02 at bounce
    my "キューくんは本当にすごいよ…こんな難しいことを全部知ってるんだ、かっこいいなあ…"
    show SCG_03 8 with fastdissolve
    sc "まぁ…"
    nar "故郷とか、州都の外の地が腐っていたのもそのせいか…{w}俺は低い声で呟いた。"
    nar "州都に旅立つ準備をしていた時、村の爺たちが絶対定められた道から離れてはいけないと、"
    nar "耳に胼胝ができるほどに言い残したことを思い出した。"
    nar "全部理由があったのか。{w}俺、本当にすごくおぞましい旅をしてきたのでは？"
    sc "…ここまでが一般的に知られる内容。これ以外にも禍の形は様々。"
    sc "キミたちは聖痕が二つしかないから、まだそこまで危ない禍と向き合うことはないだろうけど、どうせ知っておくべきことだから。"
    show SCG_03 0 with fastdissolve
    sc "もういいかい？出発するよ。"
    hide SCG_03
    hide SCG_02
    with dissolve
    nar "シーキュレットは俺たち二人にほぼ投げるように金具を渡す。"
    nar "彼の言う通り、そのおぞましい話は、今までの俺たちは実感の湧かない話だった。"
    nar "そんな事故が起こるとしても、それはあくまでも他人事で、直接禍の被害を受けたことは一回もなかったから。"
    nar "マヤは気が抜けた顔で俺と目が合った。彼女も俺と同じことを思ったようだ。"
    nar "そうして俺たち三人は、「戦闘基地」を後にして霧の中に歩み出した。"
    hide screen textbox with dissolve
    pause 1
    scene black with dissolve
    pause 1
    scene bg17 with dissolve
    pause 1
    show SCG_03 idle with dissolve
    show screen textbox with dissolve
    sc "…止まって。"
    my "え？"
    sc "ここからは禍の影響力が及ぶ範囲内だ。"
    sc "ボクがいいと言うまで絶対に振り向かないで。"
    sc "あと、霧の向こうから人の声がしてもそれは全部幻聴だから、反応しないで。"
    pl "反応したらどうなるんだ？"
    sc "知らない。知られてないし。"
    pl "何だそれ～"
    show SCG_03 7 with fastdissolve
    sc "でも今までボクが見てきた人たちは、血を吐いたり、一か月くらい前が見えなくなったりしてた。"
    sc "もしくはそのまま消えては帰って来れなくなったり。"
    sc "そこまで気になるなら、止めはしないけど。"
    pl "……"
    hide SCG_03 with dissolve
    hide screen textbox with dissolve
    nvl clear
    show screen nvlbox with dissolve
    "\n シーキュレットに付いて歩き始めてから随分経ったと思ったのに、霧のせいで時間の経過が感じられなかった。"
    et "そもそも真っすぐ前を見るのさえ辛かった。{w}後ろを向いてはいけないという規則は思ったより厄介で、神経が尖ったせいか微小な感覚にも全身が敏感に反応した。"
    nvl clear
    "\n 今日俺たちがやる仕事は、亡者に連れて行かれた人間の遺品を回収する仕事だと、シーキュレットは言った。"
    "この森は人気がなく、民家と隣り合わせしており、禍の影響を受けない亡者たちはここを通じて夜になると人間を襲うという。"
    "新入りの俺たち二人が退庁した後は、処理班の主要任務がその亡者を狩ることになるらしい。"
    et "こんな霧の中で、しかも日が落ちた後に襲撃されたら、どれだけ力強い人であれ手も足も出せないだろう。{w}納得のいく話だ。 "
    nvl clear
    "\n そして、霧に隠されてるだけで、多分、他の処理班の奴らも自分の位置について仕事をしているらしい。"
    "すぐ横からの気配が、他の処理班が出す音なのか、ただの幻聴なのか、判断がよく立たない。"
    et "マヤが何回か悲鳴を上げながら乾いた木の根の上でふらついたせいで、結果的に俺とマヤは互いの腕を掴み、気を付けて足を運んだ。"
    nvl clear
    "\n 「……」"
    "俺の袖を強く握り、胸の中で震えている小さい少女の存在だけが、霧の中からひときわ目立った。"
    "彼女の吐息が頭の中に響くように大きく聞こえてくる。小さい指の感触がやけに気になる。"
    "産毛のような髪の毛が風に吹かれるのを見ていると、後ろ首がくすぐったい。"
    "こんなところでぼーっとしたら、絶対禍の犠牲になるだろう。{w}そのため俺は何度も視線を他のところに回そうとしたが、薄情にも首の後ろ側から"
    et "慌ただしく鳴り響く脈の音が彼女に聞こえたかのように思われ、何度もマヤの顔色を窺うようにする。{w}顔が熱く、めまいがする。禍の影響かもしれない。"
    hide screen nvlbox with dissolve
    show screen textbox with dissolve
    show SCG_02 8 with dissolve
    my "あの…"
    pl "ど、どうした？！マヤ、どこか具合が悪いのか！？"
    nar "やたら声が裏返った。"
    nar "馬鹿げた俺の声に、つい口を塞ぎたくなったが、彼女は無言で首を横に振ってくれた。"
    show SCG_02 1 with fastdissolve
    my "…[na2]くんがいると、心強いね。"
    nar "深い霧に隠された彼女の表情はよく見えなかったが、こんなにも愛しい生き物が俺と同じ人間だなんて！"
    pl "天使…"
    show SCG_02 0 with fastdissolve
    my "え？"
    pl "神に授かりし可愛さ…"
    show SCG_02 6 with fastdissolve
    show SCG_02 at bounce
    my "何よそれ～…"
    sc "無駄話をしてる暇があるなら地面にも目を配ったらどうだい？"
    nar "予想通り、いい空気に冷や水を浴びさせるのはいつもあいつだ。"
    hide SCG_02 with dissolve
    nar "シーキュレットはいつも通りこちらを振り向かず不愛想に言った。"
    nar "普段なら、気持ち悪い奴だと思ったんだろうけど、状況がこうなるとあいつの癖が理解できなくもなかった。"
    nar "シーキュレットは、歩きが遅いわけでもないのに、"
    nar "よく見えない地面に怪しいものがあったら、すぐ拾って調べてみては袋の中に入れた。"
    nar "中には、人間の指や歯のように見える物もあった。"
    pl "はは、ゴメンゴメンて～"
    pl "探そうとしても、こんな濃い霧の中じゃ立ってるとこもよく見えないんだよ。{w}どうやってそんなにうまく探せるんだ？"
    show SCG_03 7 with dissolve
    sc "…やってる内に上達するよ。"
    pl "袋持つの、手伝おうか？"
    show SCG_03 0 with fastdissolve
    sc "いい。"
    pl "そんなこと言わずにぃ～"
    nar "さっきからできることは、道を迷わないように気を付けて、彼の後ろに付いて行くだけ。"
    nar "俺はあの退屈さに十分疲れてきたので、シーキュレットとの会話を続けたかった。"
    nar "じゃないと、今までの平凡な知識では理解し切れないこの森の中の奇妙な状況に、ひそかに恐怖を感じたせいかもしれない。"
    pl "それより、お前が言った振り向いちゃいけない呪いと…"
    pl "あと霧のせいで前が全然見えないのを除くと特に危ないものはなさそうだけど、刃物はなんでくれたんだよ？"
    show SCG_03 72 with fastdissolve
    sc "それは……"
    nar "都合よく吹いてきた風の音で彼の声が埋もれる。"
    pl "…あ、ゴメン。なんて？"
    show SCG_03 7 with fastdissolve
    sc "…キミ、今日の業務が終わったら州都の言葉でも勉強したらどうだい。"
    pl "さっきは本当に聞こえなかったんだよ～{w}ここ、風が強過ぎねえか？"
    hide SCG_03 with dissolve
    nar "シーキュレットは諦めたかのようにため息をついては、マヤが持っている銃を指した。"
    show SCG_03 idle at left
    show SCG_02 idle at right
    with dissolve
    sc "それは神殿から作られたものさ。"
    sc "亡者が珍しくはない禍の現象とはいえ、普通の方法で容易に始末できる訳じゃないから。"
    sc "一気に首を切らないといけないんだけど…それを、キミたち新入りに期待するには無理があるからね。"
    sc "その銃には呪術が仕掛かっていて、キミたちのように聖痕が二つしかない人でも亡者の足を止めるくらいはできる。"
    sc "まあ、その間に必死に逃げないとならないけどね。"
    show SCG_02 at huruhuru
    my "うう…"
    sc "亡者は夜によく出るというけれど、あれがいつ起きていつから彷徨い始めるのかは誰も知らない。"
    sc "自分の身は自分で守れ、ってことさ。{w}処理すべき死体が増えると、面倒なのはボクらの方だから。"
    show SCG_03 7 with fastdissolve
    sc "…あと刃物は、ただの刃物。"
    nar "さっきからシーキュレットが繰り返す「聖痕二つ」って言葉は、俺のプライドを十分傷つけた。"
    nar "一度気に食わないと思ったら、今日は特段とシーキュレットの説明も長く、鬱陶しく聞こえてくる。"
    nar "さっきから聞こえてくる風の音もやけに気に障る。"
    nar "我慢していた俺がシーキュレットに鬱憤を吐き出そうとするのとほぼ同時に、ありがたくもマヤが口を開いた。"
    nar "結果、俺の不満がシーキュレットの耳に入ることはなかった。"
    my "あの、キューくん。聖痕が多いと、何がいいの？"
    show SCG_02 6 with fastdissolve
    my "あのね、そ、そのぉ…{w}修道院では、聖痕が多いほど神聖力が強い、とだけ言ってて…それが…"
    my "話が出たついでにキューくんに詳しく聞きたくて。"
    sc "……"
    sc "見て。"
    hide SCG_02
    hide SCG_03
    with dissolve
    nar "そう言って、彼は足を止めた。"
    nar "その後、後ろに立っている俺たち二人がよく見れるよう、自分の左側に両腕を運び、"
    nar "片手に持っていた短剣の先が上を向くように立たせ持った。"
    nar "そして他の手をその上に運び、刃を覆うように掌を開く。{w}すぐにでも刺されるような、危ない様子だ。"
    nar "だが彼は、その危なさを自慢するように、開いた掌をひらひらしてみせる。"
    show SCG_03 7 with dissolve
    sc "ボクがこの掌をこのまま振り下ろすと、どうなると思う？"
    pl "や、普通に貫かれて怪我するだろ！アホ、何すんだよ！"
    sc "ただの例えさ。{w}じゃあ、もし振り下ろすのが素手じゃなくて槌だったら？"
    show SCG_03 at left
    show SCG_02 idle at right
    with dissolve
    my "う、うぅん…{w}キューくんが短剣を落とすんじゃないかなあ…"
    show SCG_03 at bounce
    sc "正解。{w}半分ぐらいはね。"
    sc "これが聖痕を持つ者と、持ってない者の違いだよ。"
    sc "禍の方向を逆らっても、比較的被害が軽微だったり、更にはその流れに影響を強く与えられる程、聖痕が更に体に現る。"
    pl "聖痕が多いほど強いんじゃなかったのか？"
    sc "同じ話だけど…因果関係が違うんだ。{w}聖痕が多いほど強いんじゃなくて、強い人にもっと多くの聖痕が刻まれる。"
    pl "うわ、じゃ、今より強くなると聖痕が増えるかもしれないんだな。"
    show SCG_03 0 with fastdissolve
    sc "さあ…{w}未だに聖痕の数が後天的に増えた者は見たことはないけど。"
    nar "シーキュレットは、俺の期待を馬鹿にするように、はっきりと言った後、そっと細目を開けては付け加えた。"
    show SCG_03 8 with fastdissolve
    sc "…歴史的の記録上は、ね。"
    hide SCG_03
    hide SCG_02
    with dissolve
    nar "それで話を終えたのか、続いて前に進む。"
    show bgw onlayer screens
    hide bgw onlayer screens with dissolve
    nar "でも俺はその場に立ち尽くし、動けなくなった。{w}シーキュレットの話が終わるのとほぼ同時に、女の笑い声が聞こえてきたから。"
    nar "背筋が寒くなる。{w}気づけてはならない何かを気づいたように、鳥肌が立った。"
    nar "今までただの風だと思っていた騒音の正体が確実になったのだ。"
    show SCG_02 idle with dissolve
    my "[na2]くん？"
    pl "あ…あ？{w}ゴ、ゴメン。最近本当どうしちまったんだろうな…"
    show SCG_02 zorder 2
    show bg17 as wave_overlay zorder 1 at sha:
        function WaveShader(amp = 0, melt='both', melt_params=(10,1.0,0.1))
    show SCG_02 as wave_overlay2 zorder 9 at sha:
        xalign 0.5
        function WaveShader(amp = 0, melt='both', melt_params=(10,1.0,0.1))
    nar "気を取り直し、俺はマヤを支えながらシーキュレットに付いて行った。"
    nar "これぐらい歩いたら終わりが見えそうなものだが、彼はどんどん深い場所に入って行くように見えた。"
    nar "頭の中に響き始めた女の笑い声は、どんどん大きくなり、脳裏に差し込んできた。"
    nar "くすくす笑う声は次第に大きくなり、息も絶えそうになっては、やがて叫ぶような高笑いとしてどんどん鮮明になってくる。"
    nar "マヤは、周りと俺を交互に見ながら、不安げな視線を周りに散らした。"
    pl "う、ぐぅっ…"
    show SCG_02 at bounce
    my "[na2]くん、大丈夫？"
    hide SCG_02 as wave_overlay2 zorder 9 at sha
    hide SCG_02
    with dissolve
    nar "多くの人々の泣き声が重なるように頭の中で響く。{w}俺は、どんな音が本物で、どんな音が幻聴なのかを区別できなかった。"
    nar "聴けない者は喋れない。丁度今の俺の状況だ。{w}めまいがする頭をついて、呻くことしかできない。"
    nar "人々の叫び声は、各自が言いたいことを叫んでいるようにも聞こえたが、風の音に紛れてほとんど聞き取れなかった。"
    nar "その中で、とりわけはっきりした声が一つ、耳元に鳴った。"
    stop music 
    play sound "audio/se/memory.ogg"
    hide bg17 as wave_overlay zorder 1
    show bgw onlayer screens
    hide bgw onlayer screens with dissolve
    play sound "audio/se/pii.ogg" loop 
    pause 0.1
    stop sound fadeout 6
    nar "「お願い…誰か、助けて！」"
    nar "聞こえた声に目が覚めた。{w}声がなる方に横向いた。この声は幻聴なんかじゃない。{w}客観的根拠はないけど、確実だった。"
    nar "誰かが、霧の向こうで、助けを求めている。"
    nar "この鮮やかで必死な声は、確実に人間の声だ。{w}山道は険しい。{w}今すぐ誰かが助けに行かないと、あの人は…"
    nar "シーキュレットが言った禍の呪いが頭の中で浮かんでくる。"
    show SCG_02 idle with dissolve
    pl "…マヤ。"
    nar "俺はマヤの手を引いてシーキュレットの背中にくっつけた。手を離した時、彼女が転んでしまうのが不安だったからだ。"
    pl "ゴメン。すぐ戻る。"
    show SCG_02 5 with fastdissolve
    play music "audio/bgm/grumble.ogg"
    my "[na2]くん…！？"
    hide SCG_02
    show bgw onlayer screens
    hide bgw onlayer screens with dissolve
    nar "マヤの手を放し、声のなる方に身を回しては、一気に駆け出した。"
    show SCG_02 5 at right
    show SCG_03 5 at left
    with dissolve
    sc "ちょっと、おい、どこに行くんだ！{w}おい！[na]！"
    sc "畜生、そっちは力場が強くなるから危ないって…！"
    show SCG_02 at huruhuru
    my "キュ、キューくん、どうしよう！？"
    show SCG_03 at bounce
    sc "クソッ…！"
    hide SCG_02
    hide SCG_03
    with dissolve
    hide screen textbox with dissolve
    nvl clear
    show screen nvlbox with dissolve
    "\n 俺は運動神経がいい方だった。{w}支えなければならない人がいればともかく、自由に動ける独り身になったら状況が違う。"
    "もしかしたらこの運動神経が、無茶を強行する無謀な勇気を俺に与えたようだ。{w}石の角を蹴って、倒れた木々を踏み台にして、走っていった。"
    "霧が濃くなるほど、泣き叫ぶ声もどんどん鮮明になってくる。{w}頭の中で最悪の状況を描いた。"
    "きっと処理班の誰かが足を滑らせて、山道を転んで、今頃丘とかの下に落ちては孤立されてるんだろう。"
    "運が良くても振る舞いが不自由な状況であるだろうし、禍の呪いを受けたらひどい出血があるかもしれない。"
    et "もしかすると、俺一人じゃ収められない人数の遭難者がいるかもしれない。"
    nvl clear
    "\n だが、こんな心配をしていても何も変わらない。{w}怪我人を見逃すわけにはいかない。まだ生きている、俺の中の正義がそう言っていた。"
    "間に合わないと…！{w}泣き叫ぶ声は、鮮明になり挙句、もう獣が吠える音のように変わっていた。"
    "しばらく走ると、足の先がしびれてくる。木の枝に掠れて皮膚が裂けた気がする。"
    "山道に慣れてなく、同じところをくるくる回っているように感じる。"
    "それでも俺は走るしかなかった。その声がとっても切実に助けを求めていたから。"
    nvl clear
    et "\n 「この辺り…のはずだが…」"
    "足を止めて、息を切らす。{w}泣き声は、すぐ隣から聞こえるように鮮明だ。"
    "周辺をきょろつきながら、用心深く前に進んだ。"
    "「おーい！誰かいるかー！」"
    "返事は戻らない。"
    et "「……」"
    nvl clear
    "\n 小さい音も逃さない様、神経を尖らせた。だけど、何も聞こえなかった。"
    "ふと、禍について戒めるシーキュレットの顔が浮かぶ。"
    "俺は今、本当に禍に化かされてしまったのか？{w}故郷で、夜の間消えてしまった人たちも皆こうなっちゃったのか？"
    et "足の力が抜ける。{w}恐怖より虚脱感が背筋に流れた。"
    nvl clear
    "\n だがそれも長くはなかった。俺が立っている所のすぐ側から、泣き声が危うい沈黙を破ったから。"
    "びっくりして反射的に短剣を取り出した。そっちに向けて慎重に目を配る。音がした所には確かに誰かがいた。"
    "彼こそが、俺に助けを求めた声を出した人に違いない。"
    et "でも慌てずにはいられなかった。{w}「あれ」は、人間ではあったものの、人間と言うには…"
    nvl clear
    show black with slowdissolve
    stop music fadeout 1
    "\n ―{space=-3}―「冒涜的」であった。"
    play music "audio/se/no more bell my buddy.ogg" fadein 5
    "―{space=-3}―見血塊のように見えるあれは、どう見てもまともなところがなかった。{w}掠れて破れた傷が、めった切りでもされたように皮膚の上に刻まれていた。"
    "折れた骨が肉を破って突き出ている。これは丘から転んでできた傷のようだ。"
    "それを考えても、手足が非常に膨らんで青黒い色をしていた。{w}拳より少し大きめの血塊が二つ、顔のように見える部位に纏わりついている。"
    "最初には何なのか分からなかったけど、血塊を包んでいる皮が瞬き、その中にある人間の虹彩と目が合ってから、すぐ総毛が立ってきた。"
    et "それ以外にも、黒い血筋のようなものが全身にはみ出て、脈に合わせてびくびくと動いた。{w}これは、俺が納得できる人間のあり様じゃなかった。"
    nvl clear
    "\n それは、理解できない言葉で絶叫しながら、自分がまき散らした吐瀉物と排泄物の上で勝手に転んでいた。"
    "前を見ることも、何かを聞くこともできない様子だった。"
    "納得がいかない光景の前で、俺は何も言えなかった。{w}深い森の中では、泣き声が聞こえ続ける。"
    "しばらく無言で立っていた俺は、遂にゆっくりと足を動かし、少し前に踏み出した。音がなる奥の方にゆったりと歩いて行った。"
    "今の状況で、恐怖を感じないと言えば嘘であろう。"
    et "見慣れない光景に思考が止まってしまったのかもしれないし、{w}向こうに更にいるはずの「遭難者」を救おうという思考のせいかも知れなかった。"
    nvl clear
    et "\n もしくは、未知への探求心が―{space=-3}―"
    stop music
    show bgw onlayer screens
    scene bg17
    show screen nvlbox
    with None
    hide bgw onlayer screens with dissolve
    "\n「おい！」" with sshake
    hide screen nvlbox with dissolve
    show screen textbox with dissolve
    pl "うわっ！" with sshake
    nar "後ろから引っ手繰る誰かの手によって、俺は投げ飛ばされるように、後ろの方に引き寄せられた。"
    nar "誰の声なのかはもう知っていた。シーキュレットだった。{w}そして、引き寄せられた俺を後ろから支えたのはマヤだった。"
    show SCG_02 idle with dissolve
    my "大丈夫？"
    nar "心配げなマヤの声を聴くと、夢から覚めるように精神がしっかりしてきた。"
    show SCG_03 0 at left
    show SCG_02 idle at right
    with dissolve
    nar "二人は俺に付いて来たのだ。{w}こんなにも嬉しいことか。"
    pl "マヤ！シーキュレット！"
    show SCG_02 3 with fastdissolve
    my "[na2]くん…無事でよかった。"
    my "あの、わたしとキューくんは、きっと[na2]くんが振り向いちゃったから、禍にやられたのかと思って…"
    my "だから怖くなっちゃって…"
    pl "俺のことを心配してここまで来てくれたのか？本当に…{w}本当にありがとう、マヤ。"
    pl "マヤは、俺が今まで見てきた人たちの中で一番優しい女の子なんだな！"
    sc "…運がよかっただけだよ。"
    pl "ちょ、ちょっと待った！{w}森からする音はやっぱ幻聴じゃなかった。ここにさっき人が！"
    show SCG_03 2 with fastdissolve
    sc "一体何がしたかったんだ、キミは。"
    hide SCG_03 0 at left
    hide SCG_02 idle at right
    with dissolve
    play music "audio/bgm/Securett.ogg"
    nar "シーキュレットの声は、湧き上がる感情を必死に抑えるように、低くて不愛想な声だ。"
    nar "彼の表情を見れないのが幸か不幸か分からない。"
    nar "その声がこの空間の空気を更に冷やす。{w}普段の様、いたずらに話を進めたいところだが、それができるような状況ではなかった。"
    nar "マヤも、生まれて初めて見るおぞましい状況に、慌てた顔で目を瞬くだけだ。"
    sc "……"
    nar "シーキュレットは、俺に彼が持っていた袋を投げつけるように渡す。{w}そして俺が見つけたあれに向かって大またに近づく。"
    nar "まるで死体を「剖検」するように、あれをあちこち覆しては、何かを取り出す。{w}粘りつく肉の音が鬼気迫る。"
    nar "シーキュレットが見つけたのは認識票だった。{w}神殿の司祭であることを示す通行証。"
    nar "マヤと俺の首にかけられてるロザリオと同じ物でもあった。"
    nar "シーキュレットはそれを調べながら何かを呟く。"
    nar "それは、誰かの名前だった。認識票に書かれてるのを読んだのだ。"
    show SCG_03 0 at left
    show SCG_02 idle at right
    with dissolve
    my "あの、キューくん…これは…"
    sc "先週失踪した処理班の奴だね。この頃降った雨のおかげで助かったのか…{w}運がいいな。"
    pl "んだと？"
    hide SCG_03 0 at left
    hide SCG_02 idle at right
    with dissolve
    nar "シーキュレットが味も素っ気もなく投げた言葉に、驚愕に耐えられなかった、他にできることはない。"
    nar "彼は気が乗らない顔で目の前の血塊を背負う。" with sshake
    pl "俺が負おうか？"
    show SCG_03 0 with dissolve
    sc "聖痕二つのくせにどうやって力場の中で負傷者を運ぶつもりなんだ。"
    pl "お前さっきから聖痕にすごい執着するな？"
    show SCG_03 2 with fastdissolve
    sc "だから何だよ。{w}急いで。禍が来る前に離脱しないと。"
    nar "シーキュレットは簡単に答えては忙しく足を動かした。{w}奥からはまだ叫び声が聞こえてくる。"
    hide SCG_03 0 with dissolve
    pl "あ？このまま行くって？"
    sc "……"
    pl "幻聴じゃなくて遭難者だっただろ！{w}お前がそう言ったじゃないか、向こうに人がいるって？"
    pl "少しでも助けるなら、なんとか…主教様を連れてきて助けてもらえないのか？{w}お前ら、この声が聞こえないのかよ！"
    sc "……"
    show SCG_03 2 with dissolve
    sc "…うるさいなぁ…"
    pl "何だって？"
    sc "まだ意味が分からないの？ここは完全に呪われた地。{w}生きる人間が足を踏み入れるとすぐさま禍にやられてしまうんだよ。"
    sc "…こいつのように。"
    sc "人間の力で禍に立ち向かうのは不可能だ。"
    sc "…だから幻聴だって言ったのに…"
    pl "それがどうしたってんだよ！こんな霧なんて、どうにか…！"
    show SCG_03 0 with dissolve
    sc "キミは…"
    show SCG_03 2 with fastdissolve
    sc "キミは何も知らない。"
    show SCG_03 at left
    show SCG_02 idle at right
    with dissolve
    my "……"
    show SCG_02 3 with fastdissolve
    my "…喧嘩はやめてよ…"
    hide SCG_02
    hide SCG_03
    with dissolve
    nar "マヤの言葉を最後に、シーキュレットは舌打ちをしてはまた歩き出す。"
    nar "後ろから聞こえてくる泣き声が気になって、何回も振り向きそうになったが、"
    nar "すぐさっき目撃した「禍に呪われた人間」の姿が思い浮かび、二人とも大人しく彼に付いて行った。"
    nar "気まずい帰り道が続く。"
    stop music fadeout 3
    hide screen textbox with dissolve
    pause 2.0
    scene black with dissolve
    pause 2.0
    if hssh_rkn:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03_8
    play music "audio/se/tutorial walking.ogg"
    show screen textbox with dissolve
    nar "神殿の病院は忙しい。{w}俺とマヤはシーキュレットに付いて忙しく動いたが、結果的には二人とも特には役立たなかった。"
    nar "書類の作成から事情聴取まで、すべてを彼一人で処理してしまったから。"
    nar "シーキュレットも、患者を引き継いだ保健部員たちも、こんなことが初めてではない様だった。"
    nar "俺たちは硬い表情で、診療室の外の待機用椅子に座り、彼が戻って俺たち二人に何らかの仕打ちをするのを待った。"
    nar "そんな俺たちの前に、グレーテが立っている。"
    show SCG_14 idle at left
    show SCG_02 idle at right
    with dissolve
    gr "あなたたち、来たのね。{w}物凄く驚いたようだったけど…大丈夫かしら。"
    my "グレーテさん…"
    pl "先生、こんにちは。忙しそうだけど、そっちこそ大丈夫なのか？"
    gr "もちろん。余裕を出せない程度じゃないわよ。{w}治療は急かすからといって早くなるわけじゃないからね。"
    hide SCG_14 idle
    hide SCG_02 idle
    with dissolve
    nar "この状況にもコーヒーを飲んでいる彼女の事を、今日に限って一層大人しく感じる。"
    nar "普段はつまらない冗談ばかり交わしたせいで、俺はグレーテ先生が保健部の補佐教だったってことをなんとなく忘れてしまう。"
    nar "彼女は、俺たち二人が落ち込んでいるのを気づいたみたいだ。"
    show SCG_14 10 with dissolve
    gr "ひどいでしょう？{w}でも、最近は患者が減ってる方なの。"
    gr "わたしたちもなんとか頑張ってはいるけど、禍って、人間の力で何とかできる現象ではないからね。"
    gr "困るわぁ。{w}頑張って、治して、ちゃんと帰しても、また数日で重傷を負って戻ってくるの。"
    gr "治療班としては正直、無力さを感じたりもするわ。"
    pl "あいつ…助かるのか？"
    show SCG_14 3 with fastdissolve
    gr "治癒術をつぎ込めば何とか延命はできるでしょう。{w}でも、その後はわたしたちも確信できないわ。"
    gr "体が不便になると、心も病を負っちゃうの。最悪、体は治っても心は治らない場合だってあるわ。"
    show SCG_14 0 with fastdissolve
    gr "だから、生き延びても、生きていけるかどうかは自分自身にかかってる。"
    show SCG_14 at left
    show SCG_02 idle at right
    with dissolve
    my "…怖い。"
    show SCG_02 7 with fastdissolve
    my "どうして、毎日こんな様を見ながら正気でいられるんですか？"
    nar "マヤは、俺よりもこの状況を深刻に受け入れたようだ。"
    nar "俺の余計な行動で、彼女が酷いのを見てしまったと思えば、少し申し訳ない気がする。"
    show SCG_14 at bounce
    gr "あなたたち、わたしが治癒術師だと思ってる？"
    nar "だが、先生の口から出てきた言葉はこの状況では少し突然だと思われる内容だった。"
    show SCG_14 8 with fastdissolve
    gr "実は違うの。わたしはただの相談役なんだ。{w}聖痕がとてつもなく足りてないからね。"
    show SCG_14 at bounce
    gr "これがね、本当に大変なの。"
    show SCG_14 10 with fastdissolve
    gr "「もう無理です、先生」とか、{w}「いっそ死んだ方がましです」とか、{w}毎日疲れて弱まった子たちと向き合うべきだからね。"
    gr "でも、諦めたことは一回もないわ。"
    show SCG_02 0 with fastdissolve
    my "どうして…"
    show SCG_14 0 with fastdissolve
    gr "どうして神殿の病院でカウンセラーなんかをやっているのか、気になるの？"
    nar "図星だったんだろう。驚いた顔をしたマヤがもたもたと頷く。"
    nar "先生は、そんなマヤが可愛かったのか、笑っては軽くため息をついた。"
    gr "残酷だなあって思うの。{w}家を出たばかりの子供たちに全てを押し付けないといけないってことがね。"
    show SCG_14 10 with fastdissolve
    gr "誰にだって、簡単に受け入れられることではないでしょうから…"
    nar "俯いて言葉を濁す彼女は、俺たちだけじゃなく、"
    nar "自分が今まで経験してきた、他の人々と関わった事件や事故を思い出しているようだ。"
    nar "だが、それもつかの間。{w}落ち込んでく雰囲気をひっくり返すように、彼女はいつものグレーテ先生に戻ってきた。"
    show SCG_14 0 with fastdissolve
    show SCG_14 at bounce
    gr "あなたたちは州都の人々の便宜を計らうために働いているけど、あなたたちのために頑張っている人たちだっているってことよ。"
    gr "あなたたちがもっと元気に耐えていてくれるなら、願ったり叶ったりよ。{w}わたしも、主教様も、そのためにいるんだから。"
    hide SCG_14 idle
    hide SCG_02 idle
    with dissolve
    nar "彼女の視線の先には、疲れている印象の茶色い髪の男の人がいる。"
    nar "彼は、同じく白いガウンを着けた司祭たちの書類を読んだり、忙しく何かを指示したりしていた。"
    nar "何回か見たことがある。彼が多分、保健部の主教であろう。"
    show SCG_14 1 with dissolve
    gr "外部に味方がいると思うと、心の中の重みが減るでしょう？"
    hide SCG_14 with dissolve
    nar "俺は、素早くいい雰囲気を作って会話を終えられるのが彼女のすごい所だと思うが、"
    nar "どうやらマヤは考えが違うのか、まだ言い残しがあるかのように気まずい顔をしている。"
    nar "だが、結果的にマヤが先生と会話を続けることはなかった。"
    nar "向こうから用を済ませたシーキュレットが、何故だか濡れた前髪を振りながら歩いて来たから。"
    show SCG_14 idle with dissolve
    gr "そうね、では今日も互いに愛し合いますように。"
    hide SCG_14 with dissolve
    nar "グレーテ先生も彼を見つけては、俺たちに手を振ってさっき見た主教様のもとに歩いて行った。"
    show SCG_02 idle at right
    show SCG_03 idle at left
    with dissolve
    pl "おかえり。お疲れ様。"
    my "キューくん…どうしたの？そんなに濡れて。"
    sc "……"
    sc "書類。"
    my "え？{w}あ…ここ…"
    nar "濡れた髪の毛を陰険に垂らしたシーキュレットは、奪うように俺らの分のファイルを握って、"
    nar "頭の中から何かを計算し始めたかのようにぶつぶつと書類を読み下した。"
    show SCG_02 8 with fastdissolve
    my "……"
    nar "マヤがまた気まずい空気の中でシーキュレットの顔色を伺っていた。{w}今朝何度も彼女に助けられたから、今度は俺の番だ。"
    pl "途中で中断になっちゃったな、今からどうする？"
    show SCG_03 2 with fastdissolve
    nar "それを聞いたシーキュレットの目が鋭すぎて、つい体をすくめるところだった。"
    show SCG_03 0 with fastdissolve
    sc "浄化部の仕事は、一度途切れたら途中参加は難しい。"
    sc "主教様に言っておくから、キミたちはもう早めに上がって、倉庫を片付けておいで。"
    pl "一人で三人分の仕事をやるってことか？"
    sc "キミたちを連れて動くよりは、一人で行動する方が早く収まるからね。"
    pl "でも、倉庫の片付けは後にでも…"
    show SCG_03 2 with fastdissolve
    sc "いい？倉庫の片付けをするんだ。{w}もう二度は言わないよ。{w}キミの独断でこれ以上主教様を困らせるんじゃない。"
    hide SCG_02
    hide SCG_03
    with dissolve
    nar "大またに近づいたシーキュレットは、俺の胸の真ん中に人差し指を指してはっきりと告げる。"
    nar "しばらくひりひりした感覚がそこに残る。"
    show SCG_03 2 with dissolve
    sc "…聖痕二つの分際で、魔導に偏愛されるからって傲慢になるなよ。"
    hide SCG_03 with dissolve
    nar "そう言い放った彼は、作業場の方に戻る。"
    nar "あきれちゃった俺は、遠さがる彼の後ろ姿に投げつける悪口さえ思い出せなかった。"
    nar "聖痕二つ？"
    nar "今日、一体何回その言葉を聞いたんだろう！"
    nar "あいつは、あいつの聖痕も一個を剥ぎ取ると二つになるってことを忘れているのか？"
    nar "あいつに無視された記憶が次々と頭の中に浮かび上がり、雪だるまを作るように怒りが増していく。"
    nar "そうやってシーキュレットの言葉を振り返る中、ふと何かの記憶が思い浮かぶ。"
    stop music
    play sound "audio/se/memory.ogg"
    scene black
    show bgw onlayer screens
    hide bgw onlayer screens with dissolve
    pl "じゃあ、その方向を先に読むと、禍も起こらないんじゃ？"
    sc "理論的には、ね。だから学術部とかで禍の流れを研究し続けてるわけさ。"
    play sound "audio/se/ding.ogg"
    if hssh_rkn:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    show bgw onlayer screens
    hide bgw onlayer screens with dissolve
    play music "audio/bgm/daily.ogg" fadein 2
    nar "そうだ、学術部。{w}学術部って、何回か聞いたことはあるものの、正確には何をするところなんだ？"
    nar "何回か遊びに行った図書館が学術部の所有だってことは分かっていたが、それだけ。他に情報を聞いた記憶はない。"
    nar "シーキュレットのヤツ、人を無視しやがって。{w}お前が想像もできない可能性ってやつを見せてやろうじゃねえか。"
    nar "聖痕二つ？{w}自慢？{w}本当に自慢してる方は誰なんだよ。"
    nar "俺があいつも知らない知識を並べると、二度とあいつが調子に乗って並べる長い説明を黙って聞いている必要はなくなろう。"
    nar "不意を食らって鼻がへし折られたあいつの顔を想像すると、少し心が浮かされる。"
    pl "マヤ、図書館に一緒に行ってくれるか？"
    show SCG_02 idle with dissolve
    my "え？"
    pl "アイツが仕事中に言ったろう？俺たちに勉強が必要だってさ。"
    pl "じゃあ、あの学術部の研究記録をこっそり見て、禍というやつを調べたら、これからの作業にも役立つんじゃねえかなって思って。"
    show SCG_02 8 with fastdissolve
    my "確かに…{w}わたしが勉強したら、今日のみたくキューくんに迷惑かけることもなくなるのかな…"
    pl "マヤは迷惑なんかかけてない！あいつが過敏なんだって。"
    show SCG_02 0 with fastdissolve
    my "でも[na2]くん、倉庫の片付けはどうするの？"
    pl "そんなの、適当に…"
    nar "倉庫の片付けみたいな雑用は、故郷でもよくやってたので、こっそり抜ける方法とか、後回しする方法などをよく知っている。"
    nar "実は、前からこんなことが起きるとそんな風に状況を免れるつもりだった。"
    nar "でもまいったことに、彼が言い残した言葉が気にかかる。"
    nar "こんな時に限って主教様の話を出しやがるなんて。{w}緻密なヤツめ。猫だと思っていたが、これじゃまるでネズミだ。"
    nar "問題はそれだけじゃなかった。{w}マヤが話を途中に止めた俺を、疑う目で見ていたから。"
    nar "そして、彼女の前でこんな話をしたら、彼女は俺の品行を不良だと思うだろう。"
    hide SCG_02 with dissolve
    nar "結局俺は、獣臭い悪臭が残っている倉庫に向かうしかなかった。"
    stop music fadeout 3
    hide screen textbox with dissolve
    pause 1
    scene black with dissolve
    pause 1 
    play sound "audio/se/luggage down.ogg"
    pause 2.0
    scene bg00 with dissolve
    pause 1.0
    scene bg104 with dissolve
    call place104 from _call_place104
    show screen textbox with dissolve
    play music "audio/bgm/Biblioteca.ogg"
    nar "図書館は静かで、依然人の気配を感じない。鼻に慣れた花の甘い香りが嗅覚を刺してきた。"
    nar "それは最初にここに来た時と同じ香りで、その時よりは大分弱まって、障りなく俺とマヤの心を静めた。"
    show SCG_02 idle with dissolve
    my "いい香りがするね…"
    pl "花を香料にしてるんだって。確か…{w}そう、アイリス！"
    show SCG_02 1 with fastdissolve
    my "へえ…"
    nar "マヤは、稀に目を輝かした。{w}どうやら彼女は花が大好きで、花に関わる話題が出ると、こんな風に興味を示すんだった。"
    nar "俺はその姿を愛しく思いながら頭を回した。この空間の寂寞感を少しでも埋め尽くすためだった。"
    pl "そうだ、俺、前にここに遊びに来て、司書のお姉さんから香水をもらったんだ。{w}それ、マヤにやるよ！"
    show SCG_02 0 with fastdissolve
    my "え、香水を…？どうしてそんな…？"
    pl "それがさ…変な話だけど、俺もよく分からないんだよな。なんとなく、って感じで…"
    stop music 
    ex7 "お探しの本は御座いますでしょうか。" with sshake
    show SCG_02 5 with fastdissolve
    nar "二人で足音を忍ばして、こそこそ本棚の間を歩いていると、いきなり後ろから無機質な声が話をかけてきた。"
    nar "それは、話をかけるという表現が恥ずかしいほど、"
    nar "録音された音声をラジオなどの絡繰りで再生したように、平易で感情が感じられない語調だった。"
    nar "おかげで、マヤの鋭い悲鳴がもっと人情味があるように聞こえる。"
    nar "多分、普段立ち入りしていた時間帯と違って、早朝だったせいでまだ監視があるらしい。"
    nar "浄化部と学術部の業務環境が似ていると思ったのがとんでもないミスだった。"
    play music "audio/bgm/dialogue.ogg" fadein 2
    ex8 "お待ちください。{w}その服装は浄化部所属の者ではありませんか。"
    ex9 "ここは歴史と発展の知恵を保管する場所。{w}誰しもが入れる場所ではありません。"
    show SCG_02 0 at shaking with fastdissolve
    my "ちょ…ちょっとだけ見回すのも駄目でしょうか…"
    pl "俺、ここの司書のお姉さんと知り合いなんだけど、それでもだめか？"
    ex8 "それはあり得ません。"
    ex9 "そして、ここに司書として働いている職員は存在しません。"
    nar "ここまで来て、人を所属で差別するなんて。"
    nar "ここの連中は全員、州都の階級政治に脳が漬けられたのか？{w}クソ野郎共め。"
    ex8 "自分の限界を知り、諦めるべきです。"
    stop music fadeout 3
    nar "心の中で静かに牙を研いでいた刹那、頭の中にエルジェーベト主教の姿が思い浮かぶ。"
    nar "魔導部の偏愛を受ける者。{w}そのあだ名が俺になんの価値を与えてくれるのか、試してみる価値は十分だった。"
    nar "相手は二名。{w}俺は、彼らの様子を伺っては、声を繕って深呼吸をした。"
    play sound "audio/se/hit.ogg"
    pl "{size=46}貴様らー！{/size}" with sshake
    show SCG_02 at bounce
    my "[na2]くん！？"
    play music "audio/bgm/anyway high person.ogg"
    hide SCG_02 with dissolve
    pl "黒曜石のように輝く髪の深き色が貴様ら微物には見えないのか！{w}俺様は処理班なんぞ知らぬ！"
    pl "{size=46}俺は、魔導の身を持ちアルタナータを補佐する者なのだぞ！{/size}"
    pl "魔導の恵みで平和と安寧を受けたもってきたお前ら雑種どもが、魔導の血を見知らず無礼を犯す様が嘆かわしくてたまらんな！"
    pl "今ここで貴様らの汚い手足で塞いだ道を開き、"
    pl "この女の立ち入りを許容するのであらば今回は寛大なる心で見逃してやろうではないか。"
    pl "どうする？学術部の名にふさわしい賢明な判断を期待するぞ。{w}{size=46}ハッ！ハッ！ハー！{/size}"
    nar "素晴らしい演技は光を放つものだ。{w}学術部の司祭二人は、互いを見つめ合って、静かに退く。"
    nar "今度だけは、魔導部のタヌキじじいがありがたい。"
    show SCG_02 idle with dissolve
    show SCG_02
    my "[na2]くん…"
    pl "わあ…マヤ…{w}俺、俳優になるべきだったかも。"
    stop music fadeout 3
    my "今後はこういうのやめてね…"
    hide SCG_02 with dissolve
    hide screen textbox with dissolve
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene bg104 with dissolve
    pause 1
    show screen textbox with dissolve
    play music "audio/bgm/Biblioteca.ogg"
    nar "俺たちは、しばらくの間図書館を探りながら、禍と聖痕に関する本をできるだけ集めこんだ。"
    nar "時々他の司祭からの視線を感じたが、二度と俺たちの前に姿を現しはしなかった。"
    nar "監視されると考えるとばつが悪いけど、直接邪魔が入るわけでもないので、俺とマヤは何も言えずに読書に集中した。"
    nar "直接調べてみると、聖痕と神聖力の関係は、俺が知ってたよりも複雑なものであった。"
    nar "丁寧な説明がない分、俺は同じく本を読んでいたマヤに何回か気まずい視線を送った。"
    nar "そしたら彼女は、俺の視線に気づき、読んでいた本を控えめに置いといては、俺の横に身を傾けてくるのだ。"
    show SCG_02 0 with dissolve
    my "神聖力は生まれた時から決まっていて、聖痕が個人の神聖力と比例するわけではないんだって。"
    pl "へえー…じゃ、そんな場合は自分の神聖力をどう測ればいいんだ？"
    my "うぅん…聖痕三つから悪霊とか禍を見れるっていうのが普通だけど…"
    my "実は聖痕を二つ持っている人だって、見える人には見えるんだって。"
    pl "おお！じゃあ、神聖力を鍛えると、俺たちだって禍を見れるようになるのか？"
    show SCG_02 8 with fastdissolve
    my "それはまた違う問題らしいよ…"
    my "さっきキューくんが、聖痕の数は後天的に変わらないと言ったのと関係あるのかは知らないけど、"
    my "後天的に幽霊とかを見たっていう事例もまだないらしいんだ。"
    pl "なぁんだ…{w}神聖力って特訓とか、何かの祈り…そんなもんで増やせるんじゃないのかよ？"
    my "そう信じる人も時々いるらしいけど、さあ…"
    nar "じゃあ、あの時魔導部の主教が言った「神聖力を鍛える」って、一体何だったんだろう？"
    nar "まるで俺の神聖力がもっと増えるって確信するような口振りだったが…"
    nar "もしあの男が知識を拒んで信仰を優先する古臭い考え方て空頼みをしているのあれば、それこそ最悪だろう。"
    nar "新たに種付けられた不安は、俺の中でどんどん深刻な色に染まってゆく。"
    pl "でもまさか…そこまでアホじゃないだろう。"
    show SCG_02 0 with fastdissolve
    my "うん？"
    pl "いやいや、ただの独り言。{w}ここの絵は何だ？"
    my "え…[na2]くん、本当に知らないの…？"
    show SCG_02 8 with fastdissolve
    my "…これは神様だよ。{w}混沌の元にあった宇宙を創り上げ、人類を立て直したとされる偉大なる我が主。それを描いた肖像画なの。"
    pl "神様…？"
    my "……"
    pl "…あ、そう、それはもちろん知ってる！"
    pl "俺は、その隣の絵のことを言ったんだって。も～マヤったら。"
    hide SCG_02 with dissolve
    nar "禍とか亡者のことを示す言葉が違ってることに気づいてからまさかと思ったら、"
    nar "やはりうちの故郷で見た神様の肖像画とは違う姿をしている。"
    nar "文化から勉強し直さないとならないのか。本棚にぎっしり並んだ本の数ほど、目の前が眩むような気がする。"
    stop music
    play sound "audio/se/hit.ogg"
    nar "突然、何の気配もなく後頭部に衝撃が走る。" with sshake
    nar "何か硬いもので殴られたような衝撃。俺は手に持っていた本を落とし、急いで周りを見回す。"
    nar "学術部の司祭だ。{w}特に探すまでもなく、あいつらはいつの間にか堂々と俺らを取り込んで立っていた。"
    show SCG_02 5 with dissolve
    my "ひぃ…！"
    play music "audio/bgm/youre in danger.ogg"
    nar "慌ててる暇もなく、二人くらいの手が同時に俺の襟首を捕まえる。"
    nar "目の前では、他の司祭一人がマヤに近づき、彼女の肩を掴む。"
    nar "さっきは二人しかなかったのに…！"
    show SCG_02 at huruhuru
    pl "おい！テメェ！マヤに何するんだ！"
    hide SCG_02 with dissolve
    nar "俺は少しでも早くこの場を逃れるために手足をひっかき回したが、彼らの力は俺が反抗する度に強くなり、俺を連行して行った。"
    hide screen textbox with dissolve
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene bg104_ns with dissolve:
        xzoom -1
    call place00 from _call_place00_1
    show screen textbox with dissolve
    nar "神殿に来た以来、自分たち同士の話を、聞こえもしない小さい声でつぶやく輩に慣れたと思ったが、"
    nar "その考えを全部取り消したい。"
    nar "俺の前でひっそりと耳打ちを交わす奴らの会話は、俺が理解できる知識の領域を超えた何かだった。"
    nar "黒いローブを被った彼らは、暗い部屋の中では年齢と性別さえ見当がつかない。"
    nar "そんな輩が一斉に俺の周りをうろつきながら口を動かしている。"
    nar "椅子に縛り付けられた手足は、動かすほどに痛く引き締まって、俺を一層焦らせる。"
    nar "また、この部屋に満ちている面妖な匂い。{w}どうやら至る所に香が焚かれているようだ。"
    nar "この香りが頭の中を空け続けるような気がして、少し油断しただけで気が遠くなる。"
    nar "俺は頭を強く振り、精神を保つために頑張った。"
    play sound "audio/se/hit.ogg"
    pl "貴様、天を慄くことを知らぬ者め…俺が誰だと思ってこんな真似を！" with sshake
    ex8 "存じております。あなたは浄化部の[na]様ではありませんか。"
    pl "何…"
    ex8 "神殿の噂は早いですからね。"
    ex8 "ちなみに、魔導部所属の人々は、自分の血統を自慢する時、左側の口角の上に僅かな皺が発生します。"
    ex8 "学術部の司祭は、皆探求と観察を毎日繰り返す者。あなたは、私たちを騙すにはとても演技が生半可です。"
    pl "うるっせ！" with sshake
    pl "っていうことは、お前ら…{w}最初からこんなつもりで！" with sshake
    ex8 "州都の外から来た外部の人間…{w}あなたに興味があるのです。"
    ex9 "同意。"
    ex10 "同意。"
    ex10 "我らの新たな実験の標本となり、新たな知識の土台として、神殿の糧になる栄光を与えましょう。"
    ex9 "同意。"
    ex10 "同意。"
    ex11 "同意。"
    nar "こいつら、どうやってどんどん増えてんだ？ "
    scene black with dissolve
    nar "腹部を覆っていた息苦しい布が覆され、はだかった素肌に冷たく滑らかなペンさきが走る。"
    nar "腹の上にインクが滲み、へそのすぐ横、その空いてるところにバツが描かれる。"
    nar "腹の底が竦むような感覚に囚われ、こめかみの中ではどんどんと血が流れる感覚が感じられる。"
    nar "目の前に銀色の鋭い光が差した時は上がる悲鳴を何とか堪えた。"
    nar "しかし何度現実から目を逸らしても、それが刃物だってことは嫌でも分かる。"
    nar "俺の様は、間違いなく実験体に縛られた蛙だ。"
    ex8 "新たな知識の地平が広がります。"
    ex9 "愉悦。愉悦とは全くこのような現象です。"
    ex10 "愉悦。愉悦。"
    ex11 "ハ。ハ。ハ。ハ。"
    nar "冷たい刃が直接素肌に当たると、ふと目が覚める。"
    extend "堪えた悲鳴を必死に張り上げても、誰も躊躇しない。" with sshake
    nar "俺を取り込んだ真っ黒な影たちは俺の視野を眩かせる。再び足に力を入れ、空を蹴り散らした。"
    nar "俺がこんな状況なら、マヤは一体どうなってるんだ！"
    scene black with sshake
    stop music
    play sound "audio/se/memory.ogg"
    scene bgw
    show bgw onlayer screens
    hide bgw onlayer screens with dissolve
    nar "椅子ごと倒れた体を何とか構えて扉の方に這おうとすると、扉が開く音とともに暗い部屋に光が差してくる。"
    nar "扉を開けて入ってきた人物は、驚くべし、俺も知っている顔だった。"
    hide screen textbox with dissolve
    scene bg104 with dissolve
    show screen textbox with dissolve
    ex8 "あぁ…ああ…"
    ex9 "イヴリン様だ…"
    ex10 "おお…イヴリン様…"
    ex11 "あああ…"
    show SCG_10 0 with dissolve
    ev_q "あらあら、これまた…"
    nar "周りを見回しながら作り眼をしていた女性は、ゆっくりと近づき、まだ床に座り込んでる俺と目を合わせる。"
    show SCG_10 2 with fastdissolve
    ev_q "御機嫌よう、物見高いお客様。{w}健気な初夏の風が、また貴方との出会いを周旋してくれましたね。"
    pl "こんにちは、怖い姉さん。まんまと俺を騙したな。"
    show SCG_10 1 with fastdissolve
    ev_q "ふふふ…私は決して嘘は言ってません。{w}でも、そうですね…自己紹介をしないと…"
    show SCG_10 0 with fastdissolve
    play music "audio/bgm/Biblioteca.ogg"
    ev "学術部の主教、{color=#b4a7d6}イヴリン・ビオレッタ{/color}が御目に掛かります。ようこそ、私の自慢の空間へ…"
    nar "彼女が軽くお辞儀をすると、周りの司祭たちは何らかの状況を把握したのか、俺の捕縛を解いてくれた。"
    nar "そして何かを詰る間もなく闇の中に身を隠しては、目の前から消える。"
    nar "今まで俺が図書館で感じた奇妙な気配には、こんな秘密が隠されていたのか。{w}怖いな。"
    pl "このまま解剖されるかと思った…{w}畜生…何が一体どうなってるんだ？アイツら…"
    ev "私の信者たちが少々迷惑をお掛けした様ですね。"
    show SCG_10 2 with fastdissolve
    ev "ですが、どうかご理解を。{w}彼らは、ただ限りなく無垢なだけですから。"
    ev "闇の中に溶け込み、湧き上がる探求心に目を煌めかせる姿を見ると、"
    ev "私は、まるで広大な夜空の下に置かれた様、恍惚境を感じるのです。"
    pl "夜空というよりは、穴の中から獲物を狙う獣の様だったがな…"
    pl "マヤはどこだ？"
    ev "ああ…あの小さなお嬢様のことですか。"
    show SCG_10 1 with fastdissolve
    ev "愛しき指をお持ちになった方でした…"
    pl "マヤをどうしたんだ！？" with sshake
    show SCG_10 3 with fastdissolve
    ev "嫌ですわ、よく窘めてから帰らせましたよ。"
    show SCG_10 0 with fastdissolve
    ev "それで、どのような御用で此処に？"
    pl "あの、それが…"
    pl "…本を借りれるかなと思って。"
    ev "本ですか。"
    pl "前は入らせてくれたから…浄化部所属が入れないようになってるとは思わなかったんだ。"
    show SCG_10 4 with fastdissolve
    ev "ふうん…"
    show SCG_10 1 with fastdissolve
    ev "それは…確かに私の不覚ですね。{w}良いでしょう。私が許します…"
    pl "え、本当か！？"
    nar "俺の答えと同時に、暗い影を垂らして口角が細く曲がる。"
    nar "この人は不思議だ。{w}言うことは優しいし、どう見ても優雅な人であるが、なんだかヒヤリとした所がある。"
    show SCG_10 2 with fastdissolve
    ev "ええ、それは勿論…{w}貴方は魔導部の貴賓ですもの。"
    ev "どうぞ徐ろに、果て無い知識を貪って下さいませ…"
    nar "学術部の主教様、そのまま振り向いて歩いては、敷居でしばし立ち止まる。{w}向こうに誰かがいるのだろう。"
    ev "ではラヴィ、私の代わりに案内を頼みます。"
    qus "はい。"
    hide SCG_10 with dissolve
    nar "案の定、彼女が扉を超えると同時に、短い返事と共に扉の奥に入ってきた者がいた。{w}だが、その姿は確実に見慣れた姿だ。"
    pl "ローズ？"
    show SCG_11 5 with dissolve
    nar "俺は慣れている彼女の名前を呼んだ。{w}そしたら、目の前の人物は目を見開いて俺を見つめる。"
    show SCG_11 4 with fastdissolve
    nar "暗い部屋に完全に光が満ちて、いつの間にか驚きを落ち着かせたその顔に穏やかな笑顔が浮かぶ。{w}初めて見る表情だ。"
    show SCG_11 at bounce
    rv_q "驚きました。その名前で呼ぶ人はほとんどいませんので。"
    rv_q "改めてご挨拶します。{w}浄化部の[na]お坊ちゃま。"
    rv "ふつつかな者ながら、学術部の補佐教を担っている{color=#ead1dc}ラヴィアン{/color}と申します。{w}ローズはボクの苗字です。"
    pl "あ、あの時とは全然人柄が違うだろう！"
    pl "まさかお前も記憶がないと言い逃れる気ではなかろうな？"
    show SCG_11 at bounce
    rv "混乱してる様ですね。無理でもありません。"
    rv "実際にボクと接触した168人の反応を統計にした結果、約31.6％の人がボクの「独特な」生態に興味を示し、16.6％の人が…"
    pl "独特って、一体何がどうなって…"
    rv "詳しく説明して欲しいですか？"
    pl "簡単な説明が欲しい。"
    rv "結論だけを申しますと、ボクは禍の被災者なんです。"
    pl "もっと詳しく？"
    rv "禍は、時々人の内面に大きい影響を及ぼします。"
    rv "ボクの場合、外部感染や外傷の危険はありませんが、ごく不規則な確率でレム睡眠状態に入ります。"
    rv "その間、普段とは違う異常行動をするのです。"
    rv "的確な要因につきましてはまだ研究中ですが、今まで分かった内容によると、脳の障害によるものではなく"
    rv "中枢神経系の活性により…"
    pl "もっと簡単に？"
    show SCG_11 1 with fastdissolve
    rv "きまぐれの夢遊病でちゅ。"
    pl "ああ、なるへそ！"
    rv "役に立てて何よりです。"
    pl "お前って、学術部の補佐教としてはなかなか感性が足りないな。"
    show SCG_11 0 with fastdissolve
    rv "学術部には文章を書いたり読んだりする素敵な方々が沢山いますが、"
    rv "ボクは残念ながら主に機械の手入れをしているつまらない者ですので。"
    pl "機械って…絡繰りのことか？印字機とか、無電機とか？"
    show SCG_11 1 with fastdissolve
    rv "それと、浄化部にある機械も学術部の作品です。{w}全ての部署は、協力しながら仕事をするのですよ。"
    pl "ふうん…"
    nar "それはともかく、そう。禍の影響ってことか…"
    nar "その時、俺の脳裏に浮かんだ人が一人いた。{w}まるで別人になったかのように二重的行動を現す異常現象。それが事実であれば…"
    pl "だから、浄化部の主教様と似たような状態なのか？"
    show SCG_11 at bounce
    rv "そうとも言えますね。"
    pl "お前もその間の記憶はないのか？"
    show SCG_11 4 with fastdissolve
    rv "ほぼそうと言えますが、今度だけは特別です。"
    show SCG_11 1 with fastdissolve
    rv "[na]お坊ちゃまとの出会いは覚えていましたので。"
    pl "え、それってどういう意味？"
    rv "ボクにとって、[na]お坊ちゃまとの出会いは特別だったって意味でちゅねえ。"
    nar "おおっと、探り出そうとしたが、逆に不意打ちされた。"
    nar "固いことしか言えないように見えたのに、いきなり恥ずかしいことを言いやがる。"
    nar "でも、そう感じたのは俺だけだったのか、相手は相変わらずニコニコ笑っている。"
    nar "そのせいで内膜を把握できず、更に恥ずかしくなる。"
    show SCG_11 0 with fastdissolve
    rv "よかったら、ボクの願いを聞き入れていただけますでしょうか。"
    pl "お願い？"
    rv "その独特な状態のボクは、今のボクとは別人なような者ですが、さっき言った通り、人格が存在しない状態ではないのです。"
    rv "気が向いたならば、どうか彼女にも優しくしてあげてください。"
    show SCG_11 4 with fastdissolve
    rv "そして、その心が通じたことを感じた時、ボクはお坊ちゃまにもう一度お願いを頼むことになります。"
    pl "礼儀正しい振りをしながら、随分と図々しいことを言うな。"
    show SCG_11 at bounce
    rv "よく聞きまちゅ。"
    pl "じゃあ、俺もちょっと図々しく振舞おうか。{w}俺が借りていく魔導書を薦めてくれないか？"
    show SCG_11 1 with fastdissolve
    rv "魔導書ですか？もちろんです。{w}イヴリン様の許可もありましたので、いくらでもボクの知識をお貸ししましょう。"
    rv "特に探している呪術がありますか？"
    pl "何と言うか、完全な白紙状態の素人でも使えるほど簡単で、俺を勝利に導いてくれる…"
    show SCG_11 4 with fastdissolve
    rv "東大陸語は読めますか？"
    pl "そんな遠くからは来てないよ。"
    rv "これは流石に難しい依頼ですね。"
    pl "じゃあ、ちょっとだけ強くなるくらいで。"
    show SCG_11 at bounce
    rv "ございます。"
    pl "ござるんだ。"
    rv "じゃあ、貸し出し期限は一か月。{w}延滞金は体で払ってもらいます。"
    pl "じょ…冗談だよな？"
    show SCG_11 1 with fastdissolve
    rv "再来を心からお待ちしております、[na]お坊ちゃま。"
    hide SCG_11 with dissolve
    nar "ラヴィアンの丁寧な見送りと共に出てくる最中、図書館は驚くほどに静かだった。"
    nar "さっきの騒がしさが一時の悪夢のように感じられる。"
    nar "図書館に出入りすることに対する忠告を皮膚で直接感じた時間だった。"
    nar "魔導書はやはり、今すぐは理解しにくい内容でぎっしり埋まっている。今は一応閉じておくことにする。"
    nar "全てがうまく行き過ぎて、残ったのは時間だけだ。"
    nar "神殿を歩きながら、事故のことを考える。{w}その中でも、今日一日俺を一番刺激したことは…"
    hide screen textbox with dissolve
    call meet_girl from _call_meet_girl
    menu:
        "未知の真実への好奇心":

            show screen textbox with dissolve
            $ meet_hk = True
            $ meet_rs = True
            nar "今日新しく習得した知識をじっくりと考えてみる。{w}その中でも一番気になるのは、やはり正体不明な彼らのことだ。"
            nar "果たして、禍は本当にあれと関わっているのか、真偽を確かめる必要がある。"
            nvl clear
        "無力感による劣等感":

            show screen textbox with dissolve
            $ meet_gr = True
            $ meet_ar = True
            nar "やるべきだった仕事をやれなくなったことにこんな感情を感じたのは初めてだ。"
            nar "今日起きた事件で、俺の扱いはもう否定できないほどに荷物そのものだった。"
            nar "こんなことは一人悩んでも深刻になるだけ。{w}優しく義理堅い誰かと相談する必要があるのではないか。"
            nvl clear
    stop music fadeout 2
    hide screen textbox with dissolve

    if hssh_rkn == True:
        $ save_name = "day 4, 昼, 楽園"
    else:
        $ save_name = "day 4, 昼"
    jump placemenu
    return




label day4_night:
    if hssh_rkn == True:
        $ save_name = "day 4, 夜, 楽園"
    else:
        $ save_name = "day 4, 夜"
    pause 1
    nvl clear
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg03_1 with dissolve
    else:
        scene bg03_1 with dissolve
    stop music fadeout 3
    call place03 from _call_place03_10
    pause 1
    show screen textbox with dissolve
    play music "audio/bgm/dialogue.ogg" fadein 2
    nar "普段なら通う人々が見える時間帯なのに、今日は珍しく寮の前が空っぽだ。"
    nar "代わりに神殿の方がまだ騒がしい。また俺が知らないイベントでも起こるのか。"
    nar "空いてる寮の近くで真っ白いシルエットが通り過ぎる。"
    nar "見間違えたのかと思ってとっさに鳥肌が立ったが、すぐ慣れた声が聞こえてくる。{w}曲がり角に立っている彼女は何かを呟いている。"
    show SCG_05 8 with dissolve
    hk "悔悟、悔悟…"
    pl "なんでそんな禍々しいことを言いながら歩いてるんだ？"
    show SCG_05 0 with fastdissolve
    hk "ああ、その姿、その声…{w}[na]兄弟ではありませんかぁ。{w}「悔悟」はまがまがしくありませんよぉ。"
    pl "いや、だから…{w}主教様みたいな人がそんなにゆらゆらと歩き回ってるとまるで幽霊みたいなんだよ。"
    hk "幽霊は、ゆらあ～♪ゆらあ～♪と動くのですかぁ～？"
    pl "それは…"
    show SCG_05 1 with fastdissolve
    hk "兄弟から見ると、優雅なのでしたか～？"
    pl "うん？"
    show SCG_05 9 with fastdissolve
    hk "やっぱり…おかしいですかぁ～？"
    pl "ちょっと待って。また話が変な方向に流れてるんだろう。"
    pl "そんな風に主教様の頭の中で話が流れていくと付いていけないんだって。"
    show SCG_05 4 with fastdissolve
    hk "はら～ひら～ほろ～♪"
    pl "もう……まあいっか。{w}はれぇ～"
    show SCG_05 0 with fastdissolve
    hk "幽霊、見たことありますかぁ？"
    pl "別に見たくもないさ。死んだ人の事情まで知るには忙しいんで。"
    show SCG_05 1 with fastdissolve
    hk "死人に口なし、ですか…{w}でも、世の中には見たくなくても見えるものがあるものですよぉ～"
    pl "例えば？"
    show SCG_05 0 with fastdissolve
    hk "さあぁ…何があるのでしょうかあ？"
    nar "俺の返答を誘導するな。{w}見たくなくても見えるもの？それはこの暑苦しい現実のことじゃねえの。"
    nar "認めなくても認めるべきこと。社会生活のために仕方なく受け入れなければならない…"
    nar "聞くまでもなくうんざりした小言の始まりだ。"
    pl "どうせ主教様も俺の単独行動に一言物申したいんだろ？"
    show SCG_05 5 with fastdissolve
    hk "あらま～…"
    pl "反省は自分でちゃんとやるから、弁解くらいはさせてよ。"
    pl "無視できなかっただけだ。{w}死んだ人の声は俺には聞こえないけど、生きている人の声はどうしても聞こえてしまうから。"
    show SCG_05 8 with fastdissolve
    hk "死人は寂しいでしょうね～"
    pl "そのまま死なせて、聞こえなくなる方が寂しいだろう。"
    pl "毎日死人の声を聴いているはずの主教様には理解できないかもしれないけど。"
    show SCG_05 0 with fastdissolve
    hk "いいえ、わたくしにも死人の声は届きません。"
    hk "ゆえに、命ある者のために祈るのですよ。"
    pl "……"
    pl "あのさ。{w}さっき、なんで「悔悟」と繰り返していたんだ？"
    hk "祈るべき時が来たからです。"
    hk "かわいそうにも、世の中には自らの意思では悔悟できない兄弟様もいらっしゃいます。"
    hk "ゆえにわたくしは、みなさまが罪を滅ぼしー正しい道を進めるよう、神様に祈りをささげるのです。"
    pl "主教としての責任ってことか。"
    hk "そうですね…{w}わたくしは確か、主教の身としてーその使命を果たすために世の中に奉仕してますが…～"
    show SCG_05 1 with fastdissolve
    hk "多分、主教じゃなくたってそうしていたはずですのでえ。"
    hk "罪深い生涯の中、一緒に声を上げて祈りをささげてくれる人がないのなら、それこそ寂しいことではないでしょうかぁ。"
    pl "はあぁ…主教様は親切すぎなんだよ。罪ある者は、それだけでもう恥の多い生涯を送るしかないんだよ。"
    show SCG_05 0 with fastdissolve
    hk "罪は誰しもが犯しうるものです。なので悔悟の機会もまた公平ですよぉ。"
    show SCG_05 1 with fastdissolve
    hk "兄弟様も、時が来たら恥ずかしがらず、わたくしに逢いに来てください…♪"
    pl "そんな事態にならないのがベストなんだろうけどな。"
    pl "あの、主教様は…{w}自分にも罪があると思ったことある？"
    show SCG_05 0 with fastdissolve
    hk "それはもちろんです。{w}わたくしもまた常に罪を担っていますよ。"
    nar "人が毎日死んでゆき、その不義を見逃さないとならない浄化部の仕事。"
    nar "その主教の座は、俺の想像以上に重いだろう。"
    nar "これからずっとこの神殿で働きながら、果たして俺はその重さを耐えられるだろうか。"
    pl "正直さ～普段の行いを見るとあまり信じられなかったけど、やっぱりすごいな。{w}主教ってただでできるもんじゃないな。"
    show SCG_05 2 with fastdissolve
    hk "うー…{w}どういう意味ですかぁ？わたくしはいつも頑張っているのにぃ～！大人に対してそれは失礼ですよぉ～"
    pl "褒め言葉だって、褒め言葉！頼もしい人だな、主教様は！"
    show SCG_05 4 with fastdissolve
    hk "わぁお～誉め言葉ですかぁ…えへへ…♪"
    show SCG_05 0 with fastdissolve
    hk "しかし…{w}主教としての責任って、これぐらいで妥協できるものではありませぇん。"
    hk "どうかその目で確と見届けてくださいねぇ。"
    pl "おう。"
    hide SCG_05 with dissolve
    nar "主教様は、その一言を残して神殿に戻る。{w}ヘンな人だ。{w}こうやって奥の深さを測れないと悟った時こそ相当気まずい。"
    nar "だが、やっぱりあの時感じた、背筋の凍る様な感じとは違う。{w}それは多分、きっと…{w}彼女とは違う者だ。"
    stop music fadeout 3
    hide screen textbox with dissolve
    pause 2
    if hssh_rkn == True:
        scene bg01_1 with dissolve
    else:
        scene bg01_2 with dissolve
    stop music fadeout 3
    call place01 from _call_place01_4
    pause 1
    nvl clear
    show screen nvlbox with dissolve
    "\n 神殿の中は騒がしい。{w}この大勢の人々は、皆何かを見物するために集ったようだった。"
    "俺は観衆の中に混ざり、何事なのかも知らずに視線が向いている所を一緒に見つめた。"
    "その瞬間、観衆が静かになる。{w}皆の視線が向いていた露台の上に誰かが現れたのだ。"
    "一斉に入ってきた彼らは、全員黒いローブを被っていて、一見体格がたくましい男性に見えた。"
    "最後尾に立っている人は見慣れていた。{w}ハク主教様だ。{w}俯いて両手を合わせた彼女の表情は、"
    "さっきまで俺と話し合ったことがもう遥か昔のことになったみたいに、厳かに静まっている。"
    et "何かが始まるってことが分かる。"
    nvl clear
    play music "audio/bgm/grumble.ogg" fadein 60
    "\n 「神に肉身を全部捧げ働くべき信者が、不純な異性交際によりその身に新たな命を宿らせた故、異端と判断しこのように連行した」"
    "一番前に出ていた人がその一言を何度か繰り返す。{w}その声はとても大きく、はっきりとすべての観衆の視線を捕らえる。"
    "さっきから心臓が忙しなく脈打つ。{w}不安な気持ちに背筋がぞわっとして、俺は周りを必死に見まわした。"
    "ここにいるべき人がここにいない。{w}こめかみの底から血が走り、早まる鼓動に拍子を足してく。"
    et "あらゆる不安と恐れの渦で、彼は言い足す。"
    nvl clear
    "\n 「元より、彼女は本来身嗜みを正しくしていなかったため、到底相手の男性を推測することはできない」"
    "彼は、引き続きあの女の名前を聞き流しもできないほどはっきり、大きく叫んだ。"
    "聞き慣れたその名前の前には、「異端」という不慣れな単語が付いている。"
    "すかさず異端の姿が現れる。{w}彼女がそこに居る。そう俺は思ったものの確信はできなかった。"
    et "その姿が、本当に、見逸れるほど醜くなっていたから。"
    hide screen nvlbox with dissolve
    pause 1
    show story10 with slowdissolve
    pause 2
    show screen nvlbox with dissolve
    nvl clear
    "\n 彼女は多分、一晩中牢獄に下されていたようで、汚物の染みで汚れたボロボロの服を着たまま後ろに立っている警備員二人が"
    "錆びた鎖を引っ張ってこそやっと不安定な歩みで歩くことができた。"
    "長く垂らした散髪は、光を失い、窓に張られたカーテンのように顔を隠している。"
    "名前を呼ばれたハク主教が一歩前に出て異端の前に立った。"
    "異端は薬に酔ったようによろよろしながらももがく。{w}縛られた腕のせいで誰かが掴んでいないと倒れそうだった。"
    et "その汚い女の前に立った彼女は、毅然たる姿勢を失わず、もの静かに両手を合わせた。"
    nvl clear
    "\n 「尊敬すべき聖母様、歓喜されし…本日、一匹の仔羊が全ての罪を洗い直し、平穏な死を受け入れ、神の御許へ…」"
    "死刑を知らせる祈祷文を詠み始めた主教様の声は酷く淡々で、今朝聞いていた声と変わらない所が気を遠ざける。"
    "もう当たり前な日常になったことと、目の前の非日常が混ざり合うのを、俺の頭は到底受け入れられない。"
    "途中から内容を聞き取れなかった祈りが終わったのか、主教様はローブを被った男一人と共に敷居を越えてゆく。"
    et "彼女が消えたこの空間にはもう汚れだけが残っている。"
    nvl clear
    "\n 切れそうにやせた肩が、ここを押し潰している重圧感を耐えなかったように揺らめく。"
    "群衆はその姿を見ながら非難の声を上げ始めた。"
    "中には涙を流す人もいれば、面前から罵倒しながら後ろ指を指す人もいた。"
    "弾き出す嘆声に歩きを止めた彼女は、しばしこっちを向いた。{w}腹の付近が一目で分かるほどに痩せていた。"
    et "彼女はしばらくの間、最後の呼吸を絞り出すと思いきや、たちまち顔を上げては叫んだ。"
    nvl clear
    "\n 「私は何も悪くない！！」" with sshake
    "神の名に於いて。額の下に垂らされた前髪の間に間に光る紅い瞳は、反省の気配もなくただただ悪に満ちている。"
    "その鋭い目線が俺に向かっているような気がして息が出来なくなる。"
    "彼女の突発的な行為に、警備員は焼かれた鉄で腰に印を付ける。止まった彼女を再び歩かせたのだ。"
    "皮が焼かれる匂いと共に、女性の絹を裂くような悲鳴が館内を満たす。"
    et "上がってくる吐き気に、俺は目を閉じて、急いで口を塞いだ。"
    nvl clear
    "\n だがそれだけでは足りなったのか、絶えられなかった反吐が涙と共に指の間から漏れ出る。"
    "その異常に気付いた周りの人たちが雑言と共にその場を避ける。"
    et "俺はそのままへたり込む。力が抜けた膝は、立ち直せる気配が全く見えなかった。"
    stop music fadeout 3
    hide bg11
    hide screen nvlbox
    with dissolve
    pause 1.0
    nvl clear
    scene black with dissolve
    pause 2
    if hssh_rkn == True:
        scene bg15_1 with dissolve
    else:
        scene bg15_2 with dissolve
    call place15 from _call_place15_1
    show screen textbox with dissolve
    nar "やっと長かった一日の終わりが近づく。"
    nar "あの衝撃的だった光景に対しての気持ちが落ち着いた後、俺の頭の中はひたすら不安感で満たされた。"
    nar "彼女は俺のせいで死んだのか。{w}じゃあ、彼らが俺を探し出してしまうのではないか。"
    nar "正直な所、彼女なんぞ目の前から永遠に消えてしまえと一回も願っていなかったなんて言ったらそれこそ嘘だ。"
    nar "故にそれがすごく怖かったのだ。{w}目を逸らしたかったのに、つまらない良心が何度も後ろを振り向かせる。"
    nar "そんな不安が相次ぐと、相手の男性を推測できなかったという言葉だけを呪文のように繰り返し唱えつつ自分自身を戒める。"
    hide screen textbox with dissolve
    show SCG_03 7 with dissolve
    show screen textbox with dissolve
    nar "そんなことを考えながら寮に戻ると、シーキュレットが自分の部屋のドアを開いていた。"
    nar "寮で見たのは初めてだ。"
    nar "あの部屋には、朝にも夜にも出入りする人がないから、空き部屋だと思ったのだが、あいつが部屋の主なら納得が付く。"
    pl "お隣ってお前だったのか？"
    nar "彼の口から出てきたのは、質問とは全然違う返答だった。"
    show SCG_03 72 with fastdissolve
    sc "もっと気を付けた方がいいんじゃない。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    pause 1.0
    scene black with dissolve
    play music "audio/bgm/securett.ogg" fadein 3
    pause 1
    show screen textbox with dissolve
    nar "門に隠されて、あの時彼がどんな表情だったのかは分からない。"
    nar "だが、あのひやりした一言がやっと落ち着いた胸を乱し、精神を蝕んでいく。"
    nar "今すぐにでも彼を捕まえて問い返したいところだったが、同時に返事が怖くてドアを叩けなかった。"
    nar "俺は、自分の部屋に籠った後にも不安を払いのけず、壁に耳を傾けた。"
    nar "自分の緩やかな心臓の鼓動だけが静かな部屋で脈動してるのが気持ち悪かった。"
    hide screen textbox with dissolve
    pause 1.0
    scene black with dissolve
    pause 1
    if hssh_rkn == True:
        scene bg10_1 with dissolve
    else:
        scene bg10_2 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "どれだけの時間が経ったのだろう。{w}壁の向こうから音がした。"
    nar "ベッドのばねが傾くような、あるいはクローゼットが開くようなわずかな音。"
    nar "俺はびっくりして壁から遠さかる。{w}幻聴かもしれない。{w}だがいらだたしさは俺の脳裏に刻まれ、剥がされなかった。"
    pl "他の部屋…他の部屋だったんだ…"
    nar "特に誰かが聞いてるわけでもないのに、言い訳のように独り言が出てくる。"
    nar "彼女の部屋と彼の部屋の間には俺の部屋一つ。{w}そして俺はあの時、彼女の部屋に{cps=*0.1}…{/cps}いたはずだ。"
    nar "何故だか脳の中に何かが這いこんで濁しているように、記憶に確信が付かない。"
    $ _skipping = False
    nar "俺は布団を被って、長い間深呼吸をした。{w}不安な呼吸は、日が昇るまで続きそうだった。"
    hide screen textbox with dissolve
    nvl clear
    stop music fadeout 5
    hide screen keymap_screen
    $ _game_menu_screen = None
    $ show_quick_menu = False
    hide screen at_frame
    scene black
    with slowdissolve
    $ _dismiss_pause = False
    pause 2
    jump day5
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
