label day1:
    $ day = 1
    if hssh_rkn == True:
        $ save_name = "day 1, 朝, 楽園"
    else:
        $ save_name = "day 1, 朝"
    play sound 'audio/SE/bell 1.ogg' fadein 2.0
    image 1day = Text("day 1",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '1day' at day00 with slowdissolve
    pause 5
    hide expression '1day' with slowdissolve
    stop sound fadeout 1.0
    pause 3.0
    show screen at_frame  with dissolve
    play music 'audio/bgm/dream.ogg'fadein 5.0
    pause 4.0
    scene bg12 with slowdissolve
    pause 2

    show screen nvlbox with dissolve
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    show screen keymap_screen
    $ _game_menu_screen = 'preferences'
    if hssh_rkn == True:
        "\n 座り込んだ脚にはもう二度と力が入らない。"
        "耳と繋がった頬から、熱が上がって火照った頭よりも更に熱い血が溢れ出ていた。"
        "俺は、俺の物でない腐った血の溜まりに座ったままで重たい頭を上げた。"
        "濁った雲で曇った真っ暗な空。真ん中に、黄色い月が一つ昇っているだけだ。"
        "恐ろしいほどに明るい月が、俺たった一人を照らしているということが怖かった。"
    else:
        "\n 一足踏み入れればずぶずぶとした地面に足が沈んでいく。{w}見て見ぬふりのまま前に進むと靴の角がぬめっとした泥によって嵌まっていった。{w}歩けば歩くほど足は重くなり、溜めきった息を吐きだす。"
        "肺が捩れる様な激痛。"
        "雨天でもないのに頭もびしょ濡れだ。{w}どれだけ走ってきただろうか…{w}汗ばんでびしょびしょの手を誰かが握ってくれている。"
        "その手を握り返しもっと強く引けば、同じく息の上がりきった彼女が俺の名前を呼んだ。"
    et "\n{cps=*0.2}………{/cps}"
    hide screen nvlbox with dissolve
    scene black with slowdissolve
    stop music fadeout 5.0
    pause 5.0
    nvl clear
    play sound 'audio/se/wake up.ogg'
    scene bg10
    show SCG_02 5 with hpunch
    show screen textbox with dissolve
    qus "きゃ……！"
    stop sound
    pl "うわっ？！"
    play music 'audio/bgm/maya.ogg'
    nar "夢から醒めた俺は状況を把握しようと必死に周りを見渡した。"
    nar "ここは確か、{w}新しくお世話になることになった神殿の寮で、{w}俺は荷物を片付けて真っすぐ寝落ちてしまって、"
    nar "今目の前にいるのは……{w}\nか、{cps=*0.1}カ{/cps}ワイイ女の子！"
    nar "…全然頭が回らない。"
    show SCG_02 0 with dissolve
    qus "………"
    qus "…あ、あのぅ…"
    pl "んぁ？！"
    show SCG_02 at huruhuru
    qus "あのぉ…そのぉ…"
    pl "お、おう？"
    qus "…新入員は…30分まで部署に集合してください…って…"
    pl "んん…？あ！そっか！"
    hide SCG_02 with dissolve
    nar "挨拶を返す間もなくその女の子は急いで外に出て行ってしまう。"
    nar "俺はそのままぽつんと部屋の中に取り残されてしまった。{w}外からはバタバタと廊下を走る音が聞こえてくる。"
    hide screen textbox with dissolve
    with dissolve
    pause 1
    show screen nvlbox with dissolve
    if hssh_rkn == True:
        "\n 窓の外はまだまだ暗かった。{w}今何時だ？{w}俺はぐちゃぐちゃのままの荷物から自分の修道着を探し始めた。"
    else:
        "\n 窓の外はもう日が昇っている。{w}今何時だ？{w}俺はぐちゃぐちゃのままの荷物から自分の修道着を探し始めた。"
    "人は誰もが成年の日を迎えると一人の大人として仕事に就く権利を得られる。{w}俺は州都じゃあもうとっくに成人式を迎えて一年は経っているはずの歳だが、今日になってやっと立派な社会人になることができた。"
    "ここに来て一番最初に気付いたのは、多分俺はここ基準じゃ少しばかり珍しい容姿だということ。{w}俺の故郷じゃ皆が似たような肌や髪の色を持っていたけど……"
    "州都の人々は皆色が薄くて細いという印象だった。{w}俺の基準からすると彼らの容姿の方がよっぽど珍しい。{w}とにかく彼らは俺のことが随分と珍しいのか、すれ違えば必ず驚いた顔をする。"
    et "そう、さっきの女の子みたいに、だ。"
    hide screen nvlbox with dissolve
    nvl clear
    pause 1
    show screen textbox with dissolve
    pl "……なんか、見たことのあるような、ないような…どっかで会ったっけか？"
    nar "不思議なことに、その女の子から既視感が拭えない。"
    nar "また出会ったら何かわかるだろうか。{w}俺は未だずっと暗いままの部屋から外へと向かった。"
    hide screen textbox with dissolve
    nvl clear
    call place10 from _call_place10
    $ show_quick_menu = False

    show screen morning with dissolve
    hide screen morning
    $ renpy.call_screen("morning")
    show story02
    $ show_quick_menu = True
    with dissolve
    pause 1
    show screen textbox with dissolve
    pl "よぅし、今日も張り切って行こうか！"
    hide screen textbox with dissolve
    pause 1
    hide story02 with dissolve
    pause 1
    stop music fadeout 3
    scene bg01 with dissolve
    call place01 from _call_place01
    show screen textbox with dissolve
    nar "奥へ向かえば見えてくる内部は妙に暗かった。扉を開けば独特の臭いが鼻を刺激する。"
    nar "古い壁紙や埃のようなかびくさい臭いを脱臭剤なんかで蓋をしておいたのか、"
    nar "腐った食べ物の臭いすら薄く散乱していて正直キツいぐらいだった。"
    nar "他とは違う空気だということが皮膚から感じ取れる。{w}こんなんじゃ分離されているのも無理じゃないか。"
    nar "中に入ると、開いた扉の音で小さい体格の女の子がこちらへバッと振り返る。"
    nar "そして、しかめっ面で、俺に向かってバタバタと足を鳴らしながら近寄ってきた。"
    hide screen textbox
    play sound 'audio/se/wake up.ogg'
    show screen textbox
    qus "ねえアンタ、遅刻したご身分にそのふざけた服装は一体何のつもり？！" with hpunch
    show SCG_101 0 with dissolve
    play music "audio/bgm/daily.ogg"
    pl "お…俺の服装が何だってんだよ！"
    lz_q1 "何で修道着にそんな変な飾りを着けているのよ！"
    pl "カッコイイじゃんかよ～{w}\nいや、正直誰があんな暑苦しい服を通常着出来るかっての！"
    show SCG_101 2 with fastdissolve
    lz_q1 "あ、暑苦しい…？！{w}ふざけるのも程ほどにしなさいよね！"
    show SCG_101 0 with fastdissolve
    lz_q1 "アンタは一体何者？{w}魔導部の特採っていうからどんなヤツか顔でも拝んでやろうかと思えば、ただのまっくろ黒助じゃない！"
    pl "な、なんだと…"
    show SCG_101 2 with fastdissolve
    nar "その無礼極まりない言動に少しばかり不意打ちを喰らって呆然としていると、後ろからキツい香水の臭いに刺激される。"
    nar "急に現れた金髪の女性が、自分の身体を押し寄せ俺の腕に掴まってきたのだ。"
    hide screen textbox with dissolve
    show SCG_101 at left
    show SCG_102 1 at right
    with dissolve
    pause 0.01
    show SCG_102 1 at bounce
    show screen textbox with dissolve
    lz_q2 "やだ、初日から喧嘩してんの？{w}あんまいじめないであげてよ～"
    show SCG_101 0 with fastdissolve
    lz_q1 "ハァ……―{space=-3}―{space=-3}―、そんな―{space=-3}―{space=-3}―{space=-3}―{space=-3}―{space=-3}じゃない？"
    pl "……?"
    hide screen textbox with dissolve
    show SCG_102 0 with fastdissolve
    show screen nvlbox with dissolve
    "\n 列車に乗ったあの日からずっと今まで感じてきた違和感が一つあった。"
    "単純に発音のアクセントが違うだけかと思ったが、どうやら州都で使う言葉は俺の方の地域の言葉とは多少違うらしい。"
    "完全に聞き取れないってレベルではないが、今みたいに早口で小さく喋られたりしてしまったらついていけなくなってしまう。{w}実際、今丁度聞いた彼女らの名前すらただでさえ聞き慣れていない単語にハッキリとしない発音でどうしても聞き取れなかった。"
    "まあ、一緒に過ごしてればそのうち分かるだろう。今は取り合えず{color=#ce8349}委員長{/color}と{color=#fce5cd}金髪女{/color}とでもしておくか。"
    et "今はこれぐらいで凌げるけど、後々重要な話を聞き間違えるなんてしたら大変なことになってしまうだろうな…"
    nvl clear 
    "\n まず、何となく雰囲気でわかったのは体格的に小さい委員長と背の高い金髪女は友達らしい。{w}委員長が何かしらゴチャゴチャと怒ると金髪女は笑いながら俺の背を一撫でしては離れる。"
    et "その感覚に何故か一瞬途轍もない寒気を感じてしまった。"
    hide screen nvlbox with dissolve
    nvl clear 
    show screen textbox with dissolve
    pl "それよりさ、ここでオリエンテーションがあるんじゃなかったのか？{w}お前たちももしかして新入り？"
    show SCG_102 0
    show SCG_101 2 with fastdissolve
    lz1 "ハア？誰が新入りよ！"
    show SCG_102 2 with fastdissolve
    lz2 "あたしらはきみたちよりちょっと前から居た方。センパイって呼んでね♪"
    show SCG_102 2
    show SCG_101 0 with fastdissolve
    lz1 "この子が一人じゃ不安っていうから付いてきてやっただけ。"
    hide screen textbox with dissolve
    hide SCG_101 0
    hide SCG_102 0
    with dissolve
    show SCG_02 0 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "どこに居たのか、桃色の女の子が手を引かれギクシャクとした姿勢でやっと前に出てくる。"
    nar "彼女は小さく不安そうな吐息を垂らしてはずっと目を伏せたまま、たまにこちらを見上げてくる。"
    nar "俺はまた、その姿をどこかで見たような既視感に囚われていた。"
    pl "その…今朝…"
    show SCG_02 at right
    show SCG_101 0 at left
    with fastdissolve
    lz1 "そう、ワタシ、彼女のお姉ちゃんだからさ。"
    pl "全然似てないけど？"
    show SCG_101 2 with fastdissolve
    lz1 "義理のよ、{cps=*0.1}義{/cps}{cps=*0.1}・{/cps}理{cps=*0.1}・{/cps}の！"
    show SCG_101 0 with fastdissolve
    lz1 "ハァ…いいからアンタも何か言ったら？挨拶ぐらい出来るでしょ。"
    hide screen textbox with dissolve 
    show SCG_02 0
    hide SCG_101
    show SCG_02 8 at center
    with dissolve
    show screen textbox with dissolve 
    qus "………"
    show SCG_02 0 with fastdissolve
    my "……{color=#ff9587}マヤ{/color}…{color=#ff9587}エルベット{/color}です、よろしくお願い致します…"
    pl "お、おう…"
    hide SCG_02
    show SCG_101 0 at left
    show SCG_102 1 at right
    with fastdissolve
    nar " {nw}"
    show SCG_102 1 at bounce
    lz2 "あはははっ！\nマヤちゃんビビっちゃったじゃ～ん！男の前だからなの？カワイ～"
    lz1 "違う違う、この子故郷に居た頃からずっとこうだったってば。{w}言ったじゃん？"
    hide SCG_101
    hide SCG_102
    show SCG_02 0
    with dissolve
    my "………"
    pl "ええっと…[na]って言うんだ。{w}\n今朝はありがとな。{w}多分俺が年上かも知れないけど一応よろしく。"
    hide SCG_02
    show SCG_101 0 at left
    show SCG_102 0 at right
    with dissolve
    nar " {nw}"
    show SCG_101 at bounce
    lz1 "どうせ一年差でしょ？{w}ここで働くんなら一年ぐらい差でもないわ。{w}アンタもこの子も同じ子供みたいなものよ。"
    lz2 "[na]ちゃんねえ～{w}ちょっと名前珍しいんじゃない？"
    show SCG_102 1 with fastdissolve
    lz2 "ねえねえ、[na2]ちゃんはここ何する所か知ってて来ちゃったの？"
    pl "何するとこなんだよ？"
    nar "俺の返しが相当面白かったらしく、金髪女は口を広げてゲラゲラと笑う。{w}他の一人も呆れたように鼻で笑う。"
    show SCG_101 3 with fastdissolve
    lz1 "アンタさ、来るとこ間違えたんじゃない？"
    pl "いや、そうじゃなくって、説明はあっち行って聞けとか言われたから…"
    show SCG_102 4 with fastdissolve
    lz2 "ねえこの子マジでウケるんですけど、説明してやりなよ～"

    show SCG_101 0 with fastdissolve

    lz1 "……ハアァ…しょうがないわね、{w}いい？一度しか言わないからちゃんと聞いといてよね。{w}マヤ、アンタももう一回良く聞きなさい。"

    show SCG_102 0 with fastdissolve

    nar "皆がクスクスと笑っている中、一人だけ不安そうな顔で佇んでいたマヤは俺とほぼ同時に頷いた。"
    nar "途中、隣に立っていた金髪女が何度か俺を見て笑うもんだからそちらに気が行ってしまったが…{w}とにかく軽く纏めるとこうらしい。"

    hide screen textbox with dissolve
    nvl clear
    show screen nvlbox with dissolve
    "\n ここは神から授かった力を以て人々を禍から救うため中央教皇庁を中心に設立された神殿、「セイント・シェオル」。"
    "神殿は六つの大陸に一つずつ存在していて、各地域の枢機卿が管理している。{w}セイント・シェオルだと四人の主教の元からまた部署が分かれている。"
    "{vspace=8}{color=#6d9eeb}{rb}魔導部{/rb}{rt}まどうぶ{/ rt}{/color}、{color=#d0a6bd}{rb}学術部{/rb}{rt}がくじゅつぶ{/rt}{/color}、{color=#93c47d}{rb}保健部{/rb}{rt}ほけんぶ{/rt}{/color}、{color=#fff2cc}{rb}浄化部{/rb}{rt}せいかぶ{/color}。"
    if hssh_rkn == True:
        et "その中でも俺たちが所属している浄化部は六つの神殿の中唯一セイント・シェオルにのみ設立された部署であり、お国の歯車が上手く回っていけるよう様々な「後始末」を担当する。{w}そして、一か月の研修期間が終われば正職員である司祭として認められる……"
        nvl clear
        hide screen nvlbox with dissolve
        show screen textbox with dissolve
        pl "一か月？一週じゃねぇ？"
        lz1 "一週？研修期間がそんなに短かったら何を学ぶの。"
        pl "そりゃそうけど…まあ、一応ありがとうな。今日入った新入りは俺とマヤだけか？"
        nar "俺がちゃんと理解できているのか確認を取りたかったが、どうやら答えてくれそうにはない。"
        nar "仕方なく疑問を畳んだ俺は、今まで頭に入った新しい情報を整理する。"
    else:
        et "その中でも俺たちが所属している浄化部は六つの神殿の中唯一セイント・シェオルにのみ設立された部署であり、お国の歯車が上手く回っていけるよう様々な「後始末」を担当する。{w}そして、一週間の研修期間が終われば正職員である司祭として認められる……"
        nvl clear
        "\n 俺がちゃんと理解できているのか確認を取りたかったが、どうやら答えてくれそうにはない。"
        et "仕方なく疑問を畳んだ俺は、今まで頭に入った新しい情報を整理する。"
        hide screen nvlbox with dissolve
        show screen textbox with dissolve
        pl "そうか、ありがとな…{w}で、今日集まった新入員って俺とマヤだけなのか？"
        nvl clear
    lz1 "元からこの部署、ずっと人力不足で月末ごとに新入りを受け入れているのよ。{w}少しずつ定期的にって感じ。"
    show SCG_102 2 with fastdissolve
    lz2 "他の子にも会ってみたいの？{w}心配しなくてもすぐ会えるって～{w}お姉ちゃんが友達いっぱい紹介してあげるね～"
    hide screen textbox with dissolve 
    hide SCG_101
    hide SCG_102
    with dissolve
    play sound "audio/SE/door close.ogg" 
    pause 1.0
    show screen textbox with dissolve
    nar "その時、扉の開く音が聞こえる。{w}それまでしょうもないことで駄弁っていた二人は動きを止めた。"
    hide screen textbox with dissolve 
    pause 1.0
    show SCG_03 0 with dissolve
    pause 1.0
    show screen textbox with dissolve 
    nar "委員長は彼を見るなり分かりやすいぐらい顔が歪んだ。"
    show SCG_03 0 at left
    show SCG_102 4 at right
    with fastdissolve
    lz2 "あらま、{color=#d9d2E9}シーキュレット{/color}くんじゃない？{w}お忙しいんじゃなかった？こんなところにどしたの？"
    nar "金髪女が先に近寄って気さくに話し掛けるも、入ってきた男子は彼女に目もくれずこちらを睨み付けてきた。"

    show SCG_03 2 with fastdissolve

    sc "…ここは新入員だけ来る場所のはずじゃ？"

    hide SCG_102
    show SCG_101 0 at right
    with fastdissolve

    lz1 "それはワタシのセリフなんですけど。{w}アンタがなんでここに居るのよ？今日は主教様が…"

    show SCG_03 0 with fastdissolve

    sc "主教様は今日は来られないよ。{w}\n忙しい人だろう。ボクはその代わりに来ただけ。"

    show SCG_03 0

    nar "多分二人は仲があまり良くないらしい。"
    nar "一方的に話をぶった切られた委員長は嫌そうな顔で、しかしあえて言葉にはしないまま睨み返す。"
    hide screen textbox with dissolve 
    hide SCG_03
    hide SCG_101
    show SCG_03 0 at center
    with dissolve
    show screen textbox with dissolve 
    nar "その短い会話は既に終わってしまったようで、「{color=#d9d2E9}シーキュレット{/color}」と呼ばれた男はこちらに近寄り俺をじろじろと見つめてくる。"
    sc "こういう仕事、やった事ある？"
    show SCG_03 0 at left
    show SCG_101 0 at right
    with fastdissolve
    lz1 "そんなこと聞いても無駄よ無駄、\nこいつ本当にな～んにも知らなかったんだもの。"
    lz1 "神殿が何する所なのかも今やっと説明し終わったところよ。"
    sc "……"
    hide SCG_101
    show SCG_102 1 at right
    with fastdissolve
    with None
    lz2 "シーキュレットくん、その子たち連れてって指導してあげてくれない？"
    with None
    show SCG_03 2
    with fastdissolve
    with None
    sc "はあ…？"
    hide SCG_102
    show SCG_101 3 at right
    with fastdissolve
    with None
    lz1 "主教様がアンタに任せたんでしょ？{w}\nまっさか、こーんな大事なことをワタシたちに押し付けるつもりじゃないでしょうね？"
    hide SCG_101
    show SCG_102 1 at right
    with fastdissolve
    with None
    lz2 "そ～そ～、あたしたちもこれから仕事だから。{w}お願いね、臨・時・補佐教様♪"
    sc "……"
    hide screen textbox with dissolve 
    hide SCG_03
    hide SCG_102
    with dissolve
    show screen textbox with dissolve 
    nar "男が何も答えずにいると、二人は勝手に彼を通り過ぎ扉へと向かった。"
    hide screen textbox with dissolve 
    show SCG_101 0 at left
    show SCG_102 0 at right
    with dissolve
    show screen textbox with dissolve 
    lz1 "その子、ワタシの妹だから！ちゃんと教え込みなよ！"
    nar "一人が彼に念押しに言い放ってはそのまま部屋を後にした。"
    with None
    show SCG_102 1 with fastdissolve
    nar "その後を追うようにもう一人は余裕げにこちらに向かって手を振っては出ていく。"
    hide screen textbox with dissolve 
    hide SCG_101
    hide SCG_102
    with dissolve
    show screen textbox with dissolve 
    nar "俺は思わずそれに応えるように手を振り返していたが、すぐハッとして隣を振り向く。"
    hide screen textbox with dissolve 
    show SCG_03 0
    with dissolve
    show screen textbox with dissolve
    nar "残された男子が目を細めてはこちらを睨み付けていた。"
    nar "そして、深い溜息を吐いてはこちらに付いてこいと言わんばかりに手招きする。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    stop music fadeout 3
    nvl clear
    pause 2
    if hssh_rkn == True:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03
    play music 'audio/bgm/dialogue.ogg' fadein 3.0        
    show screen textbox with dissolve
    nar "階段上の廊下へと出るとカツコツと靴の鳴る音がやけに大きく聞こえてくる。"
    nar "ここの人はみんなヒールブーツでも履いているんだろうか。"
    if hssh_rkn == True:
        nar "窓の外から大きな陽が余計に存在感を示す。"
        nar "廊下に飾られている派手なステンドグラスはその光を反射し、建物全体を真っ白く彩っていた。"
        hide screen textbox with dissolve
        show SCG_03 0 at left
        show SCG_02 0 at right
        with dissolve
        show screen textbox with dissolve 
        pl "今って何時？ なんかここに来てから日が沈むのを見てない気がするぞ。"
        sc "今は白夜だからだよ。"
        pl "白夜って？"
        my "夜にも陽が沈まなくって、ずっと昼のままな時期のことなの。"
        pl "へぇ、マヤは賢いんだな。なのにこんなに寒いわけ？"
        hide SCG_03
        show SCG_02 0 at center
        with dissolve
        my "州都では普通だと思うよ、[na2]くんは州都が初めてだから知らないんだ…"
        pl "マジかよ…俺、寒いのは苦手なのにな…"
    else:
        nar "外に出てもやはり陽は沈んだまんまだ。"
        nar "廊下に飾られている派手なステンドグラスは空の濁った色が反射し、建物全体を彩っていた。"
        nar "まるで朝焼けのような青白さだ。"
        hide screen textbox with dissolve
        show SCG_03 0 at left
        show SCG_02 0 at right
        with dissolve
        show screen textbox with dissolve 
        pl "今って一体何時なんだ？もしかして州都じゃ陽が昇らないのか？"
        sc "今は極夜だからだよ。"
        pl "極夜って？"
        my "昼にも陽が昇らなくって、ずっと夜のままな時期のことなの。"
        pl "へぇ、マヤは賢いんだな。ということはこの寒さもずっと続くのか？"
        hide SCG_03
        show SCG_02 0 at center
        with dissolve
        my "そうだね…[na2]くんは寒いの、きらい？"
        pl "俺は暑いとこからきたからさ、どうにもなぁ…"
    pl "…てか、今{color=#E06666}[na2]くん{/color}って言った？"
    show SCG_02 6
    with fastdissolve
    my "そ、それがね…わたし、あだ名で呼ぶのがすきで…そのぉ…いや、だったかなぁ…"
    pl "や、そんな！気に入ったぜ！俺の名前は何とでも楽に呼んでくれ！"
    show SCG_02 0
    with fastdissolve
    my "よかったぁ…"
    show SCG_03 0 at left
    show SCG_02 0 at right
    with dissolve
    my "あの…シーキュレットくん、だよね…"
    show SCG_02 6
    with fastdissolve
    my "もし良かったらなんだけど…キューくんって呼んでいいかな…"
    sc "ダメ。"
    show SCG_02 3
    with fastdissolve
    my "ふえぇ…"
    pl "テメェ！マヤが頑張って話しかけてくれてるってのになんだその態度は！"
    hide screen textbox with dissolve
    hide SCG_03
    hide SCG_02
    with dissolve
    show screen textbox with dissolve  
    nar "彼は構わず振り向きさえしないままバインダーを取り出す。"
    nar "タイプライターで書かれた書類。指定場所などの簡単な住所や訳のわからない数字の羅列があり、"
    nar "その内いくつかには赤いペンでチェックを入れられている。"
    hide screen textbox with dissolve
    show SCG_03 0 with dissolve
    show screen textbox with dissolve    
    sc "ここに各自の業務量を記録して。{w}今日は初日だから見てるだけでいいけど、明日からはちゃんとやってから記入するんだぞ。"
    pl "どんな仕事をやるんだ？"
    sc "……"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    show screen textbox with dissolve  
    nar "シーキュレットは何も答えず足を速め、そのまま角を曲がり検問所を通り過ぎていく。"
    nar "彼の首に掛かっている白いロザリオを見せただけで審査官は黙礼と共に道を通してくれた。"
    pl "どんな仕事をやるんだって聞いてるじゃんかよ。"
    nar "後ろに付きながらもう一度聞くと、彼はイライラしてきたのか神経質に小さく咳き込んだ。"
    nar "―ガコン！入口を出る前シーキュレットは荷車を一つ引っ張り出す。"
    nar "デカい音を立てて引き出された荷車は各種の掃除用具やいくつかのサックが畳んであった。"
    hide screen textbox with dissolve
    show SCG_03 2 with dissolve
    show screen textbox with dissolve   
    sc "持ってて。"
    nar "まだ声変わりもしてないのか、少しばかり高いように感じる声で彼は言う。"
    show SCG_03 0 with fastdissolve
    sc "ここでボクら浄化部のやるべき仕事は…{w}\n他の部署の退魔のせいで汚れてしまった環境を掃除していくこと、"
    sc "通報の入った死体を片付けて処理すること、{w}最近増えてきた害虫の駆除。"
    sc "あと死体の防腐処理、埋葬のお手伝い、{w}\n「亡者」の撃退…{w}その他人手が必要な面倒くさい仕事は全部だと思っとけばいいから。"
    pl "亡者……？"
    show SCG_03 2 with fastdissolve
    sc "…知らないの？"
    nar "聞き慣れない単語を噛み締めるように繰り返すと同時に、先頭のシーキュレットが立ち止まり振り返る。"
    show SCG_03 2 at left
    show SCG_02 0 at right
    with dissolve
    nar "答えないままキョトンと彼を見つめ返すと彼は隣のマヤへ目線を向けた。{w}どうやらマヤは知っているらしい。"
    nar "それを確認したシーキュレットは首を横に振ってはもう一度歩き出す。"
    hide SCG_02
    show SCG_03 0 at center
    with dissolve
    sc "人には神聖力ってものがあるだろう？"
    pl "聖痕が発現するために必要って言うアレか？"
    sc "そう、神が人間に与えた唯一の慈悲とも言うんだ。{w}それだけ人間には到底理解できない力が神聖力さ。"
    sc "で、その偉大な神聖力が…{w}その器が死んだらどうなると思う？"
    pl "…消えない、とか？"
    show SCG_03 7 with fastdissolve
    sc "正解。"
    hide screen textbox with dissolve
    show screen nvlbox with dissolve 
    "\n 故郷じゃいつも人が死んだらすぐさまその死体を燃やすように、というのが風習だった。{w}死人の顔の代わりに燃え盛る炎を拝みながら、人の燃える臭いに耐えつつ別れを告げてきたってことだ。"
    " それがずっと不満だった俺はいつの日かそれを里の長に訊いたことがある。{w}その時確か似たような話を聞いたことがある気がした。"
    et " 人の死体っていうのは、死んですぐに燃やして天に返してやらないといけない。{w}\nでないとその怨念が残り、「地を這うバケモノ」となると。"
    show SCG_03 0
    hide screen nvlbox with dissolve 
    show screen textbox with dissolve 
    sc "神聖力に体を支配された肉の塊たちには生きた頃の意識も、記憶も全くない。{w}ただ力尽きるまで動き回るか…"
    sc "もしくは高確率で人を襲う。人には意識はないけれど本能ってものがあるからね。"
    sc "だからボクらはそれらを回収して、処理する必要があるんだ。"
    sc "いつも人手が足りなくて聖痕の個数や社会的地位も調べず適当に受け入れてる。{w}だから世間からの視線もあまり良くない。"

    show SCG_03 7 with fastdissolve

    sc "キミたちはまだ研修生だから、{rb}禍{/rb}{rt}ペスティス{/ rt}に直接送られる訳ではないけど。{w}代わりに掃除とかの簡単な雑仕事になるだろうね。"
    hide screen textbox with dissolve 
    hide SCG_03 with dissolve
    show screen textbox with dissolve    
    nar "シーキュレットは歩みを止めないまま淡々とした声でそう語る。"
    nar "俺は暗がりの道を辿りながらずっと耳に刺さる聞き慣れない冷たい単語たちを、"
    nar "果たして俺が理解した内容であっているのかを疑問に思っていた。"
    hide screen textbox with dissolve 
    show SCG_03 0 at left
    show SCG_02 5 at right
    with dissolve
    show screen textbox with dissolve    
    nar "隣で一緒に歩くマヤの歩幅が少しずつ不安定になる。"
    nar "足が疲れてしまったのかと思い、心配で彼女に目をやると真っ青な顔で震えていた。"
    nar "俺はそれがただの疲れから来ているものとは思えなくて、わざと声を上げる。"
    pl "お前の言い分じゃ、「浄化部」なんてただの神殿の奴隷じゃねぇか！"

    show SCG_03 7 with fastdissolve

    sc "でも国が上手く回ってく為には必要な存在さ。"
    hide screen textbox with dissolve 
    hide SCG_03
    hide SCG_02
    with dissolve
    nvl clear
    pause 2
    if hssh_rkn == True:
        scene bg13 with dissolve
    else:
        scene bg13_1 with dissolve
    call place13 from _call_place13
    show screen textbox with dissolve 
    nar "彼は道中、一軒の住宅の前で立ち止まる。{w}人の住んでいた痕跡は至る所から目に付くのに、人の気配がまるでなかった。"
    nar "急いで彼の跡を追おうと動いた瞬間、平たい板のような物が足に引っかかる。"
    nar "地面に幾つか並べて建てられているところから、人の立ち入りを禁止する標識みたいなものらしい。"
    hide screen textbox with dissolve 
    show SCG_03 7
    with dissolve
    show screen textbox with dissolve
    pl "こんなモン、事前に何も言われてないぞ…"
    sc "ちょっとぐらい黙っててよ。"
    pl " ハアァ～？？"
    show SCG_03 7 at left
    show SCG_02 0 at right
    with dissolve
    nar "彼が冷たく言い放った言葉にカッとして声を荒げた次の瞬間、目の前にマスクが一枚スッと配られる。"
    nar "それに戸惑った俺はそれ以上何も言えずにマスクを受け取った。"
    nar "隣のマヤにも一枚同じく渡した後、彼は自分の袖を捲り始めた。"
    sc "出来れば鼻で息吸わない方がいいよ。"
    hide screen textbox with dissolve
    hide SCG_03
    hide SCG_02
    with dissolve
    show screen nvlbox with dissolve
    "\n 肘までくる白いゴムの手袋を着けた彼は、最後に自分もマスクをしてからここまで引き摺って来た荷車から自分の身より大分大きい様に見えるバケツとサックを幾つか取り出した。"
    "人が毎日の様に死んでいく過酷な環境のお陰で死体を初めて見るってわけではなかったが、それでも扉向こうの光景は酷いモンだった。"
    "息を呑んでは固まった身体でよろめくマヤを、俺は庇う様に彼女の前を防いだ。{w}撒き散らかされた消毒剤の白い煙が目の前を埋め尽くしてもまだ地面の沢山の蛆虫が目立つ。"
    et "水分をたっぷり含んで腐ってしまった木材のフロアは、溶け始めた死体の肉片がへばり付いて真っ黒に変色しかけていた。潰れた皮膚の上をハエが飛び交う。"
    hide screen nvlbox with dissolve
    show screen textbox with dissolve
    my "う゛っ…"
    nar "その惨状を呼吸も出来ず見つめていたマヤが口を塞いだままその場から崩れそうになる。"
    nar "か細い腕と足が可哀そうなぐらい震えている。{w}倒れてしまったらどうしようと不安になってしまった。"
    hide screen textbox with dissolve
    show SCG_02 7
    with dissolve
    show screen textbox with dissolve  
    my "ひどい…"
    show SCG_03 7 at left
    show SCG_02 0 at right
    with dissolve
    sc "酷いって言うんだね。{w}これは人間の生きた証拠だよ。"
    show SCG_02 3 with fastdissolve
    my "うぅ…"
    pl "そうだろうがどうだろうが今は死体だ。{w}\n人様の目前に押し付けるようなモンじゃねぇよ。"
    show SCG_03 8 with fastdissolve
    sc "…まあ、死んだという証拠でもあるさ。"
    hide SCG_02
    show SCG_03 7 at center
    with dissolve
    nar "サックを持ち上げたシーキュレットがマスク越しに溜息を吐く。"
    sc "だったらボクがやっておくから、後ろに下がってて。"
    show SCG_03 8 with fastdissolve
    sc "そこで突っ立ってるのは仕事の邪魔。"
    nar "こんな状況でそんなことを言うか普通？"
    nar "何とか言ってやりたい気分になったが\nこれ以上マヤを一人にしておくわけにもいかなかった。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    show screen textbox with dissolve
    nar "さっきまで息の詰まるような空間にいたせいか、外の空気がやけに新鮮に感じてくる。"
    nar "マヤは俺にもたれ掛かるようにしてやっと一歩ずつ踏み出してる。"
    nar "そっと掴んでいた肩の手にはいつの間にか\nギュっと力が込まれていた。{w}まだ震えてる…"
    nvl clear
    hide screen textbox with dissolve
    show screen nvlbox with dissolve
    stop music fadeout 5
    "\n 俺から離れてフラフラと壁に向かったマヤは、俺が何か言葉を掛けようとするより先に音を立てて派手に吐き出してしまった。"
    " 色薄く水っぽい中身が口から塊となってボトボト地面に落ちていく。{w}真っ白と言っていいほど顔色の悪くなったマヤが壁から崩れ落ちるように地面に座り込んだ。"
    $ renpy.music.set_volume(0.5, channel="music")
    play music 'audio/SE/prologue wind.ogg' fadein 5
    "「大丈夫か？」"
    et " 近寄って彼女の様子を窺う。{w}彼女は下唇をグッと噛みこんだまま苦痛で唸りつつ首を横に振る。{w}固く閉じた目から涙がボロボロと流れていた。"
    nvl clear
    "\n「無理…こんなの無理だもん…"
    "だからやりたくなかったのに、{w}こんなとこ、本当に来たくなかったのに！」"
    "「落ち着きなって！ほら…」"
    " 俺はマスクの外面を使ってマヤの汚れた口元を少しずつ拭き取ってやる。{w}局地に追い込まれてしまい恐怖で声を荒らげる彼女はさっきより遥かに小さく見えてしまったからだ。"
    " 俺の気持ちが通じたのか、鼻をすすったマヤが袖を伸ばし自分の目元を拭う。"
    "「[na2]くんはいいなぁ、研修期間が終わったら魔導部にいくんだもんね」"
    et " 喘鳴で呂律さえまともに回っていないのにも関わらず、彼女の言っていることは驚く程鮮明に耳に焼き付く。"
    nvl clear
    "\n 何度も目元をゴシゴシと拭ったせいか、赤い瞼は腫れきっている。"
    "「つらいなぁ、\n才能がないのって…すごくつらいんだよ、[na2]くん。{w}\n向かえる場所がどこにもないのは…」"
    " 俺は、俺に似た年頃の女子なんか見たことがあんまりない。{w}女の兄弟は故郷に沢山いたが、全部かわいい妹か俺と随分歳の離れたお姉ちゃんたちぐらい。"
    "泣いている女の子なんて、勿論慰めたことなんてないし見たことすらない。"
    et "すぐ傍で俺とたった１歳差の少女が泣いている。{w}頭の中で励ましの文句がグルグル巡っては意味もなく砕け散った。"
    nvl clear    
    "\n 頭が真っ白になった時、同時にバッと思い浮かんだ思考があった。"
    "州都じゃあ、『大人に成った』なんて理由でこんな子供を社会へと突き落とすのか。"
    "「大人になんかなりたくなかったよぅ」"
    "白紙と化した頭の中へマヤの声がコダマする。"
    "俺たちは何も準備なんかできちゃあいない。こんな状態で一体何が出来るって言うんだろう。"
    "「最悪…{w}大人なんて、サイアク！」"
    " あまりにも高く振り上げられたマヤの手がどこかしらに投げ落とされるかのように震えていたから、俺はその手を取って握ってしまった。"
    et "俺のそれより相当小さいその手は、涙や鼻まみれで裾まで汚れてしまっていた。"
    hide screen nvlbox with dissolve
    stop sound fadeout 3.0
    stop music fadeout 3.0
    nvl clear
    pause 1
    show story03 with slowdissolve
    pause 2
    show screen nvlbox with dissolve
    $ renpy.music.set_volume(1, channel="music")
    play music '/audio/bgm/train meet.ogg'
    "\n「助けるよ！」"
    "マヤは目を大きく見開いて俺を見つめる。"
    "「な、何を……？」"
    "困惑したような声はさっきよりかは随分落ち着いたように聞こえる。{w}荒かった息も徐々に安定してきていた。"
    "「俺が、マヤを助ける。何があっても、どんなことでもマヤが必要とするならさ！」"
    et "吃驚したマヤより、俺の方がよっぽど吃驚していた。{w}知らぬ間に握りしめていた彼女の手をやっと解く。"
    nvl clear
    "\n 同時に、マヤのまん丸と見開かれた目も少しずついつも通りへと戻っていく。{w}多分、これで少しは落ち着いたのだろう。{w}マヤはさっき通り目を伏せては一度鼻を啜る音を鳴らせた。"
    et "\n「ありがとう……」"
    hide screen nvlbox with dissolve
    nvl clear
    pause 1
    hide story03 with dissolve
    pause 2
    show SCG_02 0 with dissolve
    show screen textbox with dissolve
    pl "い、いや、急にゴメン。"
    my "ううん、わたしこそ、困らせちゃってごめんね…"

    show SCG_02 6 with fastdissolve

    my "[na2]くんは…初めて会った時から思ったけど、人を助けるのが好きなのね…"
    pl "初めて会った時？"

    show SCG_02 0 with fastdissolve

    my "覚えてないの…？{w}ここに来る前だって、{w}\nそのお、列車で出会ったじゃない。"
    pl "え、そうだっけ？確かに、そうだったような…"
    nar "最初マヤに出会った時感じた既視感はこれだったのか…"
    hide screen textbox with dissolve
    stop music fadeout 2.0
    nvl clear
    pause 1
    hide SCG_02 with dissolve
    pause 1
    play music '/audio/bgm/dialogue.ogg' fadein 2.0  

    show screen textbox with dissolve
    nar "住宅に戻るとガタンガタンと荷車の音が聞こえてくる。"
    nar "先ほどまでは空いていたサックがその間何かを詰め込みでもしたのかふっくらと膨れ上がっていた。"
    nar "こいつが処理したんだろうな。{w}チラっと横目に見ると彼と目が合ってしまう。"
    nar "汚れきった手袋でマスクを下ろしたシーキュレットは俺とマヤに一つずつ、今度はモップとほうきを手渡してくる。"
    hide screen textbox with dissolve
    show SCG_03 7 with dissolve
    show screen textbox with dissolve
    sc "掃除、やった事ある？"
    pl "雑巾がけか掃き掃除ぐらいなら。"
    sc "ならリビングを掃除してくれるかい。{w}片付けはボクが全部やっておいたから…"
    pl "おう…"
    show SCG_03 0 at left
    show SCG_02 0 at right
    with dissolve
    my "…"
    sc "…無理そう？"
    my "ううん、大丈夫…"
    show SCG_03 8 with fastdissolve
    sc "最初から「上手くやれ」なんて言わないさ、人なんだし。"
    sc "でもこれぐらいも出来ないってなるとそれは流石に困るから、そこは頑張ってほしいな。"
    show SCG_02 7 with fastdissolve
    my "うん…"
    hide screen textbox with dissolve
    hide SCG_02
    hide SCG_03
    with dissolve
    stop music fadeout 3.0
    pause 1
    if hssh_rkn == True:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03_1
    show screen textbox with dissolve
    nar "明日からは、死体と遭遇することだけでなくそれを触ることにまで慣れていかないといけないんだ。"
    nar "心配だけが募る中、マヤの顔が俺以上に心配そうに歪んでいたのでついついそちらの方が気になってしまう。 "
    nar "元からお喋りって訳でもなかったが、それにしてもさっきからずっと黙ったまんまだ。"
    nar "だからと言って迂闊に話掛けられるような状況でもない。"
    nar "三人分の足音と重い荷車の音ばかりが鳴り響く中、静寂を割ってシーキュレットが口を開く。"
    hide screen textbox with dissolve
    show SCG_03 7
    with dissolve
    show screen textbox with dissolve
    play music "/audio/bgm/daily.ogg"
    sc "もう昼か…"
    pl "あ？"
    show SCG_03 7 at left
    show SCG_02 0 at right
    with dissolve
    sc "神殿ではこの時間が昼給食だから。{w}キミたちは先に帰っといて。"
    pl "飯の後は何すりゃあいいんだ？"
    sc "そうだね、キミたちは…{w}まあ、適当に休んでから寮に戻ればいいんじゃないかな。"
    my "も、戻ってもいいの…？"
    sc "研修生はあまり遅い時間まで仕事を任せられないようになってるんだよ。{w}聞かなかった？"
    show SCG_02 4 with fastdissolve
    my "そうなんだ……！"
    pl "良かったな！"
    show SCG_03 8 with fastdissolve
    sc "……"
    show SCG_03 0 with fastdissolve
    sc "あと、明日から質問や仕事はあの女の人たちに聞いてくれる？{w}ボクは今日はお願いされただけだから…"
    hide screen textbox with dissolve
    hide SCG_02
    hide SCG_03
    with dissolve
    show screen textbox with dissolve
    nar "俺が何かしら問い質そうとした途端、彼はこれで終わりといわんばかりにガタンと荷車を引いていく。"
    nar "まだ返事もしてないのに。きっとわざとあんなデカい音を出したんだろう。"
    nar "ウザいヤツ。{w}腹いせで振り向きもせず去り行く彼の後ろ姿に小さく悪態を吐いた。"
    hide screen textbox with dissolve
    pause 1
    nvl clear
    if hssh_rkn == True:
        scene bg01 with dissolve
    else:
        scene bg01_1 with dissolve
    call place01 from _call_place01_1
    show screen nvlbox with dissolve
    "\n マヤと一緒に部署近くの食堂へ向かうと、さっきと違って結構人が集まっていた。"
    " 似たような雰囲気の人同士がそれぞれ自分たちが属するグループの中でしょうもない雑談をし合いながら笑いあう。{w}\n話題はすれ違いざまに聞いても皆似たようで違う会話ばかりだ。"
    " 俺とマヤが中へ入ると、顔も知らない人たちが俺たちを見るなり高笑いする。{w}彼らを中心としてまた周りが妙にざわつき始めた。"
    et " そんなに仕事帰りの新入りが面白いことってあるのか？{w}俺はどうやらこの部署じゃ相当の人気者になってしまったらしい。"
    nvl clear
    "\n あちこちで飛び交う質問や挨拶に応えてやっていると、騒々しい中後ろから誰かが俺の肩をそっと掴んでくる。"
    " 「この子、借りてくね～」"
    " 朝出会った金髪女だった。"
    et " 先程までずっと死体の臭いで充満した場所にいたからか、彼女のキツい香水の匂いが少し違うように感じられるような気もする。"
    nvl clear
    "\n 彼女もここでずっと仕事してきたんだ、自分を飾りたがる年頃の女性であるほど死臭が移るのが嫌なんだろう。{w}俺だって正直お断りだ。"
    " 彼女が俺を引っ張り上げると、俺の周りでずっと話を掛けてきた男たちも笑いながらこちらへ手を振ってくれる。"
    et " 州都は社交性の足りない陰の人間しかいないのか、とも思っていたがどうやらそうでもないらしい。"
    hide screen nvlbox with dissolve
    show SCG_101 0 at left
    show SCG_102 0 at right
    with dissolve

    show screen textbox with dissolve
    pl "お陰で助かったぜ、先輩…"
    pl "人が沢山集まってくる、ってのはウソじゃなかったんだな…"
    show SCG_102 1 with fastdissolve
    lz2 "アハハ！随分クタクタじゃん！"
    show SCG_101 2 with fastdissolve
    lz1 "マヤ！"
    pl "俺もいるんですけどネ。"
    hide SCG_102 0
    show SCG_02 0 at right
    with dissolve
    nar " {nw}"
    show SCG_101 at huruhuru
    lz1 "大丈夫？コイツとかあのウザ男とかが虐めてない？"
    show SCG_02 3 with fastdissolve
    my "おねえちゃん…"
    pl "虐めてなんかないって！"
    hide SCG_02
    hide SCG_101 0
    show SCG_102 3
    with dissolve
    lz2 "あぁ～目眩がしそうだわ。"
    lz2 "前はこんな騒がしくなかったはずなんだけど、最近日が昇らないからかしら、なんか皆災いだの滅亡だのでざわざわしてるのよ。"
    pl "何の話だ？"
    show SCG_101 0 at left
    show SCG_102 3 at right
    with dissolve
    lz1 "身も蓋もない終末論の話よ、もう！"
    lz1 "今年であの大災難からちょうど2000年目だったとか何だとか…そんな迷信はもううんざり！"
    show SCG_102 1 with fastdissolve
    lz2 "そーそー、前にも大洪水の終末説が回ったせいでしばらく請願がヤバくてうるさかったよね～"
    show SCG_101 3 with fastdissolve
    lz1 "あの時の魔導部のヤツらの過労死しそうな姿、アンタたちにも見せたかったわ、クスクス…"
    show SCG_102 4 with fastdissolve
    show SCG_102 at bounce
    lz2 "ああいう輩はただの噂好きなのよ。ね～"
    show SCG_101 at bounce
    lz1 "ね〜"
    show SCG_102 1 with fastdissolve
    show SCG_102 at bounce
    lz2 "で、きみたちの方はお仕事どうだった？タイヘンでしょ～"
    pl "想像以上っていうか…あんなん慣れられるかっての。"
    show SCG_101 0 with fastdissolve
    lz1 "知らないわよ、そんなの。こっちだって未だにキツいんだもの。"
    lz1 "ここの枢機卿、ほんとアタマおかしいんじゃない？こんなトチ狂った部署なんか建てちゃって。"
    nar "俺の分として寄こされたサンドイッチは俺が今まで見てきた中でも最悪のサンドイッチだった。"
    nar "冷たく堅いパンに、肉の欠片すらない上正体不明のソースが適当に塗られている。"
    nar "おまけに挟まっている唯一の具であるレタスすらどれだけ放置してたのかゴムみたいで噛みづらい。"
    hide SCG_101
    hide SCG_102
    show SCG_02 0
    with dissolve
    my "たったのこれだけ…？"
    nar "俺より先にマヤが口を開ける。"
    hide SCG_02
    show SCG_101 0 at left
    show SCG_102 0 at right
    with dissolve
    lz2 "牛乳もあるけど？"
    pl "いやいや、これっぽっちで腹を拵えるかよ！"
    show SCG_101 2 with fastdissolve
    lz1 "うるっさいわね！グチグチ言うんじゃないわよ！子供じゃあるまいし！"
    show SCG_101 0 with fastdissolve
    lz1 "アンタたちが騒がなくたって皆同じ気分なのよ！黙って食べなさい！"
    pl "ぐぇ…"
    hide screen textbox with dissolve 
    hide SCG_101 0 at left
    hide SCG_102 0 at right
    with dissolve
    show screen textbox with dissolve   
    nar "言いたい文句なら山々だが、不服ながらも仕方なくパンを無理矢理噛み砕く。"
    nar "そうして些細な会話と共に食事と呼ぶには冒涜的とも思える時間は過ぎていった。"
    hide screen textbox with dissolve 
    show SCG_02 0 at left
    show SCG_102 0 at right
    with dissolve
    show screen textbox with dissolve    
    my "あのぉ……"
    lz2 "ん？"
    my "シーキュレットくんはどんな子なのかなぁ…って…{w}さっき先に行っちゃったの…"
    hide SCG_102 0
    show SCG_101 2 at right
    with dissolve
    lz1 "アンタねえ！{w}ああ嫌だ、食欲が減ってきたわ。"
    show SCG_101 0 with fastdissolve
    lz1 "マヤ、アンタさぁ…{w}あのクソ男にもしかして気があるんじゃないわよね？"
    show SCG_02 6 with fastdissolve
    my "そ、そんなんじゃないもん"
    pl "アイツって何歳なんだ？やけに小さいし……てかそもそもあいつって男なのか？"
    hide SCG_02
    hide SCG_101
    show SCG_102 1
    with dissolve
    lz2 "きみと同い年よ。{w}最近は見ないような独特な雰囲気よね？聖痕も３つなんだって。"
    show SCG_102 0 with fastdissolve
    lz2 "ここには同じ修道院で育った人ばっかだから大体知り合いなのに、彼だけは皆初めて見る顔らしいの。"
    show SCG_101 0 at left
    show SCG_102 4 at right
    with dissolve
    lz2 "州都出身、とは聞いたけど一体何してた子なんだろうね。"
    show SCG_101 3 with fastdissolve
    lz1 "あ～嫌だ嫌だ！病なんかでも移っちゃったらどうしようかしら！{w}あ、もしかして、だから人とくっつかないのかも。"
    nar "さっきまでは大人しかった二人の表情がまたコロコロと変わる。{w}そんなに面白い話なのか？付いていけなくてボーっとしてきた。"
    hide SCG_101
    hide SCG_102
    show SCG_02 7
    with dissolve
    nar "未だ初めて会った時と変わらない、ずっと泣きそうな顔のまんまのマヤと二人の顔が対になる。"
    show SCG_02 0 with fastdissolve
    nar "マヤはこの流れに困ったのかまた口ごもってしまった。"
    hide SCG_02
    show SCG_101 0 at left
    show SCG_102 1 at right
    with dissolve
    lz2 "でも、ここで随分働いたらしいし。面倒事押し付けるには丁度いいよね。"
    show SCG_101 3 with fastdissolve
    lz1 "そうそう、さっきの朝みたいにね。{w}そういうヤツを相手する時は先に押し付けちゃった方が勝ちだもの。"
    show SCG_101 0 with fastdissolve
    lz1 "…あぁ…{w}もちろんアンタたちが面倒だったって訳じゃないけど、{w}ほら。わかるでしょ？"
    show SCG_02 6
    hide SCG_101
    hide SCG_102
    with dissolve
    my "先任なんだ…"
    pl "へなちょこ野郎にしてはやるな。"
    show SCG_02 6 at left
    show SCG_102 1 at right
    with dissolve
    lz2 "マヤちゃんはカワイイからさ、意外とグイグイいっちゃえば食い付かれるかもよ？"
    show SCG_02 0 with fastdissolve
    my "そ、そんなぁ…"
    show SCG_101 2 at right
    hide SCG_102
    with fastdissolve
    lz1 "ちょ、何変なこと教え込んでるのよ！"
    show SCG_102 1 at right
    hide SCG_101
    with fastdissolve

    lz2 "年下がタイプかも知れないじゃん？{w}だって、男ってどーせみんな"
    hide screen textbox with dissolve
    show SCG_102 4 with fastdissolve
    nvl clear
    show screen nvlbox with dissolve
    "\n 「―{space=-3}―{space=-3}―の―{space=-3}―{space=-3}―だから。」"
    "金髪女が前屈みになってマヤの耳元に囁く。{w}すぐ隣に居た委員長がそれを聞いたのかマヤと一緒に目をまんまるにして驚いていた。"
    "「やめなよぉ」笑いの混じった声で肩を軽く押しのける。{w}二人はまた俺の目の前でケラケラと笑い始めた。 "
    "わざと声を小さくしたのだろう。唇が目の前で動いたのにも関わらず、俺は彼女が何を言ったのかが読み取れなかった。"
    "「あは、は…」でも正直、雰囲気からして何となくならわからなくもない。{w}可哀想なマヤはまた困惑したような顔で愛想笑いする。"
    et "何で俺の前でこんな事をしてるんだろうか。{w}もしかして、俺って忘れられてる？"
    nvl clear
    "\n そんなどうでもいい事を考えていると、笑う彼女と目が合う。{w}すぐ隣の女も彼女の肩に寄り添っては目を細くしてこちらを見つめていた。"
    "クスクス……さっきの大笑いとはまた違う笑い声。{w}\nそこで俺は確信した。{w}これは偶然だったり、何かの手違いでもなく、真っ直ぐ俺に向けられた嗤いだった。"
    et "この全てが俺に対する何かしらの警告なのだろうか？{w}それ以上は考える間もなかった。{w}遠く向こうから鐘の音が響いた途端、彼女たちは冷めきった顔に戻ってしまったのだから。"
    hide screen nvlbox with dissolve
    hide SCG_02 with dissolve
    show SCG_102 0 at right
    show SCG_101 0 at left
    with dissolve
    show screen textbox with dissolve
    lz1 "あ～あ、嫌ね…また仕事に戻らないと"

    hide SCG_102
    show SCG_02 0 at right
    with fastdissolve

    my "あれ、お昼の時間終わっちゃったんだ…"

    hide SCG_02
    show SCG_102 1 at right
    with fastdissolve

    lz2 "あたしも研修生に戻りた～い！"

    show SCG_102 0 at right
    with fastdissolve

    pl "行っちゃうのか？"
    lz1 "そんなヒマだったらここ周辺でも回ってみたら？"
    lz1 "そうして慣れておかないとまたすぐに道に迷っちゃうわよ。{w}神殿は超～広いからね！"
    show SCG_02 0
    hide SCG_101
    hide SCG_102
    with dissolve
    my "はあぁ…"
    hide SCG_02
    show SCG_101 0 at left
    show SCG_102 2 at right
    with dissolve
    lz2 "じゃ、カワイ子ちゃんたちは後でね～"
    pl "おう、そっちも仕事頑張れよ！"
    hide screen textbox with dissolve
    hide SCG_02
    hide SCG_101
    hide SCG_102
    with dissolve
    pause 1
    if hssh_rkn == True:
        $ save_name = "day 1, 昼, 楽園"
    else:
        $ save_name = "day 1, 昼"
    jump placemenu
    return

label day1_hakuB_:
    show screen place_day1_hkB
    show screen place_hkB
    with None
    hide screen place_hkB
    hide screen place_day1_hkB
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg101_1 with dissolve
    else:
        scene bg101_2 with dissolve
    call place00 from _call_place00
    play music "audio/SE/prologue wind.ogg" fadein 30
    show screen nvlbox with dissolve
    "\n 青黒い空の色が溶け込んだ空気は冷たいばかりだった。{w}州都の方は寒いはず、とは聞いたがまさかこれぐらいだとは。"
    "もう夜なのか、それとも逆にもう朝なのか。{w}今朝からずっと暗いまんまの空じゃ何も分かりやしなかった。{w}目の前がだんだん暗くなってくると考えないよう蓋をしていた不安が底から這い出てくる。"
    "「まさか…道に迷ったとか」"
    et " 多分最初居た場所からそこまで離れた所ではないはず。{w}しかし舗装もされていない草木の茂る深い道は俺を怖がらせるには充分だった。"
    nvl clear
    "\n あっちゃぁ…俺は口から失態をこぼしては自分の後ろ頭を搔き乱す。{w}こうしていてもしょうがないので来た道を戻ろうと後ろを向くと、向こう側に建物のようなものが見えてくる。"
    "デカデカと張り付けられたガラスの窓に、縦に細長い形状の塔にも似たなにか。{w}俺の見間違いじゃなけりゃこれは礼拝堂のように見えた。{w}…が、何か妙に感じる。"
    et " 雑草ばかりが沢山生え出ているこんな野外に、その建物だけがまるで捨てられた廃墟のようにその地を占拠していたのであった。"
    nvl clear
    "\n 近寄って確認するもやはり人の気配はない。{w}濁った映りの窓に、腐り落ちた壁を食い散らかすように生えたツタの葉。"
    "やっぱり、使われている建物のようには見えない。"
    stop music fadeout 3
    "ザッ…ザッ…土と砂粒が擦れる音が聞こえる。{w}山獣だったらマズい。{w}俺は急いで物陰に体を潜め音のする方向に目を見やる。"
    "驚くことに、目線を動かしたその先には一人の人が佇んでいた。{w}見間違いなんかじゃない。"
    et "それもそうだ、こんなに真っ暗な夜空の下で、その人だけが真っ白な光を放っていたからだ。"
    hide screen nvlbox with dissolve
    show story04 with slowdissolve
    pause 2
    play music "audio/bgm/haku.ogg"
    nvl clear
    show screen nvlbox with dissolve
    "\n 白髪を一本に結んで薔薇の飾りを付けた人。"
    "その白い光は暗い場所にそぐわずあまりにも異質すぎて、反ってこの空間を支配するかのように目線を集中させる。{w}俺は、今までこんな人に出逢ったことがなかった。"
    "しかしその表情があまりにも冷たかったためか、人間的な面で好感を持つには難しかった。"
    et "性別すら測れない彼は繊細に飾られている広い袖をなびかせ、暗い顔で雑に散らばったまま生えている草花の周りを歩く。{w}見れば見るほど人というよりかは、一種の良く造られた芸術作品のようだった。"
    nvl clear
    "\n マズい、いくら何でも見つめすぎたか。{w}ふとした瞬間、彼が目を鋭く細めこちらへと顔を上げる。"
    "俺は目が合う前に咄嗟に座り込む。"
    "今、何で避けたんだ？"
    "途端に緊張感で胸が千切れそうになる。"
    et "自分の心音に、響く夜虫の音が余計大きく聴こえてきた。"
    hide screen nvlbox with dissolve
    pause 1
    hide story04 with dissolve
    pause 1
    nvl clear
    show screen nvlbox with dissolve
    "\n 短い静寂の時間が流れ、向こうから歩き去る音が聞こえる。{w}さっきまであんなに寒かったはずなのに、今じゃ冷や汗が流れ落ちるぐらいだ。"
    "そっと地面から起き上がって彼の居た場所へと目線を送るも既に去ってしまったのか誰もいない。"
    "立ったまま夢でも見た気分だった。"
    $ _skipping = False
    et "今から戻ってもまだ寮に間に合うだろうか？{w}…本当に目が眩む前に早く戻った方が良さそうだ。"
    hide screen nvlbox with dissolve
    nvl clear
    stop music fadeout 5
    hide screen keymap_screen
    $ _game_menu_screen = None
    $ show_quick_menu = False
    hide screen at_frame
    scene black
    with slowdissolve
    $ _dismiss_pause = False
    pause 6
    jump day2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
