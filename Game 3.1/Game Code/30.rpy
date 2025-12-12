
define ask = 0
define askA = True
define askB = True
define askC = True



label day4_hk_F:
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg04 with dissolve
    else:
        scene bg04_1 with dissolve
    call place04 from _call_place04_6
    show screen textbox with dissolve
    play music 'audio/bgm/dialogue.ogg' fadein 3
    nar "妙な雰囲気を漂わす、あの学術部の司祭だ。ラヴィアン・ローズだったっけ。"
    nar "おかげでいい情報を手に入れた。{w}奴は何心なく言い出したようだが、彼女にずっと疑問を抱いていた俺には大事な手がかりである。"
    nar "第一、人の人格や精神を操る災害も存在する。{w}第二、彼女に違和感を感じたのは俺一人ではなかった。"
    nar "軽い足取りと共に心臓が高鳴り始めたが、俺の歩きは作業場に入る前に止まってしまう。"
    stop music fadeout 2
    nar "シーキュレットがいた。{w}彼は作業場の方から来たのか最初は俺を見て驚いた顔をして、すぐ俺を睨みつけてきた。"
    nar "今日はもう会うこともないだろうと思ったのによ、嫌なやつ。"
    hide screen textbox with dissolve
    pause 1.0
    show SCG_03 0 with dissolve
    show screen textbox with dissolve
    play music 'audio/bgm/securett.ogg' 
    sc "作業場にいくのか？"
    nar "珍しくやつから先に話しかけてきた。{w}しかし安否や挨拶などとは確実に温度が違う。"
    nar "何の罪のない俺への警戒心まで感じられるその一言に、一気に気分が悪くなってきた。"
    pl "俺が何処に行こうがお前には関係ないだろ。"
    sc "関係ある。{w}主教様のごく僅かな休憩時間をお前が定期的に邪魔してるだろ。"
    pl "主教様の休憩時間だあ？普段気にもしてなかったくせに…"
    show SCG_03 2 with fastdissolve
    sc "……"
    pl "…お前は周りを注意深く見ていないから知らないだろうけどよ、主教様は俺と会話するのが好きなんだぜ。"
    sc "知ってるなら尚更そんな事しちゃ駄目だろ。"
    pl "は？何言ってんだ。"
    show SCG_03 0 with fastdissolve
    sc "キミには女性とイチャコラ遊ぶより先にやるべき事があるじゃないか。"
    sc "その未熟な精神を鍛練するとか、今日の失敗を次に活かせるよう勉強するとかね。"
    pl "…まだそれを俺のせいって言い張るつもりなのかよ？"
    sc "浄化部には常に人手が足りないんだ…{w}今もそう。"
    sc "なのにこんなに忙しい時期にボクはキミたち新入りのやらかした事故の収拾で自分の業務もマトモに出来ていない。"
    sc "これがどういう意味かわかるかい？"
    nar "それでこそ俺と全く関係のないことだ。"
    nar "やるべきことができないのも、新入りが同じミスを繰り返すことも全く指導する先任の個人の能力の足りなさのせいではないか。"
    nar "そんなに忙しければ、どこかにずっと閉じこもって溜まった仕事でも片付ければ良いのに、"
    nar "何でわざわざ神殿まで入ってきて絡んできてやがるんだ？{w}って言いたいところだったが、まずは無視することにした。"
    pl "主教様って今作業場にいらっしゃるよな？"
    hide SCG_03 with dissolve
    nar "俺の態度にイラついてきたか、シーキュレットは少し黙っていた。{w}言葉を失ったようには見えない。"
    nar "また顔を上げた時、彼は冷ややかな目で俺を鋭く睨んでいた。{w}びくっと肩が震えてしまう。"
    show SCG_03 2 with dissolve
    sc "…キミ、浄化部の為に死ねるかい？"
    pl "また突拍子もないことを…"
    show SCG_03 0 with fastdissolve
    sc "違う、キミが本気で彼女の所の司祭として働きたいならそこは「ハイそうです」って言わないと。"
    pl "主教様を冒涜するのもほどほどにしとけよ、あの方がそんなこと望んでる訳がないだろうが。"
    sc "そんな考え方が既にダメだって言ってるんだ。"
    sc "主教が神の為に働く存在であるからこそ、その司祭は主教の為に何でもするという覚悟を決めなければならないんだ。"
    pl "万が一それが本気ならお前らは神殿に籠りすぎててとうとう頭がイカレちまったんだろうな。"
    show SCG_03 72 with fastdissolve
    sc "そうかも知れないね。"
    hide SCG_03 with dissolve
    nar "その一言を最後に、シーキュレットは背を向けて作業場から離れてしまう。"
    nar "俺としては彼が一刻も早くここから消えてほしかったので、再び声をかけることなく後ろ姿を睨むだけだった。"
    nar "彼が立ち去った後に作業場を眺め回したが、ハク主教はいない。{w}後からは奴のいなさそうな時間を考えながら来た方が良いのか。"
    nar "不愉快な時間を過ごしてしまった…"
    nvl clear
    hide screen textbox with dissolve
    pause 1
    $ day_hk = True
    $ day_time = day_time +1
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_4
    return



label day4_ar_N:
    show screen nvlbox with dissolve
    "\n 気まずい歩きで訪れた訓練場に、アルネ姉さんはいない。"
    "首を出してキョロついていたら、魔導部の他の司祭たちが先に話しかけてきた。"
    "アルネ姉さんはもう仕事の為に外へ出たっていうらしい。"
    "まだ何も言っていないのに当然のように姉さんの不在を伝えてくれるなんて、負担感と共に恥を感じてしまう。"
    "姉さんは忙しい人だし、そう簡単には会えないだろうな。"
    et "残念だが、今日はここで帰ろうぜ…"
    hide screen nvlbox with dissolve

jump day4_ar_F

label day4_ar_F:
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg102 with dissolve
    else:
        scene bg102_1 with dissolve
    call place102 from _call_place102_4
    show screen textbox with dissolve
    nar "訓練場の扉を開ける前に、まず耳を押し当ててみた。中から何も聞こえない。"
    nar "もしかしたらと思って隙から覗いてもみたが、やはり中に人はいないようだ。"
    nar "しかし鍵はかかっていないようで、体の重さに扉が押される。{w}俺は慎重に隙に足を入れてみた。"
    er "誰だ？"
    play sound "audio/se/hit.ogg"
    pl "うわっ！" with sshake
    show SCG_09 0 with dissolve
    play music 'audio/bgm/anyway high person.ogg' 
    er "これはまた、この時間にコソ泥の如く魔導の基地に脚を踏み入れた輩が誰かと思いきや、我が婿殿ではないか。"
    show SCG_09 4 with fastdissolve
    show SCG_09 at er_stand
    er "どれだけ肝の据わった野郎か見てやろうかと思ったが、これは意外に嬉しいお客様だな。"
    pl "ま、魔導部主教様…{w}ハハッ、ゴメン…いるとは思ってなくて…"
    nar "誰もいないと思ってたのに…小さすぎて居るのかさえ分からなかったな。"
    pl "うーん…アルネ姉さんは？"
    show SCG_09 8 with fastdissolve
    er "アルネなら既に部屋に戻っている。今日は相当疲れていたみたいだったな。"
    er "貴様が望むのであれば降りて来る様に言っても良いのだが。"
    pl "い、いいっていいって！疲れてる人をわざわざ呼び出しちまうのもアレだし。"
    show SCG_09 0 with fastdissolve
    er "そうか、ならば我が婿殿に無駄足を運ばせる訳にはいかぬな。"
    show SCG_09 9 with fastdissolve
    er "鯛なくば狗母魚とも言う、この俺と共に談笑でもすると言うのは如何だ？"
    nar "これを狙っていたな、この狸ヅラジジイがよ…"
    pl "まあいいけど…寮閉まっちゃうかもだし、長居はできないと思うぜ。"
    show SCG_09 0 with fastdissolve
    er "案ずるな、そう長引かせん。{w}最近は如何だ？"
    pl "…これといった問題はなかったな。ベッドがちょっと心地悪くて夜はあんま寝付けてないぐらい？"
    er "処理班の頃から使われていた古い家具を置いたのだから、そうなる他あるまい。"
    pl "そういうことだったのか…なんか新設部署にしては古いと思ってたけど。"
    er "折り紙王冠なんぞを被った小娘のおままごとに妥当な玩具ではあるな。"
    pl "ハハ…主教様は浄化部の話が出るとすぐそういう言い方するよな。"
    pl "ハク主教様はそれでも主教様の事あんま嫌ってなさそうだったんだけど…"
    show SCG_09 8 with fastdissolve
    er "む？貴様は俺があの小娘を嫌っているとでも思っているのか？"
    er "そんな訳があるまい、あんな乳臭いガキを。{w}ただ自身の子の育て方を間違った親に対して指を指しているのだよ。"
    er "子とは結局親が責任を取らなければならない第一の業であるからな。"
    pl "へぇ…てか、伯父様って言ってたけどそれって結局お父さんではないってことだろ。{w}主教様は他に子供とかいないのか？"
    er "無いな。{w}何…兎にも角にも現在の俺は司祭の身。貴様は神に仕える司祭が子などを作れると思うか？"
    pl "うわ～神殿の規則は厳しいな…"
    show SCG_09 11 with fastdissolve
    er "しかしあの小娘は己の親父の顔と瓜二つだ。幼き頃から見てきたが年を取れば取る程似ていってる。"
    er "養娘という言い訳で茶を濁してはいるが、私生児に間違いない。あんな輩が神殿の枢機卿だなんて…"
    pl "あの…主教様、オトナの人にこんなこと聞くのは失礼なんだろうけど…{w}今おいくつですか？"
    show SCG_09 8 with fastdissolve
    er "普通に何歳かと聞けばいい、それ程歳は取っていないからな…{w}今年で四十五を超えたか。"
    pl "エッ、意外と若いじゃんか……！そんな喋り方するからこんがらがるだろ。"
    er "ええい貴様、目上の人の前では言葉を慎め。"
    er "こっちは頭を下げなければならない方々が未だに目も曇らずのうのうと生きているもんで日々頭を抱えていると言うに。"
    pl "へぇ…主教様もお年寄りのせいで苦労してるんだな。"
    er "奴らは死に時を逃してしまったが為に脳が膿んでしまっていてな。"
    show SCG_09 0 with fastdissolve
    er "俺に聞きたいことが多いらしいが、これもいい機会だと思って何でも聞いてみると良い。"
    pl "うーん、なら…"
    hide screen textbox with dissolve
    jump er_ask
    return

