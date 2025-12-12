
label hkb_fail:
    show SCG_06 0 with fastdissolve
    hk_b "明日からは忙しくなるな…{w}会えなくなるかも知れない。"
    show SCG_06 1 with fastdissolve
    hk_b "が、神殿で会ったら挨拶くらいはしようじゃあないか。"
    hide SCG_06 0 with dissolve
    nar "そうやって離れていくハクの背中はなんだか寂しく見えたが、ボクに彼女を引き留める事が出来なかった。"
    $ _skipping = False
    nar "仕事が忙しいのは事実だし、仕方ないよな…{w}ボクも業務に集中しなきゃ。"
    $ meet_hkb = False
    return
label day7_neru:
    $ meet_hkb = False
    show screen textbox with dissolve
    nar "……"
    $ _skipping = False
    nar "廊下で扉の開く音がした。"
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
    jump day8_sc
    return

label day8_neru:
    $ meet_hkb = False
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
    jump day9_sc
    return

label day9_neru:
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
    $ meet_hkb = False
    jump day10_sc
    return

label day7_hk:
    hide screen textbox with dissolve
    pause 3
    menu:
        "眠る":
            jump day7_neru
        "眠らない":
            show screen textbox with dissolve
            nar "…全く眠れない。"
            hide screen textbox with dissolve
            pause 3
            menu:
                "眠る":
                    jump day7_neru
                "眠らない":
                    show screen textbox with dissolve
                    nar "シーキュレットは乱れた部室を片付けているのだろう。"
                    nar "倒れた机と椅子を立てて、ゴミだらけの床を掃いて、自分が垂らした血を拭いて…"
                    hide screen textbox with dissolve
                    pause 3
                    menu:
                        "眠る":
                            call day7_neru
                        "眠らない":
                            show screen textbox with dissolve
                            nar "もし明日シーキュレットが俺のところへ再びやってきたらどうしようか。"
                            nar "そうならなかったら奴は明日から俺を避けるだろうが、また変な噂が広がらないように注意するべきだ。"
                            hide screen textbox with dissolve
                            pause 3
                            menu:
                                "眠る":
                                    call day7_neru
                                "眠らない":
                                    show screen textbox with dissolve
                                    nar "とにかくこれから一ヶ月は耐えないと。{w}一ヶ月、一ヶ月、一ヶ月もここで、チクショウ…"
                                    nar "殺してやる殺してやる殺してやる殺してやる殺してやるコロシテヤルチクショウチクショウアノアバズレノセイデ"
                                    hide screen textbox with dissolve
                                    pause 3                                
                                    menu:
                                        "眠る":
                                            call day7_neru
                                        "眠らない":
                                            show screen textbox with dissolve
                                            nar "アルネがその噂を聞けばどう思うんだろう…"
                                            hide screen textbox with dissolve
                                            pause 3
                                            menu:
                                                "眠る":
                                                    call day7_neru
                                                "眠らない":
                                                    show screen textbox with dissolve
                                                    nar "………"
                                                    hide screen textbox with dissolve
                                                    pause 3                                
                                                    menu:
                                                        "眠る":
                                                            call day7_neru
                                                        "眠らない":
                                                            show screen textbox with dissolve
                                                            nar "廊下で扉の開く音がした。"
                                                            $ save_name = "day 7, 夜, 楽園"
    stop music fadeout 3
    hide screen textbox with dissolve
    scene black with slowdissolve
    pause 2.0
    show screen nvlbox with dissolve
    nvl clear
    "\n 時間が流れることも忘れて降り注いでいたシャワーの水栓を閉める。"
    "頭の上から騒がしく流れる水の音が止むと、辺りはしんと静まり返った。{w}もう夜だ。"
    et "密閉されたシャワー室から出て外の空気をゆっくりと吸えば、冷えた唇が震える。"
    nvl clear
    "\n 人のいない神殿は恐るべし静かだ。{w}真っ直ぐな廊下を歩く途中ちらりと見た窓の外は、白い光に染まっている。"
    et "太陽の沈まない日は苦しい。{w}隠れる場所がなくなった気がするから。だからこそ更に迷わず歩き出した。"
    hide screen nvlbox with dissolve
    scene bg03_1 with slowdissolve
    call place03
    pause 1.0
    show screen nvlbox with dissolve
    nvl clear
    play music "audio/SE/prologue wind.ogg" fadein 2.0
    "\n 外に出たことを実感するような風が未だ濡れたままの髪の隙間に吹いてきた。"
    et "こんなに冷たい空気に身体を委ねていると、まるで自分の身体が綺麗になっていくような錯覚に陥る。"
    nvl clear
    "\n 嫌味ばっかだとよく言われるが、実際ボクにも好きなものくらいはある。{w}例えば、夜が好きだ。"
    et "作業をしなくてもいい、疲れた体を休められる、そしてシャワーを浴びれる。{w}夜は、自分を大切にできる時間だ。"
    nvl clear
    "\n それとこの神殿と今の職も好きだ。"
    "本来なら路頭に迷い他人が捨てた皿の残りカスでも舐めながらその日の命を繋いでた筈のくだらない人生。"
    "そんな子供を集めては空っぽの頭に知識を入れて、卑しい手に道具を握らせ、国のために働かせる。"
    stop music fadeout 3
    et "何て素晴らしきことだ。"
    nvl clear
    hide screen nvlbox with dissolve
    pause 1
    scene bg02_1 with dissolve
    pause 1
    show screen nvlbox with dissolve
    $ _history = False
    et "\nさて…{w}どこへ行こうか？"
    $ _history = True
    hide screen nvlbox with dissolve
    show screen place_day7_hk with dissolve
    hide screen place_day7_hk
    $ place = renpy.call_screen("place_day7_hk")

label day7_hkR:
    show screen place_hkB
    show screen place_day7_hk
    with None
    hide screen place_hkB
    hide screen place_day7_hk
    scene bg101_1 with dissolve
    call place101
    pause 1.0
    show screen textbox with dissolve
    nar "生い茂った草を掻き分けて、微かに木の実特有の苦い匂いがすればあの建物が姿を見せる。"
    nar "人の足跡が途切れた森の中でたった一つ聳え立つ礼拝堂は、"
    nar "未だに過去の栄光を保った厳粛な空気を醸し出している。"
    nar "ボロボロになったドアノブを思いっきり押さえて扉を開く。"
    nar "鍵の掛かっていない扉は重たい音を響かせ徐々に外の風を受け入れた。"
    hide screen textbox with dissolve
    play sound "audio/se/door close.ogg"
    pause 1.0
    scene bg100_1 with dissolve
    call place100
    pause 1.0
    show screen textbox with dissolve
    play music "audio/bgm/golden haku.ogg" fadein 4
    nar "彼女がそこに立っている。"
    nar "沈まない太陽の燦爛とした祝福の前で両手を合わせたまま、何かの為に祈りを捧げている。"
    nar "一筋ずつ光を反射させる真っ白な髪。のっぺりした肩から滑らかに続く背中の輪郭。"
    nar "小さな埃が日差しを受けてはきらきらと周りを漂う。"
    nar "長くもこの崇高な空間を守ってきた扉が再び重たい音と共に閉じられ、彼女がゆっくりと顔を向ける。"
    nar "長いまつ毛の下に秘められた瞳は窓から入ってきた光の下で黄金に輝いていたが、"
    nar "ボクの立っている陰に入るや青を取り戻す。"
    nar "その瞳に自分の姿が映るところを見たくなくて顔を垂れると、すぐ顎を掴まれた。"
    nar "目の前まで迫ってきた青は、目が眩んでしまうほどに清涼だ。"
    show SCG_06 0 with dissolve
    hk_b "なんてツラをしているのだ、"
    nar "夜はいい。{w}安らかに目が閉じられるし、人のいないシャワー室が使えるし、静かな神殿を歩けるが、"
    nar "決して一人ではないから。"
    show SCG_06 1 with dissolve
    hk_b "シーキュレット。"
    stop music fadeout 2
    nar "ボクはハク・エカルランと密会している。"
    hide SCG_06 with dissolve
    hide screen textbox with dissolve
    scene black with slowdissolve
    pause 3
    play music 'audio/SE/prologue wind.ogg' fadein 2
    show screen nvlbox with dissolve
    nvl clear
    "\n ボクは州都の滓が排出される狭い村で生まれた。"
    "家族は平凡だった。{w}幼いうちに母になった女と、女に愛される男二人。"
    et "その中で厄介者のように十一年程暮らしてきた。"
    nvl clear
    "\n 貧乏だったが、故郷での生活はとにかく幸せだった。家族を愛していたから。"
    "今はその幸せが、幼いボクの錯覚だと分かっている。{w}あの時のボクは、幸い平凡を知らなかった。"
    "母さんが可哀想な人だという事実に気付いた頃、ボクらの家族は崩壊した。"
    "彼女が大変愛した兄が家族の縁を切って、ボクと彼を繋いだ縁も切られた。{w}一枚の身分証明書と若干の金だけを置いて。"
    "貧民街の子であるボクにとって金銭欲はつまり生存欲だった。稼いでいるから体は生きている。{w}しかし精神は死んでいるかもしれない。"
    nvl clear
    "\n 「シーキュレット・レイフ」という名の司祭はそうやって生まれた。"
    stop music fadeout 2
    et "人前に出すには恥ずかしい黄色の身分証明書の代わりに、神の栄光を示す銀色の十字架を抱えて新たな生を始めたのだ。"
    hide screen nvlbox with dissolve
    scene bg101_1 with slowdissolve
    pause 1.0
    show SCG_06 0 with dissolve
    show screen textbox with dissolve
    play sound "audio/se/ding.ogg"
    hk_b "おい、あまりボーっとしてるなよ。風邪をひくぞ。"
    sc "ちょっと考え込んでただけさ。{w}ボクが風邪をひくならそれはここが寒すぎるせいだろ…"
    play music "audio/bgm/golden haku.ogg" fadein 4
    show SCG_06 8 with fastdissolve
    hk_b "冷たい風に当たらんと顔の腫れが引かんだろ？{w}ヤレヤレ、年頃の娘がこんな薄汚い顔しちゃってどうする。"
    hk_b "天にまします我らが母も悲しむぞ？"
    nar "「天にまします我らの父よ」の事か…"
    sc "ボクの顔が汚いのはいつもの事だろ、ハク。{w}何で仮にも主教がそんなヘンな事ばっかり言うんだい？"
    show SCG_06 9 with fastdissolve
    hk_b "そりゃ当然君のつまらん神殿生活に些細な楽しみを一つまみ与えてやる為さ。"
    hk_b "なのに君の反応と来たら日々薄れるばかりで。"
    sc "そんなに暇なの？"
    hk_b "そんなこった。ジョークの一つも返せない君との会話以外の時間はね。"
    hide SCG_06 with dissolve
    nar "紹介しよう。彼女はハク・エカルラン。"
    nar "燦爛とした光の下で黄金のように光る昼の姿は彼女が作り出した幻想に過ぎず、"
    nar "こうやって闇に隠れている方が本物の彼女だ。"
    nar "ハクは待つだけの祈りよりは行動を好み、神に依存するよりは人の手で人を助けることを大事にしている。"
    nar "しかし、その淀みない性格と話し振り、悪い手癖のせいで主教が適性がなく、"
    nar "今は「主教様」に大部分の時間を任せている。{w}これがボクと彼女の秘密。"
    nar "彼女が本物の自分でいられる時間はボクと会う短い夜だけで、ボクは彼女の話し相手という訳だ。"
    show SCG_06 0 with dissolve
    sc "ボクは人の衣を被った禍のフリをして奇妙な台詞を並べながら"
    sc "純粋な新入司祭をからかう事がキミの趣味だと思ってたんだけど。"
    hk_b "一体何時の話をしているんだ？{w}アレはもうやめちまったよ。良さげな機会もなさそうでな。"
    show SCG_06 12 with fastdissolve
    hk_b "台本も練っておいたというのに。"
    sc "仕事もそれくらい熱心にやってくれ…"
    hk_b "奴がいつか私を見つけ出せると思ってたんだよ。"
    nar "ボクらが毎晩集まる野外礼拝堂は元々立ち入り禁止だが、偶に勇敢な司祭が迷って入る事がある。"
    nar "ボクとしてはそうありがたくないことだ。"
    sc "あぁ…そっか、[na]の事か。{w}キミは案外あいつの事が気に入ってるんだね。"
    hk_b "気に入ったというよりかは、人目を惹くような人物ではあるな…"
    show SCG_06 1 with fastdissolve
    hk_b "君の様に。"
    sc "…また彼がここに来てたのかい？"
    show SCG_06 11 with fastdissolve
    hk_b "いや。だからそんなに顔を顰める必要はない。{w}汚い顔がも～っときちゃなくなるだろう？"
    sc "ボクはここに他人が入ることは望んでいない…"
    sc "暇なのは充分分かるけど、キミにも警戒心というものがあるならもっと気を付けてくれ。"
    sc "ここは禁じられた場所にしてはあまりにも入って来やすいんだから。"
    sc "禁止というものは人を刺激するだろう。世間知らずの新入りなら尚更。"
    show SCG_06 1 with fastdissolve
    hk_b "これで充分だ。秘密はその場に存在するという事実だけで守られる気分になれるからな。"
    sc "それだけじゃ不安だから人は秘密に秘密を重ねるんだよ。"
    hk_b "その口ぶりじゃあ、君はここが大分気に入っている様だな。"
    sc "慣れただけさ…ここは立ち入り禁止の区域だろう。好きになる訳にはいかないよ。"
    hk_b "しかし君はあまりにも情が深い。嫌いになる訳にはいかないんだろう。"
    sc "……だから、ボクらはもうちょい気を付ける必要があるんじゃないかって話だよ。"
    sc "誰かが偶然ここでボクらと会っちゃったらどんな風に見られるかわからないだろう？"
    show SCG_06 9 with fastdissolve
    play sound "audio/se/ding.ogg"
    hk_b "「こんな風」……じゃないかね？"
    sc "「こんな風」って何なんですか…？"
    show SCG_06 11 with fastdissolve
    hk_b "不正入社した信用のない人間と、ソイツを受け入れてしまう頭パッパラパーの主教。"
    hk_b "こう言いたいんじゃないのか？"
    sc "…まぁ、そうだね。"
    nar "ボクがハクに出会ったのは九ヶ月も前、特に説明することもないほどただの偶然だった。"
    nar "隠栖が体質に合わなかった彼女は、よく愚かな新入生に疑われた。"
    nar "そんな彼女に呼ばれて初めて野外礼拝堂に来た時、ボクはこの場所が好きではなかった。"
    nar "腐ったゴミと死体を投げ入れる穴の隣で放置されていた姿にぞっとした。"
    nar "しかしそれが日常となり、もう一人でここに来られるほどこの場所に慣れてきた。"
    show SCG_06 0 with fastdissolve
    hk_b "そんなに心配せずとも当分ここに誰かが来る事は無い。もう少ししたらあの穴に火を灯す心算だからな。"
    sc "あの穴？そんなにゴミが溜まってたんだ…{w}やるとは聞いていたけど、直接見るのは初めてかも。"
    show SCG_06 12 with fastdissolve
    hk_b "ああ。その時は私達もここには居られまい。{w}寒いな…そろそろ入ろうか。"
    hide screen textbox with dissolve
    hide SCG_06 with dissolve
    pause 1
    scene bg100_1 with dissolve
    call place100
    pause 1.0
    show screen textbox with dissolve
    nar "さっきと全く同じ扉なのに、ハクと共に入る際はなんだか軽く見える。ボクらはいつもここで言葉を交わす。"
    nar "外は時間帯に似合わず未だ明るいが、彼女のいる所だけに日が避けているように暗い陰ができていた。"
    nar "闇の下で彼女の瞳は青に沈む。やっと元の居場所に戻ってきた気がして、ボクの気持ちも共に落ち着く。"
    show SCG_06 11 with dissolve
    hk_b "で、今日はどうした？友達と喧嘩でもしたのか？{w}ん？"
    sc "…離してよ。"
    nar "ボクの肩を抱く手を軽く押し返して、冷たい所に座った。"
    nar "ボクは所謂「陰口」が苦手だが、それに対してハクは他人についての話を好む。"
    nar "口数の多い彼女の話をボクが聞いていることが多かったが…"
    nar "最近はそれも飽きてきたのか、ボクの話を聞きたがるようになっていた。"
    show SCG_06 1 with fastdissolve
    hk_b "その様子からして図星だな。ならばあえて言おうではないか、「おめでとう」。"
    hk_b "私は君があの二人とあまり親しくしてほしくなかったものでな。"
    nar "この言葉が妬みや嫉妬のようなものだったらよかったのにな。"
    nar "しかし只「処理班の役に立たない友人は君を愚かにする」という鋭い裏が秘められているだけだ。"
    nar "悔しいが、ボクも彼に同感だ。"
    sc "あの二人、って。{w}今回入った新入り二人の事かい？"
    show SCG_06 11 with fastdissolve
    hk_b "当然だろう？{w}一目でわかるぐらいに目立っていたぞ。あの二人が入って以来の君を振り返ってみろ。"
    hk_b "最初の数日は怒っていたのに、妙に浮かれてもいて、話に全く集中していない、"
    hk_b "二人のミスの尻拭いで礼拝堂に来るのも遅れてたし。しかも今日はそんな顔で現れて…"
    sc "……"
    show SCG_06 9 with fastdissolve
    hk_b "…私を避けるし。それが話し相手に対する態度か？"
    sc "何だか楽しそうだね、ハク…"
    show SCG_06 1 with fastdissolve
    hk_b "先程言ったように君を祝ってやりたいからな。"
    hk_b "しかし君が悲しいと感じて居たいのであれば、その時は慰めてやろうじゃあないか。"
    sc "悲しい？{w}ボクは……{w}別に悲しくはないよ。"
    sc "誤解してるようだけど…ボクはあの二人とそんなに仲が良かった訳じゃないんだ。"
    sc "単に話す頻度が多くて、もう騙しきれないなって思っただけ。どうせいつかはバレる事だったんだし……"
    sc "寧ろ良かったと思う…"
    nar "落ち着いて話せたが、何故か心拍は大きく聞こえてくる。早く静まることを願ってため息を吐いた。"
    show SCG_06 0 with fastdissolve
    hk_b "ふぅん…{w}ま、君は嘘が下手だしな……"
    sc "…今になってこんな話をする事に意味はあるかい？"
    sc "重要なのは彼があと一か月は浄化部に居るだろうという事実だけ。"
    sc "そうなれば当分魔導部の兵力が増えることは無いし、"
    sc "彼の聖痕の変化をもう少し近場で観察することもできるだろう。"
    hk_b "強引な解決法だな。わざとか？"
    sc "あれは…本当に間違えちゃっただけなんだ…"
    sc "でも、ボクがこんな事を考えているというのが事実である以上もう彼と仲良くなんて出来ない。"
    hk_b "彼を引き留めようとバカみたいな事もしでかしたしな。"
    sc "キミが絶対行けるなんていうから。"
    show SCG_06 10 with fastdissolve
    hk_b "ハ。ハ。ハ。{w}私は天下りの主教であって、預言者モドキではないのだ。"
    show SCG_06 12 with fastdissolve
    hk_b "しかしまあ…あの年頃は容易く錯覚するもので、ままごとに熱中出来るだろうと思っていたのだが…"
    hk_b "見かけよりは頭が冴えていた様だな。"
    nar "浄化部は彼らの幼い精神力だけでは耐えられない厳しい所だ。{w}だからそこかしこで妙な雰囲気が漂う。"
    nar "辛すぎるから、少しでも心を寄せる所ができたら、それを恋愛感情だと勘違いしてしまうのだ。"
    nar "彼にそういう感情が生まれれば、浄化部に未練を残してくれると考えたなんて……{w}馬鹿らしい。"
    show SCG_06 1 with fastdissolve
    hk_b "どちらにせよ……良かったな。{w}君は大事な時期を控えているんだ。そちらに集中せんと。"
    nar "ボクが口を噤んだことを気にしているのか、ハクの声が柔らかくなる。"
    nar "今までのように祝うのではなく、慰めることにしたようだ。騒がしかった心拍が再び安定を取り戻す。"
    nar "彼女が耳の痛い話をしてくる時は、必ず最後にはボクが欲しい言葉をかけてくる。"
    nar "それに本気で安心してしまうボクが少し憎い。"
    sc "そんなの、キミがわざわざ言わなくたって解ってる。{w}明日からはまた仕事に集中するつもりだし…"
    sc "今日だけでも大分時間を喰ってしまったんだ。これからはそんな事にならないように気を付けるよ。"
    nar "心を入れ替える。"
    nar "彼が浄化部に残ってほしかったのは、さっき話していたように浄化部と敵対する魔導部に利を与えない為だ。"
    nar "エルジェーベトの計画を邪魔して、彼の聖痕を観察する時間を稼ぐ為だ。"
    nar "そしてボクには今度の聖夜、正式な司祭になって浄化部の補佐教になる目標がある。{w}それだけだ。"
    sc "ボクは忙しい。これからはもっと忙しくなる。"
    sc "今まではまだ余裕があったから、雑念が混じってしまったみたいだ。"
    show SCG_06 11 with fastdissolve
    hk_b "君は変わり者だな。普通はもっと仕事がしたいとは言わんだろう？{w}休みたいとは言うがな。"
    sc "ボクがどんな人間だろうが気にしないでよ、ハク。"
    sc "キミの利益だけを考えるなら僕がもっと働いた方が都合がいいんだろ？"
    show SCG_06 9 with fastdissolve
    hk_b "そうだな。そういう個人の考え方がいつしか団体を作り上げるのだろう。"
    sc "……"
    show SCG_06 0 with fastdissolve
    hk_b "一つ聞きたいのだが…新入りの件しかり、君はなぜそこまで頑張って働きたがるんだ？"
    play sound "audio/se/ding.ogg"
    nar "ボク？{w}ボクが頑張って働くのは…"
    hide screen textbox with dissolve
    pause 1
    menu:
        "キミの為だ":
            show screen textbox with dissolve
            sc "キミの為に決まってる。浄化部の為の仕事も、彼を引き留めたのも…{w}今更それ聞く？"
            hide SCG_06 with dissolve
            nar "ボクの答えに、ハクはしばらく何も言わなかった。"
            nar "偶にこうやって話を止めてただ微笑む。"
            nar "その笑みは少なくとも面白い時の表情ではなくて、ボクも釣られて口を閉じてしまう。"
            show SCG_06 1 with fastdissolve
            hk_b "君が何故私にここまで時間を割いているのか分かるか？"
            sc "それは……キミがボクの上司だから？"
            hk_b "まあ、正解だな。"
            nar "…違うのか？ハクの考える事は分かりそうでやっぱり分からない。"
            $ love_hkb = True
        "ボクの為だ":

            show screen textbox with dissolve
            sc "決まってるだろう、お金の為だよ。"
            show SCG_06 11 with fastdissolve
            hk_b "ヘェ、補佐教になったとてそんなに賃金が上がる訳でもないのにか。"
            sc "だから違くて、言うなら…{w}ボクの働き虫っぽい性格は金を稼ぐために出来たものだから、今は…"
            sc "その目標が補佐教に変わっただけで…？"
            hk_b "君も自分の言ってることがめちゃくちゃだという事がわかるよな？"
            sc "う……ハクは何をそんな偉そうに…"
            hk_b "私は常にエラ～いからな。{w}まぁ…そうか、金を沢山稼ぎたいと。初めて会った頃も確か言ってたな。"
            show SCG_06 10 with fastdissolve
            show SCG_06 at bounce
            hk_b "ハハ！君はいつ見ても面白いな、シーキュレット！"
            play sound "audio/se/hit.ogg"
            nar "…またからかったな！" with sshake
            $ love_hkb = False

    sc "何で急にそんな事を聞くんだい？"
    show SCG_06 0 with fastdissolve
    hk_b "君の意見を聞きたかったからだな。"
    hk_b "浄化部の仕事を‘好き好んで’やる人は滅多にいない。"
    hk_b "悲しくないかね？{w}全ての人間は自身の人生の中で主人公である筈なのに、"
    hk_b "それでも世界は変わることなく汚いままだ。だから誰かしらは他人が撒いた汚物を片付けなければならない。"
    hk_b "誰だってこんな生涯など望んだ事ないだろうに。"
    sc "確かに…誰も望まない仕事ではあるね。"
    sc "でもこれはボクの意志なんだ。浄化部の仕事はあくまでも人の為の仕事、人を生かす仕事だろう。"
    sc "何だろうとボクが価値を見出せるのなら、それは価値のある事なんだ。"
    show SCG_06 1 with fastdissolve
    hk_b "上手いこと言うな。だから君の事は好きなんだ。"
    hk_b "「誰かは必ずやらなければならないから」嫌々やるのではなく、望んでやっているという点でな。"
    sc "他人事の様に言って。教えてくれたのはキミだろう。"
    hk_b "まあ…そうだな。"
    nar "ハクはボクに色んなことを教えてくれる。"
    nar "ボクが所謂「ぼんくら」だってことを考えても、ハクの知識は少し特別だった。"
    nar "禍は人の身体と魂を蝕むから、禍から被害を受けた人は異常な行動を見せる。"
    nar "それが州都の常識だが、彼女は人の精神が病むことと禍は一切の関係もないと言い立てている。"
    nar "ボクも最初は「精神が病む」という概念が分からなかったが、次第に二つの現象の差が分かってきた。"
    hk_b "それはそれとして…"
    nar "ハクはボクの短い髪を指に巻きつける。"
    nar "彼女と初めて会った頃はボクもまだ新入りで、あの時は長い髪をしていた。"
    sc "…髪はもう伸ばさないよ。仕事の邪魔になるし。"
    show SCG_06 11 with fastdissolve
    hk_b "なら近い内に少し整えてやらんとな。私が覚えていた頃よりかは長くなってる。"
    hk_b "その横髪は一体何時切るつもりなんだ？"
    sc "横髪…？何の横髪？"
    show SCG_06 at huruhuru
    hk_b "いや…何でもない。{w}いい。"
    sc "何で笑うんだよう……"
    hk_b "君は鏡を見るどころか、自身の身嗜みを整えないから分からないだろうが…"
    hk_b "君と毎日会っている私としては君の些細な違いも大きく感じられるのだよ。"
    sc "ボクの髪の毛以外であの頃と変わったところがあるのかい？"
    show SCG_06 12 with fastdissolve
    hk_b "うむ。"
    nar "ハクはボクから視線を逸らし言う。昔の記憶を思い出す時の癖だ。"
    hk_b "冷静になったな。"
    sc "能率が上がったんでしょ。"
    hk_b "死や些細な哀しみに足を引っ張られなくなった、と言えば良いものか。{w}どんな状態でも泣かなくなったな。"
    show SCG_06 0 with fastdissolve
    hk_b "初めて手術を行った日を覚えているか？{w}君が髪を切って、新しい衣服を貰った日の事だよ。"
    hk_b "同行者が皆死んでしまったせいで、葬式で虐められていただろう。"
    nar "ハクは昔話をする度に、まるで記憶を失った患者を扱うように言う。"
    nar "勿論ボクは記憶を失っていない。だからこういう時、彼女の言葉にどう反応すればいいのか分からない。"
    hk_b "あの時私は君が叫ぶか泣き出すかと思っていたものでな。普通の子供がそうするかのように。"
    hk_b "しかし君は涙一つ流さなかった。前日まではそんな顔をするような奴じゃあなかったのにな。"
    sc "それは悪い意味？"
    show SCG_06 1 with fastdissolve
    hk_b "そう思われたとは心外だな。{w}逆だよ。"
    hk_b "それを見て君が強くなったのだと感じたのだからな。私は君の成長を誇りに思う。"
    sc "……コホン。"
    show SCG_06 9 with fastdissolve
    hk_b "まさか私が君の事を褒めるだなんて思ってなかっただろう？"
    nar "ボクは彼女に関して何もかも知っているつもりでいたが、まだ知らない面もあるのだろう。"
    nar "そしてボクを知らないのは彼女も同じだろうに、彼女はボクに対して何でも知っているかのように振る舞う。"
    show SCG_06 1 with fastdissolve
    hk_b "明日からはどうするつもりだ？"
    sc "いつも通り普通に。何を期待していたのかは分からないけど、君の期待する楽しい事なら他を当たった方がいいよ。{w}晩御飯は？"
    show SCG_06 10 with fastdissolve
    show SCG_06 at bounce
    hk_b "外で。{w}酒！そして肉！"
    show SCG_06 1 with fastdissolve
    hk_b "…と言いたいところだが、今日は簡単に済ませるつもりさ。この後に仕事があるんでな。"
    sc "今日の業務、まだ終わってなかったの？{w}ボク…知らなかったんだけど。"
    show SCG_06 0 with fastdissolve
    hk_b "そうか。"
    nar "ハクは口が多いが、ボクが本当に知りたいことは言わない。"
    nar "その噤んだ口から出てくる言葉が「君が知らなくていいこと」か、"
    nar "「君が知ってはいけないこと」か、ボクは恐らくこれからもずっと知らないままだろう。"
    sc "ハク、明日もここに来るのかい？"
    nar "代わりに別の質問をする。{w}ボクはいつも別れる前に、ハクに同じことを問うていた。"
    nar "だからそろそろ慣れて当然だろうに、どうしてまだ手が震えているんだ。それはきっと彼女の態度のせいだろう。"
    if love_hkb == False:
        call hkb_fail
    else:
        show SCG_06 1 with fastdissolve
        hk_b "勿論さ。私が君を呼び出しているのだからな。{w}だから明日も来なさい。共に雑談でもしようじゃあないか。"
        nar "そしてハク毎回初めて聞いたかのような態度でいつも同じことを言う。恐らくボクを調教でもしたいんだろう。"
        nar "この瞬間ボクは数多くの不満を抱くが、結局従順な部下として頷く。"
        $ _skipping = False
        nar "これでボクの一日は終わる。{w}明日も頑張らないと、そう思って。"
        $ meet_hkb = True
    stop music fadeout 2
    hide SCG_06 with dissolve
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
    jump day8_sc
    return

