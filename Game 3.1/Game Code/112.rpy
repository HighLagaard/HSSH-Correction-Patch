label day12:
    $ save_name = "day 12, エンド"
    hide screen textbox
    show screen quick_menu_12
    hide screen quick_menu_dmy
    $ _skipping = True
    $ _game_menu_screen = 'preferences'
    show screen keymap_screen
    nvl clear
    hide screen nvlbox
    play sound "audio/se/hit.ogg"
    stop music
    scene black
    $ persistent.dmy = 0
    "\n 「あああぁぁあああ！！」" with sshake
    "裂けた包帯と共に吹きまくった激痛が脳を絞り、彼女の軽い体は床に放り出される。"
    "切羽詰まって体を起こした俺は引き手に滑った手を掛けてそのまま外へ飛び出した。"
    call bgw from _call_bgw_11
    nvl clear
    scene bg03_1 with dissolve
    call place03 from _call_place03_27
    show screen nvlbox
    with dissolve
    play music "audio/bgm/grumble.ogg" fadein 5
    "\n 今まで忘れていた外の風景は最後に見た時と同じく何の汚れもなかった。"
    "俺と彼女の臭いだけで満ちた、情欲と哀歓だけが限りなく燻る悍ましい場所。"
    "そこから逃れた俺は外の新鮮な空気を肺に一杯入れては、吐き出すことを繰り返しながら果てしなく走り出した。"
    "廊下を過ぎる。階段を飛び降りる。"
    "久しぶりに自ら動かした脚は何度も階段を踏み外して倒れる。{w}俺の体はもうとんでもないくらいに壊れている。"
    et "包帯と共に破れた肉片の隙間に汗が染み込み、それが耐えられないほど痛い。{w}ずっと痛かった。"
    nvl clear
    "\n 腐っていく血膿の臭いが自分の物だってことが怖かった。{w}逃げてきたものと再び向かい合うことが怖かった。{w}実はあの前からずっと。"
    "彼女を愛しているって錯覚したのは俺の傲慢だった。{w}ゴメン、マヤ。{w}ゴメン。"
    "自ら作り出した冷ややかな匕首が熱い心の臓を容赦なく刺してやがて爆発してしまいそうだ。"
    "もはや汗か血か分からなくなった何かが肌の上で混ざって体を伝うことが気持ち悪い。{w}しかし走ることを止めない。"
    "彼女から逃げ出した以上、俺はどこかへちゃんと至らなければいけない。"
    et "そこでこの苦痛を全て吐き出したい。{w}この罪を告解したい。{w}そして悔悟さえできれば…"
    nvl clear
    show bg04_1
    hide screen nvlbox
    play sound "audio/se/memory.ogg"
    call bgw from _call_bgw_12
    pause 0.1
    show bg06_1
    pause 0.1
    show bg102_1
    pause 0.1
    show bg104
    pause 0.1
    show bg106_1
    pause 0.1
    scene bg03_1
    call bgw from _call_bgw_13
    show screen nvlbox with dissolve
    "\n 作業場、"
    "医務室、"
    "訓練場、"
    "図書館、"
    et "階段……"
    nvl clear
    "\n 行ける全ての場所へ走った。しかし驚くほどに誰もいなかった。"
    "神殿の人々が全員俺だけをほって置いてどこかに消え去ったように、まるで最初から世界に俺一人しか存在していないようだ。"
    "俺は裂けそうに痛い心臓を押して荒い息を吐き出した。{w}よだれと涙、汗などが混ざって顔を伝う。"
    "もう立っているのもやっとの脚が震える。"
    et "本当に、そこに彼女たちはいただろうか？"
    nvl clear
    "\n 彼女たちと共にした在りし日が走馬灯のように過ぎていく。{w}まるで夢のような日々だった。"
    "それが本当にあったことなのか、俺を好きになってくれた彼女たちが本当に実在していたのか、"
    "静かな神殿ではそれを証明してくれる人さえもいなかった。"
    "近くで男の嗚咽が聞こえる。それは他でもなく俺の喉からの声だ。"
    "俺は最後に拡声して怒鳴ってみたが、声はすぐ力が抜けて木霊もなく散った。"
    "危うく体を支えた両膝から力が入らなくなった。俺は両手で熱い目頭を押さえながら暗い視界の中で泣き叫んだ。"
    et "苦痛により出てきた涙は傷に染みて更に俺を痛くする。"
    nvl clear
    "\n その痛みにすすり泣く内に、頭の上からまるで幻聴のような羽音がしてきた。"
    "可笑しい。{w}今まであんなにも軽く聞こえた音から前に無かった重さが感じられた。"
    "今すぐでも空へ飛んでしまいそうな崇高な音が、今は何かから逃げ出す為に必死に羽搏く音にしか聞こえない。"
    et "彼女と初めて出会ったのはいつだったっけ。{w}初めて天使の夢を見た日、それは圧倒的に美しかった。"
    nvl clear
    "\n 人として持つべき敬拝、然るべき恐怖、全ての感情があの燦爛とした存在にはあった。"
    "しかしあれは美しい天使の羽なんてものではなかった。寧ろ蜘蛛の糸にかかった蝶の羽に近いものだった。"
    et "そんな彼女を初めて見たのは、俺が最初に自分で作り出した幻想を信じ始めたのはいつだったっけ。"
    nvl clear
    hide screen nvlbox
    show story04:
        zoom 2
        xalign 0.8
        yalign 0.1
    play sound "audio/se/memory.ogg"
    call bgw from _call_bgw_14
    scene black with dissolve
    "\n あいつだ。"
    "全てはあいつに出会ってから始まった。"
    "壊れたままで輝きを失ったステンドグラス、埃が溜まって白っぽくなった窓。"
    "ほとんど壊れつつある壁を食らいそうに生い茂った雑草だらけの空間で、彼は俺にはっきり言っていた。"
    "滅亡、皆殺し…{w}まるでイかれた人の譫言みたいに出鱈目な話だが、もうそれ以外に俺に残っている手掛かりはなかった。"
    "俺は目の前に現れた疑いの綱を握った。"
    et "それは糸筋のように細いが、遥かに飛んでしまうところだった精神を現実まで引っ張るには十分だった。"
    nvl clear
    "\n 人、人が欲しい。{w}俺の話を聞いてくれて、俺を理解して、あの人を止める力を持った人。"
    "今度は遅れてはならない。{w}遅れてしまう前に誰かにこの事実を言わなければ。"
    "エルジェーベト主教？{w}ダメだ、あの人はもう俺への期待と好意を失ったはずだ。"
    "イヴリン主教？{w}あの人は信じ難いし、どこに行けば会えるのかも全く知らない。"
    "グレゴール主教とグレーテ先生、あの人たちも俺の話を信じてくれないだろう。{w}きっと俺を狂人だと思ってしまうはずだ…"
    "やはり{color=#ffe594}彼女{/color}に会うしかない。{w}間違ってしまうかもしれない、もう遅いかもしれない。"
    et "しかし俺は、俺の前の運命を信じるべきだ。"
    nvl clear
    scene bg101_1 with dissolve
    call place101 from _call_place101_1
    show screen nvlbox with dissolve
    "\n 浅はかな者は座して死に至り愚か者は無為の内に滅びる。"
    et "わたしに聞き従う人は確かな住まいを得、災難を恐れることなく平穏に暮らす。"
    nvl clear
    "\n 床の鉄が鳴る鈍く濁った音がする。この苔の生えた汚い建物が今はどんな場所よりも安楽に感じられる。俺はそれほどに切だった。"
    "血の染みた手で錆び付いた扉の入り口を探す。頭の中では悪態をつきながら苦しい息を吐き出す。"
    "扉を手探りする手先が何度もしおしおと滑ってしまう。{w}血と水分にふやけた指紋がしわくちゃだ。"
    "何回か掻かれる鉄の音がしたが、それさえも断たれてしまう。{w}取れた爪がぶら下がっていた。"
    play sound "audio/se/hit.ogg"
    "「クソッ、クソ、クソ、クソ！」" with sshake
    play sound "audio/se/hit.ogg"
    "「開け…開けって…頼むから！」" with sshake
    et "返答は来ない。錆び付いた鉄門の前で絶叫を吐く男が立っているだけだった。"
    nvl clear
    stop music fadeout 2.0
    hide screen nvlbox
    scene bgw
    with dissolve
    pause 1
    br2 "\n 光。{w}{nw}"
    br2 "光が暗い視界を満たした瞬間目を閉じた。{w}{nw}"
    br2 "神は穏やかな光で俺に微笑む。{w}その光は生きた者の為だった。{w}{nw}"
    br2 "俺はボロボロになった体がやっと息をつき続けていることを感じて、その光が受けられることに心から感謝していた。"
    hide screen nvlbox with dissolve
    pause 1
    show story20 with slowdissolve
    pause 2
    show screen textbox with dissolve
    play music "audio/bgm/ed.ogg" fadein 70
    hk "[na]兄弟？"
    nar "彼女は体を竦めたが、たちまち俺の所に近づいて、曇った空に指二本を厳かに上げて俺を祝福した。"
    pl "主教様？"
    nar "渇いた喉から嗄れた声が零れ出す。{w}胸が一杯になって、整え方を忘れた息は苦しく飲まれる度に食道を掻く。"
    nar "口を開く度に声の代わりに荒い咳が吐きそうに出てきた。"
    pl "本当の{color=#ffe594}主教様{/color}だよな？{w}本当の、本当にハク主教様だよな？"
    nar "何かが崩れたかのように涙が止まらない。"
    nar "しょっぱくて粘りのある液体が口の中を埋め尽くして、熱い喉を塞ぐせいで久々に動く舌が硬い。"
    nar "しかし今まで呑んできた言葉は相当多かったようで、口が言葉を紡ぐため耐え間無く動く。"
    nar "目の前の彼女が霞んでよく見えない。"
    nar "身体は俄然震えてばかりだが、それは苦痛や寒さのせいではない。{w}とても寒くて、とても痛い。"
    nar "でもこの空間で、俺はやっと「大人」に出会えた。"
    pl "俺…俺は…{w}主教様が…今…俺…"
    hk "……"
    pl "こわ…かった…！"
    pl "怖かった…！本当に、本当に、本当に辛くて怖かった。{w}神殿に誰も居ないし、誰も俺の事呼んでくれないし…！"
    pl "俺本当に頑張ったんだ。{w}ほ…ホントだよ、俺はほんとに、ほんとにほんとにほんとに頑張ったんだ。"
    pl "必死だったんだ…俺は怖かったんだ。"
    hk "……"
    pl "なのに、なのにアル姉さんは死んじまって、シーキュレットも消えてて、マヤはヘンだし、スゴく痛くてつらかった。"
    pl "死ぬほど痛かった…！"
    pl "俺は頑張ったのに…俺はこんなにこんなにこんなにも頑張ってるのに！"
    pl "俺ほんとにほんとにほんとに本当にこんなに頑張ったのに、なのにみんなおかしくなっちまって、"
    pl "俺は何も間違えてなんかない、俺にはこれが最善だったんだよ…！"
    hk "……"
    pl "神殿に誰も居ないし、みんなおかしい、全部おかしくなっちまったんだよ…{w}何もかも怖い。"
    pl "主教様までおかしくなっちまったんじゃないかって思ったんだ。"
    pl "主教様が{color=#cfe2f3}アイツ{/color}になっちまって、主教様が俺の事を憎んでて、俺…{w}そんなの俺は、すごく嫌で…"
    pl "マヤはおかしいし、アイツに殺されるかもしれないって思ったんだ、みんな死んじまうって思ったんだ…！"
    pl "それを止められるのは主教様しかいない、なのに…！"
    pl "主教様までヘンになっちまうんじゃないかって怖かったんだよぉ…！！"
    nar "感情が全く制御できない。{w}醜い、見苦しい。"
    nar "涙を拭く為に上げた傷だらけの腕が顔を血で汚し、溢れる涙がそれを洗い落とすという意味のない行動を繰り返す。"
    nar "嗚咽の混ざったまずい鳴き声が静かな礼拝堂に満ちる。{w}思い惑い只並んだだけの言葉が持つ意味なんてどうでも良くなった。"
    nar "そんな俺の愚痴を受けてくれる彼女の表情はあまりにも優しくー"
    hk "……"
    pl "………"
    pl "主教様？"
    hk "………"
    nar "彼女は俺の震える手を包むように握った。{w}そして穏やかな笑みを浮かべる。"
    hk "さぞ心苦しかったでしょう？"
    pl "……"
    hide screen textbox with dissolve
    pause 1
    hide story20 with slowdissolve
    pause 2
    scene bg100_1 with dissolve
    show SCG_05 0 with dissolve
    show screen textbox with dissolve
    nar "その温かな一言でやっと脚から力が抜けた。{w}それは俺が長い時の中で一番欲しかった一言に間違いない。"
    nar "今ここにいる人はあの人ではなく、彼女だ。{w}俺の知っている一番優しい人。{w}俺はやっとここに来たんだ。"
    pl "うん…{w}うん！すごくつらかった、とっても苦しかった。"
    pl "多分主教様にはわからないぐらい、いや！{w}主教様はわかってくれてるんだな。{w}主教様だけが俺を理解してくれるんだ。"
    pl "何もかも失った俺にとってそれがどれだけ力になるか計り知れない、{w}あぁ！やっと言えた。"
    pl "今まで何回も死境を乗り越えて来たんだ、俺にまだこの口が残っててよかった。"
    pl "俺にまだこの両手が残っててよかった。{w}俺は何もかもを失ったわけじゃないんだ。"
    pl "俺に慈悲を与えてくれてありがとう、俺の元にいてくれてありがとう。"
    show SCG_05 1 with fastdissolve
    hk "はあい、良くぞいらっしゃいました。"
    nar "座り込んだ地面は気のせいか柔らかく感じられる。{w}疲れた目は再び開く気はなく新たな涙を流した。"
    nar "今になって長い旅程の終わりが見えるようだった。"
    nar "そしてあの平穏が破れたことも一瞬だった。冷たい刃が俺の耳を直線に掻き裂いて横へ逸れた。"
    hide SCG_05 with dissolve
    hide screen textbox with dissolve
    nvl clear
    pause 1
    "{nw}" with sshake
    pause 1
    show screen textbox with dissolve
    nar "それは元々首に当てようとしたようだった。"
    nar "耳と繋がった頬から熱い血がどくどく溢れてきて、片方の視野に入った赤はくらっとするほどに鮮明だった。"
    nar "それはあまりにもいきなりのことで、俺は痛みに悲鳴をあげることさえも忘れてしまった。"
    show SCG_05 5 with dissolve
    hk "何故、避けてしまわれたのですか…？"
    nar "剣を構えた彼女は悲しそうに顔を歪めた。{w}それは偽物ではない。"
    nar "思わず心が動いてしまいそうな悲痛な表情は、心から俺を哀れんでいるようだった。"
    show SCG_05 8 with fastdissolve
    hk "兄弟の本音を信じましたが、未だその心は反省の覚悟が足りていない御様子…"
    hk "しかしそれは決して兄弟の罪ではございません…"
    pl "な、どういうことだ…？"
    nar "涙を浮かべた彼女が再び剣を持って俺に近づいた時、俺は後ろへ床を這いながら寝言のように微かな言葉で彼女に問う。"
    nar "そうすると彼女はとろんとなった目で俺ではなく空を見つめては明朗に声を鳴らした。"
    show SCG_05 1 with fastdissolve
    hk "嗚呼、贖罪の時来たり！"
    hk "人間が病魔へと陥れた大地を見守りし我が神よーどうかこの哀れな仔羊を禍から救いー"
    hk "その魂を以て罪を償い、贖罪出来ます様ーご慈悲を…ー"
    pl "なん…で…"
    nar "静まった心臓は恐怖に再び鼓動し出す。"
    nar "忙しく動く目が四方をさまよう時、俺は一生見ることはなかったであろう穴を覗いてしまった。"
    nar "座り込んだ所からもそれが見られたのはあの穴があまりにも巨大すぎて、又広く開いていたからだ。"
    nar "麻痺していた感覚が徐々に戻り、俺はやっとこの場所の所々で俺のではない血が腐っていることに気付いた。"
    nar "本能が怒鳴った。{w}もうすぐ俺もあの中に入るんだろうって。"
    show SCG_05 0 with fastdissolve
    hk "尊き我が神は穢れた魂を罰するためこの大地に禍を下さりました。{w}罪人はーその贖罪の時間を以てー神へ許しを乞うのです。"
    hk "そしてわたくしは神に献身する司祭としての道理で、罪人の魂を闇から連れ出しー"
    hk "その者が告解出来ます様、神の慈悲を願って安息を与えるのですー"
    nar "気を取られたままで座り込んだ俺に、彼女は口角を上げてにこりと微笑んでは大きく手を叩いた。"
    show SCG_05 1 with fastdissolve
    hk "告解、告解ー"
    nar "二度の音と共に赤い血を払う彼女の手はもう善行と典礼を繰り返してきた崇高な手ではなかった。"
    nar "初めてきた日のように薄暗い空は曇って、彼女の金色の目だけが見えない月の代わりをするようにこの暗闇の中で明るく昇っていた。"
    show SCG_05 0 with fastdissolve
    hk "神は空下の人間を取り除くが為禍を下さりました。しかし告解の機会とは誰にも平等なのでございます。"
    hk "なので兄弟、どうか自身の罪にあまり恐れなさらぬよう…ー"
    nar "俺はまだ恐れたままで震えていたが、驚くべしそれが段々気楽な何かに聞こえ始めた。"
    nar "襲ってくる死の恐怖は容赦なく俺の精神を齧って、不安な手足を崖に立たす。"
    nar "なのに告解を伝える彼女の声は穏やかで、静かに浮かんだ笑みは違わず心を和ませた。"
    nar "それはとても人に剣を振り回しそうには見えなかった。"
    pl "まだ、死にたくない…"
    nar "しかし俺は俯いて小さく声を零した。"
    nar "それは俺の中に残った最後の恐怖から絞られた悲鳴だった。"
    nar "優しい彼女が俺に近づく。{w}あの手は死を感じさせる冷たさがなく只温かい。"
    hk "死ぬのではございません。どうして殺害される、なんて思われたのですか？"
    pl "俺の魂が延々闇の中に突き落とされるのが怖い。"
    show SCG_05 1 with fastdissolve
    hk "そうさせないが為にわたくしがここにいます。{w}わたくしの祈りが、兄弟を遥か光へと導く事でしょう。"
    hide SCG_05 with dissolve
    hide screen textbox with dissolve
    scene black with dissolve
    br "感謝することを忘れてしまった人により地上から慈悲は引き取られ、今空下に蔓延るは禍のみです。{w}{nw}"
    br "しかし我らが父なる神は尚最後の機会を与えてくださいました。{w}{nw}"
    br "集った神聖なる魂は我々の立つ足元の養分となり、再びこの地を生き返らせることでしょう。{w}{nw}"
    br "その様な素晴らしい偉業を成し遂げた者たちに光は導かれるものです。{w}{nw}"
    br "わたくしが兄弟の穢れた魂の受け皿となりましょうーこれにてきみの魂は正しく、穢れ無くなりました。"
    hide screen nvlbox with dissolve
    scene bg100_1 with dissolve
    pause 2
    show screen textbox with dissolve
    nar "彼女の視線が至るところ。{w}そこには穴があった。"
    nar "俺が踏み込んだ冥土の中心、空に繋がった通路。"
    nar "そこが楽園だ、いつか誰もが辿り着く場所。"
    nar "斑になった世界で父の慈悲、俺の安息を願う彼女の祈り声だけがまだ神々しく残っていた。"
    hide screen textbox with dissolve
    pause 1.0
    menu:
        "告解":
            hide screen textbox with dissolve
            pause 2
            stop music fadeout 3
            scene bg12 with dissolve
            pause 1.0
            scene black with dissolve
            pause 3

    scene bg000
    call bgw from _call_bgw_15
    pause 3.0
    show screen nvlbox with dissolve
    play music "audio/bgm/maya.ogg" fadein 2
    nvl clear
    "\n あの日の朝、俺は朦朧な気持ちで夢から覚めた。"
    "そしてしばらくの間浮き立った心で、積み上げた荷物を運ぶことも忘れたままで見慣れた布団に座り、"
    "覚えてもない夢の余韻に浸っていた。"
    "しかしすぐ雄々しく起きた。{w}ついにこの里を出るんだ。"
    "やっとそんなことを気にするところではなかった。"
    "荷を運ぶ車の後ろに乗り、俺は金色に色付いた稲穂の畑を眺めた。"
    "今は夏だ。{w}降り注ぐ日光が、里が忙しき盛りの時期。"
    "期待と興奮塗れの心に少しの寂しさが入って、最後に目にした故郷の風景はそう遥かになっていく。"
    $ _skipping = False
    et "太陽の眩しい日だ。"
    hide screen nvlbox with dissolve
    pause 2
    nvl clear
    hide screen keymap_screen
    $ _game_menu_screen = None
    $ show_quick_menu = False
    hide screen at_frame
    scene black
    with slowdissolve
    pause 2
    $ _dismiss_pause = False
    jump end

label end12:
    if persistent.lovelovemaya == True:
        hide screen creditskip
        $ persistent.lovelovemaya = False
        $ persistent.dmy = 0
        $ persistent.mylove_end = True

        pause 0.5
        $ renpy.reload_script()
        $ renpy.run(MainMenu(confirm=False))
        return
    else:
        hide screen creditskip
        "\n クリア報償としてギャラリーがアンロックされました。"
        $ persistent.hssh_end = True
        $ persistent.hssh12end = True

        if not achievement.has("hss_ending"):
            $ achievement.grant("hss_ending")
            $ achievement.sync()

        pause 0.5
        $ renpy.full_restart()
        return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