label er_ask:
    if (ask == 1):
        call er_re from _call_er_re
    elif (ask == 2):
        hide screen textbox with dissolve
        pause 1
        jump er_end
    hide screen textbox with dissolve
    menu er_menu:
        "エルジェーベトについて" if askA:
            $ askA = False
            jump er1
        "家族について" if askB:
            $ askB = False
            jump er2
        "魔導部について" if askC:
            $ askC = False
            jump er3

label er_end:
    show SCG_09 0 with dissolve
    show screen textbox with dissolve
    er "兎も角俺はこの古臭い体制をひっくり返す様な改革を断行せんとしているのだ。"
    er "それが貴様をここに連れて来た理由とも因んでいる。"
    pl "それはどういうことだ？"
    er "俺は古くから強圧的に行われてきた近親婚を絶ち、古臭い歴史を立て直す。"
    er "アルタナータ家正統後継者であるアルネの相手が外部者なら、それは改革の手始めとして不足分無いだろう。"
    pl "うーん…大体言ってる意味はわかるけどな。{w}でも大事な娘さんのお隣を外部者に任せちゃっていいのか？"
    show SCG_09 8 with fastdissolve
    er "それがアルネを守る為だ。"
    show SCG_09 11 with fastdissolve
    er "相手がずっと居ないままであったら俺のアルネは間違いなく魔導師の老い耄れ共の汚らしい手に入ってただろうからな…"
    pl "他の人は…？"
    show SCG_09 8 with fastdissolve
    er "俺の他の兄弟と言えどあの子の両親で全てだったが、今やその二人も亡くなり行き止まりだ。"
    show SCG_09 0 with fastdissolve
    er "これでお前の立場がどんな意味を持っているのか理解が出来たか？"
    pl "主教様がどれだけ頑張って生きてる人間かっていうのは理解した気もするぜ。"
    er "さて、今日はこの程度にしておこうではないか。俺もそろそろ上がって残った仕事をやらねばな。"
    pl "あ…じゃあ俺もそろそろ帰らなきゃ。"
    show SCG_09 9 with fastdissolve
    er "道が暗いから気を付けて戻りなさい。"
    hide SCG_09 with dissolve
    nar "重たい扉を閉じ、訓練場から離れた。{w}姉さんに会うには明日からはもう少し早く来た方が良いかもしれない。"
    nar "エルジェーベト主教と少し親しくなってしまった…"
    hide screen textbox with dissolve
    stop music fadeout 2
    $ ask = 0
    $ askA = True
    $ askB = True
    $ askC = True
    nvl clear
    pause 1
    $ day_ar = True
    $ day_time = day_time +1
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_4
    return


label er1:

    show screen textbox with dissolve
    er "家門アルタナータ第十三代当主エルジェーベト・アルタナータ。"
    er "現在は神殿所属にあり、セイント・シェオルの魔導部を引導している。"
    pl "名前はなんで…そんな感じなんだ？"
    show SCG_09 10 with fastdissolve
    er "名前か。"
    nar "俺の言葉のどこかが彼の気に障ったのか、余裕だった彼はすぐ眉根を顰める。"
    pl "や、その…男に付けそうな名前じゃないだろ。本名なのか？"
    er "では貴様の名前は何で「そんな感じ」なんだ？"
    pl "え、んん？これは俺の両親がつけてくれた…自慢の名前なんですけど…"
    show SCG_09 9 with fastdissolve
    er "であろうな。"
    nar "…一言を負けないな。"
    show SCG_09 8 with fastdissolve
    er "名前か…{w}面白い名前よな。"
    er "何故こうなったか見当は付くか？アルタナータ家の長者には…不幸が訪れるという神託が下りる。"
    er "だから子が生まれるときは必ず逆性別の名を付けるのだ。"
    pl "長者に因んだ神託なら性別は関係なくね？"
    show SCG_09 11 with fastdissolve
    er "娘は子として認めたくないらしいな。"
    pl "はあ……"
    show SCG_09 8 with fastdissolve
    er "気持ちとしてはアルネにも新しい名前を与えてやりたいのだが、"
    er "あの子の親御が残していった物に俺が勝手に手を出すわけにはいかぬ。"
    er "彼らも彼らなりに考えたもんだろうよ。"
    pl "なら姉さんにも不幸が訪れるかもだろ？それは良いのか？"
    show SCG_09 0 with fastdissolve
    er "そんな迷信なんぞに縋る訳にはいかん。アルネは自身の力で運命を切り開ける強い子だ。"
    $ ask = ask + 1
    jump er_ask


label er2:
    show screen textbox with dissolve
    pl "主教様の家族について聞きたいんだけど。"
    show SCG_09 8 with fastdissolve
    er "俺の家族か？突拍子もない質問だな。"
    er "貴様の知る通りアルネと…{w}もう一人、その二人だけだが。"
    pl "や、伯父様ってことはつまり…主教様には他の兄弟がいるってことだろ？"
    show SCG_09 0 with fastdissolve
    er "成程、そういう意味であったか。俺は三姉弟の二人目として生まれた。"
    er "両親は何方も財力と権力に目が曇っただけのつまらん人々だったもんでな、俺は丁度お前ぐらいの歳に家を出てしまったが…"
    er "姉弟たちとは仲が良かったものだ。"
    pl "え、主教様にも親っていたんだ。"
    show SCG_09 10 with fastdissolve
    er "貴様のその言い草は他人を不快にさせたくてわざとやってるのか？"
    pl "い…いえ、サーセンっした。"
    show SCG_09 4 with fastdissolve
    er "宜しい。魔導の漢ならそれぐらい肝は据わってなければな。"
    show SCG_09 0 with fastdissolve
    er "アルネの父親であり俺の弟だった末っ子は自身の役目に忠実な責任感あふれる男で、"
    er "姉は強く優しく、決断力の有る美しい女性だった。"
    er "生憎神が彼女を早くも御連れ戻しになられたが、俺の生涯であれ程完璧な女性は未だに見た事が無い。"
    pl "姉さんよりも？"
    show SCG_09 9 with fastdissolve
    er "勿論俺のアルネもまた世界一完璧だ。{w}古来子とは親に似る物だろう。"
    $ ask = ask + 1
    jump er_ask


label er3:
    show screen textbox with dissolve
    pl "じゃあ…これからのためにも魔導部についてもっと聞いておきたいんだけど。"
    show SCG_09 0 with fastdissolve
    er "ほぉ、それは良い心構えだ。{w}魔導部とは大陸一の人類とも言える「魔導師」なる存在を育成する為の部署だ。"
    er "各自の神聖術を磨き上げ御国の役に立てる事柄を行うのだよ。"
    show SCG_09 9 with fastdissolve
    er "神聖力が重要視される此の地の主に相応しくないか？"
    pl "神聖術…？前姉さんが言ってた道術に似たモンか？"
    show SCG_09 0 with fastdissolve
    er "神聖術を利用して人をも超越する力、其れに適合するので在れば全て神聖術だ。"
    er "学術部の魔女同様情報を物体化する也、保健部の知友術も又広く受け入れるのならば神聖術と言える。"
    er "我々魔導師こそが各家門の当主が古から歴史と伝統を守り代々受け継がれて来た神聖術を以て戦う、誇り高き神の使者なのだよ。"
    pl "主教様がふわふわ浮いてんのもそう？"
    show SCG_09 9 with fastdissolve
    er "以前の身体に慣れていて、視界が低いと如何にも不便な物でな。"
    pl "へ～スゴイな。アルタナータの特技は念力なのか。"
    show SCG_09 4 with fastdissolve
    er "なぁに、この程度基本中の基本に過ぎない。"
    show SCG_09 9 with fastdissolve
    er "我々アルタナータに伝承される力は神聖を身にまとい、人間の持つ身体の限界と言う物を超える力だ。"
    pl "面白そうだな、俺もやってみたいぜ！"
    show SCG_09 0 with fastdissolve
    er "まあそう焦るな、準備の出来ていない身体で無暗に神聖力を使ってしまえば身体と精神が耐え切れず化物と化してしまうぞ。"
    pl "つまんね…"
    show SCG_09 8 with fastdissolve
    er "只興味本位で振り翳す様な力では無いぞ、神の力を借りると言う事は。人が死にうるかも知れないからな。"
    show SCG_09 0 with fastdissolve
    er "まぁ、貴様は俺が選び抜いた我がアルタナータの後継者。{w}時が来れば貴様が望まずとも自然と全て分かる事になるだろう。"
    er "其れまで貴様のやるべき事は魔導師としての誇りを持って神殿の礼儀作法を学び心と体を鍛え抜く事。常に用心しなさい。"
    pl "ハイハイ、わかりましたよ～っと。{w}あれ？でも俺うちの主教様が神聖術を使ってるとこ見たことないな？"
    show SCG_09 8 with fastdissolve
    er "それはまぁ、雑種だからな…"
    show SCG_09 11 with fastdissolve
    er "…毎日死体流しをしている小娘が神聖術を使う事など何があろう。"
    $ ask = ask + 1
    jump er_ask


