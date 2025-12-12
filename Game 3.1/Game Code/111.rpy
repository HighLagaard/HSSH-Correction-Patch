label dmy_x:
    play sound "audio/se/hit.ogg"
    show none with sshake
    hide none
    return

label dmy_day:
    if persistent.dmy == 1:
        jump dmy1
    if persistent.dmy == 2:
        jump dmy2
    if persistent.dmy == 3:
        jump dmy3
    if persistent.dmy == 4:
        jump dmy4
    if persistent.dmy == 5:
        jump dmy5

label dmy_end:
    if persistent.dmy_off == False:
        $ _skipping = False
    else:
        $ _skipping = True
    $ _game_menu_screen = 'preferences'
    show screen at_frame
    scene bg10_3:
        xzoom -1.0
    show SCG_02 A 00 100
    show screen textbox
    my "[na2]くん？"
    my "[na2]くん、どこいってたの？マヤ…[na2]くんが急に消えちゃってびっくりしちゃったの。"
    my "[na2]くんは身体が不自由だし、ここはマヤしかいないんだから、わたしを置いてっちゃだめだよ。"
    my "えーっと…どこまでお話したっけ…"
    hide screen textbox 

    with dissolve
    jump dmy_day

label dmy_skip:
    $ _skipping = False
    hide screen nvlbox with dissolve
    show bg10_3 as bg1 with dissolve:
        xzoom -1.0
    show SCG_02 A 00 100 with dissolve
    show screen textbox with dissolve
    my "…どうしたの？[na2]くん。さっきから集中出来てないじゃない。"
    my "マヤとお話するの、楽しくない？"
    show SCG_02 2 with fastdissolve
    my "…[na2]くんはよく分からないかもしれないけど、かわいい女の子の前で他のことを考えちゃうのはすごく無礼なことなんだよ。"
    my "お話に戻ろっか。"
    $ persistent.dmy_skip_seen = True
    nvl clear
    "{nw}"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    pause 1
    hide bg10_3 as bg1 with dissolve
    show screen nvlbox with dissolve
    return

label dmy_menu:
    $ persistent.dmy_skip_seen = False
    $ _game_menu_screen = None
    hide screen quick_menu_dmy with dissolve
    menu:
        "マヤが好き":
            if persistent.dmy <= 1:
                nvl clear
                stop music fadeout 5
                $ _game_menu_screen = None
                $ show_quick_menu = False
                hide screen at_frame with dissolve      
                scene black
                with slowdissolve
                $ _dismiss_pause = False
                pause 2
                play sound 'audio/SE/bell 4.ogg' fadein 4.0
                image qday = Text("？？day",antialias=True, size=48,font="SoukouMincho.ttf")
                show expression 'qday' at day00 with slowdissolve
                pause 5
                hide expression 'qday' with slowdissolve
                stop sound fadeout 1.0
                $ _game_menu_screen = 'preferences'
                nvl clear
                jump dmy2
            if persistent.dmy == 2:
                nvl clear
                stop music fadeout 5
                $ _game_menu_screen = None
                $ show_quick_menu = False
                hide screen at_frame with dissolve      
                scene black

                with slowdissolve
                $ _dismiss_pause = False
                scene black with dissolve
                pause 2
                play sound 'audio/SE/bell 4.ogg' fadein 4.0
                image qday = Text("？？day",antialias=True, size=48,font="SoukouMincho.ttf")
                show expression 'qday' at day00 with slowdissolve
                pause 5
                hide expression 'qday' with slowdissolve
                $ _game_menu_screen = 'preferences'
                stop sound fadeout 1.0
                nvl clear
                jump dmy3
            if persistent.dmy == 3:
                nvl clear
                stop music fadeout 5
                $ _game_menu_screen = None
                $ show_quick_menu = False
                hide screen at_frame with dissolve      
                scene black

                with dissolve
                pause 2
                play sound 'audio/SE/bell 4.ogg' fadein 4.0
                image qday = Text("？？day",antialias=True, size=48,font="SoukouMincho.ttf")
                show expression 'qday' at day00 with slowdissolve
                pause 5
                hide expression 'qday' with slowdissolve
                $ _game_menu_screen = 'preferences'
                stop sound fadeout 1.0
                nvl clear
                jump dmy4
            if persistent.dmy == 4:
                nvl clear
                stop music fadeout 5
                $ _game_menu_screen = None
                $ show_quick_menu = False
                hide screen at_frame with dissolve              
                scene black

                with dissolve
                pause 2
                play sound 'audio/SE/bell 4.ogg' fadein 4.0
                image qday = Text("？？day",antialias=True, size=48,font="SoukouMincho.ttf")
                show expression 'qday' at day00 with slowdissolve
                pause 5
                hide expression 'qday' with slowdissolve
                $ _game_menu_screen = 'preferences'
                stop sound fadeout 1.0
                nvl clear
                jump dmy5
        "マヤが嫌い":
            jump day12

label day11:
    $ save_name = "day ？？？"
    $ _skipping = True
    $ persistent.dmy = 1
    $ day = 11
    pause 1
    nvl clear
    scene bg10_3 with slowdissolve:
        xzoom -1.0
    call place10_2 from _call_place10_2_2
    show screen textbox with dissolve
    show SCG_02 A 1 100 with dissolve
    play music "audio/bgm/maya.ogg" fadein 3
    my "おはよう。"
    my "おそと、まだ暗いね。"
    my "夜は暗いからきっとこわいことが起こっちゃうんだ…"
    my "朝日が昇るまでずっといっしょにいてくれる？"
    hide screen textbox with dissolve
    pause 1 
    menu:
        "うん。":
            pause 1 
            hide SCG_02 with slowdissolve
    jump dmy1

