label day5:
    $ day = 5
    if hssh_rkn == True:
        $ save_name = "day 5, 朝, 楽園"
    else:
        $ save_name = "day 5, 朝"
    play sound 'audio/SE/bell 2.ogg' fadein 2.0
    image 5day = Text("day 5",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '5day' at day00 with slowdissolve
    pause 5
    hide expression '5day' with slowdissolve
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
    if hssh_rkn == True:
        show screen nvlbox with dissolve
        br "\n ふと気が付けば見慣れた空の下だ。{w}足首を握ったどろどろの泥。腐った内臓の臭いのせいで頭が壊れてしまいそうだ。{w}{nw}"
        extend "\n誰の物か知らない反物が頭の上にべとべとに振りかかる。夢だ。あの夢だ。{w}{nw}"
        extend "天使の夢だ。暗い部屋に仄かに光が入って、やがて開いた扉がこっそりと閉まる音がした。{w}{nw}"
        extend "その束の間の光が俺には明るすぎた。彼女が来たのだ。{w}純白の羽を羽搏きながら目が痛くなるほどの光を背にして、俺に細い腕を伸ばす天使。"
        nvl clear
        br "\n きっと綺麗で清廉な姿なのに、この場所の特有の腐った臭いが酷い。{w}{nw}"
        extend "\n彼女は天使だ。本来なら触れるどころか、目を合わせることさえも許されない圧倒的な存在。{w}{nw}"
        extend "俺たち二人の世界はそうやって完成された。{w}{nw}"
        extend "\n\n「[na2]くん、わたしと一緒に暮らそう。{w}{nw}"
        extend "\nもうお外なんていかなくてもいいの。{w}{nw}"
        extend "\n分かりたくもなかった真実を脳みそにたたき込む必要だってない。{w}{nw}"
        extend "\n腐りかけの腕なんてもういらないわ、嘘ばっかり行き来することばもいらない。」{w}{nw}"
        extend "\n「何故ならこれからわたしがずっとそばにいてあげるから。」"
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
        br "\n 嗚呼、いかほどに慈悲深い人か。その温気はきっと俺が長くも避けてきて、又望んできたものだった。{w}{nw}"
        extend "唇が重なり、ぬるい舌と共に口に生ぬるい液体が流れ込む。喉の下に流した液体から鉄のような生臭い臭いがした。{w}{nw}"
        extend "頭の上に広がった天使の羽が俺の視野に暗い陰を作り出す。見上げた彼女が訳もなく遠くいるように感じられた。{w}{nw}"
        extend "\nそのくらくらしてしまう距離の視界に、濃鼠に輝く光が入ってくる。{w}{nw}"
        extend "\n俺はそれが救いだと信じて目を閉じた。純白の彼女に血液が散る。"
        nvl clear
        br "\n しかし彼女の笑顔だけは何の汚れもなく、俺に差し伸べた手は引かない。{w}{nw}"
        extend "\n痛みは感じられなかった。心の臓は多く流した血を再び補うように淀みなく鼓動して、{w}{nw}"
        extend "\n熱い心臓を動かす脳も劣らずに、今すぐでも融けてしまいそうに熱い。"
        nvl clear
        hide screen grumble_cg08
        hide screen nvlbox
        show cg08 onlayer screens:
            yoffset -500
            ease 4.5 yoffset -400
        with dissolve
        pause 2.5
        nvl clear
        hide cg08 onlayer screens
        show screen grumble_cg082
        show screen nvlbox 
        with dissolve
        br "\n 部屋を満たした熱気のせいで目がぼんやりしてきた。{w}{nw}"
        extend "\nしかし彼女に全てを捧げるには未だこの身体は重すぎる。{w}{nw}"
        extend "\n曇った視界が段々暗くなる。開いた目の前にはまだ天使がいる。{w}{nw}"
        extend "\n脳に染みるその光は目を閉じても消えずに俺の中でいつまでも燦々と輝いていた。"
        hide screen nvlbox
        stop music fadeout 3
        hide screen grumble_cg082
        hide screen TrackCursor
        scene black
        with slowdissolve
        pause 2
        with dissolve
    else:
        show screen nvlbox with dissolve
        br "\n 今日の夢は何故か少し変わった夢だった。{w}{nw}"
        extend "\n相も変わらず膿んだ水の滴る内臓だらけの空間。しかしその死体の山に立っているのは俺ではなかった。{w}{nw}"
        extend "誰かがそこに立っていたようだが、間もなくして無数の死体の内の一つと成り果てる。{w}{nw}"
        extend "べったりとした水が滴り作られた穴からは規則的に粘りのある泡が上がってくる。{w}その様子を俺は遠く離れて見守っていた。"
        nvl clear
        br "\n 周りを見渡しても腐った肉片ばかり。{w}生きている人間など居ない。{w}皆何処へ行ってしまったのだろうか。{w}俺はなぜこんなところに一人佇んでいるのだろうか。{w}{nw}"
        extend "\n考えても思い当たる節はない。{w}俺はこの状況にすっかり疲れきってしまった。{w}{nw}"
        extend "ただ突っ立っては真っ赤な地面を眺める。{w}そしてゆっくり、一番近くに落ちてきた死体へと近寄った。{w}血の泡からは酸っぽく生臭い臭いがしていた。{w}{nw}"
        extend "その死体に微妙な動きが生じた気がして、俺はズレてボケたピントを合わせるため目を細くしてもっと寄る。{w}{nw}"
        extend "その顔を確認する為だった。"
        nvl clear
        br "\n しかし直に受け入れがたい光景が目の前で繰り広げられる。{w}動いてると思っていた死体の腹が膨れ上がったのだ。{w}{nw}"
        extend "もしかして雨が降ったからか？その腹はまるでカエルの鳴き袋の如く膨張しては、やがて目の前で破裂する。{w}{nw}"
        extend "息を呑もうとするもそうにもいかない。{w}既に俺の顔や頭、胸にその腹から飛び散った汚物に塗れていたからだ。{w}{nw}"
        extend "\n俺は濡れた前髪の先からドロッと零れた何かの塊に視界が塞がり悲鳴を上げる。{w}滑る地面を蹴り飛ばしながらただ走った。{w}{nw}"
        extend "\n目玉は誰かを探すように忙しく回る。{w}天使。{w}天使がまだ来ていない。"
        nvl clear
        br "\n 俺は重ねた自分の手を祈るように空へと掲げる。{w}心の底から天使の再来を願った。{w}天使が来てくれない以上俺はこの夢から醒めることが出来ないから。{w}{nw}"
        extend "\n空はまだ暗く、光の一筋すら掛らない。{w}俺は彼女が訪れ早くこの恐ろしい悪夢を終わらせてくれと何度も祈った。{w}{nw}"
        extend "\n自らの意志で天使を探していたのだ。"
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
        br "\n それは元より祈る者にのみ与えられるものなのか、永遠閉じたままかと思えた暗い空が二つに分かれ、そこから溢れ出す眩い光が閉じた眼を開かせる。{w}{nw}"
        extend "\n彼女が現れたのだ。{w}純白の翼を広げ目が痛むほどの光を背負いつつ俺にか細い腕を回す天使。{w}{nw}"
        extend "\nきっと美しく、清楚そのものである筈なのにこの場所特有の腐った臭いが充満していて邪魔をする。{w}{nw}"
        extend "\n湿った壁に添った背中は小さい蟲でも這いずり回っているのか至る所が痒い。{w}{nw}"
        extend "\n壁から離れると直ぐ目の前に天使が居る。{w}その温かさはきっと俺が長らくずっと避け続け、また求め続けてきたものだ。{w}{nw}"
        extend "\n本能的な憂苦が脳を蝕む。"
        nvl clear
        hide screen grumble_cg08
        hide screen nvlbox
        show cg08 onlayer screens:
            yoffset -500
            ease 4.5 yoffset -400
        with dissolve
        pause 2.5
        nvl clear
        hide cg08 onlayer screens
        show screen grumble_cg082
        show screen nvlbox 
        with dissolve
        br "\n 彼女は天使。{w}本来なら触れることも疎か、目を合わせることすら許されない筈の圧倒的な存在。{w}{nw}"
        extend "\nそんな彼女の手が俺の身体を撫でる。{w}{nw}"
        extend "\nお前は誰なんだ、何故彼女の顔をしているんだ？{w}甘ったるい息を呑むと脳を震わせる程の光が目を眩ませた。{w}{nw}"
        extend "\n押し寄せる吐き気に耐えきれなかった俺は粘り気のない胃液を吐き出す。{w}俺から噴き出た不潔は彼女の美しい衣服を汚し、{w}{nw}"
        extend "髪の毛に粘り付いては酷い惨状を作り出した。{w}しかし彼女の笑顔だけは一片の汚れなく、俺へと差し伸べた手を引くことはない。"
        nvl clear
        show bgw onlayer screens
        hide bgw onlayer screens with dissolve
        br "\n 嗚呼！こんなにも汚れた俺を嫌味一つなく抱きかかえてくれるなんて。{w}なんて慈愛の有る人なんだろう。{w}{nw}"
        extend "\n俺はぶるぶる震える手を恐れ多くも彼女の背に回す。{w}彼女を受け入れる。{w}抱き返したのだ。{w}{nw}"
        extend "\n「大丈夫。」俺の頭をなでる優しい指先。{w}残酷なぐらいに優しい声。{w}彼女は俺を受け入れてくれる。{w}{nw}"
        extend "\nこのまま永遠に彼女の御許で沈んでいられると言うのなら、俺は喜んでこの身を彼女に差し出す。{w}温かさと、重い心臓の鼓動音。{w}{nw}"
        extend "\n飲み込まれる様な感覚。"
        hide screen nvlbox
        stop music fadeout 3
        hide screen grumble_cg082
        hide screen TrackCursor
        scene black
        with slowdissolve
        pause 2
        with dissolve
    if hssh_rkn == True:
        scene bg10 with dissolve
    else:
        scene bg10_1 with dissolve
    pause 2
    show screen nvlbox with dissolve
    nvl clear
    "\n 朝。{w}目覚めてすぐ震える両手を目前に差し出した。"
    "ずっと握りしめていた掌からぬるい水気がする。{w}俺はまだ夢の中で迷っているような気がする。{w}薄暗い視界に鮮紅色の内壁がちらちらする。"
    et "多分昨夜の事件のせいだろう。"
    nvl clear
    "\n 頭の中でここ数日の記憶が混ざり始め、しっかりする為に何度も強く首を横に振った。"
    "服の中に吹き込んだ空気が冷たくて布団の中に入ってしまう。{w}今は何時だろう、人の犇めく声が耳に障る。"
    "しかしこれは可笑しい。{w}耳を塞いでいるのに騒めきが止まらない。"
    et "この声がどうしても 神経に障っただろうか、頭がずきずきして痛くなる。"
    nvl clear
    "\n 俺はしばらく、布団の中にいて気付いた。{w}これは頭痛からの幻聴だ。"
    "体は寒いのに眩暈のする頭だけが熱い。気のせいか焦点も合わない。{w}俺は力の入らない脚を振ってベッドから降りた。"
    et "この瞬間だけは、孤独でいることが辛くてならない。"
    hide screen nvlbox with dissolve
    call place10 from _call_place10_4
    $ show_quick_menu = False
    show screen morning with fastdissolve
    $ renpy.call_screen("morning")
    if hssh_rkn == True:
        scene bg14 with dissolve
    else:
        scene bg14_1 with dissolve
    call place14 from _call_place14_4
    pause 1.0
    show screen textbox with dissolve
    nar "部署の空気はヘンだ。{w}ひときわ静かだけど、いつもよりも妙に浮き立った雰囲気のせいでさらに騒がしく感じられる。"
    nar "まだ仲間の血を目にした興奮が沈んでいないようだ。"
    nar "誰もが人の死体を片付ける立場であるくせに、人の首を絞める事件に興味を持つ。"
    nar "人はいずれ死する。{w}当然なる事実であろうとも、ここの人はたまにそれをすっかり忘れているように見える。"
    nar "だからこんなにも喜んで、恐れているんだろう。"
    show black with dissolve
    nar "……"
    nar "脳内で事件は続く。あの女の顔が浮かぶ。"
    nar "余裕な目笑の顔は醜く歪んだ表情になり、黒のマニキュアを塗った長い爪は割れ、"
    nar "汗の染み込んだ重たい肌の匂いは、爪印が押されて焼ける匂いに替える。{w}訳が分からなく反吐が出る。"
    hide black with dissolve
    show SCG_02 idle with dissolve
    play music "audio/bgm/daily.ogg" fadein 2
    my "おはよう、[na2]くん。今日は早かったね…"
    pl "あぁ…まぁな。{w}俺だって毎日遅れてばかりってワケじゃねえんだ。"
    nar "今日は夢見が悪くて、あの部屋にいる気がしない。"
    nar "まだ夢で見た彼女の暖かさを覚えている。{w}柔らかな手、優しい声。"
    nar "夢の余韻は容赦なく現実に落ちてしまった俺に、さらに大きい虚しさを与えてくれた。"
    nar "一人きりの時間は俺の気を狂わせる。{w}しかしこんなことをマヤには言えない。"
    nar "俺は慎重に視線を逸らして話の種を探る。"
    pl "…今日は一人なのか？"
    show SCG_02 8 with fastdissolve
    my "うぅん…ちがうよ。向こうに…"
    hide SCG_02 with dissolve
    nar "マヤの声が妙に小さくなる。{w}その視線を追ってみれば短髪の女性が座っている。"
    nar "いつもとは違く、しょんぼりして肩を落とした姿を見れば何故か痩せこけたようにみえる。"
    nar "多くの人が彼女を通り過ぎながらひそひそと話していたが、そういう周りの視線を気にせずに、"
    nar "彼女はちらっと見た目にも魂が抜けている。"
    nar "俺はマヤと不安の視線を交わした。"
    show SCG_02 8 with dissolve
    pl "そうだな、二人いつも一緒だったし…"
    nar "あの先輩はそうとは思わなかったようだが。"
    pl "…マヤは大丈夫なのか？"
    show SCG_02 0 with fastdissolve
    my "…わたしは…大丈夫なんだけど…おねえちゃんが心配なの…"
    pl "大丈夫だって。{w}気の強い人だし、ちょっと休ませておけばきっとすぐに元気出すって。"
    show SCG_02 7 with fastdissolve
    my "そうかな…"
    nar "マヤは俺の機嫌を窺っては口を噤んだ。やはり俺の状態を気にしているらしい。"
    nar "それをわざと言わないってことは昨日の事件を目にしたからだろう。"
    nar "俺が彼女のことを気まずいって思っていることを分かってから気配りをしているんだ。"
    nar "優しいな、マヤは。{w}しかしかつ不安になる。マヤはどこまで考えているんだろう。"
    hide SCG_02 with dissolve
    pause 1
    show SCG_05 1 with dissolve
    hk "おはよぉございますぅ～"
    nar "幸い、主教様が入ってきて不自然な空気の対話は続くこともなく終わった。"
    show SCG_05 0 with fastdissolve
    nar "挨拶されながら俺たちの前を通り過ぎる主教様は一瞬、俺の方へ視線を向ける。"
    nar "単なる勘違いかもしれないが、それだけで毛が立った俺は視線を避け席に座った。{w}重たいため息が漏れた。"
    hide SCG_05 with dissolve
    nar "近くで見た雀斑の女の状態は想像を超えるものだった。"
    nar "凝血がくっついて乾いた唇はがたがたと震えて、まるで幾日は飢えた人のように頬は凹んでいる。"
    nar "やはり挨拶をしても受けてくれない。{w}わざと無視していることではなく、まさに何も聞こえていないようだ。"
    show SCG_05 0 with dissolve
    hk "昨日はとても不幸な事故がございましたが…{w}皆さま、どうか今日もお勤めに集中できますよう。"
    hide SCG_05 with dissolve
    nar "人が減ったことを慰めてくる主教様。今はそんなこと言わないのが得なのによ。"
    nar "沈鬱の空気の中で息を殺して笑う者を見つける度に胸のどこかががたつく。{w}彼女の死をあざ笑っているのか。"
    nar "それとも、清廉なる主教の口から性交に関した言及があったことが滑稽なのか。"
    hide screen textbox with dissolve
    stop music fadeout 3
    pause 2
    show screen textbox with dissolve
    nar "蛻の殻になっても彼女は座ったまま全く動く気配を見せない。マヤは困惑が隠し切れない。"
    pl "おい…先輩？"
    nar "そんなマヤに代えて俺が何度も話しかけてみたら、彼女がこちらへ首を回した。{w}恐ろしいほどに暗い眼だ。"
    show SCG_101 1 with dissolve
    lz1 "向こう、見える？"
    nar "嗄れた声の彼女が指で前を指し示す。{w}そこには、勿論何もない。"
    pl "何もないけど…"
    nar "俺が先に口を開いたら彼女はもう一度、小さな声で、"
    lz1 "向こうに見える？"
    nar "同じことを問いかけた。{w}今度は俺も一緒に口を閉じた。"
    nar "なのに、彼女の指先と視線が前を向いたまま全く下がらないことが怖くて、結局もう一回同じ答えを言い出した。"
    pl "何もないってば…？"
    lz1 "そう？そう…"
    hide SCG_101 with dissolve
    nar "そしてまた口を結んだ。{w}マヤの顔は絶望的だ。ぶるぶると体を震わせ、やっと涙を堪えているように見えた。"
    show SCG_02 7 with dissolve
    my "おねえちゃん？"
    nar "震う声が彼女を呼ぶ。{w}返答どころか視線さえ合わないと、マヤは差し迫って彼女の肩に手を置いた。"
    show SCG_02 3 with fastdissolve
    my "おねえちゃん…？{w}おねえちゃん、おねえちゃん…！！"
    nar "女は妹の手にただ揺らされるだけだ。その姿はまるで藁人形だ。"
    hide SCG_02 with dissolve
    nar "気の毒になりそうなその瞬間、女性と共にしおしおと揺れた机を誰かが強く打ち下ろす。"
    nar "シーキュレットだった。"
    show SCG_03 0 at left
    show SCG_02 0 at right
    with dissolve
    play music "audio/bgm/securett.ogg"
    my "……"
    nar "驚いたマヤが手を引いて、女性は浮かんだ視線を彼の方へ移す。{w}シーキュレットの鋭い視線も彼女を見下ろしていた。"
    sc "主教様が呼んでるよ。"
    nar "案外それを聞き分けたか、女性はしばらくそのままじっとしていて、ゆっくりと体を起こした。"
    nar "そしてふらついた歩きで主教室へ向かう。{w}俺たちはその危うい後ろ姿をしばらくは黙って見守っていた。"
    show SCG_03 7 with fastdissolve
    sc "…今日は来ないだろうと思ってたけど。"
    pl "……"
    nar "そっと視線を逸らしたシーキュレットと目が合う。"
    nar "彼は今度も俺の視線を避けずに俺に向かい合わせ、しかも話しかけてくる。{w}俺はわざと返答をしないようにした。"
    show SCG_02 7 with fastdissolve
    my "あの…キューくん、おねえちゃんは…"
    sc "キミの姉は神殿を出て故郷に戻ることになるはずだよ。"
    show SCG_03 72 with fastdissolve
    sc "…いや、故郷になんて戻れないだろうね。{w}キミたちは「エルベット」だろ？"
    hide SCG_02
    hide SCG_03
    with dissolve
    nar "それを聞いてマヤは驚いた目を大きく開いた。"
    nar "事情の知らない俺であっても、さっきの発言が無礼だってことはすぐ分かる。"
    pl "この…テメェ、今度はマヤにまで嫌味を言うのか。"
    show SCG_03 72 with dissolve
    sc "ボクは大事な話をしようとしてるんだよ。"
    sc "マヤ・エルベット、ずっと見守ってきたけど…キミの職務遂行能力は最悪だ。"
    sc "その態度を直さない限りキミはこの神殿では絶対に生き残れない。"
    sc "先延ばしにしてキミにとって何一つ良い事なんてないだろうしね。{w}今日ついでにキミの姉と一緒に出て行ったらどうだい。"
    nar "彼の言葉が懐剣のようにマヤに降りしきる。{w}危うく手を挙げるところだったが、やっと我慢した。"
    nar "こいつは俺の癇に障るだけでなく俺からマヤさえも奪い取ってしまいたいってものか。"
    show SCG_03 8 with fastdissolve
    sc "…それでもずっとここに居たいなら早く準備して。今日はボクもやる事が…"
    pl "いや、わざわざ来てもらう必要なんてない。{w}そんなお忙しいのに新入りまで気遣える余裕なんてないだろ？"
    pl "もう五日目だ。いつもの仕事なら俺らだけでやってもいい。"
    nar "気まずく流れていた空気は重たくなり完全に止まった。{w}彼は動きを止め俺を見つめる。"
    nar "何か言いたいようだがそれはこちらも全く同じだ。{w}退く気なんてない。"
    show SCG_03 0 with fastdissolve
    sc "…はぁ…何言ってるんだか。「もう」五日目じゃなくて「まだ」五日目なんだよ。{w}何が起こるかなんて誰にも分らない。"
    sc "神殿は保育園じゃないって言葉の意味がまだわかってないみたいだけど、オマエ一人がヘマをこいたら皆が迷惑をするんだ。"
    show SCG_03 2 with fastdissolve
    sc "なら何？{w}オマエにそれ程の遂行能力があるとでも言いたいの？"
    sc "頼むからそのお粗末なおつむをちょっとでも開けて考えてみれば答えは出るんじゃない？"
    pl "テメェはそのお粗末な口をちょっとでも黙ってみれば？"
    pl "他人をアホ扱いするにも程があるだろ、もうテメェの戯言にヨイショしてやるのもそろそろ飽きたわ。"
    pl "マジでわかんねぇのか？{w}お前と居ると気分が悪くてしょうがねぇんだよ。"
    pl "毎日そうやって何事にも嫌味ばっかなのに誰がテメェと話したがるかよ。"
    pl "死体潰す勉強する前に他人と話す社会勉強でもしたらどうなんだ。"
    nar "俺は人知れず語を選ぼうとしたが、どうしても正しい言葉が出てこなかった。"
    nar "冷えた空気のほどに視線は冷たい。俺はその目を避けなかった。"
    nar "幾つかの事件が重なって、今日はとても彼と共に働く気分ではないからだ。"
    show SCG_03 7 at left
    show SCG_02 5 at right
    with dissolve
    sc "……"
    my "……ご…{cps=*0.1}ご{/cps}めんなさい…"
    show SCG_02 3 with fastdissolve
    my "ごめんなさい、わたし……"
    sc "……"
    show SCG_03 8 with fastdissolve
    sc "八つ当たりかよ。"
    pl "……何…"
    show SCG_03 7 with fastdissolve
    sc "そう、何が言いたいかは充分分かった。"
    hide SCG_03
    hide SCG_02
    with dissolve
    nar "彼はしばし俺とマヤをこもごも見てはすぐ目を逸らした。"
    nar "こういうことを聞くと彼がどんな反応を見せるだろうか、ひそかに気にかかっていたが、"
    nar "どう見ても怒った顔ではない。{w}かと言ってショックを受けたようにも見えない。"
    nar "きっと前から自分の問題点を知っていたんだ。そういう所がさらに俺の気に食わなかった。"
    show SCG_03 7 with dissolve
    sc "勝手にどうぞ。"
    hide SCG_03 with dissolve
    nar "冷たい一言を最後に外へ出た彼を、俺はずっと睨んでいた。"
    show SCG_02 7 with dissolve
    my "[na2]くん…怒った…？"
    pl "ゴメン、マヤ…"
    pl "怒ってなんかないさ。{w}ただアイツがマヤにあんな酷いことを言ったのが許せなくて。"
    show SCG_02 8 with fastdissolve
    my "……"
    nar "今一番いじけたのは板挟みになったマヤなんだろう。{w}彼女にこんな気分を感じさせたことには申し訳ないと思っている。"
    nar "しかし彼に言い違いをしたとは思わない。{w}いつもだったら何気なくやってしまったかもしれないが、"
    nar "今は自分の言葉が守れる自信がある。"
    nar "幼い頃から何でもすぐ習ってきた。仕方なくマヤと二人きりに仕事に行ったこともある。"
    nar "気分を整えてマヤを見つめる。幸いまだ涙は見せていない。{w}いろいろ重なって不安がっているようだ。"
    pl "マヤ、行くよな？"
    nar "そのせいか、俺の質問にも答えをためらっている。彼女は元々自信がない。"
    nar "怒ったとしても自分が怒っているのかも分からない。違うって言える状況になってもそう言えない。"
    nar "だから余計な喪失感を感じていた。{w}彼はこんなことを知っていてそんな風に言ったのか。"
    nar "いや、今彼女の深さを知っているのは俺だけだ。{w}誰でもなく俺だけが、マヤの力になれるんだ。"
    nar "長い時間返答は来ない、俺はもう一度彼女を呼んだ。"
    pl "マヤ。"
    show SCG_02 7 with fastdissolve
    my "わたし…わかんない。{w}仕事に劣るから部署のお荷物になってるのは事実だし…"
    my "[na2]くんにまで迷惑かけちゃう…"
    pl "マヤ、そんなんじゃない。アイツが言った事なんて気にすんなって！"
    pl "お前が誰より一生懸命なのは今まで隣でずっと見てきた俺の方がわかる。"
    pl "アイツだけじゃなくとも仕事してりゃああいう嫌味は付き物さ。あんな小言に負けちゃダメだ。"
    my "……本当に、そう思う？"
    pl "もちろん。前も言っただろ？俺はお前の味方。{w}今日上手くいけばアイツも何も言えないだろ！"
    show SCG_02 0 with fastdissolve
    my "うん…{w}ありがとう、[na2]くん。"
    nar "やっと肯定の答えが返ってきて人知れず安堵の息を吐く。"
    nar "これで彼女にも少しは気合が入ったら良いのにな。"
    hide SCG_02 with dissolve
    nar "今日は珍しく書類挟みと書類が分けてあった。{w}一々差し挟むことも煩わしいって思ったのか。"
    nar "一様に置いてある二枚の書類を持ち内容を見る。住所を読むことも、正体の分からない記号を読むことも大分慣れてきた。"
    nar "ここでアルファベットは仕事の種類、数字はその仕事の難易度を示す。"
    nar "例えば掃除の場合、ここでの難しさは死体の腐敗の程度によって決まる。１から高くは５までが普通だそうだ。"
    nar "アルファベットは掃除と消毒、数字は２から４まで。これくらいなら何の問題もない。"
    stop music fadeout 2
    hide screen textbox with dissolve
    nvl clear
    pause 1.0
    scene bg00 with dissolve
    pause 1.0
    if hssh_rkn == True:
        scene bg13 with dissolve
    else:
        scene bg13_1 with dissolve
    call place13 from _call_place13_3
    show screen nvlbox with dissolve
    play music "audio/bgm/dialogue.ogg"
    "\n 案の定、仕事は難事もなく終わらせた。"
    "彼女の動きが鈍いなら、それだけに効率的に仕事を分配して行動すれば良い。{w}こんなに何かを頑張ってやっつけたことも久しぶりだ。"
    "床にくっついた鳥や猫の死体を見る度は俺たちのどちらも顔を顰めていたが、人の死体ほどの拒否感は感じられなかった。"
    "今まで人は死して名や、少なくとも遺品ぐらいを残すんだと思っていたが、とんでもない誤解だった。"
    et "人は死して粘ついた糞尿と脂を残す。{w}床に付いて黒く変色されていく布団を外せば、その中にはウジと名の知れない虫がうじゃうじゃしていた。"
    nvl clear
    "\n 特に大変だったのは風呂場に入って、暗褐色の液体が張り込まれた小さい風呂桶を見た時だ。"
    "死体は別の所に移されたのか、またはとっくに融けてしまったのか区別もつかない状態だった。"
    "俺はその光景を目にするや、後ろのマヤを風呂場から出て行かせては反吐を吐いた。"
    "元々ムカつく悪臭と反吐の酸っぱい匂いが生臭い空気の中で混じってしまい、精神が混迷した。"
    et "しかし、やがていしくも体を動かし出した。"
    nvl clear
    "\n 言うまでもなく嫌だったが、どこからそんな精神力が出てきたのか今になっては覚えていない。{w}混迷だったからできたことだったかもしれない。"
    "汚い泡に漂う爪、髪、肌などの落とし子が俺の反吐と共に、水と薬品に流れることを見守っては扉の向こうの彼女を思い出した。"
    et "そしてすぐ思い浮かんだのは今朝の彼の言葉だ。{w}それを思いっきり否定してあげたのは俺なのに、中々疲れていたんだろう。"

    hide screen nvlbox with dissolve
    show SCG_02 7 with dissolve
    show screen textbox with dissolve

    pl "今日のはこれで終わりか？思ったよりはちょっと掛かっちまったな。"
    my "ごめんね、わたしが邪魔になったせいで…"
    pl "ん？あぁ…"
    show SCG_02 8 with fastdissolve
    nar "疲れたせいだろうか曖昧に言葉を濁してしまった。{w}馬鹿野郎。すぐ否定するんだ、何やってんだよ。"
    nar "素早くマヤの表情を見て別の話題を探しに頭をひねってみたが、中々思い出せない。"
    nar "実は今朝のヘンな夢のせいで寝そびれた気がして、目が疲れた。{w}こうしているうちにも彼女の顔は段々暗くなっていく。"
    nar "マヤから見ても俺は疲れているように見えるのか。無理しているようには見えていないか。{w}それなら…"
    nar "そこまでとして考えを止めた。{w}万が一彼女に余計な腹いせでもしてしまうのか怖くなってきたからだ。"
    pl "今日は普段より仕事多かったな！正式司祭になったら毎日こんな感じなのかな。"
    my "そう…だね。{w}わたしたちももう五日目なんだし…"
    pl "あっという間だったなぁ。"
    my "そうかな？わたし、一日が長く感じるからまだ五日しか経ってないってことに寧ろびっくりだよ…"
    pl "俺はまぁ、マヤと一緒に居ると一日なんてあっという間なんだけどな。{w}寧ろ足りないくらい？"
    show SCG_02 7 with fastdissolve
    my "うぅ…"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    pause 1.0
    scene bg17 with dissolve
    pause 1.0
    call place17 from _call_place17_1
    show screen textbox with dissolve
    nar "帰り道の途中、空気が可笑しくなってきたことに気付いた。"
    nar "マヤが後ずさりに引っ込む。その怖がる視線が届く所には枯れた草と木があった。{w}今朝までは茂った森道だった。"
    nar "地が腐っていく。{w}その意味はもう分かっている。禍の力場はこんな形でも広がっていけるのか。"
    show SCG_02 7 with dissolve
    my "もうこの道は通れない……"
    pl "反対側から回るか。"
    my "でもそっちって一度も行ったことない道なのに…"
    pl "通れるなら何だって道だろ。普段よりもうちょい歩くぐらいだから！"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    nvl clear
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene bg17 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "俺たちは結構歩いた。{w}目に見えない禍の力場を避けることは大分厄介なんだ。どこまで広がったのかも知らないから。"
    nar "その未知の恐怖は俺たちの歩きを急がせ、随分遠くまで回り道をしたと言う実感は俺たちに不安と共に安堵感を与えた。"
    nar "そうやって俺たちが入ったのは、天井が暗く、地面がじくじくする抜け道だった。"
    nar "遠くで見たら大きな木の周りに木陰ができていると思ったのに、中に入ってみればそれは古臭い建物だった。"
    show SCG_02 8 with dissolve
    pl "随分歩いたな。マヤ、大丈夫か？"
    my "まだ大丈夫…"
    my "今は何時だろう？{w}外の状況が状況だから時間もわからないなあ…"
    pl "ホ～ント、それだよ～…"
    hide SCG_02 with dissolve
    if hssh_rkn:
        nar "時間はともかく、昼か夜か見分けられない白夜。"
        nar "明るい日の下を歩くことには慣れているが、日の沈まないことは俺の予想以上に慣れ難いものだった。"
        nar "静かな空に比べて、その下の出来事は一様に騒々しい。昼夜の境界が濁ったほどに"
        nar "夜の出来事が昼にも頻りに起こって、昼に寝てきた人は時期を逃してしまう。今の俺の状況もそうだ。"
        nar "日の消え去らない白夜。"
        nar "その永遠なる太陽はまるで一日がずっと終わらないようで俺は息苦しくなって、感覚が鈍くなってきた。"
    else:
        nar "時間はともかく、昼か夜か見分けられない極夜。"
        nar "暗闇の中を歩くことには慣れているが、極夜に適応するのって只視覚が慣れるだけだとは限らない。"
        nar "眠っているように静かな空に比べて、その下の出来事は一様に騒々しい。昼夜の境界が濁ったほどに"
        nar "夜の出来事が昼にも頻りに起こって、昼に寝てきた人は時期を逃してしまう。{w}今の俺の状況もそうだ。"
        nar "日の昇らない極夜。光と言っても日付が変わる度にほんの少しだけ入ってくる一瞬の青き光だけだ。"
    nar "その限りない夜に俺は息苦しくなって、感覚が鈍くなってきた。"
    nar "ずっと歩いてはいるが、疲れが溜まったせいなのかいつもよりも地面に近い気がする。"
    nar "低くなった空が天井のように体を押さえつけてくる感じだ。"
    nar "時折気が戻ったように肩や腰を伸ばしてみたが、歩けば歩くほど体が前へ曲がっていく。"
    nar "言われなくても息苦しい肉体と精神はもう息さえちゃんとできずに、只吐き飲みを意味もなく繰り返している。"
    nar "意図的に息をしようと努力しても、頭に酸素が回らない。"
    nar "その姿勢のまま喘いでいる様がみっともなくて、一度大きく息張って止まった。"
    pl "はぁ…"
    show SCG_02 0 with dissolve
    my "[na2]くん、疲れちゃった…？"
    pl "あんな歩いたんだし、まぁ…？でも大丈夫、心配するぐらいじゃないって。"
    pl "状況はこんなだけど、そんな特別心配しなきゃいけないぐらい遅くはなってないはずだぜ。"
    pl "まあお昼時間は過ぎちゃったかもだけど。"
    pl "どうせ外出たんだし、何か買い食いでもしてくか？"
    show SCG_02 8 with fastdissolve
    my "ううん…わたしはこのまま帰るね。{w}食欲もないし、お金もないから。"
    pl "でもマヤ、もう何日もご飯を抜いてるじゃないか。仕事だってキツいのに倒れちまったらどうするんだ？"
    my "大丈夫、どうせ時間通り戻れてても食事は多分取れなかったと思うから。{w}おねえちゃんのことでまだ頭がぐちゃぐちゃするの…"
    pl "朝のことがまだ気掛かりなのか？"
    my "気掛かり、と、言うより…{w}何だろう…こわいって言えばいいのかな。"
    pl "怖い…？"
    show SCG_02 7 with fastdissolve
    my "…さっきの禍あったでしょ、あれ、こわいよね？"
    my "ずっと思ってたことなんだ。{w}皆には見えてるのにわたしだけ見えない何かなんて、怖すぎるよ。"
    show SCG_02 8 with fastdissolve
    my "おねえちゃんの亡霊も、シーキュレットくんなら見えてたのかなあ…"
    pl "…そんな事はないと思う。"
    nar "魔導師が守っている以上神殿に亡霊が出入りすることはできない。{w}それは当然なことで、彼女が知らないはずがない。"
    nar "多分彼女も気付いているだろう。"
    nar "それはそこにいるように見えて存在しないもの。{w}俺もその正体を分かっている。"
    nar "朝の頭痛が思い浮かんで徐々に歩きが遅くなる。{w}側には彼女が歩いている。彼女は俺の返答への反応としては遅く頷いた。"
    my "もうおうちには帰れないなあ…"
    hide SCG_02 with dissolve
    nar "それは質問であり、また独り言だった。"
    nar "俺が敢えて答えられない、彼女の一人きりの対話。{w}少しは考えをまとめられたら良いのにな。"
    nar "家に帰らないことは彼女なりの断念なのかもしれない。{w}しかし俺は心の内、それを望んだ。"
    nar "これからも彼女と一緒にいられることに嬉しがっていた。"
    nar "頼られる家族、通じている友達。{w}変わらない日常、安定感のある生活。"
    nar "そういったことに囲まれていても只視界が縮れてしまうだけだ。"
    nar "世は広き、やれることは多し。{w}機会は働く者に訪れるものだ。{w}狭い巣にいてばかりでは、彼女にとっても損ではないか。"
    stop music fadeout 2
    call bgw from _call_bgw_5
    nar "遅く動く頭で言葉を取り出していると、ふと前を遮ってくる違和感に気付いてマヤに前を立ちふさがった。"
    nar "暗闇の向こう側で何かが動いていた。{w}一日中死体の山を登っていたら鼻が鈍くなっていたんだろう。"
    nar "それの存在を認めると、ここの腐った臭いが明らかになった。{w}足を地面に擦っているような音は何故か聞き慣れている。"
    nar "屋根の陰に隠されて確かな姿は把握できないが、まともな人間でないことは確実だ。"
    show SCG_02 5 with dissolve
    play music "audio/bgm/youre in danger.ogg" fadein 5
    my "亡者…？"
    pl "まだ昼のはず…道が暗くて出て来たのか。"
    nar "そういえば亡者の中ではたまに早起きする奴らもいるって言ってたか。 {w}急いで退いたが、奴はもうこちらを見つけた。"
    scene black
    play sound "audio/se/hit.ogg"
    nar "それとほぼ同時にマヤの鋭い悲鳴が鳴る。{w}奴が俺の方へ先に飛びかかってきたのだ。" with sshake
    hide screen textbox with dissolve
    scene bg17
    show screen nvlbox
    with dissolve
    nvl clear
    "\n 持っていた袋が吹き飛ばされ、体は地面と触れ合った。{w}床はまだ泥濘、やっと背が触れないように腕と脚に力を入れた。"
    "武器は持っていないし、押し出す力は案外強い。{w}ほんの少しでも力が抜けたら最後だって、頭の中で警報が鳴る。"
    "身を屈めたせいか訳もなく腰が震えてしまう。{w}俺は片脚をできる限り曲げては、奴の腹に足を差し付け、思いっきり押し出した。"
    et "その感覚は、感じられる力よりも軽い。"
    nvl clear
    "\n 自分が押されていることに反応したのか、亡者は俺から手を離し、代わりに眼孔を刺そうとするように何度も腕を伸ばしてきた。"
    "俺は脚にもっと力を入れて奴の腹を蹴飛ばし、すぐ無防備の顎をぶん殴った。"
    "顎を殴ったと思ったのに、人間であれば必ず持つべき骨や肉などが感じられない。"
    "代わりにどろどろして冷たい何かが拳に触れた。{w}それはさっきから醜くぶらぶらした舌、そして小さい歯のような物だった。"
    et "だとしても頭を掴んだのは成功だった。{w}重心がそちらに偏り、簡単に姿勢が覆された。"
    nvl clear
    "\n 俺は奴の体の一部だと把握したのは何でも押しつぶそうと全力を尽くした。"
    "「マヤ、道具入れの袋の中に魔導書が一冊あるはずだ！{w}役に立ちそうな奴なら何でもいいから、それを…」"
    "「だ、だめ、わたし呪術なんて一度も…」"
    play sound "audio/se/hit.ogg"
    et "「出来る！出来るはずだマヤ！」" with sshake
    "怯えているマヤは脚の力が抜けたか床を這い袋の中を探る。{w}ここで俺がマヤを守れなかったら…"
    "…そういう可能性は想像もしたくない。"
    "よりによってマヤと二人きりの時動いた力場、回り道でぶつかったのは早起きの亡者。"
    et "俺はもう、これは単なる偶然の連続ではないと思っている。"
    nvl clear
    "\n これだけに精巧な不幸があるとすれば、恐らくそれは試練だ。{w}誰かが俺を見守っているんだ。{w}俺はここでマヤを守らなければならない。"
    "マヤは震える声で何かを言いよどみ始めた。{w}蹴った瞬間何か切られた音がしたのに、再び見てみれば傷が徐々に癒えている。"
    "心が早急になった共にその姿を再び近くで見ることで、ある違和感に気付く。"
    "膝と脚で押している物が何故か細い。{w}体重を入れて押さえつけただけなのに直下で声の割れた悲鳴が聞こえてきた。"
    et "女性だ。{w}藁のように粗い乱れ髪の女性だった。"
    nvl clear
    if persistent.call_CG == True:
        hide screen nvlbox with dissolve
        hide SCG_02 idle with dissolve
        pause 1
        show story11 with slowdissolve
        pause 2
        show screen nvlbox with dissolve
    else:
        nvl clear
    play sound "audio/se/memory.ogg"
    call bgw from _call_bgw_6
    "\n 一瞬、俺は思わずその姿に誰かが重なったように見えた。{w}飲み誤った息が喉にかかって咳が出てしまう。"
    "後ろにいるのは怯えているマヤだ。{w}彼女は今、俺のことを信じている。"
    "このまま俺が動きを止めていれば彼女の不安感はさらに大きくなってしまうだろう。"
    "そうさせない為に拳を振り回した。{w}震えている手だが、手袋の中に写って見えた聖痕は赤色だ。"
    et "今度は亡者の傷が癒えない。{w}効果はある。"
    nvl clear
    play sound "audio/se/hit.ogg"
    "\n 俺は拳を振り回し続けた。{w}マヤは途中から息が急いては、震える呼吸を一寸で何回も吐き出した。" with sshake
    "彼女の持て余したような鳴き声。{w}亡者の荒れ狂った悲鳴。俺の呼吸も共に乱れてしまう。"
    "怖さ、そしてそれを超えてしまう絶望感のせいか、震いは止まらない。"
    "亡者は出張った目玉を大きく開き俺を見つめていた。{w}蒼白に冷えた肌は黒くて粘っこい血と一緒に潰れる。"
    et "悲鳴を張り上げる小さい喉仏がまるで生きているようにまだ動く。{w}萎びた指の先に落ちる寸前の爪をした手をこちらに伸ばしている。"
    nvl clear
    $ renpy.music.set_volume(0, channel="music")
    hide screen nvlbox
    play sound "audio/se/noise.ogg"
    show BG12_ns at ns
    pause 0.1
    stop sound
    hide BG12_ns
    show screen nvlbox
    $ renpy.music.set_volume(1, channel="music")
    "\n 「私は何も悪くない！」{w}と、絶叫に似た叫びがあの場所にいた時よりもさらに鮮明に浮かんで頭を揺らす。"
    $ renpy.music.set_volume(0, channel="music")
    hide screen nvlbox
    play sound "audio/se/noise.ogg"
    show BG12_ns at ns:
        yzoom -1
    pause 0.1
    stop sound
    hide BG12_ns
    show screen nvlbox
    $ renpy.music.set_volume(1, channel="music")
    pause 0.05
    $ renpy.music.set_volume(0, channel="music")
    hide screen nvlbox
    play sound "audio/se/noise.ogg"
    show BG12_ns
    pause 0.2
    stop sound
    hide BG12_ns
    show screen nvlbox
    $ renpy.music.set_volume(1, channel="music")
    "だったら一体誰のせいなんだよ。{w}俺が悪いんだとでも言いたいのか。{w}いや、違う。誰もそう思っていない。" with sshake
    "恐ろしい幻影が目の前で煌いて通り過ぎる度に、俺は一層強く拳に力を入れた。"
    "「怖い、怖いよ…」と、マヤは何かに縋るように必死に呟いている。"
    "亡者はもう動かない。{w}泥に混ざった肉片が時折、やっと入ってくる光にてかっていた。"
    et "息切れがして、改めて一度大きく息を吸い込むと目が眩んでしまう。"
    nvl clear
    stop music fadeout 3
    hide screen nvlbox with dissolve
    pause 2
    scene black with dissolve
    pause 3
    show bg17 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "そういえば安全な処理の為に、死体の首を切るべきだったような…"
    nar "そこまで思いやると血走った目から涙が出てきた。{w}俺は一体何をやっているんだ。"
    nar "ここでこんなことを考えてしまえばダメなのに、力の抜けた体では起きるばかりか、頭さえ上げられなかった。"
    nar "息を引く度に渇いた喉からかっかっと音がする。"
    nvl clear
    hide screen textbox with dissolve
    show screen nvlbox with dissolve
    play music "audio/bgm/grumble.ogg" fadein 5
    scene black
    "\n その瞬間、鋭い痛みが全身を刺した。" with sshake
    "爆発的な激痛に、へこたれた体に一瞬で力が戻ってくる。{w}俺は悲鳴を張り上げながらどろどろになった床の上で転がった。"
    "火がついたように熱い両腕が痺れる。苦痛が一所に集まっていた。"
    "解けた包帯の隙から見える腕は赤黒い。"
    "どこかで腐って長く溜まった血ではない新鮮な鉄の生臭い臭いがして、それが俺から流れ出たという事実が俺の頭の中を渦巻かす。"
    "怖い、怖い、と、マヤはまだ呟いている。{w}怖い。{w}って。"
    nvl clear
    call bgw from _call_bgw_7
    "\n 死体を燃やす臭いなんてはうんざりするほど吸ってきた。{w}高く積み重ねた藁に火をつけ、村の人たちは周りを回りながら夜通し酒を飲み、食べ物を喰らう。"
    "これが俺の知っている葬式の風景だ。{w}俺の知っている死とはそういうことだ。"
    et "しかしそうではなかった。{w}死とはこんなにも熱く、生臭い臭いのものだったのか。"
    nvl clear
    "\n 遠くから段々近くへ、走ってくる足音が聞こえてくるような気がした。"
    "喘ぎ呼吸の音は様子を察するように静かになる。{w}「ダメだ。」状況を詰めていそうな絶望的の独り言。"
    "きっと聞き慣れた声なのに、何故か初耳のように感じられる。"
    "その声は、もうとても近くで俺のことを何度も呼んでいた。{w}間もなく、強い布のような物が目を隠す。"
    "そしてその手は忙しく、声は切羽詰まる。"
    "「…を通っていこう、近道はそこしかない…」"
    "「…くん…ごめんね…わたし……ごめんなさい…」"
    "「…まで…目隠しを絶対に外しちゃいけないよ。頼むから落ち着いて…」"
    et "すぐ前で忙しく動く人の声が霞んでいく。"
    hide screen nvlbox
    stop music fadeout 5
    show Blsnow zorder 2
    pause 8
    play music 'audio/bgm/dream.ogg' fadein 5
    pause 2
    show bgw
    show screen TrackCursor
    with slowdissolve
    pause 2
    nvl clear
    br2 "\n {color=000}奇妙な風景だ。{w}多くの人が並んでいる。綺麗なこの場所とは似合わなく、床は汚物塗れだ。{/color}{w}{nw}"
    extend "\n{color=000}あの人たちは俺の知っている人に見えたが、また知らない人みたいにも見えた。{/color}{w}{nw}"
    extend "\n{color=000}名を呼ばれた俺は一人で、あの行列を通り過ぎて手摺りの上に立つ。{w}そこには一人の司祭がいた。{/color}{w}{nw}"
    extend "\n{color=000}見初めた人だ。{w}彼は真似してほしいみたいに俺の目の前で親指、食指、中指をまとめて見せた。{/color}{w}{nw}"
    extend "\n{color=000}俺がぎごちなくそれを真似して手を高く上げると、彼はゆっくりと話し始めた。{/color}"

    pause 1
    scene black with dissolve
    pause 2
    scene BG12
    show screen grumble_cg082
    with slowdissolve
    pause 2.0
    show screen nvlbox with dissolve
    nvl clear
    "{color=#000}{size=0}{k=0}聖なる福音書と生命の源たる我が主よ、お聞きくださいませ。{/k}{/size}{fast}{/color}{nw}"
    image day5_1 = Text("聖なる福音書と生命の源たる我が主よ、\n お聞きくださいませ。",text_align=0.5,  slow=True, slow_cps=5 ,size=36)
    if config.language == "English":
        image day5_1_en = Text("Our lord, who art the source of the \n   holy gospel and life itself, hear our prayer.",text_align=0.5, size=27)
        show day5_1_en onlayer screens at truecenter, blur_1 with dissolve
    elif config.language == "SimplifiedChinese":
        image day5_1_cn = Text("神圣的福音书与生命之源的我主啊，\n 我们向祢祷告。", text_align=0.5, slow=True, size=28)
        show day5_1_cn onlayer screens at truecenter, blur_1 with dissolve
    elif config.language == "Korean":
        image day5_1_kr = Text("거룩한 복음서와 생명의 근원인 우리 주님, \n 들으소서.", text_align=0.5, slow=True, size=28)
        show day5_1_kr onlayer screens at truecenter, blur_1 with dissolve
    else:
        show day5_1 onlayer screens at truecenter, blur_1 with dissolve
    pause 5.3
    show ctc onlayer screens at blur_1, ctc:
        xpos 512
        ypos 420
    $ _dismiss_pause = True
    $ renpy.pause()
    $ _dismiss_pause = False
    hide ctc onlayer screens
    hide day5_1 onlayer screens
    hide day5_1_en onlayer screens
    hide day5_1_cn onlayer screens
    hide day5_1_kr onlayer screens
    with gjdissolve
    pause 1
    br "\n 後ろの人たちは人ごとに、彼に従いその福音を呟き出した。{w}{nw}"
    extend "\nしかし皆が句を知っていることではなかったのか、もたもたした声が混じって途中からその内容が分からなくなってきた。{w}{nw}"
    extend "\n俺の後ろに立っていた彼たちはどんな顔をしていたんだ。{w}表情の分からないこの人の前で俺はどんな顔をすれば良いんだ。{w}{nw}"
    extend "\nすぐ前で黄色に煌く光は眩しく、共に気分を見境もなく眩ましてしまう。{w}{nw}"
    extend "\n彼が手を下げると、段々小さくなっていた声も止まった。{w}彼は次に手摺りの上に立つ信者の名を呼ぶ。{w}{nw}"
    extend "\n俺たちの誰もが神々しく思うべきの彼女の名を。"
    stop music fadeout 5
    hide screen nvlbox with dissolve
    pause 1.0
    scene black
    hide screen TrackCursor
    hide screen grumble_cg082
    with gjdissolve
    pause 3
    if hssh_rkn == True:
        scene bg06 with dissolve
    else:
        scene bg06_1 with dissolve
    call place06 from _call_place06_7
    show screen textbox with dissolve
    nvl clear
    play music "audio/se/tutorial walking.ogg"
    nar "起きてから最初に見た天井は真っ白だった。{w}目まぐるしく視界を染めた赤黒い色はもう見えない。"
    nar "永遠に続きそうな痛みも感じられない。{w}まだ朦朧で、二回ぐらいゆっくりと瞬いた。"
    nar "そのまま首を回すと、ベッドの側で目を閉じたアルネ姉さんが、整然と手を合わせて座っている。"
    nar "病院の白くて薄暗い色と全く一団にならない黒髪で、彼女はさらに異質の存在に見える。"
    nar "小さな声で名前を呼ぶと、彼女はすぐ優しい目を開いて微笑みを見せた。"
    stop music fadeout 2.0 
    nar "俺、まだ夢の中なのか。"
    show SCG_07 7 with dissolve
    play music "audio/bgm/name select.ogg" fadein 3
    ar "お目覚めになりましたか。"
    pl "何でここに…"
    ar "どうも気掛かりになってしまいました故。"
    show SCG_07 7:
        xalign 1.2
    show SCG_14 0 at left
    with dissolve
    gr "そうよ、皆びっくりしちゃったもの。"
    pl "先生が居るってことは…ここは神殿の病院か。"
    show SCG_14 1 with fastdissolve
    gr "おはよう、[na2]くん。{w}怖い目に遭ってしまったのね。どこか痛むところはない？"
    pl "俺、どうやってここに？"
    play sound "audio/se/ding.ogg"
    call bgw from _call_bgw_8
    pl "マヤ！マヤは大丈夫なのか？！" with sshake
    show SCG_14 0 with fastdissolve
    gr "あの子は別のところで休ませているわ。{w}怪我がしていないけれどとても驚いちゃったみたいでね。"
    gr "落ち着いて、[na2]くん。あの子もそうだけどあなたも当分は安静にしてないと。"
    pl "そうか…良かった。"
    hide SCG_14
    hide SCG_07
    with dissolve
    nar "マヤが安全であることを確認したら朦朧とした精神が冴えてくる。"
    nar "そういえば確かに腕に怪我をしたのに、傷は影も形もなく綺麗に癒えた。"
    nar "事実、綺麗だとは言えないかもしれない。{w}傷の癒えた所に、再び苔むした岩のように黒き痕跡が立て込んでいたからだ。"
    nar "俺の姿を見て苦笑いをした先生が、忽ち表情を固めた。"
    show SCG_07 0:
        xalign 1.2
    show SCG_14 0 at left
    with dissolve
    gr "アルネちゃん、今から[na2]くんと大事なお話があるの。{w}だから申し訳ないけど少し…"
    ar "はい。席を御貸し頂き有難う御座いました。"
    hide SCG_14
    show SCG_07 7 at center
    with dissolve
    ar "[na2]兄弟、どうかご武運を。"
    hide SCG_07 with dissolve
    nar "姉さんがすっきりした動きで部屋を出て、彼女の席には先生が座る。"
    show SCG_14 0 with dissolve
    gr "いきなりあなたの彼女さんを追い出してしまってごめんなさいね。{w}ガッカリしちゃった？"
    pl "なっ…違う、俺とアル姉はそんな…"
    nar "そこで言葉を失ってしまう。俺とアル姉の関係って何なんだ。"
    nar "本来なら一生遭遇することさえもないアルタナータのお姫様。"
    nar "そんな彼女と何という邪魔もなく話せるのは、俺が彼女の婚約者である奇妙な関係であるからだ。"
    nar "それは今までとても非現実的な他人の話であったが、彼女を近くで会うことが増える度に、それは段々と現実的になってきた。"
    show SCG_14 1 with fastdissolve
    gr "本当、良い子なのよ。{w}とても忙しい時期だろうにここでずっとあなたが目を覚ますのを待っていてくれたの。"
    pl "姉さんが？"
    show SCG_14 at bounce
    gr "そう！{w}まぁ、あんな子が娘だったらそれだけでもとても誇らしいわ～"
    show SCG_14 0 with fastdissolve
    gr "でもそれはきっと寂しいと思うわ、あんな完璧な子なんて相当厳しい家庭からじゃないと出て来ないから。"
    pl "……"
    nar "何かを考えているだろうか、そっぽを向いた彼女の左手の薬指に、指輪が銀色で輝いていた。"
    gr "[na2]くん、あなたの考え方がどうかは分からないけど、あなたを心配する人たちをあまり困らせてはダメよ。"
    pl "俺だってわざとじゃ…"
    gr "先生を含めてね。"
    pl "先生も俺のこと心配してたのか？"
    show SCG_14 1 with fastdissolve
    gr "勿論よ。{w}女を待たせちゃうなんて、将来すごくダメな男になっちゃうわよ？"
    gr "例えばね…"
    hide SCG_14 with dissolve
    nar "茶目に言葉尻を伸ばしたグレーテ先生の頭に軽く書類の束が置かれた。{w}後ろには眉をひそめた男性が立っていた。"
    nar "顔は結構見たことがあって彼が保健部の主教であることは知っていたが、こんなに近くで見たことは初めてだ。"
    show SCG_14 5 at left with dissolve
    "{nw}"
    show SCG_14 at bounce
    gr "ありゃま。"
    show SCG_14 7 with fastdissolve
    show SCG_13 0 at bigright with dissolve
    qus "[na]、と言ったか。"
    pl "えっ…はい。"
    show SCG_13 8 with fastdissolve
    gg "保健部主教、{color=#93c47d}グレゴール・コーニッシュ{/color}だ。{w}こんな形で挨拶を交わすことになるとはな…誠に遺憾だ。"
    show SCG_13 0 with fastdissolve
    gg "それでは本題に入ろう、そこで何があった？"
    show SCG_14 3 with fastdissolve
    show SCG_14 at bounce
    gr "主教様、あまり怒らないであげて。"
    show SCG_14 3 with fastdissolve
    gg "それは返事によるな。"
    pl "…間違ったことはやってませんけど。"
    pl "禍のせいで遠回りして帰ることになって、亡者と遭遇して…"
    gg "その腕も亡者に？"
    pl "や、これは急にこうなっちゃって俺もあんまり…"
    pl "…そういや、図書館で魔導書を借りてたんですけど…"
    gg "図書館…{w}あそこの奴は浄化部の人は招き入れない筈だが。"
    pl "俺もそう思ってたんですけど、そこの主教様が直接…"
    show SCG_13 2 with fastdissolve
    gg "学術部主教が…？"
    ev "単純なる魔力増幅の呪術に御座いますわ、保健部主教様。"
    hide SCG_13
    hide SCG_14
    with dissolve
    nar "雅やかな声が戦いで姿を見せる。{w}手に持っているのはあの魔導書だ。"
    show SCG_13 2 at bigright
    show SCG_10 2 at left:
        xalign -0.1
    with dissolve
    gg "イヴリン・ヴィオレッタ…{w}またお前か。"
    nar "二人は同じく主教だから顔見知りなんだろう。{w}名前を呼ばれたイヴリン主教は笑むだけで答え、俺の方に近づく。"
    nar "化粧品のくすぐったい匂いが一気に寄せてきた。"
    show SCG_10 1 with fastdissolve
    ev "ご機嫌麗しゅう御座います、素敵な貴男。"
    ev "人の子の身分なぞでは解り得ないものが運命とは良く言いますが、しかし予想よりも随分と早くして御逢い出来ましたね。"
    pl "主教様はいっつも急に出てきて俺を驚かせるなぁ…"
    show SCG_10 0 with fastdissolve
    ev "アラ、有難き幸せ。{w}しかし私は貴方の奇跡に導かれただけの野次馬に他有りませんわ。"
    pl "奇跡…？"
    nar "俺は敢えて怪しむ反応を見せたが彼女は何の返答もなくベッドの角に腰をかけた。"
    nar "まるで俺の体の隅々まで目を通しているような視線がどこか一所で止まる。{w}俺は彼女に従い、再び自分の腕を見た。"
    show SCG_10 1 with fastdissolve
    nar "どうやら正解だったらしい、彼女は視線を逸らさずににっこりと微笑んだ。"
    show SCG_10 0 with fastdissolve
    show SCG_13 at bounce
    gg "お前、自分が何をしでかしたのか分かっているのか？"
    show SCG_10 4 with fastdissolve
    ev "判り兼ねません。{w}私がやった事ではありませんもの。"
    ev "これは私の固まりきった脳では想像も出来得なかった夢の様な出来事ですもの。"
    show SCG_10 2 with fastdissolve
    ev "魔法の増幅と云うものは集中といった概念に近いものに御座います。{w}存在しない力を創り上げる様なものではありませんわ。"
    ev "ましてや彼の聖痕はたったの二つ。その程度の力を身体が耐え切れないなんて有り得ない…{w}と云うことは貴方も御存知の筈。"
    gg "……"
    show SCG_10 0 with fastdissolve
    ev "私は単に、純粋なる心から差別されてきた浄化部の新入員に学べるような機会を与えたのみ。"
    show SCG_10 1 with fastdissolve
    ev "そしてあの女の子の言い分ですと、途中で止めたはず…との事ですよ？"
    ev "勿論呪術は切っ掛けの一つとは成り得ますが、原因ではないだろうと云うのが私の意見で御座います。"
    hide SCG_10
    hide SCG_13
    with dissolve
    nar "彼女の声は緊張感もなく遅いが、目の前の男性から一歩も退かないと言っていそうな気骨が見えた。"
    nar "二人は葛藤のある目でお互いを睨んでいながらも、その対話の中心は俺のことだった。"
    nar "実際俺はその間で何も言えなかった。{w}どこか何となく馴染みのある状況だな。"
    nar "朝のマヤはきっとこんな気分だったんだろう。"
    show SCG_14 7 with dissolve
    gr "[na2]くん、腕のその傷跡は今日出来た傷なの？"
    pl "いや…元からあったぜ。{w}俺が小さい頃腕に怪我をしちまって出来たモンだな。"
    hide SCG_14 with dissolve
    nar "せいぜい何気なく投げた一言にまるで火でもついたように、二人の女性は大きく目を開く。"
    nar "その貪欲な視線を受けていると自然と背筋に冷や汗をかく感じがしてきた。{w}まるで捕食者の前の餌になった気分だ。"
    nar "よく見ればそれは学術部の主教だけでなく、グレーテ先生も同じだった。{w}彼女は気遣わしい表情で豪気に目を光らせている。"
    nar "恐怖感がひそかに上がってきて保健部の主教様の方に首を回した。彼はこの状況に頭痛を感じているらしい。"
    show SCG_13 6 at bigright
    show SCG_10 0 at left:
        xalign -0.1
    with dissolve
    gg "…理解が出来んな。"
    show SCG_10 1 with fastdissolve
    ev "そんな惜しがらずとも…{w}全ては神の御意向、人間如きに理解出来得るものではありません。{w}そうでしょう？"
    show SCG_13 at huruhuru
    gg "イヴリン…"
    nar "先ほどと同じく、反応もなくベッドから体を起こした彼女は部屋を出る前に、最後に俺の手を握って話し出す。"
    nar "目覚ましく美しくて冷たい手からは何の人情味も感じられなかった。"
    hide SCG_13
    show SCG_10 0 at center
    with dissolve
    ev "貴方様、どうかその御身と力を大切になさいませ。"
    show SCG_10 2 with fastdissolve
    ev "今の貴方は神の謁見そのものと云っても過言では御座いませんので…"
    hide SCG_10 with dissolve
    nar "グレーテ先生は部屋を出ていくイヴリン主教の後ろ姿を見て、グレゴール主教を交々見つめては、最後に俺の方に視線を移した。"
    nar "何かを心配しているのか凄然とした顔だ。それに俺と同様にこの状況に困っているのか、さっきからそわそわしていた。"
    show SCG_14 0 at left with dissolve
    gr "[na2]くん、目が覚めたばかりで何がなんだかだよね、難しい話をしてしまってごめんなさいね。"
    gr "ここにずっと居ても良いんだけれども…気分が優れないなら戻っても大丈夫からね。"
    gr "必要な物があったら遠慮なく言ってちょうだい？"
    show SCG_13 0 at bigright with dissolve
    gg "[na]、イヴリン・ヴィオレッタの言う事はあまり深く考えなくていい。"
    show SCG_13 8 with fastdissolve
    gg "彼女は無論この神殿では最も優れた知性を持つが、それと同じぐらいに…"
    pl "詩人みたいなモンだって？"
    show SCG_13 0 with fastdissolve
    gg "…随分と古い言い回しの悪態だな。"
    gg "お前の血管は大きく破損している状態に近い\n。{w}呪術で傷の再生を試み、血は止めたが痛みが無いからと言って完治とは判断するな。"
    show SCG_13 2 with fastdissolve
    gg "今回は運が良かっただけだ。{w}次同じ事故が起きればその時は二度と両腕を使えなくなる可能性も高い。"
    pl "二度と…"
    show SCG_14 3 with fastdissolve
    gr "あなた、今彼にそんなこと…"
    show SCG_13 0 with fastdissolve
    gg "どの患者にも断言は要る。治療の基本は自身の問題と向き合う所にあるからな。"
    gg "では、安静するように。"
    hide SCG_14
    hide SCG_13
    with dissolve
    nar "大人たちの出ていった病室は静かだ。"
    nar "呆然と天井を見つめながら考えをまとめてみようとしたが、うまくいかなかった。{w}難しいことばかりだな。"
    nar "冷ややかな布団から微かな消毒薬の匂いがしている。多くの患者たちがここで横になっていたんだろう。"
    nar "もしあれが元は人だったとしても誰かをそんなに殴ってみたことは初めてで、衝撃はまだ手と脳裏に残っている。"
    hide screen textbox with dissolve
    pause 1
    play sound "audio/se/door slide.ogg"
    pause 2
    show screen textbox with dissolve
    nar "独りで天井を見上げていると病室に誰かが入ってきた。"
    nar "マヤだ。{w}その懐かしい顔を見て声を上げてから一瞬、彼女の後ろに付いてきた人の顔を見て思わず表情を固めてしまった。"
    show SCG_03 8 at left
    show SCG_02 7 at right
    with dissolve
    sc "……"
    sc "…やっぱり帰るよ…"
    my "ちょ、ちょっと待ってキューくん…{w}いかないで…"
    nar "マヤがシーキュレットの腕を掴んでぶら下がり、彼は困った顔で俺とマヤを交々見つめた。"
    nar "そして俺と視線が合った瞬間、彼はそのまま頭を下げて何歩か近づいてきた。{w}しばらく気まずい静寂が流れる。"
    show SCG_03 72 with fastdissolve
    sc "…腕は？"
    pl "ああ、もう大丈夫だぜ。痛まないし…"
    show SCG_03 8 with fastdissolve
    sc "そう…"
    nar "曖昧な所で対話が切れてしまってさらに気まずい。{w}俺はこの対峙状態に耐えられずマヤに言葉を投げた。"
    pl "マヤはどう？大丈夫か？ゴメンな、怖かったろう…"
    show SCG_02 0 with fastdissolve
    my "わたしは大丈夫…おかげさまで…ありがとう、[na2]くん。"
    nar "しかしマヤは俺に答えながらもずっとシーキュレットの機嫌を伺っていた。"
    nar "シーキュレットは早くもその視線に気付いたか、改めて頭を上げる。"
    show SCG_03 8 with fastdissolve
    sc "…ボクのせい、かな。"
    pl "そ～だよん、お前が一々ケチなんかつけて回るから俺が…"
    show SCG_03 3 with fastdissolve
    sc "ごめん。"
    nar "悪戯っぽく答える気だったが、シーキュレットがびくっと体を震わせた。{w}全く思いもかけない謝りをした彼の顔は蒼白だ。"
    nar "震えている。俺は彼の当惑感に寧ろ困る。"
    nar "今までのように、当然彼が俺の行動に怒ると思ったからだ。"
    sc "キミたちはまだちゃんとした研修も終わってないのに、ボクが先輩としてちゃんと対応も出来なくて…"
    sc "逆に責めたりしちゃったからだ。{w}本当に…ごめんなさい。"
    pl "…何だよ、散々言っといて今更謝るとか…何が言いたいんだ？"
    my "[na2]くん…"
    show SCG_03 at huruhuru
    sc "…簡単に許してくれるなんて思ってもいないさ、ボクはただ…"
    pl "いいって、俺がアホでもあるまいし。お前みたいな不器用なヤツの考えてることなんか丸見えだ。"
    pl "俺やマヤみたいな新入りがヘマこいて怪我を負ったり、死んだりするのが嫌だったんだろ？"
    show SCG_03 8 with fastdissolve
    sc "……"
    pl "なのにその鬼先輩のフリも虚しく、新入りが予想もしなかったところで怪我して戻ってくるから"
    pl "その責任がお前に全部問われちゃったんだろ。"
    pl "そんでどうしたらいいかも分かんないからノコノコとやってきて頭下げて謝罪して…"
    pl "お前ほど不器用なヤツはホント初めてだぜ。"
    sc "……"
    hide SCG_03
    hide SCG_02
    with dissolve
    nar "彼は何の返答もなく只頭を下げた。"
    nar "いつも偉そうに説教ばかりだったのに、俺の言葉があれもこれもツボに嵌って逆に何も言えなくなったようだ。"
    nar "何度も想像してみた表情なのにあまりありがたくない。"
    nar "頭はもうずっと前から冷めているし、再び味わってしまった重い空気はまさに不便だ。{w}俺はしんみりとため息をつく。"
    show SCG_03 7 with dissolve
    pl "お前が俺たちをここまで連れて戻って来たのか？"
    nar "再び頭を上げた彼は俺の突然の質問を思ってもいなかったように、まだ暗い顔で一度頷いた。"
    nar "よく見れば、彼にも治療の跡が残っている。"
    pl "へぇ、どうやって？"
    sc "キミら新入りの仕事は僕が配置してたから、最初から場所は知ってたんだ。"
    show SCG_03 3 with fastdissolve
    sc "…だけど、よりによって力場がそっちに向かっちゃって。"
    nar "俺は今日までの書類の内容を思い出した。仕事としても大体掃除や消毒で、特に読みにくい所もない書類だ。"
    hide SCG_03 with dissolve
    nar "今まで俺が仕事に慣れてきたおかげだと思っていたが、やっとつじつまが合ってきた。"
    nar "だから今日は書類と別途に挟みがあったな。"
    pl "マヤ、コイツお前にもちゃんと謝ったか？"
    show SCG_02 0 with dissolve
    my "えっ、うん…[na2]くんが起きるまではずっと一緒にいたんだし…"
    pl "ならいいや。{w}ていうか俺…お前みたいなヒョロヒョロしたヤツと喧嘩する趣味なんてねえし。"
    hide SCG_02 with dissolve
    show SCG_03 7 with dissolve
    pl "でも朝言ったことは概ねマジだからな？お前はその悪い口の癖を直した方が良いぜ。"
    sc "…それはムリかな。{w}だってキミの顔を見てると自然と悪態が出てしまうんだもの。"
    pl "何っ…"
    show SCG_03 4 with fastdissolve
    sc "…冗談だよ。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve

    show screen textbox with dissolve
    nar "三人で一緒に病室から出て、前に並んだ椅子を見れば、そこにはこの真っ白の病棟とは似合わない鮮明な髪色の人が座っていた。"
    nar "俺たちを見て嬉しそうに手を振るあの人物は見慣れた本を持っていて、俺は思わず肩を竦めた。"
    show SCG_11 1 at right:
        yalign 0.11
    with dissolve
    rv "おっと、これはこれは…ふふふっ。"
    show SCG_03 0 at left with dissolve
    sc "…何がそんなに面白いんだい、ラヴィ。"
    rv "へへ、何でもないでちゅ。"
    pl "お前も俺のお見舞いか？"
    show SCG_11 4 with fastdissolve
    rv "はい、容態が優れて来ているようで何よりでございます、[na]お坊ちゃま。"
    rv "そしてささやかな謝罪を一つ申し上げたく…"
    show SCG_11 3 with fastdissolve
    rv "ボクが不注意に本を貸し出してしまったが為に、皆様に不穏な経験をさせてしまったこと、誠に申し訳ございません。"
    hide SCG_03
    show SCG_02 7 at left
    with dissolve
    my "そんな…元はといえばわたしが…"
    pl "や、こんな事態になるなんて誰も予想もつかなかっただろ"
    pl "あとさっき学術部の主教様も言ってたけど、これは呪術のせいでもないらしいし。"
    show SCG_11 0 with fastdissolve
    show SCG_02 0 with fastdissolve
    rv "その通りでございます。マヤお嬢様が気を病まれるようなことではありません。"
    pl "お前もだよお前も、ラヴィ。{w}お前もな～んかちょっと固すぎるとこあるんだよな。"
    show SCG_11 1 with fastdissolve
    rv "おっとっと…こうやって返されてしまうとはずかちいものでちゅね。"
    hide SCG_02
    hide SCG_11
    with dissolve
    pl "ちょっと待てよ…お前がここに居るってことは…"
    pl "俺、こんな短時間に補佐教を四人も会ったのか！{w}や～大人気、大人気。"
    nar "茶目に言い出した言葉に誰もが口を噤んだ。{w}真ん中の俺が慌てていれば、ラヴィとシーキュレットが目を合わしたようだった。"
    show SCG_11 3 at right:
        yalign 0.11
    show SCG_03 7 at left
    with dissolve
    rv "実は、お坊ちゃまがお眠りの間に主教会議が開かれておりまして。"
    pl "それってもしかして…"
    nar "「奇跡に導かれただけの野次馬」…{w}あの発言が再び思い浮かぶ。"
    rv "それ程に坊ちゃまは前例のない大事件ということですね。{w}理由も明確ではないので…"
    rv "これまた神託のカタチの一つではないのかという話まで出ております。"
    show SCG_03 72 with fastdissolve
    sc "大人気程度じゃ済まないぞ？どう責任取るつもりなんだよ。"
    pl "責任って、俺…"
    hide SCG_03
    hide SCG_11
    with dissolve
    show SCG_02 0 with dissolve
    my "……"
    nar "すぐ傍にマヤがいるのに、人の不安を気にすることさえできないほど不安になってきた。"
    hide SCG_02 with dissolve
    nar "俺の体に何かが起きている。{w}しかし一体それは何なのか自分自身はおろか、他の人にも説明できない。"
    nar "それは俺に恐怖感を与えるには十分だった。白い掌に冷や汗が染み出た。"
    show SCG_11 4 with dissolve
    rv "そんなに不安がらずとも大丈夫です。この事は我々以外にはまだ知らされておりませんので。"
    pl "……"
    hide SCG_11
    show SCG_03 7 at left
    with dissolve
    sc "誰かに言うつもりもない。"
    sc "こんな事実確認もできてないでたらめっぽいことなんて、どうせ逆に言った方が頭のおかしい人になるに違いないし。"
    show SCG_02 0 at right with dissolve
    my "そうだよ、[na2]くん…意外となんともないかもだし…"
    pl "でも…"
    show SCG_03 0 with fastdissolve
    sc "[na]。{w}心配になる気持ちもわかるけど、真偽の確認も取れないことでそんな考えこむ必要はないんだ。"
    sc "今はキミ自身の安静を最優先に考えなよ。"
    pl "…それさっきも聞いたって～"
    pl "…てか、なんでみんなこんな聞いちゃったら最後不安になるしかない事実を告げて置いて心配するなとか言われても…"
    hide SCG_02
    show SCG_11 1 at right:
        yalign 0.11
    with dissolve
    rv "事実を上手く包められないのがシーキュレット坊ちゃまの悪いとこでちゅから。"
    show SCG_03 at bounce
    sc "うっ…"
    show SCG_11 4 with fastdissolve
    rv "ですが、それは良いところでもあります。ボクの意見も同じですので。"
    hide SCG_03
    show SCG_11 at center
    with dissolve
    rv "[na]坊ちゃま、歴史的にもこの様な事件は大抵取らぬ狸の皮算用として終わる場合が多いです。"
    rv "今は何よりも安静が大事ですよ。"
    rv "しかも坊ちゃまは部署異動の件でもう既に頭の容量がいっぱいでしょう？"
    pl "それもそうだな。{w}やっと忘れかけてたのに蒸し返して下さってアリガトさん、ラヴィ！"
    show SCG_11 1 with fastdissolve
    rv "あっちゃ～またまたやってしまいまちた。"
    hide SCG_11 with dissolve
    show SCG_03 0 at left
    show SCG_02 0 at right
    with dissolve
    sc "ハァ…兎にも角にもキミはここでもう少し休んでから移動するなり何なりしてくれ。"
    show SCG_03 7 with fastdissolve
    sc "ボクもキミのため出来る限りのことはするから…"
    show SCG_02 7 with fastdissolve
    my "わたしも…手伝えることがあったらだけど…"
    pl "ありがとう、マヤ。その一言だけでもう元気いっぱいだぜ…"
    hide screen textbox with dissolve
    hide SCG_02
    hide SCG_03
    with dissolve
    pause 1
    scene black with dissolve
    play sound "audio/se/door slide.ogg"
    pause 2
    if hssh_rkn == True:
        scene bg06 with dissolve
    else:
        scene bg06_1 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "仲間たちに手を振って見送った後、俺はしばらく病室に入って座っていた。"
    nar "綺麗すぎた白色と微かに広がった消毒薬の匂いは心に安定感と共に不安感を与える。"
    nar "何事もうまくできているのに、どこかがずれているような焦燥。"
    nar "俺はその理由を考えようとしたが、代わりに冷ややかなシートに頭を寄せた。"
    nar "この気分を分かってしまえば何かが大きく外れてしまい、二度と元に戻れなさそうな気がして、"
    nar "遅く鳴る脈と時計の針の音が重なって静かな部屋を満たしていた。"
    nar "俺はこの問題について…"
    hide screen textbox with dissolve
    call meet_girl from _call_meet_girl_1
    menu:
        "他の人と相談してみたい。":
            show screen textbox with dissolve
            $ meet_ar = True
            $ meet_gr = True
            $ meet_crea = 0
            nar "一人で悩んでいても仕方ないし、時間を過ごしたら、こういったことに詳しそうな人に会いに行ってみようか…"
        "できれば心配は掛けたくない。":
            show screen textbox with dissolve
            $ meet_rs = True

            nar "もう何人かに迷惑をかけてしまったし、ダメな男になってはいけないな。静かなところで間を持たしてから帰ろう。"
        "解決したい。":
            show screen textbox with dissolve
            $ meet_hk = True
            $ meet_crea = 0
            nar "……"
            nar "あの人は…今何をしているんだろう。"
    hide screen textbox with dissolve
    stop music fadeout 2
    hide screen textbox with dissolve

    if hssh_rkn == True:
        $ save_name = "day 5, 昼, 楽園"
    else:
        $ save_name = "day 5, 昼"
    jump placemenu
    return
label day5_night_rkn:
    $ save_name = "day 5, 夜, 楽園"
    scene bg02_1 with dissolve
    pause 1
    nvl clear
    $ show_quick_menu = True
    scene bg10_1 with dissolve
    stop music fadeout 3
    call place10
    pause 1
    show screen nvlbox with dissolve
    "\n 一日中多くの人と出会ったが、一人で寂寞な部屋にいるのは相変わらず落ち着けない。"
    "一日中誰かと一緒にいたせいで更にそう感じてしまう。"
    "俺はベッドに腰をかけて、窓から入ってくる光に腕を照らしてみる。"
    et "腕に刻まれた黒色の残痕がインクに染まったように少しの色つやを出し光っていた。"
    nvl clear
    "\n 村の人は最初は幼い俺についていろんな話を交わったが、そういう心配にも関わらず俺はこの残痕が刻まれたまま大人になった。"
    "そうこうしているうち自然に俺の残痕に関した疑問や噂は消えて、それは俺の中でも同じだった。"
    "俺にして当然なことが、他の人には全くそうではないなんて考えてもいなかった。"
    et "当然見えない物、当然そこにあった物。その全てが突然変わってしまうのはまだ俺には難しいものだ。"
    nvl clear
    play sound "audio/se/knock.ogg"
    "\n虚しくなってやたらに横の壁を二回叩いた。中身の空いた音がする。"
    "「おい、今いるか？」と、ちらっと出張った壁紙の下の小さな隙に声をかけてみた。"
    "しかし戻ってくるのは静寂だけだ。奴はまだ帰ってきてないってことか。まじめな奴。"
    "いきなり独り言を呟いたことになって鼻白んだ途端に、壁の向こうから彼の声が聞こえてきた。"
    hide screen nvlbox with dissolve
    show screen textbox with dissolve 
    sc "…なんだよ。"
    pl "まだ寝てないんだな。"
    sc "ボクは夜にも仕事があるからね。"
    pl "じゃあいつ寝てるんだ？"
    sc "仕事終わったら。"
    pl "へぇ…じゃあ今はヒマってことなんだな？"
    sc "…何か言いたげだね。"
    pl "かもな。"
    sc "相談？"
    pl "かもな…"
    nar "そこで答えが断たれた。選りによってこんな瞬間に無視か、何たる馬鹿げた状況だ。"
    play sound "audio/se/knock.ogg"
    nar "もう一度叩く為に手を上げると、ノック音が聞こえた。まだ壁に手が触れてもいないのに。"
    nar "あの音は扉の向こうから聞こえた。"
    pl "……"
    hide screen textbox with dissolve 
    pause 1 
    show SCG_03 8 with dissolve
    show screen textbox with dissolve 
    nar "もしやとして扉を開くと、正に彼がそこに立っていた。突然の訪ねに、驚きよりは怪訝さが先立つ。"
    pl "これは予想してなかったな…"
    sc "…この前言いたいことがある時は直接しなきゃってキミが。"
    pl "俺が？いつ言ったっけな…そんなことも覚えてるのかよ、お前ホント根に持つのな。"
    show SCG_03 0 with fastdissolve
    sc "壁越しに長話も可笑しいだろ…{w}で、入って良いのかい？"
    pl "うーん…まあ、入りなよ。"
    nar "白き光を受ける廊下に垂れた陰が徐々に短くなる。"
    nar "慣れた部屋に俺ではない誰かが入っているなんて、ヘンな気分だ。"
    nar "しかしそれは彼も同じだろうか、隅っこも、真ん中でもない曖昧な所に座っては気まずさを隠そうともしていない。"
    hide screen textbox with dissolve
    pause 1
    show story21 with slowdissolve
    pause 2
    nvl clear
    show screen textbox with dissolve
    play music "audio/bgm/name select.ogg" fadein 3
    sc "見てばっかだな、言いたい事あったら言いなよ。"
    pl "お前がすっごく不便そうに座ってるから見てたんだよ。"
    sc "…これが楽なんだ。どうせ長居出来ないし…"
    pl "あ、夜も仕事あるとか言ってたよな？こんな所で時間潰してていいのか？"
    sc "まだ大丈夫。"
    nar "「まだ大丈夫」って…言われなくても気まずい空気を更にまずくしやがる。"
    pl "今日正確には何があったんだ？途中から全く記憶になくて…"
    sc "キミ大分マトモじゃなかったからね…大したことは無かったよ。{w}キミの出血のせいですぐに神殿に戻らなきゃいけなかったんだ。"
    sc "その過程で禍の力場を逆らうことになったんだ。"
    sc "昨日、霧の中に入った時ボクが振り返ってはいけないと言っただろう？{w}それと似た様にその霧では前を見てはいけなかったんだ。"
    sc "だからキミには目隠しをさせて貰った。"
    pl "前が見えないのにどうやって道を探せたんだ？"
    sc "ボクはしてなかった。{w}キミを支えてなきゃいけなかったし、マヤも歩くのがやっとだったから。"
    sc "禍は直接当たるまでその症状は分からないというのが普通だけど、学術部で観測されたものも多い。"
    sc "だから司祭達が事前に情報を入手して行けるんだ。"
    pl "大丈夫なのか、それ…？"
    sc "軽い内傷ぐらい。運が良かったんだよ。{w}出来れば強行突破はやめた方がいいんだけどね…"
    sc "でも稀にこういう選択が必要な時もあるのさ。"
    pl "そう、か…なんか世話になっちまったな。"
    sc "…腕はもう大丈夫そうだね。"
    pl "俺も運が良かったってことよ。"
    sc "さあね、単なる運の問題ではなさそうだけど。"
    pl "どういう意味だ？"
    sc "キミの再生能力が常識外れってこと。{w}そっちの主教に似た様な話を聞いた事はないのかい？"
    pl "主教様が治療を手伝ってくれたとは聞いたんだけどな。"
    sc "治癒術が傷の止血や再生に働くとはいえ、その程度なんだよ。{w}ボクがキミを支えていた時、キミの傷を見たんだ…ボロボロだった。"
    sc "あんな傷がたったの数時間で治るなんてあり得ない。"
    pl "へぇ…前例のないケースってのはこういうことか。"
    sc "まぁ…聖痕が裂けるのは稀にある事なんだけどね。"
    pl "でも怪我を負ったのは腕だぜ？"
    sc "…そういうこと。"
    pl "ハァ、俺ももう何が何だか…"
    sc "昼にも言ったけど、そんな考えこむ必要はないさ。自分で考え込んで答えが出る問題でもなさそうだし。"
    pl "だから昼にも言ったけど、ちゃんと慰めるか癪に障るかどっちかにしろって。落ち着かないんだよ…"
    sc "はいはい、こんな性格で申し訳ございませんでした。で、ボクに相談したいことってこれで終わりかい？"
    pl "…や……まだ時間あるんならもうちょっとだけ付き合ってくれ。{w}お前とちゃんとした会話をするのって実質これが初めてだろ。"
    sc "……"
    nar "沸き起こる気分の悪さを務めて耐えた。単なる気まずさのせいだけではない。"
    nar "あの事件以来、今までずっと彼の顔を見る度にこの気持ちが上がってくる。"
    nar "できれば再び口にしたくはなかったが。今言わないと一生彼との葛藤が解けなくなりそうな気がしてきた。"
    pl "お前さ…誰かと付き合った事ってあるのか？"
    sc "はぁ…急に呼び出しては恋愛の話とか、女の子でもあるまいし…"
    pl "う…うるせ、聞いてるだろうが。"
    sc "相手を見て言いなって、あると思うのかい？"
    pl "そりゃそうだな。"
    sc "急にこんな質問をするのは……あの女のせいで？"
    nar "心臓がひんやりとする。"
    nar "しかし下げていた頭を急に回して向かい合った彼の表情はとても真剣に見えて、頭に湧き上がった血が冷えたから静かに頷いた。"
    pl "やっぱ…知ってたんだな。"
    sc "…知っていた、てよりは推測しただけさ。あの女は常習犯だったからね。"
    pl "こういうことが何度もあったのか？"
    sc "そう、あの日を起点にキミを虐め始めていただろう？分かり易い手段だ。"
    sc "取り敢えず弱みを握っておけば主導権は自分にあると勘違いしてしまうんだよ。"
    pl "じゃあなんで今まで何も言わなかったんだ？あの日のアレは一体何だったんだよ？"
    sc "何をやっても通じないから。アイツらは何かをやらかす時収拾することを一切考えていない。"
    sc "単に自身の興味や、原初的な本能によって動くだけなんだ。"
    sc "そんなもの、亡者と違わないだろう。キミは亡者と話が通じると思うかい？"
    pl "……"
    sc "あと、あの日言った事は…{w}ごめん、注意するつもりが過ぎてしまった。"
    pl "今になって謝るって、お前…"
    sc "……でもあの件でキミに責任や罪を問うつもりはなかったんだ。そうする必要もなかったんだし。"
    pl "…いや、今更怒っても遅いな…どうして毎回そう他人の癪に障るような事ばっか言えるかな。"
    sc "許されたいなんて思ってなかったんだし……"
    pl "こりゃあすげえ。悪党様のお出ましだ。"
    sc "……"
    pl "じゃあ一つ聞くけどさ、お前…これからは俺たちと仲良くしたいってちゃんと思ってるのか？"
    sc "それは…"
    pl "嫌なら嫌って今ハッキリ言いなよ。"
    sc "嫌…って訳じゃないんだけども。"
    pl "ないんだけども？"
    sc "…ボクに聞く以前にキミは一体どう思ってるんだい。"
    pl "お前のやり様によってだな。残念なことに、俺はマヤほど心の広い人ではないんでね。"
    sc "…"
    pl "ま～た黙ってんな。{w}ホラ、グズってないでお前の話でもしてくれよ。"
    sc "…ボクが、"
    pl "何故ならなあ、お前がどれだけ正直に言ってくれるかによって俺の態度も変わるからな。"
    sc "そう他人の言葉を遮って…"
    pl "ド偉い先輩から学びましてね。"
    sc "…言っておくけど、そんなに面白い話は出来ないと思うよ。ボクは口上手じゃないんだし。"
    pl "それぐらい見りゃわかる。{w}じゃあまずは…ふむ…お前どこ出身なんだ？誰も知らないぽかったけど。"
    sc "ここに来る前までは州都外郭の港町で働いてた。"
    sc "ボクを知ってる人が誰もいないのは処理班には同じ出身地から成人になったばかりのヤツらが一括りになって"
    sc "そのまま入ってくるケースが多かったからなんだ。もう聞いた事あるとは思うけど。"
    pl "ヘェ、外郭なら結構遠いんじゃね？何で神殿に入ろうって思ったんだ？"
    sc "それは、まあ…金が必要で。"
    pl "ハァ？{w}カネ？{w}金ですか？？まさかまさかのお前の口から金なんて話が出るとは…"
    sc "な…何だよ、普通のきっかけじゃないか…"
    pl "普通過ぎてビックリギョーテンだぜ…"
    sc "だから面白くないって言っただろう…"
    pl "単に金が欲しいだけならそんな毎日命懸けで働く必要なくないか？"
    sc "始めは金が欲しかっただけだけど、今は補佐教になりたいから。"
    pl "補佐教じゃなかったのか？"
    sc "まだね。{w}神殿の規定上一年以上の経歴のない司祭は補佐教にはなれないんだ。"
    sc "「聖なる夜」と呼ばれる冬の記念日に、神殿は閉ざされた門を開いて州都の結界を整備する。{w}その日なんだ。"
    sc "その日洗礼を受けた司祭のみが正式司祭として認められるんだ…"
    sc "そしてその日を祝うための宴を「聖夜祭」って呼ぶのさ。"
    pl "ほぉ…お前の経歴が一年以下って事実もビックリだけど、そこまで熱心な目標があるなんて知らなかったな。"
    sc "…聖夜祭はボクにとってとても大事な意味のある日なんだ。{w}その日を台無しにはしたくない。"
    sc "キミには理解できないとは思うけど…"
    pl "や、充分理解できるし。大事な目標の為に今努力してるってことだろ？"
    pl "聞きもせずにお前の勝手で他人が何考えてるか断定するなよ。"
    sc "……"
    sc "ごめん…"
    pl "やっと話が通じたな。一ヶ月満たす前にこうなってくれてよかったぜ。{w}お前、いいヤツじゃんかよ～"
    sc "ボ、ボクをおだてたって何も出て来ないからね。{w}コホン…キミたちそろそろ一週間目だろう…仕事はどうなんだい？"
    pl "今日みたいなことさえなきゃ…{w}いや、やっぱまだまだアレだな、魔導部についても同じような感じで…掴めないままっていうか。"
    sc "そう…時間はまだあるから、その間色々考えてみなよ。"
    sc "あの御方がキミに一ヶ月という時間を与えてくれたのには何か意味があると思うから。"
    pl "神のことか？"
    sc "…？主教様のことだよ。"
    pl "お前ってヤツは…ホント司祭向いてないな。"
    sc "うぐっ…"
    pl "だから気に入った。わざわざ時間を割いてくれてありがとな。{w}仕事は大丈夫なのか？"
    sc "一日ぐらい大丈夫さ…って、思いたいね…ともかく、キミも今日はゆっくり休むんだよ。"
    pl "おう、お疲れさん。お前はなんか悩みとかないのか？"
    sc "悩み…？{w}ボクは…"
    if persistent.hk_end or persistent.cheat_happy_end:
        nar "彼は目を落としてはしばらく口を噤んだ。俺はあの表情を知っている。彼はきっと……。"
        hide screen textbox with dissolve
        menu:
            "もっと話したい":
                show screen textbox with dissolve
                sc "……"
                sc "…いや、特にないから。"
                pl "ふーん… そう来ると思った。"
                pl "ところでお前… 酒はイケるか？"
                sc "……は？"
                pl "休日に時間空けろよー。 結局俺の話ばっかしちゃったし… お前ともっと話がしたくてさ。"
                sc "……"
                pl "おい、勘違いするなよ。 「そういうつもり」じゃねぇよ～ マヤも呼ぶから。"
                sc "何の勘違いっていうわけ？ 休日かぁ、 司教様に聞いてみるけど…"
                hide screen textbox with dissolve
                show story21R with dissolve
                show screen textbox with dissolve
                sc "あまり期待するなよ。"
                nar "……！"
                $ sc_happy = True
            "また明日":
                show screen textbox with dissolve
                pl "……"
                sc "……"
                sc "…いや、特にないから。"
                pl "へえ…そっか。{w}後でもいいから絶対言えよ。友達だろ？"
    else:
        sc "……"
        sc "…いや、特にないから。"
        pl "へえ…そっか。{w}後でもいいから絶対言えよ。友達だろ？"
    pl "じゃあ、また明日。"
    sc "…ああ、またね。"
    hide screen textbox with dissolve
    pause 1
    hide SCG_03
    hide story21
    hide story21R
    with slowdissolve
    pause 2
    nvl clear
    show screen textbox with dissolve
    nar "彼が扉を閉じと部屋から出ると、見慣れた部屋の風景がどこか空いているように見えた。"
    nar "誰かに悩みを相談したお陰か、長くも息苦しかった気持ちも久しぶりに元に戻ったように軽く感じられる。"
    nar "もしかしたら只幾つかの返事が欲しかっただけかもしれない。"
    $ _skipping = False
    nar "今日に限っては、早く眠れそうだ。"
    hide screen textbox with dissolve
    pause 2
    nvl clear
    stop music fadeout 5
    $ _game_menu_screen = None
    $ show_quick_menu = False
    hide screen at_frame
    scene black
    with slowdissolve
    $ _dismiss_pause = False
    pause 2
    if sc_happy == True:
        jump sc_end_happy
    else:
        jump day6_rkn
    return

label day5_night:
    if hssh_rkn == True:
        jump day5_night_rkn
    $ save_name = "day 5, 夜"
    scene bg02_2 with dissolve
    pause 1
    nvl clear
    $ show_quick_menu = True
    scene bg10_2 with dissolve
    stop music fadeout 3
    call place10 from _call_place10_5
    pause 1
    show screen nvlbox with dissolve
    "\n 一日中多くの人と出会ったが、一人で寂寞な部屋にいるのは相変わらず落ち着けない。"
    "一日中誰かと一緒にいたせいで更にそう感じてしまう。"
    "俺はベッドに腰をかけて、窓から入ってくる光に腕を照らしてみる。"
    et "腕に刻まれた黒色の残痕がインクに染まったように少しの色つやを出し光っていた。"
    nvl clear
    "\n 村の人は最初は幼い俺についていろんな話を交わったが、そういう心配にも関わらず俺はこの残痕が刻まれたまま大人になった。"
    "そうこうしているうち自然に俺の残痕に関した疑問や噂は消えて、それは俺の中でも同じだった。"
    "俺にして当然なことが、他の人には全くそうではないなんて考えてもいなかった。"
    et "当然見えない物、当然そこにあった物。その全てが突然変わってしまうのはまだ俺には難しいものだ。"
    nvl clear
    "\n 虚しくなってやたらに横の壁を二回叩いた。中身の空いた音がする。{w}ちらっと出張った壁紙の下の小さな隙に何度も声をかけてみた。"
    "しかし返答がないばかりか、人気さえも感じられない。{w}奴はまだ帰ってきてないってことか。まじめな奴。"
    play sound "audio/se/knock.ogg"
    "もう一回叩く為に手を上げると、まだ壁に手が触れてもいないのにノック音が聞こえた。"
    "その音は扉の向こうからしていた。{w}いきなりの訪れに、まだ誰なのかも知らないのに胸が騒いでしまう。"
    et "さっきまでの虚しさが大きかったせいだ。"
    nvl clear
    "\n 彼女がそこに立っているんだ。{w}訳の分からない確信は体に血を回せた。"
    "俺は高鳴る心拍を努めて落ち着けながら扉を開いた。{w}正に彼女がそこにいた。"
    "扉が開くことを当然だと思っていたかのように最初から俺を見つめていた。"
    et "心臓はまだ鼓動する。{w}しかし俺もまた同じく、彼女の訪れを当然だと思っている。"
    hide screen nvlbox with dissolve
    show SCG_02 0 with dissolve
    show screen textbox with dissolve
    my "夜分遅くにごめんね、[na2]くん。"
    pl "いや…大丈夫。{w}どうした？"
    show SCG_02 8 with fastdissolve
    my "…実は聖痕のことが気になって…呪術、詠ったのはわたしだから…{w}なにかあったらどうしようって不安になっちゃったの。"
    pl "そうだな…保健部の人たち、まだ起きてるかな？良かったら一緒に…"
    hide SCG_02 with dissolve
    nar "マヤは静かに口を噤んでそっと俺を見上げた。{w}少し不安がっているように、丸い瞳が微細に震えた。"
    nar "俺はこの表情を分かっている。{w}今日までずっと彼女のことを見ていたからだ。俺に何かしてほしいっていう顔だ。"
    nar "一緒に口を噤んだ俺が彼女と目を合わせても、彼女が退くことはなかった。"
    nar "寧ろ部屋に入っても良いって許しを求めるように一歩踏み出した。"
    nar "垂れ込めた月明りに長く伸びた二人分の影がゆっくりと重なる。"
    hide screen textbox with dissolve
    pause 1
    show story09 with slowdissolve
    pause 2
    nvl clear
    show screen nvlbox with dissolve
    play music "audio/bgm/train meet.ogg" fadein 1 
    "\n「診るだけだよ」"
    "俺の緊張を慰めるような、自分の不安を窘めるような一言が頭の中に入ってくる。"
    "「わかってる」、やたらに強く目を閉じてしまう。"
    "何も見えないままで、只彼女の許しを、息を殺して待っている。"
    et "「何か変なところがないか、よく見てもらっていい？」"
    nvl clear
    "\n 俺は目を開いた瞬間、俺の汚い不安感と先走った心配が全く要らないものだって分かった。"
    "女の子が、小さな背をこちらに向けて外の光を浴びている。{w}脊椎と肩甲骨が鮮明に見える。"
    "その真っ白の屈曲に二つの傷跡がかかっている。"
    "痕跡だ。{w}さっきまでの自分がどんな姿をして、どんな考えをしていたのかがもう覚えられないほどに頭は冷めていた。"
    $ renpy.music.set_volume(0, channel="music")
    hide screen nvlbox
    play sound "audio/se/noise.ogg"
    show cg08 at ns
    pause 0.1
    stop sound
    hide cg08
    show screen nvlbox
    $ renpy.music.set_volume(1, channel="music")
    et "その感覚が驚くほどに気楽だ。"
    $ renpy.music.set_volume(0, channel="music")
    hide screen nvlbox
    play sound "audio/se/noise.ogg"
    show cg08
    pause 0.1
    stop sound
    hide cg08
    show screen nvlbox
    $ renpy.music.set_volume(1, channel="music")
    pause 0.1
    $ renpy.music.set_volume(0, channel="music")
    hide screen nvlbox
    play sound "audio/se/noise.ogg"
    show cg08:
        yoffset -400
        zoom 1.2
    pause 0.2
    stop sound
    hide cg08
    show screen nvlbox
    $ renpy.music.set_volume(1, channel="music")
    scene black
    hide screen nvlbox
    pause 0.5
    play sound "audio/se/memory.ogg"
    show story08:
        yoffset -100
    call bgw from _call_bgw_9
    pause 1.0
    hide story08
    show story09
    with dissolve
    show story08R:
        alpha 0.01
    pause 0.1
    hide story08R
    pause 1
    show screen nvlbox with dissolve
    nvl clear
    "\n 俺は去って行った天使の夢を思い出した。{w}これは痕跡だ、それも本来羽があるべきだった痕跡。"
    "これが無礼なことだって分かっていても思わずそう思ってしまった。"
    "近くで見る度に息が苦しくなってきた。{w}結局頭を下げてしまう。{w}俺なんぞは到底彼女に触れられない。"
    "息の触れる感覚、{w}無理やりに息を飲む音、"
    et "存在を隠せなかった気配まで全部彼女が今感じているという事実が、耐えられないほど恥ずかしい。"
    nvl clear
    "\n 「何ともない？」"
    "彼女の背が丸く曲がり、俺は脳裏を叩くぞっとする感覚と共に気を戻す。"
    "穏やかな所から強いて突き飛ばされてどこかに落ちているような、覚えのある感覚だ。"
    "一時の夢を見たのかもしれない。"
    "「ん、大丈夫。何ともない。」"
    "そうだ、何ともない。{w}俺は再び目の前の聖痕を見てはふんわりと浮かんだ精神を戻した。"
    $ _skipping = False
    et "まだその余韻が忘れられないみたいに、心臓に血が忙しく回った。{w}まるで崇高な儀式を澄ましたようだ。"
    hide screen nvlbox with dissolve
    pause 2
    nvl clear
    stop music fadeout 5
    $ _game_menu_screen = None
    $ show_quick_menu = False
    hide screen at_frame
    scene black
    with slowdissolve
    $ _dismiss_pause = False
    pause 2
    jump day6
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
