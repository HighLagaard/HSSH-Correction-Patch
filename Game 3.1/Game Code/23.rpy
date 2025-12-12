

label day3_my:
    show screen place_day3
    show screen place_my
    with None
    hide screen place_my
    hide screen place_day3
    with dissolve
    if (day_time == 0):
        jump day3_my_T
    else:
        jump day3_my_F


label day3_my_T:
    stop music fadeout 2
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg05 with dissolve
    else:
        scene bg05_1 with dissolve
    call place05 from _call_place05_4
    play music 'audio/bgm/maya.ogg' fadein 3
    show screen textbox with dissolve 
    nar "\n{nw}"
    nar "それはそうだとして、会ってからたった一日だけの人をわざと探し回っていたってことは\n、俺の気持ちを考えてくれたってことか。"
    nar "理由はともかく、そういう好意を無視してはいけない。"
    nar "そしてこれとは別個に、いつまでも暗鬱に溺れていることで損するのは俺だけだ。"
    nar "しっかりして、状況をまとめてみようか。{w}俺は目をつぶったまま両頬を軽く叩いた。"
    nar "さてと…今日分の業務は終わって、倉庫の整理はアイツに任せて来た。"
    nar "ということでシーキュレットは、今日の一日倉庫に閉じこもって埃ばっかり吸っているだろう。"
    nar "つまり、今日はもうヤツと面合わせにならなくても良いってことだ。{w}なら気を悪くすることもないだろう。"
    nar "気晴らしといえば、爽快な外の空気は必須だ。{w}じっと座ったまま倉庫の埃と寮のカビの匂いを吸い込むのはゴメンだ。"
    nar "ひょっとしたら俺と同病の人と遭遇してしまうかもしれないし。"
    nar "神殿には、まだ仕事が終わっていない司祭たちが忙しく巡っていた。"
    nar "彼らの通行の邪魔にならないよう俺も人波に混ざって歩き出す。"
    nar "そうしていると脚は勝手に慣れた道へと踏み込んでいて、俺はいつの間にか花壇に向かっていた。"
    nar "水をしっとりと含んだ花々の涼しげな香りが漂う。ここは神殿じゃ数少ない新鮮な空気が味わえる場所だ。"
    nar "それにも関わらず神殿の人々は花や植物なんかに興味を持つ余裕がないほど忙しいのか、あんまりここを訪れる事は無い。"
    nar "そのお陰でここで頭を冷やしている時は、窮屈な神殿から抜け出せた気分になれる。"
    nar "首を垂れた薔薇をちょんと突くと、いくつも重なって塊になった花弁から雨水が零れ落ちる。"
    nar "朝から気勢よく降ってきた雨は梅雨だったか、今は止んでいるが、まだ天気は鬱陶しい。"
    if hssh_rkn == True:
        nar "雨雲に隠された日もすぐ現れてもう夏の天気だ。{w}こんなに日差しの強い日々が続ければ花も枯れてしまうだろう。"
    else:
        nar "もしやこの陰気な天気は雨雲じゃなく、極夜のせいではないのか。"
        nar "こんなに暗い日々が続ければマヤの大事な花も枯れてしまうだろう。"
    nar "そんなことを思いながら遠くを眺めると、花壇の全景が見えてくる。"
    nar "見慣れた木、{w}見慣れた花。{w}そして見慣れていない髪…クレアだった。{w}そしてその隣の見慣れた髪は…"
    stop music
    hide screen textbox
    show bgw
    play sound "audio/SE/ding.ogg"
    pause 0.1
    show screen textbox
    hide bgw
    with dissolve
    pl "マヤ！"
    nar "つい大声を出してしまう。"
    nar "その声を聴いて、二人の女の子が遠巻きからこちらに視線を向ける。"
    cr "そこで何をしておられるんですか、[na]さ～まぁ～～！" with sshake
    pl "それは俺のセリフ、嬢ちゃんはもうおうちに帰る時間だろ！" with sshake
    nar "そちらに向かって声を上げたが、応える声はなかった。"
    nar "どうやら何かの話を交わしているようだが…{w}こんなに遠いままでは聞こえるわけがない。"
    nar "中途半端な様子で対話の終わりを待っていれば、"
    nar "遠く離れていてもっと小さく見える嬢さんが、こちらに来てと伝えたいように手振りをした。"
    hide screen textbox with dissolve
    pause 2
    play music 'audio/bgm/maya.ogg' fadein 3
    show screen textbox with dissolve
    nar "近づけば二人は向かい合うまま白い椅子に座っていた。"
    call day3_meet from my
    pl "あっ…待ってくれマヤ！俺も一緒に帰る！"
    my "……勝手にしたら…"
    hide SCG_02 with dissolve
    nar "まだ俺たち二人が座っているのに、マヤはそんなことは気にせず歩き出す。{w}小さな背中が段々遠くなる度に心が焦っていく。"
    show SCG_04 0 at center with dissolve
    cr "まあ、それでは今日はここで解散ですわね。"
    pl "うん、そうなるな。{w}今日楽しかったぜ、また会おう。"
    show SCG_04 1 with fastdissolve
    cr "こちらこそ、楽しい時間を過ごせましたわ。{w}ありがとうございました、またよろしくお願いいたします。"
    nar "挨拶したことまではよかったが、クレアを除けて一人で行ってしまうことが気にかかる。"
    nar "早く追いつかないとマヤを逃してしまうだろうが…"
    nar "そんな忙しさに気付いたか、クレアは相変わらずにこにこしながら、ずっと足の届かなかった椅子から降りた。"
    show SCG_04 0 with fastdissolve
    cr "わたくし、正門の方に向かいますの。皆様とは反対側になりますね。"
    pl "そっか、確かに俺よりお前の方が神殿の道には詳しいだろうな…"
    show SCG_04 8 with fastdissolve
    show SCG_04 at bounce
    cr "そうですわ！それもこれも余計なお世話ですって～"
    pl "お節介でどうも失礼しました～"
    nar "心配とは逆に、クレアは今の状況を妙に楽しんでいるように見える。多分噂好きの性格と関係があるんだろう。"
    nar "変な誤解はしていなければ良いのにな…"
    show SCG_04 1 with fastdissolve
    cr "では、頑張って！"
    hide SCG_04 with dissolve
    hide screen textbox with dissolve
    pause 1
    if hssh_rkn == True:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03_14
    pause 1 
    show screen textbox with dissolve 
    nvl clear
    nar "最後の声を後にして、俺はとにかく走り出した。{w}が、脚に込めた力がむなしく、マヤにすぐ追いつけた。"
    nar "彼女はそんなに驚いてもいない顔で俺を見つめた。{w}いつもよりももっと遅い歩みだったが、足を止めたりはしない。"
    nar "俺は彼女の隣に付いて足を合わせた。"
    show SCG_02 8 with dissolve
    my "…[na2]くんって、性格いいよね。"
    nar "俺が先に何かを言い出す前に、マヤが視線を下に向けたまま話しかけた。"
    nar "彼女から先に言葉をかけてくれるとは思ってもいなかったが、走ってきた甲斐があった。"
    my "相手が誰だってすぐ仲良くなれるんだね、うらやましいな…"
    pl "そう言われると嬉しいな、でも今日は相手が良かったのもあったんだぜ。{w}クレアだったろ。"
    my "へぇ…"
    pl "ただのお嬢さんかと思ったのに、あんなにお喋りさんとは知らなかったんだよ。趣味も合うから楽しかったし…"
    pl "ははっ、さっきマヤが居なかったときあいつ、何言ったと思う？"
    show SCG_02 0 with fastdissolve
    my "…何て言ったの？"
    pl "それがさぁ……{w}うぅん、や、やっぱ何でもない。よくよく考えたらマヤに言うのはちょっとな…"
    pl "や、妙な事言ったわけじゃないんだけど、後で話すからさ。{w}一緒に後でクレアが言ってた映画でも一緒に観に行こうか？"
    show SCG_02 7 with fastdissolve
    my "一緒に…？でもわたし映画あんまり詳しくないのに…"
    pl "俺たちが詳しいから大丈夫だって！"
    pl "きっとマヤも気に入ってくれると思うぜ、でも間っ違いなくシーキュレットの野郎がとやかく言うんだろうな～"
    pl "アイツも連れてった方がいいんかね…{w}ははっ、自分で言っといてやっぱちょっとアレだな！"
    show SCG_02 8 with fastdissolve
    my "……"
    hide SCG_02 with dissolve
    nar "たわけた冗談を浮かべて一人で笑っていると、マヤは突然足を止めた。"
    nar "あまりにも不意だったので、俺はそれをもう三歩は歩いてから分かった。"
    nar "彼女は言葉が少なく、表現が苦手だが人の話を無視する人間では決してなかった。{w}つまり彼女には何らかの不満があるってことだ。"
    nar "俺は慎ましい足取りで彼女の隣に寄る。{w}その横顔は今まで見たことのない表情だった。"
    nar "やがて陰のできた瞳が回り、冷ややかな視線が俺に刺さる。"
    stop music fadeout 3
    show SCG_02 2 with fastdissolve
    my "…[na2]くんってセンスないのね。"
    hide SCG_02 with dissolve
    nar "マヤの声は明らかだったが、その意味がはっきりしない。"
    nar "一言を伝えた彼女は、さっきより速い歩みで歩き出した。"
    nar "彼女の小さな背中は俺から段々と遠くなっていたが、今度はその後ろが追いつけなかった。"
    nar "道の上に一人になった俺はそのまま立ち止まり、彼女が無事に寮に入ることを呆然と見守っていた。"
    nar "俺は今彼女の気を悪くしたのか？"
    nar "何度も考えてみたが、考えれば考えるほどクレアの最後の張り上げが耳に留まって腹が立ってきた。"
    hide screen textbox with dissolve
    stop music fadeout 3
    pause 2
    $ love_my = love_my + 1
    $ day_my = True
    $ day_time = day_time +1
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_3
    return