label dmy1:
    pause 1
    nvl clear
    show screen nvlbox with dissolve
    "\n 再度訪れたマヤの部屋は最後に来た時の印象が薄まるぐらいに滅茶苦茶だった。"
    "薄いベッドの上には服や靴下、くしゃくしゃになったシーツが無造作に置かれてて、"
    "地面には出所が分からない紙切れや濡れたタオルで一杯だ。"
    "しかもそのタオルのせいなのか、狭い部屋に湿気が溢れてて歩く度に足がベタついた。"
    et "カーテンを閉めたままの窓からは光など一切入り込みやしない。その暗い部屋の中で、俺達の生活が始まる。"
    nvl clear
    "\n 「[na2]くん、腕痛そうだね…"
    "ちょっと見てもいい？」"
    "ゆっくり近づいてきたマヤが俺の腕をじっくり見た後、クローゼットの中から救急箱を取り出す。"
    "俺の部屋でもクローゼットを開ける度見かけたことはあるが、直接開けた事は無かった。"
    "腕を中心に始まったズキズキする痛みは全身を貫く。{w}赤黒い血が粘り付いた包帯をマヤが解くと未だにぐちゃっとした音がする。"
    "「っ…」"
    "マヤが動きを止めた。"
    "「痛いの？」"
    et "「少し…」"
    nvl clear
    "\n 知らずぐっと閉じた眼を開くと同時に、俺はその答えを後悔することになった。"
    "包帯を持ったマヤが無の表情で俺を見つめていた。"
    "「あのね、幸せな人はどんな時でも痛みを感じないらしいよ。"
    "[na2]くんはマヤのことが好きだから…いま幸せだよね？」"
    "身体が震え、固唾を飲み込む。"
    et "しかし俺に出来る答えなど一つしか無かった。{w}何故なら、俺はマヤのことが好きだから。"
    nvl clear
    stop music fadeout 3
    scene black with slowdissolve
    play sound "audio/se/r18 2.ogg"
    pause 2 
    nvl clear
    play music "audio/se/no more bell my buddy.ogg" fadein 5
    "\n 「うん。」"
    "その答えが正解だったのか、マヤの表情が穏やかに解れる。"
    "俺はまだ実感していなかったが、この会話はこれから起こる恐ろしい事への合意と一緒だった。"
    "マヤはハサミを一つ手に取る。{w}本来包帯を切るための物だったが、精一杯に開いたハサミの刃は俺に向かった。"
    nvl clear
    "\n 「わたしたちの体には神聖が流れているけど、{w}わたしたちは信仰を持って生きていくから、こんな祝福を受けたんでしょう。"
    "だから[na2]くん、一瞬たりとも疑ってはいけないの。{w}信仰は信仰から来るもの。"
    et "不信の瞬間…この祝福は腐っちゃうよ。{w}そんなの嫌でしょ？」"
    nvl clear
    "\n 俺は腰の上に乗った彼女を見上げながら頷いた。{w}もちろん完全に俺の意志が込められたのではなく、決まった答えをするだけだった。"
    "冷たい刃物が広がった傷跡の間に入り込んでくる姿に、俺は思わず口をつぐむ。{w}悲鳴を上げるのを我慢するためだった。"
    et "新しく刻まれた傷から一筋の血が流れ落ちる。{w}その鮮やかな赤に、俺は徐々に怯え始める。"
    nvl clear
    "\n その震えをマヤも感じたはずだ。{w}彼女はハサミを片手に持って、俺の脚の下に掛けていたスカートを持ち上げた。"
    "元々真っ白だったはずのドロワーズが赤黒く染められている。息を少し呑めば以前も嗅いだことのある鉄臭さが鼻を突く。"
    "「ほら…マヤにも血が出てるでしょう？{w}[na2]くんが前に言った通り、わたしたちは同じだよ。"
    et "一緒にいれば幸せになれる」"
    nvl clear
    hide screen nvlbox with dissolve
    pause 2
    show dmy1 with slowdissolve
    pause 2
    show screen nvlbox with dissolve
    "\n 俺は彼女を見上げながら、もう一度頷く。{w}窮地に追い込まれたように信頼を渇望する目で俺を見る彼女の姿は、"
    "恐怖よりも同情心を呼び起こした。速くなった心臓の音が徐々に落ち着いていく。"
    "マヤは続いて手を動かした。熱い肌を切り裂く冷たい感覚に俺は時々身震いした。"
    et "そうしている内に苦痛が麻痺し、頭が朦朧としてきたが、少しでも手の力を抜けば苦痛で腕が熱くなった。"
    nvl clear
    "\n「痛くないよね…？」"
    "「うん、痛くない…」"
    "乱れた髪が脂汗でべったりとした頬や額にへばりついて、マヤの顔は見えなかった。"
    et "しかしその表情には慈愛と満足が溢れている……{w}筈だった。{w}そうであるべきだった。"
    nvl clear
    "\n 長い間緊張していたせいか、筋肉が痙攣して震え始める。{w}マヤの手も同様に震えている。ハサミの刃は刀よりもろい。"
    et "マヤは血を出すために何度も同じところを切り付け、表皮をむいて皮をむく。{w}襟足にかかったお互いの吐息が獣のように荒かった。"
    nvl clear
    "\n 「今日のことは忘れないでね」"
    "マヤは未だに震えている手でハサミを動かした。{w}空中で音を出す刃物を見ると、"
    "いつか庭園のハサミで枝を切り取っていた彼女の姿が浮び上がった。{w}マヤはもう二度とあの庭園に行かないだろう。"
    et "俺はその時にやっと俺たちを包み始めた絶望の存在を実感する。{w}俺たちがあまりにも遠くに来てしまったということも。"
    hide screen nvlbox with dissolve
    nvl clear
    pause 1
    hide dmy1
    with slowdissolve
    pause 2
    show black with dissolve
    pause 1.0
    show screen nvlbox with dissolve
    "\n 腕をぎっしり埋めた赤い線、広がった傷跡から引き続き血が流れている。"
    "熱が上がり熱くなった腕は、ずきずきと遅く苦痛を訴える。{w}それは間違いなく「痛み」だった。"
    "しかし、俺がその苦痛に声を出すことはなかった。"
    et "熾る様に充満した血の生臭さがマヤの匂いと混ざっては、静寂の部屋を満たす。"
    stop sound fadeout 2
    $ renpy.music.set_volume(1, channel="sound")
    hide screen nvlbox with dissolve
    nvl clear
    pause 1
    scene bg10_3 with slowdissolve:
        xzoom -1.0
    show SCG_02 A 0 100 with dissolve
    show screen textbox with dissolve
    my "[na2]くん、お腹空いたよね？"
    pl "ちょっとな…"
    nar "忘れ掛けていた空腹が襲ってくる。{w}ここ数日ずっと食事を取っていなかったな。"
    nar "血を流しすぎたためか、全身に力が入らない。指一本動かせない。"
    nar "視界に映るのは暗い天井だけ。マヤの声は比較的近くから聞こえてきた。"
    show SCG_02 1 with facedissolve
    my "パンあるよ。"
    pl "ん…？いつ持ってきたんだ？"
    my "何個か部屋に置いて食べてたの。{w}食堂いくのがイヤで…"
    nar "ガサガサと布に柔らかい何かが擦れる音が聞こえる。{w}パンを取り出しているのだろうか。"
    my "そうだ、[na2]くん。"
    my "州都には食前に祈りを上げる習慣があってね、ごはん食べる前に神様に祈りを捧げなきゃだめなんだ。"
    pl "俺が住んでたとこにも似たようなのあったなあ。"
    pl "たとえば、食卓に上がった動物や植物に感謝する…{w}そういうの。"
    show SCG_02 7 with facedissolve
    my "わたしはそれあんまり好きじゃなかったの…{w}食材になった子たちに勝手に感謝するなんて欺瞞でしょう。"
    my "神に感謝するとかもそうだし。"
    pl "縋るところが他にある人も祈りは捧げるのかな？"
    show SCG_02 00 with facedissolve
    my "祈りって人の心構えみたいなものらしいよ。"
    my "今日の幸運を念押ししてくれる運勢とか、縁結びの術とかも…{w}結局同じもの。"
    show SCG_02 4 with facedissolve
    my "だから[na2]くん、今度はマヤに感謝すればいいよ。"
    pl "もちろん。{w}ありがとう、マヤ。"
    hide SCG_02 with dissolve
    nar "彼女の笑い声と共に、すぐさま口に冷たくて固いパンが入ってくる。"
    nar "最初はかび臭い麦の味ばかりだったパンの味が、途中から変わってくる。"
    nar "まるで鉄を舐める様な苦さとしょっぱさ。{w}それを感じた次の瞬間生暖かくてぬめっとした何かが歯に触った。"
    nar "完全に噛み切る前に歯の間をすり抜けていったそれはだまになっているがちゃんとした形が無くてふにゃついている。"
    nar "しかし崩れたり溶けることなく、少しばかりの粘りを残しつつ舌の上をゼリーの様に転がり回った。"
    nar "直ぐに喉奥へと通るぐらいには軽いが、息が詰まるような生臭さが食道を防ぐ。"
    $ _skipping = False
    nar "少ない量の食事で起きてしまった胃がぐうっと音を出す。"
    $ renpy.music.set_volume(1, channel="sound")
    hide screen textbox with dissolve
    pause 2
    nvl clear
    stop music fadeout 2
    scene black with slowdissolve
    pause 2
    call dmy_menu from _call_dmy_menu
    return



