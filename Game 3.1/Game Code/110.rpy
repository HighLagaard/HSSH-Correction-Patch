label day10:
    $ day = 10
    $ save_name = "day 10, 朝"
    $ renpy.music.set_volume(1, channel="sound")
    play sound 'audio/SE/bell 2.ogg'
    image 10day = Text("day 10",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '10day' at day00 with slowdissolve
    pause 5
    hide expression '10day' with slowdissolve
    stop sound fadeout 1.0
    pause 1.0
    show screen at_frame with dissolve
    scene black with slowdissolve
    pause 1
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    $ _game_menu_screen = 'preferences'

    scene bg102_1 with slowdissolve
    call place102 from _call_place102_10
    show screen nvlbox with dissolve
    "\n 哀歓を共にする声があちこちから聞こえてくる。"
    "神殿の中で行われたささやかな葬式は、彼たちの没前の業に比べれば驚くほどに空ろだ。"
    "葬式が外で行われなくて良かった。{w}黒服の人々が一斉に真っ暗な空の下で真っ黒な傘を持っている光景は、想うだけで気が滅入ってしまうからだ。"
    "幾つかの蝋燭が燃え、重い棺の周りに白い百合が何輪か投げられたが、彼たちの死体はあれの中には入っていない。"
    "事件の終わった後、俺たちは神殿の他の司祭と共に再びあの場所を訪れた。"
    et "しかし残った死体はもう崩れた残骸に押し潰され、そしてあの残骸さえも水に溶けて本来の形を失っている。"
    nvl clear
    "\n 多くの人がほぼ一日中歩き回ったが、結局見つかったのは全てを失ったという確信だけだった。"
    "だからあれはこの場を守る為の単なる飾り物に過ぎない。空っぽの棺の前にわざわざ聖水を注ぎたくはない。"
    "だから俺はどんな真似もせずに、もう小さな額縁の中で写真だけに存在する姉さんをそっと見上げながら、只生をすっかり奪われたという虚しさを感じていた。"
    "色々なことを思い出したがほとんどは長く浮かばずに、薄暗い頭の中で脆くも消えてしまう。"
    "瞬くことを忘れたままで開いた乾いた目からはまだ涙一滴も落ちていない。"
    et "一朝にして行き場と為すことを全部失った事実にまだ実感が湧かない。"
    show black
    hide screen nvlbox
    with dissolve
    nvl clear

    "\n エルジェーベト主教は葬場に現れなかった。事実、事件が起きてから俺はわざと彼と出会うことを避けている。"
    "こうなった時まず最初に心配したことは正に彼たちの反応だった。"
    "家族としての絆を持った彼たちならかんかんになって、俺にも責任を問うと思っていたからだ。"
    "しかしそれは俺だけの想像だった。{w}いきなりの事故に思考が止まったりしたか、どれだけ時間が過ぎても先に俺にやってくる人はいなかった。"
    "勿論俺も傷心を持っているが、あの人たちの前ではその悲しみは一瞬でふざけたことになってしまう。{w}それが嫌だ。"
    et "結局最後まで俺は部外者で、俺の方から一方的に距離を置いていたって勝手に誤解していただけだ。"
    nvl clear
    scene bg03_1 with slowdissolve
    call place03 from _call_place03_25
    show screen textbox with dissolve

    play music "audio/se/tutorial walking.ogg"
    nar "燃え上がる蝋燭の香りと祈り声に感情は更に落ち着いていく。"
    nar "外へ繋がる通路、並んだ椅子の中で一所に、綺麗な服を着た彼が座っている。"
    nar "夜明かししたせいでとろんとした彼の姿は見慣れない。{w}彼は俺を見て目尻を顰めて、すぐため息をつく。"
    show SCG_08 9 with dissolve
    en "…何てザマなんスか。"
    pl "しょうがないだろ、あんなことがあったんだし…人も大分減ったよ。"
    en "違くて、そっちの話ッス。{w}事故で怪我しちまったんでしょ。"
    nar "可笑しい話だ。{w}彼の言葉を聞くまでは俺は自分の体に傷が付いていたってことを知らなかったからだ。"
    nar "ゆっくりと腕を上げると、正に包帯に赤黒い血が干上がっている。"
    nar "まるで嘘みたいに刻まれた傷は今になって苦痛をさんと感じ始める。"
    nar "俺はじんじんする腕からできる限り力を抜き、再び彼に話しかけた。"
    pl "小さすぎたんじゃないかな、この葬式。"
    show SCG_08 8 with fastdissolve
    en "これぐらいで丁度いいッスよ。"
    en "やたらとでっかく行ってもアルタナータ家の若娘が死んだからにはオブラートを用意していかねば、"
    en "なんてほざく爺共の薄汚いジョークなんかを聞かされてたでしょうね。"
    nar "彼はこちらを見つめもせずに答える。両手は整然と集まっている。"
    nar "祈りでも捧げていたのか、もしくは告解か？"
    pl "姉さん、俺たちのことを憎んでるのかな。"
    show SCG_08 10 with fastdissolve
    en "姉上は憎んだりなんかしないでしょうね…"
    show SCG_08 9 with fastdissolve
    en "憎めるほど僕らに頼ってなかったんだし。"
    hide SCG_08 with dissolve
    nar "恐らく俺はまだ、もう一度だけ魔法のようなことが起きてくれないかと期待しているんだろう。"
    nar "只周りの環境が変わっただけで俺自身が変わってしまったように。"
    nar "神殿にはまだ俺の知らない多くの知識と技術があるから、"
    nar "少し時間が過ぎれば誰か俺では想像もつかない仕方を見つけてくれないだろうか。"
    nar "まだあの時の記憶は微かで、相変わらず悪夢でも見ているような気分だ。"
    nar "だからこそ俺はどんなきっかけも努力もない、突然現れる奇跡を今も心のどこかで願っている"
    hide screen textbox with dissolve
    scene bg14_1 with slowdissolve
    call place14 from _call_place14_9
    show screen textbox with dissolve

    nar "場を離れた俺は、あてもなく神殿の中を彷徨った。{w}正直、ひどく落ち込んでいる人の相手をするのは苦手だ。"
    nar "今は神殿のどこに行っても特有の鬱な雰囲気が広がっていて、まるで行き場を失った気分だ。"
    nar "人のいない部室は静かだ。{w}今度の事故で人員を失ったのは魔導部だけでなく、浄化部も同じだった。"
    show SCG_05 B 000 with dissolve
    hk "[na]兄弟でしたか。"
    pl "うん。忙しかったか？"
    hk "然うですね。これから如何にしてこの穴を埋め合わせていけば善いものか。"
    hk "死体も彼の様な状態では兄弟もさぞ傷心された事でしょう。"
    pl "マヤは？"
    hk "シーキュレット兄弟の看病の為神殿病棟に行かれました。"
    pl "まだ起きてないのか？"
    show SCG_05 9 with fastdissolve
    hk "アレはもう死んだも同然と考えた方が御心境にも宜しいかと。"
    hk "今度マヤ姉妹に御会いになりましたら彼女にもそう伝えて下さい。"
    pl "そっか。"
    show SCG_05 000 with fastdissolve
    hk "彼女は最期に何と仰いましたか？"
    nar "アル姉は…"
    pl "俺は…知らない…聞いてなかった。"
    show SCG_05 9 with fastdissolve
    hk "ふぅん。"
    show SCG_05 0 with fastdissolve
    hk "然様ですか。"
    hide SCG_05 with dissolve
    nar "彼女も何も言わず俺のそばを過ぎて行く。{w}なんでここにいるんだ、俺は。{w}俺は…"
    nar "一体何なんだ？"
    pl "……"
    nar "彼女がすれ違った瞬間、ふと花の香りのような何かが鼻先を掠めた。"
    nar "どこかで吸ったことのあるような、その仄かな香水の匂いはきっと生まれて初めて吸う不慣れの香りで、"
    nar "この場所とは合わないものだった。"
    nar "その違和感は又別の違和感を生む。どうしていきなりこんなことが起きてしまったんだ？"
    nar "神に人間を返すこと、消えていく天と地、天罰の時。"
    nar "あの夜、「彼」から聞いた言葉が空いた頭の中で燻って、肝を冷やしてしまう。"
    nar "禍はもうあの時から、いや、その前から隣に宿っていたって訳ではないか。"
    hide screen textbox with dissolve
    pause 1
    scene bg03_1 with slowdissolve
    call place03 from _call_place03_26
    show screen textbox with dissolve
    nar "何気なく足を向けた神殿の病院。遠くから慌ただしい音が小さく鳴る。"
    nar "この扉を開いて入れば、忙しく働く保健部の人たちと、ベッドの上で死んでいく司祭たちで一杯だろう。"
    nar "俺はそれと向かい合うのが怖くて静かなところでひそかに歩きを止めた。"
    nar "誰もいない静かな廊下。その真っ白な道の向こうからマヤがよたよたと歩いてくる。"
    nar "ずるずると引かれているような足音が珍しく感じられて又良く見れば、病院のスリッパを履いている。"
    pl "マヤ？"
    show SCG_02 A 1 100 with dissolve
    nar "俺が名前を呼ぶと、俺を見つけた彼女は顔を上げてしばらくそのまま立ち止まって"
    nar "口と目尻だけをそっと動かしてにこっと笑顔を見せた。"
    nar "小さく俺の名前を呼んだ気がするが喉が渇いたのか声が出ない。"
    pl "マヤ？"
    show SCG_02 0 with fastdissolve
    my "あのね、死んだよね？"
    pl "うん？"
    my "アルネさん死んじゃったよね？"
    pl "あ？"
    my "アルネさん死んじゃったよね？"
    nar "何言ってるんだ？"
    my "アルネさん死んじゃったよね？"
    pl "うん。"
    my "アルネさん死んじゃったよね？"
    pl "うん、死んだ。"
    nar "死んだんだ。"
    my "アルネさん死んじゃったよね？"
    pl "死んだ。"
    nar "アルネ姉さんが死んだ。"
    my "アルネさん死んじゃったよね？"
    pl "死んだよ。"
    nar "アルネ姉さんは死んだんだ。"
    show SCG_02 00 with fastdissolve
    my "…泣いてるの？"
    nar "アル姉は死んだ。{w}もう彼女の傍にいてあげられない。"
    nar "俺は姉さんが死ぬことを只見ていただけだ。{w}俺は姉さんの最後の言葉さえも聞けなかった。"
    nar "あれは俺が防げたかもしれない。"
    nar "もし俺があの時気を付けろって言ってあげたら、もし俺があの時慢心していなかったら、しかし本当にそうできたんだろうか？"
    nar "いや、できなかったんだろう、俺は。"
    nar "マヤは萎れた花が蕾を落とすように俺の懐に弱く倒れた。{w}手で包んだ背は数日前よりも更に痩せこけたと感じられる。"
    show SCG_02 1 with fastdissolve
    my "[na2]くん。"
    my "[na2]くんだけは、ずーっと、わたしと一緒だよね？"
    nar "胸の中から俺の名前を呼ぶ彼女は、この世で一番愛らしい。{w}彼女の傍にいよう、そうすればもう大丈夫だろう。"
    nar "俺たちにとってお互いがいて良かった。ありがとう。{w}ありがとう。"
    nar "…ありがとう、マヤ。"
    hide SCG_02 with dissolve
    $ _skipping = False
    pl "何か、望むものってあるか？"
    hide screen textbox with dissolve
    pause 2
    nvl clear
    stop music fadeout 2
    scene black with slowdissolve
    pause 2
    jump day11
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