label day3_meet:

    $ meet_crea = 1
    nar "普段は花壇がよく見えるベンチだけに座って知らなかったが、"
    nar "薔薇の庭の後ろに、小さなテーブルを挟んだ二つの椅子が置いてある。"
    nar "多分野外テラス…と呼ばれるところらしいが、蔓の生い茂っている庭と同じく長い時間放置されてきたようだ。"
    nar "然したる茶菓や茶もなく、雨に降られた跡で水垢が付いた慎ましいテーブルだが、"
    nar "本物の嬢さんが座っているとそれなりの品のある物に見える。"
    hide screen textbox with dissolve
    pause 1.0
    show SCG_04 5 at left
    show SCG_02 0 at right
    with dissolve
    nar "{nw}"
    pause 1.0
    show screen textbox with dissolve
    show SCG_04 0
    show SCG_02 6
    with fastdissolve
    show SCG_04 at bounce
    cr "まさかまさか、あんなところから飛び出すだなんて吃驚仰天ですわ！"
    cr "こんな時間にどうして此処へ？今って、確かお仕事の時間では…"
    pl "今はお昼の時間だし、俺ら研修生の退勤時間でもあるな。"
    show SCG_02 0 with fastdissolve
    my "もうそんな時間なんだ…"
    show SCG_04 5 with fastdissolve
    cr "まあ！本当ですか？やだわ、時間も忘れてしまうぐらい楽しいお喋りでしたのね！"
    show SCG_04 3 with fastdissolve
    cr "まだマヤお姉さまとお別れしたくないのに～"
    nar "今お姉さまって呼んだのか…{w}そういえば、今朝見た時も結構親しく見えたな。"
    pl "二人って、元々知り合いだったりするのか？"
    show SCG_02 6 with fastdissolve
    show SCG_02 at bounce
    my "そ、そんなあ…！{w}わたしなんかが…面識があるわけは…"
    nar "びくっと驚いたマヤの体が縮こまっていく。{w}いつもの気後れのようでもあって、クレアの気色を探っているようでもあった。"
    show SCG_04 1 with fastdissolve
    cr "マヤお姉さまとは今日お初にお目に掛かりましたの。{w}むむ、正確には今朝、ですね。"
    cr "浄化部の通常出勤時間よりはもう少し早めでしたわ。補給品の整理を前以てやってて…"
    pl "そんな早朝に？マヤは物凄い早起きなんだな…"
    show SCG_02 at huruhuru
    my "た…ただのクセだよ…うち、元々その時間辺りに起きてたから…"
    pl "ははっ、うちの故郷でも大体そんぐらい早起きしてたのになあ～"
    show SCG_04 5 with fastdissolve
    cr "では今日は珍しく寝坊を…"
    pl "いんや！俺は元々そういう規律をあんま守ってなかったから。"
    show SCG_04 0 with fastdissolve
    cr "家で定められた規律を守らないとは…{w}貴方、自由奔放にも程がありますわね！"
    pl "いや～怒られちまったな。{w}働き者のお嬢ちゃんは元からこんな朝早く訪問してるのか？"
    pl "しかもお前はお客さんだから寮からじゃなくて外部から来てるんだろ？一体何時に起きてるんだか。"
    show SCG_04 0 with fastdissolve
    cr "そうなのですが、今日は普段よりは早めに来たのです。"
    pl "ん？それは何でだ？"
    hide SCG_02
    show SCG_04 4 at center
    with dissolve
    show SCG_04 at bounce
    cr "それは当然、貴方に御会いするためですわ！{w}外部の御方！"
    pl "お…俺に？"
    show SCG_04 at bounce
    cr "勿論！冷寒の北大陸に位しながらも、東大陸の異国的な暑さを備え持ったと言われる州都外の島の国！"
    cr "知らされる情報は希薄でございますが、数多の団体や学者たちが訪問することで定期的にその歴史を確認してきたとされる…"
    cr "それこそ夢と浪漫、可能性に満ち溢れた国！かの地域からいらした御方と聞かされたからには確認せずにはいられません！"
    nar "うーわ、島から来たわけではないんだけどな…{w}一体どこからそんな噂が広がっていたんだ。"
    nar "ここで一言物申したかったが、彼女の目は今朝のように眩しく光っていて何も言えなかった。"
    nar "そんな強圧的な行動って本当に単なる好奇心ってことか…"
    show SCG_04 3 with fastdissolve
    cr "…それで、今朝は無礼を働いてしまいました\nわ。{w}改めて、大変申し訳ございませんでした。"
    pl "いや…そのことはもういいって。{w}俺も大声出して驚かせちゃってごめんな。"
    nar "言わなくてもずっと気にかかっていたが、短くても謝られてよかった。"
    show SCG_04 1 with fastdissolve
    nar "返答を聞いたクレアはにこっと笑った。沈鬱だったり明朗だったり、忙しい嬢さんだ。"
    cr "とにかく、[na]様が大胆な御遅刻をしておられなければあの時一緒に挨拶が出来てましたのに！"
    pl "ふぅん…だから俺と一緒に入った新入員のマヤに興味が移ったのか。"
    show SCG_04 5 with fastdissolve
    cr "それだけではありません！しかし同時に簡単で明確な理由ではあります。"
    show SCG_04 1 with fastdissolve
    show SCG_04 at bounce
    cr "そこの人々の中ではマヤお姉さまが一番可愛かったからですわ！"
    show SCG_04 at left
    show SCG_02 0 at right
    with dissolve
    my "ぇ…"
    pl "なるほど！それなら納得だ！"
    show SCG_02 6 with fastdissolve
    my "か、からかわないでよ二人とも…"
    show SCG_04 0 with fastdissolve
    cr "からかうだなんて滅相もない！一目見て思いましたもの。"
    cr "柔いカールの桃色の髪、頭部並みに丸いラインのある腹部…州都で流行っていたスタイルのフリルスカート…"
    show SCG_04 1 with fastdissolve
    show SCG_04 at bounce
    cr "その全てを着こなす平均年齢より小さめの体格！下がり気味のおめめもか弱い小動物の様で愛らしいですわ！"
    pl "一目でわかっちゃうなんてすげぇ観察眼だな。"
    nar "マヤはクレアの一言ごとに顔が赤く染まっては…{w}頭を垂れてしまう。"
    pl "でもお前がどんなにおだてたってマヤの隣は俺のだもんな～"
    cr "そんなぁ！マヤお姉さま、どっちがスキですか？！"
    show SCG_02 at huruhuru
    my "…もうやめなよお…"
    show SCG_04 0 with fastdissolve
    cr "駄目ですよ！これは重大な案件ですから！{w}マヤお姉さま、そろそろ退勤のお時間でしたよね？"
    cr "わたくしと一緒に映画でも観にいきましょうよ！ね！"
    show SCG_02 0 with fastdissolve
    show SCG_04 3 with fastdissolve
    cr "その名も「奇妙な屋根裏部屋」…"
    show SCG_04 1 with fastdissolve
    cr "小さい頃から共に育った家族間の禁じられし恋を描いた感動ロマンススリラー映画なんですの！"
    cr "しかも監督はあの、州都のキネマを繁盛させた大作を何本も創り上げた映画界の巨匠！マヤお姉さまも勿論知っておられますよね？"
    my "うぅん…"
    pl "ああ！俺それ知ってるかも。もう上映始まってたんだ。"
    show SCG_04 5 with fastdissolve
    nar "考える前に言葉が先に出た。"
    nar "大都市である州都は大陸の中心と言えるほど様々な媒体を生み出し、俺は当然それに見惚れるしかできなかった。"
    nar "州都との直接的な交流がほとんどなかった故郷から州都の情報を聞くのは大変だったが、そうだとはいえ正に不可能でもなかった。"
    nar "州都から来た巡察隊員や、学者から情報を抜き出したってことだ。"
    nar "そうやって俺は、彼たちが持ってきたいろんなガラクタを漁って、州都の夢を見ながら育ってきた。"
    show SCG_04 at center
    hide SCG_02
    with dissolve
    cr "まあ…[na]様、この監督の映画をご覧になったことがありまして？"
    pl "やっぱキネマってかラジオすら無い隅っこの田舎暮らしだったから、知ってるだけで一度も直接観たことはないけど…"
    pl "あらすじは大概知ってるぜ。カタログとかも全部集めたし。{w}あれだろ、夫が出張で家を出ていた間新しい恋人が出来てしまった…"
    show SCG_04 1 with fastdissolve
    show SCG_04 at bounce
    cr "『雁の季節』ですよね！あれは傑作でしたわ！"
    cr "審議上の問題で上映がちょっとだけ先延ばしになってしまったけど、蓋を開けたら想像以上のどんでん返しで…！"
    pl "そうそう、実は不倫の相手にとってその妻はただの友達でしかなかったんだよ！"
    pl "誤解がそんな悲劇を生むなんて…上映延期が虚しいくらいすぐに上映終了しちまったけど。"
    show SCG_04 0 with fastdissolve
    cr "ホントですわ！{w}同じ時期上映開始した作品の方に視線が集中してしまいましたものね…"
    cr "もし、その作品についても聞いたことは…？"
    pl "あるよ、あらすじもな。{w}でも俺が考えるには正直あれって…"
    show SCG_04 4 with fastdissolve
    show SCG_04 at bounce
    cr "最悪でしたよね！"
    pl "そうそう！そうなんだよ！お前ちょっとはイイ目してんじゃないか！"
    cr "あんな刺激だけが売りみたいな映画に圧されるような作品じゃなかったはずなのに、時代は天才を分かってくれないのですわ！"
    nar "ぱっと、クレアと掌を合わせた。{w}彼女の手は俺のより小さくて、思ったより軽快な音はしなかった。"
    show SCG_04 1 with fastdissolve
    cr "まさか、この手の話が通じる御方に出会えるなんて！[na]様もほら、立ってないでどうぞどうぞお座りくださいまし！"
    pl "え～それ今言う？{w}てか、座れったって椅子二つしかないし。"
    cr "では…わたくしがマヤお姉さまの膝に座るのはどうでしょう！一石二鳥という言葉は正にこういう場面で使うものです！"
    pl "そして本音がダダ漏れって言葉もまさしくこういう場面で使うもんだな。。{w}マヤが困るだろうが！"
    show SCG_02 8 at right
    show SCG_04 5 at left
    with dissolve
    my "わたし…退こうか？"
    pl "マヤが居てくれなきゃ俺がここまで来た理由もないんだって～"
    show SCG_04 at bounce
    cr "そうそう！わたくしがこの御方とたった二人で居る理由もないんですって！"
    my "……"
    pl "マヤは好きな映画とかあるか？"
    show SCG_02 at huruhuru
    my "あ…う～ん…{w}ごめんね、あんまりわからないの…映画とか観れる機会がなかったから…"
    show SCG_04 0 with fastdissolve
    cr "そうですか…確かに、州都の外側にはキネマはあまりないのかもですね…"
    cr "やはり我々の様な最近の若者の普遍的趣味といえば、音楽ですわね！"
    show SCG_02 0 with fastdissolve
    my "それなら興味…ちょっとだけあるかも…"
    show SCG_04 1 with fastdissolve
    cr "そして今州都を代表する歌手は誰が何と言えどMs.ギャラクティカ！"
    cr "ご自身が直接書き下ろした大胆で繊細な歌詞は若い層の心を鷲掴みにしましたわね！ミュージカルの俳優としても有名ですし！"
    show SCG_02 7 with fastdissolve
    my "ぅうん…"
    pl "ミュージカルって、サンドイッチに蛇が挟まったあれか？"
    cr "やはり、[na]様ならわかってらっしゃるだろうと信じておりましたわ！しかもそれはランチのメニューでしたものね。"
    pl "朝食の方ならまだしもな！"
    show SCG_02 0 with fastdissolve
    my "…どっちも同じじゃない？"
    show SCG_04 5 with fastdissolve
    nar "……"
    pl "ミュージカルもまあ普遍的な趣味ではないな。"
    pl "でもマヤも知ったらきっと好きになれると思うぜ！それがどういう事かっていうと…"
    show SCG_04 1 with fastdissolve
    cr "作品内の女主人公は元々ハム入りサンドイッチが好きなんですけど…{w}ああ！じれったい！"
    cr "口頭で説明したら何だか面白くなくなってくる気がしてしまいますわ。"
    cr "これはやはり直接観に行くべきですよ！次お時間ある時にでも一緒に観に行きましょ、お姉さま！"
    show SCG_02 8 with fastdissolve
    my "ミュージカルについて詳しいわけじゃないけど、二度上映してくれそうにはみえない気がするな…"
    my "おふたり楽しそうだったのに割り込んでごめんね。"
    show SCG_04 6 with fastdissolve
    cr "そ、そんな謝らなくても～{w}マヤお姉さまが好きそうなもの…何かありそうですかね？ふむむ…"
    hide screen textbox with dissolve
    pause 2
    show SCG_02 0 with dissolve
    pause 4
    show SCG_02 8 with dissolve
    pause 2
    show screen textbox with dissolve
    nar "……"
    nar "突然と対話が断たれてしまった。{w}クレアは新しい話題を考えているが、うまく思い浮かばないようだ。"
    nar "マヤの好きなものって花とか動物ぐらいで思い当たることは他にないし、肝心なところ、本人が黙っている状況で…"
    nar "一刻も早くこの静けさを破る為に何をすれば良いんだろう？"
    pl "…そうだ、俺が面白いもん見せてやるよ。"
    show SCG_02 0
    show SCG_04 5
    with fastdissolve
    my "面白いもの…？"
    pl "簡単な読心術みたいなもんさ、どっちがやってみたい？"
    show SCG_04 1 with fastdissolve
    show SCG_04 at bounce
    cr "はいはい！わたくし！わたくしにやらしてくださいまし！"
    pl "じゃあ紙とペンあったらくれるか？"
    show SCG_02 7 with fastdissolve
    my "[na2]くん、今そんなのあるわけ…"
    show SCG_04 0 with fastdissolve
    cr "メモ帳でも良ければ。"
    show SCG_02 8 with fastdissolve
    my "……"
    pl "じゃあ…{w}クレア、今から三つお前に質問するから、口に出さず頭で答えを考えといて俺が紙に書いたら正解を言ってくれ。"
    show SCG_04 2 with fastdissolve
    cr "ふぅむ…わたくしの目は鋭いですわよ、[na]様。{w}もし最後一気に書くとかでしたら許しませんからね！"
    pl "どうせ隣のマヤがちゃんと見張ってくれるから心配しなくてもいいんだって、"
    pl "じゃあまずは…お前の生まれた月を数字暦で頭に浮かべるんだ。"
    cr "こうやってどさくさに紛れて少女の情報を洗いざらいにしようと…"
    pl "映画の趣味はいいと思うけど、ちょっと控えた方がいいんじゃないの～？"
    show SCG_04 8 with fastdissolve
    show SCG_04 at bounce
    cr "わたくしが映画の趣味を控えて悲しむのは[na]様ですわよ！"
    pl "良くして頂いて大変光栄に存じます～"
    show SCG_04 3 with fastdissolve
    nar "隣で紙を見ていたマヤがいぶかしい顔をした。"
    nar "確かにすぐ傍で見ている場合なら子供騙しのようなものだが、うまく騙されてくれれば良いのにな…"
    pl "よし、じゃあ答えをどうぞ。"
    show SCG_04 5 with fastdissolve
    cr "うーん…8月ですわ。"
    pl "俺と同じじゃねえか！"
    show SCG_04 0 with fastdissolve
    cr "夏生まれは悲しいですよね、特に州都は常に空気が冷たいので…{w}わたくしも本当の暑さというものを体験してみたいです！"
    pl "州都の人にホンモノの暑さは厳しいぞ、良家で大事に育ったお嬢ちゃんが耐えられるか？{w}マヤは何月生まれ？"
    show SCG_02 0 with fastdissolve
    my "わたし…？わたしは、牧童の月だから…数字暦で5月かな…"
    show SCG_04 1 with fastdissolve
    cr "春ですか、いいですね～華やかで暖かい感じが丁度マヤお姉さまそっくりのイメージです！"
    pl "牧童の月って春だっけ？"
    show SCG_04 5 with fastdissolve
    cr "夏ではございませんよね？"
    show SCG_02 7 with fastdissolve
    my "…次の質問は？"
    pl "次は当然、生まれた日だな。"
    show SCG_02 0
    show SCG_04 1
    with fastdissolve
    cr "5秒差し上げますわ！"
    pl "急かすなって～"
    cr "3…2…1！{w}わたくしは9日生まれですの。"
    pl "俺は10日！だな。{w}ちょっとだけ遅生まれだったら同じだったろうに！惜しいな。"
    show SCG_04 7 with fastdissolve
    cr "それはわたくしのせいではありませんわ！わたくしの両親の仲がさぞ…"
    show SCG_02 5 with fastdissolve
    show SCG_02 at bounce
    my "つ、つぎで最後だね！"
    pl "最後は…何が良いだろうな。猫と犬だったらどっちが好き？"
    show SCG_04 5 with fastdissolve
    cr "最後は最後らしく難易度がちょっとばかり上がりましたわね。ふーむむ…"
    pl "ちなみにマヤは？"
    show SCG_02 0 with fastdissolve
    my "わたしはどっちも…好きかな。"
    show SCG_04 1 with fastdissolve
    cr "わたくしもマヤお姉さまが大好きですわ～"
    show SCG_02 6 with fastdissolve
    my "……"
    pl "俺もだよ！{w}でも答えはちゃんと例の中から考えときなよ！"
    cr "少し悩みましたが、決めました！"
    pl "じゃあクレアの答えと同時に俺も書いたやつを見せるぜ。"
    show SCG_04 8 with fastdissolve
    cr "ふっふーん、かなり自信がおありで…{w}わたくしは猫の方が好きですわ！"
    hide SCG_04
    hide SCG_02
    with dissolve
    nar "俺は予め取っておいた紙三枚を差し出した。{w}八月、九日、猫…これで全部正解だ。"
    nar "幸いクレアは子猫みたいに目を見張って驚いてくれたが、マヤと俺は目を見交わしてぎこちない表情をしていた。"
    nar "実は…{w}メモの順番を変えただけだ。{w}こんなとんでもない手品を赤裸々に見つめていたからそんな顔も無理もないな。"
    nar "魔術って所詮こういうものなんだが、妙に恥を感じてしまう。"
    show SCG_04 5 with dissolve
    show SCG_04 at bounce
    cr "{cps=*0.1}すすす、す{/cps}{nw}"
    extend "ごいですわ！どんな秘密が隠されているのでしょう？！" with sshake
    pl "ん～それ、言っちまったらもうマジックじゃなくなるだろ。{w}お前は賢いんだしすぐにわかるさ。"
    show SCG_04 4 with fastdissolve
    cr "とっても気になります！普段もこのような技術の練習を沢山してらっしゃるのですね。"
    pl "まあ…故郷じゃやる事もなかったし、"
    pl "じっとしてるだけでも何だったから昔の雑誌や大人のやり方を見て見よう見真似でやってただけだよ。"
    pl "俺、こう見えて手際が良いんでね。{w}縄とかの道具がもっとあったらもっとすごいモンだって見せられるんだぜ。"
    show SCG_04 1 with fastdissolve
    cr "ではわたくしもマジックをいくつか覚えてきますわ。{w}マヤお姉さまも絶対見に来てくださいね！"
    show SCG_04 1 at left
    show SCG_02 0 at right
    with dissolve
    my "うん…たのしみにしてるね。{w}二人って本当話が合うんだね…"
    show SCG_04 0 with fastdissolve
    cr "趣味が似ているからでしょうか？わたくしも吃驚しましたわ、ここまで話が合う人ってあまり会えませんもの！"
    pl "共通点も多いしな、俺も猫派なんだよ。"
    cr "あぁ、なんだかイメージ的にわかる気が…"
    pl "それは俺のセリフ！{w}俺の里には猫とか鳥が沢山いてさ、小さい頃から猫と一緒に暮らしてたんだよ。"
    pl "それとは別としてあんま懐いてはくれなかったけど…"
    show SCG_04 8 with fastdissolve
    cr "それって多分、猫は縄張り意識の高い動物だからではないでしょうか！"
    pl "奪おうとしたことないって！"
    nar "じっと話を聞いていたマヤはテーブルの下で手をいじいじとしていて、まもなく席から立ってしまった。"
    show SCG_02 8 with fastdissolve
    my "わたし、先に帰るね…"
    show SCG_04 5 with fastdissolve
    cr "あれ…先に行かれるのですか？"
    my "うん…ちょっと疲れちゃって…{w}クレアちゃんも、あまり遅くならないように帰ってね。"
    return


label day3_my_F:
    stop music fadeout 2
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg05 with dissolve
    else:
        scene bg05_1 with dissolve
    call place05 from _call_place05_5
    play music 'audio/bgm/maya.ogg' fadein 3
    show screen nvlbox with dissolve 
    "\n 花壇には誰もいない。マヤはいつもここで花に水をあげに来るのに、今日はもう立ち寄って帰ったのか。"
    "もしかしたらと思ってマヤのお気に入りの花に近づくと、やはり水を撒いた跡が残っている。{w}それだけでマヤの姿を思い出して心が温かくなる。"
    "残念だが、マヤはまた後から伺った方が良さそうだ…"
    stop music fadeout 3
    nvl clear
    hide screen nvlbox with dissolve 
    pause 1
    $ day_my = True
    $ day_time = day_time +1
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_3
    return


label day3_cr:
    show screen place_day3
    show screen place_cr
    with None
    hide screen place_cr
    hide screen place_day3
    with dissolve
    if (day_time == 0):
        jump day3_cr_T
    else:
        jump day3_cr_F