label dmy2:
    $ preferences.afm_enable = False
    $ persistent.dmy = 2
    if persistent.dmy_off == False:
        $ _skipping = False
    else:
        $ _skipping = True
    show screen at_frame  with dissolve
    show screen quick_menu_dmy with dissolve
    scene bg10_3 with slowdissolve:
        xzoom -1.0
    call place10_2 from _call_place10_2_3
    show screen nvlbox with dissolve
    play music "audio/bgm/r18.ogg"
    "\n ドアの閉じる音で目が醒める。"
    "マヤはたまに、俺が寝ている間部屋の外に出る。だからと言って人に逢ったり単純に外の空気を吸いに行ってる訳ではない。"
    "彼女はここ数日、部屋の外を恐れるようになった。{w}「他人」や「神殿の事」は一切口にしない。"
    "過去を思い出させる光も、外を思い出させる外の空気も、俺ではない誰かの顔でさえ彼女を狂わせる要因となった。"
    "そんなマヤが外出するのは絶対に必要な物が出来た時だけだった。"
    et "一緒に行けばいいのに。しかしマヤは俺が部屋を出るのは勿論動くのすら嫌がる。"
    nvl clear
    "\n 会話はもう言うまでもなく彼女が主導権を握っている。"
    "暗い部屋で二人きり、たった二人だけが分かる会話を分かち合いながら過ごす日々は過去を忘れさせてくれる。"
    et "まるで最初からこの世界には俺達二人だけで、今までの生活が夢だったみたいに。"
    nvl clear
    "\n「マヤ、どこ行ってたんだ？」"
    "「お料理。」"
    "お料理？{w}意味が解らず聞き返せば、彼女は面白いことを思いついた子供のようににんまりと笑う。"
    "そして背後に隠していた何かを取り出した。"
    "平べったい形の箱だった。{w}中身が溢れ出ているのか透明な油の様な物で濡れている。"
    et "好奇心で覗き込んでいた箱が開いた瞬間、俺は息を呑んだまま固まってしまった。"
    nvl clear
    hide screen nvlbox with dissolve
    pause 2 
    nvl clear
    pause 1
    show dmy2 with slowdissolve:
        zoom 1.7
        xalign 0.5
        yalign 1.0
    pause 2
    show screen nvlbox with dissolve
    "\n 中に入っていたソレは、一見黒い塊の様に見えた。うねうねと動いている。"
    "蟲だ。{w}箱の中は蟲で一杯だった。"
    "箱の中にたっぷりと振り掛けられた油のせいか、テカテカと光を帯びた蟲共は必死に壁を登っては滑り落ちるを繰り返す。"
    "お互いを踏みにじり、喰らっているのか形がまともでない死骸が底に沢山沈んでいる。{w}木が腐ったような臭いがした。"
    "「お互いを食べ合ってるのね。"
    "『食材に感謝するキモチ』なんて良くわかんないけど、生命を頂くっていうのは素敵。"
    et "こんな子たちの命を頂けたらずっとずっと生きられるだろうね…」"
    nvl clear 
    "\n マヤはその内の一匹をつまんでは、俺につき出した。"
    "それが何を意味するかはすぐに分かってしまった。"
    "「こ、こんなの食べられるワケがないだろ…」"
    "「どうして…？」"
    "マヤは怯える俺を見ては、つまんでいた虫を自身の口に入れる。"
    "ボリ…ボリ…{w}固い何かが砕ける音が妙に耳に張り付く。"
    et "外にはみ出た黒い脚を口の中に戻す姿に吐き気がする。{w}マヤはそんな俺がかえって理解できないのかきょとんとした顔のままだ。"
    nvl clear
    hide screen nvlbox with dissolve
    pause 2
    show dmy2 with slowdissolve:
        zoom 1.0
        xalign 0.5
        yalign 0.5
    pause 2
    show screen nvlbox with dissolve
    "\n「ほら…たべて…"
    "マヤが作ったおべんとう、たべて…」"
    "マヤが片手一杯に握ったねっとりとした蟲共がひとつ、ふたつと指から零れ落ちていく。"
    "地面に、腕に這う蟲共がすぐ目の前でうじゃうじゃと蠢く。"
    "ぐっと食いしばる歯が震える。{w}首を左右に振りつつその手を拒めば、マヤは膝で地を這いながら俺に更にくっ付いてくる。"
    "「たべて、たべてよぉ」彼女は何度も手を上に上げ、何度も同じ言葉を繰り返しぼやいている。{w}とても切実に哀願している。"
    et "こうなった彼女に言葉は通じない。その曇った目に俺は映らない。乾いて裂けた唇が震えている。"
    nvl clear
    "\n 怖い。{w}俺までもが彼女を手放してしまえば、彼女はどうなってしまうのだろう。"
    "閉じた口がゆっくり開けば、チクチクとするものが入り込む。"
    "少しずつ動いていたソレは、俺が前歯を閉じたのが最後、それ以上動かなくなってしまった。"
    "ぬめっとした湿気ある何かが口の中で砕け、長い触角が喉仏に障る。"
    "胴体に反して小さめの頭が感じられる。{w}石油か絵の具っぽい、妙な臭いがする。"
    et "すぐにでも吐き出したかったが、舌に障るチクチクとした毛のせいで飲み込むことも、吐くことも許されないまま口を閉じた。{w}全身に寒気が走る。"
    nvl clear
    "\n びくっ、口の中で真っ二つになったはずの蟲が動いた。その瞬間俺は耐え切れずそれまで食べた全てを吐き出してしまった。{w}鼻に引っかかった塊のせいで喉が痛む。"
    "さらさらとした吐瀉物が目の前のマヤに、彼女が持っていた蟲の箱に降り掛かる。"
    "吐瀉物に埋もれ脚をバタつかせる蟲共は元より浸っていた油と共に交わり合って、段々と痙攣するように体を震わせるかと思えば動きが鈍くなっていった。"
    "死にかけているんだ。{w}その姿が気持ち悪い。また吐き気がしてくる。"
    "「……」"
    et "頭から始め顔、服にまで吐瀉物まみれになったマヤはあっけない顔で箱の中の光景を見守る。{w}動きが途切れたまま言葉も発しない。"
    nvl clear
    "\n「あのさ、マヤ…」{w}恐怖が収まると心配が押し寄せてくる。"
    "気を遣う様に話し掛けると、青白い顔色の彼女はまた顔を上げる。{w}目が合うと体が震えた。"
    "じっと座っていた彼女は、そっと両腕を前に差し出す。"
    "「たべて」"
    "マヤの返事は変わりなかった。"
    "「たべて…たべて、全部たべて…」吐瀉物と蟲の死骸が波打つ汚い箱が俺の前に差し出される。"
    "冷たい絶望感が全身に染み付いた。"
    et "最後まで口に残ったのはやはり、苦くてぐにゃっとした、少しの甘さと酸味を感じさせる吐瀉物の味だった。"
    hide screen nvlbox with dissolve
    nvl clear
    hide screen nvlbox with dissolve
    pause 1
    hide dmy2
    with slowdissolve
    pause 2
    show black with dissolve
    pause 1.0
    hide black with dissolve
    show screen textbox with dissolve
    my "…あぁ！"
    nar "散らかった床を片付けていると、布団にくるまってぼーっとしたままだったマヤが断末魔の様な声を上げた。"
    show SCG_02 A 7 100 with dissolve
    my "家に戻りたいなんて思っちゃった、恐ろしいわ。"
    pl "ここが家だろう。"
    my "……"
    show SCG_02 00 with fastdissolve
    my "[na2]くん、元からお話出来るような友達がいないって言ってたよね。"
    pl "うん、故郷に同い年の子が少なくてさ。"
    my "その方が良かったのかもしれないね…{w}わたしね、小さい村で育ったから幼い頃からたくさんの子たちと遊んだの。"
    my "まあまあ楽しかったんだけど…大きくなってくにつれてだんだん会話に混ざりにくくなってたんだ。"
    my "みんな恋愛とか男の話で忙しくなっちゃって。"
    show SCG_02 8 with fastdissolve
    my "…その頃からわたしは『普通』がわからなくなっちゃったんだ。"
    my "何がそんなに楽しいんだろうね、自分を蔑んで、今の自分の人生を狂わせてもいいぐらいなのかな…"
    show SCG_02 7 with fastdissolve
    my "嫉妬…とはやっぱり違うんだ。{w}わたしも小さい頃は普通に男の人に逢って、結婚して、普通に初夜を迎えると思ってたから。"
    my "幸せに…{w}[na2]くんも思ったことある？"
    pl "あるかもな…故郷に居た頃は俺も普通に女と出逢って結婚して、家を買う…{w}みたいなこと考えてたからさ。"
    my "それはなんでだろうね…それが完璧な生き方だからかな？"
    pl "完璧な生き方ってなんだろうな？"
    my "完璧な生き方というのは、汚点の存在しない生のこと。{w}後悔も無くて、自慢できるような、そんな生き様…"
    pl "愛する恋人と、二人っきりで同等な生活ができるのがその完璧な生き方ってなら…今と別段変わらないな。"
    show SCG_02 8 with fastdissolve
    my "わたし疲れてたんだ…すごくつまらなかった。{w}生きるのをやめたかったの。"
    my "すぐにでもわたしを連れてずっと遠くに行ってほしかったし、同時に隅に追い込んでほしくもあったんだ。"
    my "粗末に扱われたいなんて思ってたんだ。{w}[na2]くんはそう考えたことない？"
    pl "俺…まず大事にされたことがないからわかんねえや。"
    show SCG_02 1 with fastdissolve
    my "あの日、わたし…嬉しかった。{w}今もしあわせ。本当に満足してるんだ。{w}この時間がずっと終わらなければいいのに…"
    show SCG_02 8 with fastdissolve
    my "………もう寝る。"
    hide SCG_02 with dissolve
    hide screen textbox with dissolve
    pause 2
    nvl clear
    stop music fadeout 2
    scene black with slowdissolve
    pause 2
    call dmy_menu from _call_dmy_menu_1
    return