label day8_hk:
    play music "audio/se/no more bell my buddy.ogg" fadein 5
    hide screen textbox with dissolve
    pause 3
    menu:
        "もう眠る":
            jump day8_neru
        "まだ眠れない…":
            show screen textbox with dissolve
            nar "………"
            hide screen textbox with dissolve
            pause 3
            menu:
                "もう眠る":
                    jump day8_neru
                "まだ眠れない…":
                    show screen textbox with dissolve
                    nar "………"
                    hide screen textbox with dissolve
                    pause 3
                    menu:
                        "もう眠る":
                            jump day8_neru
                        "まだ眠れない…":
                            show screen textbox with dissolve
                            nar "………"
                            hide screen textbox with dissolve
                            pause 3
                            menu:
                                "もう眠る":
                                    jump day8_neru
                                "まだ眠れない…":
                                    show screen textbox with dissolve
                                    nar "………"
                                    hide screen textbox with dissolve
                                    pause 3
                                    menu:
                                        "もう眠る":
                                            jump day8_neru
                                        "まだ眠れない…":
                                            show screen textbox with dissolve
                                            nar "………"
                                            hide screen textbox with dissolve
                                            pause 3
                                            menu:
                                                "もう眠る":
                                                    jump day8_neru
                                                "まだ眠れない…":
                                                    show screen textbox with dissolve
                                                    nar "………"
                                                    hide screen textbox with dissolve
                                                    pause 3
                                                    $ save_name = "day 8, 夜, 楽園"
    show screen nvlbox with dissolve
    stop music fadeout 2
    scene black with dissolve
    nvl clear
    "\n 考えてみればボクは空っぽだった。周りに気を配ったとして、残るものは何もない。"
    "アイツに反応しなかったことも同じ理由だ。{w}[na]は単なる八つ当たりによって価値のない物を壊した…それだけ。{w}だから大丈夫。"
    et "ボクは要らないものに気を取られるほど暇じゃない。{w}ボクが守るべきものはたった一つ。{w}ボクの人生に意味を与えてくれた、たった一つの……"
    hide screen nvlbox with dissolve
    pause 2.0
    scene bg101_1 with dissolve
    call place101
    pause 1.0
    show screen textbox with dissolve
    play music "audio/SE/prologue wind.ogg" fadein 2.0
    nar "ハクは色んな趣味を持っているが、そのくだらない趣味の一つはボクを驚かせることだ。"
    nar "物陰に隠れては突然飛び出てくるが、隠れる場所がいつも同じでそろそろ驚くフリをするのも疲れてきた。"
    nar "またも彼女は自らの高い背を気にせず隠れている。{w}ボクは敢えて森路に逸れ、足音を消す。"
    nar "いつも見ている後姿だが、ボクを探そうときょろきょろしている姿は見慣れない。"
    sc "ハク。"
    show SCG_06 5 with dissolve
    play sound "audio/se/hit.ogg"
    hk_b "うっわビックリした！{w}な、なん？何だ？" with sshake
    sc "ふふ…ボクだってやられてばっかりじゃあないからな。"
    sc "常々言ってるけど、あまり外を出歩いちゃ駄目だぞ。誰かに見られちゃうだろう。"
    show SCG_06 11 with fastdissolve
    show SCG_06 at bounce
    hk_b "君があんまりにも！遅すぎるから暇で暇でなぁ。"
    hk_b "どっかで転んでどんぐりにでもなったのではないかと心配したぞ？"
    sc "…今日は残業もなかったから普段より早く来たんだけど？"
    show SCG_06 0 with fastdissolve
    hk_b "ん…？そうか…？{w}今月はまた一段と一日が短く感じるな。"
    stop music fadeout 2
    hide SCG_06 0 with dissolve
    hide screen textbox with dissolve
    play sound "audio/se/door close.ogg"
    pause 1.0
    scene bg100_1 with dissolve
    call place100
    pause 1.0
    show screen textbox with dissolve
    play music "audio/bgm/daily.ogg" fadein 2.0
    nar "礼拝堂には見覚えのある表紙の本が置いてある。"
    nar "ハクはボクの反応が見たいのか、いつもここに何かを置いているのだが、これもまた反応に困る。"
    show SCG_06 7 with dissolve
    show SCG_06 at bounce
    hk_b "キャッ！{w}レディの日記を盗み見るなんて、シーキュレット様のエッチ～"
    hk_b "行政府にチクって貴方がドスケベだと訴えてやりますわ～"
    sc "あ…どうりでよく見ると思った。キミの机の上に置いてあったあれだね。"
    show SCG_06 1 with fastdissolve
    hk_b "そうさ、「わたくし」との交換日記だな。"
    show SCG_06 9 with fastdissolve
    hk_b "昏睡状態で書き下ろした文章ほど面白いものがこの世にあるだろうかね？"
    hk_b "ヘタクソな聖書かラブレターみたいでな。"
    sc "ボクに見せようとわざわざ持ってきたのかい？"
    show SCG_06 0 with fastdissolve
    hk_b "いや…処分しようと思って持ってきた。"
    hk_b "面白くはあったが、この世に残していい物ではなくてな。{w}丁度使い切ったところでもあったし。"
    sc "ふぅん…"
    show SCG_06 11 with fastdissolve
    hk_b "読まないのか？"
    sc "他人の秘密を暴く趣味はないよ…"
    hide SCG_06 with dissolve
    nar "そして読みたくもない。"
    nar "誰もが酒や薬に酔った時に記憶が断ち切れてしまうように、ハクは「彼女」になっている時の記憶がない。"
    nar "彼女は単なる外面でなく、ハクが「完璧なる正義の使徒」として残酷であれと追い立てられた姿だ。"
    nar "この日記がそういう状態で書かれた物なら、知りたくもない情報で一杯なんだろう。{w}父に関する話も。"
    show SCG_06 1 with dissolve
    hk_b "今日は何をしていたんだ？"
    sc "書類の受け渡しの件でグレーテ補佐教に会って来たよ。{w}キミの話をしてた…"
    show SCG_06 5 with fastdissolve
    show SCG_06 at bounce
    hk_b "な！{w}せ、せ、せ先生は何と仰って…？？"
    sc "…キミのことが心配なんだって。{w}それだけです。"
    play sound "audio/se/ding.ogg"
    show SCG_06 7 with fastdissolve
    nar "たったそれだけなのに、ハクは上機嫌のようだ。"
    nar "彼女の生はボクよりも長く、ボクはその一部にはなれないだろうが、"
    nar "とにかくハクの周りに彼女のことを心配する人がいるってことは嬉しい。"
    sc "保健部主教様も同じ事言ってたよ。"
    show SCG_06 13 with fastdissolve
    hk_b "…せっかく美少女の話でいい気分だっていうのに、オッサンの話をするなよ。"
    nar "しかし本人がこんな態度では、グレゴール主教も大変なんだろう…"
    show SCG_06 1 with fastdissolve
    hk_b "オッサンはどうであれ、先生がそんなことを…"













    $ show_say_ex()
    show SCG_06 10 with fastdissolve
    $ hide_say_ex()





    extend "フフ、先生が…ふふふ！"
    show SCG_06 9 with fastdissolve
    hk_b "先生はホント、心の美しい御方なもんだ。"
    hk_b "三つ編みの授ける恩賜にタレ目が共にあらんことを、ナントカカントカアーメン。"
    sc "そういや、最近は昼にも起きてるね。"
    show SCG_06 1 with fastdissolve
    hk_b "良く解ったな。どうせ昼夜構わず明るいもんだ、こういうのも悪くはない。"
    hk_b "魔導部のジジイの小言を黙って聞いてるのも癪だし。{w}最近は大人しくしていると気分が優れないのでな。"
    sc "新しい彼女にフラれでもしたの？"
    show SCG_06 0 with fastdissolve
    hk_b "チッ、何を言う？{w}そういうのは教育院と共に卒業したんだって。"
    show SCG_06 9 with fastdissolve
    hk_b "言ったろう…私には君しかいないのだ、シーキュレット。"
    nar "ハクはやっとの思いで片目を瞑り、指先で唇を押してはちゅっと音を立てる。"
    nar "ウィンクもロクに出来ない癖にいっつもこうだ。"
    show SCG_06 10 with fastdissolve
    hk_b "キュ～～レット様の冷ややかな反応はいつだって私を興奮させてくれるな…"
    sc "キミのサイテーなジョークはいつだってボクをげんなりさせるけどね。"
    show SCG_06 at bounce
    hk_b "またまたぁ、実は嬉しいクセにぃ～"
    sc "うるさいうるさい……{w}魔導部の主教は今でもキミに突っかかってくるのかい？"
    show SCG_06 12 with fastdissolve
    hk_b "ド偉いエリィ主教様は未だに私の事を直属の部下か赤ん坊として見てらっしゃるようでな。"
    hk_b "どうにかしてあのハゲ頭をぶったたく方法はないんかね？"
    sc "一度持った印象は変えにくいってことじゃない。"
    hk_b "それもそうか、私の乳歯が抜ける頃彼と初めて会ったからな。{w}あの頃はまあデカい人だったもんで…"
    show SCG_06 0 with fastdissolve
    stop music fadeout 2
    hk_b "他は知らんな。{w}私はエルジェーベト主教より彼の弟ともっと仲が良かったのだよ。"
    sc "アルネ様のお父さんと？"
    play music "audio/bgm/golden haku.ogg" fadein 2
    hk_b "お父様の知り合いでもあったし。{w}処理班に薔薇園があるだろう？"
    hk_b "元よりあれはエリィ主教の物だったらしくてな、良くそこで三人揃ってお茶会をしてらっしゃったのさ。"
    show SCG_06 12 with fastdissolve
    hk_b "彼は私の様なじゃじゃ馬にも親切な男だった。{w}だがエリィ様は…何故毎回いらしてたんだろうか。"
    hk_b "いっつも無口でお茶ばかり飲んでらっしゃったのだよ。"
    hk_b "だがたまに弟の手に私の為のプレゼントや菓子を握らせていたりしたな。"
    hk_b "いざ顔を合わせると一言も喋ってはくれなかったが…"
    hk_b "もしかしたらあれは彼なりの可愛がり方だったのかも知れんな。"
    sc "へぇ。"
    show SCG_06 0 with fastdissolve
    hk_b "まあそれも束の間だったが。{w}父様はあまりよく思っていなかったのだ。"
    hk_b "私が庭園に遊びに行ったり、菓子を頂いてたのをな。"
    show SCG_06 13 with fastdissolve
    hk_b "ともかくエリィ様はあの頃がよっぽどマシだったよ、年寄りになってから口が達者になりおって…"
    sc "そういや、最近部室に来てたって聞いたけど。"
    show SCG_06 10 with fastdissolve
    show SCG_06 at bounce
    hk_b "でもあの時は私が一発かましてやったんだぜ！"
    show SCG_06 1 with fastdissolve
    hk_b "しょうがない事だとは言え、一時は自分の管下で世話をしていたからか随分お節介になってな。"
    hk_b "頼んでもないのにありがた迷惑なこった、タヌキジジイが。"
    show SCG_06 12 with fastdissolve
    hk_b "プレゼントでご機嫌になるような歳はもう過ぎてるというのに。"
    nar "言葉とは裏腹に彼らとの思い出を語るハクは随分楽しそうだ。"
    nar "こんな話を聞いていると、ボクが必要以上の情報を聞いていると思ってしまう。"
    show SCG_06 0 with fastdissolve
    hk_b "しかし…全く尊敬できないとまでは言えない人ではあるな。{w}喋り方も雰囲気作りには丁度いい。"
    sc "最近は全く使わなくなったね。{w}その…難しい古い喋り方。"
    hk_b "そりゃあアレはああいう遊びだったからな……"
    show SCG_06 11 with fastdissolve
    hk_b "話し相手が聞き取れないんじゃあ、わざわざ台本を練るまでもない。"
    sc "あっそ、ごめんなさいね…"
    show SCG_06 12 with fastdissolve
    hk_b "それに、あれだ…子供の教育も優れていたな。"
    hk_b "特に長女はパッと見ただけでも「魔導のモノ」って感じがするだろう。"
    hk_b "私はあの子の父の葬式の時に彼女を最後に見たのだが、今は立派なお嬢様ではないか…"
    show SCG_06 1 with fastdissolve
    hk_b "あの魔導師のお嬢ちゃん、幼い頃はとんだ泣き虫だったんだぞ。"
    show SCG_06 at bounce
    hk_b "ハハ！もうその事実を知る者も少ないのか。そう思うと光栄だな。"
    sc "直接話してみた事はあるのかい？"
    show SCG_06 12 with fastdissolve
    hk_b "ん、いや…直接は…ない。{w}だが長らく見ていればそれ相応の情も湧くものよ。"
    hk_b "例えそれが一方的な物だとしてもな…{w}魔導師のお坊ちゃまの方も、結構話の通じる奴だろう。"
    hk_b "ちゃんと顔を合わせる日が来たら面白くなりそうだ。{w}そんな日が来たならばな。"
    sc "…まるでそんな日は来ないみたいに言うじゃないか。"
    hk_b "まあ…"
    nar "彼女が生きてきた人生はボクのよりもずっと長くて、そこにボクの居場所なんてない。"
    nar "ボクがその事実に要らぬ感情を持つこととは別に、彼女の隣には人が要るべきだと思う。"
    stop music fadeout 2
    nar "会話を好むハクなら、向かい合う人がボクだけであるこの状況に飽きている筈だから。"
    play music "audio/bgm/daily.ogg" fadein 2.0
    show SCG_06 0 with fastdissolve
    hk_b "…どうした？シーキュレット。{w}昼飯を抜いた様な顔をしよって。"
    sc "昼飯を実際抜いてるからじゃないかな？誰かさんが戦闘基地に置いといたおやつを食べちゃってね。"
    show SCG_06 11 with fastdissolve
    play sound "audio/se/ding.ogg"
    hk_b "そんなあ、誰がそんなことを…"
    sc "そうだね、誰がこんなことを…"
    show SCG_06 at bounce
    hk_b "そこまで睨むことか？{w}よくよく考えてみろ、シーキュレット。例えば…"
    show SCG_06 12 with fastdissolve
    hk_b "その…おやつが誰のものか…{w}とか…"
    sc "ボクのですよね…"
    show SCG_06 at huruhuru
    hk_b "そう…ですね…{w}…しかし君は……{w}誰のものでしょうｋ{nw}"
    show SCG_06 7 with fastdissolve
    play sound "audio/se/hit.ogg"
    hk_b "いや～～ん、暴力反対ですぅ～～～～" with sshake
    hide SCG_06 with dissolve
    nar "不自然に話題が変わる。"
    nar "ハクは話題に対する線引きをハッキリと強調する癖があって、ボクがその線を越える事はない。"
    nar "ボクらが互いを話し相手としているのは他に話す相手もいないからだ。"
    nar "だから「どうしてボクにこんな話をしてくれるんだろう」などといった疑問だったり、"
    nar "勘違いはタブーとされている。{w}理由のない行為に理屈を求めても仕方ない。"
    show SCG_06 11 with dissolve
    hk_b "来年にはその尖った性格をどうにか出来ると良いがな。"
    sc "なんで来年の事を今から考えるんだい？{w}まだ夏だろう。"
    hk_b "そりゃあ君が春にして既に聖夜祭を待ち望んでいることと同じさ。"
    show SCG_06 9 with fastdissolve
    sc "聖夜祭はただ正式補佐教になるという事だけではないだろう？"
    hk_b "君は罪人である以上それ相応に償わないといけないだろうが、その後は自由だというこった。"
    hk_b "堂々と成人式を挙げる事になるだろうな。"
    sc "シーキュレットという名の「男」は既に成人式は終わったけど？"
    show SCG_06 1 with fastdissolve
    hk_b "それは「君」ではないだろう。{w}新しい服を貰って、新しく女性としての人生を生きてもいいという意味だ。"
    sc "うっ………わ。" with sshake
    show SCG_06 0 with fastdissolve
    hk_b "やっぱりな、考えてもみなかったみたいな反応だな。"
    sc "キミがボクに何かしらの役割を与えてくれるなら、ボクはキミの部下として最大限期待に応えるだろうけど……"
    sc "そればかりは分からないな。そうするにはあまりにも長く人を騙し過ぎた。"
    hk_b "今は仕方なく秘密を重ねてはいるが、罪は重ねてはならない。"
    hk_b "キミは初めて会ったあの時から顔つきが変わってきている…{w}男として生涯過ごすわけにはいかないだろう？"
    sc "…そんなのわかってるさ。でももう遅い気もするんだ。{w}問題はボクを信じてくれた人まで欺いた事なんだよ…"
    show SCG_06 1 with fastdissolve
    hk_b "やはり何かあったのだな。"
    nar "さっきから変なことを言っていると思ってはいたが、探りを入れていたのか。"
    nar "もう過ぎたことだし、できれば話したくないのに…"
    hide screen textbox with dissolve

    menu:
        "正直に話す":
            show screen textbox with dissolve
            sc "[na]の話だよ。知っているんだろう…"
            sc "ボクは彼を上手く騙せていると思っていたんだけれど、勘違いだったんだ。"
            sc "アイツはただボクがいつかは真実を話してくれると信じて待っていた、"
            sc "だから最後まで隠してきたボクを裏切り者だと思ってる。"
            sc "アイツはボクに秘密を打ち明けてくれたのに…"
            show SCG_06 0 with fastdissolve
            hk_b "君の悪いクセは許されないと思いこんで行動してしまうことだ。{w}だから昨日はあんなに顔が汚れていたのだな。"
            sc "そう、彼を裏切った罪を償うために、相応の罰を受けなければならなかったから。"
            sc "なのにアイツ、まだずっと怒ってるんだ…"
            nar "ただでさえボクはキミのことで十分頭が痛いのに…"
            sc "だから罪を償ったからと言って、君の言う通り自由になれるとは…限らないかもしれない。"
            show SCG_06 2 with fastdissolve
            hk_b "まさかそれが君の罪の重さだと思っているのではあるまいな？"
            hk_b "いいや違う。{w}君は何故常に自身のせいだと決めつけてしまう？"
            show SCG_06 0 with fastdissolve
            hk_b "確かに君は彼を騙し、信頼を裏切ったさ。それは確かに君の罪。"
            hk_b "しかしそこに合理的な理由があるならば、君は正しい事をしたのであって悪行をした訳ではないのだぞ。"
            sc "…彼がボクを信じてくれていたように、ボクも彼の事を信じてあげればよかったのかな？"
            hk_b "もしそうだったとてそれを今更考えてどうするつもりだ。"
            show SCG_06 1 with fastdissolve
            hk_b "君の意志に価値があると言ったのは他でもない君なんだぞ。{w}その決断を後悔するなよ。"
            sc "うーん……昨日聞いておくべきだったな、これ…"
            hk_b "そうじゃなくとも丁度いつ吐くだろうかと思ってたところでな。"
            show SCG_06 10 with fastdissolve
            hk_b "君のその重ったい口が開くのを待ってた人はそいつだけじゃないんだぞ？{w}罪人はおでこを出せよ～"
            sc "うっ、やめてよ……"
            hide SCG_06 with dissolve
            hide screen textbox with dissolve
            $ love_hkb = True
        "違う話題に切り替える":

            show screen textbox with dissolve
            sc "…キミがさっき言ってた魔導部の姉弟の事もそうだし、ラヴィとか……"
            sc "ボクに親切にしてくれる人が居るんだから、真実を明かした時態度が変わってしまったら嫌だろう。"
            show SCG_06 2 with fastdissolve
            hk_b "君の狭い人間関係の内じゃあ大丈夫そうだがな。"
            sc "あと、その…処理班の司祭とか。"
            show SCG_06 11 with fastdissolve
            hk_b "何時からそんなどうでもいいことを気にするようになったんだ？"
            sc "とにかく、何でもかんでもいいように受け取ってもらえるかわからないって話だよ…"
            sc "キミはそう思った事は無いのかい？"
            show SCG_06 12 with fastdissolve
            hk_b "ふーむ…いや、私にもあるさ。{w}一応秘密を背負って生きる身なんだし…"
            show SCG_06 0 with fastdissolve
            hk_b "しかしな、シーキュレット。"
            hk_b "人を騙すのは確かに罪だが、君には相応の理由と確固たる目標というものがあるだろう。"
            hk_b "罪悪感によってその決断を後悔するのは逆に彼らに対して失礼だと私は思うのだよ…"
            hk_b "自分のやっている事に自信を持ってくれ。{w}何故そう出来ないんだ？"
            sc "さあね…多分ボクがキミほど強くないからかも。"
            sc "ボクは勿論自分の目標は果たしたいし、間違った事とは思ってないけど…"
            sc "でも…"
            show SCG_06 1 with fastdissolve
            hk_b "信じる心が足りてないのだな。{w}良いだろう…なら私から言ってやろうではないか。"
            hk_b "君は正しい事をしている。だからキミのやるべき事を確と成し遂げればいい。"
            hk_b "私は君なら出来ると信じているぞ。"
            sc "……うん。"
            hide SCG_06 with dissolve
            hide screen textbox with dissolve
            $ love_hkb = False
    pause 1
    show screen textbox with dissolve
    nar "話しているうちに、さっきの気まずさは消えていた。"
    nar "ハクの言葉は大袈裟でもなんでもなく、本当にそうなのだろうと思う。"
    nar "偶然転がり込んできた幸運の前で、ボクの真っ黒い欲望と不遇な人生なんてくだらないもんだ。"
    nar "そしてその中から生まれる苦痛は睡眠と食事、少しの会話ですぐ癒されるのに、何事も複雑に考え過ぎだ。"
    sc "ハク……ありがとう。"
    nar "ふと最近しっかりと伝えてなかったと思い、口に出した。"
    nar "横目で見たハクは訳が分からないというように首を傾げている。だからボクもそっぽを向いてしまった。"
    sc "き…聞こえなかったなら別にいい…！" with sshake
    show SCG_06 10 with dissolve
    hk_b "ハハハ！面白い奴め。{w}わかったわかった、私もありがとう。"
    hide SCG_06 with dissolve
    nar "ハクは微笑みながら言ってくれたが、ボクは彼女の言葉に秘められた意味が分からない。"
    nar "助けられたのはボクなのに、何が「ありがとう」なんだろう？"
    nar "ひとつだけ確かな事があるとするなら、ハクは先ほどより機嫌がよさそうだという事。"
    nar "どうやら彼女もボクと同じく心に秘めていた事を打ち明けてくれたようだ。"
    if love_hkb == False:
        call hkb_fail
    else:
        sc "…また明日もここで会うんだよね？"
        show SCG_06 1 with dissolve
        stop music fadeout 2
        $ _skipping = False
        hk_b "勿論、君と話がしたいからな。"
        hide SCG_06 with dissolve
        hide screen textbox with dissolve
        $ meet_hkb = True
    stop music fadeout 2
    hide SCG_06 with dissolve
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
    jump day9_sc
    return

