label day7_my:
    hide SCG_02 with dissolve
    my "きゃっ！" with sshake
    nar "手が勝手に彼女の髪を掴んでいた。マヤ金切り声を上げながらガクガクと手足を震わせている。"
    nar "煮え立った血が頬へ、頭へと昇って全身を熱くさせた。"
    play music "audio/se/Heart.ogg" fadein 5
    nar "暗い場所へと引き摺りながら、もう引き返せないんだろうなと思った。そうする意思もない。自分でもわかってる。"
    nar "天使が羽ばたく音は途絶えた。彼女がどんな目的をもって、何をしようと、今じゃその全ては意味を成さない。"
    nar "大きい翼、クラクラするほどの光、血肉の臭いなど、人間とかけ離れて見えていた幻想はすべて消える。"
    nar "ここに残ったのは神と内通した者の高潔な魂、手垢の付いていない純潔の身体だけ。"
    nar "俺だけがマヤ・エルベットの存在を知っている。俺は彼女の純潔を永遠に保つ方法を知っている。"
    nar "人は皆崇拝と敬愛の気持ちを込め、彼女を「聖処女」と呼ぶべきだ。"
    stop sound fadeout 2
    $ _skipping = False
    nar "その聖なる力こそが俺を楽園へ誘う。"
    hide screen textbox with dissolve
    $ save_name = "day 7, 夜, 楽園"
    hide screen textbox
    hide screen nvlbox 
    with dissolve
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
    jump day8_my_rkn
    return