label dmy3:
    $ preferences.afm_enable = False
    $ persistent.dmy = 3
    if persistent.dmy_off == False:
        $ _skipping = False
    else:
        $ _skipping = True
    show screen at_frame  with dissolve
    show screen quick_menu_dmy with dissolve
    scene bg10_3 with slowdissolve:
        xzoom -1.0
    call place10_2 from _call_place10_2_4
    show screen quick_menu_dmy with dissolve
    show screen nvlbox with dissolve
    play music "audio/bgm/r18.ogg"
    nvl clear
    "\n ブンブンと飛び回る音が耳元から離れない。"
    "その音は目の前の幽霊のような影が揺れ動く度大きくなったり、小さくなるのを繰り返す。"
    "俺は固まった首を動かしてやっとそれが自身の腕に付いた蠅だという事に気付く。"
    "とうの昔に固まってるべき血は未だにどろっとした粘性が残っている。{w}しかし血は流れず真っ黒に変色していた。"
    et "腕が腐り掛けている。{w}俺が天使の存在を疑ったからだ。"
    nvl clear
    "\n 新しい空気が回らない息苦しい部屋で、朦朧とした精神で彼女の背を見つめる度俺は彼女に対する不信を抱いた。"
    "それが許されざる行為だという事は自分でもわかっていた。{w}だから俺の神聖は穢れたんだ。"
    "臭いはいつものことで慣れてしまっていたし、痛みを感じないため長らく腕を動かしていなかったから気付いてもなかった。"
    et "その傷の裂け目から卵でも産んだのか、俺が動く度新しい蠅が出てきて周りを飛び回る。"
    nvl clear
    "\n「[na2]くん、傷見せて。」"
    "俺が不便を感じていたからか、マヤが近寄って腕を拭き取る。"
    "赤黒く変色したティッシュがマヤの膝辺りまで来る頃、血交じりの膿が滲み出る。"
    "水すら付けて貰えなかった粗いティッシュはどろっとした腕を拭けば拭く程粘り付き、やがては固まっていく。"
    "俺はずっとその苦痛に耐え凌ごうと唇を噛んだ。"
    "「痛い？」"
    "「いや…大丈夫。」"
    et "突如顔を上げた彼女は俺をじっと見やっては、俺の顔に手を差し伸べ顎と頬辺りを撫で始めた。"
    nvl clear
    "\n 温くて生暖かい手の感触に連れビリっとした痛みを感じる。{w}吃驚して見つめる彼女の指の間には一本の毛があった。"
    "「マヤ、ひげの生えた男はキライ。」"
    "顎に触ると、本当にごわごわとした毛がいくつか生えていた。"
    "普段は綿密に管理していたのに、ここ数日鏡はおろかトイレにも行けた事がない。{w}当然のことだ。"
    et "じめっとした湿気のせいで肌は常にねっとりしていて、体のあちこちが痒い。{w}俺は今どんな姿なんだろうか。急に羞恥心が押し寄せてくる。"
    nvl clear
    "\n マヤは散らかった床を膝で這いつつ、何かを探るように見回してはすぐ髭剃りを一つ持ってくる。"
    "マヤは何でも持ってるんだな、小さく感心すると彼女は恥ずかしいのか少しばかり眉を顰める。"
    "「泡は出せないから、気を付けないと。」"
    "冷たい刃が顎に触れて、ゆっくりと肌の上を滑っていく。"
    "特別痛い訳ではない。"
    "俺は元々髭があまり生えない方でもあるのだが、しかしマヤはそこからもっと綺麗に剃りたいのかたまに刃を俺の皮膚まで捩じり込ませる。"
    et "その度緊張で顎が震えた。"
    nvl clear
    "\n「綺麗になったよ。」"
    "「ゴメンな、自分でやらなきゃなのに…」"
    "「ううん、必要な物があったら言ってくれる？」"
    "『外に出してくれ』なんて聞き入れて貰えないだろうな。"
    "「じゃあ、トイレに行きたいんだけど…」"
    "「うん。」"
    "平然とした返事とは裏腹に、マヤは扉の反対側へと向かっていく。{w}ベッドの隣にずっと置かれていたバケツ。"
    et "本来ならトイレか倉庫にでもありそうなものが、何故あんなところに置いてあるのかずっと気になっていた。"
    nvl clear
    "\n マヤは俺の目の前にそのバケツをぽつんと置いては、座ったまま何もしてこない。{w}俺はバケツとマヤを何度か交互に見ては、不吉な予感に聞き返す。"
    "「あのさ、マヤ、トイレは…」"
    "「先に準備しておいたの、[na2]くんと一緒に住むんだから」"
    "「こ…こんなん使えるワケがないだろ！」"
    "無意識に声を荒らげてしまう。{w}マヤは驚いた顔で目を大きくしてはびくりと震えた。"
    et "その姿に罪悪感を覚えた俺は謝ろうと思ったが、眉を悲しげに下げたマヤが先に口を開く。"
    nvl clear
    "\n「ヒドイ……"
    "マヤ、[na2]くんのためにずっとずっと頑張ってるのに…[na2]くんは毎日不満ばっかり…」"
    "マヤは鼻をすすりながら泣き始める。{w}しまった。{w}その考えで頭が埋まっていった。"
    "「ゴ…ゴメン、マヤ。泣かしたいワケじゃなかったんだ！{w}俺はただ…{w}」{nw}"
    et "「黙ってよ！」" with sshake
    nvl clear
    hide screen nvlbox with dissolve
    pause 2 
    nvl clear
    pause 1
    show dmy3 with slowdissolve:
        zoom 2.0
        xalign 0.75
        yalign 0.7
    pause 2
    show screen nvlbox with dissolve
    "\n ガン、視界がひらめき、頭から鉄の音がした。"
    "次に肩を震わせながらバケツを手に持った彼女を見て、その時にやっと俺が殴られたという事実に気づく。"
    "体重をすべて積んだ攻撃だった。鋭い耳鳴りが耳を突き抜けて通り、体は傾いて床に座り込んだ。"
    nvl clear
    hide screen nvlbox with dissolve
    pause 1
    show dmy3 with slowdissolve:
        zoom 1.0
        xalign 0.5
        yalign 0.5
    pause 2
    show screen nvlbox with dissolve
    "\n「聞きたくない、聞きたくない、聞きたくないんだよ！」" with sshake
    "マヤは子供のように叫び、俺を打ち負かす。止める間もなく襲ってきた一撃に、骨を折る幻覚が見えた。"
    "堪えきれず体を丸めて頭を包んだ。重い痛みが肩を伝って背中に広がっていく。"
    "マヤは明らかに怒っていたが、何故か怯えたように震えていた。"
    "今まで積み上げてきた悲しみ、否定したかった現実の残忍さが俺の拒否を基点に爆発したのだ。"
    et "俺はそうやって始まった暴力を全身で浴びながら涙を飲んだ。思わず噴き出そうとする呻き声を我慢するため唇をかむ。"
    nvl clear
    "\n かさかさと乾いた唇から血の味がした。{w}ふと、この状況が非常に不条理であり、うんざりすると思った。"
    "その苦痛がついに限界に達したのか、体の内側から変な解放感が溢れてきた。"
    "我慢してたはずだった涙が顎の下へと滴り落ちるが、そんなものを気にしている余裕もなかった。"
    et "俺はできる限り止めようとしたが、久々に外に吐き出された液体は一向に止まる気はなさそうで、足元に小さな水たまりをつくった。"
    hide screen nvlbox with dissolve
    nvl clear
    pause 1
    hide dmy3
    with slowdissolve
    pause 2
    show black with dissolve
    pause 1.0
    show screen nvlbox with dissolve
    "\n マヤはいつの間にか動きを止めたが、まだ興奮が消えていないのか上気した顔で息を切らしている。"
    "耳が塞がり、視界が揺れ、マヤの顔はぼやけて見えた。俺は震えながら口を開いた。"
    et "喉にかかった咳が声を塞ぐうえに、頭に加えられていた衝撃のせいか、うまく話すのが難しい。"
    nvl clear
    "\n 「ゴ、ゴメン…ごめんな、マヤ……」"
    "そしてバケツが大きな音を立てて床に落ちる。マヤは息を整えて俺を睨んでは、涙を拭かずに微笑んだ。"
    et "湧き出る白い蒸気と鼻を突く悪臭にも、マヤは嫌な顔一つせず誇らしげな顔をする。"
    nvl clear
    "\n 「また必要な物があったら言ってね…わたしに。」"
    "間違いなく俺の幸せと安全を願う微笑だった。その親切を拒否するのがどれほど恥知らずで無価値なことだったのか知る。"
    "俺はマヤと一緒にいる。マヤの助けなしには何もできない。「前」の常識は捨てるべきだ。生きていくためには。"
    et "俺は頷いて、忍び寄ってくる泣き声を飲み込んだ。"
    stop sound fadeout 3
    nvl clear
    hide screen nvlbox with dissolve
    pause 1
    show black with dissolve
    pause 1.0
    hide black with dissolve
    show screen textbox with dissolve
    nar "共同生活が始まって以来、マヤはあまりおめかしをしないようになった。"
    nar "ほどけかけているツインテールは不安定にぶら下がっていて、靴下はいつも片方だけ脱げている。"
    nar "また、服を逆に着てたり、チャックを閉めないままボーっとしてたり、"
    nar "一日中クローゼットを開け閉めしたり、たまには靴さえ履かないまま外に出て行ったりもする。"
    nar "寝ている俺を置いて「俺」と会話することもしばしばあった。{w}その会話にはたまに、俺だけでなく他人の名前も上がったりする。"
    nar "彼女は俺と共に暮らしているが、俺と一緒には暮らしていなかった。"
    nar "俺に見えない違う生活を満喫する彼女は楽しそうだった。"
    pl "マヤ、髪ずっとほどけたままだな。"
    show SCG_02 A 7 100 with dissolve
    my "どう結ぶのかわからないの…"
    pl "俺が結んでやれたらいいんだけどな…ゴメン。"
    show SCG_02 8 with fastdissolve
    my "髪ほどけてるの、おかしい？"
    pl "いや、マヤは何やってても可愛いから。"
    show SCG_02 4 with fastdissolve
    my "へへ…"
    show SCG_02 1 with fastdissolve
    my "最初髪を結んだ時、お姉ちゃんたちが似合うって言ってくれてたの…{w}それだけ。"
    my "他の理由や可能性なんて考えたことなかった。"
    show SCG_02 8 with fastdissolve
    my "みんな知ってたんだろうな。{w}年老いていくまでそうやってずっと周りから可愛い可哀想って指を指されるだけ…"
    pl "かわいいって言葉、あんまり好きじゃないのか？"
    my "嫌いじゃないよ、でも『一番』かわいくないならそれはただのマヌケじゃない。"
    pl "マヤはマヌケなんかじゃない。"
    my "知ってる…でも中途半端はいやなんだ。"
    my "甘くないなら辛いのがマシ。{w}どうせしあわせになれないなら世界で一番ふしあわせな人になりたいの。"
    pl "でも普通になりたがってたじゃないか。"
    show SCG_02 0 with fastdissolve
    my "普通じゃないとダメだったから。"
    pl "俺にはよく分からないな。{w}俺の目にはマヤが一番可愛いし、マヤと一緒が一番幸せだからさ。"
    show SCG_02 1 with fastdissolve
    my "うん…わたしはもう髪を可愛く結ってなくてもいいんだ。{w}[na2]くんと、ここでずっといっしょだから。"
    $ renpy.music.set_volume(1, channel="sound")
    hide SCG_02 with dissolve
    hide screen textbox with dissolve
    pause 2
    nvl clear
    stop music fadeout 2
    scene black with slowdissolve
    pause 2
    call dmy_menu from _call_dmy_menu_2
    return