label er_re:
    show SCG_09 9 with fastdissolve
    er "そうだな、質問があるなら言ってみなさい。"
    return



label day4_rs_F:
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    scene bg104 with dissolve
    call place104 from _call_place104_5
    show screen textbox with dissolve
    play music 'audio/bgm/biblioteca.ogg'
    nar "階段を上がろうとしたが、すぐ道を曲がって図書館に戻った。"
    nar "せっかく話をするなら完全な状態のラヴィアンを相手するのが良いだろう。"
    nar "前は不自然な人気だけの図書館だったが、事故を過ごしてみれば大体の輪郭が見えてきた。"
    nar "多分今もどこかに隠れて俺を見守っているだろう。"
    nar "しかし主教と直に話し合った姿を見せたおかげだろうか、直接に話しかけてくる司祭はいない。"
    nar "さっき出た部屋に再び入ると、幸いまだラヴィアンがそこにいた。"
    show SCG_11 5 with dissolve
    rv "あれ、[na]坊ちゃま？何か忘れものでもございましたか？"
    pl "や、そんなんじゃないってか…普通にお前とお話でもするかなって。"
    show SCG_11 at bounce
    rv "はい？わざわざボクっちを選んで頂いたのは大変恐縮ではございまちが、ボクは面白みのある会話は特技ではないのですが。"
    pl "簡単に返事くれるぐらいで大丈夫だからさ。忙しいか？"
    show SCG_11 3 with fastdissolve
    rv "軽い談笑を交わすぐらいの余裕はあります。これをヒマって言っちゃってもいいのでしょうか？"
    show SCG_11 4 with fastdissolve
    rv "ともかくお昼の時間内にはエノク様に御会いする予定にございますね。"
    pl "エノク兄さんと？二人が知り合いだなんて意外だな。"
    rv "とても光栄に思っております。{w}神殿の人でエノク様と面識のない人の方が珍しくはありますが。"
    rv "お借りになった本はいかがでしたか？"
    pl "まだ開いてみてもねえな。"
    show SCG_11 0 with fastdissolve
    rv "然様ですか、まあ読書とは時間と気持ちに余裕があるときに嗜むものではありますね。"
    rv "魔導書はどちらかというと参考書に近いものですので、情報を脳に叩き込む感じでパパっと読んじゃった方が良いんですけどね。"
    rv "あっちゃちゃ、これはあくまでボクのやり方ですのであまり参考になされなくても大丈夫ですよ。"
    pl "…なんでそんなあたふたしてるんだ？"
    show SCG_11 1 with fastdissolve
    rv "バレちゃいました？"
    show SCG_11 7 with fastdissolve
    rv "実は[na]お坊ちゃまとちゃんとした会話をするのはこれが初めてでして、ちょいとばかり緊張しちゃいまちた。"
    rv "お恥ずかしい限りでございます。"
    pl "お前みたいなきっちりした人でも緊張はするんだな…{w}じゃあ、俺が質問をするから、返事だけしてみなよ。"
    show SCG_11 1 with fastdissolve
    rv "はい、何でもお聞きくださいませ。"
    hide screen textbox with dissolve
    jump rv_ask
    return

label rv_ask:
    if (ask == 1):
        call rv_re from _call_rv_re
    elif (ask == 2):
        hide screen textbox with dissolve
        pause 1
        jump rv_end
    hide screen textbox with dissolve
    menu rv_menu:
        "天気について" if askA:
            $ askA = False
            jump rv1
        "ラヴィアンについて" if askB:
            $ askB = False
            jump rv2
        "男の人と付き合う予定は？" if askC:
            $ askC = False
            jump rv3


label rv1:
    show screen textbox with dissolve
    if hssh_rkn == True:
        pl "…近頃は白夜が続いておりますね？"
    else:
        pl "…近頃は極夜が続いておりますね？"
    show SCG_11 1 with fastdissolve
    rv "何故そんな面白い喋り方を？"
    pl "お前が変なこと言うから俺まで気まずくなったんだろうが！"
    show SCG_11 at bounce
    rv "あちゃ～これまたやらかしてちまいまちた。"
    if hssh_rkn == True:
        rv "では坊ちゃまがこれ以上気まずくなられないよう白夜と極夜についての簡単な情報をば。"
    else:
        rv "では坊ちゃまがこれ以上気まずくなられないよう極夜についての簡単な情報をば。"
    nar "一気に退屈になってしまったな…"
    show SCG_11 0 with fastdissolve
    rv "えっへん、州都の多くの人々が極夜を禍の影響により陽が喰らわれる天罰と思い込んでおられますが、"
    rv "実は緯度の高度によって起こる自然現象なのでございます。"
    rv "州都は昼は寒いので、年に一、二回程度の極夜が起こっておりますね。{w}逆に陽が沈まない現象もあります。"
    pl "じゃあそれはずっと昼なんだな。"
    show SCG_11 4 with fastdissolve
    rv "はい、陽が沈まなくて夜が訪れなくなる現象を白夜と言います。"
    rv "極夜に比べ白夜はとても珍しく、記録によると二千年に一度の頻度で発生するとされておりますね。"
    rv "その周期が大災害の預言と重なっているため、一部の人々は白い光を禍の予兆とされていたりもします。"
    pl "州都の人ってみんなそう白色が嫌いなのか？"
    show SCG_11 at bounce
    rv "黒色は大好きですが。"
    show SCG_11 1 with fastdissolve
    rv "坊ちゃまも一度くらいは似たような話をお聞きになさってる筈ですよ、{w}黒曜石のような黒い髪は魔導師の象徴ですし？"
    pl "うっ……それとな～く人をからかうな。"
    $ ask = ask + 1
    jump rv_ask


label rv2:
    show screen textbox with dissolve
    show SCG_11 0 with fastdissolve
    rv "ラヴィアン・ローズ。未熟ながらも学術部の補佐教を担当させて頂いております。"
    rv "図書警察、排水管修理、早口、論文代筆、法律相談…なんでも出来ます。"
    rv "副業として猫探偵もやっております。"
    pl "猫探偵とは？？"
    show SCG_11 1 with fastdissolve
    rv "家出した迷子の仔猫ちゃんを検挙してご家族の元へお返しするお仕事でち。"
    pl "お前、微妙に万能なんだな…"
    pl "禍持ちの身じゃ普通の生活も難しいんじゃないか？"
    show SCG_11 0 with fastdissolve
    rv "確かに全然不便ではない、と言ったら嘘になります。仕事にも色んな支障を来たしているので。"
    pl "いつからそうだったんだ？"
    show SCG_11 5 with fastdissolve
    rv "大分幼い頃からですね。だからと言って生まれた時から、という訳ではなく…"
    show SCG_11 0 with fastdissolve
    rv "ボクの御両親が禍に巻き込まれお亡くなりになって以来でしょうか。"
    rv "州都の外側ではそういう事故は珍しいものではないので。"
    pl "ふぅん…お前は州都生まれだと思ってたんだけど。"
    pl "なんか、そういうイメージってか？苦労して育ったって意外だな。"
    show SCG_11 4 with fastdissolve
    rv "良い様に見て頂けて光栄で御座います。{w}でもそれほど辛い生涯を送って来た訳ではありません。"
    rv "ボクに出来ることは機械を弄る事と勉強だけだったけど、その特技だけでもこんなに上手く生きてってるのですし。"
    show SCG_11 at bounce
    rv "お茶を淹れるのも得意ですね、あとジャグリングを少々。"
    pl "謙遜なのか傲慢なのかどっちかにしろよ。"
    show SCG_11 1 with fastdissolve
    rv "へへ。"
    pl "そんな多才なのに禍を持ってるなんて惜しいな。"
    show SCG_11 4 with fastdissolve
    rv "さあ…こればかりは神がお決めになさったボクの運命ですので。"
    rv "万が一それのせいで何かを成し遂げなくなったとしても、"
    rv "それは自身の器の小ささのせいであり決して禍に原因があった訳ではないと思います。"
    $ ask = ask + 1
    jump rv_ask


label rv3:
    show screen textbox with dissolve
    show SCG_11 7 with fastdissolve
    rv "ぇ………？{nw}"
    extend "{cps=*0.1}お{/cps}おお、{cps=*0.1}お{/cps}、{nw}" with sshake
    extend "{cps=*0.1}男{/cps}の人と…？" with sshake
    nar "……？"
    rv "…えっ……" with sshake
    show SCG_11 at bounce
    rv "{cps=*0.1}あ…え…え～と…な{/cps}いですね…"
    pl "マジ？お前はカワイイし頭もいいから人気ありそうなんだけどな。{w}じゃあ付き合うならどんなタイプが好みなんだ？"
    show SCG_11 6 with fastdissolve
    show SCG_11 at huruhuru
    rv "………"
    rv "その…特に考えた事はない、んですけど…明るくて誠実な方なら何方でも…？"
    pl "へぇ～意外とフツーの趣味してんな。{w}あ、じゃあさ！俺とかどうなんだ？"
    show SCG_11 7 with fastdissolve
    show SCG_11 at huruhuru
    rv "ハイ？{w}あ、{cps=*0.1}あ{/cps}の、{cps=*0.1}そ{/cps}の、{cps=*0.1}そ{/cps}れが…{cps=*0.1}[na]様はで{/cps}すね…"
    rv "いや{cps=*0.1}そ{/cps}の…{cps=*0.1}ボク…は…{/cps}"
    show SCG_11 9 with fastdissolve
    show SCG_11 at bounce
    rv "そ、そういえばボク、今ゴミを捨てに行くつもりでして…！" with sshake
    pl "ゴミ？何のゴミ？"
    show SCG_11 6 with fastdissolve
    rv "うーんと…うーんと…"
    show SCG_11 7 with fastdissolve
    rv "それが、ぁ！履いてたストッキングに穴が開いちゃいまして…"
    pl "あぁ～じゃあ俺が代わりに捨てとくぜ！"
    show SCG_11 6 with fastdissolve
    rv "…………"
    hide screen textbox with dissolve
    pause 1.0
    scene black with dissolve
    $ renpy.music.set_volume(2, channel="sound")
    play sound "audio/se/r18 2.ogg"
    pause 3.0
    scene bg104 with dissolve
    pause 1
    show SCG_11 ns 6 with dissolve
    show screen textbox with dissolve
    nar "ラヴィが履いてたストッキングを手に入れた！{w}帰り道に捨てておこう。"
    nar "ラヴィのヤツ、恥ずかしがっちまって。あのワーカホリックのラヴィもやっぱ普通の女の子なんだな。"
    $ renpy.music.set_volume(1, channel="sound")
    $ ask = ask + 1
    jump rv_ask