label day3_cr_T:

    stop music fadeout 2
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03_15
    play music 'audio/bgm/daily.ogg' fadein 3
    show screen textbox with dissolve 
    nar "\n{nw}"
    nar "それはそうだとして、会ってからたった一日だけの人をわざと探し回っていたってことは\n、俺の気持ちを考えてくれたってことか。"
    nar "理由はともかく、そういう好意を無視してはいけない。"
    nar "そしてこれとは別個に、いつまでも暗鬱に溺れていることで損するのは俺だけだ。"
    nar "しっかりして、状況をまとめてみようか。{w}俺は目をつぶったまま両頬を軽く叩いた。"
    nar "さてと…今日分の業務は終わって、倉庫の整理はアイツに任せて来た。"
    nar "ということでシーキュレットは、今日の一日倉庫に閉じこもって埃ばっかり吸っているだろう。"
    nar "つまり、今日はもうヤツと面合わせにならなくても良いってことだ。{w}なら気を悪くすることもないだろう。"
    nar "気晴らしといえば、爽快な外の空気は必須だ。{w}じっと座ったまま倉庫の埃と寮のカビの匂いを吸い込むのはゴメンだ。"
    nar "ひょっとしたら俺と同病の人と遭遇してしまうかもしれないし。"
    nar "神殿には、まだ仕事が終わっていない司祭たちが忙しく巡っていた。"
    nar "暇そうに見えるのはぶらぶらしている俺だけで、ここに馴染み込んでいないままただ浮かんでいるような気分だ。"
    nar "彼たちの行き来に邪魔にならないように奥まったところを探して入ると、後門に続く道で、見たことのない通路を見つけた。"
    nar "まさか勝手に入ったって怒られることはないだろう。{w}「関係者以外立入禁止」って警告文はどこにも…"
    pl "…ってか、俺も関係者じゃね？"
    hide screen textbox with dissolve 
    stop music fadeout 2
    scene black with dissolve
    play sound "audio/se/door slide.ogg"
    pause 3
    if hssh_rkn == True:
        scene bg106 with dissolve
    else:
        scene bg106_1 with dissolve
    call place106 from _call_place106_2
    show screen textbox with dissolve 
    nvl clear
    play music 'audio/bgm/dialogue.ogg' fadein 3
    nar "入ってみると、そこには暗澹たる階段があった。{w}どうやら非常階段らしい。"
    nar "神殿に来てもう三日も過ぎたがこんなところがあったってことは知らなかった。"
    nar "司祭たちは皆正門から真っすぐに続いた中央階段だけを通うから、それもそうか。"
    nar "内側は人跡もなく穏やかだ。"
    nar "四方が塞がれて外の音もよく聞こえなくなり、息を入れる間もなく進む神殿のことから脱した錯覚まで感じられる。"
    nar "寮に帰りたくない時に来て静かに考えをまとめる為には丁度良いな。"
    nar "階段を上る途中、平たい踊場の窓枠に寄りかける。"
    nar "朝から気勢よく降ってきた雨は梅雨だったか、今は止んでいるが、まだ天気は鬱陶しい。"
    if hssh_rkn == True:
        nar "雨雲に隠された日もすぐ現れてもう夏の天気だ。{w}こんなに日差しの強い日々が続ければ花も枯れてしまうだろう。"
    else:
        nar "もしやこの陰気な天気は雨雲じゃなく、極夜のせいではないのか。"
        nar "こんなに暗い日々が続ければマヤの大事な花も枯れてしまうだろう。"
    nar "そんなことを思いながら下を眺めてみると、花壇の風景が見える。{w}花壇は確かに後門に続いているからな。"
    nar "見慣れた木、{w}見慣れた花。{w}そして見慣れた髪…マヤだった。{w}そしてその隣の見慣れない髪は…"
    stop music
    hide screen textbox
    show bgw
    play sound "audio/SE/ding.ogg"
    pause 0.1
    show screen textbox
    hide bgw
    with dissolve
    pl "クレア！"
    nar "つい大声を出してしまう。"
    nar "その声を聴いて、二人の女の子が上を見上げる。"
    cr "そこで何をしておられるんですか、[na]さ～まぁ～～！" with sshake
    pl "それは俺のセリフ、嬢ちゃんはもうおうちに帰る時間だろ！" with sshake
    nar "窓枠にぎりぎり寄りかかって声を上げたが、返信は返ってこない。"
    nar "どうやら何かの話を交わしているようだが…{w}こんなに遠いままでは聞こえるわけがない。"
    nar "中途半端な様子で対話の終わりを待っていれば、"
    nar "遠く離れていてもっと小さく見える嬢さんが、こちらに来てと伝えたいように手振りをした。"
    hide screen textbox with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg05 with dissolve
    else:
        scene bg05_1 with dissolve
    call place05 from _call_place05_6
    play music 'audio/bgm/Clair.ogg' fadein 3
    show screen textbox with dissolve
    nar "下がってみると、二人は向かい合うまま白い椅子に座っていた。"
    call day3_meet from cr

    pl "あぁ…気を付けて帰りなよ、マヤ。後で寮でな。"
    hide SCG_02 0
    hide SCG_04 0
    with dissolve
    nar "俺が急いで挨拶すると、マヤは何の返答もなく花壇を後にした。"
    nar "俺に代わりに座れと言うように、座っていた椅子は戻されないままだ。"
    nar "マヤが去ってしまうと、まるで嘘のように俺たち二人の対話も断たれてしまった。"
    nar "さっきまでは次から次へと話題が溢れてきたが、多分慣れたマヤが傍にいてくれたお陰で気楽に話せたようだ。"
    nar "こんなところまで似ているなんて、目の前の小さな嬢さんにやたらに同質感を感じる。"
    show SCG_04 0 with dissolve
    cr "マヤお姉さまとは仲がよろしくて？"
    nar "この気まずい静寂を破ったのはクレアの方からだった。"
    pl "あ…そう見えるか？"
    cr "はい、[na]様がいらっしゃる前にも少しばかり話題に上がってましたの。お二人いつも一緒だとか…"
    pl "マ、マヤが俺の話を？"
    show SCG_04 8 with fastdissolve
    cr "分かりやすく喜ばれるのですね…"
    pl "いや、そういうんじゃなくて…"
    show SCG_04 0 with fastdissolve
    cr "わたくし、お友達がいないので…{w}神殿の皆さんを見ているととても羨ましいのです。"
    nar "突然の言葉だった。"
    nar "今までずっと天真爛漫な姿を見せた彼女がいきなり自分の陰を見せたことに内心で当惑を感じたが、"
    nar "それを外へ表さない為に頭をひねった。"
    nar "こんな時の答えと言えば一つしかないな。"
    pl "…まあ、別にそうは見えなかったんだけどな。{w}俺はクレアとお話が出来て良かったと思うぜ。"
    pl "初めて見た時は州都の金持ちの家のお嬢さんって印象しかなかったけど、いざ喋ってみたら共通点も多いし楽しかったし。"
    pl "やっぱ人って外見だけで判断しちゃダメなんだなって。"
    show SCG_04 5 with fastdissolve
    cr "そうでしょうか…？"
    pl "お前も知っての通り俺は外部の人だからさ、"
    pl "あんまり知ってることも少ないし気楽に喋れる人も居なくって寂しかったとこなんだよ。"
    pl "久々にぶっちゃけた話ができて良かったぜ。"
    show SCG_04 at bounce
    cr "わ、わたくしもですわ！{w}わたくし、外部者ですし、気楽にお喋りなんて出来る人の方が手に数えるぐらいで。"
    cr "神殿の司祭の方々は勿論皆親切にしてくださいますけど、それはお客様としての扱いってだけで…"
    show SCG_04 0 with fastdissolve
    cr "わたくし自身の趣味のお話が出来たのは久々…{w}もしかしたら、初めてかも知れません。"
    cr "今日は貴重なお時間を頂きましてありがとうございます。"
    pl "や、俺の時間はそんな貴重なモンでもないって、それは俺のセリフだよ。{w}今日はありがとう。また会えるかな？"
    show SCG_04 1 with fastdissolve
    cr "はい！わたくしも微小ながらも神殿のお仕事を手伝っている身ですので、必ずまた会えますわ。"
    pl "その時はまた今日みたいに色んな話して遊ぼうぜ。"
    cr "勿論です！いや、むしろお願い致しますわ、次もまた絶対わたくしに付き合ってもらいますものね！"
    hide screen textbox with dissolve
    hide SCG_04 with dissolve
    stop music fadeout 3
    pause 2
    $ love_cr = love_cr + 1
    $ day_cr = True
    $ day_time = day_time +1
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_3


label day3_cr_F:
    stop music fadeout 2
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03_16
    play music 'audio/bgm/dialogue.ogg' fadein 3
    show screen nvlbox with dissolve 
    "\n 神殿には、まだ仕事が終わっていない司祭たちが\n忙しく巡っていた。{w}暇そうに見えるのはぶらぶらしている俺だけで、ここに馴染み込んでいないままただ浮かんでいるような気分だ。"
    "彼たちの行き来に邪魔にならないように奥まったところを探して入ると、後門に続く道で、見たことのない通路を見つけた。"
    "まさか勝手に入ったって怒られることはないだろう。「関係者以外立入禁止」って警告文はどこにも…"
    stop music fadeout 1
    "\n…ってか、俺も関係者じゃね？"
    hide screen nvlbox with dissolve 
    scene black with dissolve
    play sound "audio/se/door slide.ogg"
    pause 3
    if hssh_rkn == True:
        scene bg106 with dissolve
    else:
        scene bg106_1 with dissolve
    call place106 from _call_place106_3
    show screen nvlbox with dissolve 
    nvl clear
    play music 'audio/bgm/map select.ogg' fadein 3
    "\n 入ってみると、そこには暗澹たる階段があった。{w}どうやら非常階段らしい。{w}神殿に来てもう三日も過ぎたがこんなところがあったってことは知らなかった。"
    "司祭たちは皆正門から真っすぐに続いた中央階段だけを通うから、それもそうか。"
    "内側は人跡もなく穏やかだ。{w}四方が塞がれて外の音もよく聞こえなくなり、息を入れる間もなく進む神殿のことから脱した錯覚まで感じられる。{w}寮に帰りたくない時に来て静かに考えをまとめる為には丁度良いな。"
    "埃が付いた風景を見れば、結構長く使われていないようだ。{w}やはり何の理由もなくこんな陰気な所にわざと訪れる人はいないだろう。"
    et "秘密の場所を見つけた気分がしてちょっとワクワクしてきた…"
    hide screen nvlbox with dissolve
    nvl clear
    stop music fadeout 2
    pause 2
    $ day_cr = True
    $ day_time = day_time +1
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_3
    return


label day3_hk:
    show screen place_day3
    show screen place_hk
    with None
    hide screen place_hk
    hide screen place_day3
    with dissolve
    if (day_time >= 2):
        jump day3_hk_T
    else:
        jump day3_hk_F


