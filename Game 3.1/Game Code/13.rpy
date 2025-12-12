label day3:
    $ day = 3
    if hssh_rkn == True:
        $ save_name = "day 3, 朝, 楽園"
    else:
        $ save_name = "day 3, 朝"
    play sound 'audio/SE/bell 1.ogg' fadein 2.0
    image 3day = Text("day 3",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '3day' at day00 with slowdissolve
    pause 5
    hide expression '3day' with slowdissolve
    stop sound fadeout 1.0
    pause 1.0
    show screen at_frame with dissolve
    if hssh_rkn == True:
        scene bg10_1 with slowdissolve
    else:
        scene bg10_2 with slowdissolve
    call place10 from _call_place10_3
    play music 'audio/se/no more bell my buddy.ogg'fadein 3.0
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    $ _game_menu_screen = 'preferences'
    show screen keymap_screen
    hide screen textbox with dissolve
    nvl clear
    show screen nvlbox with dissolve
    "\n 「…ハハハ……アハハハ……」"
    "\n 何処からか女の笑い声が聴こえてくる。"
    "暗い部屋に灯りが灯されると、蛍光灯がチカチカと点滅する音が聞こえる。{w}灯りはついたはずなのに、揺らめく灰色の視界は未だ暗いままだった。"
    "女は俺に何度も問いかける。俺は答えられない。口が何かによって封じられているからだ。{w}俺に出来ることと言えばこの壁と寝具に染み付いたかび臭さに耐えることだけ。"
    "頭の奥で朱色の花火が弾けては消える。"
    et "状況は何も変わらない。真っ暗な暗闇の中に誰かが居る。"
    nvl clear
    "\n「あたしと一緒にいれば自分の立場もエラくなるとでも思ってんじゃない？」"
    "\nその気高い自尊心はこうやって作られたのだろう。"
    "\n「特採で来た癖に仕事もせず初日から女ばっか追いかけてるとか、本当に底が知れるね。」"
    "「だって、男ってどーせみんな{k=-2}―――{/k}」"
    et "\n俺のことを何一つ理解していないクセに、俺に「わかる」と寄ってきた人々へ、一体俺はどうやって自分自身を証明すれば良かったのだろうか。"
    nvl clear
    "\n 「[na]兄弟も、もうじき魔導の一員となられるお方ですので…これからも是非気楽に声をお掛けください。」"
    "\n最初からこんな場に呼び出されてしまったこと自体が間違いだったんだ。{w}ここに留まれば留まるほど俺は知らぬうちに誰かの玩具となり弄ばれる。"
    "\n「じゃ、カワイ子ちゃんたちは後でね～」"
    "\nその時点でバカにされてるということにもう少し早く気付けたら…"
    et "\n「隣同士じゃん？挨拶したくってさあ。」"
    nvl clear
    "\n 息を吸って吐くだけで彼らに嗤い者にされているという事実に、もう少し早く気付けたら。{w}しかし巻き戻すことは出来ない。"
    "既に不特定多数の人間が無謀な可能性に人生を賭けた俺を嘲笑い、そうやって自分の自尊心を満たして毎日傲慢に生きている。"
    "抜け出す為の穴なんてものはもう残っちゃいない。"
    "\n「…ヘンなの……"
    "そんなこと言われたの、初めてかも…"
    "[na2]くんってヘンなの。」"
    et "\n……"
    hide screen nvlbox with dissolve 
    stop music fadeout 2
    nvl clear
    pause 1
    scene black with slowdissolve
    $ renpy.music.set_volume(1, channel="music")
    pause 4
    play music "audio/bgm/dream.ogg" fadein 5
    pause 4
    scene bg12
    show screen TrackCursor
    show screen grumbleBG12
    with slowdissolve
    pause 1
    show screen nvlbox with dissolve
    br "\n 固まっていて冷たい土の塊の上に立っている。{w}辺りを見渡すために動かした靴先にヘドロがへばりつく。{w}{nw}"
    extend "\n足を上げて見ればそれはヘドロなんてものじゃない。{w}動物の内臓だった。潰された腸から膿に近い粘膜が散らばっている。{w}{nw}"
    extend "\n辺り一面死体、死体、死体。頭上から降りかかる生温かい血。まるで誰かの墓にでも居る気分だ。{w}俺はここを良く知っている。"
    nvl clear
    br "\nふと、耳と脳裏に染み込む感じ慣れた吐き気に顔を上げる。白く濁った空に天使の輪郭が映る。{w}{nw}"
    extend "\n「それ」は俺に向かって手を差し伸べている様だった。圧倒的なまでに美しい。{w}{nw}"
    extend "\n人間として然るべき敬拝心。当然たる恐怖心。全ての感情がその神々しい存在にあった。{w}{nw}"
    extend "\n いつの間にか俺を抱きかかえた天使は俺の下腹に真っ白な手を翳す。{w}頭から冷や汗が滴る。{w}{nw}"
    extend "\n俺は抑えきれない震えに、か細い天使の背中まで恐る恐る手を上げる。{w}降り注がれる血のせいでドロドロの色に染み付いていた。"
    nvl clear
    br "\nダメだ。{w}こんな汚らしい手では天使に触れられない。{w}彼女は俺の抗えない存在。振りほどくことの出来ない存在なのだから。{w}{nw}"
    extend "\n優雅で、汚らわしさなんて知らないような五本の指が冒涜的なまでに優しく俺の身体を這う。{w}{nw}"
    extend "\nそして息をすることさえ許されない程近く、更に近く顔を寄せてきた。"
    nvl clear
    br "\n 天使が囁く。{w}{nw}"
    extend "\n「もう飽きてしまったわ。」{w}{nw}"
    extend "\nそれに答える間を与えず、天使は白い翼を広げて遠くへと消えていく。{w}ほぼ同時に何かによって首が引っ掛けられ、引き摺られる。{w}{nw}"
    extend "\n意識が何処かに落ちる音がして、視界は暗転した。"
    play sound "audio/se/memory.ogg"
    stop music
    hide screen nvlbox
    hide screen TrackCursor
    hide screen grumbleBG12
    scene bgw
    if hssh_rkn == True:
        scene bg10 with dissolve
    else:
        scene bg10_1 with dissolve
    pause 1
    nvl clear
    $ renpy.music.set_volume(0.7, channel="sound")
    play sound "audio/se/raining.ogg" fadein 30 loop
    show screen nvlbox with dissolve
    "\n 身体が跳ね上がる様な感覚と共に目を覚ます。{w}まだ夢の中の様な感覚がして周りを見渡してみたが、いつもの天井で、いつもの部屋だった。"
    "真っ暗な部屋、静かな静寂の中で雨音が響く。外は雨が降っている。"
    "州都の夏は雨ばっかりだと誰かが言った気がする。晴れ晴れしない空のままでは時間が見計らえない。{w}俺は手探りで、枕元で置き時計を探す。"
    "ちょっと横になっただけでつい眠ってしまったようだ。{w}最後に確認してからまだ3時間も過ぎていない。"
    et "また眠れそうにもないが、ベッドの上で横になってしまう。"
    nvl clear
    "\n「女を知らないからそうなのよ。」"
    "古びた発条の音のせいか、彼女の声が頭に浮かぶ。"
    "俺は朦朧とした意識のまま、自分の体をまさぐる。昨夜のことが徐々に実感できる。"
    "冷たい手が腰を掠り、柔らかい舌が耳に差し込まれるその感覚が蘇ろうとして、展転してしまう。"
    et "ヘンな気分だ。{w}わけの分からない感情が頭を押さえつける。{w}夢見が悪かったせいか、皆こんなことを経っているのか、または…"
    hide screen nvlbox with dissolve
    scene black with dissolve
    pause 2
    if hssh_rkn == True:
        scene bg10 with dissolve
    else:
        scene bg10_1 with dissolve
    nvl clear
    if hssh_rkn == True:
        nvl clear
        scene bg14 with dissolve
        call place14
        show screen nvlbox with dissolve
        "\n 俺は考えることを止めて部屋から出た。扉を開け閉めする音、廊下を歩く自分の足音が雨のせいかいつもよりも更に大きく聞こえてくる。"
        "そろそろ出勤の時間だ。その前に、昨日の大騒ぎを何とか整理しないと。"
        "昨日の惨状を思い出しては漠々とした気持ちで部室の扉を開いたが、目に入った風景は心配したこととは少し違っていた。"
        "汚い花瓶とコップの欠片などが床に散らばっていることは昨日と同じだが、床をぎっしりと満たした書類の紙は全て消えていた。"
        et "もう片付けたのか。一瞬心臓が凍えそうになってきたが、冷たい朝の空気と雨天の湿気が心を静めたお陰か、それ以上に感情が揺れてはいない。"
        nvl clear
        "\n 俺は素直にほうきを持ち出して散々な欠片を掃き集め、袋に入れた。袋は部室の片隅に沢山積もっていたが、その使い道を思い出したら少し気持ち悪くなってきた。"
        "普段はいつも死体の焼ける臭いが立ち上がる作業場の捨て場だが、早朝に来たらやはりそういう不便さもない。いつも煩く作動した絡繰りの音も今は聞こえない。"
        "多分今頃は部署に人が集めてきたんだろうか。まだ帰りたくない。"
        et "冷ややかな壁に寄りかかって立っていれば、やはり昨夜のことが思い浮かぶ。俺のことを知らないくせに知っているという人々に、俺はどうやって自分を証明すべきだったんだ。"
        nvl clear
        "\n ここにいればまるで俺の知らない内に誰かの玩具になって踊らされてしまう。馬鹿げたことに早く気付くべきだった。"
        "息を吸うことにさえも彼たちの嘲笑を買っていることにもっと早く気付くべきだった。だったら、もっとマシな対処ができていただろうか。"
        "……"
        "遠くから微かに人の声が聞こえる。これ以上時を稼いだら更にとんでもないことになるだろう。"
        nvl clear
        hide screen nvlbox with dissolve
        scene black with dissolve
        pause 3
    else:
        show screen nvlbox with dissolve
        "\n 俺は考えることを止め、布団の染みを数えながら夜明かしした。隣の部屋から音が聞こえてくる。"
        "間違いなく出勤時間だ。{w}雨のせいか、扉が開き閉まる音、人の群れが騒ぐ声、廊下を往来する足音がいつもよりも大きく聞こえてくる。"
        "俺も今すぐ起きて支度をしないといけないのに、分かっているはずだが、体がなんとなく重たい。"
        "目の前の現実がまるで他人事に見える。{w}布団を頭の上まで引き上げてしまう。{w}外へ出たくない。"
        "扉と壁の向こうから女性の声が聞こえる度にやたらに驚いてしまう。{w}俺は玉繭のように布団の中に閉じこもる。"
        et "このまま騒ぎが消えるまでじっといよう、そんなことを思いながら気楽に目を閉じた。"
        hide screen nvlbox with dissolve
        scene black with dissolve
        pause 3
        scene bg10_1 with dissolve
        nvl clear
        show screen nvlbox with dissolve
        nvl clear
        "\n 音が一つ一つ去っていくのをじっと待っていると、突然誰かが扉を叩いた。{w}布団の中で息を詰めて数秒、やがて恐る恐る扉に近づく。"
        et "外は静かだ。そっと指何本かをかけて僅かな隙間を作る。{w}そうやって誰もいないことを確かめてから、俺は出勤の支度を始めた。"
        hide screen nvlbox with dissolve
        nvl clear
        $ show_quick_menu = False
        show screen morning with fastdissolve
        $ renpy.call_screen("morning")
    if hssh_rkn == True:
        scene bg03 with slowdissolve
    else:
        scene bg03_1 with slowdissolve
    call place03 from _call_place03_11
    pause 1.0
    show screen textbox with dissolve
    nar "廊下にはもう誰もいない。{w}朝から降っている雨は段々と強く窓にぶつかる。{w}空が暗くて、沈んだ建物が広く感じられる。"
    nar "俺は部署の前でのそりと歩き回し、角を曲がれば気まずい人の顔と行き当たった。"
    nar "彼は、俺と同じくいきなりの遭遇に驚いたように、しばらくは黙り、すぐ眉根を顰めた。"
    stop sound fadeout 3
    hide screen textbox with dissolve
    show SCG_03 2 with dissolve
    show screen textbox with dissolve
    sc "キミ、さぁ……"

    play music "audio/bgm/daily.ogg"
    show SCG_03 0 with fastdissolve

    sc "頼むから面倒事を増やさないでくれる？{w}仕事すっぽかしてどうするつもりなんだよ。"
    pl "あ？あぁ…ゴメン。"
    if hssh_rkn == True:
        sc "仕事、こんな風にしかやれないんだったら今からでも別の職場探してもらっていいよ。"
    else:
        sc "昨日任せておいた仕事も適当やって帰っちゃったし…{w}やる気がないなら今からでも別の職場探してもらっていいよ。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    show screen textbox with dissolve
    nar "シーキュレットは大股に部室へ歩く。"
    nar "人が悪いと言うならそこでおしまいにしてしまえば良いことを、あいつは酢につけ粉につけイラつく一言を必ず付け加える。"
    nar "おかげでさらに機嫌が悪くなる。そんなに急いでどこへ行くつもりだったんだ……"
    hide screen textbox with dissolve
    show SCG_03 0 with dissolve
    show screen textbox with dissolve
    if hssh_rkn == True:
        pl "おい、昨日のことだけど…"
        sc "…何が？"
        pl "いや…いい。朝っぱらから忙しいんだな。"
    else:
        pl "お前…俺を探してここまで走ってきたのか？"
        sc "…主教様の指示だったから。"
        pl "朝からお忙しいこった。"
    show SCG_03 8 with fastdissolve
    sc "お陰様でね。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    show screen textbox with dissolve
    nar "話が途切れる。{w}勿論、なんとかかんとか言ってみれば対話は続くだろうが、今はそんな気分ではない。"
    nar "気まずい空気のまま、二人分の足音だけが廊下に満ちる。{w}するとシーキュレットから先に話を掛けてきた。"
    hide screen textbox with dissolve
    show SCG_03 7 with dissolve
    show screen textbox with dissolve
    sc "今日は一段としっかり言動を慎んでもらうよ、{w}「お客様」がいらっしゃるから。"
    pl "お客様？{w}それって？"

    show SCG_03 8 with fastdissolve

    nar "そうやって、また黙ってしまう。{w}答えたくなければ最初からそう黙っていれば良かったのに、ヘン人め。"

    show SCG_03 0 with fastdissolve

    nar "俺のそういう不満を読み取ったように、シーキュレットがいきなり立ち止まってこちらに横目を使う。"
    nar "慌てる間もなく言葉が聞こえる。"
    sc "貢献者。{w}寄付金だけでなく直接的な物資の支援を手伝ってくれる方がいらっしゃるんだ。"
    sc "元々こういうのは保健部署が受け取って信者たちに分配するものなんだけど…"
    pl "だけど？"

    show SCG_03 8 with fastdissolve

    sc "…"
    pl "…ゴメン、{w}聞き取れなかったんだけどもう一回言ってくれるか？"

    show SCG_03 7 with fastdissolve

    sc "……何でもない。キミにわざわざ言う必要はなさそうだなって思っただけ。"
    sc "とにかくお客様の前ではさっきボクが言った通り行動しなよ。"

    show SCG_03 idle with fastdissolve

    sc "もし話を掛けてきたらマニュアル通り返事するだけで良いんだ。{w}向こうが興味を持ち始めたらすっごく…"

    show SCG_03 8 with dissolve

    sc "…面倒だから。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    show screen textbox with dissolve
    nar "こいつは声も小さいくせに言葉を濁してしまうから、何かを言う度に俺の耳に当たる。"
    nar "さっきもこいつ、話す途中に息抜きをしてからさらに声を落としたせいで、それを聞こうとした俺だけがひどい目にあった。"
    nar "ったく、ちっとも思いやりの無いやつだ。{w}面倒だあ？自己紹介か？"
    nar "実際俺は面倒な大人の相手をすることには自信があるから。"
    nar "人は年を食うと考えが単純になって、単純なる考えはそのまま人の言行を決する。"
    nar "適当に相槌打って煽ててあげれば、それほど扱いやすい人もいない。"
    hide screen textbox with dissolve
    stop sound fadeout 1
    pause 1
    if hssh_rkn ==True:
        scene bg14 with dissolve
    else:
        scene bg14_1 with dissolve
    call place14 from _call_place14_3
    $ renpy.music.set_volume(2, channel="sound")
    play sound "audio/se/door slide.ogg"
    show screen textbox with dissolve
    nar "部室の扉を開く前から、騒ぎが外へ漏れ出していた。シーキュレットが先に扉を開く。"
    nar "一緒に中に入ると、茶髪の女性が俺を見つけ、足音を立てながら俺に近づいた。"
    hide screen textbox with dissolve
    show SCG_101 0 with dissolve
    show screen textbox with dissolve
    lz1 "……"
    nar "女性は何も言わず、俺の前に立ち止まって俺をじっと睨む。"
    nar "シーキュレットはこちらへ横目を使っているようだったが、すぐ俺たちを通り過ぎて部室の中に入ってしまう。"
    lz1 "退いて。"
    nar "女性が気まずい雰囲気の中で先に口を切る。{w}先に近づいていきなり退いてって…{w}俺は聞き間違えたか分からなくて首をひねた。"
    nar "そうすると女性は、もっと不愉快な顔で、ゆっくりと、はっきりと言い直す。"
    show SCG_101 4 with fastdissolve
    lz1 "退・い・て、{w}って言ってるでしょ。{w}聞こえないの？"
    hide SCG_101 with dissolve
    nar "答える間もなく、彼女は肘で俺を突き飛ばし、外へ出た。"
    nar "道を遮ったわけでもないのにわざとこんなことを言うなんて、きっと悪意だろう。{w}俺は叩かれた方の腕をはたいた。"
    nar "力が入っていたとはいえ、所詮俺より結構小さい女の子だ。{w}が、{w}まるで不愉快が泥になりくっついたように気まずさが消えない。"
    nar "遅刻者が目立って何の得もないだろう。{w}もしやさっきよりももっと気まずいことが起きるかもしれない。{w}それだけはゴメンだ。"
    nar "慌ただしい人波を避け、足音を落とし、位置へ向かう。"
    nar "全くツイてないが、この不運さを自ら招いたことは知っているからこそ更に息苦しい。"
    hide screen textbox with dissolve
    show SCG_02 idle with dissolve
    show screen textbox with dissolve
    my "[na2]くん…？"
    nar "その負担感にため息を吐くと、隣でまるで鈴を転がすような声が聞こえてくる。"
    nar "今日は初めて会ったその懐かしい顔を見て、俺の顔色がすぐ明るくなっていくと感じた。"
    pl "あぁ、マヤ！{w}早かったじゃないか。"
    my "うぅん……[na2]くんが遅かったんじゃないかなぁ…{w}おねえちゃん、さっき出てっちゃったけど…"
    pl "そうそう、さっきすぐそこで会ったぜ。{w}普段より機嫌悪そうだったけど、何か言われたりはしてないよな？"
    show SCG_02 8 with fastdissolve
    my "…お話とかしてたわけじゃないんだけど…{w}わたしたち、[na2]くんが…あのおねえちゃんと一緒なのかなあって思ってたから…"
    nar "一瞬笑みが消える。{w}まさかその事をマヤから聞かれるとは全く想像もしていなかったからだ。"
    nar "明確ではないが、それでもはっきりと、彼女のイメージが浮かぶ。"
    nar "俺は慌てて表情を整え、口を切る。{w}その一瞬だけでもマヤが違和感を抱いたと思えば、さすがにぞっとする。"
    pl "あ…はは、その、俺はただ体調がちょっと悪くて。"
    pl "…枕が違うとなんだか寝付けなくなっちまって…{w}そう、アレだよアレ！時差酔い的な？"
    show SCG_02 0 with fastdissolve
    my "へぇ…"
    pl "それより！"
    nar "俺は一度手拍子をして、彼女に近づき身を屈める。{w}マヤは肩を震わせて、横目だった目を見張った。"
    nar "そんな姿を見て少しはすまないと思って、俺は声を落とす。"
    pl "今日ってなんかあるのか？{w}シーキュレットの野郎が言うにはお客様がいるとかどうとか…結構騒がしそうだったけど。"
    show SCG_02 0 at huruhuru
    my "あの…その…それがね…"
    stop music fadeout 2
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    pause 1
    show SCG_04 5 with slowdissolve
    pause 1
    show screen textbox with dissolve
    $ renpy.music.set_volume(0.5, channel="music")
    play music "audio/bgm/Grette.ogg" fadein 5
    nar "マヤは言葉を継がずに目を落とした。"
    nar "誰が見てもその姿は気まずいって感じなんだろうが、どうやらその理由が俺ではないようだ。"
    nar "彼女の視線を追うと、そこに小さい子がいた。{w}いつからそこにいたのか、マヤの腕を抱き込んでいた。"
    nar "見積もって130センチ辺りで、{w}綺麗に整えられたベビーブルーの長い縮毛の子だ。"
    nar "よくアイロンがかかった重い色の正装から、他の司祭からは見られない古めかしさが視界に漂う。"
    nar "その装いはこの場所とは全く似合わなく、{w}現実感は消え去り、まるで出来の良い人形のようだ。"
    nar "淑女はこちらを見つめている。{w}一体どこからいらっしゃった金持ちの譲さんなんだ。"
    pl "どちら様…？"
    nar "対話が成立する前に、まるで宝石のような目が光る。{w}淑女はあっという間に俺の腕を引っ手繰って、荒っぽく袖を捲った。"
    stop music 
    play sound "audio/se/hit.ogg"
    show SCG_04 4 with sshake
    nar "その衝撃で俺は淑女と一緒に倒れる様になったが、そんなことを意に介していないように手はさらに忙しく動く。"
    pl "うわっ？！"
    qus "う、"
    $ renpy.music.set_volume(1, channel="music")
    play sound "audio/se/hit.ogg"
    play music "audio/bgm/WTH.ogg"
    show SCG_04 1
    qus "うおあああーーー！！！" with sshake
    show SCG_04 at bounce
    qus "これぞ噂に聞いた暗色の肌！{w}黒曜石のように光る神々しい黒髪！{w}そして太陽のごとく情熱的に燃え上がる紅い瞳！！"
    qus "貴方こそが外部の方なのですね？！！"
    nar "大人しい顔立ちだけでは想像もつかないほどに声を高めた淑女は、まるで犬や猫を扱うように、"
    nar "明らかに「初めて見るモノ」への好奇心を剥き出した。"
    nar "腕から顔へ、{w}また顔から髪、{w}そして耳、{w}腹…{w}息をつく暇もなく続く手の動きに……{w}俺は恍けそうになった。"
    pl "ちょっ…"
    show SCG_04 4
    qus "わ～～！{w}わたくし、実際の外部の方なんて初めて見物致しました！" with sshake
    qus "肌はスベスベで弾力がありますね。{w}冷たくてちょっと固めなところが粘土を思わせます！"
    show SCG_04 5 with fastdissolve
    qus "全体的にがっちりしていますね、{w}やはり本で見た通り農耕社会の外部に適合する健康体です。"
    qus "身長は想像してたより小さいですが、腹は触るとちゃんとふわっとして…"
    show SCG_04 1 with fastdissolve
    qus "あれま！脂肪がついていますのね！今もしかして息我慢してます？{w}ほら力抜いて～！"
    show SCG_04 at bounce
    qus "爪も10本、これは基本ですね…{w}あ、{w}腕のこの包帯は普通の包帯なんです？解いてみてもイイですか？！"
    pl "あの…！"
    nar "口を開いた抵抗の瞬間を逃がさないとしている小さな両手が、今度は顎を掴んだ。"
    nar "その強圧なる行為に、ふと覚えのある感覚が浮かんだ。"
    nar "顔と背中、胸を撫で下ろすべたついた手の動き。{w}頬を押し口を開けさせた冷たい指。気が遠くなり、不快感が上がってきた。"
    show SCG_04 at bounce
    qus "舌と歯はこちらの人々と大差ない明色なんですね、素晴らしい！{w}個数も同じなのかしら？歯並びはちょっと不規則的で…"
    show SCG_04 4
    play sound "audio/se/hit.ogg"
    qus "ああ、探求の魂が昂ってきちゃいます！" with sshake
    play sound "audio/se/hit.ogg"
    qus "もし、時間あります？よかったら今すぐ薄暗いとこで二人っきり…" with sshake
    play sound "audio/se/hit.ogg"
    extend "やや、やっぱりここで一回脱いで貰えます？！" with sshake
    nar "こちんと固まった体に力を入れ、俺は彼女の手を荒っぽく振り切った。"
    stop music 
    $ renpy.music.set_volume(0.5, channel="music")
    play music "audio/se/raining.ogg" fadein 10
    play sound "audio/se/hit.ogg"
    pl "何やってるんだよ！俺はお前のペットじゃねぇ！" with vpunch
    show SCG_04 5 with fastdissolve
    qus "…あ…"
    pl "失礼だろ！いきなりあちこち触ってきたり、気持ち悪いんだって…！{w}いい加減にしろよ！"
    nar "勢いだけで吐き出した言葉は、自ら考えても慌てそうだ。{w}なんで俺はこんなチビを相手にイラついてしまったんだろう。"
    show SCG_04 at right
    show SCG_02 5 at left
    with dissolve
    my "ク、クレアちゃん…"
    hide SCG_04 at right
    hide SCG_02 5 at left
    with dissolve
    nar "騒がしい場はいつの間にか静かになっていた。{w}浄化部のやつらの視線を一斉に感じると、のぼせ上った頭は再び冷静に戻る。"
    nar "注目されること自体がしんどいってわけではないが、"
    nar "確かに俺くらいの大の男が女の子を脅かす状況は、どこから見てもみっともない様だ。"
    ex1 "うわ、怖～"
    nar "盛り下がった雰囲気に与するように、後ろで誰かが一言を言ってしまう。"
    nar "それに軽薄な口笛が続いて、俺はどうしようもないこの状況でただ息を整えた。"
    hide screen textbox with dissolve
    show SCG_02 0 at left
    show SCG_04 3 at right
    with dissolve
    nar "{nw}"
    show SCG_04 3 at huruhuru
    show screen textbox with dissolve
    qus "…ごめんなさい…"
    show SCG_02 7 with fastdissolve
    my "あのぉ…{w}ごめんね、こんなこと言う子じゃないんだけど…"
    show SCG_04 at bounce
    qus "いえ、マヤお姉さま。{w}今のは明白なわたくしの失敬でした。"
    show SCG_04 at center
    hide SCG_02
    with dissolve
    qus "申し訳ございませんでした、外地の民の御方。{w}ミオソティスの名を汚すような行為、誠に恥しく存じます。"
    show SCG_04 at huruhuru
    qus "どうかその怒りを鎮め、わたくしめを御許し頂けますでしょうか？"
    pl "いや、許しなんてそんな大層な…{w}そこまで怒ってないって。"
    nar "大袈裟だとも感じられる誤りを受け取ると、気の折れた顔がすぐ明るくなる。{w}分かりやすいお嬢さんだ。"
    stop music fadeout 1
    show SCG_04 0 with dissolve
    qus "ふむふむ！挨拶が遅れました。"
    $ renpy.music.set_volume(1, channel="music")
    play music "audio/bgm/daily.ogg" fadein 0
    show SCG_04 at bounce
    cr "わたくしはミオソティス家の自慢の長女、{color=#c9daf8}クリオネ・ミオソティス{/color}。"
    cr "普段はセイント・シェオルの貢献者として、また奉仕活動の一環として信者の方々が申請された補給品を直接調達しております！"
    pl "司祭の備品か…"
    nar "こいつがシーキュレットの言った客か？{w}想像とは全く違うが、なんで喧しいって言っていたのかは分かってきた。"
    hide screen textbox with dissolve
    show screen nvlbox with dissolve
    "\n 「多分既にお話であったかと存じますが、{w}正式に成人式を迎えずしては神殿の司祭には…」"
    "「…ので、{w}わたくしも毎回浄化班へ伺う際色んな新入員の方々と出逢いますが、その中でも皆さんは特別…」"
    "「…して、{w}神殿内の司祭様方はわたくしにとても良くしてくださるのです！ありがたい事に…」"
    "すぐ元気を出した少女は長々と言葉を並べ始めたが、なぜか俺は朦朧となってしまう。"
    et "何を話しているのか耳によく入らなくて、最後にはいくつかの文だけがようやく聞き取れた。"
    nvl clear
    "\n 「な～んだ、謝っちゃったの？お嬢様の割に口が軽いなぁ。」{w}「そうそう。いっつも変なもの弄ってるし、病気でも移ったらどうしちゃうの！」"
    "…のはずだったが、そのいくつかの言葉だけは鮮明に耳に入ってしまう。"
    "面白い見世物に満足でもしたように、何人かの司祭があのお嬢さんに話しかけて、{w}また通り過ぎる。{w}言葉の裏を読めなかったか、お嬢さんは照れくさそうに笑った。"
    "また何人かは俺へ視線を向けたが、俺はどんな顔をすれば良いのか分からなく、つい横を向いてしまう。{w}結構胸が焼けるな。"
    et "もしかしたらさっきの騒ぎでマヤが被害を受けたかもしれないって思って、彼女に目が向けられない。"
    stop music fadeout 5
    hide screen nvlbox with dissolve
    nvl clear
    show screen textbox with dissolve
    show SCG_04 5 with fastdissolve
    show SCG_04 at bounce
    cr "まあ！{w}わたくしったら、もうこんな時間！"
    cr "わたくしの話が長引いてしまいましたわ。研修生ですので刻一刻が大事ですものね。"
    show SCG_04 0 with fastdissolve
    cr "うん、うん。その気持ち、とてもわかります！{w}わたくしもまた、この神殿に居られる一分一秒がとても大切ですもの。"
    $ renpy.music.set_volume(0.5, channel="music")
    play music "audio/se/raining.ogg" fadein 10
    pl "…えっ？"
    nar "いつの間にか少女は、手慣れた身振りでスカートを握り、丁寧なお辞儀を口ずさんでいた。"
    show SCG_04 1 with fastdissolve
    cr "それでは外部の御方、またお会い致す時をお待ちしております。{w}その時までどうか御達者で！"
    hide screen textbox with dissolve
    hide SCG_04 with dissolve
    pause 1
    show SCG_02 idle with dissolve
    show screen textbox with dissolve
    my "ま、まって…"
    hide screen textbox with dissolve
    hide SCG_02 idle with dissolve
    pause 1
    show story07 with slowdissolve
    pause 2

    show screen textbox with dissolve
    nar "その時、俺はマヤと目が合った。"
    nar "マヤは時折、{w}実はよく、{w}眼差しを伏せ、遠くを見てしまう。{w}多分今ここから離れたい時の癖だろう。"
    nar "ここから逃げ、身を隠せる物陰を自ら作り出したってことだ。"
    nar "その証拠として、俺が彼女の薄いまつげに隠れた瞳を見た時、{w}彼女はただ頭を下げ、口を噤んでいた。"
    nar "その視線はどこへも向いていない。"
    nar "だが、{w}そのマヤが、たまには人をはっきりと見つめる時もある。"
    nar "とりわけ目を剥いて、困ると言いたそうに眉根をひそめる彼女は、なぜか何かを欲しがっているように見えた。"
    nar "確かにマヤが掴んだのは俺ではないのに、俺にそういう視線を向けるんだ。"
    nar "俺にはその訳が分からなく、またそれが聞けないままだ。"
    hide screen textbox with dissolve
    pause 1
    stop music fadeout 2
    scene black with dissolve
    pause 3
    show screen TrackCursor with dissolve
    show screen nvlbox zorder 1
    show screen grumbleBG12
    with slowdissolve
    pause 1
    image day3_10 = Text("……", slow=True, slow_cps=12 ,size=36)
    if config.language == "English":
        image day3_10_en = Text("......", size=27)
        show day3_10_en onlayer screens zorder 2 at truecenter, blur_1
    elif config.language == "SimplifiedChinese":
        image day3_10_cn = Text("……", size=28)
        show day3_10_kr onlayer screens zorder 2 at truecenter, blur_1
    elif config.language == "Korean":
        image day3_10_kr = Text("……", size=36)
        show day3_10_kr onlayer screens zorder 2 at truecenter, blur_1
    else:
        show day3_10 onlayer screens zorder 2 at truecenter, blur_1
    pause 0.7
    show ctc_ent onlayer screens zorder 2 at day3_10_ctc, blur_1
    $ _dismiss_pause = True
    $ renpy.pause()
    $ _dismiss_pause = False
    hide screen grumbleBG12
    hide screen nvlbox
    hide day3_10 onlayer screens
    hide day3_10_en onlayer screens
    hide day3_10_cn onlayer screens
    hide day3_10_kr onlayer screens
    hide ctc_ent onlayer screens
    hide screen TrackCursor
    with dissolve
    $ renpy.music.set_volume(0.5, channel="music")
    play music "audio/se/raining.ogg" fadein 6
    pause 1
    if hssh_rkn ==True:
        scene bg13 with dissolve
    else:
        scene bg13_1 with dissolve
    call place13 from _call_place13_2
    show screen textbox with dissolve
    nar "……"
    hide screen textbox with dissolve
    show screen nvlbox with dissolve
    "\n 足下に何かが転がり込む。{w}目を落として確かめてみれば人の首だ。{w}見開いたまま息は途切れ、凸凹の断面の、{w}名の知らない誰かの首。"
    "出張った舌に真っ白のカビが生えている。{w}俺はあまりにも不意な状況に体が固まり、悲鳴も出せず、{w}その光景から目が離せなくなっている。"
    stop music fadeout 3
    et "…しかし突然、首が視界から消えてしまう。{w}誰かに取り上げられたってことだ。"
    hide screen nvlbox with dissolve
    show SCG_03 idle with dissolve
    show screen textbox with dissolve
    $ renpy.music.set_volume(1, channel="music")
    play music "audio/bgm/daily.ogg" fadein 3
    sc "何をボーっと突っ立ってるんだい。"
    pl "え、あ？"
    show SCG_03 8 with fastdissolve
    sc "はぁ…{w}頭がそこまですっからかんだと詰め込めるものが多そうで羨ましいね。"
    nar "湿っぽい袋に首を投げ込むシーキュレットを見て、周りを眺め回す。"
    nar "家具の跡だけを残して堆く溜まった塵、視線の至る所に咲いた浅黒い跡形。{w}段々と焦点が合っていく。"
    if hssh_rkn == True:
        pl "死体を切ったのに血が出ないな。"
        sc "…腐っている肉片に血が流れるわけないだろう。朝礼の話ちゃんと聞いてるのか？"
        pl "そうか？おかしいな…"
    else:
        sc "…だからといって、仕事中に余所見をされちゃあ困るな。"
        pl "仕事…中？マヤは？"
        show SCG_03 0 with fastdissolve
        sc "その子なら貢献者さんの荷物を持つって口実で午後の業務から逃げただろう？"
        sc "浄化部の仕事は途中からの参加は難しいんだし、今日は多分保健部署の仕事をずっとお手伝いしてるだろうね。"
        pl "そうだっけ？流石マヤ、八方美人じゃないか……"
    show SCG_03 9 with fastdissolve
    sc "…今の話聞いてました？{w}ほんと、何考えてんだか…"
    stop music fadeout 4
    hide screen textbox with dissolve
    nvl clear
    hide SCG_03 with dissolve
    show screen nvlbox with dissolve
    "\n 神父様、{w}と人の後列の塞がれた出入り口から、青年の細い声が聞こえてきた。"
    "真っすぐな声で答えたシーキュレットが、ついて来いと言わんばかりに目線を送る。"
    play music "audio/bgm/dialogue.ogg" fadein 3
    "死体が発見されてから三、四時間。{w}興味を失った見物人どもが散って、道が開いた。"
    "家跡の周りをうろうろしていた青年は、俺たちが出てきたところに及び腰で歩いてきた。"
    "さっきの死体の首、それは確かに老人だった。{w}そしてこの青年の顔から、少しはあの老人が見えてきた。"
    "今度の「処理」の対象は、青年の年老いた父上だろう。"
    et "口を隠した布を下したシーキュレットは、{w}簡単な状況をいくつか知らせ、整理した遺品を持ち出す。"
    nvl clear
    "\n 死因は心臓麻痺のショックで、寒い日が続くせいで多くの年老いた人が命を落とすって言っている。{w}家が広くなかったから、持ち物も多くなかった。"
    "額縁の写真を見た男は大きく体を震わせ、すぐ目を落とした。"
    "俺はこの男のことは見たことがないが、悲しみよりも苦しみを先に感じてしまう姿を見れば大体分かる。"
    "父上の死をただ悼んでいる場合ではないのだろう。{w}多分彼には今後も別の問題が残っているだろうから。"
    "「どう致しましょう。」"
    "「ごめんなさい、すべて処分してください…」"
    et "声を戦かしながら苦しんでいる男に、{w}シーキュレットは「分かりました」以外は何も言わない。"
    hide screen nvlbox with dissolve
    nvl clear
    show screen textbox with dissolve
    nar "家から出れば、{w}シーキュレットは小さいスプレーみたいなものを取り出し振りまいて、腕だけを伸ばして俺にも渡してくれた。"
    nar "どうしたものか今度はすぐ説明をつける。"
    show SCG_03 7 with dissolve
    sc "香料を入れた軟膏。"
    pl "…ってことは、脱臭剤？"
    sc "こんなので消しきれはしないけど、まあ形式美程度さ。事務室にいくつか取り揃えてあるから次からは自分で持ってくること。"
    pl "へぇ…"
    pl "お前、外だとよく喋るじゃないか。{w}普段もそんな感じにしときゃもっとマシだろうに。"
    sc "……"
    pl "…そんな顔すんなって、冗談だろうが。"
    show SCG_03 8 with fastdissolve
    sc "…笑ってるのも今のうちだろうな。"
    pl "は？"
    show SCG_03 0 with fastdissolve
    sc "早く準備して、そろそろ神殿に戻るから。"
    nar "少しは雰囲気を和らげたと思ったのに、やはり彼のその怪しからん癖が出てくる。"
    nar "でも実は、彼との話は退屈なだけ、不愉快とは感じていない。{w}浄化部の女二人を相手にした時とは全く違う。"
    nar "あの女たちと話す時の俺は、自分だけの一方的な気まずさを感じてしまうが、{w}むしろシーキュレットは俺を面倒がっているようだ。"
    nar "彼と話す度の気まずさはそこから始まる。"
    nar "意味深な言葉を投げて人を揶揄う趣味でも持ってない以上、俺に不満があるってことが確かなのに、"
    nar "いつも曖昧なところで対話を断ってしまう。"
    nar "俺は、彼にもらった脱臭剤を振りまく前に、まずその匂いを嗅いだ。"
    nar "花よりは浅く、草よりは響く香りだ。{w}やっぱり、覚えのある匂いだ。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    show screen nvlbox with dissolve    
    "\n 彼への不満を繰り返し考えながら後ろを追うと、{w}ぱしゃ、っと。頭に衝撃が走る。"
    "何かに当てられたのか？{w}痛みに代わり広がる冷たくて湿っぽい感覚のせいで、状況が分かり難い。" with hpunch
    "さっきまでの香りは影も形もなく消え、酸っぱい匂いが浮かんできた。"
    "「汚らわしい司祭共め！{w}貧しい人から巻き上げた税金で肥えることしか考えてない無能なクソったれ共がどのツラ下げて日の下歩いてんだ！」"
    et "後ろからがつがつしい男性の声が聞こえる。なぜかすごく腹を立てている。"
    nvl clear
    "\n 俺は手をゆっくりと上げ頭を探った。{w}何かの果実だ。{w}俺は今、誰かが投げた腐った果実に当たったってことだ。"
    "それに気づいても、この全てがまだ実感できない。{w}男性はもう聞き取れないほど発音を崩しながら声を張り上げていた。{w}が、悪口だってことは俺にも分かる。"
    "彼から次々と、一瞬で周りは騒がしくなってきたが、只自分たちでひそひそと話しているだけで、誰一人も前へ出ようとはしていない。"
    "「申し訳ございません。」"
    et "お先が真っ暗になるところに、シーキュレットが前へ出る。{w}彼はこんなことに慣れたのか、男へ近づいて頭を下げる。"
    nvl clear 
    "\n 「申し訳ございません、我々の不甲斐なさに皆様へご不便をお掛け致しました。{w}精進致します。」"
    "「精進だぁ？{w}貴様らがそこらに座り込んで口ばっかり叩いてる間俺の娘は死んだんだ！"
    "枢機卿の下で泥靴を舐めて温存した自分の身が惜しくて死んでいく人たちを傍観してきたのか！{w}この恥知らずの乞食めが！」"
    "「申し訳ございません、誠に申し訳ございません。」"
    "「無念にも死んでいったご老体に沸く蛆虫の方が貴様よりは綺麗だろうよ。"
    et "貴様らにほんの少しでも信仰心というものが残ってるならその存在こそが神に対する冒涜だと知れ！」"
    nvl clear
    "\n 激しい息の男性がシーキュレットを突き放し、彼が離れてから立ち止まった村人たちもわらわらと散っていった。"
    et "深々と下げた頭を上げた彼は服から土埃を打ち払った。{w}振り向くと目が合ったが、いつもと同じ顔だ。"
    hide screen nvlbox with dissolve
    nvl clear
    show SCG_03 8 with dissolve
    show screen textbox with dissolve
    sc "行こう。"
    pl "ちょ、ちょっとちょっと…{w}今のは何だったんだ？"
    sc "見て分からないのかい？{w}これこそ神殿の外で言動を慎むべき理由だよ。"
    sc "目に付いたならとにかく謝るのが最善さ。{w}ああいう人たちは大体とても気が立ってるから、余計な事を口に挟んだら…"
    pl "いやいや、そういうのを聞いてる訳じゃねぇんだよ！{w}一体俺たちが何したってんだ？初対面の人にこんな…"
    show SCG_03 2 with fastdissolve
    sc "はぁ…"
    sc "キミが今までどんな生き方をしてきたのかはわからないけど、ここはキミのおうちじゃない。"
    sc "皆が皆キミのことを好きになるなんて無理なんだよ。"
    sc "そして、中にはキミの行動に関係なく悪意を晒す者も居る。{w}そこに理由なんかは存在しないのさ。"
    pl "そ…そういう問題じゃないだろ…"
    show SCG_03 0 with fastdissolve
    sc "何が違うんだ。{w}ないったらない、これ以上どう説明すればいいんだい？"
    hide SCG_03 with dissolve
    nar "神殿と今の枢機卿に不満を抱いている人たち。{w}怪しいほど入り易い新設の部署。{w}劣悪な作業環境。"
    nar "頭の中でパズルが段々と完成されている。"
    pl "浄化部は神殿が差し出すデカい恨みの受け皿なんだな。"
    nar "先立って歩くシーキュレットは只黙っている。{w}多分正解だろう。"
    nar "もしそうであれば、他の部署に比べて明らかに水準が低いってことも分かりそうだ。"
    nar "国の為に必須な存在、処理班。{w}俺は今更その真意を分かった気がする。"
    hide screen textbox with dissolve
    if hssh_rkn ==True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    call place02 from _call_place02_1
    show screen textbox with dissolve
    show SCG_03 7 with dissolve
    pl "よくこんなところで働こうって思ったな…"
    sc "…何度も言うけど、慣れる自信がないなら今からでも別の職場を探した方がいいからね。"
    sc "実際今日までの君たち新入員の業務能力は居ない方がマシに思えるぐらいだし。"
    pl "仕事も仕事だけど、それよりかきゅ～くんのその嫌味の方が断然キツイんですけどね！"
    show SCG_03 2 with fastdissolve
    sc "…ヒトを変なあだ名で呼ぶな。"
    show SCG_03 0 with fastdissolve
    sc "こっちは今朝キミがやらかした不作法の収拾で業務のスケジュールもめちゃくちゃなんだよ。"
    sc "キミのお粗末な処理能力に賠償を要求するのも無理だろうし、今回は仕方ないとするけどさ。"
    pl "お前って奴は一々嫌味ばっかだよなぁ～…"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    pause 1
    "{nw}" with sshake
    show screen textbox with dissolve
    pl "…おい、シーキュレット、ちょっと。"
    sc "？"
    nar "怪しい騒ぎにぴたりと立ち止まった。{w}原因を探した視線が止まったところに、同じ年に見える二人の子供がいた。"
    nar "浄化部で何度か見たことのある顔だ。{w}声も名も知らないが、そんなことはどうでもいいほど雰囲気がやばい。"
    nar "ここまで聞こえてくるほど声を荒立て悪口を交わしていたら、つい一人が他のやつの顔をぶん殴った。"
    pl "おいおい…これ結構ヤバいんじゃ…{w}主教様とか誰か呼んできた方がいいんじゃねえの？"
    show SCG_03 72 with dissolve
    sc "…あれが何？{w}あと、あの人を呼んだって何の役にも立たないよ。{w}神殿が保育園でもあるまいし。"
    pl "「あれが何」って…{w}どんな状況でも暴力が許される訳ないだろうが！"
    show SCG_03 8 with fastdissolve
    sc "はぁ…こんな些細な事で騒ぎ立てるなってことだよ。{w}キミが余計探りそうだから言っとくけど、あの二人は元々仲が悪かったんだ。"
    sc "あの二人だけじゃない、良くある事さ。{w}ここの人たちは皆常に気が立っているんだし。"
    sc "ああいう風に自分たちで勝手に解決してくれりゃこっちは助かるもんさ。{w}ボクにまで被害が及ぶのは御免だしね。"
    sc "キミも面倒事に巻き込まれたくなかったらそうやって露骨に視線をやるのはやめた方がいいよ。"
    pl "お前…{w}何をそこまで言う事ないだろ、お前ってその…{w}委員長とか、そういう感じじゃなかったのかよ。"
    show SCG_03 0 with fastdissolve
    sc "…ボクはキミたちみたいな阿呆どもの尻拭いをしてやるために神殿で働いてる訳じゃないんだよ。"
    nar "シーキュレットは言い切ってすぐ速足で場を離れる。{w}俺は仕方もなく彼に付いて歩いていくが、彼たちから全く目が離せない。"
    nar "俺たちが口喧嘩をしている間に、あっちの方はさらに深刻になった。"
    nar "右のやつが別のやつの上に乗り上がって首を絞め、{w}下のやつはボロボロに潰れた顔で、"
    nar "折々抵抗でもしているように藻掻いている。"
    nar "床は段々と血塗れになっていく。{w}なのに、この騒ぎから目が離せないのは、本当に俺だけのようだ。"
    nar "もう動かない相手への拳が振り上げられたその時、ふと横を向いた彼と目が合う。{w}もうあれは、只の狂人の目だ。"
    ex1 "おい、何見てんだこのカスが！死にてぇのか！"
    show SCG_03 7 with fastdissolve
    sc "ほら見ろ、大分イカれちゃってる。"
    pl "……"
    nar "歩幅を狭めて先に歩いていたシーキュレットが、後ろに首を回して、空笑いをして一言を流した。"
    nar "俺はどうしても気が差して、何度も後ろに振り返ってみるが、今俺にできることは無かった。"
    nar "再び息苦しさが上がってくる。{w}俺はそれを抑える為に、足を速めた。"
    hide SCG_03 with dissolve
    hide screen textbox with dissolve
    if hssh_rkn ==True:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03_6
    show screen textbox with dissolve
    nar "シャワー室が近くなると徐々に安定が戻ってくる。{w}まさか俺がこの湿っぽい空間を懐かしむとはな。"
    nar "一方、シーキュレットは歩度を緩めては、俺の後ろに立ち止まる。"
    pl "おい、これ服にも付いちゃってるか？"
    show SCG_03 7 with dissolve
    sc "…ちょっと跳ねてるね。"
    pl "マジかよ…{w}髪の毛に臭いとか染み込んでなきゃいいけど。"
    nar "話しながら狭苦しいボタンを一つ一つ外して両脚を抜き出す。{w}これ以上何かが頭に触る感触だけは避けたかったからだ。"
    nar "俺は、まるで虫のもぬけのように床に垂れたスータンを折り畳んで、そのままシーキュレットに投げ飛ばした。"
    nar "見た目より結構重い服で、いきなり受け止めたシーキュレットは一瞬バランスを失いよろよろした。"
    pl "それも一緒に洗っといてくれるか？"
    show SCG_03 0 with fastdissolve
    sc "はぁ…？{w}なんでボクが…"
    hide SCG_03 with dissolve
    nar "不満を言おうとしたシーキュレットが一瞬目を丸くして止まる。{w}どこかへ向かっている視線は、恥ずかしいが俺への視線だ。"
    nar "俺はいつも両腕に包帯を巻いておくが、これは只傷跡を隠す為だった。"
    nar "暗い肌で明らかに目立ってしまう、真っ黒の傷跡は細く、{w}また太く、{w}数々の筋に割れ、"
    nar "まるで血管が外に突き出たようにも見えた。{w}別に痛かったことはなかったし、触ってみれば屈曲があって、中は滑らかだ。"
    nar "幼い頃からあったので、もう自らは不思議だとは思っていないが、他の人から見れば驚くべきの姿だってことは事実だ。"
    nar "今朝、クレアが部署の真ん中で包帯を解かなくてよかったと思っている。"
    show SCG_03 7 with dissolve
    pl "これ、俺がすごく小さい頃からあったんだ。"
    pl "村の人々が言うには腕を思いっきりぶつけて出来た傷痕らしいけど…{w}あんま小さい頃の出来事だしよく覚えてないんだよ。"
    show SCG_03 72 with fastdissolve
    show SCG_03 at bounce
    sc "…それが傷？"
    pl "そう。カッコイイだろ？"
    show SCG_03 8 with fastdissolve
    sc "……"
    nar "いつもの味気ない顔に戻ったシーキュレットは、何も言わずに俺の腕をじろじろ見ては、目尻を細く震わせた。"
    nar "不思議だと思っているのか？{w}そっちから先に俺に興味を持つなんて、俺としてはそっちの方がもっと珍しいと思うが。"
    pl "お前はシャワー室入らないのか？"
    show SCG_03 7 with fastdissolve
    sc "ボクは…{w}キミの次にいくよ。"
    pl "どうして？"
    show SCG_03 8 with fastdissolve
    nar "シーキュレットは、ぶら下げている俺のスータンの布をぎこちなく触って、惑っているようにぼんやりした顔をする。"
    nar "そして目をくりくりさせ、また俺を見つめた。"
    show SCG_03 0 with fastdissolve
    sc "キミと並んで水を浴びるのはイヤだから。"
    nar "確固とした答えに比べて表情はまだぼんやりしている。{w}それが妙だとは思ったが別に気にしていない。"
    nar "俺もあいつと仕切りの無いシャワー室にたった二人だけで入るのは正直嫌だから。"
    pl "そっか。じゃあいいや。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    show screen nvlbox with dissolve
    "\n お互い様で短い返答を返して俺は一人でシャワー室に入る。"
    "隅っこで誰かが壁にくっついて泡をつけていた。{w}幸い、俺に関心はなさそうだ。"
    "上から降り注ぐ冷たく激しい水流。{w}纏わりついた髪に悠々と指を入れる。{w}落ちた汚染物は水に溶けて消える。"
    "冷やした頭で、村の風景を再び思い浮かべる。{w}親族を失った悲しみに苦しみ、怒りを見せた人たち。"
    et "彼たちが、力のない司祭に当たり散らすことにも、多分理由があるだろう。"
    nvl clear
    "\n ルーズな仕事の処理への不満、自分もいつかはそんな死を迎えてしまうという恐怖。"
    "誰もが知っている。それは確かに、単なる処理班の立場では無視すべき理由だった。"
    et "訳がないってわざわざ強調した彼の冷たい忠告がまた鮮明になってくる。"
    stop music fadeout 3
    hide screen nvlbox with dissolve
    scene black with dissolve
    pause 4
    if hssh_rkn ==True:
        scene bg01 with dissolve
    else:
        scene bg01_1 with dissolve
    call place01 from _call_place01_3
    show screen textbox with dissolve
    play music "audio/bgm/daily.ogg"
    pl "…ん？"
    show SCG_03 7 with dissolve
    sc "随分早かったね。"
    pl "お前…{w}友達いないだろ。"
    show SCG_03 0 with fastdissolve
    sc "…変な誤解しないでくれるかい。{w}倉庫の後片付けがあるから待ってただけだよ。"
    pl "えっ、まだ仕事が残ってるのか。"
    sc "今日からは帰ったあと他の引継ぎの教育もあるって事前に言ったじゃないか。"
    pl "初めて聞きましたけど。"
    show SCG_03 2 with fastdissolve
    sc "…あいつら……"
    pl "直接口に出して言ってくれないからそうなるんだよ。"
    sc "……"
    show SCG_03 0 with fastdissolve
    sc "だからと言って勝手に抜けてもらうと困るよ。{w}元々はあの女の子も一緒にしなきゃいけない事だったのに。"
    pl "かしこまりー{w}って言いたいとこだけど…"
    pl "大変申し訳ないことに俺は今日魔導部主教様のお呼び出しで神殿に戻ったらすぐ御会いしに行くことになってるから。"
    show SCG_03 2 with fastdissolve
    sc "聞いてないんだけど。"
    pl "そりゃまだ言ってなかったからな。"
    pl "ほらね、ちゃんと言うのが遅くなるとこういう事が起きるんだよ。"
    pl "信じられないなら一緒に行くか？{w}浄化部主教様も多分その辺にいると思うけど。"
    show SCG_03 9 with fastdissolve
    sc "……はあぁ…"
    show SCG_03 0 with fastdissolve
    nar "眉をひそめて俺を睨んでいたシーキュレットは、{w}まもなく鋭い視線をそらして、やれやれと首を振った。"
    nar "噂と関係があるかもしれないが、彼が主教に関した何かの弱点を持っていることは確実だ。"
    nar "だが、今の俺が気にすることではなかった。"
    show SCG_03 at bounce
    sc "これからは日程に支障をきたすような別の用事がある場合はちゃんと事前に報告すること。{w}いいね？"
    pl "はいはい、あんがとさん。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    pause 1.0
    show screen textbox with dissolve
    nar "別に返答もなくすぐ部署へ歩いていく彼の後ろ姿が、今日に限った事でもないが尚更気に入らない。"
    nar "俺は一瞬立ち止まって、しばらく彼を見つめては、すぐ反対側に向き直った。"
    hide screen textbox with dissolve
    stop music fadeout 3
    if hssh_rkn ==True:
        scene bg107 with dissolve
    else:
        scene bg107_1 with dissolve
    call place107 from _call_place107
    nvl clear
    play music "audio/bgm/map select.ogg" fadein 3
    show screen nvlbox with dissolve
    "\n 魔導部室に自ら入るのは今度が初めてだが、幸いにも迷わずに着けた。"
    "魔導部は部室さえその上のない名声を誇っていたからだ。"
    "埃のついていないカーペット、中央の巨大な円卓、暗い背景と混ざり、傲慢な光を出す金色の装飾。"
    "浄化部の見窄らしい部室と比べていれば、なんとなく空笑いが出てくる。"
    "とんとん、{w}「入りたまえ。」{w}心のうち、人のいない光景を頭に思い浮かべたが男性のどっしりした声は身元も問わずに俺の出入を許した。"
    et "特に高く見える背もたれに寄って座った彼は、客が入ったのにも関わらず一方も動かないまま、只持っている書類に視線を向けている。"
    nvl clear
    "\n 息をついた男性は顔を上げて俺を見ると固まった口元を和らがせた。"
    "「ほぅ、貴様か。{w}いいだろう、近う寄りたまえ。」"
    "ひときわ重たい空気自体は安定感があるが、今はその重さが重圧感に化け、わけもなく心を押さえつけてくる。"
    "{color=#6d9eeb}エルジェーベト・アルタナータ{/color}。{w}彼は、一目で「男性」か「男」と呼ぶには多少無理があるほど幼児の姿の主教だ。"
    et "俺がまだ州都の外、村にいた頃、突然の「客」としてやってきた彼はまず彼自身の外観の説明をしてくれた。"
    nvl clear
    "\n 神の力を借りて魔力を使う者はおおよそ相当の対償を払うことになる、それはずっと昔から大人たちから聞いていた。"
    et "だから彼の外観は只適応の問題だけで、納得し難いわけではない。"
    stop music fadeout 3
    hide screen nvlbox with dissolve
    nvl clear
    pause 1
    show SCG_09 idle with slowdissolve
    pause 2
    show SCG_09 idle at er_stand
    play music "audio/bgm/anyway high person.ogg"
    show screen textbox with dissolve
    er "無事到着したという報告は聞いてあったが…"



    show SCG_09 4 zorder 0 with newfastdissolve


    extend "こうやって面と面で向かうのはあの日以来だな。"
    pl "ホントだよ、先にこっちに来いとか言ったクセに何の事前打ち合わせもなしに知らない部署に放置されちゃってさ。"
    pl "話が違うだろ～？どうなってるんだ？"

    show SCG_09 idle with fastdissolve

    er "ふむ、説明が足りてなかったか。"
    er "今現在貴様の所属している「処理班」というものは、元々我々魔導部直系の附属部署だった。{w}昔は連携もされていてな。"

    show SCG_09 8 with fastdissolve

    er "本来、血統と縁を重視する我々魔導部で州都の地理すら把握されていない外部者を受け入れるというのは"
    er "異例、という言葉では足りない程の出来事だったのでな。"

    show SCG_09 idle with fastdissolve

    er "手順としては適切かと思ったのだが…"

    show SCG_09 4 with fastdissolve

    er "やはり多少なり不満はあったか。"
    pl "だから処理班か…"

    show SCG_09 9 with fastdissolve

    er "無論、{w}俺とて貴様をあの下劣極まりない雑種共の巣窟に置いていく形になってしまい実に不愉快だが、"
    er "こればかりは仕来りなのでな。"

    show SCG_09 idle with fastdissolve

    er "あちらの下品なやり方に慣れないと良いのだが。"
    pl "ふーん…{w}主教様は大分浄化班が嫌いなんだな。"

    show SCG_09 11 with fastdissolve

    er "嫌い、だと？"

    show SCG_09 4 at er_stand with fastdissolve

    er "はっ、{w}その程度の価値すら無い！{w}あんなモノに気を遣う暇なんぞ存在しない位には俺も忙しくてな。"

    show SCG_09 9 with fastdissolve

    er "誤解はしないで頂きたいな。{w}俺は私的な感情で相手を排斥しようとはしない。"

    show SCG_09 8 with fastdissolve

    er "全ての事柄には相応の理由があるのだ。{w}理解したか？"

    show SCG_09 idle at er_stand with fastdissolve

    nar "嵩の高い口振りで、態度は保守的といえるが、人の陰口をたたくって、部署の女の子とほとんど同じだ。"
    er "何をじっと見つめている？{w}物言いたげそうではないか。"
    pl "いや、まあ。{w}何で子供の姿なのかが気になって。"

    show SCG_09 9 at er_stand with fastdissolve

    er "切実にまで願う物があったからこそそれ相応の対価を受け入れただけだ。{w}今はその影響で永久に時の流れを逆らい続けているな。"
    pl "うーん…{w}簡単に言えば逆戻りしてるってワケか。"

    show SCG_09 4 with fastdissolve

    er "正解だ。{w}大体だがな。{w}流石目の敏い…俺の目は間違っていなかったという訳だ。"
    nar "何から始まっても最後は自賛だな、それだけは尊敬すべきの大人だ。"

    show SCG_09 9 at er_stand with fastdissolve

    er "なに、遅かれ早かれたったの一週だ。"
    er "正式に司祭となるまで貴様がやるべき事は、この神殿の地理や知識を最大限身に付けておく事。"
    er "業務の遂行に慣れておく事、{w}そして俺のアルネから成るべく多くを学ぶ事。"
    er "以上だ。{w}他は貴様の気にする事でない。"
    pl "へぇ。{w}主教様はここじゃ結構なお偉いさんって聞いたけど、俺には親切にしてくれるじゃないか。"
    pl "ここまでしてくれる理由ってあるのか？"

    show SCG_09 idle with fastdissolve

    er "当初から言った通り、我々魔導の存続には貴様が必ず必要であるからだ。"
    er "今はその為りだが…{w}一度我々魔導部に無事編入し、実績を重ね、信仰を集めてさえくれれば、"

    show SCG_09 9 with fastdissolve

    er "アルネの相手として不足分はないだろう。"
    pl "ちょ…{w}ちょっと待て！相手って……{w}結婚の？"

    show SCG_09 idle with fastdissolve

    er "然様。{w}理解が早いな。"

    show SCG_09 9 with fastdissolve

    er "我がアルタナータが長い歴史を重ねながらもこの座を守る事が出来た理由……{w}それは群を抜いて優れた神聖力にある。"
    er "そしてその力は貴様にも流れているのだ。"
    pl "神聖力って言っても…{w}俺の聖痕はたったの二つなのに？"

    show SCG_09 idle with fastdissolve

    er "貴様の可能性に期待している、ということだな。"
    pl "可能性…"
    nar "どうしたものか気になっていたが、思ったよりもとんでもないことだった。"
    nar "初見の大人の突然の勧誘を、説明も聞かずに受けて、ここまで来た俺も俺だが、"
    nar "無謀な可能性に何人かの人生をかけるこの人もなかなか肝が太い。"
    nar "いや、{w}そこまで魔導部は差し迫った状況、ということか。"
    pl "ここまで良い事言ってくれたとこ申し訳ないんだけど、もし俺がそれに答えられなかったら…{w}どうするんだ？"

    show SCG_09 8 with fastdissolve

    er "応えられなかったら、か？{w}ふむ、面白いな。{w}この俺が、ここまでして貴様に機会を与えてやると言っているんだ。"

    show SCG_09 4 at er_stand with fastdissolve

    er "そこに応じられないなど弱音を吐く愚か者は居ないだろう。"
    nar "少しずつ圧迫してくる声が部屋に響く。{w}肩を抑えつくてくる負担感が重たい。"
    nar "神経に障ることがいくつもあったが、{w}我慢しなければ、ここで終わりだ。"
    pl "そっか、ありがとな、主教様。{w}じゃあ俺はこの神殿内なら勝手にうろついててもいいってことなんだよな？"

    show SCG_09 9 with fastdissolve

    er "多言無用。{w}このエルジェーベト・アルタナータが貴様に保証しよう。{w}出入りは自由にしても構わない。{w}だが…"

    show SCG_09 8 with fastdissolve

    er "神殿には頭の可笑しい輩しか居ないのでな、あまり関わらない方がいいだろうが…{w}特別気に入った場所でもあるのか？"
    pl "別にそういうわけじゃないんだけど…{w}神殿には面白い場所が多いだろ？{w}鍛練室とか、医務室とか、図書館だったりさ？"
    er "癒す傷もない者が迂闊に医務室を出入りするでない。{w}彼らの怠惰が貴様の刃を脆くするだろう。"

    show SCG_09 11 with fastdissolve

    er "しかし図書館か、そうか…{w}貴様は確かに州都の知識が足りていない、その知識を補うことは大切だな。"

    show SCG_09 8 with fastdissolve

    er "ただし学術部の輩は常に詩を詠う、それは注意したまえ。"
    pl "詩…？"

    show SCG_09 9 with fastdissolve

    er "これは流石に理解しきれなかったか。{w}俗に言えば奴らの頭はイカれているということだな。{w}あそこは蛇の巣窟のようなものだ。"

    show SCG_09 idle with fastdissolve

    er "後は…{w}ゴホン、{w}先程も言ったように俺の姪、アルネとは親密な関係を築くように。"
    pl "そうしとくぜ。"
    er "いい返事だ。{w}そろそろ下がりなさい。"
    nar "俺の答えに満足したのか、彼は書類を手にする。"

    show SCG_09 9 with fastdissolve

    er "今日も互いに愛し合うのだぞ。"
    stop music fadeout 3
    hide screen textbox with dissolve
    hide SCG_09 9 with dissolve
    pause 1
    if hssh_rkn:
        scene bg03 with slowdissolve
    else:
        scene bg03_1 with slowdissolve
    call place03 from _call_place03_7
    show screen textbox with dissolve
    nar "扉を閉めて出ていくうちに、無理して上げていた口角が小刻みに震える。"
    nar "俺は我慢した息をようやく吐き出した。{w}なかなか幼く見えて少しは可愛げのある人だって思ってたのに、中身は全く酷いジジイだ。"
    $ renpy.music.set_volume(1, channel="sound")
    hide screen textbox with dissolve
    show SCG_08 0 with dissolve
    show screen textbox with dissolve
    play music "audio/bgm/daily.ogg"
    play sound "audio/se/ding.ogg"
    show SCG_08 0 at bounce
    en "ああ！ここにいらっしゃったんスね！{w}やあ～ずっと探したんスよ？"
    nar "疲れた足を引きずって外へ出るうちに、いつ来たか背の高い男性が、懐かしむように声を上げた。"
    pl "あれ、昨日会った…{w}俺をずっと探してたって？"
    show SCG_08 1 with fastdissolve
    en "そーそ、聞けばこっちの主教様と面談があったじゃないッスか、{w}昨日パッと見なんにもわかんなそうだったんで……"
    en "本当に心配したんスよ～？"
    show SCG_08 0 with fastdissolve
    en "お話、終わったんスかね？{w}あの主教様と個人面談だなんて、これまたご苦労ッスねぇ…"
    show SCG_08 at bounce
    en "でも[na]さんはかな～り偏愛されてる方なんスよ？{w}僕なんか想像するだけで胃がイガイガするッス…"
    pl "マジかよ…"
    pl "正直言って未だに状況が呑み込めてないんだよな。{w}それが何の特になるのかも分からないから胸も張れないだろうが…"
    pl "本当にこのままで大丈夫かよ…{w}てか、俺は神殿が何なのかすらわかってなかったんだって！"
    show SCG_08 10 with fastdissolve
    en "魔導の血統って事実自体が最大事ッスからね。{w}それだけで理由は充分ッスよ。"
    en "信じるか信じないかを差し置いて神通力は貴方を選んだんスよ。{w}[na]さんは間違いなく魔導の人間ッス。"
    show SCG_08 0 with fastdissolve
    en "だからちゃんとその力にそぐうよう自身の言動や態度を戒めるべきッス。"
    show SCG_08 1 with fastdissolve
    en "今朝もクリオネお嬢さんに大声出したらしいじゃないッスか。"
    pl "げっ、{w}何処でそれを？！" with sshake
    show SCG_08 0 with fastdissolve
    en "神殿は噂が流れるのが早いんスよ。"
    show SCG_08 7 with fastdissolve
    show SCG_08 7 at huruhuru
    en "特にクレアお嬢さん！{w}彼女は一瞬で他人のプライバシーを丸裸にしちゃうッスからね。"
    show SCG_08 0 with fastdissolve
    en "でもクレアお嬢さんはここで遊ぶのが好きだし、{w}まだ神殿に残ってるかもッスよ？"
    pl "ふぅん……"
    pl "で？{w}何が目的なんだ？本当に心配で探したわけじゃあるまいし…{w}もしかしてその話のためわざわざ？"
    show SCG_08 8 with fastdissolve
    en "むぅぅ……{w}その…昨日の僕の態度は本当に申し訳ございませんでした。"
    show SCG_08 7 with fastdissolve
    en "でも違うんスよ、僕はそんな薄情な人間じゃないッス！{w}それだけは信じてほしいッス。{w}ただぁ…"
    pl "いいから気楽にぶちまけてみなって。"
    show SCG_08 8 with fastdissolve
    nar "俺は答えを聞こうとして、一寸黙って彼の顔を伺う。{w}そろそろ人の顔色を窺うこともうんざりだったところだ。"
    nar "彼は、この追い立てられた状況に困っているように見えるが、{w}一方このような状況を心掛けていたように、"
    nar "照れくさがって、{w}自分の首を触る。"
    nar "目を伏せて考え込んでもいたが、そう長くは続かなかった。{w}えっへん、と、{w}彼は心を決めたのか咳払いをして口を開ける。"
    show SCG_08 at huruhuru
    en "そのぉ…{w}質問に質問で返すようで申し訳ないんスけど…"
    show SCG_08 12 with fastdissolve
    en "正直…{w}うちの姉上のこと、{w}どう思います？"
    nar "それは一見外れているが、{w}俺の質問については、どんなことよりもはっきりした答えだった。"
    hide screen textbox with dissolve
    call love from _call_love
    $ _skipping = False
    menu:
        "気に入ってる":
            $ _skipping = True
            jump day3_q_ar
            nvl clear
        "よく分からない":
            $ _skipping = True
            jump day3_q_rs
            nvl clear
        "姉さんのことが好きなのか？":
            $ _skipping = True
            jump day3_q_gr
            nvl clear


label day3_q_ar:

    $ meet_ar = True
    show screen textbox with dissolve
    pl "アル姉のことなら…{cps=*0.1}結{/cps}構気に入ってるぜ。{w}すごく良い人だしよ。"
    show SCG_08 3 S with fastdissolve
    nar "俺の答えに、彼は一瞬ぼんやりした顔をするが、{w}すぐ陽気な笑顔を見せた。"
    nar "彼女と話してみたのはほんの少しだったが、その短い瞬間でも十分分かる。"
    nar "彼女はどうしても嫌えない、{w}嫌がれない、{w}そういう人だってことを。"
    nar "露骨的な主教の態度はまだ疑わしく、気疎いとも思われるが、{w}彼女には過ちが問えないだろう。"
    en "そう…{cps=*0.1}ッ{/cps}スか。"
    show SCG_08 1 with fastdissolve
    show SCG_08 at bounce
    en "そうッスよね～！やっぱ！"
    en "あ～良かった！"
    show SCG_08 at bounce
    extend "万が一でも姉上の悪口を言われてたならこの場で叩きのめしてやろうって思ってたんスよね！"
    pl "暴力反対ッス～"
    show SCG_08 at bounce
    en "ははっ、冗談ッスよ～！"
    show SCG_08 0 with fastdissolve
    en "…姉上のこと、宜しくお願いするッス。"
    show SCG_08 1 with fastdissolve
    en "何なら僕のことも兄貴って呼んでくれていいッスよ？"
    pl "え、{w}なんで俺が？"
    show SCG_08 11 with fastdissolve
    en "えっ…"
    pl "あはは！冗談冗談！{w}ありがとう、兄ちゃん。"
    show SCG_08 8 with fastdissolve
    en "はぁ～…"
    pl "兄ちゃんって姉さんのことを良く知ってるんだよな。"
    show SCG_08 12 with fastdissolve
    en "流石に全部知ってる、とまではいかなくてもまあ大分そんな感じッスね…"
    pl "そっかぁ…{w}でも俺はまだ何一つ知らないんだよなぁ～"
    nar "結婚か…"
    nar "どう考えても生ぬるい響きだ。{w}俺は一生そんなことを考えてみたこともないし、"
    nar "ぶっちゃけ、俺とは全く関係のない事案として残ってほしいと望んでいた。"
    nar "勿論、今もこの考えに変わりはない。{w}が、{w}話を聞いていれば、共に一つの疑問が浮かんだ。"
    nar "彼女もこの事実を知っているだろうか？"
    nar "知っていて、その好意的な態度を見せたのか？{w}もし本当にそうなら、何を思ってだ？"
    nar "彼女についていろいろと考えていると、いつの間にか鬱陶しい気分も少し変わっていくようだ。"
    pl "話題が出たついでにちょっと会いに行ってみようかな？"
    show SCG_08 1 with fastdissolve
    show SCG_08 at bounce
    en "それは良いアイデアッスね。{w}姉上も[na]さんのこと、心配してたんスし。"
    nar "この気持ちを完全に解く為に、彼女について直接調べてみれば良いだろう。"
    hide SCG_08 with dissolve
    hide screen textbox with dissolve

    if hssh_rkn == True:
        $ save_name = "day 3, 昼, 楽園"
    else:
        $ save_name = "day 3, 昼"
    jump placemenu
    return

label day3_q_rs:
    $ meet_rs = True
    show screen textbox with dissolve
    pl "どう考えてるのかって、そりゃあ…"
    pl "{cps=*0.1}……正{/cps}直よく分からないな。{w}昨日会ったばっかの人を迂闊に評価するわけにもいかないし。"
    show SCG_08 10 with fastdissolve
    nar "俺の答えに、彼は少しだけ顔色を暗くする。"
    nar "彼女は多分、すごく良い人だ。{w}彼女のことが嫌いではない、{w}が。{w}好きでもない。"
    nar "それに今は、彼女の顔よりも、既に飽き飽きしてきた魔導主教の顔が浮かび上がる。"
    show SCG_08 9 with fastdissolve
    en "そう…{cps=*0.1}ッ{/cps}スか。"
    nar "彼は、俺の状態に気づいたように、おずおず視線を上げた。"
    show SCG_08 10 with fastdissolve
    en "ていうか…{w}昨日となんだか雰囲気が違う気がするんスけど、何かあったんスか？"
    pl "そりゃあ色んな事があったけれども、他人に話すのもちょっとアレだし…"
    pl "ざっくり纏めりゃ一日中仕事で疲れたってだけだよ。"
    show SCG_08 8 with fastdissolve
    en "うっ…{w}そんなに僕って信用出来ない人柄に見えるんスかね…"
    pl "兄ちゃんとも昨日会ったばっかだけどな。"
    show SCG_08 at huruhuru
    en "むぅ…"
    nar "結婚って、どう考えても生ぬるい響きだ。{w}俺は一生そんなことを考えてみたこともないし、"
    nar "ぶっちゃけ、俺とは全く関係のないことに残ってほしいと望んでいた。"
    nar "こんなことに関わった不機嫌を感じ始めた途端に頭を振った。{w}気分の悪い時に頭をひねたせいだ。"
    nar "このままではアル姉どころか、誰とも会えない。"
    nar "どこか静かなところで独りで頭を冷やしたい気分だ。{w}俺とは全く関係のない話で、{w}乱された脳を満たしながら。"
    nar "例えば、{cps=*0.1}蛇の巣窟の{/cps}ような…"
    show SCG_08 0 with fastdissolve
    en "強要したい訳じゃないんスけど…{w}僕にも何か手伝えそうな事があったら何時でも言ってくださいね。"
    pl "おぉ…"
    show SCG_08 10 with fastdissolve
    en "？"
    pl "兄ちゃんって見た目と違って案外マトモなんだな。"
    show SCG_08 7 with fastdissolve
    en "それ、良く聞くッス…"
    hide SCG_08 with dissolve
    hide screen textbox with dissolve

    if hssh_rkn == True:
        $ save_name = "day 3, 昼, 楽園"
    else:
        $ save_name = "day 3, 昼"
    jump placemenu
    return

label day3_q_gr:
    $ meet_gr = True
    show SCG_08 9 with fastdissolve
    show screen textbox with dissolve
    en "{cps=*0.1}な、な{/cps}{nw}"
    show SCG_08 6
    play sound "audio/se/hit.ogg"
    extend "ななななん…？！" with sshake
    play sound "audio/se/hit.ogg"
    show SCG_08 3
    en "ちがっ、{cps=*0.1}何を…そ{/cps}{nw}" with sshake
    show SCG_08 8
    play sound "audio/se/hit.ogg"
    extend "{cps=*0.2}そんなこと…ち{/cps}{nw}" with sshake
    play sound "audio/se/hit.ogg"
    show SCG_08 6
    extend "{cps=*2}ちちちがうッス！{/cps}" with sshake
    nar "俺の答えに、彼は飛び上がりそうに驚いた。{w}その大袈裟な反応と表情を見れば、多分正解だろう。"
    nar "さっきまでちょっと不機嫌だったが、意外の餌に口角が上がってしまう。"
    pl "えぇ～{cps=*0.1}じ{/cps}ゃあ嫌いってこと？"
    show SCG_08 3 with fastdissolve
    en "そ、そ、そんな訳ないッスよ！"
    show SCG_08 at huruhuru
    en "そんな、僕なんかが…{w}てかそれより！"
    show SCG_08 9 with fastdissolve
    en "姉上のことをそんな軽々しく呼ばないで貰いたいッス！"
    en "勝手にタメ口も良くないッスよ。{w}姉上はそんな扱いを受けてもいい人じゃないんスよ…"
    pl "その姉さんが良いっつったんだってば～"
    pl "他人にそんなデカい口叩いてる暇があるなら直接姉さんとお話でもして親しくなればどうなんだ？{w}兄ちゃん。"
    show SCG_08 7 with fastdissolve
    play sound "audio/se/hit.ogg"
    en "さり気なく兄ちゃんって呼ばないでほしいッス！" with sshake
    show SCG_08 11 with fastdissolve
    en "ま…{w}まさか、主教様の前でもそんな無礼極まりない言い方してたんスか？！{w}あの方はそういう無礼が一番嫌いなんスよ！"
    show SCG_08 7 with fastdissolve
    show SCG_08 at huruhuru
    en "この前も司祭の一人が身の程知らずに勝手に敬語を外してて、結局その日クビになって故郷に戻ってったんスよ…"
    pl "分かりやすいな…"
    show SCG_08 at huruhuru
    en "くうぅ…！{w}本当、過敏で怖い人ッス…"
    show SCG_08 9 with fastdissolve
    en "コホン、{w}とにかく！{w}[na]さんがいくら遠くから来たっても、神殿では神殿のやり方に従ってもらうッスよ！"
    en "全ての組織にはちゃんと上下があるもんなんスよ！{w}こっちの立場も考えてほしいッス！{w}州都の言葉が難しいなら学んでほしいし…"
    show SCG_08 4 with fastdissolve
    show SCG_08 at bounce
    en "…何なら僕がちょっと手伝ってやってもいいッスけど～？{w}ふっふん…"
    pl "えっ、{cps=*0.1}俺{/cps}普通に敬語使えますけど？"
    show SCG_08 11 with fastdissolve
    en "え？"
    pl "わかったわかった。{w}だから要は、魔導部主教様は救いようのない老害野郎で、"
    pl "エノク兄ちゃんは一昨日入った新入りに先輩ヅラすることでアル姉の目に立ちたいってことだろ？"
    show SCG_08 5 with fastdissolve
    en "は？！"
    pl "じゃあこれからは俺がちゃんと\nセ{cps=*0.1}・{/cps}ン{cps=*0.1}・{/cps}パ{cps=*0.1}・{/cps}イ{cps=*0.1}と{/cps}して慕って差し上げますから！"
    pl "だからそんな固くならないでくれよ、おにいちゃぁ～ん…{w}魔導部主教様みたいだぞ？"
    show SCG_08 at bounce
    en "な～んでそうなるんスか！？"
    show SCG_08 2
    play sound "audio/se/hit.ogg"
    en "てかまた勝手におにいちゃ～んとか変な呼び名で呼ばないでほしいッス！" with sshake
    play sound "audio/se/hit.ogg"
    show SCG_08 7
    en "あとあの御方の御名前を悪口に使わないでください！" with sshake
    nar "将来が心配なほど弱点を見せる男を前にすると、ふと故郷のことを思い出した。{w}俺はよく、新しい言い草で人を困らせた。"
    nar "だが決して憎まれ口ではなかった。人の不運をあざ笑うことも、弱点を貶すことも、ここに来る前には想像もしていなかった。"
    nar "だからこそもっと驚いた。"
    nar "とにかく、俺はエノク兄さんに感謝している。{w}気晴らしの言い草をくれたからな。"
    play sound "audio/se/ding.ogg"
    if hssh_rkn == True:
        scene bg03 at bounce
    else:
        scene bg03_1 at bounce
    show SCG_08 7
    show SCG_08 7 at bounce
    pl "そっか！{w}じゃあ次からは気を付けま～す。{w}じゃ！{w}お邪魔虫はここらで失礼！"
    show SCG_08 6
    play sound "audio/se/hit.ogg"
    en "えっ、{cps=*0.1}ち{/cps}ょっとちょっと！{w}行かないでくださいよ～～！" with sshake
    nar "だったら誰とこの楽しさを分けてみようか。"
    nar "人をバカにしそうなやつはダメだ。{w}そして兄さんのことをよく知っていて、俺との会話を好む人とは…"
    nar "頭の中で茶髪の優しい先生が懐かしく手を振ると、足取りが軽くなっていく。"
    hide SCG_08 with dissolve
    hide screen textbox with dissolve
    if hssh_rkn == True:
        $ save_name = "day 3, 昼, 楽園"
    else:
        $ save_name = "day 3, 昼"
    jump placemenu
    return

label day3_night:
    if hssh_rkn == True:
        $ save_name = "day 3, 夜, 楽園"
    else:
        $ save_name = "day 3, 夜"
    pause 1
    nvl clear
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg02_1 with dissolve
    else:
        scene bg02_2 with dissolve
    stop music fadeout 3
    call place02 from _call_place02_3
    pause 1
    show screen textbox with dissolve
    nar "寮への帰り道。{w}特に長かった今日の一日が終わるという安心感のせいか、段々と足の力が抜けていく。"
    nar "すぐ辺りに、俺と同じく足の遅い人がいた。{w}間違いなくマヤだ。"
    pl "マヤ！{w}今日もお疲れ様！"
    show SCG_02 idle with dissolve
    my "ぅえ…？"
    show SCG_02 at bounce
    extend "あ、[na2]くん…{w}うん、[na2]くんもお疲れさま。"
    if meet_crea == 1:
        pl "今日も無事終わったな～！{w}ホント、疲れて体が持たないぜ。"
    else:
        pl "クレアの見送りはどうだった？今日も無事終わったな～！{w}ホント、疲れて体が持たないぜ。"
    my "なにかあったの…？"
    pl "色々、な…{w}あのさ、実はさっきまで…"
    pl "…その、{w}お仕事が！{w}今日マヤが来れなかったじゃないか。{w}だから午前中に仕事が溜まっちゃって。"
    pl "それをちょっくら片付けてきただけだぜ。{w}その場でテキパキやっとかないと後でマジに苦労すんだな～って！"
    my "うぅん…ご苦労さまだったんだ…{w}今日お手伝いできなくてごめんね。"
    show SCG_02 8 with fastdissolve
    my "でも…{w}もしかしたらわたしが居てても邪魔になるだけだったかも…"
    pl "いやいや、マヤが居なくて一日中辛かったんだって！"
    my "……"
    nar "少しずつ話を遅くしていたマヤは、ふと足を止めた。"
    $ renpy.music.set_volume(0.5, channel="music")
    play music 'audio/SE/prologue wind.ogg' fadein 5
    show SCG_02 0 with fastdissolve
    nar "そして体を俺の方にひねって、只物静かに俺を見つめてくる。"
    nar "もしさっきの言葉が不愉快だったのか、{w}と心配するところに彼女は、自分の顔を俺の体に向けて押し込んだ。"
    nar "触れなさそうで、すぐ触れそうな距離。"
    nar "見下ろしたら、マヤはじっと目を閉じている。{w}そのまま何度か鼻を鳴らし、また俺から離れる。"
    pl "マ…マヤ？"
    show SCG_02 7 with fastdissolve
    my "[na2]くん…{w}なんか、臭わない…？"
    nar "さっきの行動で何かの疑問を解いたのか、今度は俺の後ろの風景へ視線を移す。"
    nar "その心配する顔を見て、俺は彼女に続いて空に鼻を何度か鳴らしてみる。"
    nar "血生臭い、どこかで臭いがする。{w}俺は違和感に気づいて、マヤと目を合わせ、一度頷いた。"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    show screen nvlbox with dissolve
    "\n その跡を慎重に追っていけば、覚えのある道だ。{w}職場とは近く、確かに昼に来た、喧嘩を目にしたところだ。"
    "それに気づいたら、心が忙しなくなってしまう。{w}自らの心拍が聞き辛いくらいに騒がしい。"
    "いくつかの不安のイメージが頭の中を掠めて、角を曲がればそれも現実となった。"
    "血塗れの床、{w}その上には幼虫のように見える何か。"
    "それが人の指だって気づいたのは僅かな瞬間だった。{w}さっきまでも騒がしかった心臓が落ち着いてしまう。"
    et "後ろに付いてきたマヤが短い悲鳴を上げ、朦朧になった俺の気もすぐ正気に戻る。"
    nvl clear 
    "\n 再び鋭くなった嗅覚に血生臭さがまた酷く。"
    "結構最近の惨状のようだ。まだ乾いてない血は、石床の上でてかてかする。"
    "俺は、{w}ゆるゆると血が足下まで流れてくるのを見て尻込みをしてしまう。"
    "一歩、{w}また一歩。{w}そして三歩目、何かが体に触れた。"
    "さっきまではなかったはずの影法師が、いつの間にか後ろに垂れている。"
    "「……」"
    "頭の混乱を鋭く切り取る踵の音、蒼白な肌に、まるで絵のような白髪…"
    et "間違いなく主教様だ。{w}が、{w}いつも彼女と共にあった眩しさが、今の彼女には見えなかった。"
    nvl clear
    "\n 闇の垂れ込んだ物陰の下。両目で揺らいだ金色の光は跡形もなく消え去り、{w}暗闇を詰め込んだ青色だけが、冷たく沈んでいる。"
    "たった一つの感情さえも感じられない目は、冷たい視線で、{w}目先の俺たちを過ぎ、向こうの惨状を眺めていた。"
    "「主教様…？」"
    "忌まわしいほどの寂寞。{w}それが堪えられなかったマヤが先に慎重に彼女を呼ぶ。"
    et "それに彼女は斜めに頭を上げ、笑顔を見せた。{w}俺はなぜか鳥肌が立つ。"
    hide screen nvlbox with dissolve
    stop music fadeout 2
    nvl clear
    pause 1
    show SCG_02 5 at left
    show SCG_05 B 00 at hkright
    with dissolve
    pause 1
    show screen textbox with dissolve
    play music "audio/bgm/Securett_ver2.ogg"
    hk "危険ですよ？{w}こんな時間に…"
    show SCG_05 1 with fastdissolve
    hk "研修生である御二人が、"



    show SCG_05 0 with newfastdissolve



    extend "{cps=*2.5}駄目でしょう。{/cps}"
    show SCG_02 at huruhuru
    my "ぁ…{cps=*0.1}ご{/cps}めん、{cps=*0.1}な{/cps}さい…"
    show SCG_05 90 with fastdissolve
    hk "{cps=*2.5}あれは…{/cps}"
    show SCG_05 0 with fastdissolve
    hk "{cps=*2.5}…何方かが、亡者の袋を投げ捨てて置いたのですね…{/cps}"
    hk "{cps=*2.5}私が処理致しましょう、{w}御二人はどうか心配無き様、寮に戻って御休みくださいませ…{/cps}"
    nar "低く、冷え切った声。{w}しかしにこやかな口振り。{w}その口が開くことが怖くて、俺とマヤは只ひっそりと頭を下げ、すれ違った。"
    show SCG_02 7 with fastdissolve
    my "{cps=*0.1}し…{/cps}失礼いたしました…"
    pl "…失礼いたしました。"
    hide SCG_05
    hide SCG_02
    with dissolve
    nar "彼女は俺たち二人を笑顔で見送ってくれたが、俺はつい見てしまった。"
    nar "俺たちから首を回したその瞬間の笑みの消えた顔を。ぞっとした違和感が再び輝く。"
    nar "しかしそれ以上に込み上げてくる感情。{w}昨夜、古びた礼拝堂の外で見つけた彼女は、やはり見違えなかった。{w}間違いなく別人だ。"
    nar "あの日の衝撃を忘れられなかった心の臓が高鳴る。{w}それは恐怖感に似たものだが、かつ全く別の何かでもある。"
    nar "不思議だ。{w}彼女とはもう充分出会っている筈なのに。"
    nar "俺は今更、どうしても探したい物を再び見つけた時の高揚感を感じている。"
    hide screen textbox with dissolve
    if hssh_rkn == True:
        scene bg03_1 with dissolve
    else:
        scene bg03_2 with dissolve
    pause 1
    show SCG_02 7 with dissolve
    show screen textbox with dissolve
    my "わたしたち、ね…"
    nar "内務班の階段を上る前に、ずっと頭を下げて軽く震えていたマヤが、突然口を切る。"
    nar "全く落ち着く気配のしなかった心拍は、彼女の声に、再び元の速さを取り戻す。"
    nar "彼女も今までずっと落ち着こうとしていたのか、まだ震える自分の手を不安そうに触っていた。"
    my "わたしたちね、死体の片付けがお仕事だったよね…"
    pl "ん？あぁ…そうだよな。"
    show SCG_02 8 with fastdissolve
    my "……"
    pl "それが…どうしたんだ？"
    my "なんだか…{w}なんともないことで驚いちゃってるんじゃないかなって…"
    pl "でもさ…{w}あんなの見せられて、驚かない方がおかしいだろ？"
    show SCG_02 7 with fastdissolve
    my "…だよね…？"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    show screen textbox with dissolve
    nar "マヤはそこで黙ってしまう。{w}俺たちは結局唐突とも思える挨拶の後別れた。"
    nar "この数日間、神殿に何とか慣れてきたと思ったのに、まだ俺たちは、"
    nar "この神殿で何が起きているのか、どう生きていけば良いのか、何も知らないままだ。"
    nar "神殿の人は可笑しい。{w}長く住めば住むほど、ここの「正常」が疑わしくなってしまう。"
    nar "この空間が人をそうしてしまうのか。{w}明け暮れ真っ暗な天がさらに時間知覚を麻痺させ、"
    $ _skipping = False
    nar "もう昨日のことも遠い昔の出来事のように感じる。{w}俺は、まだ来てもいない明日が、既に気遣わしいんだ。"
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
    jump day4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