label day9_hk:
    hide screen textbox with dissolve
    pause 3
    menu:
        "眠る":
            jump day9_neru
        "眠らない":
            show screen textbox with dissolve
            nar "…全く眠れない。"
            hide screen textbox with dissolve
            pause 3
            menu:
                "眠る":
                    jump day9_neru
                "眠らない":
                    show screen textbox with dissolve
                    nar "機会があればアルネにもう一度謝ろう。それでいい。"
                    hide screen textbox with dissolve
                    pause 3
                    menu:
                        "眠る":
                            call day9_neru
                        "眠らない":
                            show screen textbox with dissolve
                            nar "俺の手で振るう暴力を罪だと思ってはいけない。そうやって自ら生み出した感情に溺れて苦しむことこそが悪魔の狙いだ。"
                            nar "悪魔を罰したことが何故罪となる。これは神を信仰するものとして当然の行為だ。"
                            hide screen textbox with dissolve
                            pause 3
                            menu:
                                "眠る":
                                    call day9_neru
                                "眠らない":
                                    show screen textbox with dissolve
                                    nar "彼はこれからも俺を色んな誘惑で引き摺り落とそうとするだろうが、俺は今の俺を保つべきだ。よくやっているんだ、俺は。"
                                    hide screen textbox with dissolve
                                    pause 3                                
                                    menu:
                                        "眠る":
                                            call day9_neru
                                        "眠らない":
                                            show screen textbox with dissolve
                                            nar "気持ち悪い。彼は今日俺の視界に現れなかった。"
                                            nar "なのに俺は朝から晩までこんな考えでずっと苦しんでいるなんて、一体どこで間違えてしまったんだろう。"
                                            hide screen textbox with dissolve
                                            $ save_name = "day 9, 夜, 楽園"
                                            pause 3
    play music "audio/SE/prologue wind.ogg" fadein 2.0
    hide screen textbox with dissolve
    scene black with dissolve
    pause 1.0
    show screen textbox with dissolve
    nar "今日礼拝堂にハクがいなかったらどうしよう。{w}ふとそんな考えが過る。"
    nar "そんなことはないとは思うのだが、それでも不安になってしまうのだ。"
    nar "どれだけ秘密を共有しているとしても、ハクはボクなんかじゃ到底近付けない人だ。"
    nar "ボクらが他愛のない話を交わすのも夜の一時だけ、昼は主教とその部下としてただ黙々と働くだけだ。"
    hide screen textbox with dissolve
    pause 1.0
    scene bg101_1 with dissolve
    call place101
    pause 1.0
    show screen textbox with dissolve
    nar "そんなボクの不安に拍車を掛けるように、いつもの場所にハクの姿が見えない。"
    nar "暗い森路、木間の陰を調べる。彼女はわざと光を避けるように、いつも陰を探す。"
    nar "ボクは彼女に闇は似合わないと思っているが、彼女はそう思っていないようだ。"
    stop music fadeout 2
    nar "ハクはそこにいてもまるでいない人のようだった…"
    hide screen textbox with dissolve
    pause 1.0
    show SCG_06 10
    show SCG_06 at bounce
    show screen textbox
    play sound "audio/se/hit.ogg"
    hk_b "ばぁ！" with sshake
    play sound "audio/se/hit.ogg"
    sc "うわぁっ……？！" with sshake
    play music "audio/bgm/daily.ogg" fadein 2.0
    hk_b "フフフ、君のアドバイス通り今日は別のところに隠れていたのさ。"
    hk_b "カッコつけてた割には全く探せなかった様だがな。"
    show SCG_06 8 with fastdissolve
    hk_b "とにもかくにも君は遅すぎる。{w}暇すぎて死ぬかと思ったんだぞ！"
    sc "いや…{w}本当に死にそうじゃない？なんて様なんだよ、ハク…"
    hide SCG_06 with dissolve
    nar "突然現れたハクは血を流している。{w}腹、いや、正確に言えば脇腹から新鮮な血をぼたぼたと垂れ流している。"
    nar "思ってもみないところから急に現れたことでも十分驚いたが、飛び出してきた本人がこんな姿なら尚更だ。"
    show SCG_06 11 with dissolve
    hk_b "フフン…主教ともあらば色んな事が起こるものよ。"
    show SCG_06 10 with fastdissolve
    show SCG_06 at bounce
    hk_b "これくらいで死ぬ訳でもないんだし、まあ気にするな！ハッハッハ！"
    nar "昨日洗濯したばかりの白い服は赤く、黒い外衣は泥色になっていく。"
    nar "最初は血の気が引いたが、今血を流している肝心のハクが、"
    nar "とてものんきなことを言いつつ笑っているから段々冷静になってきた。"
    stop music
    play sound "audio/se/door close.ogg"
    show SCG_06 5 with fastdissolve
    nar "ボクはすぐに礼拝堂の扉を開いた。" with sshake
    nar "元々重い扉は大きな音を響かせ開くと、そこから吹いてきた風がハクの髪を靡かせる。"
    nar "一瞬で彼女の笑い声が止まった。"
    hide SCG_06 with dissolve
    nar "ハクの驚いた顔が段々不満げになり、大人しくボクに付いて中に入ってくる。"
    hide screen textbox with dissolve
    scene bg100_1 with slowdissolve
    call place100
    pause 1.0
    show screen textbox with dissolve
    show SCG_06 2 with dissolve
    hk_b "尻尾バンバンする仔猫でもあるまいし、怒る度にそうやってガンガン音を鳴らすなよ。"
    sc "ならボクが怒る様な事をしなきゃいいだろ。"
    hide SCG_06 with dissolve
    nar "彼女の表情を窺わずに、床に膝をついて椅子の下から救急箱を持ち出した。"
    nar "物は持ってきた以上必ず一度くらいは使いどころができる。"
    nar "そんなんだから部外者を更に警戒せざるを得ないんだ。"
    sc "治療するから脱いで。"
    show SCG_06 5 with dissolve
    show SCG_06 at bounce
    hk_b "今？{w}マジ？！"
    sc "どうせ見る人もいないだろう、いいじゃん。"
    show SCG_06 0 with fastdissolve
    hk_b "そうか…？{w}まあそうだな…毎回世話になるな。"
    play sound "audio/se/luggage down.ogg"
    nar "ハクは腰の革帯を外そうとしていたが、ぎこちなく止まる。"
    nar "ボクは怪訝に思い首を傾げる。{w}彼女の真似をするつもりではなかったが、固い首から骨の鳴る音がした。"
    show SCG_06 13 with fastdissolve
    hk_b "こ…これはどうやって外すんだ。"
    sc "はぁ…毎朝説明してるのに。"
    show SCG_06 0 with fastdissolve
    hk_b "しょうがないだろう？「私」はこんなひらひらした服なんぞ着ないんだから。"
    hide SCG_06 with dissolve
    hide screen textbox with dissolve
    play sound "audio/se/r18 2.ogg"
    scene black with dissolve
    pause 1.0
    show screen nvlbox with dissolve
    nvl clear
    "\n やむを得なく彼女の後ろに回り、手探りで背中のチャックを探す。あくまでも普段通り。"
    et "ボクは毎朝誠実に主教の身支度を手伝っていた。{w}厚い上着を脱がし、シャツのボタンを外しては、白い髪を掻き集め、治療の邪魔にならないように束ねて避ける。"
    nvl clear
    hide screen nvlbox with dissolve
    show cghk02 with slowdissolve
    pause 2
    show screen nvlbox with dissolve
    play music "audio/bgm/train meet.ogg" fadein 2.0
    "\n 浄化部で長い髪を管理するなんてそう簡単でない。髪の長さを見れば自分にどれだけ気を配っているか、その自己愛が分かる筈だが、残念ながらハクはそういうことに興味がない。"
    "ボクは髪を切りながらそういうことも同時に切り捨てた。{w}ボクは欲張りだから、未練ができる前に断ち切った方が気が楽だった。"
    "彼女の美しい髪を保つことだけに集中したかったのだ。人々が髪の毛一本だけを見ても彼女の自己愛がすぐ分かるように。"
    et "服を脱がせると、彼女の白い背中が現れる。{w}そこの無数の傷跡も。"
    nvl clear
    "\n 夜の空気は冷たいが、ハクは寒さに震えてはいない。どくどくと血が流れる傷に直接消毒薬が触れても微動だにしない。{w}震えているのはボクの手だけだ。"
    et "実際はこんな人なのに、未だ多くの関心とデマが彼女に付きまとう。{w}きっと彼女の目立つ外見のせいだろう。"
    nvl clear
    "\n 鮮明に浮き出る脊椎と肩甲骨、真っ白い肌…ハクは美しい。{w}その美しさを言葉で表現しても何の意味があるんだろう。"
    "彼女を初めて見た瞬間、ボクは世の中にこんなにも美しい人がいるのかと感動した。{w}不自然だと感じられるほどに。"
    "余裕のある振る舞い、礼儀を忘れない丁寧な態度を含めて、その美しさは「浄化部」という清廉な名を被ったゴミ捨て場の主人だけで済ませるにはもったいないように思えた。"
    et "ボクはそれがこの傷を隠す為だとは知っていても、これが何時からのものかは知らない。"
    nvl clear
    "\n 「手が冷たくなくて丁度いいな。」"
    "「ボクの手が？別にそうでもないけど。」"
    "「少なくとも、私に触れる際は常に温かいぞ。」"
    et "「普通だよ、ボクの体は。」{w}キミが冷たいんだよ、失礼な事を言うかの様に慎重に付け加えた。"
    "\n ボクの体は温くて、外の温度によってすぐ変わってしまう。"
    "彼女は…蒼白だ。"
    et "きっと服で包まれているのにいつも大理石のように冷たくて、ボクは彼女が寒さが苦手だと知っていても正反対に思ってしまう時がある。"
    stop music fadeout 2
    hide screen nvlbox with dissolve
    pause 2
    scene bg100_1 with slowdissolve
    pause 1.0
    show screen textbox with dissolve
    sc "そろそろどうしてこうなったか説明してもらっていい？"
    show SCG_06 0 with dissolve
    play music "audio/bgm/daily.ogg" fadein 2.0
    hk_b "あ、それが森に行く前、学術部のかしこちゃんに力場の情報の報告を貰ったんだが、"
    hk_b "そちらの主教様からのプレゼントだとお守りをくれたもんで。"
    show SCG_06 11 with fastdissolve
    hk_b "ここまでは良かったんだが、私がそれを持ってくるのをすっかり忘れちまってだな。"
    play sound "audio/se/ding.ogg"
    sc "すっかり？"
    hk_b "取りに戻るのも面倒で。"
    play sound "audio/se/ding.ogg"
    sc "面倒？"
    hk_b "だからフツーに森に行って…"
    play sound "audio/se/ding.ogg"
    sc "行って？"
    play sound "audio/se/hit.ogg"
    show SCG_06 13 with fastdissolve
    hk_b "おいおいおい、何をそんな一々聞き返す必要があるんだ？" with sshake
    show SCG_06 10 with fastdissolve
    show SCG_06 at bounce
    hk_b "そうして亡者を引き寄せてしまい、16対1で勝ち遂げてただ今戻りましたとさ～"
    hk_b "いやあ～武勇伝がまた一つ増えてしまった、"
    show char_hk_b onlayer screens at slowname
    image dayhk9_1 = Text("{k=1}いやあ～武勇伝がまた一つ増えてしまった、{/1}", size=36)
    if config.language == "English":
        image dayhk9_1_en = Text("{k=1}Whew! One more tale to add to the saga,{/1}", size=27)
        show dayhk9_1_en onlayer screens at slowsay
    elif config.language == "SimplifiedChinese":
        image dayhk9_1_en = Text("{k=1}哎呀～英勇事迹又多了一桩……{/1}", size=28)
        show dayhk9_1_en onlayer screens at slowsay
    elif config.language == "Korean":
        image dayhk9_1_en = Text("{k=1}이거 참, 갈수록 무용담이 늘어만 가는…{/1}", size=36)
        show dayhk9_1_en onlayer screens at slowsay
    else:
        show dayhk9_1 onlayer screens at slowsay
    show SCG_06 11 with fastdissolve
    hide dayhk9_1 onlayer screens
    hide dayhk9_1_en onlayer screens
    hide dayhk9_1_cn onlayer screens
    hide dayhk9_1_kr onlayer screens
    hide char_hk_b onlayer screens
    extend "な…"
    sc "キミのそういうとこホント嫌い。"
    show SCG_06 0 with fastdissolve
    hk_b "そういうとこ、とは？"
    sc "そういうとこだよ、そういうとこ。{w}大体なんで呼び出しの命令をくれないんだ？"
    sc "主教…特にキミは一人出歩くのは良くないってずっと言ってるだろ。"
    show SCG_06 12 with fastdissolve
    hk_b "あ～はいはい、わかったわかった。{w}じゃあ命令します。すりゃあいいのだろう？"
    sc "他の主教たちは言われなくてもやってんのに。"
    show SCG_06 0 with fastdissolve
    hk_b "怒りんぼをやめなさい。命令します。"
    play sound "audio/se/hit.ogg"
    sc "キミはともかく人の話を聞かないったらないからさあ！" with sshake
    play sound "audio/se/hit.ogg"
    show SCG_06 13 with fastdissolve
    hk_b "だから怒りんぼをやめなさい！命令だぞ！" with sshake
    hide SCG_06 with dissolve
    nar "こんな傷だらけの体でも、ボクはハクこそが誰よりも清廉な体を持っていると思う。"
    nar "何故ならハクは禍の影響を受けない人、神聖力のない無聖痕だからだ。"
    nar "時折、七才を過ぎても聖痕が現れないことがある。"
    nar "神聖力を持てなかった人間は禍に対抗できず若くして死ぬのが普通だった。"
    nar "ボクがハクを助けられる数少ない方法が正にこれだ。{w}力場を見て、彼女に注意を促すこと。"
    nar "しかしハクは生きている。足りていないまま完成され、無能な身体で主教の座を手に入れた。"
    nar "ボクはそんな彼女の為に、彼を傍に置き観察しようとしていた。彼の傷は聖痕の発現に間違いないと思ったから。"
    sc "はい、終わりです。" with sshake
    show SCG_06 5 with dissolve
    show SCG_06 at bounce
    hk_b "痛って！{w}患者をこんな風に扱っても良いのか？"
    sc "ヘンな事言ってるぐらいなんだしもう大丈夫かなって。{w}でも当分は安静にしてよね、ハク…"
    show SCG_06 12 with fastdissolve
    hk_b "……"
    nar "…返事がない。聞くつもりがないんだな。"
    sc "普段も学術部主教から贈り物を頂いてたりするのかい？"
    show SCG_06 0 with fastdissolve
    hk_b "ん？ああ、あの人はああいうのを好んでいてな…"
    hk_b "私が幼い頃にもたまに人形だったり、本だったりを渡してはそのままふらりと消えてしまっていた。"
    hk_b "あの人が嫌いって訳ではないのだが、私的に顔を合わせるのはどうもニガテなんだ。"
    nar "イヴリン・ヴィオレッタ。"
    nar "あの女性はハクのお父様が未だに学術部の主教だった頃の補佐教で、"
    nar "幼い彼女が神殿に住んでいた時面倒を見てくれた保母でもある。"
    nar "ハクは武勇談を含めた昔話を好むが、あれに関したことだけは話したくないようだ。"
    nar "だからボクが知っているのは、幼い頃のハクが彼らの無関心に疲れていたってことだけだ。"
    hk_b "彼女と話した事はあるか？"
    sc "そういやないね。"
    show SCG_06 12 with fastdissolve
    hk_b "イヴリン様はご自身を女性の象徴だと考えている。"
    hk_b "女性として生まれた以上、皆ご自身と同じ生き方をするのだと思ってるんだ。"
    hk_b "君もいつか女性としてあの女の前に立つときは気を付けるが良い。"
    nar "ここにボクしかいないってことは分かっている筈なのに、ハクは周りを気にしているように声を殺して言い出す。"
    sc "前もお香みたいなのを貰ってなかったっけ。"
    hk_b "あれは…私が毎晩寝付けないのを気遣って下さったようでな。"
    show SCG_06 0 with fastdissolve
    hk_b "一度たりとも言った事がないのに、一体どうやって知ったのかは解らんがな…"
    sc "でもキミの心配をしてくれるなんて、ありがたい事だね。"
    hk_b "それは私だってわかるさ。わかってる、けど…{w}解らんな。複雑だ…"
    sc "じゃあ…今日神殿でラヴィ以外で会った人はいるかい？"
    hk_b "うーむ、グレーテ先生くらいかな？"
    sc "良かったね。どんな話をしたんだい？"
    show SCG_06 12 with fastdissolve
    hk_b "ただの……仕事の話。"
    nar "背中のチャックを上げていて彼女の表情が窺えなかったが、"
    nar "ハクはチラっと見ただけで淡々としていることは分かる。"
    nar "いつもならグレーテ補佐教の名が出てくるだけで一際嬉しそうにしているのに、珍しい。"
    show SCG_06 0 with fastdissolve
    hk_b "そういう君は今日誰と会ったんだ？"
    sc "うーん…今日はボクも仕事ばっかりだったな。業務量は普段と同じ筈なのに、妙に一日が長く感じて…"
    show SCG_06 11 with fastdissolve
    hk_b "ヒマだったようだな？業務中にボーッとしてちゃあいけないな。"
    hk_b "君の考えることなんて部署の心配ぐらいだろうがな。"
    sc "主教がマトモに仕事をしてくれないからだろ。"
    hide SCG_06 with dissolve
    nar "思わず口に出してしまったが、直ぐに失言だと気づきハッと口を手で覆った。"
    nar "ハクは寧ろボクのミスを喜ぶように笑う。"
    show SCG_06 1 with dissolve
    hk_b "じゃあ無能な主教の代わりに、我らが補佐教様は何を考えていらっしゃったのか聞いてみようじゃないか。"
    nar "またこんな……答えなんて知っている癖に、わざとボクに言わせようとする堂々としたあの態度に狼狽えてしまう。"
    nar "ボクに悩みなんて…"
    hide screen textbox with dissolve
    menu:
        "ある":
            show screen textbox with dissolve
            play sound "audio/se/ding.ogg"
            sc "…実は新入りたちが心配でね。"
            hk_b "ほぉ。"
            sc "彼らは…まだ知らない事だって多いんだ。"
            sc "そのままにしておいたらまたこの前みたいな事が起こるかも知れないのに、[na]はボクに口すら聞いてくれないんだ。"
            sc "マヤ…あの子もボクの事を避けてるし。{w}まだ仕事にも慣れていないだろうに…"
            show SCG_06 11 with fastdissolve
            hk_b "だろうと思った。君もまあ面倒見がいいこった。"
            sc "彼らだけじゃない、前から考えてた事なんだ。{w}神殿は過酷だよ。処理班は尚更…"
            sc "ボクは運良く慣れる事が出来たけど、何も知らない子達が無理に連れてこられては"
            sc "狂ったり死んでいくのを見るのはボクの立場からすると好ましくないんだ…"
            sc "主教のキミにどう映ってるかは分からないけど…"
            show SCG_06 0 with fastdissolve
            hk_b "…いや、君の言っている事は一理ある。{w}私も一時期は同じことを考えていたものだ。"
            nar "俯いていた顔を上げる。ハクは先ほどまでの笑みを消し、重たい表情をしていた。"
            hk_b "冥土に足を踏み入れたその時から、その命は既に失ったも同然とは言うが…"
            hk_b "自分の目には生きている人間に見えるのに、そのままにしておく訳にはいかないだろう。"
            hk_b "誰もが救いを待ち、助けてくれるかもわからん神に祈りを捧げるなら、"
            hk_b "誰かしらはその願いを聞いてやらんと、なあ？{w}神でなくとも、ヒトとして…"
            nar "……"
            show SCG_06 12 with fastdissolve
            hk_b "…しかし誰もが夢が叶う瞬間を想像しながら死んでいく。"
            hk_b "淘汰されると決められた者共が淘汰されていくのがこの宗教が決めた方針ならば、"
            show SCG_06 0 with fastdissolve
            hk_b "我々はそれに従う他ないのだよ。"
            nar "ハクはまるで独り言のように言い、再びボクを見つめた。"
            nar "いつもは彼女がボクを励ますために言ってくれてたけど、今回ばかりは彼女が彼女自身を励ますために言っている様に感じた。"
            hide SCG_06 with dissolve
            $ love_hkb = True
        "ない":

            show screen textbox with dissolve
            sc "そんな…ないよ。なんで当然の様にあるって考えちゃうの？"
            show SCG_06 2 with fastdissolve
            hk_b "無いと？{w}それは妙だな。私は君があの二人を心配していると思っていたのだが。"
            sc "…何日も悩んだんだし、そろそろ割り切らなくちゃ。"
            sc "ボクが忙しいって分かっているだろう。もうボクはアレについては考えたくもないんだ。"
            show SCG_06 0 with fastdissolve
            hk_b "疲れている様だな。"
            sc "そうであってほしいのかい？"
            hk_b "いや…私も近頃人間関係について悩んでいたものでな。{w}そこで君の意見も聞きたいと思って。"
            nar "言っている割には、ハクはそれに関して話す気はなさそうだ。ボクと同じく。"
            nar "相談はしないとしても、共感もしくは励ましが欲しかったのかもしれない。"
            hide SCG_06 with dissolve
            $ love_hkb = False

    sc "たまに思うけど、キミって怖いもの知らずだよね…"
    show SCG_06 8 with dissolve
    hk_b "私が？ハハハ…違うな。{w}君なら分かっているだろう？"
    nar "ハクは呆れたように笑う。そうは言ったがボクも、勿論違うと知っている。{w}ハクが恐れているのが何なのかも。"
    nar "それでもそう言ってしまったのは、ハクがそう言われることを好んでいたからだ。"
    hk_b "私は多くを恐れている。{w}自分が恐れているのが何なのかを良く解っているのさ。例えばあまりに暗い場所や…"
    show SCG_06 12 with fastdissolve
    hk_b "犬や、お父様の命令だったりな。"
    sc "…ボク、あの人はあまり好きじゃない。キミがあの人を恐れているのなら尚更だよ。{w}不気味だろう。"
    show SCG_06 0 with fastdissolve
    hk_b "他人の父に対して冗談が過ぎるな。"
    sc "本気だよ。{w}もしボクが男だったなら……あっ。"
    play sound "audio/se/ding.ogg"
    hk_b "……"
    sc "……"
    play sound "audio/se/hit.ogg"
    show SCG_06 10 with fastdissolve
    show SCG_06 at huruhuru
    hk_b "ぷふっ！君が男だったら？{w}どうするんだ？{w}ん～？" with sshake
    hk_b "ハハハ！お前なぁ、またその話か？本当に病んでしまったのではないのかね？{w}ハハハッ！"
    nar "チクショウ、そういう意味じゃなくて…{w}さっきから失言だらけだな。よりによってハクの前で！"
    show SCG_06 11 with fastdissolve
    hk_b "クックック……ほらみろ、君は私とは違って、自分が何を恐れているのかもわかっていないではないか。"
    show SCG_06 12 with fastdissolve
    hk_b "別に阿呆だと言いたい訳ではな…{w}うむ、まあ全くそうでは無いとは言えんがな。{w}逆に怖がりなのかもな。"
    nar "ボクはそれについて深く追求せず、ただ彼女を睨んだ。彼女が判断したボクの弱点なんて、聞きたくもない。"
    sc "ボクは少なくとも何かを恐いとは思わないよ。{w}常に死を覚悟しているのならば死なんて恐れるに足りないだろう？"
    sc "そういうものだよ。{w}その心構えすら出来ていない者のみが、何かを恐れるものさ。"
    show SCG_06 0 with fastdissolve
    hk_b "それは違うな。{w}それは自身の身や生涯に未練もないということではないか。"
    hk_b "君は正にその状態だ。そんなの死んでいるも同然だよ…"
    hk_b "だからといって君が実際死んでいる訳ではない。{w}何故なら君は死体とは違って常に不安がっているだろう。"
    hk_b "今みたいに心配もするし…昨日だって…"
    hide SCG_06 with dissolve
    nar "ハクはもう上機嫌になったのか、視線を宙に向け考え事に夢中だ。"
    nar "ハクがあんな表情だとどうしても不安になってしまう。"
    show SCG_06 11 with dissolve
    hk_b "君は死を恐れないと言ったが、どうしてそうと確信できる？"
    sc "馬鹿にするなよ、ハク。ボクも処理班の司祭である以上、命の危機くらい毎回のことさ。"
    show SCG_06 1 with fastdissolve
    hk_b "でもどうにかして生き延びているではないか。{w}なんなら一度死んでみるかね？"
    stop music fadeout 2
    sc "は？"
    hk_b "私が与えてやろう。"
    hide SCG_06 with dissolve
    nar "言葉とは裏腹に、ハクはいつも通りの笑みを浮かべたままナイフを持ち出した。"
    nar "ナイフ…{w}その正体は一目で分かったが、"
    nar "ボクはそれがどのように使われるか知らないかのようにただぼうっとしていた。"
    hk_b "じっとしていなさい。"
    play sound "audio/se/Heart.ogg"
    nar "低い声と共に、首元にナイフが近付けられる。脱力していた腹が硬くなっていくのを感じる。"
    nar "冷たい刃。{w}死刑囚と接するかのようなハクの冷たい声は、本能的に死を感じさせる。"
    nar "ボクはそれを恐れる必要がない。このとんでもない状況に慌てる必要もない。"
    play sound "audio/se/wake up.ogg"
    sc "……っ！" with sshake
    nar "なのに、ボクは後ろへ退いてしまった。{w}止まったような呼吸と、心臓が再び速くなっていく。"
    nar "ボクが詰まる息を吐き出すと、ハクはのんきに刃を触っていた。"
    sc "ハク！冗談が過ぎるよ…！" with sshake
    show SCG_06 11 with dissolve
    hk_b "冗談とわかっているくせにどうした？"
    hk_b "君だってわかっているだろう、私が果物の皮を剥く為に持ち歩くナイフ！{w}人間用じゃあないんだぞ。"
    play sound "audio/se/Heart.ogg"
    nar "彼女の言う通り、ボクはそのナイフが人の首を落とすには頼りないと知っている。"
    nar "彼女がいつものような戯れをしていることも、ボクが死ぬことはないという事実も知っていた。"
    nar "のに、目をぎゅっと閉じてしまう。"
    sc "一体何がしたいんだ、キミは。"
    show SCG_06 0 with fastdissolve
    hk_b "君に淘汰されないでいて欲しいんだよ。"
    hk_b "夢をみるのに資格など要らないとは言うが、目標を叶えるためには自身の弱さを知り尽くす必要があるのさ。"
    hk_b "それを乗り越えることが出来なければ、今までの新入りと同然で淘汰されて行くばかりだろう…"
    hk_b "君は自分を悲観するタイプではあるが、本当に知るべき欠点に関しては目を背ける傾向にある。"
    sc "…それが何になるって言うんだい？{w}神殿では自身の役割だけ知っていればいい。"
    sc "取り返しのつかない些細な問題をいつまでも抱えてるばかりじゃあ、仕事は誰がやってくれるんだ？"
    sc "ボクは明日も忙しいんだよ。{w}ボク……もう帰るから。"
    play sound "audio/se/luggage down.ogg"
    nar "慌てたように席を立った。驚いた心臓は未だにバクバクと音を鳴らしている。"
    if love_hkb == False:
        call hkb_fail
        hide screen textbox with dissolve
        scene black with dissolve
        pause 1
        play music "audio/bgm/dialogue.ogg" fadein 2.0
    else:
        show SCG_06 1 with fastdissolve
        hk_b "明日も来るのか？私は君に来て欲しいのだが。"
        sc "…心配しなくていいよ、ハク。{w}ボク別に怒ってないんだし。だからここに来ない理由はない。"
        hide SCG_06 with dissolve
        hide screen textbox with dissolve
        scene black with slowdissolve
        pause 1.0
        show screen textbox with dissolve
        play music "audio/bgm/dialogue.ogg" fadein 2.0
        nar "ハクの笑顔を見たくなくて、振り返ることもなく礼拝堂を出た。"
        nar "ハクの人をからかうような笑顔は、少なくとも上の者が下の者を見る時の顔ではなかった。"
        nar "それがボクを更に混乱させる。"
        nar "誰かに特別さを感じたって、それは勝手に押し付けているだけに過ぎない。"
        nar "人が必要としているのはいつも誰かでなく何かの役割で、その人が消えても代わりを探せば満たされるのだ。"
        nar "ボクはそう言い聞かせて、早く心臓が静まることを願った。"
        hide screen textbox with dissolve
        $ meet_hkb = True
    jump day9_hk_M