label dmy4:
    $ preferences.afm_enable = False
    $ persistent.dmy = 4
    if persistent.dmy_off == False:
        $ _skipping = False
    else:
        $ _skipping = True
    show screen at_frame  with dissolve
    show screen quick_menu_dmy with dissolve
    scene bg10_3 with slowdissolve:
        xzoom -1.0
    call place10_2 from _call_place10_2_5
    show screen nvlbox with dissolve
    play music "audio/bgm/r18.ogg"
    nvl clear
    show screen nvlbox with dissolve
    "\n ベッドの上から目を覚ます。隣で同じ状態のマヤが寝ていた。"
    "こうやって寝ている彼女の顔を見ていると、何となく忘れていた昔のことを思い出す。"
    "広い神殿、初めて彼女に出逢った時の事…"
    "色褪せかけていた記憶は段々ただの良い思い出に留まらず不安へと色が変わっていく。{w}今は何日なんだろう？"
    et "外はどうなってる？{w}俺たち二人はここにどれだけ長い間居たんだろう？{w}いや、意外と一日や二日しか経ってないのかも知れない。"
    nvl clear
    "\n そうでなければ外がここまで静まりきっている筈なんてないのだから。"
    "この生活が始まって以来、マヤではない誰かが扉を叩いたりすぐ前の廊下を過ぎて行ったことは一度もなかった。"
    "ここは神殿なんだ。{w}司祭の二人が何日も引き篭もっているというのに、誰も訪れて来ないのはおかしいじゃないか。"
    et "今頃みんなどこで何をしているんだろうな、主教様は？{w}病棟は…"
    nvl clear
    "\n「うぅん…」"
    "「……」"
    "やっとの思いで身体を起こす。"
    "大分不便になってきたこの身体は少し動くだけでも苦痛を伴うようになった。{w}しかし慣れれば気にならない。"
    "ベッドの下には俺たち二人分の服、ベッドの上にはマヤのドロワーズがあった。"
    "マヤは数日前からずっと生理中だったらしく、ドロワーズは血塗れだ。"
    "服に泥が付いただけで泣きそうな顔をしていた姿が嘘みたいだ。{w}病気に掛からないといいけど…"
    et "下着を持ち上げた途端、全身が固まる。"
    nvl clear
    "\n まるで大きな穴でも空いたかのように真っ黒なゴキブリが引っ付いていた。{w}今まで見た事もない大きさだ。"
    "蟲が自身の存在を証明するかのように動き出したと同時に、俺も悲鳴を上げながら下着を離す。"
    et "その声で未だ眠そうなマヤが寝返りを打った。"
    nvl clear
    "\n「どうしたの…？」"
    "「ご…ゴメン、ちょっとビックリしちゃってさ…」"
    "やっとの思いで深呼吸をしてドキドキと高鳴る胸を抑える。"
    "マヤはまだ眠気が醒めていないのか半目のまま辺りを見回すと、手探りでベッドの上を這い回る蟲を探す。"
    "その手を結局蟲に被せてしまい、俺は吃驚して息を呑んでしまう。{w}マヤはくすぐったいのか小さく声を出して笑っていた。"
    "「うごいてる…」"
    "「…大丈夫か？」"
    "蟲を獲った手で優しく包みながら微笑む彼女の表情にゾクっとする。"
    et "手はわざと強く握っていないのか、隙間から黒いものがチラチラ見えてきた。"
    nvl clear
    "\n「また嫌な顔してる…虫さんがそんなに嫌い？」"
    "…正直、もう見ているだけでも舌に苦みを感じて吐き気がする。"
    "俺はどうにも答えられず、その視線から逃れたまま頷いた。"
    "「みんな猫を飼ってる人は猫のママさんって呼んでくれて、花を育てる人はお花のママさんって呼んでくれるのに…"
    "どうして虫さんを育てるマヤのことは誰も虫のママさんって呼んでくれないんだろうね…？」"
    et "へんなの。{w}マヤはそう呟いて握っていた手を離す。"
    nvl clear
    "\n 窮屈な手から逃れた蟲は細っこい腕を這って、繊細な肩へ、甘い首筋を過ぎ、その下の柔い太ももまで這い回る。"
    "俺はその感触を全て知っている。"
    "今まで穢れなど知りもしなかった彼女の真っ白な肌の上を、真っ黒の蟲が汚らしい脚を忙しなく動かしながら引っ付いたまま這いずり回る。"
    "その光景から目が離せないままの俺の手に彼女の小さい手が被さった。"
    "マヤの手だ。{w}とても軽くて小さい掌。ぎゅっと握ってしまえば壊れてしまいそうな細く白い指。"
    et "掌を少し握らせていたからか、ちょっとばかりの湿気と温もりが残っていた。"
    nvl clear
    "\n その温もりを逃さんとばかりに彼女の手を握る。そうしなければ俺の中のマヤの存在が薄れて行ってしまいそうだったから。"
    "「ああ…今ちょっとだけドキドキしちゃった。」"
    "マヤは俺の好きな人。"
    et "もし、もしもマヤが俺を離れてしまうなら、俺は…"
    nvl clear
    hide screen nvlbox with dissolve
    pause 2 
    nvl clear
    pause 1
    show dmy4 with slowdissolve:
        zoom 1.7
        xalign 0.56
        yalign 1.0
    pause 2
    show screen nvlbox with dissolve
    "\n 「…見て」"
    "マヤは鋭い髭剃りを高く持ち上げて手首を切った。顔の上にぬるい血が降り始めた雨のように落ちてきた。"
    "赤く染まったベッド、俺たちの体の上を蟲が這っている。{w}今は頭が朦朧としてその恐ろしい感触がまだちゃんと感じられはしない。"
    "それはどっちかというと本能的な防御行為でもあるようだった。"
    "あれほど臆病だった彼女が、自分の体に思いっきり傷をつける姿は俺を悲しませた。"
    et "もしかしたら彼女はずっと前から死を考えていたかもしれない。"
    nvl clear
    "\n 俺は彼女に生きてほしかったが、一方ではそこに一体何の意味があるのか考えた。{w}しかし、そのような考えは彼女の口づけでぼやけていく。"
    "口に含んだ血があっという間に舌を包み、滑らかに食道を越えていく。鼻をつく血のにおい。"
    et "俺たちが体を動かす度に背中の下で、肘の下で砕ける蟲共。{w}そこで正気に戻ってきたのは不運だった。"
    nvl clear
    "\n 俺は吐き気に耐えきれずに胃液を吐き出す。{w}酸っぱい吐瀉物が喉を痛めて鼻まで逆流したが、マヤは口を離さなかった。"
    "漏れようとする咳と吐き気のために体がけいれんした。{w}もう何度も感じてきた蟲の食感と違って、マヤの舌は温かく柔らかい。"
    et "長い爪を俺の背中に突き立てては、優しさで俺を窒息させていた。"
    nvl clear
    hide screen nvlbox with dissolve
    pause 2
    show dmy4 with slowdissolve:
        zoom 1.0
        xalign 0.5
        yalign 0.5
    pause 2
    show screen nvlbox with dissolve
    "\n 熱い涙が頬を伝って零れ落ちる。マヤの目元にも涙が浮かんでいる。"
    "しかしそれは俺のとは違って生理的なものだった。{w}それを証明するかのように彼女は口元についたさまざまな異物を拭き取りながら笑う。"
    et "その視線が俺に向けたものだったのか、それともまだ生きている蟲共に向けたものだったのか…彼女の暗い瞳からはわからない。"
    nvl clear
    "\n「わたしの死体がきみのお家になるよ……」"
    et "生気などない目で希望も何もない言葉を口にする彼女が、俺にはとても愛らしく感じられた。"
    nvl clear
    "\n 背中に触れている彼女の手。{w}その暖かい温もりは、冷たい州都の記憶を忘れさせ、まるで家に帰ってきたような感覚を思い出させた。"
    "俺は流れなかった吐瀉物がまた俺の中に流れてくるのを感じ、さらにマヤの懐に潜り込む。"
    "肺が空っぽになって死んでいくような苦痛の末に、明らかな恍惚感が脳裏で点滅する。"
    et "それはもう否定しようもなく気持ちの良いものだった。{w}頭が真っ白になるぐらいに。"
    $ renpy.music.set_volume(1, channel="sound")
    stop sound fadeout 3
    hide screen nvlbox with dissolve
    nvl clear
    hide screen nvlbox with dissolve
    pause 1
    hide dmy4
    with slowdissolve
    pause 2
    show black with dissolve
    pause 1.0
    hide black with dissolve
    stop music fadeout 3
    show screen textbox with dissolve
    nar "重い瞼が開く。"
    my "…神聖な祭りを祝う前に、わたしたちの犯した罪を認めましょう。"
    my "主よ、わたしをあわれみたまえ。死体の様な悪臭を放ち皆がわたしを避ける様、"
    my "両目をくり貫き前を見つめられぬ様、四肢が完全にわたしの物でなくなる様、"
    my "そして自身の意志では動く事さえままならぬ様にさせ、"
    my "手を腐らし誰かの手を握ることも出来ぬ様、"
    my "年老いた者の如く背筋を丸め誰もわたしの手に荷を掛けられぬ様にさせて下さいませ。"
    my "世の罪を除きたもう主よ、わたしをあわれみたまえ。"
    my "永遠と守られし魂を陵辱する事で、無暗に純潔を感じさせない様にさせて下さいませ。"
    my "誰一人とてわたしに頼れぬ様にさせて下さいませ。"
    my "罪無きわたしを短命の道へとお導き下さい。"
    my "神なる主の恩讐を願う迷える仔羊を御救い下さい、アーメン…"
    nar "マヤが寝ぼけたような声で祈りを捧げていた。"
    $ renpy.music.set_volume(1, channel="sound")
    hide SCG_02 with dissolve
    hide screen textbox with dissolve
    pause 2
    nvl clear
    stop music fadeout 2
    scene black with slowdissolve
    pause 2
    call dmy_menu from _call_dmy_menu_3
    return