label day3_hk_T:
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg04 with dissolve
    else:
        scene bg04_1 with dissolve
    call place04 from _call_place04_4
    show screen textbox with dissolve
    play music 'audio/bgm/dialogue.ogg' fadein 3
    nar "忙しく行き来する神殿の人波を中央階段の上で眺めながら、俺は今日のことを再び思い出す。"
    nar "ぼっとしていたらすぐ昨日の夜の出来事が頭に浮かぶ。{w}しかし、今考えるべきことはそれではない。"
    nar "俺が思い出したいのは空白の記憶だ。{w}マヤとクレアを見送り、里で仕事をする前までの空いた記憶。"
    nar "ここにずっと立ってばかりいると、辺りを通って行く人の邪魔になりそうでまずは歩こうとした。"
    nar "外へ、そしてできれば人のいないところへ。"
    nar "寮の方はさすがに混んでいるが、反対側の道に入ると目の前の人影も全部消えてしまった。ここは作業場への道だ。"
    nar "人何人かが横になって歩いても十分であるほど広やかなのに、この時間帯はがらんとしている。{w}昨日もそうだったし。"
    nar "どす黒い空に煙が舞い上がり、肺を苦しめてくる苦い煙に思わず咳が出る。"
    nar "作業場の空気は屋外であり冷ややかだが、あちこちからの煙のせいで決して清いわけではなかった。"
    nar "空気の質といえば今日行った里のもそんなに澄んではいなかった。{w}汚れた空気はさすがに州都そのものの問題なのかもしれない。"
    nar "その煙たい空気の中で俺たちは死体を処理していた。{w}いや、実際処理したのは彼一人だったが。"
    nar "干からびた黄色いスープの跡の焦げ付いた床の狭い部屋の中で、老人の死体は亡者になる寸前だった。"
    nar "処理が早かったおかげか特に危険性はなかった。{w}只黒い手足が動いていただけ。"
    nar "骨と皮ばかりの痩せぎすの手足はまだ主が生命を有していると勘違いしたように動いて、{w}やつはすぐ刀を振り上げた。"
    nar "俺は遠目に立ってその光景を見ていた。"
    nar "思い出してみればやたらに気まずくなってきた。{w}今この焼却炉で燃えている物も、その死体の一部か。"
    nar "近づくと喉が辛くなってきた。{w}焼却炉の中には、もう元の判明できない灰の山だけが残っている。"
    stop music fadeout 3
    hk "焼却炉にあまり近づくと、あぶないですよぉー"
    nar "のんびりした声が集中を散らす。{w}どうやら絡繰りの作動音のせいで足音が聞こえなかったようだ。"
    nar "声の主人は俺の後ろでにっこりと笑っている。"
    nar "人の良い笑顔とは言えるが、今の俺にとっては少しありがた迷惑な人物だ。{w}この人の前に立つと余計に考えが増えてしまうから。"
    hide screen textbox with dissolve
    show SCG_05 1 with dissolve
    pause 1
    show screen textbox with dissolve
    play music 'audio/bgm/golden haku.ogg' 
    hk "たまぁ～に、こうやってうしろから、とんっ♪と押しちゃう人がいるんですよぉ？"
    pl "主教様…うっ、冗談にしては殺伐だ。"
    hk "今回は、相手がわたくしでよかったですねえー"
    pl "それも何かの冗談の一環なのか？悪質だな…{w}冗談じゃ終わらねえぞ、人が死ぬかもだろ？"
    show SCG_05 idle with fastdissolve
    hk "冗談ではございませぬ～神様でさえ、人の命を弄ぶ権利はございませんのでー…"
    hk "こういう行為は、実際に悪意を持った人間の行為です。"
    pl "悪意、と言えば…？"
    show SCG_05 8 with fastdissolve
    hk "心ぐるしいことに、浄化部の司祭は、他の部署の司祭と違い遺家族と直接対面いたしますので～"
    show SCG_05 7 with fastdissolve
    hk "理由なき怨みを買うことが多いのですぅ…"
    nar "それなら俺も心当たりはある。{w}俺は今日、それを骨身に感じた。"
    nar "行き場を失った憎悪と憤怒、悲嘆を吐き出すところを欲する人を相手するのもまた「処理班」の業務だ。"
    nar "理不尽であるが、誰かを恨むことでは決してない。"
    nar "それをじっくりと考えれば、今更気になる人がいた。{w}司祭もそうだが、今目の前のこの人はどうだろう。"
    show SCG_05 idle with fastdissolve
    hk "どおしてわたくしを…そんなじま～じま～と…？"
    pl "いや、主教様ってのは団体の代表ってことだろ？{w}ならこんな部署のハク主教様は普段大丈夫なのかなって…"
    show SCG_05 1 with fastdissolve
    hk "わぁお！わたくしの心配をしてくださるんですかあ？あらあら、とてもおやさしいことに～…"
    hk "司祭の御方が個人的に心配してくださったのは、これが二度目ですぅ～"
    pl "いつ主教になったんだ？"
    show SCG_05 idle with fastdissolve
    hk "うぅ～ん…浄化部は新設ですのでぇ…{w}3年ですねえ。"
    pl "3年もの間で2回程度は問題あるだろ…"
    show SCG_05 8 with fastdissolve
    hk "そおですかぁ…？"
    pl "主教様って見てると何だか不安になる人なのにさ。"
    show SCG_05 1 with fastdissolve
    hk "不安って、もしもし…こ～やってひら～ひら～と動いてるからですかぁ？"
    pl "目を離したら危なそうっていうか、どこかに紐付けしておかないとヤバそうっていうか…"
    play sound "audio/se/hit.ogg"
    show SCG_05 6
    hk "わ…わたくし紐づけされちゃうんですかあ？！" with sshake
    pl "あとこう話の焦点ズラされるとことかよ、くそっ！{w}急に変な話すんなって！"
    show SCG_05 8 with fastdissolve
    hk "こ～みえて会話にはちゃんと集中してるのですぅ…{w}だいたい[na]兄弟は、話が早すぎますぅ～"
    hk "会話のテーマがぐるぐる～変わっちゃって忙しぃのですぅ。"
    pl "主教様が遅いんだって。{w}主教様が一言喋る間、俺みたいな人は普通十言ぐらい喋っちゃうんだって。"
    show SCG_05 6 with fastdissolve
    hk "そんなぁ……"
    pl "じゃなくても聞きたかったことなんだけど、喋るのが遅いのってただのクセ？"
    show SCG_05 9 with fastdissolve
    hk "くせってゆーか…{w}わたくし自身としては遅いという自覚はございませんのですがぁ…"
    hk "わたくし、お相手様のお言葉には必ずちゃんとお返しいたしたいのに…"
    pl "喋るのが遅いってか考えるのが遅いのか？"
    play sound "audio/se/hit.ogg"
    show SCG_05 6
    hk "…い、いまもわたくしの話を途中で切っちゃいましたぁ！{w}こうなっちゃうとお答えができないですぅ！" with sshake
    pl "うわ、ゴメンゴメン！最後なんだか濁してたから終わったのかと…"
    show SCG_05 2 with fastdissolve
    hk "次の言葉を考えておりましたのですぅ…"
    pl "……"
    hk "……"
    show SCG_05 1 with fastdissolve
    hk "あ、今の話は先程で終わりです♪"
    pl "紛らわしいだろうがっ！"
    show SCG_05 6 with fastdissolve
    hk "うぅ、大声出さないでくださいぃ…！"
    pl "でも主教様ってさあ、朝の授業とか礼拝の時はきっちり話せるじゃんか。"
    show SCG_05 8 with fastdissolve
    hk "それは当然事実を伝達させていただいてる\nだけですからあ…"
    hk "教えを与える立場である以上、戸惑いがあってはいけないのですよぉ。"
    show SCG_05 7 with fastdissolve
    hk "そのふたつはまるで別問題なんですぅ。{w}わたくし、自分の意見を言葉として伝えるのがとってもとってもニガテで…"
    pl "神殿で使われる銀色のロザリオとは？"
    show SCG_05 idle with fastdissolve
    hk "{cps=*4}神殿の司祭であることを表すために使われる身分証の様なものです。{/cps}"
    show SCG_05 9 with fastdissolve
    hk "{cps=*4}側面に小さく司祭の名前が記載してあるので、紛失や破損された場合再発行は可能ですが、{/cps}"
    show SCG_05 1 with fastdissolve
    hk "{cps=*4}発行までは最短で一週間が掛かりますねえ。{/cps}"
    pl "明日の昼なんだと思う？"
    show SCG_05 9 with fastdissolve
    hk "うう～～～んとぉ…"
    show SCG_05 4 with fastdissolve
    hk "……ぐらたん？"
    pl "ほぉ、なるほど。意外な弱点発見。"
    play sound "audio/se/hit.ogg"
    show SCG_05 6
    hk "うぅ！オトナのひとをからかってはいけませ～ん…" with sshake
    nar "ふわふわとか、ピカピカとかの曖昧なオノマトペを恥を知らずに乱用するのも表現が苦手だからか。"
    nar "思ったことはすぐ言葉に出してしまう俺としては納得いかないことだ。"
    nar "透きを見つければ見つけるほどこの人への疑いは深まる。{w}だが今度は彼女の正体ではなく、主教たる役目に関しての疑いだった。"
    pl "こ～んな主教様のことを誰も心配してくれないなんて、神殿の司祭たちも冷たいよなぁ。"
    show SCG_05 idle with fastdissolve
    hk "それは多分、わたくし自身それを心配すべき問題と思っていないからでもあるかもですぅ。"
    hk "わたくしは、わたくしへ降り掛かる数多の事柄を「苦痛」と思ったことなどないのですからぁ…"
    pl "後ろで指を指されたり、嫌な事されても？"
    show SCG_05 1 with fastdissolve
    hk "それらすべてを苦痛と受け取ってはいけません。"
    hk "負の感情は同じく負を呼び起こすだけーすべては神の摂理によって巡っておりー"
    hk "浄化部は州都と神殿の循環を手伝うため存在するものでありー"
    show SCG_05 idle with fastdissolve
    hk "その怨みがすべてわたくしへ回されるのだとしたらそれは浄化部がその役割を果たしてるという素晴らしい証拠なのでございますー"
    pl "はぁ…そんなのが本当に国のためになるのか？"
    show SCG_05 1 with fastdissolve
    hk "勿論でございますぅ、浄化部は人間のための部署ですのでぇ。"
    hk "それにこの役割はわたくしの父親から授かった使命、苦痛を感じる訳などございませんのですぅ～"
    pl "主教様がいいってんなら良いんだろうけど、俺を含めた他の司祭たちが受け入れられるかどうか…"
    show SCG_05 idle with fastdissolve
    hk "しかし、わたくし同様、司祭のみなさまもまた、その役割を上手く遂行して頂いているがため浄化部が存続されているのでしょう…"
    show SCG_05 1 with fastdissolve
    hk "ああ、どれほどありがたいことか…♪"
    nar "また心が重くなってきた。{w}この人ってまさか、自分の部署の部下たちがどんな生活を営んでいるのか分かってないのではないか。"
    nar "あいつは神経質な口振りで「主教様に告げたって」って言っていたが、俺はそう思わない。"
    nar "彼女も主教たる者なら知らざるを得ない。"
    pl "主教様、浄化部の司祭たちって仲悪いの知ってるか？"
    show SCG_05 idle with fastdissolve
    hk "はいぃ？"
    pl "今日の昼もさぁ、仕事中偶然喧嘩沙汰になっちゃってるのを見ちまって。"
    pl "一人顔が血塗れになるぐらい殴り合って大変だったんだぜ？"
    pl "それだけじゃない、寄ってたかって一人を虐めたり、悪意しかない噂が流れたり…"
    show SCG_05 7 with fastdissolve
    hk "それは…"
    pl "勿論、俺が偶然不良な奴らに出くわしただけかも知れないけど…"
    pl "俺がここに来てまだ三日ぐらいなのに、その割にはこんな状況に出くわしすぎとは思わないか？"
    nar "彼女の顔に陰りが差す。{w}俺は一方遅れて口を噤んだが、余計なことを言ったとは思っていない。"
    nar "確かめてみたかった。彼女への噂は今まで十分聞いてきた。{w}親の後光に依存する無能な主教だって。"
    nar "俺は、その悪意ある烙印がどれほど真実を帯びているのか、気になっていた。"
    nar "しかし彼女はまた頭を上げた。{w}その顔には相変わらず笑顔が浮かんだままだ。"
    show SCG_05 idle with fastdissolve
    hk "[na]兄弟、わたくしはそこまで無関心ではございません。"
    nar "その声はいつものように穏やかで、いつもと違ってきっぱりとしている。"
    show SCG_05 1 with fastdissolve
    hk "わたくしの部署で起きてる事柄については理解しているつもりです。"
    pl "なん…なら何で何もしないんだ？主教なら声を掛けるとか、仲裁とかするべきなんじゃないのか？"
    show SCG_05 idle with fastdissolve
    hk "何もしないだなんて、わたくしは充分お話をさせて頂いているつもりですぅ。"
    hk "個人的に主教室で面談を行ったり、注意させていただいたり…"
    pl "でも何も変わっちゃいないだろ、浄化部にはもっと強硬な対策が要る。"
    show SCG_05 1 with fastdissolve
    hk "ちがいますよぉ、わたくしは司祭のみなさまを信じておりますゆえ。"
    hk "先ほども申し上げました通り、負の感情はまた新たに負を呼び起こすだけ…"
    hk "わたくしは、わたくしの司祭たちを突き放すような行為は一切、致しませんのでぇ。"
    pl "人はそれを安易だって言うんだぜ…{w}一人信じてるばかりじゃ誰が分かってくれるって言うんだよ。"
    show SCG_05 0 with fastdissolve
    hk "[na]兄弟、わたくしが信頼する人々が常にそれに応えるという保証はございません。"
    hk "それゆえの、信頼ですので…わたくしは彼らを信じておりますぅ。{w}一度も、目を離したことなどございませんのでぇー"
    nar "最初はなぜあいつがそういうことを言ったかよく分からなかったが、今話してみるとその理由が分かってきた。"
    nar "確かにこんな人に喧嘩の仲裁を任せたってそれは単なるひと時、実質の解決には至らないだろう。"
    nar "人は自らの意思のない握手には仲直りできないものだ。{w}どれだけ祈りを捧げようとしても憎悪は消えない。"
    nar "彼は多分これが言いたかっただろう。"
    pl "主教様は、もしこの部署以外のところで働けるようになったらどうする？"
    show SCG_05 1 with fastdissolve
    hk "ふふふ。"
    nar "ゆらゆらと、やけに背の高い彼女の体が動くと髪の結びも共に揺らぐ。{w}感情を表現する前に揺れるなんて、まるで獣のしっぽだな。"
    hk "わたしたち浄化部は、他の部署とは違います。"
    hk "他の部署は自身の選択によって行ける場所ですが、浄化部は現実に限界まで追い込まれた人々の陥る場所なのです。"
    pl "そんな言い方、まるで…"
    show SCG_05 0 with fastdissolve
    hk "地獄、みたいと？"
    nar "かすかに頭の中で浮かんでいた単語が、彼女の口から出てきた。"
    nar "ぼうっとなった俺は答えるどころか頷けずに只固まっていたが、その反応全ては肯定を示している。"
    nar "そんな俺の姿を見ては彼女は袖で口を隠して笑っている。"
    hk "ですがここは地獄ではございません。{w}落ちた人々はみな、生きている以上は上を目指すことができるのです。"
    hk "わたくしは、それを願って司祭のみなさまを教える仕事についているのですから。{w}自身の罪と向き合えるよう、人を愛せるよう…♪"
    pl "じゃあ…自分の考えが間違っているかも、って思ったことは？"
    show SCG_05 1 with fastdissolve
    hk "ございません。{w}わたくしはわたくし自身と、わたくしに知恵をお授けくださったお父様を信じておりますゆえ。"
    show SCG_05 0 with fastdissolve
    hk "自身を信じることの出来ない人など、誰も信じることは叶わないのですぅ。"
    pl "司祭たちはハク主教様のことあんま好きそうじゃなかったけど…"
    show SCG_05 1 with fastdissolve
    hk "わたくしは司祭のみなさまを公平に愛しております。"
    pl "ぐっ、そういうところなんだって。"
    hk "それがわたくしの「信頼」ですのでぇ…♪"
    nar "立ち上がっていた煙は徐々に消え去る。{w}肺と喉が息苦しくなり、音のない空咳が出てきた。"
    nar "この人のことはやはりよく分からない。"
    nar "普段人って話してみれば今何を考えているのか、俺から何を欲しがっているのか見えてくるはずなのに、"
    nar "それが分からなくてどうすればいいのか困っている。"
    show SCG_05 0 with fastdissolve
    nar "情報を得れば得るほどもっと謎になっていく。{w}じろじろ見ているとなぜか目が合いそうでうっかりと視線を逸らした。"
    nar "だが一つ確実になったのは、この人の前では何を言っても無駄だってこと。"
    nar "直接的な解決の為には動くとは決してないってこと。{w}なぜならその頭の中は全く別の世界なんだから。"
    nar "しかしこれがそう悪いことでもない。{w}おかげで俺は自分の言葉に負担感を重く感じなくて良いってことだからだ。"
    pl "実は今日街で色々あって。"
    show SCG_05 8 with fastdissolve
    hk "色々とはぁ…"
    pl "どっか怪我したとかじゃないんだけど、俺に向かってめちゃくちゃにブチギレしてて。"
    pl "俺はその人達に今日初めて会ったし、その人達に何があったかなんて知らないけど…"
    hk "そおですねぇ。"
    pl "それで、ちょっと複雑な気分になっちまって。"
    pl "この程度のことでここまでやられちゃうとかさ、本当にここで仕事していく資格なんてないんじゃないかって…"
    show SCG_05 0 with fastdissolve
    hk "彼らは無論人の子ですが、彼らの負の感情の受け皿である我々もまた人の子です。人は、感情を得てこそ人となるものなので。"
    nar "近づいてきた彼女が自分の手を俺の肩に置いた。{w}最初は驚いたがすぐ静まってきた。"
    nar "硬い革の手袋の彼女の手からは何の暖かさも感じられず、それが寧ろ落ち着けるところだった。"
    nar "俺を慰めようとしているように手は柔らかく肩を撫でる。"
    show SCG_05 1 with fastdissolve
    hk "哀しいときは哀しいと、辛いときは辛いと、悔しいときは悔しい、と、そう仰れば良いのです。"
    pl "……"
    show SCG_05 0 with fastdissolve
    hk "がんばったのですねえ、兄弟は…"
    pl "そう…正直びっくりしたんだ。{w}理由とか、部署の役割とかを置いといてただ。"
    show SCG_05 1 with fastdissolve
    hk "うんうん、そうやって正直に話せばいいのですよぉ。"
    pl "ああだったりこうだったりせわしない人だな、主教様は…"
    show SCG_05 at bounce
    hk "お世話は、だ～いすきですよぉ～"
    pl "いや、そういう意味じゃなくて…"
    hk "お世話のためにあちこち忙しく動き回っているとーわたくしがここに存在する、という実感が湧きませんかぁ～？"
    pl "仕事の虫みたいなこと言うじゃん…{w}仕事っても仕事によってだろ？"
    pl "どうせ実感したいならさ、もっと自分だけにしか出来ないことをやりたくはないのか？"
    hk "この仕事こそが、わたくしだけができることだと思っておりますぅ～"
    pl "せわしなく動き回るのが？"
    show SCG_05 0 with fastdissolve
    hk "兄弟の悩みを聞くことですねぇ。"
    pl "悩みを聞くって…"
    hk "浄化部は人のため存在しますがーしかし主教は司祭のために在ります。"
    hk "[na]兄弟、きみはきっと魔導部特採としていつか部署を離れてしまうのかもしれませんが、"
    hk "今は我々浄化部司祭の一員ですので。"
    hk "わたくしにはきみを管理すべき義務があるのです。"
    show SCG_05 1 with fastdissolve
    hk "辛いことや悩みがございましたら是非、ご相談くださいねえ～"
    pl "……"
    nar "僅かな隙間。{w}俺は彼女を覗いては、一足遅れて距離を取った。"
    nar "彼女の手に触れた肩の片方がなぜか重たい。答えを言い出す前に、まず頭を横に振った。"
    pl "や、いいんだ。別にそんな悩みとかないし…"
    nar "彼女に俺が今何を経験しているのか話す気はない。"
    nar "他の誰かがそれを知ったとしても十分忌まわしいのに、彼女に知られて良いことは決してあるわけがない。"
    nar "たとえ特別な処置がなくても彼女だけには言いたくない。"
    nar "こういう拒否感を感じるのはやはり彼女への信頼が足りないせいだろう。"
    hk "そおですかぁ。{w}それではまた別のお話でもよければ、いっぱい聞かせてくださいねぇ。"
    show SCG_05 at bounce
    hk "お話、だ～いすきなのでぇー"
    pl "主教様が忙しくなけりゃな。"
    nar "彼女が信頼できる人かどうかはまだ見当がつかない。"
    nar "個人の能力って、見た目で確認できることではないし、彼女の正体とか本質とかもまた不明だ。"
    nar "俺は彼女のことを無意識的に警戒しているのかもしれない。"
    nar "只分かってきたことが一つ、なぜ彼女が浄化部の主教に任されたかについてだ。"
    show SCG_05 0 with fastdissolve
    hk "[na]様、浄化部での暮らしは楽しいですか？{w}神殿のことは、好きになりましたか？"
    nar "巨大な檻のようだと思った。{w}ヤギやウサギなどのあらゆる動物を取り込んでおいた檻。"
    nar "暴れる獣が檻から脱しようとでもしないと何の制裁も加えない主教。{w}この人はそうやってバランスを合わせていた。"
    pl "こんなモン、好きって言えるならそれこそイカれてるって証拠だろ。"
    hide screen textbox with dissolve 
    pause 0.5
    show SCG_05 1 with dissolve
    pause 0.5
    hide SCG_05 with dissolve
    pause 1 
    show screen textbox with dissolve
    nar "無理やりにでも肯定的な答えをしようとしたがどうしてもできなかった。{w}彼女は何も言わずに笑ったまま離れた。"
    nar "彼女が何者なのかは聞けなかったし、気持ちも複雑になってきた。{w}彼女が嫌いではないが、浄化部は嫌だ。"
    nar "特に、彼女が主教である浄化部のことは実に厭わしい。"
    hide screen textbox with dissolve 
    stop music fadeout 3
    pause 2
    $ day_hk = True
    $ love_hk = love_hk +1
    $ day_time = day_time +1
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_2