label rv_re:
    show SCG_11 0 with fastdissolve
    rv "ボクの答えが必要であれば、何でもお聞きください。"
    return


label rv_end:
    show screen textbox with dissolve
    show SCG_11 0 with fastdissolve
    rv "お話の途中申し訳御座いません、ボクはそろそろ食事の準備に向かわせて頂きますね。"
    pl "あ、そうだったな。いきなり引き留めてゴメンよ。"
    rv "いえ、寧ろ感謝させて頂きたいですもの。お坊ちゃまと会話できてとても楽しかったです。"
    show SCG_11 1 with fastdissolve
    rv "でも…次いらっしゃる際は今よりもう少し遅めに来た方が良さそうですね。"
    pl "心掛けておくぜ…"
    show SCG_11 4 with fastdissolve
    rv "それではお気を付けてお帰り下さい。今日も互いに愛し合います様に。"
    hide SCG_11 with dissolve
    nar "ラヴィアンに見送られて図書館から離れた。どうやら早く来すぎて余裕がなかったようだ。"
    nar "でも、この違和感は一体何だろう？俺が普段知っているローズとはまた何か違う様な気がする。"
    nar "やっぱり「彼女」ではないからだろうか…"
    nar "ラヴィアン・ローズと少し親しくなった。"
    hide screen textbox with dissolve
    stop music fadeout 2
    $ ask = 0
    $ askA = True
    $ askB = True
    $ askC = True
    nvl clear
    pause 1
    $ day_rs = True
    $ day_time = day_time +1
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_4
    return



label day4_rs_N:
    show screen nvlbox with dissolve
    "\n いつも静かな図書館だったが、今日はまた一段と静かだ。司祭たちは俺には目向きさえせず、各自の研究に励んでいる。"
    "もしやと思って部屋を探したが、やはり誰も居ない。今日はどうやらみんな忙しそうだ。"
    et "残念だが、後でまた来よう…"
    hide screen nvlbox with dissolve


label day4_gr_F:
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg06 with dissolve
    else:
        scene bg06_1 with dissolve
    call place06 from _call_place04_7
    show screen nvlbox with dissolve
    play music "audio/bgm/grette.ogg"
    "\n 珍しく、医務室の扉は閉めてある。医務室はいつも開いていると思っていたが、そうでもないようだな。"
    "かかった門札には子熊や蝶などの絵と共に\n「不在中{font=amii.otf}♡{/font}」と文字が書いてある。どうやら行き違ったようだ。"
    et "残念だが、後でまた来よう…"
    stop music fadeout 2
    hide screen nvlbox with dissolve
    nvl clear
    pause 1
    $ day_gr = True
    $ day_time = day_time +1
    scene bg06_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_4
    return




label day5_my_F:
    $ show_quick_menu = True
    with dissolve
    scene bg05_1 with dissolve
    call place05 from _call_place05_7
    play music 'audio/bgm/maya.ogg' fadein 3
    show screen nvlbox with dissolve 
    "\n 花壇には誰もいない…どうやらマヤは先に寮に帰ったようだ。"
    if (day_hk == True):
        "心の荷を下ろしたことまでは良いが、結局新しい情報はなかった。"
        et "やはり、直で解決するには…腕を切り取る以外には適当な仕方がないかもしれない。"
    else:
        et "残念だが、マヤはまた後から伺った方が良さそうだ…"
    stop music fadeout 3
    nvl clear
    hide screen nvlbox with dissolve 
    pause 1
    $ day_my = True
    $ day_time = day_time +1
    scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_5
    return


label day5_hk_F:
    $ show_quick_menu = True
    with dissolve
    scene bg04_1 with dissolve
    call place04 from _call_place04_8
    play music 'audio/bgm/golden haku.ogg' fadein 3
    show screen nvlbox with dissolve 
    "\n 作業場には何人かの司祭が巡っているだけで、主教様の姿は見えない…別の仕事の処理に行ったのか。"
    et "残念だが、ハク主教はまた後から伺った方が良さそうだ…"
    stop music fadeout 3
    nvl clear
    hide screen nvlbox with dissolve 
    pause 1
    $ day_my = True
    $ day_time = day_time +1
    scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_5
    return



label day5_cr_F:
    $ show_quick_menu = True
    with dissolve
    scene bg106_1 with dissolve
    call place106 from _call_place106_4
    play music 'audio/bgm/Clair.ogg' fadein 3
    show screen nvlbox with dissolve 
    show screen nvlbox with dissolve
    "\n 階段には誰もいない…どうやらクレアは、時間も遅いしもう家に帰ったようだ。"
    et "残念だが、クレアはまた後から伺った方が良さそうだ…"
    stop music fadeout 3
    nvl clear
    hide screen nvlbox with dissolve 
    pause 1
    $ day_my = True
    $ day_time = day_time +1
    scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_5
    return



label day5_gr_F:
    $ show_quick_menu = True
    with dissolve
    scene bg06_1 with dissolve
    call place06 from _call_place06_6
    play music 'audio/bgm/name select.ogg' fadein 3
    show screen textbox with dissolve
    nar "医務室の灯りはもう消してある。今まで灯りの消えた医務室は見たことがないのに、もう退勤したのか。"
    nar "怪しい気分で窓辺を覗き込んだら、中から微かな光が見える。そういえば扉もまだ開いているようだ。"
    nar "誰がいるのか…"
    show SCG_13 0 with dissolve
    gg "どうした？"
    pl "んぇ？昼間会った…"
    gg "[na]か。医務室に用事でもあるのか？"
    pl "別にそんなワケじゃないけど…グレーテ先生は何か別の用事があるんですね？"
    show SCG_13 8 with fastdissolve
    gg "そうだな。保健部は今日一日お前の件で騒がしかったものでな。"
    nar "そんな風に言われてもな…"
    show SCG_13 0 with fastdissolve
    pl "主教様がここにいらっしゃるのは初めて見た気がしますね。"
    gg "医務室に結構良く通っているらしいな。"
    pl "はい？い、いや、その…"
    gg "目的はグレーテか？"
    play sound "audio/se/hit.ogg"
    pl "は、はぁ？そんな不純な目的で来たわけないじゃないですか！{w}人を何だと思って…" with sshake
    pl "カウンセリングで来たんですよ。"
    show SCG_13 1 with fastdissolve
    gg "そうか？どうせカウンセリングが目的なら相手が俺でも構わんだろうな。{w}座れ、話を聞こう。"
    pl "いやいや…俺別に主教様に言いたいことは～…"
    show SCG_13 0 with fastdissolve
    gg "安心しろ、無意味なお説教はせんからな。"
    nar "…やってみろってんだ、コノヤロウ。"
    hide screen textbox with dissolve
    jump gg_ask
    return

label gg_ask:
    if (ask == 1):
        call gg_re from _call_gg_re
    elif (ask == 2):
        hide screen textbox with dissolve
        pause 1
        jump gg_end
    hide screen textbox with dissolve
    menu:
        "保健部について" if askA:
            $ askA = False
            jump gg1
        "グレーテについて" if askB:
            $ askB = False
            jump gg2
        "グレゴールについて" if askC:
            $ askC = False
            jump gg3

label gg_re:
    show SCG_13 0 with fastdissolve
    gg "で、何か言いたいことはあるか？"
    return

label gg1:
    show screen textbox with dissolve
    pl "じゃあ…保健部って正確にどんな部署なのかが聞きたいんだけど。"
    gg "どんな質問をしてくるかと思ったが、見た目よりは大分堅実な質問だったな。"
    pl "だから、主教様とはあんま話す事もないんだって…"
    show SCG_13 8 with fastdissolve
    gg "保健部は…お前の知る通り、神殿内の司祭達の手助けのための部署だ。"
    gg "主に神殿病院と並立し患者を治療する仕事をしているが、司祭達の細々とした便宜も見てやっている。"
    pl "こまごまとした便宜って言うと？"
    show SCG_13 0 with fastdissolve
    gg "服に追加のポケットをくっつけたり、外れたボタンを直したり…"
    gg "お前達が勝手に放っぽったタオルや布団の洗濯もしたりだな。"
    pl "保健部ってのはクリーニング店さんなのか？"
    gg "その通りお前達の雑巾さながらの精神を縫い合わせる仕事も兼ねている。{w}後は配食のメニューも考えて置いたり。"
    pl "マジ？アップルパイの日をもっと増やしてください。"
    show SCG_13 6 with fastdissolve
    gg "お前みたいな奴らのせいでやり甲斐がないってことだ。"
    pl "前から思ってたことなんだけど…"
    pl "どっちにしろタバコ臭いオッサンにはあんまり似合わない繊細な仕事っぽいけど"
    pl "何がどうなって主教の座まで上がっちゃったんですか？"
    show SCG_13 0 with fastdissolve
    gg "お前が言わずとも俺も最初は同じことを思ったもんだな…"
    gg "どれ、あれはもう八年前だったか。{w}大事な仕事の為に司祭をやめて、故郷に戻るつもりだったが…"
    show SCG_13 8 with fastdissolve
    gg "丁度前任主教の退任と事が重なってしまい、この報告を聞いて枢機卿様が俺を主教に昇らせてしまったんだ。"
    gg "しかし俺が主教の職を得たのと同時にその「大事な事」も解決してしまった。"
    pl "主教になるぐらいなら結構有能な司祭だったんだろうな…"
    pl "それを全部やめちまうぐらい大事な事って何だったのか気になるぜ。"
    show SCG_13 1 with fastdissolve
    gg "さあな…熱情的な誰かさんに魅かれてしまったとだけ言っておこうか。"
    $ ask = ask + 1
    jump gg_ask