label day9_hk_M:
    nvl clear
    scene bg15_1 with slowdissolve
    call place15
    pause 1.0
    show screen textbox with dissolve
    sc "…？"
    nar "寮の入口に着くと、廊下の向こうから人影が見える。{w}その影はそのまま立ち止まって動かない。"
    play sound "audio/se/ding.ogg"
    sc "マヤ？"
    nar "そこには見慣れた顔がいた。{w}マヤはボクを見つけて喜んだかのように動き出したものの、表情は複雑だ。"
    show SCG_02 0 with dissolve
    my "キューくん、思ったより早かったんだね。{w}その、部屋に居なかったから…どこか行っちゃったのかなって。"
    show SCG_02 7 with fastdissolve
    my "顔合わせるのも久々だよね？{w}毎朝見てはいるんだけど…直接話すのは久々っていうか…"
    sc "ボクに言いたい事でもあるのかい？"
    nar "すぐ本題に入る。彼女もそれを求めていたようだったから。"
    my "あのね…わたし、ふたりがケンカしたことがどうしても気になって…"
    show SCG_02 8 with fastdissolve
    my "[na2]くんだって、キューくんに悪意はなかったって分かってるはずだよ。{w}ただ、頭に血が上っちゃって…"
    my "取り返しがつかなくなったって言えばいいのかな、その…つまりね、"
    show SCG_02 7 with fastdissolve
    my "キューくんがもう一度謝ってあげれば、ふたりは仲直り出来るんじゃないかなあって…"
    sc "……"
    show SCG_02 at huruhuru
    my "あ…も、もちろんキューくんにだけ非があるって言いたい訳じゃなくてね、"
    my "でもキューくんが先に言ってくれるならきっと[na2]くんも謝るだろうから、だから…！"
    sc "ごめん、マヤ。謝るのが遅くなって。"
    show SCG_02 0 with fastdissolve
    my "……"
    sc "キミにはずっと謝りたかったんだ。"
    sc "ボクにガッカリしちゃっただろうし、こんな事に巻き込まれて災難だったよね。{w}ごめんなさい。"
    sc "でも彼には謝らない。"
    show SCG_02 5 with fastdissolve
    my "ど、どうして…？"
    sc "謝る必要がないからさ。キミの気持ちは解るけど、もう遅いんだ。"
    sc "ここでボクが何をどうしたって解決できる事は無い。"
    stop music fadeout 1
    pause 1.0
    show SCG_02 2 with fastdissolve
    my "…じゃあわたしは？"
    play music "audio/bgm/grumble.ogg" fadein 5
    nar "彼女の顔を再び見た瞬間、これ以上隠し通せないということをもう一度実感した。"
    nar "もう何もかもが取り返しのつかない事になっていた。"
    my "ふたりが何で喧嘩しようが、わたしとは何の関係もないじゃない。"
    my "でもあの人がどれだけわたしの事をいじめてくるか分かる？"
    my "わたしがあなたたちふたりの間でどれだけ顔色を伺ってたのか分かる？！" with sshake
    sc "……"
    show SCG_02 3 with fastdissolve
    my "もっと…もっと考えてよ、わたしを…"
    my "見てないフリして置いてかないでよ！シーキュレットくんだってわたしが可哀想なんでしょ！！" with sshake
    sc "…もう帰って。明日遅刻したくないならね。"
    my "……"
    hide SCG_02 with dissolve
    nar "ボクはもうなに答えられなくて、話は終わったとマヤの横を通り過ぎる。"
    nar "そのまま進もうとしたが、すぐ振り向くこととなった。"
    "{nw}" with sshake
    nar "マヤはボクに飛び掛かって、聞いたことのない声で怒りを露わにしていた。"
    nar "噛み締めた歯の間から鋭い息が聞こえる。"
    nar "慌てて彼女の腕を掴んだボクは、荒々しくもがくマヤをやっとの思いで抑え込んだ。"
    play sound "audio/se/cup.ogg"
    nar "その瞬間、硬い何かが落ちたような気がした。"
    stop music fadeout 2
    sc "……"
    my "……"
    show SCG_02 7 with dissolve
    my "…キューくんはずっと、知ってたんだよね？"
    play music "audio/se/Heart.ogg"
    nar "マヤは俯いていたが、ボクはすぐに彼女が泣いていると気が付いた。"
    show SCG_02 3 with fastdissolve
    my "わたしだって知ってたもん…全部。{w}キューくんのことずっと見てきたんだから…"
    my "わたしだってそこまでバカじゃない、わたしだって全部知ってるんだよ！！" with sshake
    hide SCG_02 with dissolve
    play sound "audio/se/running.ogg"
    nar "彼女はボクを押し退けては暗い廊下を走っていった。"
    nar "その後ろ姿が転んでしまいそうに見えて不安で、しばらく見つめてから俯き。床には鋭利な錐が転がっている。"
    nar "ハクがボクにナイフを向けた時、ボクは未練に気付いた。"
    nar "ハクの為に[na]を引き留めていただなんて、そんなくだらない言い訳が事実な訳がない。"
    nar "本当は彼らとの時間が楽しくて、彼が魔導部に行って欲しくなかっただけだ。"
    nar "顔を見ることが減って、彼がもうボクを友達として見てくれなくなることが怖かったんだ。"
    sc "ボクだって…"
    stop music fadeout 2
    nar "知っていた。{w}ボクが彼らを傷付けた時、ボクも共に傷付いたことを。"
    nar "ハクはそれを乗り越えてこそ夢が叶えられると言っていたが、"
    $ _skipping = False
    nar "ボクは自らの惰弱さには勝てないってことを知っていた…"
    stop music fadeout 2
    hide SCG_06 with dissolve
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
    jump day10_sc
    return
    nvl clear

label day10_hk:
    $ save_name = "day 10, 夜, 楽園"
    hide screen textbox with dissolve
    scene bg06_1 with slowdissolve
    call place06
    pause 1.0
    show screen textbox with dissolve
    play music "audio/se/no more bell my buddy.ogg" fadein 5
    nar "目が覚めると病室だった。"
    nar "最後の記憶を辿ってみれば、風呂場の汚い風景が浮かぶ。{w}主人が帰ってくる前に掃除しておかないと。"
    nar "視線を移した所で[na]が眠っている。{w}声には出さなかったが、果物用ナイフを持っていたので随分驚いた。"
    nar "意識が戻ってきたと共に痛みが腹を押し潰す。慎重に手で触ると、やはり血が付く。"
    nar "ため息の代わりに息を吸った。いつかはこうなるとはわかっていたが、それがまさか今日だとは。"
    nar "しかし怯えている暇はない。幸い傍に司祭服が畳んで置いてある。"
    nar "ボクはてきぱきと病衣を脱ぎ捨て、本来の司祭の姿に戻った。"
    pl "…どこ行くんだ？"
    sc "うわっ…！" with sshake
    nar "今度は耐えられず声を出してしまった。"
    nar "ベッドのすぐ隣に座っている彼は、未だ半分夢の中なのかぼんやりした目で俺を見ている。"
    sc "…仕事。"
    nar "できる限り簡潔で明確な言葉で伝えた。"
    nar "[na]はボクの言っている事が分かったのか、彼はうつろに頷いた。{w}ボクはその前に近付く。"
    pl "その内死ぬぞ。"
    sc "死なないよ。"
    nar "まだそう命令されていないから。{w}彼の一言に、ボクも短く答えた。"
    nar "そして死体や子供を扱うように瞼に手をあて、うとうとと閉じては開いてを繰り返す瞼を完全に閉ざしてあげた。"
    nar "彼が静かになると部屋はいつもの静寂を取り戻す。"
    stop music fadeout 2
    hide screen textbox with dissolve
    pause 1
    scene black with slowdissolve
    pause 2.0
    show screen textbox with dissolve
    nar "風呂場の掃除はもうできている。"
    nar "正確に言えば床を水で流しただけだが、基本的な処理ができていたことに驚いた。"
    nar "ボクが湯船の掃除を終わらせても、ハクは部屋に来なかった。時間はもう三時を過ぎている。"
    nar "不安になってきた。"
    nar "ハクは稀に礼拝堂に来ることなくずっと神殿にいるときがある。{w}そんな夜は珍しいが、必ずある。"
    hide screen textbox with dissolve
    pause 1
    scene bg03_1 with dissolve
    call place03
    pause 1.0
    show screen textbox with dissolve
    nar "ボクは階段を上って、暗くなった床を踏んだ。{w}ここだけ日差しが届かない。"
    nar "ハクは暗くて寒い、狭い所に一人でいることが嫌いなのに。"
    nar "並んだ椅子、その内の一つに彼女が座っていた。"
    play music "audio/bgm/haku.ogg" fadein 3
    nar "ハクは普段口数が多い方だが、彼女が本来漂わせる空気はとても奇妙で、静かで、ボクまで息を殺してしまいそうになる。"
    sc "ハク、探したよ…何かあったのかい？"
    show SCG_06 0 with dissolve
    hk_b "……"
    hide SCG_06 0 with dissolve
    nar "反応を見せないハクを怪訝に思い、ボクは彼女の目の前で手を振った。" with sshake
    nar "彼女は視線だけを動かしてボクを見ては、バッと手首を掴む。"
    show SCG_06 2 with dissolve
    hk_b "君こそ何があった？血の匂いがするぞ。{w}怪我をしたのか？誰がやった。"
    nar "咄嗟に手を引こうとしたが、途中で止めた。{w}ここで慌てた方が逆に変に思われるだろうから。"
    sc "ただの怪我。仕事してるとよくある事だろ。"
    hk_b "ただの怪我ではなさそうだが？しかも君は仕事を上がってから随分時間が経っているではないか。"
    sc "離して。"
    show SCG_06 13 with fastdissolve
    hk_b "何故私に嘘を付く？{w}私を騙したいんだったらもう少し頭を捻れよ。"
    hk_b "それが出来ないならちゃんと口を開くんだな。{w}何処の誰に刺された？"
    nar "青く沈んだ目が瞬きもせずボクを睨む。{w}締めあげるような強さで手首を掴む彼女は、興奮を隠す気はなさそうだ。"
    hide SCG_06 0 with dissolve
    play sound "audio/se/slap.ogg"
    nar "ボクは結局その手を振り払ってしまう。"
    sc "やめてよ…！{w}ボクが何処でどう事故に遭おうが、明日ちゃんと出勤してれば何の問題もないんだろ？" with sshake
    show SCG_06 13 with dissolve
    hk_b "何だと？{w}君は、そんな事、本気で……"
    show SCG_06 0 with fastdissolve
    hk_b "いや、ハァ…もういい。"
    hide SCG_06 0 with dissolve
    nar "ハクは今にも怒り出すかのように言いつつも、すぐに諦めたように頷いた。"
    nar "強く締めつけられた手首がまだ痛い。"
    nar "顔色を伺いながら隣に座ると、眉間に手を当てた彼女はゆっくりとボクを見つめる。"
    show SCG_06 0 with dissolve
    hk_b "殴られっぱなしは良くない。なんなら殴った方がいいぞ、先手こそ必勝だからな。"
    sc "あぁ…はいはい。"
    nar "過程がどうであれ、彼女が諦めてくれたのは好都合だ。"
    nar "彼とボクの私的ないざこざに彼女を巻き込むわけにはいかないから。"
    sc "…香水の匂い。"
    show SCG_06 12 with fastdissolve
    hk_b "ヴィオレッタ、愛する女に似ているという理由で私のお父様が好んでいた花だな。"
    show SCG_06 0 with fastdissolve
    hk_b "私はこの匂いを嗅ぐと気分が悪くなる。"
    nar "無意識に撒いた香りに未練が垣間見える。"
    nar "ハクは「彼女」になりたがった。"
    nar "「無邪気で献身的、無垢で冷静、が愚昧で隙だらけの高貴なる女」に、お父様に愛でられる女に。"
    nar "昼の主教は彼女が長い時間望んでいた、幻想と懇望の集合体だった。"
    nar "だからこそボクは「彼女」と向き合いたくない。{w}誰が尊敬する人の弱点を見て楽しむことができるんだろう…"
    show SCG_06 12 with fastdissolve
    hk_b "私は君との接触は好きなんだがな、どうも好ましくはない…"
    hk_b "悪夢は私の気分を悪くさせてはいたが、同時に恐怖するまでのものではなかった。"
    nar "彼女が突然言い出した言葉がバラバラすぎて、ボクは彼女が酒や眠気、もしくは薬に酔っているのかと思った。"
    sc "ハク、今日はそろそろ戻って休んだ方が良さそうだね。"
    show SCG_06 0 with fastdissolve
    hk_b "私が邪魔なのか？"
    nar "その聞き慣れた言葉が続かないように、ボクは口を噤んで頭を振った。{w}幸い、ハクは何も言わずに目を閉じた。疲れた顔だ。"
    hk_b "ごめんな…隣にいてくれ、ただ…ただ、それだけでいいんだ。{w}話でもしようじゃないか。"
    nar "重たい沈黙が流れて、ハクは一歩遅れて何かを思い出したように懐を探った。"
    nar "そして取り出したのは小さな箱だ。"
    hk_b "プレゼントだ。開けてみるといい。"
    hide SCG_06 0 with dissolve
    nar "その中には金色の琥珀が入ったブローチがある。"
    nar "図々しい。こんな物、よくもボクへのプレゼントだなんて言い張るもんだ。"
    nar "凸凹のブローチの下にはハクが好む紅茶の葉が敷いてある。"
    nar "その仄かな香りに女性の優しい笑みを思い浮かべた。"
    nar "プレゼントとは、真心を込めれば受け取る者の顔が見えるんだな。"
    sc "なんでこんな物を…ボクに捨てるんだ？"
    show SCG_06 11 with dissolve
    hk_b "捨てる？プレゼントと言ったろう。{w}今日君の機嫌が悪いだろうという読みが当たってな。大事にしろよ。"
    nar "誰のセリフだっての。"
    sc "最近は保健部の主教とはお話してないのかい？"
    show SCG_06 12 with fastdissolve
    hk_b "まぁ…業務の話ぐらいだな。"
    nar "グレーテはボクとハクの事情を全部知っているたった一人の方だ。"
    nar "ボクにとっては神殿で働けるように助けてくれた恩人で、ハクにとっては主治医であり初恋の相手だ。"
    nar "ハクは教育院に入る前に敢えて州都を去ってグレーテの家で世話になっていた。{w}精神病を治療する為だった。"
    nar "その機会を作ってくれたのが今の保健部の主教たるグレゴール・コーニッシュで、"
    nar "彼は本当のお父様に代って幼い彼女を保護したという。"
    nar "だからか、彼らを相手する時のハクはまるで子供みたいだ。"
    show SCG_06 0 with fastdissolve
    hk_b "アレがもう3年前になるのか…私が主教として就任した頃先生に貰った物だ。"
    hk_b "イヴリン様が手工芸を学んでらっしゃる真っ最中だったものでな。"
    show SCG_06 12 with fastdissolve
    hk_b "仕事は私にとって重く、正直そぐわなかったが…それでも先生や主教様方や、まぁ、その…"
    show SCG_06 1 with fastdissolve
    hk_b "ちょっとぐらいはあのオッサンも応援してくれたもので、やってみようと思えるようになったのさ。"
    hk_b "その後も私が気を引き締めるように救ってくれた物だ。"
    sc "そんな物、どうしてボクに？"
    show SCG_06 0 with fastdissolve
    hk_b "置き場がなくてな。"
    nar "数日前は日記を捨てて、今は部屋の片付けまで。"
    nar "ボクとしては何故彼女が自分を成してきた物を一つずつ処分しているのか分からない。"
    sc "要らなくなった？"
    show SCG_06 8 with fastdissolve
    hk_b "ハハ…いっつもそうやって正論ばかり言うから殴られるんだぞ。"
    sc "……"
    hk_b "私が今まで感じてきた物事は全て錯覚だと気付いてしまってな。寧ろ真反対だったのさ。"
    nar "ボクは徐々に苛立ってきた。{w}彼女の中で何かが起きているような気がして。"
    nar "今日が過ぎてしまえばもう二度と彼女と話せない気がして。"
    show SCG_06 11 with fastdissolve
    hk_b "もっと高い物が好ましかったか？"
    sc "そんな訳。"
    hk_b "顔色が暗いからそんなモンかと。"
    sc "ボクの顔色なんていつも暗いだろ…"
    play sound "audio/se/luggage down.ogg"
    nar "その反応に腹が立ったのか、ハクはボクの頬を両手で挟み無理矢理顔を合わせる。"
    show SCG_06 1 with fastdissolve
    hk_b "顔に影が差すから目が紫色になっちゃったじゃあないか。太陽の色は何処にもない。"
    hk_b "光から逃げ更に奥地へ隠れる様に…{w}いいな、君らしい色だ。"
    sc "…タバコ臭いよ。"
    hide SCG_06 with dissolve
    nar "首を強く振って、彼女の手から逃れた。今日になってもう二回も彼女を拒んだ。"
    nar "ボクはこれが彼女が鬱である時の癖だと知っている。普通の人が人形や動物を抱き締めたくなるのと同じだ。"
    nar "でもよりによって今日だなんて。"
    nar "彼女は怒っていないような、だからといって平気でもないような顔をしている。"
    nar "それをじっと見ていられなかったボクは、一度突き放した手を握ってやることしかできなかった。"
    show SCG_06 11 with dissolve
    hk_b "昨日とは少し違うな。アンガーマネジメントが出来たのか？"
    sc "だから、昨日は怒ってたんじゃなくて……ただ怖かったんだよ。{w}ボクって受け入れるまでが長いだろう。"
    sc "だから…キミの言ってる事をそのまま受け入れていたら傷付いてしまいそうで、それが嫌だったんだ。"
    show SCG_06 1 with fastdissolve
    hk_b "君がちゃんと恐れを感じられるようになったとは嬉しい。"
    hk_b "誰もが恐れのない状態を勇敢と錯覚してしまうが、実はそれは単に愚かなだけなのだよ。"
    hk_b "君は自分の恐れる物を知ったから、これからは克服していけるだろう。"
    sc "…じゃあどうしても克服する自信がなかったら、その時はどうすればいいの？"
    show SCG_06 0 with fastdissolve
    hk_b "淘汰されるのさ。{w}昨日言った通りな。"
    nar "ボクが当然のように彼女からの助言や励ましを望んでこんなことを言ってしまうなんて、信じられない。"
    nar "そんな利己的な欲に傷付いていたなんて。"
    nar "震える息を吐きながら、弱く頷いた。{w}彼女はまるで気を遣うかのように別の話を始めた。"
    hk_b "…その時まで私は私自身が狂っているとは知らなかったのさ。{w}禍の影響だろうと思っていた。"
    show SCG_06 12 with fastdissolve
    hk_b "そんな私に彼女の知識がどれだけの助けとなったか。病気はヒトの手で治せるだろう？"
    hk_b "いつかこの病気が綺麗さっぱり治れば、お父様に誇らしい我が娘として認められる日が来るだろうと思っていた。"
    hk_b "そんな前向きな時期など一瞬だったがな。子供には思春期というものが来るだろう、丁度今の君の様に。"
    sc "……"
    show SCG_06 0 with fastdissolve
    hk_b "私の信ずる心全てが意味を成していないと解ったその瞬間から、私は何もかもが嫌になった。"
    hk_b "お父様に似た顔、愛する先生に迷惑を掛けてしまう状況、私に付いて回るであろう噂、宗教…"
    hk_b "何もかも全てが嫌になってしまって先生の家を離れ、男女問わず遊んでいた。"
    hk_b "あの頃は常に酒に浸った状態だったもので記憶はあまりないのだが、"
    hk_b "本当に辛くなった頃は常にグレッグ様に電話していた。それだけは覚えている。"
    hk_b "そうすると朝方でも仕事の途中でもすぐに駆け付けて慰めて下さったものだ…"
    show SCG_06 8 with fastdissolve
    hk_b "ハッ、何故そんな事をなされていたんだろうな。"
    hk_b "私なんかの、私みたいな女にどうしてそこまで良くしてくださったのか…"
    hide SCG_06 with dissolve
    nar "ハクは両手で目を塞ぎ俯いた。声は涙を堪えるように震えていく。"
    stop music fadeout 2
    nar "彼女を慰めようとした瞬間ハクは突然顔を上げ目を見開いた。{w}悲しみなんて全く感じられない表情で。"
    show SCG_06 0 with dissolve
    hk_b "しかしいつまでも過ぎた事を引き摺る訳にはいかん。そうだろう？"
    nar "そして真っ直ぐ、前向きな声で言い出した。"
    nar "ハクはいつも気分の浮き沈みが激しい方ではあったが、今日はそれより…"
    sc "ハク、本当にどうしちゃったんだ？{w}枢機卿から何か言われたのか…？"
    show SCG_06 2 with fastdissolve
    hk_b "宜しくないな、シーキュレット。遠い上司には様を付けて敬わんと。"
    sc "ボクはあの人はどうしても尊敬なんて出来ない。{w}人ってものは地位や名誉だけがすべてじゃないだろう。"
    show SCG_06 0 with fastdissolve
    hk_b "しかし世が彼を必要とするのならば、我々は彼を受け入れなければならないだろう？"
    hk_b "逆に私の些細な感情や決定が世に迷惑を掛けるのであらば、全てを諦めて、そこに順応するべきではないか？"
    play music "audio/se/Heart.ogg"
    sc "…一体何を言っているんだ。{w}本気か？"
    sc "キミ、変わっちゃったんだね…数日前までだってキミはそんな人じゃなかっただろう。"
    sc "いくら州都が宗教や序列なんかに押しつぶされようと、"
    sc "キミだけはキミ自身の信念を貫き通す正義の人間だったじゃあないか。"
    nar "徐々に声が震えてきた。"
    nar "何か一言でも言ってくれたのなら途中で口を閉じるつもりだったのに、彼女は淡々としている。"
    nar "ボクの知っているハクはこんな人じゃない。"
    sc "ねえ、最近変だよ…{w}しかも昨日…今日だってそうだ。何で仕事にボクを呼んでくれなかったの？"
    sc "ボクはキミの補佐教として、キミを護衛する義務がある。"
    sc "だけど最近のキミは…まるで幸福から逃げようとしているみたいだ。{w}何故変わろうとしているんだい？"
    stop music fadeout 2
    show SCG_06 2 with fastdissolve
    play sound "audio/se/ding.ogg"
    hk_b "変わる？私が？{w}そう感じたのであらば君は今まで私の事を勘違いしていたのだろう。"
    hk_b "変わったのは君だよ。ずっと前から。{w}君は空っぽだった。"
    show SCG_06 0 with fastdissolve
    play music "audio/bgm/Securett.ogg" fadein 2.0
    hk_b "「私の為に何でも」捧げられる覚悟が出来たのは、最初から君が全ての物事に価値を見出せなかったからだ。"
    nar "ボクは彼女の言葉に何も答えられなかった。"
    nar "ハクの話は速かったが、バカなボクでも理解できるくらい正確だった。"
    hk_b "もし君に価値ある物、例えば友達や他の縁があったのなら、"
    hk_b "その時も君は私のために「全て」諦める事が出来たのだろうかね？"
    nar "只固まっていたボクに、彼女はいつも通りボクに道を提示する。{w}その二つの道はどちらも暗くて長い。"
    nar "その道を一人で歩くのだと思えば息が詰まりそうだった。ボクは…"
    hide screen textbox with dissolve
    pause 1
    menu:
        "諦められる":
            show screen textbox with dissolve
            sc "…出来る。{w}キミの為なら、今だって…"
            show SCG_06 8 with fastdissolve
            hk_b "ハァ。"
            nar "随分回らなくなった頭でポツポツと語る。ハクはため息のような息遣いで、目を閉じては笑った。"
            nar "あの笑みが満足を意味しているのであれば、どれほどよかったんだろう。"
            hk_b "今は「失っている」から出来るんだろう。"
            sc "ハク、ボクは…"
            show SCG_06 0 with fastdissolve
            hk_b "誤解するな。{w}それが悪いと言いたい訳ではない。君がそうなってくれて嬉しい。"
            show SCG_06 13 with fastdissolve
            hk_b "しかし…何故自分を否定したり、私を騙そうとするのだ？"
            sc "騙そうとなんてしてない…！" with sshake
            hk_b "じゃあ何故君はこんな夜中に私に叱られているのだ？罪人にでもなったようじゃあないか。"
            hk_b "それはやめなさいと前に言ったはずだぞ。"
            sc "……"
            show SCG_06 12 with fastdissolve
            hk_b "まぁ…良い。{w}君の理解が遅いのは昔ながらの事よ。"
            hide SCG_06 0 with dissolve
            $ love_hkb = False
            $ meet_hkb = False
        "諦められない":

            show screen textbox with dissolve
            sc "……そうは出来ないだろうね。{w}もう知り過ぎたんだ、もう…"
            nar "それ以上彼女の話は否定できなかった。これが本来彼女が望んだ姿ではないかと思う。"
            nar "ボクが自分の人間性を知り、意志を持つこと。"
            nar "そう知ってしまった以上、ボクはそれに肯定せざるを得なかった。"
            sc "もう…キミとボクの二人だけで籠っていた頃とは違う、気がする。"
            sc "あまりに色んな事が怖くなってしまったんだ。"
            sc "今もそうだよ、ハク…{w}死ぬのは怖くないけど、キミと会えなくなるのは…"
            show SCG_06 1 with fastdissolve
            hk_b "誤解するな、シーキュレット。{w}それが悪いと言いたい訳ではない。"
            show SCG_06 0 with fastdissolve
            hk_b "寧ろ君がそう考えるようになってくれて嬉しい。{w}ただ私たちは向かうべき道が違うのだよ。"
            hk_b "だが君が一度歩もうと決めた道から少しでも外れるのであれば、"
            hk_b "その時こそ永遠に会う事も無い他人同士になるだろうな。"
            nar "今は彼女が何を言っているのか分かってきた。{w}彼女は独立を望んでいた。"
            nar "それがボクのことか、彼女のことかどちらになっても。"
            nar "本当の自分として一人で道を歩もうとしている。"
            sc "…ボクは自分が大嫌いなんだ。"
            nar "代わりに偽りの姿は大好きだった。{w}できればずっとそのまま溺れていたかった。"
            nar "ハクはボクの心情を理解しているかのように微笑んで、肩を叩いてくれた。"
            show SCG_06 11 with fastdissolve
            hk_b "しかし嘘偽りとは自身の生き方ではない。{w}私達はちゃんとした生き方をせんと。なぁ？"
            nar "そして元の表情に戻る。"
            hide SCG_06 0 with dissolve
            $ love_hkb = True
            $ meet_hkb = True

    nar "ハクの顔は冷静だが、事実そうでもなかった。平凡だ。{w}今までの彼女が平凡でなかっただけだ。"
    nar "彼女の話にボクを傷付ける意図はなく、只事実のみがそこにあった。"
    show SCG_06 0 with dissolve
    hk_b "君が自分を護る為の言い訳として私を使うまではまあいい、しかしそれにあまり依存するなよ。"
    hk_b "それは正しくない道だ。"
    sc "……"
    show SCG_06 12 with fastdissolve
    hk_b "それと私が君を呼ばないのはただ仕事に君が必要ではないからだよ。{w}深い意味はなかった。"
    hk_b "君は力場を見れるが、それ以外の欠点が多すぎるだろう。"
    show SCG_06 0 with fastdissolve
    hk_b "それなら他の正式司祭を呼ぶか、一人でやった方が捗る。"
    nar "だからボクは彼女の言葉に傷付かない。彼女は当然のことを語っているだけだからだ。"
    sc "わかった。"
    nar "その一言で言い切った。{w}ハクは憎らしくも、首を捻りながらボクの顔を窺う。"
    show SCG_06 11 with fastdissolve
    hk_b "やっぱ泣かないなぁ～{w}…ま、そんなもんだろうが。"
    nar "ボクの手を握っていた彼女の手が離れることが嫌で首を横に振った。"
    nar "しかしハクは顔色一つ変えずにボクの手を離してしまう。"
    nar "その手に温かさなんてなかったのに、ボクは一気に寒く感じてしまった。"
    show SCG_06 0 with fastdissolve
    hk_b "…正直に言うと、空っぽだった君に「生きる」という事を教えたのがほんとに正しい事だったのか、"
    hk_b "今じゃよく解らん。"
    hk_b "私が君を恋しく想えば想うほど、私は徐々にそれに鈍くなり、君は弱くて卑賎になるだけだったろうに。"
    show SCG_06 12 with fastdissolve
    hk_b "もしかしたら、人間とは最初から互いに触れる事など叶わない存在なのかもな。"
    nar "……"
    show SCG_06 0 with fastdissolve
    hk_b "君との会話は楽しかったよ、これだけは事実だ。{w}しかし私は…間違いなく君に会ったことを後悔している。"
    nar "ボクが過ごしてきた全ての日々のなかで、今日が一番不幸だ。"
    show SCG_06 11 with fastdissolve
    hk_b "今までご苦労だったよ。もう私に会いに来なくてもいい。{w}私が君の秘密を言わなかった様に、君もまた…"
    show SCG_06 0 with fastdissolve
    hk_b "いや、やっぱり勝手にするといい。{w}それは間もなく君だけの秘密になるだろうからな。"
    sc "ハク…"
    hide SCG_06 0 with dissolve
    nar "ボクが言葉を繋ぐ前に、彼女は席を立つ。{w}遠くなっていく彼女の後姿を只眺めることしかできなかった。"
    nar "ボクは彼女と「戯れ」をしていたんだ。"
    nar "互いに自分を渡す代わりに、足りないものを埋めていく共生を長い間続けてきた。"
    nar "夜や秘密なんぞの一言が年甲斐もなく心を浮き立たせた。"
    nar "彼女がいきなり大人の顔に戻ってこの関係に線を引いてしまうことが怖くて、"
    nar "ボクはいつも先手を打って距離を置く言葉で自分を窘めた。"
    nar "愛情なんて要らない、特別もいらない。{w}ボクらは互いに何らかの代用品なだけだと。"
    nar "そんな関係がずっと続く訳がないのに。夢の中に閉じ籠っていたのはボクだった。"
    stop music fadeout 2
    $ _skipping = False
    nar "彼女はもう完全に闇の中へ消えた。ボクの人生で一番長い夜も、徐々に過ぎていく。{w}もうすぐ朝が来る。"
    stop music fadeout 2
    hide SCG_06 with dissolve
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
    if meet_hkb == True:
        jump day11_hk
    else:
        jump day11_sc
    return
    nvl clear