label day3_hk_F:
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg04 with dissolve
    else:
        scene bg04_1 with dissolve
    call place04 from _call_place04_5
    show screen nvlbox with dissolve
    play music 'audio/bgm/dialogue.ogg' fadein 3
    "\n 寮の方はさすがに混んでいるが、反対側の道に入ると目の前の人影も全部消えてしまった。"
    "ここは作業場への道だ。{w}人何人かが横になって歩いても十分であるほど広やかなのに、この時間帯はがらんとしている。{w}昨日もそうだったし。"
    "どす黒い空に煙が舞い上がり、肺を苦しめてくる苦い煙に思わず咳が出る。{w}作業場の空気は屋外であり冷ややかだが、あちこちからの煙のせいで決して清いわけではなかった。"
    et "空気の質といえば今日行った村のもそんなに澄んではいなかった。{w}汚れた空気はさすがに州都そのものの問題なのかもしれない。{w}その煙たい空気の中で俺たちは死体を処理していた。{w}いや、実際処理したのは彼一人だったが。"
    nvl clear
    "\n 干からびた黄色いスープの跡の焦げ付いた床の狭い部屋の中で、老人の死体は亡者になる寸前だった。"
    "処理が早かったおかげか特に危険性はなかった。{w}只黒い手足が動いていただけ。{w}骨と皮ばかりの痩せぎすの手足はまだ主が生命を有していると勘違いしたように動いて、奴はすぐ刀を振り上げた。{w}俺は遠目に立ってその光景を見ていた。"
    et "思い出してみればやたらに気まずくなってきた。{w}今この焼却炉で燃えている物も、その死体の一部か。{w}近づくと喉が辛くなってきた。{w}焼却炉の中には、もう元の判明できない灰の山だけが残っている……。"
    nvl clear
    hide screen nvlbox with dissolve
    pause 1
    $ day_hk = True
    $ day_time = day_time +1
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_3
    return


label day3_gr:
    show screen place_day3
    show screen place_gr
    with None
    hide screen place_gr
    hide screen place_day3
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg06 with dissolve
    else:
        scene bg06_1 with dissolve
    call place06 from _call_place06_5
    play music 'audio/bgm/grette.ogg' fadein 3
    show screen textbox with dissolve
    nar "歩き慣れた医務室へ一走りに駆け付けた。"
    nar "神殿の司祭の為にいつも開いたその扉を見ると、暖かい空気と浅いシナモンの香りが一気に冷えた体を包んだ。"
    nar "その感覚に肩を降ろして前を見れば、お菓子一つを銜えたグレーテ先生が座っている。"
    nar "いつもだったら俺が来たことにすぐ気付くはずだが、集中しているのか書類に視線を向けたまま、"
    nar "お菓子を銜えた口だけが動いている。"
    pl "先生？"
    nar "俺が呼ぶと、一瞬頭を振り上げた彼女の目が大きくなる。"
    nar "そしてちょっと慌てたように、片手に書類を持ったまま席から立ち上がっては、また片手で口を隠してお菓子を飲み下す。"
    hide screen textbox with dissolve
    show SCG_14 6 with dissolve
    show screen textbox with dissolve
    show SCG_14 at bounce
    gr "あ…あらまあ！{w}この子ったら…ノックも無しに入ったらいけませんよ～"
    pl "ゴメンゴメン、開いてたからつい…{w}おやつタイムの最中だったり？"
    show SCG_14 5
    play sound "audio/se/hit.ogg"
    gr "おやつタイムじゃありません、書類読んでました！" with sshake
    pl "へへっ、何だっていいだろ。美味しそうだね～"
    show SCG_14 9 at huruhuru
    gr "うう、そうですよ…わたしはだらしなくって品もない先生ですよ～だ…"
    show SCG_14 7 with fastdissolve
    pl "ちょっと色々雑談でもどうかな、って思ったんだけど。{w}忙しいか？"
    show SCG_14 1 with fastdissolve
    show SCG_14 1 at bounce
    gr "いいえ、全然問題ないわ！{w}わたしもちょうど誰かとゆっくりお話がしたかったんですもの。"
    pl "よかった～先生とお話したらちょっと気が楽になるかなって思ったんだよ。{w}あっ、もしかしてそのお菓子手作り？"
    show SCG_14 idle with fastdissolve
    gr "いつもお世話になってる子から頂いちゃったの。"
    show SCG_14 1 with fastdissolve
    gr "州都の有名なお菓子屋さんのらしいんだけど、しっとりしたバター生地と紅茶の香りが素晴らしかったわ…"
    nar "先生は説明の途中にも再びあの味を思い起こしたか、うっとりした顔で余韻を浸る。"
    nar "グレーテ先生ぐらいのお人好しなら周りからのプレゼントもいっぱいなんだろう。"
    nar "俺としても、神殿に来てまだ幾日も過ぎていないのにもう彼女から多くの物を貰ったからだ。"
    nar "親切、そして甘いお菓子はもう俺の頭の中では彼女を代表する何かになっていた。"
    show SCG_14 7 with fastdissolve
    gr "あ…でもごめんね、今のでお菓子食べ切っちゃったのよね…"
    pl "そんな気にしなくていいって、先生が貰ったモンだし先生が食べなきゃ。"
    show SCG_14 idle with fastdissolve
    gr "でも折角来てもらったのに…{cps=*0.2}う～{/cps}ん…"
    show SCG_14 1 with fastdissolve
    gr "そうだ、今朝焼いたアップルパイがちょっと残ってるはずだけど、いかがかしら？"
    pl "食べる！"
    hide screen textbox with dissolve
    hide SCG_14 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "花の絵が描かれた皿の上に小さな黄金色のアップルパイの盛り付けをすると、"
    nar "さっき扉を開いた時のシナモンの香りが直に俺の前に溢れてくる感じがした。"
    nar "皿の前に揃っているフォークも小さくて可愛い柄が描かれ、まるでままごとをやっている気分だ。"
    nar "とろとろして、甘すぎではないパイが口の中で粉々に砕ける。"
    nar "立派な味でも、その逆でもない素朴な味は故郷でよく食ったパイを思い浮かべる。"
    nar "沈んでいた心が今になって心地よくなってきた。"
    hide screen textbox with dissolve
    show SCG_14 idle with dissolve
    show screen textbox with dissolve
    show SCG_14 at bounce
    gr "お味はどうかしら？"
    pl "超美味い！今まで味わったパイの中で最高！"
    show SCG_14 6 with fastdissolve
    gr "全くこの子ったら、お世辞が上手だわ～"
    show SCG_14 idle with fastdissolve
    gr "冷めちゃっててごめんね。さっき保健部の子たちに分けてあげてたのよ。"
    pl "丁度お昼の時間だしな。{w}こんなおやつまで貰っちゃえるなんて、保健部はいいとこだな。"
    show SCG_14 8 with fastdissolve
    gr "栄光だわ。でも神殿で料理していることをあまり良く思ってない人もいてね…"
    show SCG_14 10 with fastdissolve
    gr "わたしもまた、全員に分け与えられるわけじゃないから…"
    pl "そんな人も先生のお菓子を食べると考えが変わるかもよ？"
    show SCG_14 8 with fastdissolve
    gr "ふふっ、そうなるといいわね。"
    show SCG_14 idle with fastdissolve
    gr "それでは、[na2]くんの運んできたお話を聞いてみましょう～"
    pl "周知の事実かも知れないけど…{w}俺って、魔導部からの採用で神殿に入っただろ？"
    gr "うーん、そうね？"
    nar "やはり神殿の誰だって知っているものか…"
    pl "で、今日ちょっと魔導部の主教様とお話してきたんだよ。"
    show SCG_14 7 with fastdissolve
    gr "あらま…{w}大丈夫？何か酷い事を言われてたりは？"
    pl "えっ、いや、そこまでじゃなかったけど。みんな似たような心配するんだな。"
    show SCG_14 0 with fastdissolve
    gr "良かったわ、エルジェーベト様は魔導部の司教らしく威厳があり、芯の強い人だけど…"
    gr "言葉遣いが荒い傾向にあるのよね。あの人の言葉に傷付いてしまう子が多いの。"
    pl "ふぅん…確かに、高圧的な面があった気もするな。{w}上から目線っていうか。"
    show SCG_14 5 with fastdissolve
    gr "そう、わたしが作ったお菓子に目もくれないの！{w}ひどいわ、全く。"
    pl "さっきの話ってエリィ主教様の話だったんだ～？"
    show SCG_14 0 with fastdissolve
    gr "こほん、また恥ずかしい話をしてしまったわね。{w}でも次こそは成功させて見せるわ。"
    show SCG_14 1 with fastdissolve
    show SCG_14 at bounce
    gr "エルジェーベト様は毎回会議の度紅茶を召し上がるの。{w}紅茶にピッタリお似合いのデザートを沢山作っておかなきゃ！"
    pl "先生なら必ず成功するって！俺にも味見させてくれよ～"
    show SCG_14 0 with fastdissolve
    gr "勿論、分けてあげるわ。{w}失敗作になっちゃうかもだけど…？"
    pl "失敗作でも全部食べてやるからさ～"
    pl "あ、とにかく。{w}主教様と話し合った後エノク兄ちゃんに会ったんだよな。{w}知ってる？あの魔導部の…"
    gr "知ってるとも。一段と身長の高い人よね。"
    pl "そう！すっごく派手な人だったな。"
    gr "ふふ、あの子に何か聞かされたのかな？"
    show SCG_14 7 with fastdissolve
    pl "それが、エノク兄ちゃんってアル姉といっつも一緒だろ？{w}で、その兄ちゃんが俺にアル姉のことを聞いてくるんだよ。"
    gr "それってもしかして…"
    pl "もしかしてのもしかしてだよ！"
    show SCG_14 1 with fastdissolve
    gr "あらあら～～～"
    nar "先生は幼い女の子のように頬を包んでは身を捩った。{w}こんな話をわざと言葉にしなくても伝わるのはなぜだろう。"
    nar "さっきもそうだった。エノク兄さんは隠そうとしたことだが、俺はそれがすぐ分かってきた。"
    nar "好感や人への愛情ってことはなぜそんなに見え見えだろうか。{w}わざと隠そうとしてからそう見えてしまうのか。"
    show SCG_14 at bounce
    gr "あの子は若い方なのにとてもお行儀が良くて愛想も良いから一緒にいるととても穏やかな気分になれるの。"
    show SCG_14 0 with fastdissolve
    gr "通りすがりにもいつもちゃんと挨拶を交わしてくれたり、何か必要な物はないかとすぐすぐ気に掛けたりしてくれて…"
    pl "そう、最初ちょっと怖そうだったけど話してるうちに分かったよ、悪い人じゃなさそうだな～って。"
    show SCG_14 3 with fastdissolve
    gr "はぁ…だからこそなんだか心配なのよね…"
    gr "あの子があんなに融通が利くのは多分周りの目をとても気にしながら育ってきたからだと思うの。{w}魔導部家は大体保守的だから。"
    pl "あぁ…そういえば確かに第一家門やら第三家門やら言ってたような。"
    nar "記憶を辿って話すと、グレーテ先生は眉をひそめて短い呻き声を出した。"
    show SCG_14 2 with fastdissolve
    gr "人を出身で差別するなんて……"
    show SCG_14 3 with fastdissolve
    gr "そんな環境で育ってきたからこそ、あの子は多少誠実すぎるとこがあってね、"
    gr "言いたいことがあっても言えない気質なんだと思うの。"
    gr "先生としては皆まだ子供なんだし、やりたいことは我慢しないでほしいな。"
    pl "ふぅん…"
    nar "先生の説明を聞いてみれば、あの人がどんな人なのかまたと分かってきた気がする。"
    nar "只照れてそんな風に否定したことではなく、内心を探っていたってことか…"
    pl "先生は観察眼が鋭いな。{w}何回か話し合っただけでそこまでわかっちゃうのか？"
    show SCG_14 8 with fastdissolve
    gr "これくらいも出来なければカウンセラーとしてお仕事できないもの。"
    show SCG_14 2 with fastdissolve
    gr "いい？{w}こどもたちに何より必要な物は、自分を気に掛けてくれる大人の存在よ。"
    gr "自分の周りにはいつでも助けを求めることが出来る大人がいるという事実を忘れてはいけません。"
    nar "彼女はのぼせ上ったようにきっぱりした言葉を吐き出す。{w}迫ってきているような口ぶりが\n、俺の悩みを間接的に聞いているようだ。"
    nar "俺は再び昨夜のことを思い出したが、すぐ考えを止めた。{w}せっかく上機嫌になったばかりなのにまた鬱になりたくはない。"
    nar "今の気分が昨晩の記憶に因って流されないように、残ったアップルパイを一口食べる。"
    nar "ちょっと入れすぎのシナモンの味が喉を苦しめる。"
    pl "先生が真面目にカウンセラーとして働いてるとは思ってもなかったぜ。{w}保健部の仕事もあるだろ、忙しくはないのか？"
    show SCG_14 7 with fastdissolve
    gr "あれ、言ったことなかったっけ？{w}まだまだこれから、って感じだけどね。"
    show SCG_14 at bounce
    gr "う～ん…{w}正直忙しくない、って言ったら嘘になるけど…"
    show SCG_14 1 with fastdissolve
    gr "わたしはいつもカウンセラーとしていられてよかったな、って思ってるわ。"
    gr "少しでも神殿の子たちの力になれるなら、この程度の忙しさなんてへっちゃらよ。{w}寧ろありがたいくらいですもの。"
    pl "わぁ…前から凄いなって思ってはいたけど、先生ってやっぱかっこいいよな～{w}言葉に余裕があるじゃん。"
    show SCG_14 8 with fastdissolve
    gr "でもわたしなんてまだまだ。人と対していると色んなことを学べるな、って思う時があるの。"
    gr "しかも神殿の全ての子がわたしを頼ってくれるわけじゃないから…"
    nar "そりゃまあ、神殿にカウンセラーがいたとしても悩みをそう気軽に話せる人は少ないだろう。"
    nar "人は誰でも自分の悩みや秘密に恥を感じて隠したがるものだから。"
    nar "人は嘘をつき、事実を隠す。{w}さっきの俺もそうしたように。"
    pl "じゃあ…{w}カウンセリングは神殿入ってから始めたのか？"
    show SCG_14 0 with fastdissolve
    gr "いいえ！学生の頃から勉強はしてたの。{w}もっと色々学びたくて州都を離れていた頃もあったわ。"
    gr "初めてカウンセリングをしたのは…{w}もう10年ちょっと前ぐらいかな？"
    show SCG_14 8 with fastdissolve
    gr "あの日のことは忘れられないわ、あの頃はわたしも未熟だったものね…"
    pl "おぉ、先生のひよっこ時代の話だなんて、気になるな！"
    show SCG_14 6 with fastdissolve
    show SCG_14 at bounce
    gr "ん？え、そんな！{w}急に話そうとすると恥ずかしいわ…{w}本当に聞いてみたい？"
    pl "勿論！"
    gr "それなら、こほん…"
    show SCG_14 0 with fastdissolve
    nar "今まで前の俺から視線を離していなかった彼女はふと思い出を偲ぶ目で、視線を移った。"
    nar "そこには見慣れた医務室の風景だけだが、彼女には別の何かが見えているようだ。"
    nar "彼女は集中する時、目の前の物や者から目を離さない。"
    gr "そうねぇ…もう10年も経っちゃったんだ…"
    gr "わたしが初めてカウンセリングを担当した子は幼い女の子だったわ。"
    gr "そう、今の[na2]くんよりもうちょっと年下ぐらいかな？"
    gr "その子は元々わたしの知り合いが担当でね、最初はちょっと不安だったけど…"
    gr "その子の顔を見ると同時に不安なんて吹き飛んでしまったわ。"
    pl "すっごく可愛かったからとか？"
    show SCG_14 1 with fastdissolve
    gr "そう！肌は真っ白でまつげも長くて、良く造られたお人形さんみたいだったの。"
    show SCG_14 10 with fastdissolve
    gr "本当にお人形さんみたいに無表情で目が暗かったから。"
    gr "その時思ったわ、この子のためにわたしの出来る事なら何でもしなきゃ、って。"
    gr "そんな彼女に初めて先生って呼ばれたときは、そのぉ、こういう事を言うのはすごく恥ずかしいんだけど…"
    show SCG_14 8 with fastdissolve
    gr "ちょっぴり泣いちゃってね。"
    pl "今は皆が先生って呼んでくれてるのにな。"
    show SCG_14 1 with fastdissolve
    gr "そうそう、本当感謝してもしきれないわ。{w}今のわたしを作ってくれたあの子にはずっと感謝してる。"
    pl "どんな子だった？"
    show SCG_14 0 with fastdissolve
    gr "詳細はクライアントの個人情報だから流石に言えないけど、"
    gr "酷い事故に遭ってて心理的に不安定で記憶が混乱している状態だったわ。"
    gr "最初は口数も少なくて、全然心を開いてくれなかった。"
    pl "へぇ…"
    gr "でもすっごくいい子だったわ。{w}わたしの言うことをよく聞いてくれてて、どんどん自分からも話してくれるようになったの。"
    gr "小さい悩み事から段々大きいこともお話するようになって…"
    gr "ありがたい事にわたしを凄く頼ってくれててね、妹が出来たみたいで嬉しかったわ。{w}これは運が良かったっていうか…"
    pl "それは運じゃなくて、先生のお話が上手だったからだと思うぜ。"
    pl "俺はその子のことはまるっきり知らないけど、"
    pl "先生がどれだけその子のことが好きだったのかは聞いてるだけで伝わってくるからさ。"
    pl "その心が通じ合ったんじゃないか？"
    show SCG_14 1 with fastdissolve
    gr "本当、そう言う[na2]くんもとてもお口が上手じゃない。"
    gr "先生、感動しちゃったわ…"
    pl "泣くなよ先生～{w}先生の幸せを願う人は多いだろうけど、俺だって先生には笑っていてほしいからさ。"
    show SCG_14 at bounce
    gr "もちろん！あなたたちが居てくれるなら先生はいつだって、何なら寝ててもずっとにっこりにこにこしていられます！"
    pl "ホント、先生を見てると俺まで元気になるな！"
    show SCG_14 0 with fastdissolve
    gr "ふふ…それだわ。{w}わたしを思ってくれるのも嬉しいけど、一番の喜びはあなたたちが幸せで居てくれる姿を見守る事ですから。"
    gr "あなたたちが笑っていればわたしもずっと笑っていられるし、"
    gr "わたしの笑顔で[na2]くんが元気になるなら、これ以上は望まないわ！"
    pl "うわ、本当にこれだけで成り立つならずっと幸せになれるな。"
    gr "そうそう、幸せも不幸せもすべて連鎖の一環。{w}全ては気持ち次第なのよ。"
    pl "でも先生の近くにいると本当にそうなってるような気がするんだよな。{w}保健部のヤツら、羨まし～…"
    show SCG_14 8 with fastdissolve
    gr "羨ましがらなくても神殿に居る限りあなたたちはみんな私の子供たちですから、いつでも会いに来てくれていいのよ？"
    pl "本当にありがとう。{w}そういえば…さっき言ってた子とはどうなったんだ？"
    show SCG_14 0 with fastdissolve
    gr "その子とはもちろん、今でもよく会ったりしてるわ。{w}立派な大人に成ったの。"
    gr "とても素敵で、美人で…{w}お土産もわざわざ持ってきてくれるもの。とても偉い子なのよ。"
    pl "よかったな！もう10年前って言ってたのに、今もずっと縁があるって不思議だな…"
    pl "ん？ちょっと待てよ、わざわざお土産を持ってくる、ってことは…{w}もしかして神殿の人？"
    show SCG_14 1 with fastdissolve
    gr "あら……{w}ふふ、また秘密が増えてしまったわ。"
    pl "えっ、マジかよ！会ってみたいな！"
    show SCG_14 0 with fastdissolve
    gr "いつか会えるはずよ。{w}わたしの古い友人でとても賢い子がいてね、"
    gr "その子が言うには人の繋がりという物は巡るものだから、"
    gr "わたしがそのつながりを大切にしていればまたそれら同士で繋がることがあるんですって。"
    pl "難しい話だな…"
    gr "わたしもそう思うわ、でも簡単に言えば友達の友達は友達…{w}みたいな話じゃないかしら？"
    gr "実際わたし、こうやってできた友達が多いのよね。"
    pl "それなら何となくわかる！"
    show SCG_14 1 with fastdissolve
    gr "でしょう？周りに知り合いが多いってとてもいいことなのよ。{w}こうやってゆったりお話も出来るしね。"
    pl "俺もそう思う～先生とは色々話が合うしな。"
    gr "偶然ね、わたしもそう思ってたの！{w}[na2]くんから先に話題を呼んできてくれて本当に嬉しいわ。"
    nar "軽く談笑する間にどれだけの時間が過ぎたか、壁にかかった鳩時計が鳴いた。時計の針はもう午後を示している。"
    show SCG_14 0 with fastdissolve
    gr "もうそろそろ仕事に戻らなきゃ。[na2]くんも戻らないとでしょう？"
    pl "ああ。今日はありがとうな、先生！{w}雨でちょっとげんなりしてたけど、お陰様で気分が晴れたぜ。"
    gr "なあに、これからも良かったらたまにこのお喋りおばちゃんの話し相手になって頂戴ね。"
    pl "寧ろこっちからお願いしたいぜ。"
    pl "俺、人と喋るの大好きなんだけど神殿じゃああんまりおしゃべりする機会なんてないから窮屈でさ…"
    gr "それならわたしの専門ね。[na2]くん、好きなお菓子とかはあるかしら？作り置きしておきたいの。"
    pl "好きな菓子か～{w}…や、正直お菓子について詳しくはないんだ。{w}嫌いじゃないけど、食べる機会があんまりなかったもんで。"
    pl "俺らの故郷じゃよくドライフルーツとか、普通にパンを食ってたりしてたな。"
    pl "バターやジャムを加えて。おやつってより食事の代用だな。"
    show SCG_14 7 with fastdissolve
    gr "あらら、そう…"
    pl "だから先生の作りたいものを毎日作ってほしいんだ！そうすればいつか俺にもお気に入りが出来るかもだろ？"
    show SCG_14 1 with fastdissolve
    gr "あらあらまあまあ！[na2]くん、頭が冴えてるのね！お陰様で久々に菓子作りのやる気が湧いてきたわ。{w}先生に任せて！"
    hide screen textbox with dissolve
    hide SCG_14 with dissolve
    stop music fadeout 3
    pause 2
    $ love_gr = love_gr + 1
    $ day_gr = True
    $ day_time = day_time +1
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_3
    return