label gg2:
    show screen textbox with dissolve
    pl "グレーテ先生についてどう思いますか？"
    show SCG_13 7 with fastdissolve
    gg "何が聞きたいのかが丸見えだな。"
    show SCG_13 0 with fastdissolve
    gg "それは勿論、良い人だと思っている。"
    gg "強く、何事にも熱情を持って取り掛かるから学ぶところも多い。それはお前も良く知っている所だろう。"
    pl "まあ…それはそうなんですけど。{w}昼間会った時とか妙に気兼ねないなって印象だったからどれだけ古い知り合いだったのかなって…"
    gg "グレーテから聞いてなかったのか？俺とグレーテは同じ修道院出た昔からの友達だ。"
    show SCG_13 8 with fastdissolve
    gg "成人式を迎える前からずっと知り合っていたな…{w}イヴリン・ヴィオレッタと共に。"
    pl "あれ？グレーテ先生ならともかく学術部主教様とも…？すっごく意外だな。仲悪いのかなって思ってたんですけど。"
    show SCG_13 0 with fastdissolve
    gg "…俺もそう思っている。あの女とは両親の間の縁で知り合っていたのだが…"
    gg "幼い頃から結構独特でな、グレーテじゃなけりゃずっと一言も交わさず終わっていたのかも知れないな。"
    pl "はは、そう言うと大体想像つくな。"
    gg "俺達二人とはまた違ってグレーテは州都生まれじゃなかったから、通学路でかなり苦労していたな…"
    show SCG_13 1 with fastdissolve
    gg "しかし嫌味一つ言った事がない。{w}全く、一生見て来たがやはり凄い女だよ。"
    $ ask = ask + 1
    jump gg_ask

label gg3:
    show screen textbox with dissolve
    nar "…待てよ。"
    nar "………いくら…気まずいからってこんなの本当に聞いていいのか？"
    nar "…こんなけむくじゃらのオッサンに詳しくなって何が嬉しいんだ…？"
    pl "………"
    gg "どうした？"
    pl "イ、イエ…その…何も。"
    gg "…そう言えば、お前は一人っ子なのか？それか歳の離れた兄弟がいるのか。"
    pl "ぅえ、一応後者ですけど。"
    gg "だろうな。{w}妹弟は幼すぎるし、逆に兄や姉たちは歳の差が大きくて一緒に遊べる兄弟がいなかったのだろうな。"
    gg "そのまま孤立するのが嫌で家を出たのか。"
    pl "おっ！ソレっす。{w}でも孤立されるのが嫌だったってか、何か息苦しかったっていうか。"
    gg "里では出来なかったことがしたくて？"
    pl "あ～！合ってます合ってます。"
    gg "お前、A型の夏生まれだろう？犬より猫派。{w}懐かれてはいなさそうだが。"
    pl "ヤバ！どうやってわかったんですか？"
    show SCG_13 at bounce
    show SCG_13 1 with fastdissolve
    gg "少しばかり読心術が出来るんでね。"
    gg "外地の若い子が好み進んで州都の神殿まで来るのは珍しい。"
    gg "生活が変わって適応しづらいだろうが、少しばかりの辛抱だと思って頑張りなさい。"
    gg "ココアでも飲むか？"
    pl "おぉ～あざーっす！頑張ります！ココアより牛乳派～…"
    play sound "audio/se/hit.ogg"
    nar "…ハッ！いつの間に自分についてばっか喋ったじゃないか！" with sshake
    $ ask = ask + 1
    jump gg_ask

label gg_end:
    show SCG_13 0 with fastdissolve
    show screen textbox with dissolve
    gg "これぐらいでその好奇心も満たされただろう。"
    pl "何でもない雑談ばっかしたクセに、何が…"
    gg "お前もそろそろ寮に戻るべき時間ではないのか？"
    gg "休むべき時を逃しその腕に更なる負担が掛かれば、お前自身だけでなく周りの人間にも大きな迷惑となるぞ。"
    pl "お説教はしないって言ってなかったっけ～？"
    show SCG_13 8 with fastdissolve
    gg "「無意味な」説教はしないと言っただけだ。"
    pl "……ウザ。"
    show SCG_13 0 with fastdissolve
    gg "容態が悪くなるようだったら遠慮なく訪ねなさい。"
    hide SCG_13 with dissolve
    nar "俺は大人しく医務室を離れた。{w}結局オッサンの時間潰しに釣られた様だな。"
    nar "後からは医務室に来るときは、もう少し早く来た方が良いかもしれない。"
    nar "グレゴール主教と少し親しくなってしまった…"
    hide screen textbox with dissolve
    stop music fadeout 2
    $ ask = 0
    $ askA = True
    $ askB = True
    $ askC = True
    nvl clear
    pause 1
    $ day_gr = True
    $ day_time = day_time +1
    scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_5
    return


label day5_ar_F:
    $ show_quick_menu = True
    with dissolve
    scene bg03_1 with dissolve
    call place03 from _call_place03_17
    play music 'audio/bgm/daily.ogg' fadein 3
    show screen textbox with dissolve
    nar "遅すぎたせいか、訓練場の扉には鍵がかかっていた。仕方なく帰ろうとしたが…後ろからヘンな臭いがする。"
    nar "決して慣れていないが、何度か嗅いだことがあって覚えている臭い…{w}タバコの臭いだ。"
    nar "魔導部の訓練場でタバコって、どういうことだ？"
    nar "…建物の後ろに行ってみれば、真っ黒の男何人かが集まって煙を出していた。"
    nar "どうやら処理班の司祭らしいが、真ん中の男は特に背が高くて目立つ。しかも俺を見つけたか驚いた顔をした。"
    play sound "audio/se/hit.ogg"
    en "おいおい、はよ火消せよ。{w}主教様もうすぐいらっしゃるんだぞ。" with sshake
    nar "タバコを踏み消した司祭たちが忙しい歩きでちらほらと離れる。"
    nar "彼は司祭たちに手を振ってあげたり、笑って挨拶してあげたりして親しく見送りをしては俺の方に向き直った。"
    hide screen textbox with dissolve
    pause 1
    show SCG_08 3 with dissolve
    show screen textbox with dissolve
    en "……あの、そのォ…[na]さん？"
    pl "ぇ…うん、俺が邪魔になったっぽいな、ゆっくりどぞ…"
    show SCG_08 5 with fastdissolve
    en "あ！いえ、違うッス！{w}僕普段酒も口にしてないんスよ、これは…" with sshake
    show SCG_08 0 with fastdissolve
    show SCG_08 at bounce
    en "これが実は今さっき初めて吸ったヤツで！"
    pl "だろーな…"
    show SCG_08 7 with fastdissolve
    en "うぅ…お願いだから姉上には言わないでほしいッス…"
    pl "あ、主教様はいいんだ。"
    show SCG_08 1 with fastdissolve
    en "まあタバコぐらい主教様もやってますしね、ハハッ。"
    nar "そういう問題じゃないだろう…"
    show SCG_08 0 with fastdissolve
    show SCG_08 at bounce
    en "丁度暇だし、良かったら話相手に付き合ってくださいよ～！"
    hide screen textbox with dissolve
    jump en_ask
    return

label en_ask:
    if (ask == 1):
        call en_re from _call_en_re
    elif (ask == 2):
        hide screen textbox with dissolve
        pause 1
        jump en_end
    hide screen textbox with dissolve
    menu:
        "天気について" if askA:
            $ askA = False
            jump en1
        "エノクについて" if askB:
            $ askB = False
            jump en2
        "友達について" if askC:
            $ askC = False
            jump en3

















label en1:
    show screen textbox with dissolve
    pl "……今日はいい天気だな。"
    show SCG_08 5 with fastdissolve
    en "うわ、やめて！あからさまに気まずいオーラ出さないで！" with sshake
    pl "明日のお昼なんだろ～な～？"
    show SCG_08 2 with fastdissolve
    en "う…大体、なんでこんな遅く訪問なさったんスか…？僕もう既に戸締りしちゃいましたよ。"
    pl "戸締り確認の人が外に居ていいの？"
    show SCG_08 0 with fastdissolve
    en "いッスよ別に、中入って締め直せばいいッス。"
    pl "神殿の戸締り方針は不思議なこった。"
    en "…お恥ずかしい姿を御見せした上無駄足させたのも申し訳ないし、簡単に運試しでもどうッスか？"
    pl "ん？そんなことも出来るのか？"
    show SCG_08 1 with fastdissolve
    en "僕、こう見えて預言者家門の末っ子なんスよ、ハハ！{w}全く才能無くて追い出されたんスけどね…"
    pl "あれま…兄ちゃんにもいろいろあったんだな。"
    show SCG_08 0 with fastdissolve
    en "ともかく…元々能力をこういうとこに乱用しちゃダメなんスけど、折角だし見てあげますよ。"
    pl "いいぜ！聞いて損はないだろうし。"
    show SCG_08 9 with fastdissolve
    en "うーむ……"
    play sound "audio/se/ding.ogg"
    call bgw from _call_bgw_3

    $ import random
    $ r = random.random()

    if r < 0.7:
        $ fate = "normal"
    elif r < 0.9:
        $ fate = random.choice(["small", "bad"])
    else:
        $ fate = random.choice(["greatbad", "greatgood"])
    jump show_fortune

