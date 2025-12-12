label day6_rkn:
    $ day = 62
    $ save_name = "day 6, 朝, 楽園"
    play sound 'audio/SE/bell 2.ogg' fadein 2.0
    image 6day = Text("day 6",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '6day' at day00 with slowdissolve
    pause 5
    hide expression '6day' with slowdissolve
    stop sound fadeout 1.0
    pause 3.0
    show screen at_frame  with dissolve
    play music 'audio/bgm/dream.ogg'fadein 5.0
    pause 4.0
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    $ _game_menu_screen = 'preferences'
    $ renpy.music.set_volume(1, channel="music")
    scene bg12
    show screen TrackCursor
    show screen grumbleBG12
    with slowdissolve
    pause 1
    show screen nvlbox with dissolve
    br "\n 夢。{w}またもや俺は真っ赤な空の下泥じみた地面に立っている。{w}俺はこの嫌悪してやまない場所に安心感を覚え始めている。{w}{nw}"
    extend "\n頭を叩くような頭痛もない。部署に立ち入る時の視線がない。俺を圧迫する未来も、俺を惨めにする過去もない。{w}{nw}"
    extend "\nここに居るのはただ彼女と俺だけ。{w}{nw}"
    extend "\n彼女は神々しい光を背負い、世に存在する全ての美しさを清廉潔白な身体に詰め込んでいる俺の気持ち悪い天使。{w}{nw}"
    extend "\n彼女が存在するここに他でもない俺が居られるなんて、どれだけ幸運なんだろう。{w}俺はその感謝の気持ちを示すため喉元に詰まる吐き気に耐えながら笑顔で応える。"
    nvl clear
    br "\n どうにか吊り上げた口端が震える。額には消せない皺が寄り、喉からはどれだけ耐えようが結局汚い音が鳴る。{w}{nw}"
    extend "\n冷や汗がだくだくと流れる顔に柔い手が触れる。それに応ずるように目を閉じれば、嘘みたいに美しい声が俺の名を囁いてくれたような錯覚に陥る。{w}{nw}"
    extend "\n何時ぶりに感じる平穏なのだろう。{w}俺はこの夢を知っている。{w}{nw}"
    extend "\n頬に当たる優しい指先、摺合せの心臓の鼓動、俺の胸の中の彼女と、暖かな温もり…{w}{nw}"
    extend "\n天使が死ぬ夢だ。"
    nvl clear
    br "\n 朦朧とした意識がハッと覚める。急いで目を開きすぐ前の彼女を見つめると、天使はまだ燦々とした光を失ってはいないまま隣にいる。{w}{nw}"
    extend "\n永遠に続く光の様にみえるが、俺はその光が消えてしまう瞬間を覚えている。思い出してしまった記憶に、忘れていた恐怖心が沸き上がる。{w}{nw}"
    extend "\n俺は天使のか細い身体を力の限り抱き締める。{w}{nw}"
    extend "\n真っ直ぐな背中と、空に向かって広がった翼に手が届いた途端、目の前で金色の光が何度もたかれる。程なくして脳が砕けるほどの激痛が訪れた。{w}{nw}"
    extend "\n 触れてはいけない存在に手を出してしまったからだ。それはヒトなる者として受けて当然の罰であった。"
    nvl clear
    br "\n この腕がもがれようと彼女を離さない覚悟が俺にはあった。彼女は抵抗したり、逃げる素振りもなく俺の肩に手を乗せてくれる。{w}{nw}"
    extend "\nその優しさに、耐えていた嘔吐がやがては咳と共に外へと噴出してしまう。喉につっかえていた熱い塊を吐き出せば、溜まっていた温い唾液が共に溢れた。{w}{nw}"
    extend "\n俺は慌てて片手で自身の口を防ぐ。{w}しかしその手に付いたのは黄白い吐瀉物ではない、真っ赤な血だった。{w}{nw}"
    extend "\nもう見慣れた色なのに、その鮮明度は辺り一面のそれらとは違った。"
    nvl clear
    br "\n 顎を伝ってまた何かの液体が落ちる。{w}震える指で確認すると、やはり血が流れている模様だった。{w}{nw}"
    extend "\n天使は困惑で力を抜けた俺の両手からいとも容易く離れてしまう。{w}{nw}"
    extend "\nよろめく体は支えになっていた天使が抜けてしまった為泥まみれの地面へと墜落する。べったりとした地面が顔に貼り付いた。{w}{nw}"
    extend "\nその時、視界に奇妙な物が映る。"
    nvl clear
    hide screen nvlbox with dissolve
    pause 1
    hide screen grumbleBG12
    show story22
    with slowdissolve
    pause 2
    show screen nvlbox with dissolve
    br "\n 青く薄い膜に包まれ紫に近い色を発する真っ赤な腸、その上を綺麗になぞる血管、そしてどろどろと流れ落ちる大量の血。{w}{nw}"
    extend "\nそれもまた周りに落ちている物とは違う。新鮮な生肉特有の薄っすらとした甘さと鉄臭さが鼻がヒリヒリする程漂う。{w}{nw}"
    extend "\nもう遅いのか。{w}俺が彼女を掴んだ手を放してしまったからなのか。{w}{nw}"
    extend "\n重い頭を上げて見れば、依然と真っ白な光は意識を遠のかせるくらいだ。{w}彼女はまだ其処に佇んでいる。{w}{nw}"
    extend "\n未だ残忍な程清廉で、圧倒的な程に美しい姿で。"
    nvl clear
    br "\n 今度は頭を下げ自身を見つめる。{w}くっきりと刻まれた刃の跡を辿るように裂かれた腹の中には長い荒縄の様な腸が繋がっている。{w}{nw}"
    extend "\n今になってなお状況を理解しきれていない脳味噌と共に心臓は止まることなくゆっくりと動く。{w}{nw}"
    extend "\n再び近寄ってくれた光は死にかけの俺を見つめていた。{w}{nw}"
    extend "\nまるで写真機の様に、瞬く二つの瞳に俺の穢れがすべて記録されているという事実が恥ずかしい。{w}{nw}"
    extend "\nその羞恥心に目を瞑るも、一度は手放した真っ白な手が裂けた痕を探り腹底へと入ってくる。"
    nvl clear
    br "\n 開いた口から情けない喘声が漏れるだけでなく、またもや湧き上がってくる真っ赤な嘔吐感が口を伝い滴る。{w}{nw}"
    extend "\n腹を探るひんやりとした感覚は俺が今まで触れてきたどれよりも酷く冷たかった。{w}{nw}"
    extend "\nねっとりとした血が糸を引く音が身体全体に響き、あばらと脊髄に触れられた不気味さに本能的な悲鳴は鳴りやまない。{w}{nw}"
    extend "\nどんどん上へと登ってくる冷たい異物感は、やがて二つの肺の合間で蠢く一つの心臓へと行き着く。"
    nvl clear
    br "\n 五つの指と長く伸はした爪が一つ一つ心臓を撫でるのかと思いきや、やがて鷲掴みにされる。{w}{nw}"
    extend "\n枯れ切った喉から止め処なく垂れていた悲鳴が止まった。{w}{nw}"
    extend "\n煩い程自身の場所を知らせていた心臓の拍動も、刹那動きを止めてしまった感じがした。{w}{nw}"
    extend "\n心臓に熱く圧迫がかかる。"
    hide screen nvlbox with dissolve
    pause 1
    stop music fadeout 3
    hide screen grumbleBG12
    hide story22
    hide screen TrackCursor
    scene black
    with slowdissolve
    pause 2
    with dissolve
    scene bg10 with dissolve
    pause 2
    show screen nvlbox with dissolve
    nvl clear
    "\n 悲鳴と共に目を開ける。{w}全身の感覚が過敏になっていて、血が抜けたかのように気持ちが悪い。"
    "流れる冷や汗を拭う間もなく荒呼吸する。はち切れんばかりに動く心臓の鼓動音が俺を更に不快にさせる。"
    "冷たいうなじを拭っても全身を覆う鳥肌が消えない。"
    "ふと、悪い予感がして布団の中に目をやる。"
    "俺は力の入らない手をガタガタ震わせながらゆっくりと下着の中を確認した。そして目に入る光景に息を呑んでしまう。"
    et "圧力を受け、腹を潰された昆虫の分泌物かの様に、白い泡が染み出ていた。"
    nvl clear
    hide screen nvlbox with dissolve
    call place10
    $ show_quick_menu = False
    show screen morning with fastdissolve
    $ renpy.call_screen("morning")
    scene bg03 with dissolve
    call place03
    pause 1.0
    show screen nvlbox with dissolve
    "\n 淡い灰色の廊下に薄い影がさす。{w}俺はまだ朝のショックから抜け出せず、疲れた目をつり上げた。"
    "昨日、みんなから休んでいいって言われたが、俺の状態は彼らの心配が顔負けになるぐらいとても健康だった。"
    "腕は無理なくよく動く。{w}傷はすべて治ったし、少しの痛みや不便もない。それが怖かった。"
    "俺はどうして平気なのか。俺の状態を確認した皆がそう思っただろう。"
    et "だから俺を部屋の中に閉じ込めようとするのではないか。{w}そんなことを考えると、とてもその部屋にじっとしていられなかった。"
    hide screen nvlbox with dissolve
    scene bg14 with dissolve
    call place14
    pause 1.0
    show screen textbox with dissolve
    play music "audio/bgm/daily.ogg"
    nar "部署に立ち入ると、中の全員がビクリと一瞬身構えた様に見えたが、それだけだ。"
    nar "気にせず席に座る。いつもの席、いつも通りに主教様がのっそりした物言いで挨拶する。"
    nar "変わらぬものに対する安定感…{w}俺は必死にこの場でそれを見つけようとしたが、なかなか気を緩めない。"
    nar "その時、誰かが固まった肩を軽く叩いた。"
    show SCG_03 7 with dissolve
    sc "よう。"
    pl "シ…シーキュレット？！お前なんでこんな時間に…"
    sc "何でって言われても…ボクはいつだってこの時間に居たんだけどな。"
    pl "その…{w}ハハッ、まさかあのシーキュレット様ご本人から直接ご挨拶を頂けるなんてな！"
    show SCG_03 0 with fastdissolve
    sc "…妙な反応はやめなよ。{w}ボクもまさかキミが来るとは思ってもなかった。今日休みなんだろう？"
    pl "早起きしてしまったのもあるし、部屋に篭ってばっかじゃやることないんだよ。"
    show SCG_03 7 with fastdissolve
    sc "マヤが気になったからじゃなくて？"
    pl "な～んでマヤの話がここで出てくるんだよ！"
    my "わたしの話は出しちゃだめなの？"
    hide SCG_03 with dissolve
    nar "聞き慣れた声にびっくりして後ろを見れば、そこにはマヤが立っていた。"
    nar "しかしさっき聞こえた声は彼女の声ではない。"
    nar "夢の中で何度も聞いてきた、柔らかくて優しい天使の声だった。"
    nar "それを認識した次に彼女の顔が目に入った。"
    nar "丸い顔の間間のちまちました出入り、薄い服にくっついた柔らかい線、白くて小さな手。"
    nar "間違いなく彼女は…"
    show SCG_02 8 with dissolve
    my "…ごめんね、おふたり話してる途中だったのに邪魔になったかな…"
    pl "ち…違う！{w}ゴメン！急に話掛けられてビックリしただけだって。"
    show SCG_02 0 with fastdissolve
    my "うん…{w}腕はもう大丈夫？[na2]くん。"
    pl "マヤがお見舞いに来てくれたお陰でヘッチャラよ！"
    hide SCG_02
    show SCG_02 6 at left
    show SCG_03 7 at right
    with dissolve
    my "キューくんもおはよ…{w}きょ、今日は一緒にお仕事できるの…？"
    sc "おはよう、マヤ。{w}残念ながらボクは今日一緒に行けないんだ。主教様からのお使いがあってね。"
    pl "朝からご苦労なこった。"
    show SCG_02 0 with fastdissolve
    my "そっか…でも挨拶できてよかったな…"
    show SCG_03 8 with fastdissolve
    sc "…実はすぐ向かうつもりだったんだけどね、キミたちが早めに出勤してて良かった。"
    show SCG_02 4 with fastdissolve
    my "へへ…"
    pl "ほぉ、そこまで気を遣ってくださるとは大変光栄だな。"
    sc "……"
    pl "いってらっしゃい、マヤの業務は俺が手伝うから。"
    show SCG_03 7 with fastdissolve
    sc "昨日の事もあったし…{w}今日は簡単な仕事に配属させといたから、キミたち二人で行けば早めに終わるはずだよ。"
    show SCG_02 0 with fastdissolve
    my "なんか、ごめんなさい…{w}二人とも…忙しいのにわたしのせいで…"
    pl "どうせ暇だったしいいって。"
    sc "じゃあ、お先。{w}頑張ってね。"
    pl "おう、ありがとよ。"
    show SCG_02 at bounce
    my "キューくんもがんばってね…！"
    hide SCG_02
    hide SCG_03
    with dissolve
    nar "俺の隣に並んだマヤはいつもと変わらないままだ。{w}可笑しいのは俺だけだった。"
    nar "どうして今まで気付かなかったんだろう、何故今更気付いたんだ。{w}俺は夢の中の彼女を知っていたのに。"
    show SCG_02 with dissolve
    my "[na2]くん、どうしたの？"
    pl "や…まだちょっと眠気が。"
    my "何か悪いことでもあったの…？"
    pl "…そんなんじゃないって、どうしてそう思っちゃったんだ？"
    my "最近なんだか、元気なさそうで…"
    pl "ハハ、心配させちまって恥ずかしいな。{w}最近考え事が多くなってさ…"
    hide SCG_02 with dissolve
    nar "早く他のを考えよう。仕事にかかるとそっちに気が向くはず。{w}そう思ってロッカーを開けたが、すぐに頭の回転が鈍くなった。"
    nar "その中に俺のじゃない道具が入っていたから。{w}俺はドアを閉め番号を確認する。開け違いには見えない。"
    ex1 "あ！わりぃわりぃ、ずっと空っぽだったから、空いてると思ったんだよ。" with sshake
    nar "待っていたかのように話しかけてきたヤツはこの間会ったあの男だ。{w}金髪女と一緒にいた連中の一人。"
    nar "つい数日前そんなことがあったが、こいつらは感じることがないのだろうか。"
    nar "穴のある歯をまる見えに口を開けてニヤニヤする姿がおのずと反感をそそる。"
    nar "すると、彼のそばにいたもう一人の司祭が俺よりも顔をしかめ、彼のほうにつかつか近寄ってきて、わっと大きな声を出す。"
    ex2 "オイ！テメェ、俺のモン片付けるとか言っといて、あっちに全部突っ込んどいたのか？" with sshake
    nar "目の前の俺は無視したまま、下品な笑い声と共にヤツら同士の軽い争いが行き交う。"
    nar "この状況を理解するため頭を使ったところで子供っぽい理由だけが明らかになるだけで、"
    nar "それはくやしくにも俺の気分を害するに十分だった。"
    nar "まだ騒がしい空間の中、すぐ隣で道具を取り出したある女性が俺に声をかけてくる。"
    ex3 "編入生くん、ごめんね…"
    ex3 "でも、私たちのスペースもかなり足りてないんだ。{w}どうせすぐ魔導部に行くんだったら荷物なんかさっさと空けてほしいんだけど。"
    nar "この女性は席が近いため顔は知っていたが、直接話したことはこれまで一度もなかった。"
    nar "そうなのに彼女は疑いなく俺を敵視していた。"
    nar "冷たい視線は話の途中俺といっさい合わず、ロッカーの閉め音も必要以上に大げさに聞こえた。"
    nar "周りを見回すと、その子だけではない。"
    nar "みんな何かの異物感、あるいは敵対感を表現するかのように俺に向けて嘲笑し睨みを付けている。"
    nar "最初からこの団体が俺を遠ざける気はかすかにあったが、今ではその距離感が空間に溢れている。"
    nar "俺をいじめる連中が特別なわけでもなかった。{w}彼らは俺に感じる感情を表にあらわしただけ。"
    nar "本当はみんな黙っているだけで、同じ気持ちを持っていたのだ。"
    nar "俺のロッカーの中にあった道具を汚物であるかのように引っ張り出す連中を見ていると、思わずせせら笑ってしまう。"
    nar "滑稽な状況への嘲笑だった。"
    nar "その声を聞いたかちらほらと部室を出た群れがしばし後ろを向いたが、すぐ足を早めた。"
    show SCG_02 0 with dissolve
    my "[na2]くん…大丈夫？"
    pl "ああ、大丈夫。マヤもそんな気にしなくていいぜ。"
    show SCG_02 7 with fastdissolve
    my "み…みんなひどいよ、もうすぐで七日目なのに…"
    pl "まあ、どうでもいいな。それもこれも全部俺に嫉妬してのことだろ？{w}勝手にさせとこうぜ。"
    my "う…うん…"
    nar "気を悪くしたことだけは事実だが、それだけだ。"
    nar "魔導部とは元々セイントシェオルの栄光。"
    nar "しかも俺はその頂点であるアルタナータの偏愛を受けているから、これくらいの猜忌は当然だ。"
    nar "言葉でまとめてみれば簡単なのに、俺は普段その事実を冷静に受け入れられなかった。"
    nar "今こんなにも落ち着いているのは、多分さっきまで彼女に関して考えていたからではないか。"
    pl "じゃあ行こっか。"
    my "うん…"
    hide SCG_02 with dissolve
    hide screen textbox with dissolve
    pause 1
    scene bg04 with dissolve
    call place04
    pause 1.0
    show screen textbox with dissolve
    nar "マヤは歩き出した俺の後ろに急いで追いついた。"
    nar "仕事の途中にも不安で何度も後ろや横を振り向いたが、そこには怪しむ首をひねたマヤが立っているだけだった。"
    nar "一人前になったことで仕事の負担ははるかに減り、俺たちは二人とも早めに神殿に戻った。"
    nar "黒ずんだ袋を荷車から運んでいる途中、火がついていなくてまだ真っ黒な火鉢を見ていたマヤがふいと言い出した。"
    show SCG_02 0 with dissolve
    my "[na2]くん、最近なんかお悩みとかないかな？"
    pl "お…お悩み？なんで？"
    my "ううん…最近色んなことがあったじゃない…{w}だからもし何か悩んでることがあったなら…"
    pl "ないない！最近は仕事にも慣れてきたし、マヤもいるからさ…"
    show SCG_02 8 with fastdissolve
    my "…そっか。でも悩みごとが出来たら相談してね。"
    pl "ん…ありがとう。"
    nar "突然の質問に思わず嘘をついてしまった。"
    nar "ずっと鼓動していた心臓は、その答えを口走るや更に騒々しく弾け出す。"
    nar "悩みって、いきなりなんで聞くんだ？"
    nar "ずっと気になっていた。{w}彼女が毎晩俺の夢に現れる理由は、もしかしたら俺に何かを知らせる為ではないか。"
    nar "だとしたらそれは警告か？{w}もしくは、助けを呼ぶ為か？それとも…"
    nar "マヤは俺の不自然な態度を心配しているような、もしくは疑っているような視線を逸らそうとしない。"
    nar "彼女はもう何もかも知っているかもしれない。{w}そうだ、俺を試す為に…しかし何を？"
    pl "マヤは最近…なんか悩みとかないのか？"
    my "悩み…まだ全然慣れてないのが悩みかな…{w}[na2]くんとか、他の人もみんなすごく手伝ってくれてるのに…"
    pl "じゃあ…もし研修期間が終わっても仕事に慣れなかったらどうする？"
    my "……その時は…"
    pl "傍に居てくれるか？その時も！"
    my "……"
    pl "…って…その時は来ないのが一番だろうけど…"
    my "…時がきたら、ね。{w}考えてみるね。"
    hide SCG_02 with dissolve
    nar "袋は重たい音を立てて穴に落ちる。{w}火のついた火鉢からはすぐかび臭い煙が立ち昇り、視界は橙色に揺れた。"
    nar "俺たちはしばらく静かに、人の骨片が火の中でぱちぱちと灰になって燃えるのを見守り、やがて他の場所へと足を運んだ。"
    hide screen textbox with dissolve
    pause 1
    stop music fadeout 2.0
    scene bg14 with dissolve
    call place14
    pause 1.0
    show screen textbox with dissolve
    nar "慣れてきた部室の扉を開いた時、俺は突然足を止めた。"
    nar "沈んでいた空気が、今日に限ってとっくに尖ったように感じられた。"
    nar "遠くから人の声が聞こえてくる。"
    nar "しかし灯りは全部消してあり、まず見てみれば誰か残っているようではなかった。{w}主教室だ。"
    nar "ずっと堅く閉じられていたその隙間から唯一の微かな光が抜け出ていた。"
    nar "思い浮かんだ好奇心に、近づいてはそっと目と耳に神経を集中してみれば、狭い隙間から中の風景が見えてきた。"
    nar "煙たい空気の臭いが顔面に吹いてきて危うく咳が出るところだった。"
    nar "彼女とは似合わない苦い香り、タバコの臭いだ。どうやら客が来たらしい。"
    nar "浄化部では見つけられない黒い髪と、小さな体躯。{w}間違いなく魔導部の主教だ。"
    nar "その向かい側にハク主教が座っている。"
    nar "外貌と性格、何もかもが相反する二人の主教が同じ場所にいる姿は、今の状況と共に現実感が全く感じられない。"
    show SCG_09 8 zorder 3 at bigright
    show SCG_05 8 zorder 2 at bigleft:
        xalign -0.5
    with dissolve
    play music "audio/bgm/golden haku.ogg" fadein 2.0
    nvl clear
    "{nw}"
    show SCG_09 8 at bounce
    er "…部下共の統率一つまともに出来ずこの事態を呼び起こしておいて、下した処置がたったの一日休暇とは如何に嘆かわしい事か。"
    er "主教の座も楽になったものだな？"
    show SCG_09 zorder 1 with fastdissolve
    hk "主教様も御存知の通り、浄化部は全ての司祭が兵力であるがため一人の空席を埋めるのがむずかしいのです…～"
    hk "兄弟の容態もまた良好に向かって…"
    show SCG_09 zorder 3 with fastdissolve
    er "それは貴様の目で直接確認した結果か？"
    show SCG_09 zorder 1 with fastdissolve
    hk "…司祭の方を通じて報告いただきました。{w}それはエルジェーベト主教様も同じでは…～"
    hide SCG_09
    hide SCG_05
    with dissolve
    nar "…俺の話が去来している。{w}まさか喧嘩か？"
    nar "あの二人に限ってそんな訳はないだろうが、何となく心臓が騒がしくなる。"
    nar "二人の表情は視野が狭いせいで良く見えないが、その声と雰囲気は一目で分かってしまうほどに鋭い。"
    show SCG_09 8 zorder 3 at bigright
    show SCG_05 8 zorder 2 at bigleft:
        xalign -0.5
    with dissolve
    er "下劣極まりない出身地の、乳臭いガキ共で適当に埋め合わせた兵力。"
    er "それらを教えるもまたイロハのイの字も分からぬ案山子主教と来た。"
    er "これが今セイント・シェオルと州都を裏から支える浄化部か？"
    show SCG_09 9 with fastdissolve
    er "約束された一ヶ月だけでも見守る心算だったのだが、これはもう見てられんな。"
    er "こんな所に埋もれていては、死んでいるも同然だ。"
    show SCG_09 zorder 1
    show SCG_05 1
    with fastdissolve
    hk "エルジェーベト主教様？{w}申し訳ございませんが、その話には語弊がありますねぇ…"
    hk "浄化部が魔導部の旗下から離れ、別の部署として創立された以来、基礎教育のおかげで文盲率が減り…"
    show SCG_05 8 with fastdissolve
    hk "につけず、社会から孤立される哀れな兄弟たちの苦しみも解決されており…"
    show SCG_09 10 zorder 3 with fastdissolve
    er "そして聖なるべき神殿が犯罪者と出身も知らぬ雑種の巣となった。"
    show SCG_09 9 with fastdissolve
    er "今やここが神様を祭る所か裏通りに散らばっている刑務所かわからん。{w}この間も、飽きもせず事件があったって？"
    show SCG_09 11 with fastdissolve
    er "セイント・シェオルの位相は完全に地ベタに落ちてしまった。"
    show SCG_09 10 with fastdissolve
    er "神殿を公園のガキの砂場の如く土足でズケズケと入り込んでお偉い顔する貴様と、"
    er "そんな貴様に主教の名を付けた一層ド偉い父親のおかげでな。"
    show SCG_09 zorder 1
    show SCG_05 0
    with fastdissolve
    hkn "依然御自身の意思通り事が動かなくなると思考が硬くなってしまわれるのですね。"
    hkn "裏で他者を批判する事こそ負け犬の遠吠えという自覚が御座いませんでして？"
    nar "……"
    show SCG_09 4 zorder 3 with fastdissolve
    show SCG_09 at bounce
    er "ほぉ、この俺を凌辱するか。"
    show SCG_09 zorder 1
    show SCG_05 5
    with fastdissolve
    hk "凌辱？"
    show SCG_05 10 with fastdissolve
    hkn "ははっ、恥多くも無知なる私めがエルジェーベト・アルタナータ主教様を凌辱する等恐れ多い！"
    hkn "私は只、共に神に仕える兄弟となる者として主教様の今後のためささやかながら助言を申し上げた迄で御座います。"
    show SCG_09 zorder 3 with fastdissolve
    er "その無知な脳ミソの乱れた思考を正す方法は無い癖して、他人を嗤い中身の無い虚勢を真似る方法は入ってるらしいな。"
    show SCG_09 9 with fastdissolve
    er "子は親の背中を見て育つと言うが、正に舐痔得車の鑑だな。"
    show SCG_09 zorder 1
    show SCG_05 8
    with fastdissolve
    hkn "主教様は浄化部の主教たる私めと会話にいらっしゃった筈ですが、先程から父上の名無くしては一言も発せられないのですね。"
    show SCG_05 1 with fastdissolve
    hkn "大変申し上げ難いのですが、過去の亡霊に囚われた者に明日は御座いません。"
    hkn "浄化部がセイント・シェオルの地位を落としたのであれば、"
    show SCG_05 0 with fastdissolve
    hkn "州都と神殿の明日が塞がれた儘なのはその頂点に立つ貴方様が垂直的位階秩序を暴力的に強要しているからではないのですか？"
    hide SCG_05
    hide SCG_09
    with dissolve
    stop music fadeout 2.0
    nar "その瞬間、彼と目が合った。"
    nar "俺は体を竦めては慌てて扉から離れる。いつの間にか滴になった冷や汗が蟀谷からずり落ちた。"
    nar "しばらくして彼が扉の外に姿を現した。なんでも言わないと、しかし体が固まって動かない。"
    show SCG_09 11 with dissolve
    er "…盗み聞きなど、既に大分染まってしまった様だな。"
    hide SCG_09 with dissolve
    nar "彼はその一言だけを呟いて首を横に振っては、そのまま部室を出た。"
    nar "ひっそりと静かになった部室に俺の騒がしい心臓の音だけが鳴っている。{w}固く閉まった扉の向こうからはもう何の声も聞こえない。"
    nar "刹那の幻覚でも見ていたのかと自ら疑ってしまうほどに、何事が一瞬で過ぎてしまった。"
    nar "その事実を確かめたくなってきたが、とても扉に手を伸ばす勇気が出なかった。"
    nar "この先にいるのは、本当にハク主教様なのか？{w}ばらばらに分かれた記憶が一つずつ走馬灯のように頭の中で走る。"
    nar "間違いない。{w}俺は彼と、「アレ」と会ったことがある。"
    sc "そんなところで突っ立って何やってるんだ、キミは。" with sshake
    show SCG_03 7 with dissolve
    nar "ふと聞こえた声に後ろを向くと、書類何枚かを手に持ったシーキュレットがいた。"
    nar "思わずぼうっとしていたのか、彼が部室に入ったことに気付かなかった。"
    play music "audio/bgm/daily.ogg" fadein 3
    pl "いや、まあ…{w}お前はお使いか？"
    sc "まあね。マヤは？"
    pl "先に帰ったぜ。{w}うーん…多分寮か花壇に居るんじゃないか？"
    show SCG_03 8 with fastdissolve
    sc "ふぅん…"
    nar "シーキュレットは閉まった扉と俺を交々眺めた。"
    show SCG_03 7 with fastdissolve
    sc "主教様に用事でも？"
    pl "や、別に…"
    sc "ならちょっと退いてくれる。"
    pl "おう…"
    hide SCG_03 with dissolve
    nar "俺が何歩か退いたら、彼はあまりにも簡単に扉を開いては中に入った。"
    nar "狭く開いた扉の隙間からはやはりタバコの臭いがしていた。"
    nar "そして何分経ったか、彼は入る時よりも更に多くの書類を持ったまま出てきた。"
    show SCG_03 7 with dissolve
    sc "…もしかしてボクに用事あった感じ？"
    pl "お前今日は書類とにらめっこばっかして退勤するつもりか？"
    sc "まさか…これは午前中に終わらせなきゃいけない書類だよ。"
    pl "じゃあ午前まではヒマなんだな？"
    show SCG_03 0 with fastdissolve
    sc "いや、暇って訳でも…{w}はぁ…なんだい？"
    pl "や…まぁ…"
    nar "俺は横目で睨んでは、ゆっくりと主教室と離れた所に足を運んだ。"
    nar "彼は怪しむ顔をしているが、書類を持ち上げたまま付いてきている。"
    pl "主教様はどうだった？"
    show SCG_03 7 with fastdissolve
    sc "別に…普通だったけど。"
    pl "そっか…{w}実はさっき魔導部主教様がいらしててさ。"
    pl "あの人浄化部の人にちょっと当たりキツいだろ？それが心配でさ～"
    show SCG_03 8 with fastdissolve
    sc "ふぅん、魔導部主教ね…{w}キミがそこまで主教様のことを気に掛けているとは知らなかったな。"
    pl "俺だって一応浄化部司祭だろうが…"
    nar "仲直りはできたとはいえ、奴の言葉にはまだ棘がある。{w}元々そういう奴らしい。"
    nar "彼はしばらく俺を見つめては、すぐ書類一枚を引き出しては俺の方に押し入れた。"
    nar "まるで受け取れ、と言っていそうに手を伸ばしている。"
    pl "これは？"
    show SCG_03 72 with fastdissolve
    sc "部署異動に関する書類。{w}これのせいで扉の前で待ってたんだろう？"
    pl "え？{w}あ…うん。ありがと。"
    sc "主教様が明日まで提出してくれって言ってたよ。"
    pl "主教様が直接…？{w}じゃあ俺が扉の前に立ってることを知ってらっしゃったのか？"
    show SCG_03 7 with fastdissolve
    sc "そんなぼうっと突っ立ってるのに知らない方が可笑しいだろう…"
    pl "ハハ…そうだな、直接渡してくれた方が早いだろうに…"
    sc "……"
    sc "…で、どうするのさ？{w}一応もう一か月後に再提出でもいいとは言ってらっしゃったんだけど。"
    pl "いや……もう決めてる。{w}魔導部にいくぜ。"
    pl "俺がずっと居座ってても部署の雰囲気が気まずくなるだけだろうし。"
    show SCG_03 8 with fastdissolve
    sc "そうか…それは残念だな。"
    pl "おぉ、朝から大分正直じゃねえか～本気でそう思ってんのか？"
    show SCG_03 7 with fastdissolve
    sc "本気だよ。{w}マヤはどうするのさ。"
    pl "マヤ…？"
    stop music fadeout 0.5
    sc "キミ、マヤのこと好きなんだろう。"
    nar "いきなり彼の口からとんでもない言葉が出てきた。"
    nar "俺はあまりにも驚いてしまい、反論さえも考えられずにぼんやりと口を開いた。"
    nar "マヤが好きだって？{w}俺が？{w}俺にとってマヤは…"
    play sound 'audio/se/memory.ogg'
    hide screen textbox
    scene black
    with fastdissolve
    pause 0.2
    hide SCG_03
    scene bgw
    show story22 with dissolve:
        zoom 2
        xalign 0.9
        yalign 0.2
    scene bg14
    show SCG_03 7
    with dissolve
    show screen textbox with dissolve
    nar "滅相もない話題に最初は混乱してしまったが、彼女の姿をゆっくり思い出したら動揺した感情が落ち着いていった。"
    pl "そんな。{w}マヤはもちろん好きだけど、そういう意味で好きなワケじゃない。"
    sc "…そういう意味で好きな訳じゃない、と？"
    pl "そうだよ、まさか他でもなくお前からそんな話が出て来るなんて想像もつかなかったぜ。"
    pl "噂とか恋愛ごっこやらは嫌いだったんじゃないのか？"
    show SCG_03 8 with fastdissolve
    sc "……"
    nar "もし人の常識から外れたとはいえ、俺の中にマヤはもう、友達や恋人以上の存在になっていた。"
    nar "彼女は誰よりも弱弱しくて崇高で、人を正しい道へ導き、罪人の業を救う存在。"
    nar "救援される為に舞い降りた、地上に現存する天使。"
    nar "人間たる俺がそんな天使に恋心を抱くなんて、とんでもないことだ。"
    play music "audio/bgm/daily.ogg" fadein 2
    sc "そっか…また勝手に決めつけちゃってごめん。"
    pl "ごめんなさいのついでにちょっと頼みごと。"
    show SCG_03 7 with fastdissolve
    sc "頼み事？"
    pl "この書類、お前が俺の代わりに主教様に渡してくれ。"
    show SCG_03 0 with fastdissolve
    sc "…ボクが？{w}余計面倒くさくなると思うけど。"
    pl "他の書類のついでにやってくれてもいいじゃんか。"
    sc "はぁ…{w}署名はキミがやらないといけないのは知ってるよね？"
    pl "知ってる知ってる。"
    nar "今すぐは主教様に会うのは気まずい。"
    nar "あの人についてはもう十分知っているのに、どうしてかたまにはこんなに対面を憚る時もある。"
    nar "それははっきりした理由があるというよりは、本能的な恐れに近い。"
    nar "そこから好奇心が兆す時もあるが、今はない。"
    show SCG_03 7 with fastdissolve
    sc "……？{w}何？"
    pl "いつまで「お前」とか「[na]」って呼んでんだよ、堅苦しい。"
    sc "それがキミの名前だろう。"
    pl "普通に他の人みたいに呼べやいいのに。"
    show SCG_03 8 with fastdissolve
    sc "…そういうの慣れてないから…"
    pl "またまたキューくんったら、嬉しいクセに～"
    show SCG_03 0 with fastdissolve
    sc "五月蠅い。"
    nar "力強く握っていた書類をシーキュレットが引っ手繰るように持っていく。{w}これで違和感も見逃されるだろう。"
    show SCG_03 8 with fastdissolve
    sc "それで、その…"
    show SCG_03 72 with fastdissolve
    sc "…[na2]、これからどうするんだい？"
    pl "時間もまだあるし、ちょっと歩き回ろうかなって。"
    pl "忙しいとこゴメンな。{w}お疲れさん。"
    hide SCG_03 with dissolve
    nar "書類を押し付けた俺は逃げるように部室を去った。"
    nar "皆が出て行った部室は、最初から空いていたように静かだ。{w}狭いすきまだけをおいて詰まっている机と椅子。"
    nar "日陰の中でさらに暗くなる影、風一つ吹かない息苦しい空気。{w}みんなこの鶏舎の中でよくも暮らしている。"
    nar "もうそこには留まりたくない。もうすぐで一週間が過ぎる。{w}一か月の時間なんて、もっと早く過ぎてくれればいいのに。"
    nar "俺は再び後ろを振り向くことなく歩き出した。"
    nar "何故か、今日で最後かもしれないという漠然とした不安が押し寄せる。"
    nar "彼女に会わなければならないという確信が出来た。{w}頭の中に浮かぶ「彼女」を。"
    call meet_girl
    hide screen textbox with dissolve
    stop music fadeout 2
    hide screen textbox with dissolve

    $ save_name = "day 6, 昼, 楽園"
    jump placemenu
    return

label day6_n_rkn:
    $ save_name = "day 6, 夜, 楽園"
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
    jump day7_sc
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