label day3_ar:
    show screen place_day3
    show screen place_ar
    with None
    hide screen place_ar
    hide screen place_day3
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg102 with dissolve
    else:
        scene bg102_1 with dissolve
    call place102 from _call_place102_3
    show screen textbox with dissolve
    nar "彼女に会いに来たのは良いが、訓練場の前に立つと昨日の記憶が思い浮かぶ。"
    nar "俺を警戒した何十の瞳。一瞬で響いた声。{w}特にトラウマってことまでもないが、印象深い経験だったってことは事実だ。"
    nar "建物に似合って巨大な扉は、どこに手を触れたら良いのか全く分からない。"
    nar "しかも訓練場の中は騒がしい。ノックしても誰にも聞こえないだろう。"
    nar "俺は結局、浮き腰になって、曖昧な姿勢で扉に耳を押し当てた。{w}中に何人がいるか予想でもしようと思った。"
    nar "かすかに騒ぐ声を聴いていたら、突然、あの重い扉が開く。"
    nar "びっくりして一歩退いた目の前、扉の向こうには一人の司祭がぽかんと立っていた。"
    pl "あ、あのぉ～"
    nar "やっべ、今きっと不審者に見えただろう。"
    nar "しかし案外布で顔を隠した司祭の声は明朗であった。"
    ex6 "[na]様ですね！お待ちしておりました。"
    play music 'audio/bgm/daily.ogg' fadein 2
    pl "え、俺を？"
    ex6 "左様でございます。{w}アルネ様は奥の方でございます、ご案内致します。"
    nar "何だ？{w}昨日までも人の前でひそひそと取り沙汰していたくせによ。"
    nar "疑いを持ったまま彼に付いて入ると、昨日と同じく司祭たちの動きが止まった。{w}が、これは雰囲気がまるで違う。"
    nar "人の声は全く聞こえなく、俺が視線を送る度に丁寧な黙礼だ。{w}彼女の怒号のおかげか。"
    nar "俺はいきなり変わっていた態度を受け入れることが気まずくなって、誰とも目を合わせずに前だけを見ながら真っすぐ歩いた。"
    nar "そのうちにふと、前のアル姉と目が合った。"
    nar "周りを取り囲んだ静かな観客、そしてその中心にいた彼女の前に立つと、昨日まではなかった妙な緊張感がしてきた。"
    nar "まるで見えない演出家が何とかして演劇などの舞台を盛り上げているようだ。"
    stop music fadeout 2
    hide screen textbox with dissolve
    pause 1
    show SCG_07 idle with dissolve
    pause 1
    show screen textbox with dissolve
    play music 'audio/bgm/arne safe.ogg' fadein 2
    ar "お早うございます、[na2]兄弟。{w}またお会いできて光栄でございます。"
    pl "いんや、昨日もそうだったけど…{w}なんだか忙しい中俺が邪魔しちゃってるみたいで申し訳ないな。"
    show SCG_07 9 with fastdissolve
    nar "長いまつげに箍をかけたまぶたが上下に動いた。{w}その清潔な顔に浮かんだ表情は、まるで困っているように見える。"
    ar "魔導部の司祭は基本的に団体行動を最重要視する為、個人的に時間が捌けないのは大変、申し訳ないと思っております。"
    pl "姉さんが謝ることないって！いきなり遊びに来る俺が悪いんだし。"
    ar "暫し、お待ちいただけますでしょうか。{w}すぐ片付けてお茶を…"
    pl "や、忙しそうだし、今日は姉さんの仕事の見学でもしていくよ。"
    show SCG_07 10 with fastdissolve
    ar "しかし…"
    pl "いいっていいって、これこそ研修生のすべきことだろ～？"
    nar "俺はできる限り活気を出して答えたが、彼女はまだすっきりしない顔で司祭と俺を交互に見つめた。"
    show SCG_07 0 with fastdissolve
    nar "そうしたら何かの決心を立てたか、俺の方にはっきりと目を向けた。"
    ar "畏まりました…{w}しかし、私が直接お手本を見せている時以外は、隣に居てやっては頂けないでしょうか。"
    pl "ん？司祭たちの鍛練を見てほしいってこと？"
    ar "左様です。"
    pl "まあ…それぐらいなら。{w}俺が邪魔にならないといいけどな。"
    show SCG_07 9 with fastdissolve
    ar "私めの無茶をお聞き入れ頂き感謝いたします。"
    nar "アルネ・アルタナータ、{w}州都の名家たるアルタナータの長女、"
    nar "魔導部の主教であるエルジェーベトの姪っ子で、{w}弟のエノク・アピスと共に魔導部の補佐教として働いている。"
    nar "彼女について知っていることならこれくらいだ。{w}なのにそんな彼女と俺が婚約だって、州都の酷い冗談を俺が聞き分けてないのか。"
    show SCG_07 0 with fastdissolve
    ar "どうかいたしましたか？"
    pl "あ？あ、いや…{w}そういえばエノク兄ちゃんはまだなのか？"
    ar "はい、まだ来てはおらなくて。{w}多分違う仕事に回っているのでしょう。エノクは魔導部司祭の中では一番自由行動が多いので。"
    pl "確かに他の魔導部の人に比べると空気が違うよな。{w}そんな兄ちゃんが補佐教って面白いな。"
    show SCG_07 11 with fastdissolve
    ar "…[na2]兄弟、もし、エノクと別の場所で言葉を交わされたのでしょうか。"
    pl "まあ…ここ来る前にちょっとぐらい？"
    ar "そうですか…"
    pl "どうかしたか？"
    show SCG_07 7 with fastdissolve
    ar "申し訳ございません。{w}御二人の仲が深まったようで、嬉しくてつい…"
    pl "え、俺とお兄ちゃんが？"
    ar "彼への呼び名が大分親しくなっておられるではありませんか。"
    pl "ああ、それで…"
    ar "エノクは私と違い、人の扱いに慣れている上社交性が高いので会話するに当り最適の人物なのです。"
    ar "傍に置くようになればきっと、兄弟の助けとなることでしょう。"
    pl "アハハ…"
    ar "そして…エノク自身にも影響が有る筈です。"
    pl "俺と仲良くすることが？"
    ar "左様でございます。{w}彼はとても幼い頃我が家に訪れ、同じく幼かった私の力添えとなってくれました。"
    ar "成人式を終えた後もすぐ神殿に入り私を手助けして頂いております。"
    show SCG_07 9 with fastdissolve
    ar "その間彼は一度たりとも私へ不満を晒した事は無いのですが…{w}本来彼は縁や親睦を深めることを重視している身でして、"
    ar "今の生活が全く息苦しくない、と言うのは私や他の者の為についた善意から来た嘘でしょう。"
    pl "ふぅん。"
    show SCG_07 0 with fastdissolve
    ar "ですので、兄弟の様な自由な御方との会話は必ず、彼に良い影響を齎すであろうと思いましたのです。"
    pl "アル姉は本当に兄ちゃんが好きなんだな。"
    show SCG_07 7 with fastdissolve
    ar "勿論、エノクは私の自慢の家族ですので。"
    nar "只大事にしていることで止まらず自慢ってことか。俺は自分の家族を只の一度もそう思ったことがない。"
    nar "家族にそれなりの情はあったが、俺の自慢は、いつも陳腐な周りに染まらずに意志を守ってきた自分自身だった。"
    nar "自己主張性、それはあくまで原則を大事にする清廉なる彼たちには毒になるのではないか。"
    pl "でも俺からしたらエノク兄ちゃんも姉さんと一緒にいられることがすっごく自慢らしかったけど。"
    show SCG_07 11 with fastdissolve
    ar "エノクが、ですか。"
    pl "そう、だから多分姉さんがそう思ってるって知ったら驚くと思うぜ。{w}兄ちゃんと姉さん、良い家族だな～"
    show SCG_07 7 with fastdissolve
    ar "[na2]兄弟も我々の家族ではありませんか。"
    pl "俺…？"
    nar "思わず鳥肌が立ってきた。{w}しかし拒否感からの不愉快ではない。今日は一日そういう気分だったからすぐ分かる。"
    nar "心臓がぞっとして、背筋が冷えてしまう気持ち。{w}しかしさっきの鳥肌はそういうことではなかった。"
    hide screen textbox with dissolve
    hide SCG_07 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "その疑問を問おうとした瞬間、二人の司祭が近づき、しゃんと頭を下げ挨拶した。その間に終わったのか。"
    ar "ご苦労だった。どちらも良い実力だったぞ。"
    nar "その簡単な一言で二人の司祭の顔が明るくなった。{w}続いて姿勢、呼吸、動作などの説明が一つずつ言われ、"
    nar "二人の司祭は代わる代わる頷いたり、自分の手足を動かしてアル姉の動作の真似をしたり、まともに話を聞いているようだ。"
    ar "しかし貴公、一瞬だが左足首を後ろへと引いていたな。{w}午前の業務中無理をしたのではないか？"
    nar "あっという間に言葉を失った俺は興味を失い、全ての対話を聞き流していたが、その中の一言で驚いてしまう。"
    nar "きっと俺と話していたはずなのに、いつの間にそんなことを見切ったんだ？"
    nar "やがて二人の司祭が挨拶をする。{w}なのに、よく見れば俺に向けても頭を下げている。"
    nar "こっそりと退いた俺は鼻白んだ気分でするりと頭を下げる振りをした。"
    show SCG_07 11 with dissolve
    ar "会話中、申し訳ございません。"
    pl "姉さんすげぇや、俺と話してる最中にも全部見えてたのか？"
    show SCG_07 0 with fastdissolve
    ar "無論でございます。{w}ただの鍛練であろうと、彼らは熱意と誠を以て本気で実力をぶつかり合っているのです。"
    ar "それに私もまた本気で御相手をさせて頂くのが、彼らに対しての最低限の礼儀と云う物ですので。"
    pl "ふーん…"
    ar "そして、[na2]兄弟もそうなのです。"
    show SCG_07 7 with fastdissolve
    ar "兄弟は私へ言葉を掛けて下さいました。{w}この数多くの人の中他でなく私に向けて…"
    ar "ですので、兄弟の一言一句もまた逃す訳にはいかないのです。"
    pl "沢山の人の興味や支持を受けるのは良いけど…{w}たまに煩わしかったり、重いなって思ったことはないか？"
    ar "未熟者ですが、必要として頂けるのであればそれは感謝すべきではありませんか。"
    pl "…でも二つの事を同時にするのはさ、それなりの優先順位ってのがあるんだろ？"
    show SCG_07 0 with fastdissolve
    ar "はい、御座いますね。"
    pl "その順位の基準は普通どんな感じで決まるんだ？"
    ar "ふむ…鍛練室では主に皆の安全と、司祭達の士気、鍛練…の順でしょうか。"
    pl "あれ、士気を高めるのが一番なんだ。"
    ar "はい。身体能力の向上も大事ですが、更に大事なのは精神力です。"
    ar "集中が途切れたり、自尊心が下落してしまえば鍛練は自然と怠る様になってしまうではありませんか。"
    pl "まあな…何にしたってやる気がないとな。"
    nar "昨日の「突然の客」である俺を優先したこともそうだからか。"
    nar "整理されていないまま部外者をそこに残しておけば、司祭は訓練に集中できないだろう。"
    nar "賢明な人だ。{w}まるで全ての答えを備えているように迷わず答えて、戸惑い気味も一切見せない。"
    pl "じゃあさ…"
    pl "エノク兄ちゃんと俺だったらどっちを先に選んでくれるんだ？"
    show SCG_07 5 with fastdissolve
    nar "これはまたとんでもないことを聞いてしまった。"
    nar "いつもの冗談のように軽く投げればよかったのに、妙な重さが入って治めるにも困る。{w}今不機嫌であるせいだ。"
    nar "そういった言葉が俺の口から出たこともそうだが、さらに驚いたのは彼女の反応。"
    show SCG_07 7 with fastdissolve
    show SCG_07 at bounce
    ar "ふふっ…{w}あはははっ！"
    nar "ずっと静かだった彼女の顔に突然と笑いが弾ける。{w}その思いがけない光景に、俺はしばらくぼっとなってはパッと我に返った。"
    pl "ちょっと…笑いで誤魔化すなよ～"
    show SCG_07 4 with fastdissolve
    ar "軽薄にもお見苦しい姿をお見せして申し訳ございません。{w}しかし…"
    show SCG_07 1 with fastdissolve
    ar "そんな事を悩める立場になれるだなんて…{w}私は何て幸せな女なのだろう、と考えてしまいまして。{w}ふふ、申し訳ありません。"
    pl "……"
    show SCG_07 0 with fastdissolve
    ar "そうですね。ふむ…{w}確かに、これは少し悩まれます。"
    pl "だよな？"
    ar "兄弟はどうお思いでしょう？"
    pl "えっ…どうって？"
    ar "この場合、どちらを優先して頂きたいですか？"
    pl "…それを俺に聞くとか…{w}俺は当然俺のことを優先してほしいけど？"
    ar "では、そう致しましょう。"
    pl "はぁ…？！マジで？"
    show SCG_07 7 with fastdissolve
    ar "はい、兄弟がそれを望まれるのであれば私はその願いを成るべく聞き入れて差し上げたいのです。{w}それこそが私の喜びですので。"
    pl "兄ちゃんが聞けば寂しがるぜ～？どこの馬の骨に席取られちゃってさあ～"
    show SCG_07 11 with fastdissolve
    ar "そうでしょうか、私には違う様に思えますが。"
    pl "姉さんは人の心を知らないからそんな事簡単に言えちゃうんだよ。"
    show SCG_07 7 with fastdissolve
    ar "心というものは時折言葉で伝えなくとも視えるものなのです。{w}そして、私は常に兄弟に私の真心を込め接しております。"
    ar "それが私との会話において真実のみを告す兄弟へのせめてもの礼儀ですので。"
    hide SCG_07 with dissolve
    nar "言葉を終えた彼女は再び司祭の調子を見た。{w}やはり人の心を知らないんだ、誰が真実のみを告げるっていうんだ。"
    nar "都合の良い言葉とは、一時しのぎの為のものに違いない。{w}しかも今もこんなに背を見せているのではないか。"
    nar "その好意にどんな理由もないって考えれば只々恐ろしい。"
    nar "いっそ確かな理由でも分かれば良いのにな。"
    show SCG_07 11 with dissolve
    ar "長々と失礼致しました。"
    pl "んぇ、もう終わり？"
    ar "核心となる要点だけ説明致しました。{w}この方がお互い時間の短縮にもなりますので。"
    pl "そんなことも出来るんだ。{w}そんなに賢い手が使えたのになんで今まではやって来なかったんだ？"
    show SCG_07 0 with fastdissolve
    ar "今までは隣で私が言葉を終えるまで待ってくれるような人は居なかったので。"
    pl "うわ…"
    nar "思わず息を飲み込んだが、すぐ気を取り直した。"
    pl "それは…栄光だな。"
    show SCG_07 7 with fastdissolve
    ar "こちらこそ。"
    pl "姉さん、聞きたいことがあるんだけど…"
    show SCG_07 11 with fastdissolve
    ar "はい、何でしょう。"
    pl "人気の多い所で言うのはちょっとアレでさ、ちょっと場所を移して貰えないか？"
    nar "彼女は浮かぬ顔をした俺をしばらく瞬きをしながら見つめては、また何気なく答えた。"
    ar "承知致しました。"
    hide SCG_07 with dissolve
    hide screen textbox with dissolve
    pause 1
    scene black with dissolve
    pause 1 
    if hssh_rkn == True:
        scene bg102 with dissolve
    else:
        scene bg102_1 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "「承知致しました」って、どこまで俺の無理押しを受け入れようとしているんだ。{w}二人だけの湯沸室は静かだ。"
    show SCG_07 idle with dissolve
    ar "お茶は如何なさいましょう？"
    pl "いや、いいんだ。{w}あまり手間取らせたくないし。"
    show SCG_07 9 with fastdissolve
    ar "はい、それでは。"
    nar "彼女は俺の前側に慎ましやかに座った。{w}何度見ても不思議な人だ。{w}さらに、びっくりするほど今日見た彼と似ている。"
    nar "しかも彼は子供の姿をしていたのに、似ているって一目で分かってしまう。"
    nar "彼の言葉が再び頭に浮かんだ。"
    pl "今日魔導部の主教と話をしてきたのは…知ってるよな？"
    show SCG_07 11 with fastdissolve
    ar "はい…そうと伝え聞き致しました。そちらで何か問題でも…"
    pl "いや、問題って言うかさ…"
    nar "意味もなく髪を掻き上げた。{w}同じ問題だけを繰り返し思い出す頭が苦しい。"
    pl "俺が妙な話で騒ぎ立ててるだけなんだったら申し訳ないんだけど、{w}結婚…って何の話か知ってるか？"
    ar "結婚…"
    nar "まるで初耳の語のように、俺の言葉をそっくりつぶやく彼女を見ていると面から火が出そうだ。"
    nar "しかしそれもようやく沈んだ。{w}ずっと平常であった彼女の顔が、徐々に憂いで満ちていったからだ。"
    show SCG_07 0 with fastdissolve
    ar "…そうですか、その話を今やっとお聞きしたのですね。{w}それで今日…"
    pl "……"
    nar "やはり知っていたな、最初から。{w}なら他の司祭の態度が好意的になったことも…"
    pl "実はそれ以外は聞かされてないから、詳しい説明が欲しいんだけど。"
    show SCG_07 0 with fastdissolve
    ar "無論。{w}少し、我々の家門についての話になりますが…よろしいでしょうか。"
    pl "構わない。"
    show SCG_07 9 with fastdissolve
    ar "わかりました。"
    nar "彼女は頷いては、小さく息を吐いた。"
    ar "魔導部が神殿の他の部署と差別化されている点は、彼らが皆家族であると言う事実ですが…{w}その理由はお判りでしょうか。"
    pl "昨日も言ってたな、そういやそこの詳しい話は聞かされてない。"
    ar "我ら魔導師は遥か昔から紡がれてきた由緒ある家柄です。"
    ar "現時点で家門は派閥が別れていますが、その根は全て同じ所から来ているのです。"
    pl "根っこが同じ？{w}ってことは、ただ絆が深いって意味での比喩的表現じゃなくて、本当に魔導師はみんな親戚同士ってことか？"
    show SCG_07 0 with fastdissolve
    ar "はい、これこそが我々魔導師家門の伝統です。"
    pl "ふーん…{w}確かに、司祭がみんな怖いぐらい同じ顔してるなって思ったけど…"
    ar "吃驚させてしまいましたでしょうか。"
    pl "や、そんなに？{w}俺の元いた里の人たちもみんな同じ血筋から繋がった大家族みたいなモンだったし。"
    show SCG_07 9 with fastdissolve
    ar "安堵致しました。"
    pl "で…{w}そこでどうして赤の他人の俺を連れて来たんだ？"
    ar "それは伯父様の方から先に説明されたかと思いますが、兄弟にも魔導師血筋が繋がっている故です。"
    pl "それが一番理解できないんだよなぁ…"
    show SCG_07 0 with fastdissolve
    ar "魔導師はとても古くから代を繋いで来ましたので、遠く昔から大勢存在しておりました。"
    ar "そして彼らは州都外にも充分存在し得まして…{w}その内の一人が、兄弟の先祖様に当たるのです。"
    nar "確かに、故郷の里で俺と同じ年頃の男の子ってまるで全滅だった。"
    nar "その為、大人たちは俺の悶着や奇行に舌を巻きながらも、俺への教育を最後まで諦めてはいなかった。"
    nar "しかしこれは只そういったことでは説明ができない。"
    pl "州都に魔導師は沢山いるだろうに、どうしてそれが俺だったんだ？"
    pl "俺は聖痕もそんな無いし、血が繋がっているのかも不確かじゃないか。"
    ar "…それについて説明させて頂く為には、先に私の伯父様について話さなければなりませんね。"
    pl "魔導部主教様？"
    ar "はい、私の伯父様はよく「冷徹で保守的」と評価されますが…"
    ar "実は若くして当主の座に着かれた為、数多なる苦悩を抱えておられます。"
    ar "現在の定型化された親近婚体制に対し、改革を要すると主張なされました。{w}故にわざと外部者を家門に招かれたのです。"
    pl "あの人が…"
    ar "多分兄弟の存在を内密として先に浄化部に所属させたのもそれ故でしょう。"
    ar "現在伯父様の為されようとされる行為は家門に向けての反抗同様ですので。"
    pl "それで…当事者の俺にまで秘密にして？"
    hide SCG_07 with dissolve
    nar "彼女は唇を噛んだままで頭を垂れた。{w}その顔は再び上がることはなくずっと下がり、やがて顔が見えなくなった。"
    nar "黒き髪がテーブルの下に流れ下る。"
    ar "ごめんなさい。"
    nar "その一言を聞いてから分かってきた。{w}彼女は今俺に謝っているんだ。"
    show SCG_07 9 with dissolve
    ar "私共の私情に部外者である兄弟を引き込むような形になってしまった事、誠に、面目次第もありません…"
    ar "この件で私共に対して情が冷めてしまったとしてもそのお気持ちは充分理解致します。{w}心からお詫び申し上げます。"
    nar "今まで現実感のない、かすかな夢のように耳に留まった話が脳裏を突き抜けた。"
    nar "堂々として座を守っていた彼女の重々しい声が震えていたのはあまりにも衝撃で、家門の改革とか、"
    nar "利用されたってことよりももっと俺の胸に響いた。"
    nar "頬に生ぬるい液体が流れ落ちる。{w}びっくりして確かめてみれば、涙ではなく汗だった。{w}なぜ涙だろうと思ったのか。"
    pl "落ち着けよ、アル姉！謝らなくてもいいって、俺はどうってことねえよ！"
    pl "ただほんのちょっとびっくりしただけだから…顔を上げてくれ、な？"
    nar "緊迫に吐き出した声は嗄れている。{w}しばらく誰のものか知らぬ呼吸音だけが寂寞の空間を満たし、彼女がゆっくりと顔を上げる。"
    nar "陰になった顔と向かい合った時は再び心臓が冷えてしまったが、その濃い目頭に水が曇ってないってことを見てから安心できた。"
    pl "…正直言ってまだ戸惑ってるし、受け入れる準備とか何もなってないけど…{w}俺はこれからも姉さんとは仲良くしていきたいんだよ。"
    pl "今日はただ俺の知らなかった真実について確認したかっただけなんだ。"
    ar "……"
    pl "だから…事実だけを言ってくれた姉さんには逆に感謝してるよ。"
    show SCG_07 10 with fastdissolve
    ar "…許して頂けるのですか、こんな私共めを…"
    pl "許すも何も、はじめから怒ってもいなかったさ。"
    pl "州都で働きたいって言ったのは俺だよ。{w}しかも姉さんや他のみんなに悪意があったワケでもなかっただろ？"
    hide SCG_07 0 with dissolve
    nar "彼女はじっと目を閉じたまま頷いた。{w}俺に答えたより、自分の中で何かを思い切ったように見えた。"
    show SCG_07 0 with fastdissolve
    ar "お望みであらば、何でもお申し付けください。{w}このアルネ・アルタナータ、全力を尽くし貴殿の力となりましょう。"
    nar "声に迷いはなく、姿勢に偽りはなく、視線は俺に向く。{w}その姿を見れば逆に不安になってきた。"
    pl "アル姉は大丈夫か？{w}この話を初めて聞いたときとか、何ともなかったのか？"
    ar "伯父様は私の命の恩人の様なお方です。"
    show SCG_07 7 with fastdissolve
    ar "その伯父様や家門の未来に、不肖者のこの私めが役立てられるのであれば…{w}私にそれ以上の栄光は御座いません。"
    nar "家門の栄光、それを聞くとまた気まずい疑問が思い浮かんだが、わざと聞かないことにした。"
    nar "俺にそういうことを伝える彼女は今日中一番気楽な顔をしていたから。"
    nar "俺には分からなくても、彼女にとって家族への献身は大いなる幸福なのだ。{w}家族か。"
    pl "俺、本当に姉さんの家族になれるのかな。"
    ar "私は確かに、兄弟に出会うまで貴殿の顔も、性格も知り得ませんでしたが…{w}名前だけは最初から聞かされておりました。"
    ar "その名は「兄弟」です。"
    show SCG_07 4 with fastdissolve
    ar "私にとって兄弟は、出会う前から既に私の心の中に新しい家族として根付いておりました。"
    hide screen textbox with dissolve
    hide SCG_07 with dissolve
    pause 1.0
    show screen textbox with dissolve
    nar "二人だけの部屋から出て迎えた外は、相変わらず各自の力を修練する司祭の足音と気合が重なって騒がしく、"
    nar "外に出てからすっきりした心はどこか暗澹としている感じだ。{w}特に裏切られたって感じたことではない。{w}拒否感ってことでもない。"
    nar "しかし彼女から直に話を聞くのが本当に正しい選択だろうか。{w}彼女の親切さにわけを付けることが。"
    nar "やはり今日はツイてねぇな。"
    stop music fadeout 3
    hide screen textbox with dissolve
    pause 2
    $ love_ar = love_ar + 1
    $ day_ar = True
    $ day_time = day_time +1
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_3