label day11_hk:
    $ day = 11
    $ save_name = "day 11, 楽園"
    play sound 'audio/se/bell 1.ogg' fadein 2.0
    image 11day = Text("day 11",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '11day' at day00 with slowdissolve
    pause 5
    hide expression '11day' with slowdissolve
    stop sound fadeout 1.0
    pause 3.0
    show screen at_frame with dissolve
    scene black with slowdissolve
    pause 1
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    $ _game_menu_screen = 'preferences'
    scene bg10 with dissolve:
        xzoom -1
    call place10
    pause 2.0
    show screen nvlbox with dissolve
    nvl clear
    "\n 自分の部屋に戻ってきたが、全く眠れない。"
    "五分十分の短いうたた寝を繰り返していたら夜が明けた。{w}疲労が容赦なく脳に刺さる。"
    "どうしても起きたくなくて、ベッドから出られぬまましばらくしてから動きだした。{w}新しくできた傷の包帯を替えなくては。"
    et "古びた包帯を袋に詰め、出勤の支度をした。{w}その間に山盛りになったゴミ袋が玄関を塞いでいて、足で避けては扉を開く。"
    hide screen nvlbox with dissolve
    scene bg03 with slowdissolve
    call place03
    show screen nvlbox with dissolve
    play music "audio/se/tutorial walking.ogg" fadein 2.0
    nvl clear
    "\n まだ誰もが眠っている時間、誰もいないシャワー室に入って体を洗った。落ちる水の音に耳が痛くなる。"
    "暑がりだからありがたく思っていたこの寒さも、今日は気持ちが悪い。"
    et "まず夜の間に入ってきた申告を処理して、司祭たちに配る作業のリストを作らなければ。{w}そして、今日は三番地で葬式があるから…"
    play sound "audio/se/pii.ogg"
    pause 0.1
    stop sound fadeout 3
    nvl clear
    scene black with slowdissolve
    "\n ふと、脳が豆粒ほどに収縮したような感覚がして、一瞬針のような耳鳴りが走る。"
    "周りにはまだ誰もいない。ボクはそのまま座り込み乱れた息を整えた。"
    play sound "audio/se/Heart.ogg"
    "心臓が飛び出てしまうほどにバクバクする。理由は分からない…{w}前からたまにこうなることがあった。"
    "体を屈めると夜に傷付いた腹が再びズキズキと痛み出した。{w}一晩ずっと病院で横になっていて、治療も受けた筈なのに、"
    et "何故未だ痛いのかと腹が立ってきた。体が一つの重荷にしか感じられない。"
    nvl clear
    "\n そして仕事が始まった。{w}あちこちを忙しく巡って、夢中になって仕事をしていくとすぐに時間が過ぎていく。"
    stop music fadeout 2
    "時間の流れが速く感じられるのは幸いだ。{w}早く夜になってくれないんだろうか…"
    et "そこで考えを止めると、再び吐き気がしてくる。{w}何度も戻しそうだったが、実際は何も吐くことはなかった。空腹でよかった。"
    hide screen nvlbox with dissolve
    scene bg03 with dissolve
    call place03
    pause 1.0
    show screen textbox with dissolve
    play music "audio/SE/prologue wind.ogg" fadein 2.0
    nar "真昼になり、昨日の書類を主教様に報告する時が来た。書類を数えながらため息を吐く。"
    nar "こんな状況でも冷静になれないなんて、情けない。"
    nar "午前が午後になっただけなのに、可笑しいと思ってしまうほど一気に暑くなってきた。"
    nar "炸裂する太陽が灰色の空に白い層を作り出し、空気は徐々に濃くなって息が苦しい。"
    show SCG_05 8 with dissolve
    hkn "シーキュレット兄弟？"
    nar "やがて部室から彼女が出た。"
    nar "ボクの知っているハク主教だ。{w}ボクは現実と非現実の間に投げ飛ばされたような気持ちで彼女の前に立った。"
    sc "はい…"
    hkn "その書類は、私が午前に任せて置いた物ですか？"
    sc "いいえ、昨日の午後でした…午前の書類は、未だ受理中です。"
    hkn "ふむ…そうですか。{w}私が知っておくべき事項はございますか？"
    sc "あ…本日午後3時に団体の件がございます。{w}出来るのであれば2時から顔を合わせて日程の相談がしたいと。"
    show SCG_05 9 with fastdissolve
    hkn "2時ですか…なら今から作業場に向かうべきですかね。"
    hide SCG_05 with dissolve
    nar "ボクはぼやけていく目をやっとの思いで開いて、目の前の主教を見つめた。"
    nar "平常を演じる彼女の身振り、口振りが丸見えで息苦しくなってきた。"
    nar "しかし彼女はたった一度さえも苦い顔はしなかった。"
    nar "ボクのように元気なく答えたり、視線を避けたりはしなかった。"
    nar "今のハクはまるで彼女が元々なりたがっていた「主教」だ。"
    nar "彼女の後ろで揺れる髪を見つめる。{w}今日は彼女を起こしに行けなかった。"
    nar "服を着させても、髪を整えさせてもいなかったのに、彼女はしわ一つもなく優雅だ。"
    nar "元々ボクの助けなんて要らなかったんだろう。{w}ボクなんかは…"
    stop music fadeout 1
    scene black with dissolve
    nar "歩き出した瞬間、視界が暗くなる。"
    nar "ハクは暗いところが苦手なのに、大丈夫かな。"
    play sound "audio/SE/luggage down.ogg"
    nar "直ぐに全身から血が抜け出るような感覚がして、頭が壁にぶつかった。" with sshake
    nar "四方へ散った書類を見てやっと意識がはっきりする。"
    scene bg03 with dissolve
    nar "ボクは急いで書類を拾い集めた。{w}こんなにも暑いのに、手だけが驚くほどに冷えている。"
    nar "今ボクは何かおかしい、今になって気が付いた。"
    sc "ごめん…"
    nar "頭上の影が近付いてくる。"
    nar "顔を上げると、陰の中でハクの目は青く光っていてボクは再びぼんやりして彼女を見つめた。"
    nar "口が頭よりも先に動いてしまう。"
    stop music fadeout 2
    sc "あの…ハク、キミに言いたい事があって…"
    nar "ハクは冷静な朦朧さが抜けたような無表情で、書類を拾ってはボクに手渡す。"
    nar "声が先ほどよりもはっきり聞こえてくる。"
    show SCG_05 11 with fastdissolve
    hk_b "中で話そう。"
    hide SCG_05 with dissolve
    nar "しかしボクはその言葉の意味が分からなかった。"
    play sound "audio/se/Heart.ogg"
    nar "頭をぶん殴られているような頭痛、鳴り響いていた心拍が静まっていくのを感じた。"
    nar "その表情は少しの優しさもなく淡々として、声はあまりにもいつも通りで思わず昨日のことを忘れてしまった。"
    nar "事実もう忘れてもいいことだ。{w}今大切なのは、ボクが再び機会を得たということだ。"
    nar "主教でないハクと再び話せる機会を…"
    play sound "audio/se/ding.ogg"
    pl "おい、シーキュレット！どこ行ったかと思えばこんなところにいたんだな、探してたぜ～"
    hide screen textbox with dissolve
    pause 1
    show SCG_01 with dissolve
    pause 1
    show screen textbox with dissolve
    play music "audio/SE/no more bell my buddy.ogg" fadein 5.0
    nar "その声は突然やってきた。{w}うんざりするほどに聞き慣れていたはずが、随分久しぶりに聞いた声だ。"
    nar "ポンと肩に彼の重い手が乗せられる。ハクも同じく驚いた目をしていた。"
    nar "ボクはゆっくりと視線を隣に向け彼を見た。"
    show SCG_05 5 at hkright
    show SCG_01 1:
        xalign -0.35
    with dissolve
    pl "主教様、今忙しいか？俺、シーキュレットとちょっと話があるんだよな。{w}借りてっていい？"
    show SCG_05 1 with fastdissolve
    hk "はい…まぁ。"
    nar "ハクは途端に猫を被るかのように笑顔を張り付ける。"
    nar "その笑みはボクから書類を受け取る為に頭を下げた瞬間スッと消えた。"
    show SCG_05 11 with fastdissolve
    hk "お二人はとても仲が宜しい事で…"
    hide SCG_05
    hide SCG_01
    with dissolve
    nar "明白に警戒と疑心が満ちた目で、ボクの肩越しに彼を睨んでいた。{w}本能的な恐怖が湧き上がってくる。"
    hide screen textbox with dissolve
    pause 1.0
    show screen textbox with dissolve
    nar "ボクと[na]は並んで、いや[na]に引っ張られるような形で歩き出した。"
    nar "前に彼を力場から引き離した時もほぼ同じ速度だったな。"
    nar "ボクはずっと俯いたまま、彼の顔を見ないようにしていた。全身の力は既に抜けている。"
    nar "ボクを更に前へ、奥まった所へ引き摺ろうとしている彼がいなかったら倒れたかもしれない。"
    show SCG_01 1 with dissolve
    pl "気持ち悪い。"
    sc "……"
    show SCG_01 3 with fastdissolve
    pl "ゴキブリが、死にもしねえでまたノコノコと…{w}お前もそんな生き方じゃウンザリしねえか？"
    pl "能力もない、口だけ達者で、無責任で、理由もないのに人に当たり散らして、"
    pl "そうやって人様に迷惑かけやがって…"
    nar "彼は未だに錯覚に溺れているが、ボクは彼がずっと前から何に対してここまで激怒し、"
    nar "憤慨しているのか知っている。"
    nar "答えは「無」だ。真っ当な理由や対象など、とうの昔に消えている。"
    nar "その「怒って然るべき理由」が消えたのと同じくらいの頃に彼はボクに形のない憎悪を重ね始めた。"
    nar "ボクの目に映った自分を見ては、そこに憎悪を重ねていたんだ。"
    nar "ほら、彼は今現在もボクではなく、まるで彼自身の話をしている様ではないか。"
    pl "お前の主教はお前がこんなことしてるって知ってんのか？{w}自信満々で格好付けやがって…"
    pl "そりゃそうだもんなあ、お前みたいなヤツが何がエラくて臨時補佐教なんだ？"
    pl "そうやって態度をコロコロ変えてお偉いさんに尻尾振って昇進したら気持ちいいか？"
    pl "それも主教様から習ったんだろ？{w}なあ。"
    hide SCG_01 with dissolve
    nar "何もかも明確になった。{w}それと同時に頭が冷えてくるのを感じる。"
    nar "ボクたちはいつかのように互いを睨んでいて、ボクは自分の仕事を済ませる為に一人でこの場を去ろうとした。"
    nar "なのに彼はまだボクを引き留める。手首を締め付けられる苦痛が醜い何かに感じられて、相当不快だった。"
    nar "殴られっぱなしは良くない、なんなら殴った方がいいぞ。なんで今ハクの話を思い出したんだろう。"
    play sound "audio/se/slap.ogg"
    nar "ボクは彼女の言葉に従うように彼の頬を打った。" with sshake
    sc "ボクへの暴言を言い尽くしたことはわかった。{w}けどたわ言も大概にしろよ。"
    sc "オマエみたいな奴が勝手に彼女を語るな。"
    nar "ボクはすぐ彼に髪を掴まれ苦痛に顔が歪む、しかしこの言葉に後悔なんてない。"
    stop music fadeout 3
    nar "廊下の風景が目眩がするほどに速く過ぎていく。"
    nar "近くで見ると長いな、腕と脚。{w}[na]を羨んでいたことを思い出した。"
    nar "ボクもこんなに強くて、背の高い人になりたかったのに…"
    nar "部室の扉が開く音がする。ボクの視界は真っ赤に光ったあと暗くなった。"
    hide screen textbox with dissolve
    scene bg14 with dissolve
    call place14
    pause 1.0
    play sound "audio/se/door close.ogg"
    show screen textbox with dissolve
    play music "audio/bgm/grumble.ogg" fadein 2.0
    show SCG_02 5 with dissolve
    my "な…なに？" with sshake
    hide SCG_02 with dissolve
    nar "頭の上からマヤの声が聞こえた。{w}最初は幻聴か何かだと思っていたが、その姿が傾いたまま目に入った。"
    play sound "audio/SE/humanstrike.ogg"
    nar "ボクは床に転ばされ背中や腹が蹴られる度に咳をして、[na]は未だよくわからない罵詈雑言を叫んでいた。"
    nar "偶々視野に入ったマヤは消極的に首を振ったり、口を塞いで悲鳴を我慢しているように見えた。"
    nar "彼女の姿は徐々に小さくなっていくようだった。"
    nar "恐らくここから逃げ出して、永遠に見なかったことにしたいんだろう…"
    show SCG_02 3 with dissolve
    my "やめて…{w}もうやめて、[na2]くん！キューくんを殺さないで！だめだよ、そんなの…！" with sshake
    hide SCG_02 with dissolve
    play sound "audio/SE/slap.ogg"
    nar "ボクが再び目を開いた時、彼女の声はとても近い所から聞こえた。"
    nar "体の感覚が鈍くなって、痛みでズキズキとしていた腰と額が徐々に暖かくなっていく。"
    nar "ふわりと浮かんだ精神が、重たくて傷だらけになった体から出て遠くへ旅立つような気分だ。"
    stop music fadeout 3
    show SCG_01 2 with dissolve
    play sound "audio/se/Heart.ogg"
    pl "おい……何か言えよ、言いたいことあるんだろ。"
    nar "そのせいか、ボクは彼が怖くない。{w}事実、今までもそうだった。"
    nar "ボクを殺そうと振るわれる暴力より、たった一言の、ボクに対する憎悪の方が傷つく。"
    nar "だから彼のこういう行動にも腹が立たない。{w}只、うんざりしてきただけだ。"
    sc "…ボクはキミに何も言う事は無い。"
    sc "一体キミは…何がしたいんだ？{w}さっきから理由もない侮辱ばっかりじゃないか。"
    sc "もう、もう勘弁してくれよ…ボクはキミとしたい話なんかない…{w}キミがそうさせたんだろ。"
    nar "彼は立ち止まったまま動かなくなった。脚が固まっているだけで力は抜けている。"
    nar "ボクは自分の口から出てきた言葉が再び彼を、そして隣で聞いていた筈の彼女を傷付けたことに気が付いた。"
    nar "しかしボクも彼らと同じく、関係が終わってしまうことに衝撃を受けている。"
    nar "三人の不安な息遣いだけが渦巻のように混ざっていく。"
    stop music fadeout 2
    show SCG_01 at huruhuru
    pl "…うるさい…"
    play sound "audio/SE/hit.ogg"
    show SCG_01 4
    pl "うるせえ、うるせえ、うるせえ…黙れ、黙れ！！" with sshake
    hide SCG_01 0 with dissolve
    hide screen textbox with dissolve
    pause 1.0
    show screen textbox with dissolve
    nar "視界に一筋の血が滴って落ちる。"
    nar "目の前から起きているあらゆることに現実感がなくなっていたボクは、鈍くなっていた体の感覚が蘇ることに気が付いた。"
    nar "ボクは目を大きく見開いて、鮮明な視界で目の前だけを見つめる。"
    play music "audio/bgm/golden haku.ogg" fadein 2.0
    nar "[na]が振り上げた手を、ハクが掴んでいる。{w}彼は困惑することもなく、憤怒を殺さずに唇を噛んでいる。"
    nar "ハクは彼のそういう状態を分かっているのか、まるで袋を投げるかのように彼を横へ投げ倒した。"
    nar "そしてボクを見つめた。{w}正確に言えば「ボク」でなくこの事件の被害者を見ている。"
    nar "慈悲のない残忍な、審判者の姿だった。"
    show SCG_06 0 with dissolve
    hk_b "シーキュレット、娘を連れて出てなさい。"
    hide SCG_06 0 with dissolve
    nar "ボクはそれに答える代わりに、体を起こそうと力を入れる。"
    nar "手足が今すぐにでも体から落ちてしまいそうなほど軋んでいる。"
    nar "マヤはずっとボクたちの隣に立って、顔を覆ったまま泣いている。"
    nar "彼女はボクが声をかけなくても死体のように重い足取りで、そして大人しくボクに付いて歩いた。"
    nar "部室から出る前にもう一度ハクを見た。ハクはボクが落とした血痕や倒れた机を見て、最後にボクに振り向いた。"
    nar "しかしボクはそこから出ていくしかなかった。"
    stop music fadeout 2
    hide screen textbox with dissolve
    scene black with dissolve
    pause 3
    hide screen textbox with dissolve
    scene bg14 with dissolve
    pause 1.0
    show screen nvlbox with dissolve
    nvl clear
    play sound "audio/se/kick.ogg"
    "\n 鋭い靴が背中を蹴飛ばし、蟀谷を踏み潰した。{w}一瞬で視野は暗くなって、硬い靴の底が俺の髪を踏み躙る音だけがしていた。"
    "俺は顔を上げて彼を見つめた。女は部室の沈んだ空気の中、午後の陰の下で泰然として立っている。"
    play sound "audio/se/running.ogg"
    et "二人分の足音が頭の上を通り過ぎる。{w}二人のどちらもびっこを引いて歩くせいでまるで四、五人居るのかと思うような足音だ。"
    hide screen nvlbox with dissolve
    pause 1.0
    show screen textbox with dissolve
    play music "audio/bgm/golden haku.ogg" fadein 2.0
    nar "俺は床に伏せて熱い頭を冷やした後、ゆっくりと起き上がった。"
    show SCG_06 8 with dissolve
    hkn "随分と楽しそうではないか、あんな小さい女の子を血塗れにしておいて。"
    nar "攻撃的な言葉とは違って、声はまるで文を読むかのように淡々としている。"
    nar "その無表情があまりにも頑強で呆れてしまいそうだ。"
    nar "今までの図々しい姿が一つに重なる。{w}この野郎、最初からそうだったんだ。初めて会った日からそうだった。"
    nar "陰鬱な陰にずっと隠れていたくせに、今更俺を何とかするって？"
    nar "狭い空間で禍と対峙している状況に、昔の記憶が浮かんでくる。{w}みすぼらしい野外の礼拝堂で彼女の刃に刺された記憶。"
    nar "昔の記憶というよりは、夢の方が正確だろう。徐々に息が荒くなる。"
    nar "俺は彼女が怖くないのに、体は実際に起きてもいない夢の記憶に恐怖を感じている。{w}それがとても不愉快だった。"
    show SCG_06 12 with fastdissolve
    hkn "一言言わせてもらおう。"
    nar "俺に罰が必要だろうと、奴がそう言うと思っていた。"
    nar "そして微かに浮かんだ恐怖に拍車が掛けられ、息が荒々しくなっていく。汗が出てきた。"
    nar "今度こそ俺を殺そうとしているんだ。うっかりそう思ってしまった。"
    nar "しかし違った、全く。"
    nar "彼はなにかとんでもない、恐ろしいことを言い出す準備でもしているようにゆっくりと息を吸った。"
    nar "一気に出てくると思っていた話が出てこない。"
    nar "俺はその口からどんな言葉が出てくるのか考えるが、全く見当が付かない。"
    stop music fadeout 2
    show SCG_06 0 with fastdissolve
    hkn "シーキュレットには手を出すな。私には何をどうしても構わない。"
    play sound "audio/se/ding.ogg"
    pl "…は？"
    nar "俺は驚き過ぎて阿保らしい声で問い返した。{w}只呆れだけを感じていたいが、そう容易くはいかなかった。"
    nar "そんな言葉が出てくるとは思わなかったが、理解ができない言葉ではないからだ。"
    show SCG_06 8 with fastdissolve
    hkn "どうせ君が必要としているのは「憎悪を押し付ける対象」だろう。{w}なら相手が私でも構わないな？"
    hkn "それに、初めから君は私の事が嫌いだったろうし。"
    hide SCG_06 with dissolve
    play sound "audio/se/Heart.ogg"
    nar "その話に、はいそうですと共感するつもりなんてないが、頭よりも体が先に反応してしまう。"
    nar "額に一つずつ血管が浮き出て、肌がズキズキしてきた。{w}あの声のせいだ。"
    nar "認めたくないが、俺はもう「彼女」の声を無条件に信じてしまう。感情があまりにも簡単に憤怒へ導かれていく。"
    nar "ならばお望み通りにやるしかない。俺は彼女の体を拳で殴りつけた。"
    nar "この場所で同じように倒した誰かとは違って、彼の体は重たく転ぶ。"
    stop music fadeout 2
    nar "床に広がった真っ白い髪がまるで虫の糸のようで気持ち悪い。"
    play sound "audio/se/hit.ogg"
    pl "乳繰り合うんならお互いだけでしてろよ、なんで俺まで引き込むんだよ……{w}何でだよお！！" with sshake
    play sound "audio/se/kick.ogg"
    hide screen textbox with dissolve
    pause 1
    show cghk03 with slowdissolve
    pause 2.0
    show screen nvlbox with dissolve
    play music "audio/bgm/Haku.ogg" fadein 2.0
    nvl clear
    "\n 俺は声を張り上げながら彼女を容赦なく蹴飛ばした。{w}十字を切るときにだけ屈める腰、善行と典礼を繰り返してきた崇高なる手、"
    et "いつか「回帰」を表現した時に撫でていた腹まで何もかも靴底で蹴り倒した。"
    nvl clear
    play sound "audio/se/humanstrike.ogg"
    "\n この死体のような姿！誰もが想像できないだろう。" with sshake
    "いつも綺麗にアイロンが掛けられていた服は埃が付き灰色になって、念入りに束ねた髪も縺れて顔を覆う。"
    et "狂人が汚い欲望を込めて描いた絵のように、只微動だにせず横になっている。{w}まるで棺に入った死体だ。"
    nvl clear
    "\n もし彼女がそこで目を閉じていたら、俺は全てを止めたかもしれない。"
    play sound "audio/se/humanstrike.ogg"
    "しかし主教は俺の不安と期待をそのまま実行するようにと、気を失うことなく俺を見つめていた。" with sshake
    et "目が合った瞬間、俺は反射的に顔を蹴飛ばした。{w}上に乗って拳を高く持ち上げた。柔らかい肌の感触が汚く感じられた。"
    nvl clear
    play sound "audio/se/humanstrike.ogg"
    "\n 俺はどうか彼女の顔に憎悪や屈辱が満ちていることを願っていたが、女は制御のできない獣を見るような無関心な表情で俺を見つめている。" with sshake
    "彼女に合う表現で言えば、死刑の寸前、土壇場の抵抗している囚人を見ているような顔だ。{w}暴れる狂人を見る目だ。"
    "俺が最も恐れていたその表情。{w}シーキュレットがしていた男子への奉仕は全てこの女から教わったものだな。"
    play sound "audio/se/hit.ogg"
    et "阿婆擦れ野郎共、俺の人生を壊したクソ野郎共、お前らの、お前らのせいで俺が…！" with sshake
    hide screen nvlbox with dissolve
    pause 2.0
    hide cghk03 with slowdissolve
    pause 1.0
    show screen textbox with dissolve
    pl "……"
    hkn "終わったか？"
    pl "……"
    hide screen textbox with dissolve
    pause 1.0
    show screen textbox with dissolve
    show SCG_06 8 with dissolve
    hkn "だろうな。まっとうな理由のない憎悪は爆発的ではあるが、長くは持たない。"
    hkn "自身がそろそろ阿呆の様に感じられてくる頃だろう。{w}どうだ？"
    pl "うるせぇ、口を開く前にお前自身の立場を理解した方がいいぞ。"
    pl "主教様だって精神異常者のくせに、誰に向かってエラそうに口叩いてんだよ…{w}クソッ！" with sshake
    hide SCG_06 with dissolve
    play sound "audio/se/luggage down.ogg"
    nar "俺は主教の胸倉を掴んで、服のボタンを荒々しく取り離した。"
    nar "石膏のように真っ白い首からは浄化部の臭いがする。"
    nar "化粧品や石鹸でできる限り切除された悪臭。その日常の臭いが慄然になり広がる。{w}すぐ薄い喉頸が動く。"
    show SCG_06 10 with dissolve
    hkn "ハッハッハッハッハ！これは傑作だ！" with sshake
    nar "女は首を反らして笑った。濁った笑い声が再び俺を混乱させ、彼女は長い脚を伸ばして俺の腰に触れた。"
    nar "縺れた前髪の間から大きく開いた瞳が鋭い光を出した。"
    show SCG_06 8 with fastdissolve
    hkn "テメェみたいな輩は初めてじゃあないんでな。"
    nar "耳元に低く囁く声が俺の首を絞めてくるような感じがした。"
    nar "俺は憤怒でなく、恐怖を感じる時の不安な息を出した。又笑い声が聞こえる。"
    show SCG_06 2 with fastdissolve
    hkn "で？この後はどうする？{w}これは君が本当にしたかった事か？"
    show SCG_06 4 with fastdissolve
    hkn "君は「この後」も後悔しない自信があるのか？"
    nar "俺の息は、その中に混じる声が聞こえてしまう程に大きくなっていた。"
    nar "俺が「本当に」したかった事かって？{w}いや、そんな訳ないだろう。"
    nar "誰がこんな惨いことを、正気でない限り一体誰が…！"
    hide SCG_06 with dissolve
    play sound "audio/SE/humanstrike.ogg"
    nar "俺は彼女の胸倉を掴んだまま、床に投げ飛ばす。"
    hide screen textbox with dissolve
    scene black with slowdissolve
    show screen nvlbox with dissolve
    nvl clear
    stop music fadeout 2
    play sound "audio/se/running.ogg"
    "\n そして彼女が顔を上げて、目が合ってしまう前にその場から逃げた。"
    "酷いものから目を逸らしたい一心だったが、それは自ら彼女の言葉を認めてしまうようなものだった。"
    et "彼女の姿は最後まで振り返らなかった。{w}俺に付いてきているなら、寧ろそうだったらよかっただなんて思っていた。"
    nvl clear
    "\n しかし彼女は人々の中にいる罪人を間引く「禍」ではなかった。"
    et "彼が俺のことをどれだけ心配してくれたのか分かっている。{w}魔導部に行けなかったことも単なるミスだと理解していた。"
    nvl clear
    "\n 彼が自分を守る為にどれだけ努力してくれたのか、勿論分かっている。"
    "それをとんでもない理由でずっと否定してきたのは、シーキュレットを許した瞬間俺はこの地を去らざるを得なくなるからだ。"
    "一度ヒトデナシになったと認めてしまえば、以前までの人生には戻れない。"
    et "俺がしてしまったことを認める勇気がなかったからだ。{w}思い通りにいかない息苦しい状況で、憎悪を押し付ける相手が必要だったからだ…"
    nvl clear
    stop music fadeout 2
    et "\n 残酷な記憶は各々の重さを持つ。それに対しごめんなさい等という謝罪の言葉はあまりにも軽く感じられた。"
    hide screen nvlbox with dissolve
    pause 3
    scene bg03 with slowdissolve
    call place03
    pause 1.0
    show screen textbox with dissolve
    play music "audio/se/tutorial walking.ogg" fadein 2.0
    nar "マヤはゆっくりと、肩をびくびくさせながらボクに付いてきた。"
    nar "彼女を支える為に握った肩がとても痩せこけていると感じられた。"
    nar "ボクはあの日の夜に起きたことで、マヤがボクの死を望んでいると思っていた。"
    nar "だから彼女がか弱い体で[na]に必死に縋りついた時は、本当に驚いた。"
    nar "マヤはボクに憎悪を抱いている、それだけは確かだが、その怨望には未練が秘められていたのかもしれない。"
    nar "ボクたちがやがて足を止めた時、マヤはボクを見つめていた。{w}鼻と目尻が赤く腫れたままだ。"
    sc "マヤ…"
    nar "彼女に先に言うべき言葉が「アリガトウ」か「ゴメン」か決められなくて顔を顰めた。"
    nar "するとマヤの表情も歪んでしまう。"
    nar "止まっていた涙が再び零れ落ちて、喉から苦痛を搾るような呻き声が聞こえてくる。"
    nar "マヤはそのまま拳を作っては、とてもゆっくりボクを一回、二回と叩いた。"
    nar "その力があまりにもひ弱過ぎて、ボクは三回目になってやっと彼女はボクを殴っているんだと気付いた。"
    show SCG_02 3 with dissolve
    my "だいきらい…"
    nar "ボクは同じくゆっくりと、動きを止めた彼女の背中に手を置いた。"
    nar "マヤは痛いほどに強くボクの腰を抱き締めては、大声で泣きだした。"
    nar "彼女の流した涙でボクの服は徐々に濡れていくが、ボクは彼女を突き放す事無く抱きしめていた。"
    nar "震える背中を摩る。"
    stop music fadeout 2
    hide SCG_02 0 with dissolve
    hide screen textbox with dissolve
    pause 2
    show screen textbox with dissolve
    nar "ボクたち二人はしばらくそうしていて、それから別れたのだ。"
    play sound "audio/se/running.ogg"
    nar "部室に戻る為に進路を変えると、ボクと反対側へ走っていく[na]が見えた。"
    nar "急いで扉の前に立つ。"
    nar "彼が無事だと分かったまではよかったが、ということはハクに何かがあったってことか？"
    nar "中で何が起きていたのか、想像することが怖くなった。"
    play sound "audio/se/door slide.ogg"
    nar "その時、扉が開いた。"
    sc "うわっ……" with sshake
    show SCG_06 5 with dissolve
    play sound "audio/se/hit.ogg"
    hk_b "ワッ！？" with sshake
    hide SCG_06 with dissolve
    play music "audio/bgm/golden haku.ogg" fadein 2
    nar "ハクは驚いた顔で一歩後退りをした。ボクも驚いた顔で彼女を見ていた。{w}心臓が止まるかと思った。"
    play sound "audio/se/luggage down.ogg"
    nar "ハクはそんな視線を避ける為にそっぽを向いたが、ボクは彼女の顔を覆ってこちらに引き寄せた。"
    sc "何て顔なんだよ…"
    nar "傷だらけの顔に触れる手が震えた。彼女がボクの手から離れてからも、震えは止まらず全身へ広がる。"
    show SCG_06 0 with dissolve
    hk_b "誤解はしないでくれたまえ。"
    nar "ハクは青く腫れ上がった頬を撫でながら話す。"
    show SCG_06 1 with fastdissolve
    hk_b "私が負けた訳ではない、そうさせてやったんだよ…小僧め、餓鬼にしてはいい拳だったもんだ。"
    sc "………"
    show SCG_06 11 with fastdissolve
    hk_b "なあに泣いてんだ。"
    nar "びっくりして目尻を指で拭う。{w}そこは少し湿っていたが、冷や汗かもしれないと思ってしまった。"
    sc "泣いてないし…"
    hk_b "ハハ。主教たるものとして誤った道を歩む仔羊を矯正したまでよ。個人の為ではない。"
    hk_b "だから変に責任を感じるなよ。"
    sc "……"
    hk_b "しかも君、自分の顔は気にしないんだな？私よりめちゃくちゃだぞ。"
    sc "ボクの顔なんてどうでもいい！キミをそのまま人前に立たせる訳にはいかない…！{w}早く治療しなきゃ……"
    show SCG_06 12 with fastdissolve
    hk_b "なら…"
    show SCG_06 1 with fastdissolve
    play sound "audio/se/ding.ogg"
    hk_b "私の部屋に来るか？"
    hide SCG_06 with dissolve
    hide screen textbox with dissolve
    pause 2.0
    scene bg15 with slowdissolve
    call place15
    pause 1.0
    show screen textbox with dissolve
    nar "ボクたちは久しぶりに一緒に寮に帰った。"
    nar "静かな一階、廊下の末端にある自分の部屋を前にして、ハクはしばらく立ち止まっている。"
    show SCG_06 0 with dissolve
    hk_b "シーキュレット、鍵。"
    sc "ん？"
    nar "嗚呼、小さく声を発した。{w}ポケットから持ち出した予備の鍵が未だ輝いている。"
    hk_b "やっぱり君が持っていたのだな。{w}返してくれ。"
    nar "彼女が差し出した手に鍵を渡した。"
    nar "ボクは彼女が鍵穴に鍵を差し込み、手首を回して鍵を開けるところをじっと見つめていた。"
    sc "何で？"
    show SCG_06 12 with fastdissolve
    hk_b "何でって、それは…いつも開いてるから？"
    hide SCG_06 with dissolve
    play sound "audio/se/door close.ogg"
    hide screen textbox with dissolve
    scene bg108 with slowdissolve
    call place108
    pause 1.0
    show screen textbox with dissolve
    nar "今思いついたかのように付け加えた言葉と共に、扉が開く。{w}毎日訪れる場所なのに今日は何故か落ち着かない。"
    nar "ベッドの隣、灰皿と一緒に置いてある蝋燭はもう完全に溶けきっていた。"
    show SCG_06 0 with dissolve
    hk_b "シーキュレット、何を見ている？そっちではないぞ。"
    sc "最近も寝付けていないの？"
    show SCG_06 11 with fastdissolve
    hk_b "前ほどではない。悪夢を気にしないようになってな。{w}仕事が増えたから寝る時間も減ったまでだ。"
    sc "へぇ…"
    hide SCG_06 with dissolve
    nar "部屋に戻ればすぐに治療やいつもの会話を始めるものだと思っていたが、"
    nar "ハクはボクと同じく部屋をうろつきながら食器棚を覗き込む。"
    nar "ボクも続いて部屋を見回して、本棚の横に置きっぱなしにされたゴミ袋に気が付いた。"
    nar "透けて見える袋の中にはハクが好んでいた映画のフィルム、"
    nar "特にアクション映画や英雄をテーマにした映像などが入っている。"
    show SCG_06 2 with dissolve
    hk_b "オイオイオイ、ネズミでもあるまいしコソコソ探るなよ。"
    sc "これ、捨てるのかい？キミが毎日の様に見返してた……{w}ジャガイモ特攻隊だっけ、あれじゃないか。"
    show SCG_06 9 with fastdissolve
    hk_b "初代のシリーズまで全部あるんだぞ。{w}フフ、成人式を行なう前から観ていた物だが…"
    show SCG_06 11 with fastdissolve
    hk_b "そろそろ卒業せんと。仕事に集中せねばならん時期だしな。"
    hide SCG_06 with dissolve
    nar "ずっと部屋を歩き回っていたハクは黒い瓶、そしてグラスを二つ持ってきた。{w}聞かなくても酒だと分かる。"
    sc "キミ……"
    nar "ハクは口を噤んだまま微笑んだ。それは初めて見る笑顔だったが、恐らく返事を誤魔化したい時の表情だろう。"
    nar "しかもあの笑顔はボクに酒を勧めている。"
    nar "ボクが野外礼拝堂に訪れ始めてから酒も煙草も辞めたことを知っている筈なのに。"
    sc "治療すると言ったじゃないか…仕事は？"
    show SCG_06 1 with dissolve
    hk_b "そんなものは君が気にしなくていい事だ。患者に仕事は任せられないだろう。"
    sc "患者に酒を勧めるのは良くて？それに…{w}ボク、まだ飲めないよ。"
    show SCG_06 9 with fastdissolve
    hk_b "大人が勧める酒は飲んでも良い酒さ。"
    sc "…部屋にはいつもこんな物が？"
    hk_b "勿論、棚一つが酒の保管庫になっていてな。"
    sc "なんで寮で趣味生活を…"
    show SCG_06 0 with fastdissolve
    hk_b "そりゃあ…本家には私の部屋がないからさ。{w}さあ、両手でぐいっといくんだぞ。"
    nar "褐色の透明な酒は、一口飲んだだけで喉が辛い。"
    nar "冷たい酒なのに食道がひりついて、その熱気に腹が熱くなってきた。"
    nar "渋い後味と焦げた木の様な匂いが鼻に伝ってくる。{w}げっ…これは割らないと飲めない酒だったんじゃ？"
    sc "これ…高いやつだ。"
    show SCG_06 1 with fastdissolve
    hk_b "君なら間違いなく好きになるだろう。"
    nar "ハクは多分口の中にも傷がある筈なのに、こんなにも強い酒をゴクゴク飲み干す。まるで急いで酔おうとしているように。"
    show SCG_06 0 with fastdissolve
    hk_b "…シーキュレット、君は君の本当の名前を憶えているか？"
    nar "ハクがいきなり問い掛けてきた。ボクはハクのこういう突然の質問に慣れている。"
    sc "名前…{w}今更それに何の意味があるんだい。ボクは既にシーキュレットという名前で呼ばれてるんだよ？"
    hk_b "もっと慎重に考えた方がいいぞ。名前にはその人の運命や生命が宿るものでな……"
    show SCG_06 11 with fastdissolve
    hk_b "なぁに、君の言っていることが間違っているという意味ではない。"
    hk_b "必ず本名でなくとも、 名前として呼ばれるのであればそれもまた自身の名前になるだろうからさ。"
    sc "…もしそうならさ、キミは何て呼ばれたいんだい。"
    show SCG_06 12 with fastdissolve
    hk_b "私か？そうだな……{w}英雄、かな。"
    nar "ハクはその言葉を最後にしばらく口を噤んで、酒を堪能しながら目を伏せる。"
    nar "恐れていることを口に出すための時間を持つようだった。"
    stop music fadeout 2
    nar "そしてすぐ、世の中誰もが仰天するような言葉を吐き出した。"
    show SCG_06 0 with fastdissolve
    hk_b "アルネ・アルタナータを殺したのは私だ。"
    nar "今朝、正確には昨日の夜にアルネ・アルタナータは死んだ。"
    nar "噂では怪しい男の襲撃で、共にいた彼女の弟が死体を運んできたと言われている。"
    play sound "audio/se/Heart.ogg"
    nar "どこからどう見ても真実を語っている彼女の目付きに、ボクは臆してしまった。"
    nar "その目を逸らすことはできなかったが、「そうか」と頷くこともできなかった。"
    sc "うん…"
    nar "結局馬鹿みたいな返事をしてしまう。{w}ハクは目を細めて首を横に振った。"
    nar "いつもとは違い、理由を聞いて欲しいのだろう。"
    sc "…どうして？"
    hk_b "それを説明するには、大分遡る事になるが…"
    sc "言ってみなよ、全部。"
    nar "ハクは頷いた。ゆらゆら揺れる酒瓶の空いた部分が紫色に光っている。{w}そうしてとんでもない話が始まった。"
    play music "audio/bgm/Haku.ogg" fadein 2.0
    hk_b "幼い頃の私はお父様の関心を引くため必死だった。"
    hk_b "彼は冷静で、無口な人だったから私を養子として受け入れたのには何か特別な理由があるだろうと思っていた。"
    show SCG_06 12 with fastdissolve
    hk_b "それはきっと、怖い事なのだろうと、それなりの覚悟もあったのだが…"
    show SCG_06 0 with fastdissolve
    hk_b "彼の元で暮らすことになって以来、父様が私を呼んだのはたったの三回だった。"
    sc "…今まででたったの三回は問題アリだろう。"
    hk_b "皆各々の家庭の事情ってものがあるのさ。私が初めて命令されたのは「小さい動物を殺す事」だった。"
    hk_b "ウサギや猫の様なものだな。{w}他の説明もなくただナイフを私に握らせては『おやりなさい』と、仰ってな。"
    hk_b "なので私はお父様の前で動物を殺さなければならなかった。"
    nar "ハクは動物を嫌がる。{w}動物が嫌いな人はありふれているので大したことないと思っていたが、"
    nar "今になって考えてみればそれは動物への嫌悪感からでなく、何かもっと別の感情で避けているようにも思えた。"
    hk_b "そして動物を殺す事に慣れてきた頃、私は獣の代わりに繋がれた人間の前に立つことになった。"
    hk_b "お父様はいつも通り私にナイフを握らせたが、幼い私はこればかりは無理だと言った。"
    show SCG_06 13 with fastdissolve
    hk_b "すると…家から追い出されてしまったのだ。それは今まで覚悟してきたどの罰よりも怖かった…"
    hk_b "だから私は人を殺してきたのだよ。"
    sc "…キミの精神病の原因もそのせい？"
    show SCG_06 0 with fastdissolve
    hk_b "病気の決定的な原因を推測するのは愚かな真似だよ。"
    show SCG_06 12 with fastdissolve
    hk_b "だが確かに…あれ以来私は可笑しくなってしまったような気がする。"
    hk_b "私はそこまで大人しい子供でもなかったが故に、文字通り「狂った真似」をして回っていたのさ。"
    hk_b "日夜大声で叫びながら目に見える物全てを壊し、他人を狂わせる事ばかり考えていた。"
    hk_b "皆が私を指差しては悪霊に憑かれたと言っていたな。{w}だから悪霊祓いの儀式も受けていたんだ。"
    sc "悪霊祓い？"
    show SCG_06 0 with fastdissolve
    hk_b "田舎の儀式だよ。{w}馬小屋で、「儀式」を行なえると自称するジジイ共の掌で踊らされるだけの事さ。"
    nar "彼女がその言葉を発した途端に口を噤み、視線を上げてボクを見つめたのには訳がある筈だ。"
    play sound "audio/se/Heart.ogg"
    nar "ボクはその意味を窺い知って不安に呼吸が乱れそうになる。"
    nar "頭がガンガンと響いて、心臓はもうそれを確信しているかのように痛みを発している。"
    show SCG_06 11 with fastdissolve
    hk_b "また誤解をしているな。そうだろう？"
    hk_b "そういう人は大体宗教に狂った人間よ。そんな者共が悪霊とまぐわおうとなんて思う訳がないだろう。"
    sc "…じゃあ何だったんだよ。"
    show SCG_06 0 with fastdissolve
    hk_b "彼らが言う悪霊祓いとは即ち人間の身体と精神を以て、"
    hk_b "言わば常識的には受け入れられない様な事をして悪霊を引き摺り出すのだよ。"
    show SCG_06 1 with fastdissolve
    hk_b "人間ではない口の通じない獣を使うのもその理由だ。{w}つまり…"
    nar "彼女は空になったグラスを傾けて空気を飲んでは、口を閉じたまま笑った。"
    nar "その笑みは話が始まる時に見た、誤魔化す為の笑顔だ。"
    hide SCG_06 with dissolve
    nar "しかしボクはもうその「答え」を理解してしまった。"
    play sound "audio/se/luggage down.ogg"
    nar "ボクは持っていたグラスを投げ付けて立ち上がる。全身が震える。" with sshake
    play sound "audio/se/Heart.ogg"
    nar "ハクは暗くて冷たい所を嫌がった。{w}特に犬のことを嫌っていた。"
    nar "よく寝付けなくて、今もずっと悪夢を見ていると言っていた…"
    nar "見たことのないはずの幼いハクの姿が思い浮かんだ。{w}蒼白だった。ボクはそれを普通だと思えなかった。"
    nar "憤怒で身震いがする中、顔が火照っていることに。{w}頭は痛くないが酷く混迷している。"
    nar "心拍が弾ける度に太ももの辺りが痒くて熱くなっているような感じがしていた。"
    nar "それは憤怒や驚愕でなく、つまり、興奮した時みたいに…{w}死にたいと思った。"
    show SCG_06 0 with dissolve
    hk_b "お父様の二つ目の命令は、神殿に入社し仕事する事だった。"
    nar "ハクはじっとボクを見上げては、気にもせず話を続ける。"
    hk_b "そして3年が過ぎた頃、浄化部が出来た。"
    hk_b "君は浄化部の存在について疑ってみたことは無いか？"
    hk_b "こんな都合のいい部署が一体なぜ、急に出来上がったのかを…"
    sc "また何を言い出すんだよ。"
    hk_b "君にとっての浄化部とはどんな部署だ？"
    sc "…浄化部は生きる人々の為の部署じゃあないか。"
    hk_b "そうさ。{w}「これからを」生きる人々の為の部署。浄化部は生贄を集める為の部署だ。"
    nar "ハクはゆっくりと席から立ち上がり、ボクを見下ろした。"
    nar "ボクたち二人はどちらも酔っているようで、足元がおぼつかない。"
    show SCG_06 11 with fastdissolve
    hk_b "二千年ごとに訪れる「大禍」の事を知っているか？{w}父様が私に下した三つ目の命令がそれだ。"
    hk_b "禍が集まる州都の中心に大きい穴を作り、その中に生贄を埋め、"
    hk_b "天高くまします我らが神にもう一度この地を人間に貸して下さる様祈る事。"
    hk_b "幼い頃の訓練は全てこれの為の練習だったのさ。"
    sc "……"
    show SCG_06 0 with fastdissolve
    hk_b "司祭は神の意志に逆らえない、だから全ての主教はその儀式に同意した。"
    hk_b "自分らの城に気が取られその伝達が貰えなかった魔導部以外はな。"
    hk_b "だから我々は神殿で一番神聖力の高い魔導部の集団と行き場をなくした浄化部の司祭達を贄とすることにしたのさ。"
    sc "でも、自主退職をした司祭は皆家に帰るんじゃ…？"
    show SCG_06 4 with fastdissolve
    nar "ハクはまるで可哀想な人を見るような目でせせら笑う。{w}彼女は今まであんな目でボクを見たことはない。"
    hk_b "だからそれは違った、という事だ。{w}私は「真実」を語っているのだよ、シーキュレット…"
    show SCG_06 11 with fastdissolve
    hk_b "この前も二人が贄となったな。特にあの金髪のお嬢さん。"
    hk_b "全く自分から出て行ってくれないもので少し予定が狂ってしまったが、被せるに丁度いい罪があって助かったよ。"
    sc "…じゃあ正式司祭は何なんだよ。何をしていたんだ？"
    show SCG_06 0 with fastdissolve
    hk_b "正式司祭にはこの真実を教え、贄集めに参加できる機会を与える。辞退するのであらば…{w}残念だが。"
    sc "キミは…キミはそれを知っててボクの悩みをただただ聞いてたのか？"
    sc "ボクが新入りを心配してるって、分かってて全部…{w}どうして、キミは…"
    hk_b "正式司祭ではない君には与えられる情報など無かったからな。それだけの事よ。"
    nar "昨日までなら、ハクの話を聞いてもただ驚くか、怒るだけだった。"
    nar "それはボクが受け入れられる範囲の絶望だったからだ。"
    nar "とめどなくボクの生涯を覆った真実は重たく、暗く、黒くボクを押さえ付けている。"
    sc "そんなモノ…英雄な訳がないじゃあないか、この汚らしい殺人鬼が…"
    nar "誰かを非難する権利なんて誰にもないだろうが、罪を犯した人は当然非難されるべきだ。"
    nar "彼女の行動で本当に大禍を防ぐことができるなら、その罪は栄光で上塗りされ誰も罰せなくなるだろう。"
    hk_b "…贄が全て集ったら、穴に火を燈す心算だ。"
    nar "ハクはどう見ても楽しくなさそうな、寂しそうな顔で話を続ける。"
    hk_b "エルジェーベト・アルタナータの首を狩り、残った浄化部司祭と魔導師を全て殺すのが我々の計画だ。"
    show SCG_06 11 with fastdissolve
    hk_b "明日だよ。{w}明日、私はやがて英雄となる。"
    hk_b "外的には腐敗しきって民衆の血ばかり吸う魔導師を屈服させた英雄、"
    hk_b "水面下では人類を滅亡させる大禍を防いだ英雄として知られるだろう。"
    sc "魔導部を廃止する、って意味？{w}そんなバカみたいな計画が通じると思うのか？"
    show SCG_06 0 with fastdissolve
    hk_b "何故あり得ないと思うのだ？"
    hk_b "アルタナータの芽を潰してしまえば魔導師協会の老い耄れ共がお父様の下を這う事になる。"
    hk_b "そうなれば新しい魔導師を受け入れる事も容易くなるだろう？"
    show SCG_06 1 with fastdissolve
    hk_b "それと…今心配すべきは大禍であって、その後始末では無い筈だぞ。"
    sc "ボクはキミが彼らのことを愛していると思っていたのに…！{w}グレーテ補佐教がそんな事納得する訳がないよ。"
    sc "保健部の主教だってそうだ！{w}今までずっと共にして来た処理班の子達は？"
    sc "キミはキミが愛してきた全ての人々を裏切るつもりなのか？！" with sshake
    show SCG_06 0 with fastdissolve
    hk_b "今私の背中には数千人の命が乗っている。{w}数千人の人々と、私が愛した数人の人。"
    hk_b "必ずどちらかを選ばなければならないのなら、私は当然数千人の人々を救うさ。"
    sc "…今になってもまだキミはお父さんの関心や愛を欲しがってこんな事をするのかい？"
    show SCG_06 12 with fastdissolve
    hk_b "…私は結局あの人に指一つ触れる事さえ出来なかったが、ここ数日で確かになったことが一つだけあって、"
    show SCG_06 0 with fastdissolve
    hk_b "それは私の父上と呼ばれる神聖な存在もまた、ただ人の血が流れ、単なる肉で出来た「普通の男」だという事だ…"
    hk_b "いつまでも惰弱な錯覚などに溺れていては目標は果たせないだろう。"
    nar "頭痛が酔いと混ざって胸がムカムカする。{w}痛む頭を抱えて、目の前のハクを見た。"
    nar "彼女は間違いなくハク・エカルランだ。"
    nar "ボクがよく知っていると思っていた人、ボクよりもボクのことをよく知っていると思っていた人…"
    nar "そうではないと前から分かっていたのに、"
    nar "ボクたちが実際互いに関して何も知らなかった事実がどうしてこんなに悲しいのか分からない。"
    sc "………"
    show SCG_06 5 with fastdissolve
    play sound "audio/se/ding.ogg"
    sc "なんで…ボクにこんな事を、言うんだ？"
    nar "勝手に口から出た言葉、その問いは今までのボクたちにとってタブーとされていたことだった。"
    nar "ハクもボクが今までずっと我慢していたこのことを問われると予想していなかったのか、只目を瞬くだけだ。"
    nar "酔っているボクに彼女はとてもゆっくり動いているように見える。"
    nar "そしてすぐボクの知っているいつもの表情に戻り、暗く沈んだ声で語った。"
    show SCG_06 12 with fastdissolve
    hk_b "さぁな…私にはもう…この様な話ができる人が君しかいないのさ。"
    hk_b "君との時間が楽しかったと言ったのは嘘ではない。{w}私にとっての君は大切な人だ。"
    show SCG_06 0 with fastdissolve
    hk_b "だから私は君が真実を知り、生き延びて欲しい。{w}それが今の私が君に与えられる唯一の情けだからな…"
    nar "このクソ女。{w}その憎悪と共にボクに胸が弾けるような感覚がする。今まで感じたことのない程の動悸だ。"
    nar "いや、実はいつも感じていた。彼女と一緒に居る時はいつも。"
    nar "そんな顔をボクに見せなかったら、彼女の闇に触れる機会がなかったら、二人は一生他人のままでいた筈なのに。"
    nar "ボクは彼女に恋をしていると自覚してしまった。"
    hk_b "君は補佐教になりたがっていたが、私としては君がずっと臨時である方が良かったのだよ。"
    hk_b "正式補佐教なら仕方ないが、臨時ならいつでもここから去る事が出来るだろう。"
    sc "ボクは…ボクはそんなの望んでいない…！" with sshake
    show SCG_06 11 with fastdissolve
    hk_b "私が望んだのだ。君がこの冥土から去り、自分らしい生き方をしてほしかった。"
    hk_b "私が君を高く買っているのだから、この期待に応えてくれよ。"
    hide SCG_06 with dissolve
    nar "ハクはいつも通り、流麗な足取りで歩きだす。{w}不思議なことだ。"
    nar "残酷な真実を知ってしまい、真心を裏切られ、その身が汚れた殺人鬼だって知っていても、"
    nar "ボクの目には彼女が未だ残忍なほどに美しく見えた。"
    nar "彼女はやがてボクに瓶を一つ手渡した。透明なガラスの瓶に黄金色の酒がゆらゆら揺れる。"
    show SCG_06 0 with dissolve
    hk_b "君の昇進祝いとして準備していた物だよ。"
    show SCG_06 1 with fastdissolve
    hk_b "共にすることは出来なくなったが、心は通じる。構わないだろう？"
    nar "受け取りたくなかった。{w}ボクの長い長い目標が虚像だったってことを認めたくなかった。"
    nar "彼女がボクを騙してきたってことを受け入れたくなかった。{w}しかしボクは生きている。"
    nar "彼女がボクに虚しい目標を与えてくれたお陰で、今まで生きていられた。"
    nar "いつも通り話したかったが声が震える。全身が震えている。"
    sc "ハク、ボクはキミの行動を支持することは出来ない、キミを応援することも出来ない。"
    sc "でも…すべてを知った今でも、ボクはキミの事を幸せにしてやりたいと思う…"
    show SCG_06 0 with fastdissolve
    hk_b "それじゃあダメだ。{w}そんな考え方では生き抜いていけない。"
    hk_b "私に君の人生を任せるのではなく、「幸せになりたい」と正直に言いなさい。{w}堂々と生きるんだ。"
    hk_b "私が私である様に、君は本当の「君」なのだから。{w}私が居なくなっても……生きてくれ。"
    hide SCG_06 with dissolve
    nar "ボクはそれに何も答えられなかった。{w}ハクは他でもないボクを見つめていて、決して視線を逸らさない。"
    nar "滑らかな瓶から反射された光が、彼女の手の中で煌く。"
    nar "その光が消えた後に映った女性の姿がどれだけに幼くひ弱だったか。{w}嫌だ。"
    nar "悲鳴を上げたくなる心を辛うじて堪える。息が今すぐにでも止まってしまいそうなほど荒くなった。"
    nar "体の中が熱い何かに満たされて、もう爆発して消えてしまいそうだ。"
    nar "しかしそうやって逃げてはいられなかった。ボクは結局、自らの手で自分の運命を受け入れるしかない。"
    nar "ボクがそのプレゼントを受け取ると、ハクは顔色も変えずにボクの肩を掴んだ。"
    nar "そのままボクを後ろへ向かせ扉の前に連れて行く。硬い手袋を填めた手は驚くほどに重い。"
    show SCG_06 11 with dissolve
    hk_b "引き留めてしまってすまんな。{w}治療は必ず受けろよ。さようなら。"
    nar "今までの話が何もかも、まるで酒に酔って見た蝶の夢のように、その挨拶はいつも通り軽いものだった。"
    nar "だからボクもいつものように挨拶をした。"
    sc "また明日。"
    show SCG_06 0 with fastdissolve
    hk_b "……さようなら。"
    hide SCG_06 with dissolve
    play sound "audio/se/door close.ogg"
    hide screen textbox with dissolve
    scene bg15 with slowdissolve
    pause 1.0
    show screen textbox with dissolve
    nar "そして扉が閉まる。"
    nar "追い出されて来た廊下の陰は夜ごとく暗いが、窓の向こうには未だ月の代わりに日が昇っている。"
    nar "静かな廊下を歩く度に懐の酒が揺れる。"
    nar "ちゃぷちゃぷという水の音、倒れそうに不規則な足音が耳に漂っては消える。"
    nar "彼女と並んで立ちたかったのではない。{w}ボクはいつも彼女の少し後ろに立っていたかった。"
    nar "それだけで満足できる人生はどれだけに幸せだったのか。"
    nar "その幸福を守る為に「ボク」は要らないと思っていた。{w}事実それを一番否定したかったのはボクなのに。"
    play sound "audio/se/Heart.ogg" loop
    nar "止まった脚が震える。座り込んでゆっくりと深呼吸をした。"
    nar "アルコールの臭いがする熱い息が頭に刺さる。もうここで立ち上がれなくなるほどに。"
    nar "断ち切れる…今になってあの時を思い出してしまったのは何故だろう。{w}もうとっくに遠くまで来てしまったのに。"
    nar "彼女の口から出てきた重い真実。"
    stop music fadeout 2
    nar "とんでもない話だったが、ボクはその真実に、本当に彼女の真心が込められていると…"
    hide screen textbox with dissolve
    menu:
        "信じる":
            stop sound fadeout 2
            scene black with dissolve
            pause 1.0
            show screen nvlbox with dissolve
            nvl clear
            play sound "audio/se/memory.ogg"
            "\n 嗚呼！口から短い悲鳴がこぼれる。{w}生まれて初めて聞いた声だ。" with sshake
            "慌てて塞ぎ、そのまま痛む心臓を押さえた。{w}とてつもない痛みを感じる時自然と傷口を庇うように、身体が本能的に動いてしまう。"
            "手から落としてしまった瓶が床でばらばらになった。そして全身の肌が裂けるように痛い。"
            et "ボクは死んでいく獣のように濡れた床を這い、漏れ出してしまいそうな悲鳴を我慢した。"
            nvl clear
            play sound "audio/se/Heart.ogg"
            "\n 何故？{w}何故こうなってしまった？{w}只幸せになりたかっただけなのに。" with sshake
            "彼女の幸福でボクが幸せになれると信じていたのに。やれることを頑張ってきたと思っていたのに。"
            et "どこから間違えてしまったんだ。いつからこんなことになってしまったんだ。{w}[na]？{w}[na]は、ボクの友達なのに…"
            nvl clear
            scene black with slowdissolve
            play music "audio/bgm/Securett_ver2.ogg" fadein 2.0
            "\n もしかすると間違えていたのはボクだったかもしれない。"
            "ハクはボクが知っている人の中で一番強い人なのに、ボクなんかがそんな人を助けたいと思っていたなんて。"
            "彼女が恵んでくれた最後の慈悲を苦痛として受け入れてしまうなんて。"
            "ハクが正しいと思っているなら、それはきっと正しいのだろう。{w}ハクの歩む道に正義あり。"
            et "時代が彼女を受け入れないなら、ボクはこの時代に主人なんていないと思うんだ。"
            nvl clear
            "\n 暗闇の中で白い光が視界を満たした。{w}目の前でキラキラと輝いていたものは、熱を持って流れ落ちる。"
            $ _skipping = False
            et "彼女に、本当に恋をしていたんだ。ボクは一番大事にしてきた恐れに気付いてしまい、ずっと泣いていた。"
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
            jump day12_hk_2
            return
            nvl clear
        "信じない":

            stop sound fadeout 2
            scene black with dissolve
            pause 1.0
            show screen nvlbox with dissolve
            nvl clear
            "\n ボクは再び立ち上がり汗と混ざった涙を拭いた。{w}そしてそこからもう二度と涙なんて流れないよう目を剥いて前を睨んだ。"
            et "目の前はやはり暗くて、とても幸福があるとは考えられないが、それでもボクは進むしかない。"
            nvl clear
            hide screen nvlbox with dissolve
            scene bg15 with slowdissolve
            pause 1.0
            show screen nvlbox with dissolve
            play music "audio/bgm/Golden Haku.ogg" fadein 2.0
            "\n ハクを信じているほど、彼女の話はどうしても信じられない。{w}大切にした人々を裏切って、完全に一人になるだなんて。"
            et "ハクがそんなことを本気で思っている訳がない。きっとボクに、そして彼女自身に嘘を吐いている筈だ。"
            nvl clear
            "\n 彼女は今まで幼い自分をボクと重ねて見ていたようだ。"
            "ボクに語った言葉は何もかも自分が聞きたかった助言だったんだろう…"
            "ボクはそれに同意している訳ではないのだが、確かに彼女とボクは生まれながらに同じ運命を受けた。"
            et "卑賎な地に生まれた泥塗れの体、永久に怨望する人。{w}しかしボクはその怨望には未練が満ちていることを知っている。"
            nvl clear
            "\n あぁ、彼女に恋をしていたんだな。一番否定したかった恐れを、もう認めざるを得ない。"
            $ _skipping = False
            et "力の抜けた脚を動かして歩き出した。{w}窓から入ってくる白い光を眺めながら、もう二度とそこへ戻れないことを実感した。"
            stop music fadeout 5
            hide screen textbox
            hide screen nvlbox 
            with dissolve
            pause 2
            nvl clear
            $ _game_menu_screen = None
            $ show_quick_menu = False
            hide screen at_frame
            scene black
            with slowdissolve
            $ _dismiss_pause = False
            pause 2
            jump day12_hk_1
            return
            nvl clear

label day12_hk_1:
    $ day = 12
    $ save_name = "day 12, 楽園"
    $ renpy.music.set_volume(0.4, channel="sound")
    play sound 'audio/se/bell 1.ogg' fadein 2.0
    image 12day = Text("day 12",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '12day' at day00 with slowdissolve
    pause 5
    hide expression '12day' with slowdissolve
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
    scene black with dissolve
    pause 1.0
    nvl clear
    hide screen textbox with dissolve
    scene bg02_2 with dissolve
    pause 1.0
    show screen nvlbox with dissolve
    nvl clear
    play music "audio/SE/prologue wind.ogg" fadein 2.0
    "\n 耳が千切れそうなほどに寒かったあの冬、ボクが神殿で初めて迎えた聖夜。"
    "ボクは洗礼の秘跡を見物する人々に揉まれ人酔いを起こしていた。"
    "魔導師たちが州都に結界を広げて、神殿が外部の人の出入りを許す祭りの日。{w}人が多過ぎる。"
    et "寒いのに汗が出て、足が震える。{w}その時、彼女はボクの手を引っ張って走り出した。"
    stop music fadeout 1
    nvl clear
    show black with dissolve
    play sound "audio/se/running.ogg"
    pause 1.0
    scene bg101_2 with dissolve
    "\n ボクたちはできる限り遠く、人の来ない物静かな所まで走った。"
    et "こんな人波の中で手を繋いで走るなんて！{w}ハクは興奮した声で笑う。今年の聖夜祭が楽しいと言っていた。"
    hide screen nvlbox with dissolve
    show black with dissolve
    pause 2.0
    show screen textbox with dissolve
    play music "audio/bgm/golden haku.ogg" fadein 2
    sc "今までは楽しくなかったのかい？"
    show SCG_06 12 with dissolve
    hk_b "聖夜祭は私の父が嫌っててな。それだけだったのさ。"
    hk_b "だから好きになる訳にはいかなかったが、嫌いになるまでの理由もなかった。"
    show SCG_06 1 with fastdissolve
    hk_b "しかしそれももう昔の事になりそうだな。"
    hide SCG_06 with dissolve
    nar "そのくだらない所から眺めた州都の風景が、未だに目に浮かぶ。"
    nar "暗い空を覆い隠すように遠くからうじゃうじゃと見える黒い霧。"
    nar "ボクはそれを見て「怖い」と言ったが、ハクはその下に溢れている灯りを見ては「美しい」と言っていた。"
    show SCG_06 0 with dissolve
    hk_b "何を視たんだ、シーキュレット？"
    sc "その…州都に張られた結界を。"
    show SCG_06 1 with fastdissolve
    hk_b "なら我々は同じものを見たのだな。我々はどちらも生きる人々を見たのだから。{w}なあ？"
    sc "…でもボクはキミの考えている事が理解出来ないよ。"
    show SCG_06 9 with fastdissolve
    hk_b "努力する者に価値は付いてくるものよ。"
    show SCG_06 1 with fastdissolve
    hk_b "それに私達は同じことを考えることは出来なくとも、互いの考え方を理解することは出来るようになるだろうさ。"
    hk_b "そうなれば今日はキミにとっても価値ある日となる。"
    nar "同じ場所で共に冷たい風に触れるボクたちが、一生違う世界を見ながら生きていくことが理不尽だと思った。"
    nar "きっとハクもボクと同じく、恐らくボクが知った以上に世界の残忍さを知っている筈だ。"
    hk_b "少し考えてみたのだがな…"
    show SCG_06 10 with fastdissolve
    hk_b "私の部署にも補佐教が一人いると良さそうじゃあないか？"
    nar "なのにハクが未だこの世に十分な価値を感じているなら、ボクは彼女に祝福されたいと思った。"
    stop music fadeout 2
    hide SCG_06 with dissolve
    show black with dissolve
    pause 3
    hide screen textbox with dissolve
    scene bg10 with slowdissolve
    call place10
    pause 1.0
    show screen nvlbox with dissolve
    nvl clear
    "\n 朝。{w}夜中ずっと寝返りを打っていて布団の中はすっかり冷えていた。"
    "ボクは真っ白に広がった空を見ながら昨日のことを思い出す。{w}もっと正確に言えば、また彼女のことを思い浮かべている。"
    et "ボクは毎朝起きる度に彼女を思い出す。それがボクの日常だ。"
    nvl clear
    "\n しかし一番に浮かんだのが昨日の記憶で、正しく正義を追い求めるハクと汚い殺人鬼がぶつかっていた。"
    "落ち着かないのはボクだけでなく、他の人も同じだった。{w}魔導部が大きな柱を失ってから、彼らを中心にしていた神殿は平常を失った。"
    "人々を支えた神殿が平常を失うと、もうすぐ世界が揺れてしまうだろう。{w}未だに夏は始まってもいないのに、大きな陽炎が燃えている。"
    et "ボクはずっとそこに昇っていそうな太陽を睨んで眉を顰めた。"
    nvl clear
    hide screen nvlbox with dissolve
    scene bg14 with dissolve
    call place14
    pause 1.0
    show screen nvlbox with dissolve
    play music "audio/se/tutorial walking.ogg" fadein 3
    "\n しかし働くしかない、仕方がないだろう。{w}彼女がボクに生き延びる機会をくれたから、生きているからできることをやるべきだ。"
    "だからロッカーに押し込んであるシャベルと袋を取り出さないといけないのに、どうしてもできなかった。{w}手が止まったまま空で震えていた。"
    "浄化部の主教は未だ出勤していない。{w}後ろでは主教の到着を待つ司祭たちが騒々しい。"
    et "息苦しい部室を見回すと、ふと彼らがまるで、とても遠くて小さなもののように見えた。"
    nvl clear
    "\n 彼らは今日死ぬだろう。{w}ボクが知ってしまった真実の重さを今更思い出す。"
    stop music fadeout 4
    "ボクはいつでもそれを口に出し、彼女に罰を与えられる人間だった。"
    et "ハクはボクに逃げる機会を与えたんだ。{w}狭い部室でなく村の広い空気、街一杯の灯りを思い出した。"
    nvl clear
    scene bgw with slowdissolve
    "\n 金はある。柔らかい服を着て美味しい物を食って、温かくて広いベッドで眠れる人生。"
    et "もしかしたら教育院に進んで勉強の機会を得るかもしれない、そんな自分を想像する…"
    hide screen nvlbox with dissolve
    play sound "audio/se/memory.ogg"
    scene bg14 with dissolve
    show screen textbox with dissolve
    pl "なあ。"
    nar "その慌ただしい世界から誰かが話しかけてきた。{w}[na]だ。"
    nar "ボクはそれが誰なのか一目で分かったが、それを寧ろ怪訝に思った。"
    sc "…ん？どうしたの。"
    nar "だから気の抜けた声を出してしまう。"
    play music "audio/bgm/dialogue.ogg" fadein 2.0
    pl "話があるんだ。"
    nar "彼は更に不思議なことを言っている。{w}話？"
    sc "ボクとの話は昨日で終わりだと思ってたけど。"
    nar "彼は暗い顔で外を見ていた。大事な話だと言っている。{w}ボクは彼に従い外へ出た。"
    hide SCG_01 with dissolve
    hide screen textbox with dissolve
    scene bg03 with slowdissolve
    call place03
    pause 1.0
    show screen textbox with dissolve
    nar "彼をもう一度信じてあげようという訳ではないが、敢えて断る理由もなかった。"
    sc "…話ってなんなんだい。"
    nar "全く気にならないが一応聞いてみた。ボクを見つめる彼の目が重い。"
    nar "ボクが先に話し出すと、彼は視線を逸らして考え事をしているように見えた。"
    pl "お前に謝りたくてさ…"
    sc "謝る？"
    pl "今までお前に酷いことをしてしまった。"
    pl "お前を信じてやることだってできたのに、俺は自分のことにだけ気が向き過ぎてお前にとんでもない…"
    pl "嫌なことばっかしちまって、こんなこと言う資格もないよな。{w}本当に…ゴメン。"
    nar "彼は全身を震わせながら話を切った。これは痛ましいほどだ。"
    stop music fadeout 2
    nar "ボクはじっと目を瞬きながら、何と返そうかと頭を回している。{w}一体ボクはここで何と言えばいいんだ。"
    play music "audio/se/no more bell my buddy.ogg" fadein 5
    nar "すると、[na]はボクの手首を掴んだ。" with sshake
    nar "それがあまりにも突然で、彼の手は汗でびしょ濡れで、"
    nar "ボクは思わず怯えた女の子みたいに悲鳴を上げてしまうところだった。"
    play sound "audio/se/hit.ogg"
    pl "お前に無視されたくなかったんだ！お前が俺を騙したことにただ苛ついてただけで…！" with sshake
    pl "でも今はそれがただの八つ当たりだったってことを理解してる、反省してる！"
    pl "これで何かが変わるなんて期待もしてない。{w}友だちに戻れなくてもいい、"
    pl "もう二度と俺を手伝ってくれなくたっていい、挨拶を交わせなくてもいい、"
    pl "顔合わせるのも嫌だってんならそれでいい！" with sshake
    pl "でも俺…俺お前に酷いコトをしてしまったって後悔してるんだ。{w}ホントだよ…"
    pl "だからもう、いい訳にもならないってのはわかってる、でも…謝罪だけでも受け入れてくれないか…？"
    nar "握られた手から震えが感じられる。{w}彼の目は未だに揺れているが、視線を避けてはいない。"
    stop music fadeout 5
    nar "奴の深い呼吸の音が響く。{w}この広い空間に二人だけ…今までは誰かが助けてくれたが、今は誰もいない。"
    nar "危うく膨れ上がった空気が二人を圧迫する。{w}やがて口を開いた。"
    play sound "audio/se/ding.ogg"
    sc "なんで、それをボクに言うんだ…？"
    nar "彼を騙したことには罪悪感を抱いている。"
    nar "彼をここまで追い詰めて、こんなにも壊してしまった者の一人がボクだということも認める。"
    nar "だから彼がボクに鬱憤を吐いた時、残酷な暴力をボクに振るった時、ボクはそれを受けて当然の罰だと思っていた。"
    nar "しかし彼はずっとボクに何かを求めていて、ボクは最後までそれが何か分からなかった。"
    play music "audio/bgm/Haku.ogg" fadein 5.0
    nar "彼とは友達に戻りたかったかもしれない。"
    nar "しかし彼が簡単な言葉でボクに憎悪を表した時、ボクたちの関係が完全に終わったことを理解した。"
    nar "彼はそのような気持ちを感じたくないのか。"
    sc "キミがボクに何をしようが、もうボクにとっては何も関係ない。"
    sc "ボクがキミに怒った理由はボクではない他の誰かに八つ当たりをしたからなんだよ。"
    sc "ハクには手を出さないでくれって言ったじゃないか。{w}彼女はボクの大切な人なんだよ！" with sshake
    sc "ボクたちの事にどうして彼女を巻き込む必要があったんだ？"
    sc "なんで彼女に危害を加えたんだよ、そうすればボクがこの終わってしまった関係を考え直すとでも思ったのかい？"
    sc "いいや、違うね。"
    sc "それら全てに何の関係があるんだ？{w}もう終わったんだよ。ボクはキミから何も聞きたくない。"
    sc "キミが本当にボクの為に謝りたかったなら、それはボクじゃなくてハクに言うべきだったんだ！" with sshake
    hide SCG_01 0 with dissolve
    nar "彼に声を張り上げて、詰まってしまった息を吸う。"
    nar "今初めて本人ではない他人の前で彼女を主教ではなく「ハク」と呼んだ。{w}彼女が「大切な人」だと言ってしまった。"
    nar "再び彼を見た時、[na]は悲しそうで、虚しそうにも見えた。{w}どちらにせよもう怒ってはいないらしい。"
    nar "いつも、彼が今よりもいい暮らしができることを願っていた。"
    nar "ボクが経験した失敗や痛みを彼らが同じく経験してしまうことがないように願っていた。"
    nar "もうそれを隣で見守ってはいられないだろうが。"
    sc "もうじき神殿にとても大きな災いが訪れる。マヤを探し出して逃がしてくれ。{w}あの子には何の罪もないだろ。"
    nar "だからボクにできる最大限の言葉を残して立ち去る。{w}できる限りの速さで走った。"
    nar "手はとっくに振り切ったが、強く握られすぎて未だに痛みを感じる。"
    nar "もう彼との思い出よりこの痛みの印象の方が強く残るだろう。"
    hide screen textbox with dissolve
    play sound "audio/se/running.ogg"
    pause 1.0
    show screen nvlbox with dissolve
    nvl clear
    "\n ボクはハクが犯した罪を知って、彼女がもうボクの記憶の中に存在する完璧な女性ではないことは分かっている。"
    "長く追っていた夢が虚像だってことを知ってしまった。"
    "ボクが長く知っていた、想像していた彼女が実際と異なることも分かった。この心さえも偽物なのかもしれない。"
    et "しかしどうしようもなく、彼女のことを想ってきた時間が長過ぎた。"
    scene black with dissolve
    nvl clear
    "\n ハクが探している人がボクではなければどうしよう。"
    "もしボクがこの選択を後悔し、互いに失望し、彼女との思い出さえも何もかも痛みに変わってしまったらどうしよう。"
    et "今だってこんなことで悩んでいる。"
    nvl clear
    "\n ダメだ、ダメだ！{w}弱気な自分を窘めた。でなければ今すぐにでも立ち止まるか、転んでしまいそうだった。" with sshake
    "一体どういう訳で、どんな魅力があってボクは、よりにもよって彼女に心が惹かれてしまったんだ。"
    et "彼女は、ハクは、"
    nvl clear
    hide screen nvlbox with dissolve
    play sound "audio/se/memory.ogg"
    scene bgw with slowdissolve
    show screen nvlbox with dissolve
    "\n 文を書く前にペンを回す。{w}長い話をする前には必ず一度目を閉じる。{w}そんな小さな癖さえも特別に見えていた。"
    "ボクの名前さえも、キミの口から出てくると全く別の意味を持って聞こえるようだと、そんなことまで思っていたんだ。"
    et "特別さに溺れた人は愚かで卑賎なんだな。"
    stop music fadeout 5
    hide screen nvlbox with dissolve
    pause 1
    scene bg02 with dissolve
    pause 1
    show screen place_day12_hk with dissolve
    hide screen place_day12_hk
    $ place = renpy.call_screen("place_day12_hk")

label day12_hk_end:
    show screen place_hkBR
    show screen place_day12_hk
    with None
    hide screen place_hkBR
    hide screen place_day12_hk
    with dissolve
    hide screen nvlbox with dissolve
    pause 2
    scene bgw with dissolve
    show Blsnow zorder 0 with slowdissolve
    pause 1.0
    nvl clear
    "{color=#000000}{size=0}{k=0}\n さぁ私たちは真に幸せに生きていこう。怨みを抱く人々の中でも怨むことなく。{/k}{/size}{fast}{/color}{nw}"
    image day12_3 = Text("{color=#000000}さぁ私たちは真に幸せに生きていこう。\n怨みを抱く人々の中でも怨むことなく。{/color}", text_align=0.5, slow=True, size=36)
    if config.language == "English":
        image day12_3_en = Text("{color=#000000}Now let us live in true bliss together.\nWe alone shall forgive and forget whilst surrounded\nby those who cling to their grudges.{/color}", slow=True, size=27)
        show day12_3_en at truecenter
    elif config.language == "SimplifiedChinese":
        image day12_3_cn = Text("{color=#000000}那么，就让我们真正幸福地生活下去吧。即便在心怀怨怼的人群之中亦无怨无悔。{/color}", text_align=0.5, slow=True, size=28)
        show day12_3_cn at truecenter
    elif config.language == "Korean":
        image day12_3_kr = Text("{color=#000000}우리 진정 행복하게 살아가자. 증오 속에서도 증오 없이.{/color}", text_align=0.5, slow=True, size=36)
        show day12_3_kr at truecenter
    else:
        show day12_3 at truecenter
    pause 8
    show ctc onlayer screens at ctc:
        xalign 0.5
        ypos 420
    $ _dismiss_pause = True
    $ renpy.pause()
    $ _dismiss_pause = False
    hide ctc onlayer screens
    hide day12_3
    hide day12_3_en
    hide day12_3_cn
    hide day12_3_kr
    with gjdissolve
    "{color=#000000}{size=0}{k=0}\n 怨みある人々の中で暮らしていこう。怨むことなく。{/k}{/size}{fast}{/color}{nw}"
    image day12_4 = Text("{color=#000000}怨みある人々の中で暮らしていこう。\n 怨むことなく。{/color}", text_align=0.5, slow=True, size=36)
    if config.language == "English":
        image day12_4_en = Text("{color=#000000}Let us live among those who fester with resentment.\n Free of malice.{/color}", text_align=0.5, slow=True, size=27)
        show day12_4_en at truecenter
    elif config.language == "SimplifiedChinese":
        image day12_4_cn = Text("{color=#000000}就让我们在心有怨怼的人群中生活下去吧。\n 毫无怨怼地。{/color}",text_align=0.5, slow=True, size=28)
        show day12_4_cn at truecenter
    elif config.language == "Korean":
        image day12_4_kr = Text("{color=#000000}미워해야 할 사람 속에서도 미움을 버리고.\n 우리 자유롭게 살아가자.{/color}", text_align=0.5, slow=True, size=36)
        show day12_4_kr at truecenter
    else:
        show day12_4 at truecenter
    pause 6.5
    show ctc onlayer screens at ctc:
        xalign 0.5
        ypos 420
    $ _dismiss_pause = True
    $ renpy.pause()
    $ _dismiss_pause = False
    hide ctc onlayer screens
    hide day12_4
    hide day12_4_en
    hide day12_4_cn
    hide day12_4_kr
    with gjdissolve
    hide screen TrackCursor
    hide screen grumble_cg082
    pause 1
    hide screen nvlbox with dissolve
    scene bg101 with dissolve
    call place101
    pause 1.0
    show screen textbox with dissolve
    play music "audio/SE/prologue wind.ogg"
    nar "ボクはいつものあの場所に辿り着く。ゴミを捨てる穴から死体の臭いがする。"
    nar "寒いはずなのに汗が吹き出し、脚は震えている。"
    nar "禍が集う州都の中心である神殿。{w}あらゆる命は結局、この窪みを通って生まれた所へ戻るのではないのかと思う。"
    nar "誰もが口を合わせて神を敬うが、彼らの語る神と言う輩は様々な災いを降らし人を害する。"
    nar "そんな理不尽だらけな人生にも価値があるなら、人間はそれを探し出すべきだろう。"
    hide screen textbox with dissolve
    pause 1
    play sound "audio/se/door close.ogg"
    scene bgw with dissolve
    show screen textbox with dissolve
    nar "それは例えるなら、光を目に受け入れることだ。"
    stop music fadeout 3
    scene bg100 with slowdissolve
    nar "彼女はそこに立っていた。{w}沈まない太陽の燦爛とした呪いを拒まずにその身に受け入れて、黄金の瞳を光らせる。"
    nar "白っぽい色のステンドグラスが輝いて、高い天井に垂れた長い影に埃が漂う。"
    nar "ボクはその光と真っ直ぐ向き合おうと目を大きく見開いた。"
    show SCG_06 0 with dissolve
    play music 'audio/bgm/haku.ogg'
    hk_b "…君が来るとは思ってもいなかった。{w}君が最後まで私の事を信じてくれたら良かったのに。"
    nar "ハクは顰め面を隠そうともしていない。一歩歩くと剣が床に引き摺られる。"
    nar "彼女からは死体の臭いが漂っていた。"
    nar "心臓が裂けてしまうほどに震える。本気で彼女はやってしまう気だ。"
    nar "ボクと会う為ではなく、手に入れた供物を投げ入れる為にここに来たんだ。{w}ハクは手を振って赤い血を払った。"
    show SCG_06 8 with fastdissolve
    hk_b "実感が湧くだろう。{w}どうだ？シーキュレット。これが禍から生き残る為に人間が創り出した禍だ。"
    hk_b "これから皆が全ての始まりとなる地へと戻り、現人類の母である禍の懐に還るだろう。"
    hk_b "そしてそれらを叶える為には直接その魂を罪に陥れる為の審判者が要る。"
    show SCG_06 0 with fastdissolve
    hk_b "どうだ、私が怖いか？"
    nar "ハクは低く冷たい声で問う。{w}今まではあの声が望む通りに従順に頷くだけだった。"
    nar "ボクはこれから彼女に、自分の言葉を伝えるべきだ。{w}彼女が望んでいない、ボクの言葉を。"
    sc "…綺麗だと思う。"
    sc "キミの目、まるで初めて見た様な気分だ。{w}やっぱり光の下がキミには似合うよ、ハク。"
    show SCG_06 12 with fastdissolve
    nar "ハクは驚いたように黄金の目を見開いて、そしてそっぽを向きじっと別の所を見ている。"
    nar "ボクも彼女に続きこの場所を見渡した。"
    nar "ハクがボクとの関係を絶って、この空間の魔法は解けた。"
    nar "年季の入った崇高さが感じられた柱はただの古びた石になり、"
    nar "厳粛な沈黙は陰鬱な雰囲気に、慣れたはずの鼻には再び腐った悪臭が感じられた。"
    nar "この当然の事実が悲しく感じられるなんて、"
    nar "知らないうちにこの空間はボクにとって聖域になってしまったようだ。"
    show SCG_06 0 with fastdissolve
    hk_b "私は君に選択の機会を与えた。しかし君は何を選んでここに来た？{w}愚かな死か？"
    sc "キミを選んだのさ。{w}キミが自分自身でさえ望んでいないことをしているから。"
    sc "だからキミともう一度話がしたくて。"
    show SCG_06 2 with fastdissolve
    hk_b "ハァ…一体何を根拠にそう思うのだ？{w}君が私ではない様に、私もまた君ではないのに。"
    hk_b "本気で君が私を説得できるとでも思うのか？"
    sc "…勿論、ボクたちは全く違う人間だ。{w}でもキミの幸せとボクの幸せは繋がっている。"
    nar "仮にボクと彼女が違う考えを持っているとしても、ボクはボクたちの記憶を思い浮かべる。"
    nar "それは過去を偲ぶ為でなく、それを大事にする為だった。"
    sc "ボクは他人に尽くすために生まれたんだなあって、思ってたんだ。"
    sc "自分自身の為に生きる事なんて不可能だと思ってた。"
    sc "でも今なら解る。{w}ボクは今この時を生きるために生まれたんだ。"
    sc "キミがボクに機会を与えてくれた様に、キミにだって選択の機会は与えられるべきだろう。"
    sc "本当に名前一つにその人の運命や生命なんかが宿ると言うなら、"
    sc "ボクに命を与えてくれた人は他でもない、キミだよ。"
    show SCG_06 0 with fastdissolve
    hk_b "………"
    sc "剣を降ろそうよ、ハク。{w}こんなのキミが望んでいた事じゃないだろう。"
    sc "ボクの知るキミは自由で、正義に満ちた人だ。他の誰かの命令で人を殺すような人じゃあない筈だ。"
    hk_b "………"
    sc "…どうしてボクらがここで、毎日同じ時間に遭っていたのか、最初はそれすら自分の為だと思ってたんだ。"
    nar "ボクが一歩近付くと、ハクも動き出す。{w}ここで一番日が当たる所から足を進め、再び陰のできた所に入る。"
    nar "ボクが彼女にとって陰になったような気分だ。"
    sc "でもこの場所は、実はキミの為の場所だったんだろう？帰るための場所が欲しかったんだろう。"
    sc "でも、{w}でもねハク、実は帰らなくたっていいんだ。"
    sc "どうして必ずどこかに戻らなきゃいけないんだ？{w}進もうよ！"
    sc "もっと広い世界を旅して、歩きながら生きようよ。"
    sc "これからはボクが道を作るから…！" with sshake
    stop music fadeout 2
    hk_b "……シーキュレット。"
    hide SCG_06
    hide screen textbox
    with dissolve
    scene black with dissolve
    pause 1.0
    play sound "audio/se/slap.ogg"
    nvl clear
    "{nw}" with sshake
    pause 1
    show screen textbox with dissolve
    nar "斜めに顔を上げてボクを見つめるハクが、長くて浅い息を吸ったようだった。"
    nar "沈まない太陽のせいで時間が止まったように、もしくはとても遅く流れているように見える。"
    nar "そしてハクは剣を握った。風を裂く音と共に目の前が赤く、暗く光った。"
    nar "冷や汗が首と背中に流れ、ボクは何度かふらついた。{w}その度にぼたぼたと水の落ちる音が聞こえた。"
    sc "ぅぐ…" with sshake
    play music "audio/se/Heart.ogg"
    nar "喉と鼻から熱くて生臭い物が上がってきて、咳のようにそれを吐き出してしまう。" with sshake
    nar "震える喉から血の味がする。本来なら悲鳴を上げていただろう。"
    nar "ボクは状況を理解しようと頭を上げたが、視界があまりにもぼやけて暗く揺れた。"
    nar "全てが朦朧としている。{w}その闇の中で白や、黄金のような光が丸く溢れ出ていた。"
    sc "つ、き…？"
    stop music fadeout 1
    hk_b "いいや、月はもう二度と昇らない。"
    scene bg100 with slowdissolve
    play sound "audio/se/memory.ogg"
    nar "ハクの声が聞こえて目を瞬いた。{w}視界に入ったハクは冷静な顔で手を震わせていた。"
    nar "ここは全然寒くないのに。"
    hide screen textbox with dissolve
    pause 1
    show cghk04 with slowdissolve
    pause 2
    show screen textbox with dissolve
    play music "audio/bgm/Haku2.ogg" 
    hk_b "私が贄を捧げ、この地から大災害を払わぬ限りは。"
    nar "彼女はとても近くにいて、未だ剣を握っている。"
    nar "ボクはその頑強さを見て彼女の生がまだ完璧で、燦爛と輝いていると分かった。"
    nar "いつかこのような苦痛を味わった時に彼が語った言葉を思い出した。"
    nar "嗚呼、ボクが悪魔だったんだ。"
    nar "ボクがキミの完璧になるべき人生に傷を残して、正しくない道へ行けってキミを惑わしていたんだ。"
    nar "だからボクたちは今日もここに来たんだ。{w}ボクを消して、キミが完璧な「英雄」になる為に。"
    hk_b "…私の本当の気持ちが此処にあるのだと、君が信じてさえくれたのなら。"
    nar "ハクはもう迷わずにボクに剣を構えた。その剣は昨晩のように脆くなくて鋭い。"
    nar "首の傷のせいで悲鳴が上げられないことだけが、彼女がボクに与える配慮だ。"
    hide screen textbox with dissolve
    pause 2
    scene black with dissolve
    show screen textbox with dissolve
    nar "やっぱりこうなるんだね。{w}知ってたよ。"
    nar "ボクが彼女を助けたいと思う心は、単なる自分勝手な欲ってことくらいは。"
    nar "でももし、叶うならいいなって、そう思っただけなんだ。"
    nar "部室のがらんとした風景が脳裏に浮かぶ。"
    nar "神殿に来る前まで働いていた港の村の生臭くて冷たい空気を未だに肌で感じる。"
    nar "まだボクの中に恐れが残っていた頃、ボクはそこに帰る想像をしたりもしていた。"
    nar "ボクはキミの言った通り、生きている限り新しい友達も作れるし、マシな方法で稼げるし、"
    nar "ボクだけの楽しみを探しながら生きていけるだろう。"
    nar "でもそうなったら、キミの髪は誰が梳かしてくれるんだ？"
    scene bgw with dissolve
    pause 1.0
    nar "誰がキミと共にご飯を食べて、誰が毎朝キミを起こしてくれるんだ？"
    nar "ボクには他の縁が出来るだろうけど、キミはこれから過ごすであろう夜がずっと、うんと寒くて寂しいだろう。"
    nar "ボクはそれが心配なんだ。"
    nar "だからボクはここに来たことを一生後悔しない。"
    scene bg100 with slowdissolve
    nar "体が力を失い崩れたが、ボクは床に転びはしなかった。{w}恐らくハクが支えてくれたんだろう。"
    nar "曖昧な闇の中でもボクを包んだのが彼女の手だと分かった。"
    nar "震えもなく硬い手袋の向こうから、微かな温かさを感じた。"
    nar "ぼやけた網膜にハクの輪郭が映る。"
    nar "ボクはその顔が少しでも鮮明になって欲しいなと思って、記憶の中にある彼女の姿を思い出す。"
    nar "名前を呼ぶ為に、口を動かした。"
    nar "声には出なかったんだろうが、その意味が、どうか。伝えられたらいいな。"
    scene black with dissolve
    play sound "audio/se/slap.ogg"
    nar "やがて最後に、心臓に冷たい刃が刺さる。"
    hide screen textbox with dissolve
    pause 1.0
    show screen nvlbox with dissolve
    nvl clear
    stop music fadeout 3
    "\n シーキュレット・レイフは叫ぶことなどなくそのまま死んだ。{w}そして同時にハク・エカルランは剣を落とし、空いた手でその体を抱いた。"
    "ぼそぼそした髪に触れ、早くも冷えていく体から自分の心拍だけを聞いた。"
    "その下にできた血溜まりを見つめる。{w}そこに映った女性は蒼白で惨たらしいが、もはやそれこそ世を救う英雄の姿であり。"
    et "ハク・エカルランは長く深呼吸をして、再び剣を手に握った。{w}そして外へ進む。"
    pause 1.0
    hide screen nvlbox with dissolve
    scene bgw with slowdissolve
    pause 1.0
    show screen nvlbox with dissolve
    nvl clear
    "\n 大きく開いた扉が外からの光を受け入れ、外で機を待った烏が飛び込む。"
    "どれだけその光は眩しいか、四方へ散ったその羽毛は真っ白。"
    et "陰った闇の中、真っ黒の烏共が死体を啄む。{w}ハク・エカルランはしばらくそれを眺めては、もはや再び振り返らないように首を回す。"
    hide screen nvlbox with dissolve
    play sound "audio/se/door close.ogg"
    pause 1.0
    scene bg101 with dissolve
    show screen nvlbox with dissolve
    nvl clear
    play music 'audio/se/tutorial walking.ogg' fadein 5
    "\n そして光のある外へ歩き出した。{w}禍の集まる神殿、その中心なる窪みを引き裂き、血塗れの体で外へ出た。"
    "もはやこの世の全てが彼女にあろう。栄光と名誉、賛美される生、父の評価。"
    $ _skipping = False
    et "太陽は正に一歩を踏み出した女王たる者の誕生を称えて、燦爛と輝く。"
    hide screen nvlbox with dissolve
    stop music fadeout 2
    pause 1
    scene black with dissolve
    pause 3.0
    play music "audio/bgm/title.ogg" fadein 2
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
    $ persistent.hssh_end_2 = True
    jump end_hk

label day12_hk_end2:
    pause 2
    $ day = 0
    $ save_name = "day 0, 楽園"
    show screen at_frame with dissolve
    scene black with slowdissolve
    pause 1
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    $ _game_menu_screen = 'preferences'
    nvl clear
    scene bg101_1 with slowdissolve
    call place_t_9
    pause 1.0
    show screen textbox with dissolve
    sc "………"
    sc "…はあ。"
    sc "そこに居るのは分かってますよ。"
    play music "audio/bgm/haku.ogg" fadein 4
    show SCG_06 4 with dissolve
    hk_b "…ほぉ、私に気付くとは。{w}ガキ臭い若造かと思いきや、見かけよりかは頭が冴えるな。"
    sc "気付くも何も、数日前からずっとボクに付きまとってるだろ……！" with sshake
    show SCG_06 9 with fastdissolve
    hk_b "君が偶然私の尻尾を見てしまった様だったので、後をつけさせてもらったまでよ。"
    show SCG_06 8 with fastdissolve
    hk_b "フン、で？{w}如何する心算かね？私が君を観察した所…"
    hk_b "無暗に他人に干渉するような軽率さはないが、正しさを語れる程賢くも無さそうだな。"
    hk_b "此の儘君の悪足掻きを見守るのも面白そうだが、君が望むので有らば恐るるべき真実を教えてやろうではないか…"
    show SCG_06 10 with fastdissolve
    hk_b "ハハハ！"
    sc "キミが言わなくとも、ボクはキミが誰だか知ってるぞ。"
    show SCG_06 11 with fastdissolve
    hk_b "決め付けるには未だ早いぞ？傲慢は常に人の命を…"
    stop music fadeout 2
    sc "この悪霊！" with sshake
    play sound "audio/se/ding.ogg"
    show SCG_06 5 with fastdissolve
    hk_b "ふぇ？"
    sc "ハク主教の身体を使って何を…{w}何をするつもりかは知らないけど、オマエの思惑通りにはさせないぞ！"
    pause 1
    hide screen textbox with dissolve
    hide SCG_06 with dissolve
    show cghk05 with slowdissolve
    pause 2
    show screen textbox with dissolve
    play music "audio/bgm/name select.ogg" fadein 2
    hk_b "ちょちょちょちょい、まだ喋ってる最中…"
    sc "うるさいっ！" with sshake
    hk_b "うあっ！{w}適当に塩撒けば何にでもなるってモンじゃあないんだぞ、ぺっ！ぺっ！" with sshake
    hk_b "真実を教えてやるっつってんだろうが！"
    sc "何を語るつもりなんだ？{w}い…いっとくけど、ボクだって先週からこの神殿の司祭なんだからな…！"
    sc "あまり舐めるなよ…{w}はっ、近寄るな！"
    hk_b "そんな事を言われちゃ哀しいな。{w}当然君の事は知ってるさ、シーキュレット・レイフ。私は君の主教ではないか。"
    hk_b "それに君の事が大層気に入りそうなのだよ。{w}君が毎晩この場所で私の話し相手になってくれるのなら、だが…"
    hk_b "私はお喋りなもんでな。"
    hide screen textbox with dissolve
    pause 2
    hide cghk05 with slowdissolve
    show screen textbox with dissolve
    sc "な…なにを馬鹿なことを…ここは立ち入り禁止の場所だぞ、ボクがそんな事に付き合うはずがないだろ…！"
    sc "ちょっ、どこ行くんだよ！"
    hk_b "君も一緒に来るのだよ。勝手に付いてきたまえ。"
    sc "ぼ、ボクをどこに連れてくつもりだ…？"
    show SCG_06 10 with dissolve
    $ _skipping = False
    stop music fadeout 2
    hk_b "君……酒はイケるか？"
    hide screen textbox with dissolve
    hide SCG_06 10 with dissolve
    pause 2
    $ _game_menu_screen = None
    $ show_quick_menu = False
    hide screen at_frame 
    with slowdissolve
    scene bgtitle with slowdissolve
    pause 5
    scene black with slowdissolve
    nvl clear
    pause 2
    $ MainMenu(confirm=False)()
    return

label day12_hk_2:
    $ day = 12
    $ save_name = "day 12, 楽園"
    $ renpy.music.set_volume(0.4, channel="sound")
    play sound 'audio/se/no more bell my buddy.ogg' fadein 2.0
    image 12day = Text("day 12",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '12day' at day00 with slowdissolve
    pause 5
    hide expression '12day' with slowdissolve
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
    scene black with dissolve
    pause 1.0
    nvl clear
    hide screen nvlbox with dissolve
    pause 2
    scene bg03_2 with slowdissolve
    call place03
    pause 1.0
    show screen nvlbox with dissolve
    play music "audio/bgm/dream.ogg" fadein 2.0
    "\n こんばんは、夜分遅くに申し訳ありません。{w}ただ、ただもう耐え切れなかったものでして。"
    et "彼女が罪人だという事実を知って欲しいのです。それは一人で背負うにはあまりにも重い罪でございます。"
    nvl clear
    "\n ボクは昨年の秋、彼女と出会いました。{w}共に過ごしてきた時間は貴方や他の方々に比べますととても少ないのですが、"
    "他人は知らない彼女の罪をボクだけが知っているのです、年月の長さなんて関係ございません。"
    et "誰もが彼女を正しく、美しい人とだけ知っていますが、ボクは彼女のことを真に知っております。{w}彼女は大胆で、自己中心的な人です。"
    nvl clear
    "\n 常に他人に教えを与えようとしている癖して自力では行動する勇気を持てない人です。{w}自身が与えた影響に責任が取れない人なんです。"
    "彼女に出逢って以来、ボクの中の宗教は消えました。人を神として崇めていた訳ではありません。"
    "ただボクはもう神を信じられなくなったのです。{w}州都で生まれて育った大体の人々と同様、祈れば願いを叶えてくれるという期待が持てなくなった。"
    et "彼女はボクに街や、海の向こうや、月へ行こうと旅の約束をしたのですが、それは実際に叶ったと思いますか？"
    nvl clear
    "\n ボクは期待によって傷付いてしまう事が怖いんです。"
    "ボクが今まで彼女を否定してきたのは、彼女が進むべき道をボクが共に歩めないと解っていたからです。"
    et "ボクにどんな影響を与えてしまったのかを、彼女自身も知っている筈です。{w}しかしボクがこれからどこへ進むかは分からないのでしょうね。"
    nvl clear
    "\n 恐れていた通りもう彼女と共に居ることは出来ないし、彼女の今後を応援することも出来ないし、"
    et "ボクはハクに恋をしてしまいましたが、他人に選択や考えを押し付けて逃げる事も出来ません。"
    nvl clear
    "\n ボクが女の身でありながら彼女に恋をしたのは、彼女が同性愛者だからではありません。"
    "彼女の正義を疑った訳でもなく、虐殺犯である彼女を軽蔑した訳でもございません。"
    et "彼女はもう恐れない。{w}心の拠り所など要らないのです。ただ独りでも清く、美しい人なんです。{w}ボクはそれに耐えられなかった。"
    nvl clear
    "\n 彼女が選んだ道に正義があり、ボクにその道を共にする事は出来ないけど、それが英雄の行くべき道と分かっております。"
    "だから貴方に今こうやって告げているのです。"
    et "この暗い廊下に来ると、まだ世界に夜があったあの頃に戻ったような気分になりますね。"
    nvl clear
    "\n あぁ…目眩いがするなぁ。{w}なんでこんなに興奮してんだろ、ボク…"
    "彼女はこれからも正義を成す人でしょう。そんな彼女に今までの罪は重すぎます。"
    et "その罪を分かって頂きたい。{w}彼女の身を清めて頂きたい。{w}それだけです。"
    nvl clear
    "\n 貴方を責めようとして来た訳ではございません…彼女がもう過去の苦しみや愛を記憶する事もないんです、だからボクの憎悪は意味を成さない。"
    stop music fadeout 2
    et "ただ、ボクだけがこの罪を告げることが出来ます。{w}この地上で、ただ一人、ボクだけが、彼女から真実を聞いた人間なのですから。"
    hide screen nvlbox with dissolve
    pause 1.0
    show screen textbox with dissolve
    nar "一気にあまりにも多くの言葉を吐き出した唇がか細く震える。{w}廊下には依然としてボクしかいない。"
    nar "誰一人この前を通らない。"
    play sound "audio/se/r18 2.ogg"
    hide screen textbox with dissolve
    pause 1
    show cghk6 with slowdissolve
    pause 2
    nvl clear
    show screen textbox with dissolve
    sc "…では、失礼致しました。{w}枢機卿様。"
    nar "ボクは扉の前に立ったまま深くお辞儀をした。そうしてからその場を離れるつもりだった。"
    play sound "audio/se/door close.ogg"
    nar "しかし再び顔を上げると、扉は開いていた。"
    nar "僅かに開いた陰気な扉の隙間からは当然ながら光は漏れていない。"
    nar "代わりに真っ白な手がその間を通って出てくる。"
    nar "ボクはその手に殴られでもしたかのようにくらっとする。"
    play music "audio/se/Heart.ogg" fadein 5
    nar "しかし手は袋を一つ持ったまま止まっていて、ボクは両手を掲げ丁寧にそれを受け取った。"
    nar "その間男性の声が聞こえたかどうかは分からない。"
    nar "その手の主が本当に枢機卿であったのかも分からない。{w}ただ掌にカタチの感じられる物体が転がる。"
    stop music fadeout 2
    hide cghk6 with dissolve
    hide screen textbox with dissolve
    scene black with slowdissolve
    pause 1.0
    show screen textbox with dissolve
    nar "袋の中には銀貨が入っていた。"
    sc "…ぁ。"
    sc "あぁ……" with sshake
    hide screen textbox with dissolve
    scene black with dissolve
    pause 2.0
    play sound "audio/se/running.ogg"
    pause 3
    play music "audio/se/no more bell my buddy.ogg" fadein 5
    scene bg11 with dissolve
    show screen textbox with dissolve
    nar "一人で神殿を歩き回る。{w}古い建物の隅々がボクと彼女で構成されていた。"
    nar "神殿は何気ない会話を分かち合いながら、笑い声でボクの頭を乱す。{w}ボクはそこに差す影を避ける為に逃げた。"
    nar "熱い目の穴から時折水が流れ落ちる。脳もゆっくり溶け落ちる。"
    nar "彼女を欲していた。"
    nar "全身から感じる欲はとても熱く、鋭く、何時かは手も出せない程に大きくなってボクを殺すだろうと思っていた。"
    hide screen textbox with dissolve
    pause 2
    stop music fadeout 2
    scene bg02 with dissolve
    call place02
    pause 1.0
    show screen textbox with dissolve
    play music "audio/SE/prologue wind.ogg" fadein 2.0
    nar "そのほとぼりも朝になると冷めていった。夜中ずっとボクを苦しめていた熱も嘘のように下がる。"
    nar "朝一で街に向かったボクは古い本を真似するように銀貨を取り出し、ハクがくれたものでない服を買って身に纏う。"
    nar "ヒリヒリする顔に冷水を浴びせ、神殿に向かう見慣れた道を歩いた。"
    nar "もう誰も「駄目だ」という言葉で責める事は無い。"
    hide screen textbox with dissolve
    pause 2.0
    scene bg01 with dissolve
    call place01
    pause 1.0
    show screen textbox with dissolve
    nar "時間は午前九時。{w}主教たちは早くからの会議の為に通路を歩く。"
    nar "彼らが並んで前を歩けば、すべての司祭は祈るような姿勢で頭を下げる。"
    nar "当然の様にいつもの日常が目の前に広がる。"
    nar "癖っ毛一つもない高く結んだ白い髪、シワ一つない修道服。見慣れた優雅な姿勢。"
    nar "その美しい女はただ一つの罪も刻まれた事が無いかの様に軽い足取りで歩みを進める。"
    stop music fadeout 2
    sc "御覧下さい、あの女こそが禍でございます。"
    nar "はっきりとした声が響くと、その場の全ての人が動きを止める。"
    sc "真っ白なあの白髪に、あまりにも突然新設部署の座に就いた事まで。{w}何故誰も疑わないのですか？"
    sc "あの女が神聖術を使う姿を一度でも直接見た事がありますでしょうか？"
    sc "彼女には聖痕がない、全身で神の存在を否定しているのですよ。"
    sc "それだけではございません。{w}アルネ・アルタナータを殺したのもあの者です。"
    sc "彼女は神の恩賜を頂けなかった反逆者であり、薄汚い殺人鬼なのです。"
    sc "…ワタシには分かります。"
    play sound "audio/se/luggage down.ogg"
    nar "顔を覆っていた黒い布を捲り、彼女を見る。{w}ハクと目が合う。"
    play music "audio/bgm/haku.ogg" fadein 2.0
    sc "当然他の主教たちもこの事実を知っていたはずです。"
    sc "何故このような真実が今まで伏せられていたのでしょうか？"
    sc "これは明白な罪です。{w}これ以上あの詐欺師の祝福を受け、命令に従う者を無くすべきです。"
    sc "ワタシの言葉が疑わしいのであれば今、ここに行政部の者を御呼び下さい。"
    sc "あの禍の服を剥ぎ取り、座から降ろしましょう。"
    sc "然るべき罰を受けさせ、皆の手で正義を成しましょう！" with sshake
    nar "大勢の人が扇動に流される。"
    nar "ボクらの思い出がボクだけのものとなり、密かに抱いた夢を壊すしかないのなら、"
    nar "ボクは彼女に憎まれてでも憶えていてほしい。"
    nar "ハクはとても不安げに、こんな状況を全く予想出来ていなかったかの様な貌でボクを睨む。"
    nar "裏切り者を見る目だ。"
    nar "ボクに裏切られたと思ったんだろうな。{w}これがボクを恋しく想った罰だよ。"
    show SCG_06 13 with dissolve
    show SCG_06 at huruhuru
    hk_b "ちょっと…何をするつもりですか、離せ…！！"
    nar "直ぐに行政部の司祭が彼女を捕える。"
    nar "その気になれば押さえつける手くらいすぐ振りほどけるはずなのに、ハクは思いっきり抵抗できていない。"
    nar "口調が妙に丁寧だ。{w}他の主教達も戸惑うのみで、迂闊に乗り出せていない。"
    hide SCG_06 with dissolve
    nar "何人かは来るべき時が来たと言わんばかりに後ろへと身を引く。"
    nar "妙な夢から醒めたかのように、鮮明になった視界がグルグルと回る。"
    sc "嗚呼、贖罪の時来たり！これで正義は護られる事でしょう！" with sshake
    nar "この全ては、彼女があんなにも護りたかった正義の為。"
    nar "これで彼女の大事な秘密が一つ残らず曝されるだろう。"
    nar "あちこちで響く女の悲鳴、群衆の歓声！{w}ボクは声を上げて笑う。"
    nar "その反動で胸が揺れるが、もう以前みたく不快にはならない。"
    nar "ボクは神に身を捧げた一人の司祭として、最後の使命を終わらせた。{w}これもまた大義の為だ。"
    stop music fadeout 4
    nar "私的な感情など、一切、無かった…"
    show SCG_06 5 with dissolve
    play sound "audio/se/hit.ogg"
    hk_b "シーキュレット補佐教！君は本気ですか…！{w}シーキュレット！！" with sshake
    sc "………"
    hide SCG_06 with dissolve
    nar "午後になると、外の光はさらに強まる。この光がもうじき世界を焼き消すだろう。"
    nar "ボクは段々と遠くなっていく女を見つめる。{w}塩っ気のある風が頬を殴る様な感覚があった。"
    hide screen textbox with dissolve
    scene bgw with slowdissolve
    pause 1
    scene bg0000 with slowdissolve
    show screen textbox with dissolve
    play music "audio/se/prologue wind.ogg" fadein 2
    nar "海から吹いてくる風に似ている。幼い頃働いていた港町の風景を思い出す。"
    nar "もうじき夏が来る。{w}汚染された海に腐敗物がどんどん上がってくる時期だ。"
    nar "港じゃあ歳や性別に関係なく仕事が出来ますよ。"
    nar "こんな季節だとワタシ共の様な商人達は、養殖場で育てた魚を市場に売ったりしているんです。"
    nar "そうすると船に乗ってきた船員たちが比較的安いお値段で魚が買えますからね。"
    stop music fadeout 2
    $ _skipping = False
    nar "申し遅れました。{w}ワタシの名は、商人のトゥルーディ・レイフ。"
    hide screen textbox with dissolve
    pause 3.0
    play music "audio/bgm/title.ogg" fadein 2
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
    $ persistent.hssh_end_2 = True
    jump end_hk2
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