label show_fortune:


    "{nw}"
    nvl clear
    if fate == "normal":
        en "[na]さん、悪運が強いッスね。{w}望んでいたものを手に入れることが出来るんスけど…"
        en "大事なものも失ってしまいそうッス。いつか大事に巻き込まれてしまうかもッスよ。"
        en "安全になるまではあんま好奇心とかお節介になるのは禁物ッス。"
        pl "エッ…よくないことばっかじゃないか、聞いて損した！"
        show SCG_08 1 with fastdissolve
        en "まあ、運試しってのが元々合ってたら不思議で合ってなかったらそんなもんッスよ！"
        show SCG_08 at bounce
        en "そんな気にしなくても良いッスよ～ハハ。"

    elif fate == "small":
        show SCG_08 0 with fastdissolve
        en "[na]さん、今日は小吉ッスね。{w}悪くはないけど、めっちゃ良くもないッス。"
        en "やる気次第で結果がガラッと変わる感じッス。{w}ま、どっちかって言えば頑張った分だけ報われる方ッスね～！"
        show SCG_08 1 at bounce
        en "あと、人に優しくすると倍になって返ってくるかもッスよ。"
        play sound "audio/se/ding.ogg"
        pl "倍返し？{w}じゃあ献金しとくか～！"
        play sound "audio/SE/hit.ogg"
        show SCG_08 12 with fastdissolve
        en "そっち系の倍返しじゃないッス～！"

    elif fate == "bad":
        show SCG_08 10 with fastdissolve
        en "[na]さん、今日は…{w}うむ、ちょい凶ッス。{w}焦ると空回りする日ッスね。"
        show SCG_08 1 with fastdissolve
        en "けどッスね、運ってのは、日々の積み重ねで引き寄せるもんッス！"
        show SCG_08 0 with fastdissolve
        en "目の前の一歩を丁寧に踏みしめていけば、結果はあとからついてくるッスよ！"
        show SCG_08 at bounce
        en "だから、どんな時でも姿勢正しく！心折れずに！全力疾走ッス！"
        pl "お、おう…慎重に生きるわ。"
        show SCG_08 at bounce
        en "いいッスね！その意気ッス！でも慎重すぎもダメッス！"
        show SCG_08 1 at bounce
        play sound "audio/SE/hit.ogg"
        en "行動あるのみッス！" with sshake
        extend "止まったら終わりッス！" with sshake
        extend "汗は裏切らないッス！" with sshake
        pl "お、お、おう…。"
        show SCG_08 2
        play sound "audio/SE/hit.ogg"
        en "気合いだ!!" with sshake
        show SCG_08 7
        play sound "audio/SE/hit.ogg"
        extend "君ならできる!!" with sshake
        show SCG_08 5
        play sound "audio/SE/hit.ogg"
        extend "諦めんな!!!" with sshake
        nar "……やっぱり聞くんじゃなかった。"

    elif fate == "greatbad":
        show SCG_08 7 with fastdissolve
        en "[na]さん、聞きたくなかったら今のうちに耳ふさいでくださいッス…{w}今日、大凶ッス。"
        show SCG_08 at huruhuru
        en "何やっても裏目に出る可能性がマシマシッスね。"
        show SCG_08 1 at bounce
        en "…{w=0.2}…{w=0.2}でも{w=0.2}逆に言えば、ここからは上がるしかないッス！"
        nar "……"
        pl "おい、"
        play sound "audio/se/ding.ogg"
        extend "それ慰めになってねぇぞ。"
        play sound "audio/SE/hit.ogg"
        show SCG_08 11
        en "あ、いやいやいやいや！安心するッス！{w}こうして肩でも…" with sshake
        show SCG_08 8:
            easeout 0.07 xoffset 6
            easeout 0.07 xoffset -6
            easeout 0.07 xoffset 5
            easeout 0.07 xoffset -5
            easeout 0.1 xoffset 2
            easeout 0.1 xoffset 0
            easein 0.15 xoffset 30
            ease 0.6 xoffset -520
        extend "トントン。"
        play sound "audio/SE/hit.ogg"
        pl "ちょ、なんで距離取ってんだよ！" with sshake
        hide SCG_08 with fastdissolve
        show SCG_08 13 with fastdissolve
        en "い、いや～そのッスね……し、神聖の流れは身体接触でも伝わるって言うんスよ！"
        show SCG_08 8 at bounce
        en "ま、魔導師同士の話ッスけどね！？"
        show SCG_08 14 at bounce
        en "うむ……あ、そ、そろそろ主教様を起こしに行かなきゃ～！"
        play sound "audio/SE/hit.ogg"
        pl "逃げんな！説明になってねぇぞ！" with sshake
        play sound "audio/SE/hit.ogg"
        show SCG_08 1
        en "あ、安心するッス！運命に負けず、今日を生き延びたら、明日は確定で大吉ッス！" with sshake
        $ show_say_ex()
        show SCG_08 8 with exfastdissolve
        $ hide_say_ex()
        extend "……たぶん"
    else:

        show SCG_08 1 with fastdissolve
        en "[na]さん、今日の運勢はバリバリ大吉ッス！{w}努力がちゃんと報われる日ッスよ！"
        en "欲しかったものも自然と手に入るし、周りも味方してくれるッス！"
        show SCG_08 0 with fastdissolve
        en "ただし、調子に乗りすぎると運気が逃げるッス。感謝は忘れないでほしいッス！"
        pl "うわ、完璧じゃん！これで今日サボっても許される気がする！"
        play sound "audio/SE/hit.ogg"
        show SCG_08 5
        en "サボるのは大凶フラグッス！フラグ立てないでほしいッス！" with sshake

    $ ask = ask + 1
    jump en_ask

label en2:
    show screen textbox with dissolve
    show SCG_08 at bounce
    en "僕ッスか！魔導部補佐教エノク・アピス、収穫の月十九日生まれ！"
    en "血液型はA型！夏か冬かって言うなら夏！猫派か犬派かって言うなら犬派ッス！"
    en "職業は大陸で数えて三番目に来る凄腕の魔導師！あと趣味で神殿の広報大使やってるッス。"
    en "サインはどこにしましょっか？"
    pl "い…いや欲しくねえよ！"
    show SCG_08 1 with fastdissolve
    en "あ！サーセン、つい癖で…{w}いや～しっかしこれ恥ずかしいッスね。ハハッ！"
    en "[na]さんもミサにはちゃんと毎回参加して、献血も定期的にやりましょ～！"
    pl "兄ちゃんっていっつも元気だよな。{w}兄ちゃんが三番目ってことは一番と二番は主教様に姉さんか！"
    show SCG_08 0 with fastdissolve
    en "勿論ッス。あの方々は大陸で最もで、自分の中でも最高なんスよ！"
    show SCG_08 4 with fastdissolve
    en "実は三番目なんておこがましい発言ではあるんスけど…{w}しかし目標は高く持つべしってね！"
    pl "ふ～ん{w}けどお兄ちゃんはそんな立派な司祭様のくせに聖痕がこれっぽちも見当たらないな？"
    show SCG_08 8 with fastdissolve
    show SCG_08 at bounce
    en "あんまりジロジロ見ないで欲しいッス！{w}これには全部「オトコの事情」ってものがあるんスよ～エッヘン。"
    pl "へぇ…"
    pl "オトコの事情かぁ…{w}よおくわかりました。"
    show SCG_08 10 with fastdissolve
    pl "じゃあ俺も神殿で唯一背中を任せられる漢の兄上が実は常に非行を行うヤニカスでしたって"
    show SCG_08 11 with fastdissolve
    pl "魔導部主教様に相談しようかなって思うんだけどいいよな？"
    show SCG_08 2 with fastdissolve
    en "いやそんな卑怯な…！こういう時ばっか兄貴扱いやめてくださいよ～！" with sshake
    show SCG_08 7 with fastdissolve
    show SCG_08 at huruhuru
    en "普通に見せるにはちょっと恥ずかしいとこにあるから隠してるだけッスよ…[na]さんは配慮が足りないッスね！"
    pl "ハハ、最初っからそう言えよ～！今回ばかりは好奇心が[na2]くんを生かしたな！"
    pl "聖痕が恥ずかしいとこにあるってどんだけだよ～…"
    pl "……"
    pl "{cps=*0.1}……ェ…"
    show SCG_08 10 with fastdissolve
    en "……"
    pl "あのさ…勝手に言っちまってゴメンな…お墓までもってくからさ…"
    show SCG_08 9 with fastdissolve
    en "……あの、何考えてるのか分からないッスけど、とりあえず言っとくとちんこじゃないッスからね。"
    pl "えっ…あぇ…"
    show SCG_08 7 with fastdissolve
    nar "……"
    $ ask = ask + 1
    jump en_ask