label day3_rs:
    show screen place_day3
    show screen place_rs
    with None
    hide screen place_rs
    hide screen place_day3
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    scene bg104 with dissolve
    call place104 from _call_place104_4
    show screen textbox with dissolve 
    play music 'audio/bgm/rose.ogg' fadein 3
    nar "再び尋ねた図書館は昨日と同じく人影は見えなかった。"
    nar "もしかしたらと思い何度も後ろを見てみたが、いきなり話しかけてきた女性の司書も今日は見えない。"
    nar "昨日出会った謎の少女は誰だろう。"
    nar "静かな図書館、隅っこに居着いた小さな扉はもう俺には新しい関心事となって、只通り過ぎるにはあまりにも気にかかる。"
    hide screen textbox with dissolve
    scene bg105 with dissolve
    call place105 from _call_place105_2
    show screen textbox with dissolve
    nar "扉をゆっくり開くと、期待に応じるように、昨日見たあの女の子が目に入った。"
    nar "彼女は本一冊を開いたまま傍に置いて、腹の上に両手をきちんと合わせたままじっと横になっていた。"
    pl "おーい、ローズ、寝てるのか？"
    hide screen textbox with dissolve
    show SCG_12 11 with dissolve
    show screen textbox with dissolve
    rs "きゅうけいちゅう。"
    hide SCG_12 with dissolve
    nar "俺は床に広がった桃色の髪を踏まないように気を付けながら、本を拾った。"
    nar "花と木などの森の風景で彩った黄色い表紙に、簡単に書かれた文。{w}故郷でもたまに見つけられた子供向けの本だ。"
    pl "絵本読むのに休憩が要るって…"
    show SCG_12 idle with dissolve
    rs "人が新たに物語を作るにおいて要る脳の分量はどれくらいだと思うのだ？"
    pl "い、いきなりなんだよ。"
    rs "集計の結果、全体のうち約48％が「脳を使わない」と答えた。{w}哀しくも人間は完成されない物に置いて興味が深まる傾向にある。"
    rs "物語の流れが一本とすると、それ以外の変数を考える事こそが読者のすべきことである。{w}とローズははっぴょうした。"
    pl "まとめると想像は自由…って奴？"
    show SCG_12 8 with fastdissolve
    rs "例1、{w}どうやってお姫様と王子様は再会できたのだろう？"
    pl "え、俺はよくわかんないけど…{w}お互いを忘れてなかったからじゃねえの？"
    show SCG_12 7 with fastdissolve
    rs "例1-1、{w}何故彼らは再会した後涙を流したのか？"
    pl "お互い愛してたから？"
    show SCG_12 idle with fastdissolve
    rs "例2、{w}それでは何故魔女は罰を受けたのだろう？"
    pl "んー…"
    rs "例1-2、{w}二人の間にどうやって愛は存在してたのか？"
    pl "てか最初言ったけど俺、この本読んだことないし内容あんまわかんないって。"
    show SCG_12 7 with fastdissolve
    nar "突然、ローズは言葉を止めて、目玉を回し俺をじろじろ眺める。"
    show SCG_12 idle with fastdissolve
    rs "おまえ…{w}だれ？"
    pl "それ今更聞く？"
    show SCG_12 2 with fastdissolve
    rs "どうやってここにはいった？"
    pl "扉が開いてたから。"
    rs "どうしてローズをローズとよぶ？"
    pl "そりゃあ、お前が昨日お前の名前がローズって言ったろ？さっきも言ったし。"
    show SCG_12 7 with fastdissolve
    rs "理解不能…"
    hide screen textbox with dissolve
    hide SCG_12 with dissolve
    show screen textbox with dissolve
    nar "本を引き返して本棚に差し込んでは部屋を眺め回す。{w}ここって平凡な事務室らしい。"
    nar "壁には金と銀のように輝くトロフィーが埃の付いたままで並んでいて、本棚には本か書類などがいっぱい差し込まれていた。"
    nar "只見ているだけでは落ち着ける場所なのに、床の色とりどりの毛布と座布団が、風景についての感想を濁す。"
    nar "ここが彼女の部屋っていう証拠だ。"
    hide screen textbox with dissolve
    show SCG_12 2 with dissolve
    show screen textbox with dissolve
    rs "おまえ、ここからでてけ。{w}お前は此処に居ては為らない、突然の不法侵入に加え物を触るなど。{w}ローズはあせった。"
    pl "あ…それってそうなるのか。{w}ゴメンゴメン、ここってお前の部屋なのか？"
    show SCG_12 idle with fastdissolve
    nar "不自然に言葉が切られる。{w}すぐ答えればいいことを、俺をじっと見つめたまま瞬きをするだけだ。"
    pl "何でこんなとこに居るんだ？"
    rs "此処は許されし場所だから。"
    pl "もしかして…外に出られないとか？"
    show SCG_12 8 with fastdissolve
    rs "人間には皆それぞれ許されし空間が存在する。{w}おまえはそれがローズより少し広いだけだ。{w}ごうまんになるな。"
    pl "別にそういうのに傲慢になったわけじゃ\nなくって…{w}何でなんだ？誰がそうしろって言った？"
    show SCG_12 2 with fastdissolve
    rs "しつもんがおおい。質問に対し返答を求めるのであれば先に相手の質問に確と答えよ！{w}おまえはだれだ？"
    pl "おぉ、そういえば言ってなかったな。{w}[na]だ。{w}浄化班の光る新入り！"
    pl "間もなく神殿一の人気者になる予定だから俺とここで仲良くなっておいて損はないと思うぜ？"
    show SCG_12 8 with fastdissolve
    rs "傲慢に満ち溢れる人間は良く本人の作り上げた溝に陥って死ぬとされる。"
    pl "俺は謙遜に満ち溢れてるからその心配はいらなさそうだな。"
    hide screen textbox with dissolve
    show SCG_12 idle with dissolve
    show screen textbox with dissolve
    nar "彼女が体を起こしたおかげで、その姿をろくに確認できるようになった。"
    nar "服や状況などを見れば学術部の司祭のようだが、どういう仕事をやっているのか。"
    nar "マヤが言うには、学術部は頭の良い人たちの研究班のようなものらしいが…"
    show SCG_12 8 with fastdissolve
    rs "『浄化班の光る新入り[na]』はなぜここにいる？"
    pl "扉が普通に開いてたし、部屋の主が床に寝っころんだままだったからな。"
    show SCG_12 7 with fastdissolve
    rs "けいかいしんのたりないぬしだな。"
    pl "それな。"
    show SCG_12 8 with fastdissolve
    rs "『浄化班の光る新入り[na]』はなぜここにくる？"
    pl "図書館には本を読みに来たに決まってるだろ。{w}あと光る新入りの称号を認めてもらって嬉しいけど一々呼ばなくていいよ。"
    show SCG_12 2 with fastdissolve
    rs "その答えは大変不適切だ。{w}とローズははんだんした。"
    rs "もしそうとして、図書館で大人しく本でも読んでいれば良い事を何故この空間に入り込んだのだ？"
    pl "質問に質問で返してゴメンけど…{w}その喋り方ってそういうキャラなのか？"
    play sound "audio/se/hit.ogg"
    show SCG_12 3
    rs "質問に質問で返すな！{w}ローズはげきどした。" with sshake
    pl "質問に従順に答えを返してるばっかじゃ面白くないだろ～{w}気になりすぎて思い出してもすぐ忘れちまいそうだ。"
    show SCG_12 2 with fastdissolve
    rs "質問に対する返答の手本を見せよう。{w}これはローズが相手に確とローズの意を伝えるための表現である。"
    rs "感情、言動、意図は確実にしておかねば相手にも伝わらない。{w}それはローズの中でも意味が薄れていく。"
    pl "確かにお前は表情も読み取れないし、あんまり話すようにも見えないからそういうのも要りそうだな。"
    rs "それではローズのしつもんにこたえろ。"
    pl "わーかったって、急かすなよほんと…"
    pl "ここの司書の人にここには好きな時に訪問してもいいって聞かれてたんだけど、"
    pl "あの時偶然会ったお前が面白そうだったから気になって寄ってみただけ。"
    rs "また不適切な返答。"
    pl "お前のお見せした手本も同じようなモンだったろ。"
    rs "ローズはせめて嘘で場を流す様な破廉恥な行為に走ったりしなかった。"
    pl "嘘じゃねえって。{w}これ以上どう説明すりゃいいんだよ～"
    pl "お前は俺のこと忘れてるからそう思ってるんだろうけど…"
    show SCG_12 7 with fastdissolve
    rs "わすれてない。"
    pl "はぁ？だったらさっきは何で…"
    show SCG_12 idle with fastdissolve
    rs "おまえはだれで、なんでここにいるのかに対する返答は、その記憶だけでは導出できないからである。"
    nar "しっかりしながらも外れた答えだな。{w}それが同時にできるなんて、すごい子だ。"
    pl "じゃあもうわかったからいいだろ？{w}俺は浄化部所属の[na]、{w}ここに入ったのは戸締りがなってなかったからうっかり！"
    show SCG_12 8 with fastdissolve
    rs "待て。{w}疑問はまだ数多だが、ローズはその内一番の疑問に対する回答を得ようとする。"
    rs "『おもしろそう』とはどういう意味だ？"
    pl "それは説明が要りそうな部分じゃないと思うけどなあ…"
    rs "説明を要求する。"
    pl "どう言えばいいもんか、うーむ…{w}さっきお前が言ってたアレだよ。{w}人は完成されない物語に興味を惹かれる、だっけ？"
    pl "それは結局物語の穴が人の創造力や、好奇心をくすぐるってワケだろ？{w}それと同じようにお前にも興味がくすぐられたんだよ。"
    show SCG_12 7 with fastdissolve
    rs "それはつまり、ローズはみかんせいと…"
    pl "今のはただの引用ってだけ。{w}そこまで言うつもりじゃなかったが…まあ似たようなモンだな。"
    show SCG_12 idle with fastdissolve
    rs "では…{w}かんせいされるには、あとなにがひつようなのだ？"
    pl "そんなに落ち込まなくていいって。{w}どうしてもどっかしら足りない部分があるのが人なんだしさ。"
    pl "そういう人が完成されるには、他人と出会って会話するのがベストだな。"
    rs "りゆうは？"
    pl "こんなところで一人縮こまってばっかじゃ何も変わらないからだろ。"
    pl "それに、誰かがお前に興味を持ったならそれもチャンスだ。{w}こういう機会はあんま来ないんだよ。"
    rs "ふむ。"
    nar "自分から考えても疑わしい言葉がぺらぺら出てきた。{w}しかしこっちからもまだ気になることは多いし、ここで引くもんか。"
    pl "お前は一日中何をしながら時間を過ごしているんだ？"
    rs "読書。"
    pl "絵本の？"
    show SCG_12 8 with fastdissolve
    rs "不満か？"
    pl "悪いとは言ってないって。{w}一日中本読んでばっかじゃ仕事はいつやってるんだ？"
    rs "しごと？業務か。"
    pl "そう、学術部の司祭としての仕事があるだろ。"
    show SCG_12 idle with fastdissolve
    nar "ここで二度目、答えが断たれてしまう。"
    pl "ちょちょちょ、仕事してないのか？それとも学術部じゃなかったり？"
    show SCG_12 8 with fastdissolve
    rs "仕事はしている、学術部の司祭でもある。"
    pl "じゃあそうと言えばいいじゃんか。"
    show SCG_12 7 with fastdissolve
    rs "そうであるとどうじに、そうではないから。"
    nar "さっきから妙に言葉が短くなっているようだが、もしかしたら対話に集中できないのか。"
    pl "そっか…ここまで来て質問ばっかってのもアレだな。{w}本読んでるって言ったよな？邪魔してゴメンよ。"
    show SCG_12 8 with fastdissolve
    rs "自身の過ちに対する謝罪にはそれに伴う行動で示す必要がある。"
    pl "うっ…余計なこと言っちまったな。"
    rs "謝罪を行動で示すのであれば、四列目一番右側の本を取ってその内容を読むがいい。{w}と、ローズはめいれいした。"
    pl "あ？{w}朗読？{w}朗読しろって？"
    rs "そうだ。"
    pl "うわあ、恥ずかし…"
    show SCG_12 idle with fastdissolve
    rs "おまえは物語を読みながら羞恥を感じるのか？"
    pl "いや、そういう問題じゃなくって…{w}まあいいや、アホらし。{w}読めばいいだろ。"
    hide screen textbox with dissolve
    hide SCG_12 with dissolve
    show screen textbox with dissolve
    nar "それを聞いてまた本棚に近づくと、ふと違和感が浮かぶ。"
    nar "この本棚の本はほとんどが厚い辞書とか専門書なのに、四行だけに童話や幼児向け教本などが差し込まれている。"
    nar "こんなに難しい本だけ読んでいれば、たまには童話でも読んで脳の換気でもしたくなるのか。"
    nar "疲れた脳を読書で休ませるなんて俺にはよく分からない発想だ。"
    hide screen textbox with dissolve
    show SCG_12 idle with dissolve
    show screen textbox with dissolve
    nar "本を取り上げてローズに見せると、彼女は二度か頷く。"
    nar "表紙には海を表現したような波模様が描かれて、横には下半身が鰭になっている姫がいた。{w}俺には初見の本だ。"
    pl "えーっと、{w}遠{cps=*0.1}くの海は美しく…{/cps}{cps=1}青…{/cps}"
    nar "恥ずかしいが、最初の文から絶句だ。"
    nar "童話は子供たちが読む物だって思っていたのに、俺の言語は州都の子供よりも格下ってことだったのか…"
    nar "読めない語を飛ばして読もうとしたが、黙々と俺を見守っていたローズが早くも口を開いた。"
    show SCG_12 10 with fastdissolve
    rs "藍き達磨菊にも似た青さであった。"
    pl "何だ、内容知ってんなら他人に読ませなくたっていいだろ。"
    rs "聞きたかったので聞きたいと言った。{w}言語が分からないのか？"
    pl "…外地出身だから州都の言葉はまだあんまわかんないんだよ。"
    show SCG_12 8 with fastdissolve
    rs "ふうむ…{w}ローズもことばはむずかしい。"
    pl "はあ？"
    show SCG_12 idle with fastdissolve
    rs "言語そのものを読み取る分には不足はないが、頭に入ってもそれはローズの情報とはならない。"
    rs "よって、言語にはまだ慣れていないのだ。"
    pl "…もし慰めてんならそういうのいいから。"
    rs "理解不能。"
    pl "故郷で使ってた言葉と大差ないんだし、ちょっと勉強すれば分かるような気がしなくもないんだけどなあ…"
    show SCG_12 8 with fastdissolve
    rs "ローズはこたえた。{w}勉強しろ。"
    pl "ここ使わせてくれんの？"
    show SCG_12 7 with fastdissolve
    rs "理解不能。理解不能。"
    pl "さっき話の流れ的にそうだったろ。"
    show SCG_12 2 with fastdissolve
    rs "ローズは外部者をこの空間に入れるわけにはいかない。{w}浄化部所属[na]。{w}おまえは外部者である。"
    rs "立ち入りは許可されていない。ここからでてけ。"
    pl "冷たいなあ。{w}はいはい、俺だってそろそろお暇するつもりでしたよっと。"
    show SCG_12 idle with fastdissolve
    rs "バイバイ。"
    pl "挨拶はしてくれるのか…{w}バイバイ。"
    hide screen textbox with dissolve
    hide SCG_12 with dissolve
    show screen textbox with dissolve
    nar "ローズはあの時のように手を振っては、俺が部屋から出ることもちゃんと見ずにすぐ毛布の上に倒れた。"
    nar "まるでねじの緩んだ玩具のようだ。"
    nar "彼女は、本当に人間だろうか。{w}明日また図書館に来れば何かを知り得るかもしれない。"
    stop music fadeout 3 
    hide screen textbox with dissolve
    pause 1
    $ day_rs = True
    $ love_rs = love_rs + 1
    $ day_time = day_time +1
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_3
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