label dmy5:
    $ preferences.afm_enable = False
    $ persistent.dmy = 5
    if persistent.dmy_off == False:
        $ _skipping = False
    else:
        $ _skipping = True
    show screen at_frame
    with dissolve
    show screen quick_menu_dmy with dissolve
    scene bg10_3 with slowdissolve:
        xzoom -1.0
    call place10_2 from _call_place10_2_6
    show screen nvlbox with dissolve
    play music "audio/bgm/r18.ogg"
    nvl clear
    show screen nvlbox with dissolve
    "\n 暗い部屋にたまたま光が入ると、すぐ開いた扉が静かに閉じる音がした。{w}その少しばかりの光が俺には眩しすぎる。"
    "真っ白な翼のような光を背にして入ってきた天使は、真っ暗な部屋で俺を抱き締めた。"
    "俺たち二人の世界は、そうして完全となる。"
    "「待っててくれてありがとう」"
    "「戻ってきてくれてありがとう」"
    "痛む腕を上げ彼女の小さい背に手を回そうとすると、彼女はもっと強く俺を抱き締めた。"
    "まるで俺の行動を阻止せんとするばかりに俺の肩に顔を埋めたまま首を縦に振るマヤは、"
    "やがて身を後ろへと逸らし俺と目を合わせてきた。"
    et "行き場を失いぶら下がったままの腕は冷たい床に触れている。"
    nvl clear
    "\n 「[na2]くん、わたしと一緒に暮らそう。"
    "もうお外なんていかなくてもいいの。"
    "分かりたくもなかった真実を脳みそにたたき込む必要だってない。"
    "腐りかけの腕なんてもういらないわ、嘘ばっかり行き来することばもいらない。」"
    "だって、これからはわたしがずうっと一緒にいるから。"
    "マヤはいつも以上に確信を持った声で言う。{w}そこには一切の嘘も、戸惑いも存在しない。"
    et "それは理想だ。{w}その理想が魅せる甘さに惚れるように頷くと、彼女は俺の首に腕を回しもう一度俺を抱き締めてくれた。"
    nvl clear
    "\n マヤは一旦、俺にコップが透けて見えるぐらい透明な液体を飲ませた。"
    "『鎮痛剤』という言葉と共に飲み込む生温い液体からは水道水特有の鉄臭さがあった。"
    "何枚も敷かれたタオルの上に横たわって見つめる天井はなぜか普段以上に広く、暗く見える。"
    "そのせいか上で俺を見つめるマヤがいつもより遠く感じた。"
    et "そのクラっとしそうな距離の視界に、濃い鈍色の光がギラギラと入り込む。"
    nvl clear
    "\n鉄の塊に刃と皮の取っ手をくっ付けただけの阿呆みたいな見た目の鈍器は、実際浄化部で人の身体を斬るため使われていた道具だ。"
    "マヤのか細い身体じゃ取っ手を両手でちゃんと握っても重さに耐えきれず左右にグラグラしてしまう。"
    et "その重さ故か刃が落とされるのも一瞬だった。"
    hide screen nvlbox with dissolve
    pause 2
    show dmy5 with slowdissolve
    pause 2
    show screen nvlbox with dissolve
    nvl clear
    "\n 恐ろしい速度で振り落とされた刃はベッドのシーツまで突き破り、さっきまで見つめていたマヤの顔や天井までもが一瞬で血まみれになった。"
    "「ぁ…ぐあぁっ！！」"
    "「ごめんね、[na2]くん…{w}次はちゃんとするから。」"
    "マヤは荒く息を呑む。その言葉で急いで顔を背けた。"
    "「ごめんね、[na2]くん…{w}[na2]くん、ごめん、ごめんなさ…」"
    "凶悪な鈍器の重さ故か、彼女の腕が細すぎる故か武器を持つ彼女がふらつき、"
    "刃こぼれして脆い刃先は振り下ろされるたび毎度新たに筋肉を斬って腕の中へと深く突き刺さる。"
    "「うぐ、ぅ…うぁああああ！」"
    et "「ああああぁあ！！」"
    nvl clear
    "\n 気を失う暇さえなかった。{w}マヤが変なところに鈍器を振り下ろすたび、俺の意志と関係なく首が反り、手足が動く。"
    "固く噛んだ奥歯が骨を砕く苦痛で開く度潰れた喉元へ唾液や鼻水なんかが流れ込んでいく。息を吸って吐くのすら困難だ。"
    "今までのやり方の程度が透けて見えるかのようなマヤのヘタクソなやり方のせいで、俺の腕はミンチになりかけていた。"
    "閉じる事さえできない目に黒くにじむグチャッとした液体が映る。"
    et "無造作に散らばる肉片、黄色いゼリーにも似た塊の凸凹の隙間に糸の様に真っ赤な血が引っ付いている。"
    nvl clear
    "\n 俺は死んだものたちからこんなものが出て来る光景は見た事がない。"
    "マヤは藻掻く俺を自身の太ももで抑えては、荒く息を吐きながら聞き取れない何かをぼやいている。"
    "血が飛んでかすむ視界のせいで彼女の顔も伺えない。"
    "これが本当に天使の恩寵なのか？{w}この苦痛が本当に迷える俺を引導する神聖なる儀式なんだろうか。"
    et "血の臭いがする。"
    nvl clear
    "\n 「[na2]くん…{w}[na2]くん、[na2]くん、[na2]くん、[na2]くん……{w}これで本当に最後だよ。」"
    "腕はまだ、俺にくっついている。"
    "動けるかどうかは分からなかったが、切々と感じられる過度な痛みに絶え間なく悲鳴が上がる。{w}醜き声が上がる。"
    "腫れ上がった指先が俺の頭に触れている。元々広げておいたはずの腕が、自身でも全く理解できない方向へと曲がっている。"
    "マヤは上気する顔でもう一度重い取っ手を手にした。"
    et "「しあわせになろ、一緒に…」"
    nvl clear
    hide screen nvlbox with dissolve
    pause 1
    $ _game_menu_screen = None
    menu:
        "受け入れる":

            $ _game_menu_screen = 'preferences'
            show dmy5:
                zoom 2
                xalign 0.9
                yalign 0.2
            show bgw
            stop music
        "拒絶する":
            jump day12
    play music "audio/se/no more bell my buddy.ogg" fadein 5
    pause 2
    hide bgw with dissolve
    pause 2
    show screen nvlbox with dissolve
    "\n 確か相当な苦痛が感じられた筈なのに、いざ変な方向へと噴出した大量の血を見ていると頭が真っ白になる。"
    "潰れた喉からはもう悲鳴すら出て来ない。"
    "皮膚を突き破って出た真っ白の骨。{w}それが先程までは俺の体の一部だったという事実が信じられないぐらいだ。"
    "呆れるほど痛みばかり感じていた腕にはもう感覚がない。"
    "俺は無意識に天使の存在を疑っていたのだ。"
    et "天使とは神が人間を赦す為与えて下さった存在、天使を信じないという事は神に背く行為。"
    nvl clear
    "\n 俺はもう彼女の存在を疑うことは無い。彼女こそが天使、俺の罪を赦し、俺の魂を受け止めてくれる地上唯一の天使だ。"
    "だから腐ったこれはもう俺の腕ではない。{w}天使に対する疑い、過去への未練、又は穢れた俺の魂そのもの。"
    "彼女の言う通りこんな腕はもう要らないんだ。{w}これを切り取る事で俺は自身の罪を懺悔することが出来る。"
    et "やっと安息出来るのだから。"
    nvl clear
    "\n 「わぁ、わああ！」部屋の中に充満した新鮮な血の匂いに、青白い顔が真っ赤に上気したマヤは歓喜の様な声を上げて血の飛び散った頬や開いた目に軽く口付ける。"
    "その部位を中心に身体がまるで炎に触れたかの様に熱くなる。{w}血の混じった汗が二人の触れ合った顎下へと雨の様に流れ落ちていく。"
    "心の臓は多く流した血を再び補うように淀みなく鼓動する。"
    "熱い心臓を動かす脳も劣らずに、今すぐでも融けてしまいそうに熱い。"
    "部屋を満たした熱気のせいで目がぼんやりしてきた。"
    et "しかし彼女に全てを捧げるには未だこの身体は重すぎる。"
    nvl clear
    "\n 「もういらない。」"
    "熱い俺たちにそぐわない冷たい声が一気にその場の空気を裂く。"
    "俺の中心へと向かう凶器は震えていた。"
    "それが回ってしまった目の錯覚なのか、彼女の手が震えていたからかは永遠分からなくなってしまった。"
    "霞む視界は段々と暗くなっていく。{w}もう二度と明るみを見る事は無いのかもしれない。"
    "しかし俺は一度抱いた光を忘れる事はなかった。"
    "一筋の光にさえ頼らず、ただ暗く狭い部屋の中で祈る天使の姿を思い出す。"
    "救いはそこにあったのだ。"
    et "俺は、彼女が望む理想にもう少し近付けたのだろうか。"
    hide screen nvlbox with dissolve
    pause 1.0
    menu:
        "「マヤが好きだ」":

            stop music fadeout 2.0
            hide dmy5
            call bgw from _call_bgw_16
            pause 1.0
            show screen textbox with dissolve
            nar "何度も夢見た彼女の限りなく明るい笑顔。"
            nar "俺はこれの為に生きて来たんだ。"
            nar "彼女の笑顔によって俺の世界は完璧となった。"
            show SCG_02 A 10 100 with dissolve
            $ _skipping = False
            my "わたしも[na2]くんすき！"
            $ persistent.dmy = 0
            $ persistent.lovelovemaya = True

            if not achievement.has("maya_love"):
                $ achievement.grant("maya_love")
                $ achievement.sync()

            hide screen textbox with dissolve
            pause 1
            play music "audio/bgm/maya.ogg"
            nvl clear
            hide screen keymap_screen
            $ _game_menu_screen = None
            hide screen quick_menu_dmy
            hide screen at_frame
            scene black
            with slowdissolve
            $ _dismiss_pause = False
            jump end
    show screen textbox with dissolve
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