label en3:
    show screen textbox with dissolve
    pl "今の…浄化部の司祭達だよな？"
    show SCG_08 0 with fastdissolve
    en "まあ、そッスね。{w}ちょっと行き過ぎる感はあるんスけど、でも愉快な弟たちッスよ。"
    pl "友達とはああやって遊んでんのは元から？"
    show SCG_08 3 with fastdissolve
    en "だ…だから、違いますって…{w}不良は神殿に入る丁度一年前ぐらいちょっとやって辞めたッス。"
    pl "おっ、ならガールフレンドとかもいたんじゃね？"
    show SCG_08 2 with fastdissolve
    en "なんで話がそうなるんスか…？まあ、いたっちゃいたんスけど…"
    pl "へぇ…気になるな～"
    show SCG_08 8 with fastdissolve
    en "そんな面白い話でもないッス…{w}短髪の、かわいい系だったんスけど…"
    en "僕より一つ下だったのもあって、段々申し訳ない気持ちが勝ってしまって別れちゃいました。"
    pl "兄ちゃんって意外とワルな男スタイル？"
    show SCG_08 11 with fastdissolve
    en "ち、ちがうッス！僕はどうにも、神殿に行くまであと僅かでしたし…"
    show SCG_08 8 with fastdissolve
    en "あの子は僕なんかよりもっと良い人に出会えそうな気がして…ってのと、その…"
    en "他の誰か想っている人が居るクセに誰かと付き合うのは無礼だなって気がして。"
    show SCG_08 12 with fastdissolve
    pl "兄ちゃん…そういや、姉さんとも歳一つ差だったよな？"
    show SCG_08 8 with fastdissolve
    en "………とにかく、僕は外出ても友達が勧めてくる酒は全部断ってるし、"
    show SCG_08 4 with fastdissolve
    show SCG_08 at bounce
    en "どれだけ楽しい時間を過ごしてても門限はキッチリ守って帰宅する規則正しいはなまる生活を送ってるんスよ！"
    nar "はなまるよりは「ヤなまる」が付けられそうだな…"
    $ ask = ask + 1
    jump en_ask

label en_re:
    show SCG_08 0 with fastdissolve
    en "折角の機会なんだし、気になる事があるならバンバン聞いて欲しいッス！"
    return

label en_end:
    show SCG_08 0 with fastdissolve
    show screen textbox with dissolve
    pl "こんなところであんま騒いでても兄ちゃんに迷惑だろうし、俺そろそろ大人しく帰るよ。"
    show SCG_08 8 with fastdissolve
    en "そうして頂けるとありがたいッス…{w}はぁ、姉上が今日ずっと[na]さんの心配を凄くしてたッスよ。"
    show SCG_08 10 with fastdissolve
    en "もうちょっと早めにいらしてたら良かっただろうに…"
    pl "あ…そういえば、姉さんは忙しい中に俺のお見舞いにも来てくれてたもんな。これは申し訳がないな…"
    pl "姉さんが起きたら俺の代わりに挨拶しといてくれよ。"
    show SCG_08 0 with fastdissolve
    en "ええ、こっちはご心配なく。お気を付けてお帰りくださいね。"
    hide SCG_08 with dissolve
    nar "昼と夜の差が曖昧であるこの時期にも、遅くなってからは色々起きるんだな…"
    nar "後からは訓練場に来る時は、もう少し早く来た方が良いかもしれない。"
    nar "エノク・アピスと少し親しくなったかもしれない…"
    hide screen textbox with dissolve
    stop music fadeout 2
    $ ask = 0
    $ askA = True
    $ askB = True
    $ askC = True
    nvl clear
    pause 1
    $ day_ar = True
    $ day_time = day_time +1
    scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_5
    return

label day5_rs_F:
    $ show_quick_menu = True
    with dissolve
    scene bg104 with dissolve
    call place104 from _call_place104_6
    play music 'audio/bgm/biblioteca.ogg' fadein 3
    show screen textbox with dissolve
    nar "扉が開いたのでまだ人がいると思ったが、図書館には誰もいない。"
    nar "もしかしたら学術部の司祭たちが人っ気を隠しているのかもしれない。"
    nar "せっかくここまで来たし、せめて本でも読んで行こうか…"
    nar "角を曲がると、本を開いておいたイヴリン主教がいた。"
    nar "この人はいつもいきなり後ろから現れたりするから、じっと立っている姿は到底見慣れないな。"
    pl "よぉ。"
    show SCG_10 0 with dissolve
    ev "…アラアラ、これはまた…フフ。"
    pl "やっぱ驚きもしないな。"
    ev "驚きましたとも、丁度貴方の事を考えておりましたので。"
    pl "え、マジで？"
    show SCG_10 2 with fastdissolve
    ev "無論で御座います…{w}貴方が昼間御見せして下さいました奇跡、はぁ…"
    ev "一瞬たりとも忘れられません。終日頭から離れないのです…"
    pl "……"
    show SCG_10 0 with fastdissolve
    ev "其れで、素敵な貴方様は図書館には如何なさいまして？"
    pl "ん？や…まだ開いてたから入ってみただけだけど。"
    show SCG_10 2 with fastdissolve
    ev "ウフフ…如何やら、この私が貴方を引き寄せてしまいました様で…時間を奪ったからには其れ相応の責任を取らねばなりませんね。"
    ev "宜しければ、私と談笑等は如何でしょう…"
    pl "イヴリン主教様と？なんか珍しいチャンスみたいでドキドキするな。"
    show SCG_10 1 with fastdissolve
    ev "私も同じく感じます。ウフフ…フフ…"
    pl "罠に嵌まっちまったってワケじゃなきゃ良いけどな…"
    hide screen textbox with dissolve
    jump ev_ask
    return

label ev_ask:
    if (ask == 1):
        call ev_re from _call_ev_re
    elif (ask == 2):
        hide screen textbox with dissolve
        pause 1
        jump ev_end
    hide screen textbox with dissolve
    menu:
        "学術部について" if askA:
            $ askA = False
            jump ev1
        "主教について" if askB:
            $ askB = False
            jump ev2
        "イヴリンについて" if askC:
            $ askC = False
            jump ev3

label ev1:
    show screen textbox with dissolve
    pl "あのさ…学術部って正確には何やる所なんだ？禍を研究してるだとかは聞いたんだけど。"
    show SCG_10 0 with fastdissolve
    ev "朝方には大地の動きを観察し、夜中は宇宙の震えを観測して…その恩を受け入れる場所で御座います。"
    pl "めちゃめちゃにヒマそうじゃんかよ…"
    show SCG_10 4 with fastdissolve
    ev "そして又は…古代の遺物を解読し実用化したり、自由研究を進めたり等…浪漫のない仕事も兼ねております。"
    pl "そっちがもっとロマンありげだけどな？古代の遺物って正確にどんな感じなんだ？"
    show SCG_10 0 with fastdissolve
    ev "我々が生きている此の地、現在は誤って足を踏み入れるだけで"
    ev "哀れな魂達の断末魔が上がる様な呪われてしまった地で御座いますが…"
    ev "二千年前、大災害の起こる前までは電気で構成されたコンクリートの建物が並んだ広くも狭苦しい地であったそうです。"
    pl "そ、それって一体どういう事なんだ？"
    show SCG_10 2 with fastdissolve
    ev "ですから、古代の人々は神の下った禍よりも人間の悪に怯え生きて来た…とても気楽で進歩した、怠惰な種族だったと云う事です。"
    ev "なので我々もまた彼らの足跡を懸命に追いつつ、彼らを更に怠けた魔獣とさせたであろう便利を研究しているのです。"
    pl "何で話がそう繋がるのかは分かんないけど…スゴいことをやってるってことはわかったぜ。"
    pl "電気を使うって言うと、電話やラジオみたいなモンなのかな…"
    show SCG_10 3 with fastdissolve
    ev "アラ…私の司祭達にその様な疑問をお聞きなさるなら、更に素晴らしい物を貴方の視神経に捧げられますのに…"
    pl "見てて思うんだけどさ、イヴリン主教様って司祭たちの事ホント好きだよな。"
    show SCG_10 1 with fastdissolve
    ev "無論…何と言っても、私が直接厳選した可愛い我が子たちですもの…フフ、フフフ…"
    $ ask = ask + 1
    jump ev_ask

label ev2:
    show screen textbox with dissolve
    pl "イヴリン様って…やっぱ保健部主教様とは仲が悪いのか？"
    show SCG_10 1 with fastdissolve
    ev "そんな、とんでもない。"
    ev "彼は私の古くからの縁の内の一つで、私という人間を作る数多の欠片の内の一部となってくれていますもの。"
    show SCG_10 2 with fastdissolve
    ev "勿論…彼の愛らしいグレーテちゃんも。"
    pl "グレーテ「ちゃん」…？"
    show SCG_10 0 with fastdissolve
    ev "私、あの二人とは幼い頃から友達でして。"
    ev "よく雑巾を縫って作ったボール一つで草原を走り回ったり、短くなって行く黄昏の影を追いながら鬼ごっこもしていたものです。"
    show SCG_10 2 with fastdissolve
    ev "私は幼い頃身体が弱かったもので、遠くから彼らの美しい時間を目に留める事しか出来ませんでしたが…"
    pl "主教様たちと先生にも幼い頃があったなんて…{w}まあそりゃそうだろうけど、想像付かないな。"
    ev "勉強のため教育院に入った彼らと違って、私は成人式を終えて直ぐ神殿に入ってしまったので、"
    ev "彼らと再会するのはまた後日となりましたが…"
    show SCG_10 0 with fastdissolve
    ev "別れがあれば出会いもまたあると云うもの。{w}貴方の慕うハクにゃんに出会ったのもその頃ですね。"
    pl "もしかして俺をからかいたくてわざとそんな呼び方してるのか？"
    show SCG_10 4 with fastdissolve
    ev "勿論当時は恐れ多い私が撫でられるような猫様ではなく、お世話すべきお嬢様でした。"
    ev "彼女も初めて会った頃は綿毛の様に軽かったのに、今は…"
    show SCG_10 1 with fastdissolve
    ev "更に色気が増していると云うか、フフ。本当のお嬢様になられておりますね…"
    pl "……あ、じゃあ魔導部主教様も？"
    show SCG_10 3 with fastdissolve
    ev "魔導部の…{w}嗚呼、エリィ主教様ですか。"
    show SCG_10 4 with fastdissolve
    ev "はい。あの頃はとても身長のお高い方でした…{w}それも全て彼が齎した結果でありましょう。"
    pl "なんか知らない人いなくね？枢機卿様とも仲いいんじゃない？"
    show SCG_10 0 with fastdissolve
    ev "たかが主教である私が親密さなど感じていい存在ではないでしょうが、まぁ…"
    show SCG_10 1 with fastdissolve
    ev "丁度昨日も図書館にいらして、お茶をお供致しましたね。"
    pl "わぁ…"
    $ ask = ask + 1
    jump ev_ask