label day8_my_rkn:
    $ day = 8
    $ save_name = "day 8, 楽園"
    $ renpy.music.set_volume(0.4, channel="sound")
    play sound 'audio/se/bell 5.ogg' fadein 2.0
    image 8day = Text("day 8",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '8day' at day00 with slowdissolve
    pause 5
    hide expression '8day' with slowdissolve
    stop sound fadeout 1.0
    pause 3.0
    show screen at_frame with dissolve
    pause 1
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    $ _game_menu_screen = 'preferences'
    $ renpy.music.set_volume(1, channel="sound")
    scene bg10_3 with dissolve:
        xzoom -1
    call place10
    pause 1.0
    show screen nvlbox with dissolve
    play music "audio/bgm/r18.ogg" fadein 5
    nvl clear
    "\n マヤの部屋は俺の部屋と構造が大分似ていて親しみがあった。{w}ただ、小さいベッドの上には脱ぎ捨てた服や靴下、"
    "ぐちゃぐちゃになった布団が無造作に置かれていて、椅子には濡れたタオルが幾つか掛けてあった。"
    et "マヤは整理整頓が下手でなんでも置きっぱなしにする癖があるから、そこまで驚く程の事でもない。"
    nvl clear
    "\n 外はまだ明るく、カーテンを閉じても完全に暗くはならない。これではマヤが気持ちよく眠れないのに。"
    "神殿での一日は既に始まっているが、マヤはまだぐっすり眠っている。"
    "昨日俺は、マヤに部屋の外に出ないように様念を押して「お願い」した。{w}怯えた彼女は頷くだけで、返事は返さなかった。"
    "合間合間に体をビクつかせながらごめんなさい、と寝言で謝るマヤがとても哀れに見えた。"
    stop sound fadeout 1.0
    et "これからは俺がマヤを守ってあげなきゃ。"
    hide screen nvlbox with dissolve
    scene bg14 with dissolve
    call place14
    pause 1.0
    show screen textbox with dissolve
    nar "部室の扉を開いて奥へ足を踏み入れると、並んだ気持ち悪い顔共が目に入る。"
    nar "主教のゆったりとしたあいさつ、窓を叩く風の音、あちこちから聞こえるあくびの音…"
    nar "日常を作っていた全ての音が一晩で不快な騒音へと変わっていた。"
    nar "ここは穢れている。早く、光のある場所に戻りたい。"
    stop music fadeout 2
    hide screen textbox with dissolve
    scene bg04 with dissolve
    call place04
    pause 1.0
    show screen textbox with dissolve
    play music "audio/se/fire.ogg" fadein 2 
    nar "神殿に着いてすぐ作業場へと向かった。{w}街に人がいないしもう昼飯の時間だろう。"
    nar "ここまではいつもと変わらないが、作業場には未だに灰色の煙がまるで黒雲のように立ち上っている。"
    nar "火が消える時の煙ではなく、勢いよく燃え上がる煙だ。それも驚くことではない。"
    nar "俺は袖で鼻を覆ったマヤの前に立って、染みる目を顰めて、煙の中に入った。"
    nar "そうすると向こう側から咳が聞こえてくる、続いていらいらしたため息も聞こえた。それで十分、ここにきてから何度も聞いた声だ。"
    show SCG_03 100 with dissolve
    pl "…お前がなんでここにいるんだ？"
    ex1 "なんでいるんだ、って。作業場には作業をしにくるだろ。"
    nar "立ち上がっていた煙が徐々に消える。奴は顰めっ面もせずに袋を開きながら、丁度今思い出したように付け足した。"
    ex1 "こっちこそ、キミは今日来ないと思ってたんだけど。"
    pl "俺も一応ここの司祭なんだし、来ないワケにもいかないだろ。"
    ex1 "へぇ…思ったより大丈夫そうで良かったよ。{w}マヤは？"
    pl "そう、それなんだけど…俺も朝聞いたばっかりなんだけどさ、マヤは今日体調が悪いらしいんだ。"
    pl "一日だけ休みを取りたいって言ってたから、お前が代わりに主教様に伝えてくれ。"
    ex1 "あの子が？{w}それは……心配だね。道理で朝から見当たらないと思ったら…"
    pl "あ、仕事なら心配しなくていいぜ。俺が代わりにやっておいたから。"
    ex1 "一人でやったのかい？"
    pl "どうせ簡単な雑用だろ？舐めんなよ～俺だってもうここの仕事には慣れてきたんだぞ、コラ。"
    ex1 "…キミがそう言うなら、まあ。とりあえず主教様には伝えておくよ。"
    pl "ハハ、頼むぜ。"
    hide SCG_03 with dissolve
    hide screen textbox with dissolve
    show screen textbox with dissolve
    nar "人の死体は、もう見る事の叶わない眼を開けたまま死体袋へ入っていく。"
    nar "そして動物の死体は生きていた頃の姿を忘れて死体袋へ入っていく。"
    nar "生きる全ての者たちは死を受け入れ地へと還る。そしてそれは誰にも抗えない。"
    stop music fadeout 3
    nar "生きとし生ける者のみが帰る場所を選べる。"
    hide screen textbox with dissolve
    scene bg14 with dissolve
    call place14
    pause 1.0
    show SCG_05 101 with dissolve
    show screen textbox with dissolve
    play music "audio/se/tutorial walking.ogg" fadein 2
    ex2 "わぉ…[na]兄弟ではありませんか。"
    pl "…主教様？部室に居るとは意外だな。"
    ex2 "そんなに不思議がられましても、主教が自分の部室に居るだけの事ですので。普段もよく出入りしておりますよぉ。"
    pl "この時間はいつも作業場にいるもんだと思ってた。今日はいかなくてもいいのか？"
    ex2 "まっさかぁ、もう行って参りましたよ。兄弟の足が遅いだけでして…"
    pl "へぇ…"
    nar "さっきまで思いっきり嫌悪感に身悶えていたせいか、今日の彼女の笑顔は更に忌まわしく見える。"
    nar "忌まわしいどころか憎悪すら感じる。何故よりによって俺の気分が悪い時に現れて、更にどん底まで落とそうとするのか。"
    nar "この後彼女が大人として、責任者として俺に何を言い出すか、余りにも丸わかりで思わずため息が出てしまう。"
    ex2 "魔導部の件は誠に遺憾に思います。"
    pl "そうだな。"
    ex2 "でも来月にもまたチャンスは訪れますのでぇ、あまり落胆なさらぬ様…"
    pl "ま、そうだよな。仕方ないよ。"
    ex2 "わぁお！お優しい～たいへんよくできましたぁ。{w}これからもまた一か月、互いに愛し合いましょうねぇ。"
    pl "もっちろんさ！"
    hide SCG_05 with dissolve
    stop music fadeout 3
    nar "風の涼しい夏、落ちる事のない陽の呪いが州都を包んでいる。俺は道なりに神殿へと戻っていった。"
    nar "一度胸に抱いた光を思い出しては、冷たい場所で血を流して死んでいく女を想像する。気が楽になった。"
    hide screen textbox with dissolve
    scene bg10_3 with dissolve:
        xzoom -1
    call place10
    pause 1.0
    show screen textbox with dissolve
    pl "マヤ、俺にはもう無理だ…辛いよ、マヤ…"
    play music "audio/bgm/r18.ogg"
    nar "戻った部屋にはマヤが居る。俺は彼女の平べったい胸に抱かれ、小さい身体を抱いたまま泣いた。"
    nar "古い布の匂いがする服をくしゃくしゃに握りしめ、蹲って彼女の膝を濡らす。"
    show SCG_02 7 with dissolve
    my "[na2]くん…"
    pl "これ以上何をどうすればいいのかわかんねえ、こんな仕事辞めちゃいてえんだ。"
    pl "頑張って生きたくない…将来の事なんて考えたくない…{w}マヤが大好きだから、だから、ただマヤとずっと一緒にいたい…"
    show SCG_02 8 with fastdissolve
    my "[na2]くん…"
    pl "ゴメンな、マヤ…お前のことが好きすぎてゴメン、でもどうしようもないや…"
    hide SCG_02 with dissolve
    nar "頭上でマヤの不安げな息遣いが聴こえてくる。俺の懐でマヤの心臓が跳ねているのが分かる。"
    stop music fadeout 2
    $ _skipping = False
    nar "他は何もいらない。{w}この暖かさをずっと感じていられるなら、マヤさえいてくれるなら、俺はこの先もずっと生きて行ける…"
    $ save_name = "day 8, 夜, 楽園"
    hide screen textbox
    hide screen nvlbox 
    with dissolve
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
    jump day9_my
    return


label day9_my:
    $ day = 9
    $ save_name = "day 9, 楽園"
    $ renpy.music.set_volume(0.4, channel="sound")
    play sound 'audio/se/bell 5.ogg' fadein 2.0
    image 9day = Text("day 9",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '9day' at day00 with slowdissolve
    pause 5
    hide expression '9day' with slowdissolve
    stop sound fadeout 1.0
    pause 3.0
    show screen at_frame  with dissolve
    pause 4.0
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    $ _game_menu_screen = 'preferences'
    $ renpy.music.set_volume(1, channel="music")
    hide screen textbox with dissolve
    scene bg10_3 with dissolve:
        xzoom -1
    call place10
    pause 1.0
    show SCG_02 8 with dissolve
    play music "audio/se/no more bell my buddy.ogg" fadein 5
    show screen textbox with dissolve
    pl "おはよう、マヤ。今日は早起きできたんだな。"
    my "……"
    pl "どうしたんだ…？"
    show SCG_02 7 with fastdissolve
    my "……その…"
    pl "なにか、頼みたいことでもあるのか？"
    show SCG_02 at huruhuru
    my "わたし、その…そろそろ仕事に戻りたい…"
    my "ずっと何日も部屋に居てばかりだったでしょ。このままじゃ主教様に怒られちゃう。{w}それにキューくんも…"
    pl "嘘だ。マヤは仕事がとっても嫌でずっと俺に任せっぱなしだっただろ。"
    pl "マヤはここで一週間も働いたと思ってるだろうけど、実際働いた日はたったの四日ぐらいなんだぞ。"
    pl "面倒事は全部俺が引き受けるから、そんなのは気にしないでお前のやりたいことやってていいんだぜ～"
    pl "あの二人にももう俺が言っておいたんだし。"
    show SCG_02 5 with fastdissolve
    my "…………"
    hide SCG_02 with dissolve
    nar "マヤの世話をするのは大変だ。心配で仕事にも集中できないし、一時も目は離せないし、常に機嫌を伺わないといけない。"
    nar "高貴な身体で生きて来た可憐な少女なのだから、手が掛かるのは仕方ない。"
    nar "しかしマヤは世間知らずで純粋なので、すぐ花壇に行きたいと駄々を捏ねる。"
    nar "マヤをあんな汚い土埃の飛ぶ場所になんて行かせられない。"
    stop music fadeout 3
    nar "俺の不注意でカワイイカワイイマヤが死んでしまっては大変だ。"
    hide screen textbox with dissolve
    scene bg14 with dissolve
    call place14
    pause 1.0
    show screen textbox with dissolve
    nar "静かなはずの浄化部の部室はまだ何人かの声で満たされていた。彼らは俺が入ってきたのを見るや話を止めて俺を見つめる。"
    nar "俺は辺りも見ずに大股で歩き出した。{w}いきなり笑い声が聞こえた気がする。書類にはいつも通り簡単な業務の指令が数行書いてある。"
    nar "そして埃臭いロッカーに手を入れ重い道具を引き出した。シャベルに付いた泥が固くなってくっ付いていた。"
    nar "拭き取っておくのを忘れてたな。"
    ex1 "おい、オンボロ処理班にチンカスくせぇ魔導部特採様がお通りだぜ。"
    ex2 "やっべ、オレ息出来ねぇや～ゲホゲホ！"
    ex3 "おいおいお前ら、悪ふざけもいい加減にしろよな？{w}特採様の気に障ったら一晩でお前らの女もちんぽ漬けにされちまうぜ～？"
    nar "彼らは仲間内で肩や背を叩きながら笑う。苛立ちからではなく、寒気で体が震える。"
    nar "日はまだ出ているが、初めて来た時に似た寒気がする。"
    nar "手に取った荷物を袋に入れようとしたが、震えのせいかゴムの手袋片方を落としてしまった。"
    nar "それを拾う為に屈んで手を伸ばそうとしたが、その前に誰かの足が手袋を踏んだ。"
    nar "曖昧に伸びた指先に男のズボンの裾が一瞬触れた。"
    ex1 "おい、自分の手を汚さず人を殺すってどんな気持ちなんだ？ん？"
    stop music fadeout 0.5
    nar "頭に血が昇る。そして次の出来事は一瞬だった。"
    hide screen textbox with dissolve
    nvl clear
    play sound "audio/se/humanstrike.ogg" 
    "{nw}" with sshake
    pause 2
    show screen nvlbox with dissolve
    play music "audio/se/no more bell my buddy.ogg" fadein 5
    nvl clear
    "\n 何度か視界が点滅する。俺はシャベルを持ち上げていた。{w}その後は、椅子を持っていた気がする。"
    "元々空を飛ぶものではないはずの椅子と机が何度も目の前を飛び交い、ガラスの割れる音が響く。{w}そして気が付くと俺は血塗れの男性の胸ぐらを掴んでいた。"
    "投げ飛ばされた男性は腫れあがった唇を開き悪態を吐く。背は俺とほぼ同じで、俺の力が特に強くなったわけではない。{w}彼らは最初から俺より弱かったのだ。"
    "宙を舞う涎の泡を見ていると、突然目の前が暗くなった。後頭部に大きな衝撃を受ける。"
    et "焼けるように広がる痛みに目を閉じた。{w}真っ暗な視界の中で、物が落ちる音が騒がしい。"
    nvl clear
    "\n 「チンカス野郎が、お前がこんな事したって何も変わんねえんだよ！"
    "みんなお前の事キモいって思ってんだぜ、知ってっか？！クソッタレがよぉ！！」"
    "その声は激しく昂っていた。その憎悪と憤怒を一気に受ければ不思議と頭が冷えてきて落ち着いた気がする。{w}俺も同じ感情を持っていたはずなのに。"
    "冷たい風に触れた肌は冷えていったが、一筋の赤い血が垂れる額は熱い。"
    "「ハハ……ッ」"
    et "その笑い声は俺の喉から出てきた。"
    nvl clear
    "\n 突然窓から雨と風が勢いよく吹き付け寒さが極まったが、それはどうでも良い。"
    "喉と肌が燃えるように熱くなり、真っ赤になった視界では埃が生き物かのように揺れた。"
    "形の崩れた机が俺の頭の上まで飛んできて彼らに陰を落としたが、大きな音とともに壊れた。"
    et "窓の外で激しく揺れる窶れ果てた木の枝はまるで死体の黒く細い手に見えて、俺に手招きしているかのように思えた。"
    nvl clear
    "\n 長い悪夢を見ていたようだ。しかし今痛みを感じ、冷たい肌の下では血液が熱く脈打っている。"
    et "ここはもう夢ではない。俺は俺を苦しめる長い悪夢から覚めたんだ。{w}その悪夢から脱したこここそが楽園だ。"
    stop music fadeout 2.0
    hide screen nvlbox with dissolve
    scene bg102 with dissolve
    call place102
    pause 1.0
    show screen textbox with dissolve
    pl "アルネ姉さん、何だか久々だな…"
    play music "audio/se/tutorial walking.ogg" fadein 2 
    show SCG_07 100 with dissolve
    ex6 "久々、と言うには4日前にも御会いしていたでは御座いませんか。"
    pl "そうだっけか…4日前には何があったっけ。"
    ex6 "兄弟が事故に遭ってしまい、腕を怪我なされたとお聞きしてお見舞いに伺いましたね。"
    pl "あぁ…そうだ、思い出したぜ。"
    ex6 "…部署異動の件につきましては、大変気の毒でしたね。"
    pl "ただのミスだったんだって、姉さん…{w}こんなことになっちまってゴメンな。俺のせいで困ったりしてないか？"
    ex6 "兄弟とはこれからも長い時間を共にするのです。"
    ex6 "一か月程度の差など、どうってことありません。私たちの心配はなさらずとも大丈夫です。"
    hide SCG_07 with dissolve
    stop music fadeout 2
    pl "へぇ……ハハハ……"
    hide screen textbox with dissolve
    scene bg03 with dissolve
    call place03
    pause 1.0
    show screen textbox with dissolve
    nar "そろそろ点呼が終わる時間か？{w}俺は司祭たちが部室から出て外へ向かうことを確認し隅に入る。"
    nar "すると、足音が少しずつ重なるように聴こえ、遠くの方から人影が見えてきた。"
    nar "小さな女性のようだ。その容貌があまりに華麗で、誰なのかはすぐ見当がつく。"
    play sound "audio/se/running.ogg"
    nar "花やリボンで飾られた空色の脳天はまるで俺の姿を確かめるように見て、頭を上げてすぐ前まで走ってきた。"
    show SCG_04 100 with dissolve
    show SCG_04 at bounce
    ex12 "[na]さま～ぁ～！"
    pl "うわっ、そんなデカい声出さなくても聞こえてるって！"
    ex12 "へへ、お返事を聞くまでは安心できませんもの。お昼の食事は済まされましたの？"
    pl "お前は…"
    play music "audio/se/tutorial walking.ogg" fadein 2.0
    ex12 "んもー！全く！たったの数日会ってないからって忘れてしまいましたの？"
    ex12 "神殿に貢献するミオソティス家の一人娘、クリオネ・ミオソティスとはわたくしの事ですわ。"
    pl "知ってる。マヤと一緒だったろ。{w}久しぶりだな、クレア。"
    ex12 "ま…まあ、そうですわね。覚えて下さり光栄ですわ。{w}その間いかがお過ごしでしたか？"
    pl "俺はぼちぼち。{w}それで、俺に何か用か？"
    ex12 "実はお聞きしたい事がございまして。{w}マヤお姉さまにお会いしませんでしたか？"
    pl "マヤ…？俺も今日は見かけてないけど、マヤに何かあったのか？"
    ex12 "それは解り得ないのですが、最近めっぽう連絡が届かなくて…この前まではほぼ毎日電話していたのですが。"
    pl "電話って…{w}ああ、寮のすぐ前にある電話機か。あれ使う人いたんだ。"
    ex12 "電話は楽しいですわよ、離れていても会話が出来るなんて～[na]様も今度わたくしといかがです？"
    pl "顔も合わせず人と喋るって何が楽しいんだ？そんなこと言わずに、もっと頻繁に遊びに来ればいいじゃないかよ～"
    ex12 "うー！わたくしにもわたくしなりの事情やプライベートというものがございますのですよ！"
    ex12 "知らないならもういいです！失礼します！"
    pl "気を付けてな、あと何かわかったら俺にも教えてくれよ。"
    hide SCG_04 with dissolve
    stop music fadeout 3
    nar "上品な挨拶の後、せわしない足取りで去っていく彼女の小さい身体が、角を曲がって視界から消える。"
    scene bg05 with dissolve
    nar "花壇に生まれたばかりだった芽は結局蟲に自らの身体を差し出し、花を咲かせる事なく死んでしまった。"
    $ _skipping = False
    nar "マヤに、何かあったんだろうか？大した事じゃないといいな…{w}心配だ。"
    $ save_name = "day 9, 夜, 楽園"
    hide screen textbox
    hide screen nvlbox 
    with dissolve
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
    jump day10_my
    return

label day10_my:
    $ day = 10
    $ save_name = "day 10, 楽園"
    $ renpy.music.set_volume(0.4, channel="sound")
    play sound 'audio/se/bell 5.ogg' fadein 2.0
    image 10day = Text("day 10",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '10day' at day00 with slowdissolve
    pause 5
    hide expression '10day' with slowdissolve
    stop sound fadeout 1.0
    pause 3.0
    show screen at_frame with dissolve
    scene black with slowdissolve
    pause 1
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    $ _game_menu_screen = 'preferences'
    $ renpy.music.set_volume(1, channel="sound")
    hide screen textbox with dissolve
    scene bg10_3 with dissolve:
        xzoom -1
    call place10
    pause 1.0
    show SCG_02 8 with dissolve
    play music "audio/SE/no more bell my buddy.ogg" fadein 5.0
    show screen nvlbox with dissolve
    "\n マヤは俺との永遠を誓って以来ずっと俺の隣に居てくれる。"
    "嗚呼、とても可愛くて優しくてか弱くて愛らしいマヤ。俺にはお前だけだし、お前には俺しかいない。"
    "マヤは処理班の業務で酷くストレスを受けていて、たまに服を着たままお漏らしをするようになった。"
    "夏が近づいたせいか髪の毛が抜ける量も大分増えた。故郷で飼っていた猫も夏になると良く毛が抜けていたものだ…"
    et "俺はそんなマヤを心配して、彼女がこれ以上仕事に出なくてもいい様にした。"
    nvl clear
    "\nマヤはずっと俺の部屋で過ごしてくれる。信頼されているみたいで嬉しい。"
    "その気持ちへのお返しと言うと少し恥ずかしいのだが、気弱なマヤの為に毎日扉に鍵を掛けてあげているんだ。{w}マヤも喜んでくれるだろう。"
    "マヤは段々とご飯を食べなくなってきている。多分神殿の硬いパンは神聖な彼女が口にすることは難しいのだろう。"
    "ある日思い切って彼女の大好きなゴキブリを捕まえて弁当を作ったのだが、差し出した途端真っ青になって断られた。何か問題があったのだろうか。"
    et "きっと処理班の汚い空気が箱入り娘として育ってきた彼女には毒だったんだろう。"
    nvl clear
    "\n ここの空気は毒性があって、神殿に居る全ての司祭を殺そうとしているんだ。"
    stop music fadeout 3
    et "俺だけがその事実を知っている。{w}俺だけが、俺だけがマヤを…"
    hide screen nvlbox with dissolve
    show SCG_02 8 with dissolve
    show screen textbox with dissolve
    pl "おはよう、マヤ。今日は早起きできたんだな。"
    my "………"
    pl "どうしたんだ…？"
    show SCG_02 7 with fastdissolve
    my "……その…"
    pl "なにか、頼みたいことでもあるのか？"
    show SCG_02 at huruhuru
    my "わたし、その…トイレ、いきたい…"
    pl "ションベンなら俺が毎日片づけてやってるだろ？"
    show SCG_02 at huruhuru
    my "そ…そうじゃなくて、その…その…"
    pl "……？"
    hide SCG_02 with dissolve
    nar "マヤはもじもじと次の言葉を言い出すのに躊躇っている。{w}何かおかしい。"
    play music "audio/SE/no more bell my buddy.ogg" fadein 5.0
    nar "俺は津波のように押し寄せる不安に耐え切れず、彼女を押し倒し、両手で押さえていたスカートを捲った。"
    nar "白いフリルの下の白いドロワーズ、それと白いシーツ……その純白で一杯の視界に乱暴な紅が入り込む。"
    nar "マヤは血を流している。{w}股から漂う汗の臭い、陰部特有の臭い、そして血生臭い臭いが混ざり合う。"
    hide screen textbox with dissolve
    scene black with dissolve
    show screen nvlbox with dissolve
    nvl clear
    "\n 長らく起こる事のなかった気持ち悪い頭痛が再び訪れる。{w}これは一体？俺はどうにかしてこの状況を理解せねばならなかった。"
    "悪魔。{w}彼女は邪悪で絶対的存在と姦通したのだ。処女を失った証拠として血を流しているのだ。"
    "そんな！一生懸命護ってきた、俺の聖処女が…"
    nvl clear
    play sound "audio/SE/Heart.ogg"
    "\n さっきからマヤは何か言葉を発している様だったが、その声はよく聞こえない。"
    "たまに[na2]くん、と俺の名前を呼ぶ声だけが耳についた。"
    "俺の身体は音を殺していく。肋骨の下で静かに心臓が鳴り、手の震えも段々と引いていく。"
    "その静かな場所で湿った、荒っぽい息遣いが鮮明に聞こえてきた。"
    et "それが俺ら二人の内どちらの物なのかは分からない。確かなのは、どちらも怯えていたという事だった。"
    nvl clear
    "\n 再び、マヤの許しを乞う声が聞こえてくる。"
    stop music fadeout 1
    et "分かってるよ、マヤ。{w}マヤは何も悪くない。マヤを守り切れなかった俺のせいだ。{w}俺はお前に懺悔をしなければ。"
    nvl clear
    play music "audio/bgm/r18.ogg" fadein 2.0
    "\n 彼女の穢れた魂を責任を持って浄化してやらねばならない。それこそ俺が彼女に出来る贖罪だ。"
    "大きく見開いたマヤの瞳孔に俺の姿が映り込む。{w}黒く、大きい瞳に映った俺は絶望していた。"
    stop music fadeout 3
    et "全てが真っ赤に染まる中、ただ一つマヤの顔だけが青白くなっていく。"
    hide screen nvlbox with dissolve
    pause 2
    scene bg10_3 with dissolve
    show screen textbox with dissolve
    play sound "audio/SE/hit.ogg"
    $ _history = False
    my "[na]、この、ゴミカスがあああああああ！！！" with sshake
    $ _history = True
    my "{color=000}やだ…やだ、やめて…！{/color}{fast}{nw}"
    nar "マヤは死にかけの獣の様に浅く息を吐く。乾いて茶色くなりつつある血に染まった服を着て藻掻いている。"
    nar "空を切る脚によって股が開かれた。"
    play sound "audio/SE/hit.ogg"
    $ _history = False
    my "お前のせいで、お前のせいで、お前のせいで！！あああぁああ゛あ゛！！" with sshake
    $ _history = True
    my "{color=000}[na2]くん…やめてよ、お願い…{/color}{fast}{nw}"
    play sound "audio/SE/hit.ogg"
    $ _history = False
    my "死ね！死ね！死ね死ね死ねくたばれくたばれくたばれ！！くたばってよおおおおぁああああああ！！！" with sshake
    $ _history = True
    my "{color=000}こわい、こわいよぉ……！！{/color}{fast}{nw}"
    nar "俺に怒ってくれるマヤ、すごくカワイイな。{w}悪態をつくマヤが大好き。"
    play sound "audio/SE/humanstrike.ogg"
    nar "もっと怒ってくれ、もっと軽蔑してくれ、もっと嫌ってゴミみたいに扱って人間じゃないかの様に扱って無視して"
    nar "蔑んで殴って狂って嫌悪してくれマヤマヤマヤカワイイ！愛してる！アイシテル！" with sshake
    nar "どうやら俺は嫌われる事が性癖だったらしい。"
    play sound "audio/SE/humanstrike.ogg"
    nar "発作を起こすマヤの身体が動物の死骸の様に固くなる。"
    play sound "audio/SE/humanstrike.ogg"
    nar "口から飛び出た真っ赤な舌が軟体動物の様にテカテカと光り、小さい目玉はぐるぐると回っている。"
    nar "俺は至る所に飛び散る血潮と、あちこちで弾けている彼女の一部を余すことなく見届けた。"
    play sound "audio/SE/humanstrike.ogg"
    nar "熱い血の飛沫を顔に浴びたまま拳と腕、脚にじんわりと伝わる余韻に浸る。"
    nar "人間は悔悛の時に過去を思い返すとも言うが、マヤは文字通り幼児退行したように泣きながら悲鳴を上げる。"
    nar "ぽてっとした手が何かを掴むため、もしくは俺を殴ろうと動くも、彼女の手に届いたものは何もない。"
    nar "天使の口から俺の名前、侮蔑、憎悪の言葉が放たれる。{w}それが最期の言葉であった。"
    play music "audio/se/no more bell my buddy.ogg" fadein 2.0
    $ maya_dead = 0
    if persistent.call_CG == True:
        hide screen textbox with dissolve
        show cgmy03 with slowdissolve
        pause 2
        nvl clear
        show screen textbox with dissolve
        jump maya_dlog
    else:
        nvl clear
label maya_dlog:
    $ persistent.dead_maya = True
    $ _game_menu_screen = None
    $ _skipping = False
    $ maya_dlog = renpy.random.choice(("1", "2", "3","4","5"))
    if maya_dead == 20:
        if persistent.call_CG == True:
            show cgmy03_1
        else:
            scene bg10_4
    if maya_dead == 45:
        if persistent.call_CG == True:
            show cgmy03_2
        else:
            scene bg10_5
    if maya_dead == 50:

        $ renpy.quit(relaunch=False, status=0, save=False)
    if maya_dlog == "1":
        $ maya_dead = maya_dead + 1
        nar "マヤは本当にカワイイ。マヤは本物の天使なんだ。"
        jump maya_dlog
    if maya_dlog == "2":
        $ maya_dead = maya_dead + 1
        nar "マヤ・エルベットは天使だ。その理由をここに示そう。ずっと見てきたから分かる。"
        nar "彼女にはきっと人の目には見えない天使の羽が付いている。これはただの推測ではない、確信だ。"
        nar "何故なら、彼女は時折空を飛びたがったからだ。羽のない彼女が空を飛びたがるなら、それは非常に悲しいことではないか。"
        jump maya_dlog
    if maya_dlog == "3":
        $ maya_dead = maya_dead + 1
        nar "この子は俺の大好きな女の子、マヤ・エルベットだ。俺はその天使の顔が誰かに似ていると思っている。"
        jump maya_dlog
    if maya_dlog == "4":
        $ maya_dead = maya_dead + 1
        nar "マヤは最近悲しそうだ。好きな人でもできてしまったのだろうか？"
        nar "この子は俺の大好きな女の子、マヤ・エルベットだ。"
        jump maya_dlog
    if maya_dlog == "5":
        $ maya_dead = maya_dead + 1
        nar "ああ、可愛いマヤ。お前を守ってやりたい。お前の事を一番大切に思ってあげたかった。"
        jump maya_dlog

label day11_my:
    $ _history = True
    show screen quick_menu_12
    $ _game_menu_screen = 'preferences'
    show screen at_frame
    $ persistent.dead_maya = False
    hide screen textbox with dissolve
    scene bg10 with dissolve
    call place10
    pause 1.0
    show screen textbox with dissolve
    nar "朝。真っ白なベッドの上で目覚める。"
    nar "掠れた視界に見慣れた風景が映り込む。どれ程寝ていたのか、気だるい頭痛で頭が割れそうだ。"
    nar "今は何時だろうか。もしかしたら、一週間以上寝ていたのかもしれない。"
    nar "バラバラに砕けた夢の風景が一つ、二つと頭に浮かぶ。その記憶はとても長く、ゆっくりと続いていった。"
    nar "そこで出会った人々や、祈り、ご飯を食べはしゃいだすべての瞬間。その記憶は鮮明では無かったが、確かに脳内に刻まれた。"
    nar "俺はその長い、長い夢が見せる記憶に長らく浸っていたが、暫くしてベッドから起き上がる。"
    nar "脚が震える。ここにはマヤが居ない。"
    hide screen textbox with dissolve
    scene bg02 with dissolve
    call place02
    pause 1.0
    play music "audio/se/prologue wind.ogg" fadein 2.0
    show screen nvlbox with dissolve
    nvl clear
    "\n 外はすっかり晴れていた。ずっと降り注いでいた雨が止み、雲が晴れ、明るい太陽の身が地上を照らしている。"
    "外はまだ寒くて指先が小刻みに震える。"
    "俺は生まれて初めてあんよをする獣の様に一歩ずつ踏み出す。やっとの思いで太陽の光を浴びた途端走り出した。"
    "神殿の扉は堅く閉まっており、辺りは静かだった。急に俺以外の人が消えてしまったわけではない。"
    "皆がこの中で死んでしまったのだ。生命の集うこの神殿で、この大穴で。"
    nvl clear
    "\n 目的地の定められていない道を走り回り、過ぎた記憶を辿ろうと努力を尽くした。"
    "崩れ落ちた俺とのこの一年と、これから襲い掛かってくるであろう全ての事柄に対しての心配。"
    "その何もかもが俺を悲しませるばかりだったが、俺を救ってくれるであろう祈りがそこにあった。"
    "誰もが彼女を普通の少女として見ているが、一時は俺にとっての天使であったという事実に変わりはない。"
    "花壇、部室、作業場…"
    "俺は天使がいそうな場所を彷徨って、ついにあの場所へと辿り着いた。"
    stop music fadeout 3
    et "全てが始まった所、誰もがいずれ戻るべき所へ。"
    hide screen nvlbox with dissolve
    nvl clear

    show screen place_day12_my with dissolve
    hide screen place_day12_my
    $ place = renpy.call_screen("place_day12_my")
    return
label day12_my:
    show screen place_day12_my
    hide screen place_day12_my with dissolve
    scene bgw with dissolve
    pause 1.0
    "{color=#000000}{size=0}{k=0}安らかだと思っている者は衰えている者をさげすみ、足のよろめく者を押し倒す。{/k}{/size}{fast}{/color}{nw}"
    image day12_my = Text("{color=#000000}安らかだと思っている者は衰えている者をさげすみ、\n 足のよろめく者を押し倒す。{/color}", text_align=0.5, slow=True, slow_cps=5 ,size=36)
    if config.language == "English":
        image day12_my_en = Text("{color=#000000}Those who are at ease have contempt for misfortune\n as the fate of those whose feet are slipping.{/color}",text_align=0.5, slow=True, size=27)
        show day12_my_en at truecenter
    elif config.language == "SimplifiedChinese":
        image day12_my_cn = Text("{color=#000000}自以为安宁的人蔑视那些衰弱的人，推倒那些步履蹒跚的人。{/color}", text_align=0.5, slow=True, size=28)
        show day12_my_cn at truecenter
    elif config.language == "Korean":
        image day12_my_kr = Text("{color=#000000}평안하게 사는 자는 재앙당한 자를 멸시하고\n 재앙은 곧 실족하는 자를 기다리고 있구나.{/color}", text_align=0.5, slow=True, size=36)
        show day12_my_kr at truecenter
    else:
        show day12_my at truecenter
    pause 8
    show ctc onlayer screens at ctc:
        xalign 0.5
        ypos 420
    $ _dismiss_pause = True
    $ renpy.pause()
    $ _dismiss_pause = False
    hide ctc onlayer screens
    hide day12_my
    hide day12_my_en
    hide day12_my_cn
    hide day12_my_kr
    with gjdissolve
    scene bg101 with dissolve
    call place101
    pause 1.0
    show screen textbox with dissolve
    play music "audio/SE/prologue wind.ogg" fadein 2.0
    nar "茂った草むらを掻き分けながら走った。醜い真実を秘めていた鉄門は、寿命がきてしまったかのように開け放たれていた。"
    nar "生い茂る草を踏む。汗でびしょびしょになった体に風が触れて寒い。"
    nar "頭に熱が上がっているのか、焦点を失ったかのように世界が揺れている。"
    nar "しかし足を止めずにひたすら進んだ。長い旅が終わろうとしている。"
    nar "草や土でない何かがぶつかる。よく見ればそれは内臓、誰かの腹に収まっていた肉だった。"
    nar "所々で俺の物でない血が腐っていた。{w}刺激的な臭いが頭の中の本能を呼び起こして、あの日の記憶を思い出させる。"
    nar "そのシルエットに小さな女の子の姿が重なる。{w}薄い桃色の髪をした女の子は赤くなった目頭で頭を下げている。"
    nar "その視線は遥かに深い窪みへ落ちる。魂で罪の代償を支払って、贖罪の慈悲を受けた死体を見ながら哀感の混じった表情をしている。"
    nar "例え汚い服を着ていても、痩せ衰えた顔でも、一目で俺は彼女だと解った。"
    nar "この不潔な空間でも決して彼女の光を奪うことは出来ない。"
    pl "マヤ…！"
    show SCG_02 A 8 100 with dissolve
    nar "俺はよろける脚を引き摺りながら彼女に近付いた。"
    pl "マヤ、本当にマヤなんだ、俺、ずっと探してたんだよ…"
    my "……"
    pl "…本当に、ゴメンな、マヤ。"
    nar "謝罪の言葉が口から飛び出る。{w}いや、それは俺の意志だった。まだ贖罪しきれていない罪が俺の中にあった。"
    nar "悔悛の機会があるというのは、告解出来る場所があるという事は、どれ程幸せな事なのだろう。"
    pl "今までずっと酷いことしちゃったこと…反省してるんだ。"
    pl "マトモじゃなかったんだよ、お前なら分かってくれるだろ！俺があの時どれだけ辛かったか…"
    pl "だからちょっとだけ頭がイカれちゃってたみたいなんだ。"
    pl "で、でもだからといってお前にあんな八つ当たりなんかしちゃいけなかったのに…"
    pl "今は後悔してる、ホントだ！本気じゃなかったんだ、分かるだろ？{w}なあ、マヤは、マヤだけは俺のこと、分かってくれるよな？"
    my "……"
    nar "彼女は返事をする事無く俺を見つめる。{w}重い首がまた下を向いてしまうのが怖くて、腕を掴んでこちらへと引っぱった。"
    nar "枝のような腕にくっついた身体はいとも容易く俺に寄る。"
    pl "ここから逃げよう。"
    nar "俺たち二人で、花が咲き木々が生い茂る、俺たちを脅かす事のない心豊かな人々の居る場所へ。{w}出来る限り、遠く、"
    nar "今度こそ間違わないから…"
    hide SCG_02 with dissolve
    nar "一歩前へ踏み出すと、じめじめした地に靴が沈んでしまう。{w}それを無視して何歩か更に歩いたら、靴の踝が滑って泥に沈み込んだ。"
    nar "足取りが重くなって我慢していた息を吐く。肺が潰れそうな激痛、雨でもないのに髪が濡れている。"
    nar "汗でじっとりとした手を彼女が握っている。引っ張る手に力が入って、同じく荒く息をしていた彼女が俺の名を呼んだ。"
    my "[na2]くん。"
    nar "マヤは俺の手を離し、暖かい表情を見せる。一歩進んで、俺のすぐ前に立った。"
    show SCG_02 A 1 100 with dissolve
    my "誓いのキスをしよう。"
    nar "彼女の両腕が俺の身体を優しく包む。{w}彼女は数多の誓いの内、一体俺にどれを誓ってほしいと願っていたのだろうか。"
    nar "永遠無事に無害な存在として生きるという誓い？{w}もしくはマヤを遠く、安全なところまで連れて行くという誓いか？"
    nar "それともこれからの幸せを願う誓い？"
    nar "そのどれでも構わない。彼女がそうと願うのであれば、俺は、何だって聞いてやれる。"
    hide SCG_02 with dissolve
    hide screen textbox with dissolve
    scene black with dissolve
    show screen nvlbox with dissolve
    stop music
    nvl clear
    "\n その瞬間、体が押し出された。"
    "軽い力が俺の体を押して、すぐ消える。{w}落ちる。{w}落ちている。"
    "浮かんだ服と髪が上へ跳ね上がる。{w}真っ逆さまになった体を立てようとしても、足が床に付いていない。"
    "眼前を満たした黒い渦巻が俺を飲み込もうと動いている。"
    "数え切れない罪が急流のように目の前を過ぎていく。"
    "明るい日の下で人の目を恐れて、しでかした罪を隠す為に深く、更に暗い所に入らなければならなかった日々が俺を追い詰める。"
    et "だからこそ結局こんな所まで来てしまった。{w}更に深く、更に暗い所へ。誰も彼を見つけられない所まで。"
    hide screen nvlbox with dissolve
    show bg12 with dissolve
    pause 1.0
    hide bg12 with dissolve
    nvl clear
    pause 1.0
    show screen nvlbox with dissolve
    play music "audio/bgm/Maya.ogg" fadein 2.0
    "\n [na]の身体は真っ暗な穴のどん底へと消えた。"
    "マヤ・エルベットはぼやけた視界で彼の身が落ちていく姿を見守る。{w}闇の中で未だ生きている彼の影が動く姿を見守る。"
    "その動きが死体の山の上で完全に動きを止めるまで、ただゆっくりと見守る。"
    "何の兆しも無かったが、終わりを感じ取ると重い脚を動かした。自身の物ではない足音がゆっくりと重なっていく。"
    "冥土に堕ちた者が亡者として生きる様に、穴に落ちた人間は二度と這い上がっては来られない。{w}マヤ・エルベットはそんな道を歩いて行く。"
    et "濁った煙に目が痛くなり、ふと自身が歩いてきた道を振り返る。"
    nvl clear
    "\n 色褪せた神殿に霞の様な煙が昇っていく。過敏になった五感が燃える音を聞いた気がした。"
    "誰もがその場所を「楽園」と呼んだ。{w}しかし彼女は皆が向かう方向とは逆に、独り歩いていく。二度は振り返らない。"
    $ _skipping = False
    "告解する事のない罪は元より在るべき場所へ、その機会は生きる者にのみ与えられり。"
    hide screen nvlbox
    scene bg101
    show SCG_02 A 00 100
    with dissolve
    pause 1.0
    show SCG_02 1 with slowdissolve
    pause 2
    nvl clear
    hide screen keymap_screen
    $ _game_menu_screen = None
    $ show_quick_menu = False
    hide screen at_frame
    scene black
    with slowdissolve
    $ _dismiss_pause = False
    $ persistent.dmy = 0
    $ persistent.hssh12end = True
    $ renpy.quit(relaunch=False, status=0, save=False)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