label ev3:
    show screen textbox with dissolve
    show SCG_10 0 with fastdissolve
    ev "アラアラ…{w}誰でしょうねえ？その聡明さと美しさを兼備した人は。"
    show SCG_10 1 with fastdissolve
    ev "私も其の御方について是非詳しく知りたい物です。フフ…"
    pl "……"
    show SCG_10 2 with fastdissolve
    ev "私の所見ですと、憶測では御座いますが新入生の頃から既に非凡な頭脳を用いて"
    ev "世を翻す様な論文を書き下ろし上司の総愛を受けて居て、歩く姿は丸で一匹のペルシャ猫の如く足音をも立てず、"
    ev "他人の体液を採取し魅惑的な香水を創る趣味が有りそうですが…ウフフ。"
    pl "マジでワケわかんねえ女…"
    show SCG_10 0 with fastdissolve
    ev "誓いをばら蒔く女性で御座います。"
    pl "誓い？なんだそれ……"
    hide SCG_10 with dissolve
    call bgw from _call_bgw_4
    nar "……？？？！！"
    nar "急に触れられた柔い何かによって、俺の口は塞がれてしまった…"
    show SCG_10 2 with dissolve
    ev "口は災いの門。然し又関係の始まりを知らせ、生命を繋ぐ一番純粋なる門…"
    ev "州都では誓いを「此処」で行うのですよ。ウフフ…"
    play sound "audio/se/hit.ogg"
    pl "こ…こ…こんなのを誰にでも…？！軽薄だ！アンタ修道女だろうがよぉ！" with sshake
    show SCG_10 3 with fastdissolve
    ev "それは失礼ですよ。「誰にでも」なんて行いません。"
    show SCG_10 2 with fastdissolve
    ev "何処までも好意からの誓い、貴方と私の縁が繋がった事を祝福する為の儀式で御座います…"
    show SCG_10 0 with fastdissolve
    ev "然し、フフ…{w}軽薄、ですか。{w}其の通り、私は未だ皮も剥けておらぬ御転婆娘なのです。"
    ev "誰かに真なる愛を受ける日には、一人の女性として羽化出来るやも…"
    pl "イヴリン様に恋するなんて相当肝が据わってないと無理そうだな…"
    ev "肝は然程大事でもありません。重要なのは真心…愛は全てを凌駕するのです。"
    ev "人間は誰もが皆、互いに愛をする為生まれて来た動物ですから。"
    show SCG_10 2 with fastdissolve
    ev "ただその中でも質素で安定的な、然し人一倍の熱情を心に秘めており常に私の好奇心に応えてくれる、"
    ev "根性と優しさを兼備した可愛い人が良さそうですね…"
    show SCG_10 1 with fastdissolve
    ev "学歴は…私の頭の良さ程度で、まあ然程大事では無いのですが…せめて私と会話が出来る位であれば。{w}ウフフ…"
    pl "いや、それもうその時点で常人じゃないから…"
    show SCG_10 0 with fastdissolve
    ev "[na]様もそれなりに美味しかったですよ。"
    show SCG_10 1 with fastdissolve
    ev "何と言いましょうか、子供の優しさと男性の激しさを併せ持つ唇でした。"
    ev "百点満点を基準に、64点と云った所でしょうか…フフ。"
    ev "お外で自慢なされても良いのですよ。大陸一明晰な美女との初めてのキスを…"
    play sound "audio/se/hit.ogg"
    pl "は、初めてじゃねえし！" with sshake
    show SCG_10 2 with fastdissolve
    ev "アラ、はいそうですか…其の様に思われてしまうとは残念ですね…フフ。"
    nar "…クソッ！やっぱり嵌められた！"
    $ ask = ask + 1
    jump ev_ask

label ev_re:
    show SCG_10 0 with fastdissolve
    ev "それで…他には何が御気になさいまして？"
    return

label ev_end:
    show screen textbox with dissolve
    show SCG_10 0 with fastdissolve
    pl "俺、そろそろ帰らないとな。"
    ev "もうお帰りに為られるのですか？中で温かいお茶でも飲んで行かれたら如何でしょう。"
    pl "いや…主教様にはどうでもいいかもだけど、浄化部の俺はあんま遅く帰ると大変なことになるから…"
    pl "主教様はまだここに残るのか？"
    show SCG_10 1 with fastdissolve
    ev "ええ、本達と共に夜を過ごすのが好きでして。{w}夜通しお互いが見て来た物について語り合う心算です…"
    ev "ですので、私でない他の縁を御捜しの場合はもう少し早めにいらした方が良いですよ…"
    pl "うっ…俺が誰に会いたがると思って…"
    show SCG_10 2 with fastdissolve
    ev "其れは勿論…私の可愛いラヴィではないでしょうか。{w}或いは…塔の御姫様でしょうね。ウフフ…"
    pl "……"
    show SCG_10 0 with fastdissolve
    ev "では…御機嫌よう。次に逢うその日まで、その御身体を大切に…"
    hide SCG_10 with dissolve
    nar "背筋がぞっとして図書館から離れた。何度も会ってもおぞましい人だ。"
    nar "次図書館に来る時は、もう少し早く来た方が良いかもしれない。"
    nar "イヴリン主教と少し親しくなってしまった…"
    hide screen textbox with dissolve
    stop music fadeout 2
    $ ask = 0
    $ askA = True
    $ askB = True
    $ askC = True
    nvl clear
    pause 1
    $ day_ar = True
    $ day_time = day_time +1
    scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_5
    return


label day5_ev:
    stop music fadeout 3
    pause 1
    $ show_quick_menu = True
    scene bg02_2 with dissolve
    call place02
    show screen textbox with dissolve
    nar "…もう空が真っ暗だ。"
    hide screen textbox with dissolve
    hide screen textbox with dissolve
    $ show_quick_menu = False
    show screen place_day5_hkA with fastdissolve
    $ place = renpy.call_screen("place_day5_hkA")
    return

label day5_hkA:

    if persistent.no_girls == False:
        $ persistent.no_girls = True
        if not achievement.has("outsider"):
            $ achievement.grant("outsider")
            $ achievement.sync()

    show screen place_day5_hkA
    show screen place_rs
    with None
    stop music fadeout 3
    hide screen place_rs
    hide screen place_day5_hkA
    $ show_quick_menu = True
    with dissolve
    scene bg104 with dissolve
    call place104
    play music 'audio/bgm/biblioteca.ogg' fadein 3
    show screen textbox with dissolve
    nar "何となく図書館へ足を運ぶ。扉は開いていたので人が居るのかと思いきや図書館には誰も居ない。"
    nar "角を回ると人の気配を感じる。見慣れた白髪。"
    nar "嬉しい顔に挨拶でもしようかと思った瞬間に違和感を感じてしまった。"
    nar "男は俺の方には目線もくれずに本を読んでいる。"
    nar "もっと正確に言うと、本を開いたまま考え事に夢中の様だった。"
    hide screen textbox with dissolve
    show SCG_05 A 0 with dissolve
    pause 1
    show screen textbox with dissolve
    hk_A "……"
    show SCG_05 A 100 with dissolve
    hk_A "イヴリン……"
    hide SCG_05 A 0 with dissolve
    nar "そしてふとそう呟く。{w}どうやら俺の様に、会うべき人に会えなかったお客様らしい。"
    nar "彼は俺の気配を感じ取ったからか、こちらに横目をやってはすぐ頭を背け内側へと消えて行った。"
    nar "そんな絡みたい顔でもないし、そろそろ帰るか。"
    nar "不思議な経験をしてしまった様だ…"
    stop music fadeout 3
    hide screen textbox with dissolve
    jump day5_night
    return

label day_cr_FF:
    if (day == 4):
        show screen place_day4
        show screen place_cr
        with None
        stop music fadeout 3
        hide screen place_cr
        hide screen place_day4
    elif (day == 5):
        show screen place_day5
        show screen place_cr
        with None
        stop music fadeout 3
        hide screen place_cr
        hide screen place_day5
    $ show_quick_menu = True
    with dissolve
    stop music fadeout 3
    scene bg106_1 with dissolve
    call place106
    play music 'audio/bgm/dialogue.ogg' fadein 3
    show screen nvlbox with dissolve 
    "\n 階段には誰も居ない。人気のない所を探していたので俺には良かったが…本当にここは誰も来ないのだろうか？"
    "辺りを見回してから座りこむ。こんな陰気な所でも、一息つける場所があるということは幸運に思えた。"
    et "一人だけの時間を過ごした。"
    stop music fadeout 3
    nvl clear
    hide screen nvlbox with dissolve 
    pause 1
    $ day_cr = True
    $ day_time = day_time +1
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    if (day == 4):
        jump day_time_4
    elif (day == 5):
        jump day_time_5
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
