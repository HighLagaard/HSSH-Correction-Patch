label day2:
    $ day = 2
    if hssh_rkn == True:
        $ save_name = "day 2, 朝, 楽園"
    else:
        $ save_name = "day 2, 朝"
    play sound 'audio/SE/bell 1.ogg' fadein 2.0
    image 2day = Text("day 2",antialias=True, size=48,font="SoukouMincho.ttf")
    show expression '2day' at day00 with slowdissolve
    pause 5
    hide expression '2day' with slowdissolve
    stop sound fadeout 1.0
    pause 1.0
    show screen at_frame with dissolve
    scene bg10 with slowdissolve
    pause 1
    play music 'audio/bgm/daily.ogg'fadein 1.0
    nvl clear
    $ _skipping = True
    $ show_quick_menu = True
    show screen keymap_screen
    show screen textbox with dissolve
    $ _game_menu_screen = 'preferences'
    nar "重たい瞼を開けば朧げな意識と視界に見慣れない白が入り込む。知らない天井だ。"
    nar "所々汚れが目立っていて、少しばかり低い気がしなくもない白い天井。{w}まだまだ全く見慣れない。"
    pl "朝か……"
    hide screen textbox with dissolve
    show screen nvlbox with dissolve
    "\n 途切れ途切れの夢の破片が、醒めきっていない頭の中で漂っては消えていく。{w}ぐっすり眠ってしまっていたようだ。"
    "初日に沢山歩いてしまったのが睡眠にはかえってプラスとして働いたようだ。{w}俺は寝癖のついた頭を掻きつつ辺りを見渡す。"
    "昨日の夜適当にそこらに放り投げたままの服を見ては現実感に段々頭が覚めていく。{w}今日は荷物を片付けておこう。"
    "当然のことながら今日は誰も起こしに来てはくれなかった。{w}初日は昨日だったが、俺にとっては今日こそが初勤務日となるわけだ。"
    et "窓外の状況は昨日とは全く変わりがなくて、本当にちゃんと時間通り起きたのか？と疑問に思ってしまう。"
    hide screen nvlbox with dissolve
    nvl clear
    call place10 from _call_place10_1
    $ show_quick_menu = False
    show screen morning with fastdissolve
    $ renpy.call_screen("morning")
    scene bg15 with slowdissolve
    call place15 from _call_place15
    show screen nvlbox with dissolve
    "\n 寮を出る直前俺は鍵でちゃんと扉を閉めておく。"
    "部屋が指定された日に一緒に貰ったこの鍵は随分小さく、紐なども結ばれてなくてちょっとした隙に無くしてしまいそうな形だ。"
    "俺が扉を閉めるとほぼ同時に隣の部屋の扉が開く。{w}今になっては見慣れただらしのない恰好の金髪の先輩が中から出てきた。"
    hide screen nvlbox with dissolve
    show SCG_102 outfit 1 with dissolve
    show SCG_102 at bounce
    play sound "audio/SE/ding.ogg"
    show screen textbox with dissolve
    lz2 "[na2]ちゃんおっは～"
    pl "は？"

    show SCG_102 0 with fastdissolve

    lz2 "きみ昨日部屋に居なかったよね？{w}何処で遊んでたかわからないけど、初日から夜遊びだなんて大胆だわ～"
    play sound "audio/SE/hit.ogg"
    show SCG_102 3
    pl "大胆なのはそっちだろーが！{w}一体何なんだよ、その恰好…？！" with sshake
    show SCG_102 at bounce
    lz2 "あ、これ？{w}さっき起きたばっかで着替えるのも忘れちゃって…"

    show SCG_102 2 with fastdissolve

    lz2 "てへっ、あたしったらドジ～"

    show SCG_102 0 with fastdissolve

    nar "自身の容姿を見渡した彼女は、その場で一回くるっと回っては雑誌の女がしてそうなポーズを真似る。"
    play sound "audio/SE/hit.ogg"
    nar "何なんだ、この服としての機能が一切ない様な布切れは？{w}州都の女って皆こんなモンなのか？" with sshake
    pl "服を着るって忘れるようなモンだっけ…？{w}わかったから、早く着替えろよ！"

    show SCG_102 2 with fastdissolve

    lz2 "どうどう？似合う？"
    pl "…もういいって。"

    show SCG_102 1 with fastdissolve

    lz2 "あっそ？"
    play sound "audio/SE/hit.ogg"
    nar "俺、完全に弄ばれてるんだな。" with sshake
    pl "昨日俺の部屋に来てたのか？"

    show SCG_102 0 with fastdissolve

    lz2 "隣同士じゃん？挨拶したくってさあ。"
    pl "そうか？{w}昨日は遅くなりたくてなったワケじゃなくて、ただ周りを見回ってたら道に迷っちゃっただけだって…"
    pl "神殿って結構デカいんだな。"

    show SCG_102 1 with fastdissolve

    lz2 "相当お楽しみだったのねえ。いいわいいわ、どんどん見て慣れてきなよ～"
    lz2 "でも今日は遅れちゃ嫌よ？{w}お部屋に遊びに行きたいんだもの。"

    show SCG_102 0 with fastdissolve

    lz2 "あ、あと皆に今日は遅れるって言っといてね？"
    pl "どうして？"

    show SCG_102 5 with fastdissolve

    nar "その一言が一体何がどうして癪に障ったのか、金髪の彼女は目を逸らしつつ自身の後ろ頭を乱暴に搔き乱す。"
    lz2 "ハァ、{cps=*0.5}{size=0} {/size}{/cps}{nw}"
    play sound "audio/SE/hit.ogg"
    extend "{k=-1}―{/k}―……{w}女子には身体が重くて具合の悪いそういう日がたまにあるんです。{w}こーゆーのも教えてあげないとわからないの？" with sshake
    pl "ふうん{cps=*0.1}……わ{/cps}かった、{w}風邪にならないよう服はちゃんと着とけよな！"

    show SCG_102 1 with fastdissolve

    lz2 "アッハハ！"

    show SCG_102 0 with fastdissolve

    lz2 "きみマジで面白い子ね。"
    hide screen textbox with dissolve
    nvl clear
    hide SCG_102 with dissolve
    pause 1
    if hssh_rkn == True:
        scene bg14 with dissolve
    else:
        scene bg14_1 with dissolve
    call place14 from _call_place14
    show screen textbox with dissolve
    nar "先輩の甲高い笑い声を後にしつつ、俺は集合場所へと向かう。"
    nar "ひときわ薄暗いところにある浄化部署はいつも影が掛かっているからか、{w}近づけば近づく程妙に湿気を感じる。"
    hide screen textbox with dissolve
    pause 0.5
    $ renpy.music.set_volume(2, channel="sound")
    play sound 'audio/SE/door slide.ogg'
    pause 1
    show screen textbox with dissolve
    pl "おはようございます。"
    nar "低い変な声が喉から飛び出す。{w}肩に力を入れすぎて喉まで妙になってしまった。"
    nar "辛うじてごにょごにょした声で帰ってくる挨拶が聞こえたが、"
    nar "誰一人顔すら上げないので流石にどこからなのかまでは聞き取れなかった。"
    nar "同じく反射的にこちらへ振り返った奴らもすぐに興味が失せたのか目を避ける。"
    $ renpy.music.set_volume(1, channel="sound")
    hide screen textbox with dissolve
    pause 1
    show screen textbox with dissolve
    pl "おはよう、マヤ！"
    nar "まあ、しょうがないか。{w}取り敢えず見慣れた顔の居る方へと近寄り話し掛けてみる。"
    hide screen textbox with dissolve
    show SCG_02 0 with dissolve
    show screen textbox with dissolve
    my "あっ、[na2]くん…{w}おはよう、昨日はちゃんと帰れたの？"
    nar "しとやかな姿勢で座ったまま顔だけをこちらに向ける、{w}まるで牡丹のようなマヤは今日もやっぱりカワイイ。"
    pl "俺、道を覚えるのは得意って言っただろう？{w}それよりマヤはよく眠れた？ここの枕ってちょっと高くて不便だからな～"

    show SCG_101 0 at left
    show SCG_02 0 at right
    with fastdissolve

    lz1 "ねえ、アンタ一人で来たの？"
    pl "えっ、居たんだ？"

    show SCG_101 2 with fastdissolve

    lz1 "質問に答えなさいよ！{w}あの女は？{w}隣部屋なんでしょう？"
    pl "あの金髪の先輩ならちょっと遅れるらしいぜ。"

    show SCG_101 0 with fastdissolve

    lz1 "ま～た仮病で抜けるつもりね…"
    pl "たまに具合が悪くなるって言ってたぞ。"

    show SCG_101 4 at left with fastdissolve

    lz1 "なわけ！朝の会が面倒な時に使うお得意の言い訳よ。{w}アンタもそれぐらい見抜きなさいよね！怒られるのはワタシなのよ？！"
    pl "てか、まずここの朝は早すぎるんだよ…"

    show SCG_101 0 with fastdissolve

    nar "そう、浄化部の朝は早い。他のどの部署よりもだ。"
    nar "浄化部には修道院での義務教育すら受けられなかった身分の低い子たちが沢山いて、"
    nar "その為主教様が基礎的な知識を教え込んであげる必要があるらしい。"
    nar "なのでまだ幼い司祭たちは他より早めに出勤して教育を受けて、{w}その後からゆっくり他の司祭たちが集まる形になったそうだ。"
    my "わたしはちゃんと修道院出たのになあ…"
    lz1 "ほ～んと、{w}神殿で仕事したいって抜かしてるクセにちゃんとした州都の作法やマナーも学べてない非常識な人間が"
    lz1 "蝿のように集ってくるんだから、ワタシたちみたいな常識人が飛び火を喰らっちゃうじゃない。{w}いい迷惑だわ！"
    pl "……"
    nar "一瞬にして空気が冷める。{w}多分俺が中途半端なところで口を閉じてしまったからだ。{w}そういうつもりではなかったが。"
    nar "俺が気分を悪くしたと思ったのか、{w}マヤが間で不安そうにちらちらとこちらの機嫌を伺う。"

    show SCG_02 7 with fastdissolve

    my "あ、あのね…[na2]くん、{w}おねえちゃんはね、{w}そういう意味で言ったんじゃなくってね…"

    show SCG_101 2 with fastdissolve

    lz1 "何よ！{w}別に間違ったこと言ってないじゃない！ああもう、クソ…"
    hide screen textbox with dissolve
    hide SCG_101
    hide SCG_02
    with dissolve
    show screen nvlbox with dissolve
    "\n ふと窓の外から見える背の高い影と、カツカツと鳴り響く靴の音。"
    "その音に喉の詰まるような沈んだ空気が一変する。"
    "「おはようございます！」{w}勢いよく扉の開く音と同時に、先程の俺へと返されたソレとは段違いに大きい挨拶が部署内に響く。"
    "ゆっくり中へ足を踏み入れる人の姿に、{w}昨日の記憶が脳裏を強打するように過っていく。"
    et "俺はポカンと口を開けたまま挨拶すら返せず、{w}ただその人からまん丸になった目を離せずに居た。"
    hide screen keymap_screen
    $ _game_menu_screen = None
    hide screen nvlbox with dissolve
    show SCG_05 1 with slowdissolve
    play sound 'audio/SE/ding.ogg'
    show SCG_05 at bounce
    pause 1
    show screen textbox with dissolve
    show char_hkq onlayer screens zorder 2 at slowname
    if config.language == "English":
        show hk1_en onlayer screens at slowsay
    elif config.language == "SimplifiedChinese":
        show hk1_cn onlayer screens at slowsay
    else:
        show hk1 onlayer screens at slowsay
    pause 13.0
    hk_q "{color=#000}{size=0}{k=0}みなさぁ～ん、お元気ですかあ？ここ最近、季節に沿わずずう～…っと寒い日が続いてまぁす…～{/k}{/size}{fast}{/color}{nw}"

    hide hk1 onlayer screens
    hide hk1_en onlayer screens
    hide hk1_cn onlayer screens

    if config.language == "English":
        show hk2_en onlayer screens at slowsay
    elif config.language == "SimplifiedChinese":
        show hk2_cn onlayer screens at slowsay
    else:
        show hk2 onlayer screens at slowsay
    pause 13.0
    hk_q "{color=#000}{size=0}{k=-0}みなさんのだあいじなお身体はですねえ、すべて神様がお貸出しになったものなのですよお？ですので、{/k}{/size}{/color}{fast}{nw}"

    hide hk2 onlayer screens
    hide hk2_en onlayer screens
    hide hk2_cn onlayer screens

    if config.language == "English":
        show hk3_en onlayer screens at slowsay
    elif config.language == "SimplifiedChinese":
        show hk3_cn onlayer screens at slowsay
    else:
        show hk3 onlayer screens at slowsay
    pause 8.0
    hide char_hkq onlayer screens
    hide hk3 onlayer screens
    hide hk3_en onlayer screens
    hide hk3_cn onlayer screens
    $ _game_menu_screen = 'preferences'
    show screen keymap_screen
    hk_qns "どうか病気にだけはならないよう～ご自愛くださいませえ…♪"
    nar "ちょっとした身動きでひらひらと舞い上がる長い裾、相反するようにきっちりと結ばれた真っ白の髪…"
    nar "浄化部主教の{color=#ffe594}ハク・エカルラン{/color}。{w}昨晩森の中に居たあの人に間違いない。{w}はず、だが…"

    play sound 'audio/se/memory.ogg'
    hide screen textbox
    scene black
    with fastdissolve
    pause 0.2
    hide SCG_05
    play sound 'audio/SE/ding.ogg'
    scene bgw
    show expression 'cg04.png' with dissolve
    scene black with dissolve
    show screen textbox with dissolve
    pl "なんだかイメージと違うような…？"
    play sound 'audio/se/wake up.ogg'
    if hssh_rkn == True:
        scene bg14
    else:
        scene bg14_1
    show SCG_101 0
    with hpunch
    lz1 "しっ、うるさいわよ！"
    hide screen textbox with dissolve
    show SCG_101 2 at left
    show SCG_05 1 at hkright
    with dissolve
    show screen textbox with dissolve
    nar "忠告されるも時すでに遅し。{w}俺はずっとじまじまと見つめていた彼と目が合ってしまう。"

    show SCG_05 0 with fastdissolve

    nar "昨日と違って、ゆったりとした目線と速度で。"
    hide screen textbox with dissolve
    hide SCG_101
    show SCG_05 0 at center
    with dissolve
    show screen textbox with dissolve
    hk "あぁ…そういえば～そうそう、"
    hk "よいお知らせですがあ…{w}昨日から、新しく兄弟姉妹のお二方が我々とご一緒することになりましたあ。"
    hk "こうやって面と向かい、直接ご挨拶するのははじめて……"
    show char_hk onlayer screens at slowname


    show SCG_05 1 with fastdissolve

    hide char_hk onlayer screens
    hide char_hk
    extend "ですよね～？"
    hk "昨日は急用で席を外してしまい、大変申し訳なかったのですぅ…"
    hide screen textbox with dissolve
    show SCG_05 0 with dissolve
    show screen textbox with dissolve
    nar "無理してか細く高い声を絞り出しているような微妙な低い声。"
    nar "ゆったりとした口調に曖昧な発音までが合わさったお陰でどう頑張っても聞き取りにくい。"
    nar "彼の仕草とは真逆に室内あちこちからの目線は鋭く、素早く突き刺さる。"

    show SCG_05 1 with fastdissolve

    hk "それではお二方～{w}お集まりの先輩のみなさんへご挨拶を、ど～うぞ…♪"
    hide screen textbox with dissolve
    hide SCG_05 with dissolve
    show screen textbox with dissolve
    nar "俺は全身を舐め回すように巡る気まずさを振り払うかのようにわざと小さく咳き込んだ。"
    nar "さっきみたいな変な声が出ないといいけど。"
    pl "[na]です。ここからはちょっと離れた地方から来ました。{w}正直神殿…っていうか、州都自体初めてなので何が何だか…"
    pl "まあ、研修期間終わったら他の部署に移されるかもとは聞いたけど、{w}取り敢えずそれまではよろしくな。"
    nar "首を傾げたまま聞いていた主教は一拍遅れて拍手を送る。{w}俺はもしかして、何か言い間違えてしまったのか？"
    nar "俺は別にいいけど……"



    show SCG_02 7 zorder 0 with dissolve


    extend "次の彼女が心配だ。"
    nar "横目に確認すると、やはりマヤは全身が凍ったようにガチガチになっちゃってて、{w}自分の指先ばっかりを見つめている。"

    show SCG_02 5 with fastdissolve

    lz1 "ゴホン！"
    show SCG_02 at huruhuru
    my "ひぃ…"
    nar "沈黙が続く前に彼女の姉が先に手を打つ。"

    show SCG_02 7 with fastdissolve

    nar "震える脚でやっと起き上がって、{w}それでも顔すら上げられないままのマヤは見ていられない程可哀想に思えた。"
    nar "こんなの、まるで生まれたばかりの小動物だ。"

    show SCG_02 0 with fastdissolve

    my "マヤ…{w}エルベットです…{w}よろしくおねがいいたします…"
    show SCG_05 1 at in_right
    hk "まあ！エルベット姉妹なんですね～{w}かわい～"
    show SCG_05 1 at out_right
    nar "先程とは違って何人かが拍手を送る音が聞こえてくる。{w}それは歓迎の声と言うにはあまりにも嘲笑の籠った音だった。"
    hide SCG_05
    nar "そしてそれは多分、マヤではなくその隣の人へと向けられたものだった。"

    show SCG_02 3 at huruhuru, right
    show SCG_101 0 at left
    with fastdissolve

    my "…うぅ…"

    show SCG_101 4 with fastdissolve

    lz1 "クソッ…何なのよ…処理班の奴らが皆こっち見てるじゃない…"

    hide SCG_02
    hide SCG_101
    with fastdissolve

    nar "いつも堂々と顔を上げたまま人を接してきた彼女だが、{w}今回ばかりはその俯いた顔を上げられることはなかった。"
    nar "誰にも聞こえないよう小さな声で{w}先程からずっと誰もいない方向に向かってブツブツと悪態をついている。"
    hide screen textbox with dissolve
    show SCG_05 1 with dissolve
    show screen textbox with dissolve
    nar "そんなことにも気付いていないのか、{w}ニコニコしていた主教がまた口を開ける。"
    nar "多分普段もこういった空気の読めない性格が人を散々苦しめているんだろう。"

    show SCG_05 0 with fastdissolve

    hk "それではお二人、是非今後も頑張ってください♪"
    hide screen textbox with dissolve
    hide SCG_05 1 with dissolve
    show screen textbox with dissolve
    nar "その後主教が説明し始めたのは歴史に関するものばかりだった。"
    nar "神託を得た人間、{w}聖痕の発現、溜まったまま腐っていく海の話や、{w}人が生きることの出来なくなった不毛地の話…"
    nar "途中で居眠りしなかっただけで偉いと思えるぐらいだ。"
    hide screen textbox with dissolve
    show SCG_05 1 with dissolve
    show screen textbox with dissolve
    hk "他人の為のことは、我らが父なる神の為のことでもあります。{w}父は常に我々を見守り…"
    hide screen textbox with dissolve
    show SCG_05 5 at hkright
    show SCG_03 72 at left
    with dissolve
    show screen textbox with dissolve
    sc "主教様、そろそろ会議のお時間が…"

    show SCG_03 7 with fastdissolve

    nar "そんな主教の悪意なき{rb}あ{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}り{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}が{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}た{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}い{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}お{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}説{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}教{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}に割り込み止める人。"
    nar "それは大きい声ではなかったものの、状況を変えるには充分だったようだ。{w}主教様もびっくりしたのか一瞬目を丸くする。"
    hk "あらあらまあまあ、{w}わたくしったらまたまたすっかりぽっかり……"

    show SCG_05 1 with fastdissolve

    hk "それではぁ、{w}新入員のお二方に先輩の皆様は色々教えてあげてくださいねえ。"
    hk "お二方も、先輩の言うことはちゃんと聞いておくのですよぉ。{w}何か気になる点がございましたら、お気軽にお尋ねくださいねえ。"

    show SCG_05 1 at center
    hide SCG_03
    with fastdissolve

    hk "何か質問はございますでしょ～か～？"
    nar "一瞬の静寂、その刹那にまた割り込むようにして奴が口を開く。"
    hide screen textbox with dissolve
    show SCG_05 1 at hkright
    show SCG_03 0 at left
    with dissolve
    show screen textbox with dissolve
    sc "なさそうです。"

    show SCG_05 0 with fastdissolve

    hk "ではでわ、今日も互いに愛し合いましょ～"
    hide screen textbox with dissolve
    hide SCG_05
    hide SCG_03
    with dissolve
    show screen textbox with dissolve   
    nar "主教様がゆっくりと歩き出すと、その後ろに付くシーキュレットは黒いベールを被っていった。"
    nar "主教という人はやはり不思議な挙動で外へと出て行く。"
    nar "まるで自分の意思ではないような、{w}見えない糸のようなものに関節ひとつひとつが引っ張られて行ってるように見えるというか…"
    nar "今でも倒れそうで、{w}それを受け止めてくれる人が一人要るんじゃないかって思えるぐらいだ。"
    nar "その証拠として現にシーキュレットはこちらには全く目線も向けず、"
    nar "ただひたすら主教様の背中ばかり見つめながら一緒に出て行った。"
    nar "扉が閉まり、{w}二つの靴音が遠のくと約束でもしたかのように浄化部内はいつも通りの騒がしさを取り戻し始める。"
    hide screen textbox with dissolve
    show SCG_02 0 with dissolve
    show screen textbox with dissolve
    pl "な～んかゆるい人だったな。"
    my "確かに、話に聞いてたのとはちょっと違うかも…"

    show SCG_02 6 with fastdissolve

    my "喋り方もそうだし、お花畑のおひめさまみたいだったね。"
    pl "女だっけ？"

    show SCG_02 0 with fastdissolve

    my "そうらしいよ…"

    show SCG_02 0 at right
    show SCG_101 0 at left
    with fastdissolve

    lz1 "白髪のクセに主教の座にいるなんて面白いわよね。"

    show SCG_101 3 with fastdissolve

    lz1 "もっと面白いこと教えてあげようか？天下りなのよ、あの女。"
    pl "それってどういう意味なんだ？"
    nar "俺が話に食い付くと、先輩の目が光る。{w}さっきまでの元気のなさはどこへ行ったのか意気満々のご様子だ。"
    nar "他人の噂話ってそんなに面白いんだろうか？"

    show SCG_101 0 with fastdissolve

    lz1 "枢機卿の娘なの。{w}だからあんな適当やってても皆うんともすんとも言えないのよ。"

    show SCG_101 3 with fastdissolve

    lz1 "ワタシたちなんかこんなところに勝手に入れられて死体なんか磨いてばっかなのに、いいご身分よねえ～"

    show SCG_101 0 with fastdissolve

    lz1 "あ、そうそう。アンタたちこういう話はワタシたちの間だけにしといてよね。"
    lz1 "特にあのウザ男の前では気を付けなさいよ。"

    show SCG_02 6 with fastdissolve

    my "シーキュレットくん？"

    show SCG_101 2 with fastdissolve

    lz1 "あんなヤツの名前なんか覚えなくていいわよ！"

    show SCG_02 3 with fastdissolve

    my "あうぅ…"
    hide SCG_02
    show SCG_101 0 at center
    with dissolve
    nar "やっと声に出したはいいが、その一喝にまた可哀想なマヤは口を閉じてしまう。"
    nar "この姉妹は仲がいいのか悪いのか。"
    nar "ずっと見てるだけ、というのも何だったので{w}またマヤになにかとやかく言う前にこちらへと興味を逸らさせる。"
    pl "なんで？"
    show SCG_101 at bounce
    lz1 "アイツが処理班の中じゃ一番主教様のこと嫌いだから。"
    lz1 "主教様の名前が話題に上がるだけで嫌がるんだもの。"
    pl "えっ、マジで？さっき一緒に出てったのに？"
    lz1 "{rb}取{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}り{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}敢{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}え{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}{rb}ず{/rb}{rt}{size=28}{k=16}.{/k}{/size}{/rt}彼は補佐教だからね。"

    show SCG_101 3 with fastdissolve

    lz1 "経歴が足りないから臨時らしいんだけど、多分アイツも主教を狙ってるんじゃない？"

    show SCG_101 0 with fastdissolve

    lz1 "……とにかくほんっとメチャクチャよ。こんなドブネズミの巣窟なんか、早く潰れちゃえばいいのに。"
    pl "補佐教は何なんだ？"

    show SCG_101 2 with fastdissolve

    lz1 "もう、いい加減にしなって！アンタ自分で調べるってことも出来ないの？！"
    pl "お前、そんな怒ってばっかだとすぐ老けるぞ…"
    play sound "audio/se/hit.ogg"
    lz1 "ああああもう！" with sshake
    hide screen textbox with dissolve
    hide SCG_101 with dissolve
    show screen textbox with dissolve
    nar "「先輩って大変そうよね～」"
    nar "二人の女性の通りすがりの声にプツンと糸が切れたように小さい先輩の動きが止まる。"
    nar "「私も妹と一緒に仕事してみたいな～」"
    nar "「…―って居るの？」"
    nar "「{k=-2}―{/k}―…あはは！…」"
    hide screen textbox with dissolve
    show SCG_101 2 with dissolve
    show screen textbox with dissolve    
    nar "耳をよく傾けていなけりゃ聞こえもしないはずの会話。{w}しかし彼女はその些細な会話一つで耳まで真っ赤になってしまっている。"
    nar "どうやら堪忍袋の緒が切れてしまったらしい。"

    show SCG_101 4 with fastdissolve

    nar "彼女は怒りが抑えきれないのか、{w}椅子に向かって八つ当たりの蹴りを何度か入れては息を荒くしながらこちらをカッと睨み付ける。"
    play sound "audio/se/hit.ogg"    
    lz1 "アンタたちと居るからワタシが恥をかいちゃうじゃない！{w}鬱陶しいんだって言ってるのが分からないの？！" with sshake
    hide screen textbox with dissolve
    hide SCG_101 with dissolve
    show screen textbox with dissolve
    nar "そうやって声を荒げた彼女は、{w}鬼の様な面相で足を踏み鳴らしながら外へ出て行ってしまう。"
    nar "俺は良いけどマヤまで置いて行ってしまうなんて…{w}マヤは暗い顔で項垂れる。"
    hide screen textbox with dissolve
    show SCG_02 7 with dissolve
    show screen textbox with dissolve
    my "今日、どうしよ…"
    my "お姉ちゃんたちもいないし…{w}今日はキューくんも朝早くから行っちゃったし…"
    pl "落ち着けって、マヤ…{w}基本的な説明は聞いたんだし昨日みたいにだけやっとけばどうにでもなるって。"
    pl "もし何かやらかしちゃってもそれは俺たちを放置した先任たちの責任だし、{w}新入りに責任を問う人なんかいないって！"

    show SCG_02 0 with fastdissolve

    my "そ…そうかなぁ…{w}うぅ…わたし、一人になっちゃうと頭真っ白になっちゃうの……"
    nar "俺が適当に誤魔化しようとした言葉で、マヤの不安を少しは取り除いたようだ。{w}単語もなんとか間違えなかったようだ。"
    hide screen textbox with dissolve
    nvl clear
    show screen nvlbox with dissolve
    "\n 俺はもともと、どちらかといえば人に心を遣わない方だが、{w}またマヤが泣いてしまうことだけはなんとしても避けたい。"
    "その理由は自分でもはっきりと分からなかったが、同時に単純で明確でもあった。"
    "それはつまり、「困る」。{w}相手がマヤじゃなく他の人であっても、また泣いている女の子を励まさないといけない状況に至ることはゴメンだ。"
    et "多分それはマヤにも同じだろう。{w}俺は生まれて初めて、今、退屈な平和が続くことだけを本気で願う。"
    nvl clear
    "\n 他のやつらに目を移る必要もなく、{w}書類挟みはこの部署で一番目立つところに差立ててあった。"
    "その中で、俺らの名前が書いてあった書類挟みも置いてあった。"
    et "二つの書類挟みにはそれぞれ薄い書類が一枚ずつ入れてあって、{w}場所と日付、{w}簡単な仕事の内容だけが書いてあるだけ、分かり難いことは無かった。"
    hide screen nvlbox with dissolve
    show screen textbox with dissolve
    pl "マヤ、これの内容はわかるか？"

    show SCG_02 7 with fastdissolve

    my "うん、多分…"

    show SCG_02 0 with fastdissolve

    my "この書類…毎日新規のものを貰うんだよね、誰が入れてるんだろう…？"
    pl "どうだろうな、多分主教様なんじゃね？"
    my "すごいなあ…"
    hide screen textbox with dissolve
    stop music fadeout 3
    hide SCG_02 with dissolve
    nvl clear
    pause 1
    scene bg00 with slowdissolve
    pause 1
    if hssh_rkn == True:
        scene bg13 with dissolve
    else:
        scene bg13_1 with dissolve
    call place13 from _call_place13_1
    show screen nvlbox with dissolve
    play music "audio/bgm/dialogue.ogg"
    "\n 憂えたことは起きなかった。{w}俺らを待っているのは、気合の入れ顔負けの簡単な仕事だった。{w}汚れた家を掃除することだけ。"
    "反吐が出ることが無かったとはいえないが、{w}昨日のことと比べれば、綺麗だ、と思えるほどだった。"
    et " マヤと二人でいる間はたまに昨日のことを思い出す。"
    nvl clear
    "\n マヤは仕事が下手だ、それだけは事実だ。"
    "床を掃くことだけはなんとかできるように見えるが、{w}動きが鈍いせいだかそれ以上は見難い。"
    "拭き掃除の後は床に足跡、{w}窓の拭き方も知らなくうろうろ。{w}何事も二回はやり直すせいで、きっと簡単なはずなのに時間が結構かかる。{w}で、マヤの仕事が終わっても、その全てを手伝った俺の仕事が渋滞してしまった。"
    et "暗雲垂れ込めてくる天気と一緒に、彼女の顔色も真っ青になっていく。"
    hide screen nvlbox with dissolve
    show screen textbox with dissolve
    pl "…戻るか！"

    show SCG_02 0 with fastdissolve

    my "えっ？"
    pl "俺の仕事なんてもう一回戻ってからやればいいんだし、{w}そろそろ曇ってきたのにマヤをずっと待たせるのも申し訳ないだろ？"

    show SCG_02 7 with fastdissolve

    my "そ、そういうことならわたし一人で帰れるよ…{w}[na2]くんの二度手間になっちゃう…"
    pl "大丈夫だって！{w}俺もちょっと休憩を頂きたかったとこだし。{w}な？"

    show SCG_02 0 with fastdissolve

    my "…うん…"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    nvl clear
    pause 1
    scene bg00 with slowdissolve
    show screen textbox with dissolve    
    my "あ…"
    play sound "audio/se/doro.ogg"
    pause 0.1
    stop sound fadeout 2
    nar "突然降ってきた雨のせいだ、帰り道が泥道になった。"
    nar "結構深い溝だ、足を踏み出せば容赦なく泥に溺れてしまうだろう。{w}俺は泥を掻き分ける感じでなんとか進められたが、"
    nar "後ろで追いかけていたマヤは一歩も動けず、不安そうにあたふたとしている。"
    pl "大丈夫か？マヤ。{w}あんまり焦ると転んじゃうかも知れないから気をつけて…"
    pl "ほら、手貸すから！"
    hide screen textbox with dissolve
    nvl clear
    if hssh_rkn == True:
        scene bg13 with slowdissolve
    else:
        scene bg13_1 with slowdissolve
    show screen nvlbox with dissolve
    "\n 俺は不安がるマヤの両手を取る。{w}恥ずかしがり屋の彼女は呻きと一緒に目をくりくりさせるが、すぐ俺の手にその指をかけた。"
    "溝を掻き分けるマヤは足を踏み出して、{w}たまに立ち止まり足首を遅く動かした。"
    "彼女がショートブーツを履いているせいだ。{w}浄化部の人が長くて重みのあるブーツに拘ることには理由がある。"
    "時間はかかったが、二人とも無事で乾いた地を踏む。"
    et "無事とはいえとんでもない様で、{w}靴は勿論、キャソックの裾までくっついた泥は地団太を踏むだけでは払い落とせなさそうだ。"
    hide screen nvlbox with dissolve
    nvl clear
    show screen textbox with dissolve
    my "……"
    hide screen textbox with dissolve
    show screen nvlbox with dissolve
    "\n 一足遅れて地を踏んだマヤの顔色が真っ青だ。{w}容態を見ると彼女の真っ白のニーソックスも俺と同じく黒い泥で濡らされている。"
    "長く握っていた訳でもないのに、マヤの手を取った方の手が少し痺れる。{w}きつい仕事のせいでいつも綺麗で薄い指に、ちらほらと、さっきの汚れが残っていた。{w}それに気づいた彼女は口をつくんで震える。"
    "「ごめんなさい、[na2]くん。」"
    et "そして又、謝った。"
    nvl clear
    "\n ここに来る間ずっとマヤは誤ってばかりで、それ以外は何も言わない。{w}俺は彼女が「迷惑をかけている」とか、{w}「不愉快だ」とは全く思っていない。{w}でも彼女はどうしてもそうとは思わないのか、{w}俺の答えを聞いてからもっと俯くだけだ。"
    "俺の答えが只、{w}彼女をもっと苦しめるだけだった。"
    "溝から出ても靴の中の泥が邪魔なのは俺にとっても全く同じだ。{w}できれば大股に歩いて、一分も早く靴を脱ぎ捨てたい。"
    et "だが、途中で休むことなく俺についてくるマヤがしおらしく、{w}俺はそれに合わせて歩きを緩めることにした。"
    hide screen nvlbox with dissolve
    nvl clear
    stop music fadeout 3
    pause 2
    if hssh_rkn == True:
        scene bg01 with dissolve
    else:
        scene bg01_1 with dissolve
    call place01 from _call_place01_2
    show screen textbox with dissolve
    nar "神殿に至ると、なぜか通路の方にまばらに人が集まっていた。"
    nar "この時間の通路はいつも騒がしいらしいが、今日はどうしてか誰もが二階の階段の上へ視線を向けていた。"
    hide screen textbox with dissolve
    show story05 with slowdissolve
    pause 2
    play music "audio/bgm/golden haku.ogg"
    show screen nvlbox with dissolve
    "\n 視線を追って頭を上げると、多くの司祭と、俺らの足を止めさせる風景がそこにあった。"
    "ヘンテコな装いの三人が列になって階段を下りる。"
    "その姿が現れると、まるで規則でも決まっているように、{w}司祭の皆が頭を下げ、手を合わせた。"
    "俺はこの現象が疑わしく、隣のマヤに目を向けたが、{w}いつの間にか彼女もそっと頭を下げていた。"
    "異質だ。{w}だけど、この中で俺自身こそが一番異質だ。{w}そう思いつつ俺もなんとか頭を下げ、他人の真似をする。{w}俺は横目で前を通る人を見分けてみる。"
    "一番前の人が俺の故郷に尋ねた背の低い男、{w}その後ろがグレーテ先生と一緒にいた人、{w}最後に浄化部の主教様…"
    et "一、二、三…"
    hide screen nvlbox with dissolve
    nvl clear
    show screen textbox with dissolve
    pl "一人足りなくね？"
    my "うぁ？"
    nar "その行列が通り過ぎたばかりの頃、俺は頭を下げ、{w}マヤに違和感について伝える。"
    nar "マヤはこっちを見つめて、腰を屈めたまま手をのろのろしながら人数を数えた。"
    hide screen textbox with dissolve
    pause 1
    stop music fadeout 3
    hide story05 with slowdissolve
    pause 1
    show SCG_02 0 with dissolve
    show screen textbox with dissolve
    play music "audio/bgm/dialogue.ogg" fadein 3
    my "多分、学術部の主教様じゃないかなあ…"
    pl "そういえばそこの話だけはあんま聞いたことない気がするな。"
    my "えっとね、{w}遺物の解読だったり研究をするとこなの。{w}すっごく頭のいい人だけいけるんだって。"
    pl "へえ、そうなんだ。"

    show SCG_02 7 with fastdissolve

    my "うん…"
    my "…うちのおねえちゃんね、{w}実は学術部希望だったんだって…{w}でも何年勉強してもダメで…"

    show SCG_02 0 with fastdissolve

    my "あ……{w}この話、おねえちゃんの前ではしないでね。{w}わたしまた怒られちゃう…"

    show SCG_02 5 with fastdissolve

    ex5 "そこの処理班！{w}ボーっと突っ立ってないで早くシャワー室にでも行きな。"
    nar "司祭が通りながら伝えた言葉で俺ら二人はすっかり忘れていたことを思い出す。{w}ズボンの裾にくっついた泥がもう乾いたままだ。"
    nar "同じく自分の足を見下ろしたマヤの顔が、{w}あっという間に真っ赤に染まる。"

    show SCG_02 6 with fastdissolve

    my "あ、{w}あの、わた、{w}わたし先にシャワー室行ってくるね…"
    my "[na2]くんも早く行ってから着替えてね。"
    pl "マヤ、今日は早めに帰っちゃうのか？"

    show SCG_02 0 with fastdissolve

    my "…わかんない…"

    show SCG_02 6 with fastdissolve

    my "…ごめん、そろそろ本当に行かなきゃ…"
    pl "ああ…{w}帰り、気を付けろよな。また後でな！"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    show screen nvlbox with dissolve
    "\n マヤは急いで抜け出すも、{w}どうやら足跡が残ることが気になったせいだろうか、{w}奥まったところでゆっくりと進んでいった。"
    "俺はマヤが泥だらけになろうがぼろだらけになろうがかなんて構わないが、{w}彼女にはそうでもないだろう。"
    et "神殿の中に一つ、寮に又一つ。{w}シャワー室が二つに分けてある部署は浄化部だけらしい。"
    nvl clear
    "\n 時間が時間だからか、人の肌の色だけで満ちたシャワー室はどう見ても忌まわしい。{w}ともかく長居するところではない。{w}シャワー室の湿っぽい空気と肺を押さえつけるような息苦しさが、{w}さすがに気に食わないんだ、俺は。"
    "特にこの「ジャグチ」ってやつは全く分からない。{w}お湯は熱すぎるし、水は冷たすぎる。"
    et "これからも何度も来ないといけないのにもううんざりだ。"
    hide screen nvlbox with dissolve
    nvl clear
    stop music fadeout 2
    pause 1
    if hssh_rkn == True:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03_3
    play music 'audio/bgm/daily.ogg'
    show screen nvlbox with dissolve
    "\n 俺が急ぎすぎたか、食堂にマヤの姿は見えない。{w}彼女と一緒についている先輩の二人はもうあそこに席を取ったのに、シャワーが長びいているのだろうか。"
    "俺の立っていた入口に、人波が繰り込む。"
    "一つ二つと、空席に人が座る度にかび臭い空気が漂う。{w}水浴びや洗濯なんかじゃあ剥がしきれない獣特有の死臭。{w}ここの人にはいつもそんな匂いがついていた。"
    et "人は口を合わせ「一生慣れない匂い」とは言っているが、もう慣れたように見える。{w}俺はそれがあまり気に食わない。{w}\nいずれかこの不快感も俺の日常になるだろう。"
    nvl clear
    "\n ごたつく頭中から自然とマヤを思い出す。"
    "泥だらけのブーツを履いて、恥かしそうにスカートをしわくちゃにした姿が見える。{w}相変わらず彼女のことが心配だ。自分で考えても可笑しいほど。"
    "彼女にも笑顔の時はあるのだろうか。{w}当然と言えば当然だが、{w}俺の記憶の中のマヤは、まだ憂鬱な顔で頭を下げている。{w}なんとなく思いついたイメージが段々と形を組み立て始める。{w}マヤの姿はまだ見えない。"
    "今日の飯は抜く気なんだろう、なぜかそういう確信をして、自分の分が無くなるまえにパンを何個か取る。"
    "どうやら俺は彼女に会いたいらしい。{w}理由は分からない、が。{w}かび臭さが俺の鼻先にくっついて離れようとしない。"
    et "今後迷わないためにもこの神殿の構造についてしっかり覚えておこう。"
    hide screen nvlbox with dissolve
    if hssh_rkn == True:
        $ save_name = "day 2, 昼, 楽園"
    else:
        $ save_name = "day 2, 昼"
    jump placemenu
    return



label day2_my:
    show screen place_day2 
    show screen place_my
    with None
    hide screen place_my
    hide screen place_day2 
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg05 with dissolve
    else:
        scene bg05_1 with dissolve
    call place05 from _call_place05_1
    play music 'audio/bgm/maya.ogg' fadein 3
    show screen textbox with dissolve
    nar "庭に出ると、馴染みのある姿が見えた。{w}マヤは膝を抱いてベンチに座っている。"
    nar "話しかけようとしたが、その前に足元から小石の音がした。{w}そのせいでマヤは体を竦めてこちらを見る。"
    nar "驚いたのは俺も同じで、両手を一気に挙げてみる。{w}大きくなったマヤの目もそれを見て和らぐ。"
    nar "その姿を見ると俺もなぜか安心してしまう。"
    hide screen textbox with dissolve
    show SCG_02 0 with dissolve
    show screen textbox with dissolve
    pl "マヤ！ここにも居なかったらどうしようかと思ったぜ。{w}ご飯はちゃんと食べたか？"
    my "ううん、今日はおねえちゃんたちも居なかったし…{w}なんか、食欲湧かなくて…"
    pl "いいのか？"

    show SCG_02 7 with fastdissolve

    my "大丈夫、もう慣れてるから…"
    nar "慣れているって、こんなことがよくあるってことなのか。"
    nar "俺は答えの代わりに、食堂で持ってきたパンを一個マヤに見せた。"
    nar "本来他の材料が入っているはずのコッペパンから、まだ暖かいバターの匂いがした。"
    nar "マヤは又驚いた目をする。{w}さっきとは違って少しずつ震えている。"

    show SCG_02 0 with fastdissolve

    my "…わざわざ持ってきてくれたの…？"
    pl "その……{w}何となく、食べてないだろうな～って思って…"
    pl "俺もここで食うついでに幾つか持ってきたんだ。{w}何も食べないよりかはマシだろう？"

    show SCG_02 6 with fastdissolve

    my "……"
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    show screen textbox with dissolve
    nar "彷徨うように見えたマヤの手がパンを一つ持っていく。"
    nar "小さな口がこっそりパンを食いつく姿はなんとなく可哀そうだ。{w}丸く固まった姿勢もいつの間にか和らいでいた。"
    nar "俺も隣に座ってのんびりと視線を前へ移る。"
    nar "花壇とはいえ目立たないくらいで、{w}俺が見るにここは多分、蔓薔薇の庭だろう。"
    nar "垣を巻き付けた蔓に、真っ赤な薔薇がふさふさ咲いた姿は、"
    nar "手入れがちゃんとできていないせいだろうか、{w}半分以上が萎れて、壮観とは言えない。"
    nar "最初に見つけたときは他でもなく浄化部にこんなに華やかな場所がついていることに違和感しか感じなかったが、"
    nar "今のこの薔薇の墓には同質感を感じる。"
    nar "だがマヤの気に入ったものは満開した薔薇でも、垣でもなく、{w}花壇だった。"
    nar "とても小さくて花を見ようとするにはしゃがみ込むしかないし、{w}花さえも今は咲いていない。"
    nar "まぁ、ここに座ってみて分かったが。{w}ここからはマヤの気に入りの花壇がよく見える。"
    nar "マヤの顔もいつもより一段気楽そうだ。{w}まるで雑草のような若芽は、花が咲くにはまだ足りないだろう。"
    hide screen textbox with dissolve
    show SCG_02 0 with dissolve
    show screen textbox with dissolve
    pl "マヤは、マヤのお姉ちゃんとは仲が悪いのか？"

    show SCG_02 5 with fastdissolve

    my "えっ…？"

    show SCG_02 7 with fastdissolve

    my "ど…どうしてそういう…"
    nar "突然の質問にマヤの表情が又固まる。彼女をいじめるつもりではない。{w}むしろ逆だ。"
    pl "どうしてってそりゃあ…"
    pl "昨日もマヤを放っぽったまま行っちゃったし、先輩なのにあんまり教えてくれるわけでもなかったし。"
    pl "今もほら、マヤはここで一人ぼっちだろ？"
    pl "…他人の家庭事情に首突っ込んでゴメン、{w}でもなんか見てられなくってさ。"

    show SCG_02 0 with fastdissolve

    my "…ううん、いいの。{w}わたしもう知ってるから…"

    show SCG_02 8 with fastdissolve

    my "おねえちゃんはね、{w}ちょっとだけ心配症で、{w}でもだから色んなことをいっぱい教えてくれるようないい人なの。"
    my "おねえちゃんがわたしに冷たいのは……{w}役立たずで、{w}面倒くさいわたしに呆れちゃったからなんだと思う…"

    show SCG_02 7 with fastdissolve

    my "だってわたしもそうだもん…"
    pl "…"

    show SCG_02 0 with fastdissolve

    my "それと…{w}[na2]くんがわたしのことを心配してるってこともちゃんとわかってるよ。"
    pl "えっ？{w}い、いや、まあ…{w}そんなに落ち込んで蹲ってたら誰だって心配するだろ？"
    my "…そう…だよね…うん。"

    show SCG_02 8 with fastdissolve

    my "…心配かけちゃってごめんね、{w}でももう本当に気にしなくてもいいから…"
    nar "ここで俺は考える。"
    nar "もしここでもっと気まずくなっても、泥だらけの女の子に「大丈夫」ってちゃんと返したほうが正解だったのではないかと。"
    nar "彼女が俺の話を聞かなかったのは、そこに混じるべきたった俺の本心が曖昧だったからではないかと。"
    pl "そんな毎回謝らなくてもいいって。"
    pl "他の人の考えなんて俺にはわからないけど…"
    pl "せめて俺は面倒くさいだなんて思ったことないし、{w}マヤがいつも頑張ってることくらい…知ってるからさ。"
    pl "どっちかというとそういうマヤの力になりたいだけなんだ、{w}俺の前では謝らなくていいんだぜ。"
    nar "何度も考えても俺の決断はまだ曖昧な状態で足踏みだ。{w}それに、本人の前では最初のように言葉が狂ってしまう。"
    nar "静寂が続いて、俺に後悔のような感情が打ち寄せるところだった。"

    show SCG_02 0 with fastdissolve

    my "…ヘンなの……"
    my "わたしなんかと一緒にいてもつまらないだけなのに…{w}[na2]くんはずっと一緒だったからわかるでしょ。"
    my "そんなこと言われたの、初めてかも…"
    my "[na2]くんってヘンなの。"
    pl "うっ…"
    pl "ヘンじゃないって…可笑しいのはお前の周りの奴らだよ。{w}人を目の前で無視したりさ…そういうの良くないと思うんだ、俺は。"

    show SCG_02 6 with fastdissolve

    my "……"
    nar "しまった、どれだけ俺が理解できない相手だといえ、ともかくマヤの知り合いだ。{w}本人の前で陰口をたたくと不愉快だろう。"
    pl "あっ、ゴメンな、今のはそういう意味で言ったんじゃなくて…"
    my "ありがとう。"
    nar "ひょっとすれば聞き流してしまうほどの小声。"

    show SCG_02 1 with fastdissolve

    my "心配してくれて、ありがとう…"




    show SCG_02 6 zorder 0 with newfastdissolve



    extend "次からはこう言った方がいいのかな？"
    pl "…え…ああ、うん。{w}そっちの方が断然いいと思うぜ。"
    nar "彼女は口元を少し上げて微笑みを見せた。{w}が、決して明るい笑みではない。"
    nar "頭の中で描いた姿とは違って、燻った虚しささえも感じられる。"
    nar "本心ではないかもしれない、思ったよりは嬉しくないかもしれない。"
    nar "だが微笑みとは言えないその微細な表情を、{w}俺は多分忘れられないだろう。"
    stop music fadeout 3
    hide screen textbox with dissolve
    hide SCG_02 with dissolve
    pause 2
    $ day_my = True
    $ day_time = day_time +1
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with slowdissolve
    else:
        scene bg02_1 with slowdissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_2
    return


label day2_rs:
    show screen place_day2
    show screen place_rs
    with None
    hide screen place_rs
    hide screen place_day2
    with dissolve
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg02 with dissolve
    else:
        scene bg02_1 with dissolve
    call place02 from _call_place02_2
    show screen nvlbox with dissolve
    "\n 神殿の壮大なシルエットを満たす寮の一つ。{w}その奥に、正体の知らない可愛い建物がある。"
    "昨日から気になっていたが、立ち寄ってみる気がしない場所でその一つだった。"
    "気前よく入ってみたが、中は気が抜けるほど静かだ。"
    "木の特有の油っこい匂いが漂う。{w}ここの人もランチを食べに行ってしまったのか。"
    et "又はこの下にいるのだろう、俺は通路の先の階段へ視線を向けた。"
    nvl clear
    hide screen nvlbox with dissolve
    stop music fadeout 3
    pause 1
    scene bg104 with dissolve
    call place104 from _call_place104_1
    show screen nvlbox with dissolve
    "\n 地下へ繋がっているように見える階段には、扉や標識などは見えない。{w}その深さは実感できないが、ところどころ照明がつけてある。"
    "俺はこういう場所をよく知っている。{w}つまり俺のような部外者が入ってもいいってことだ。"
    "階段を下りるほど木の匂いが無くなり、代わりに花を香として火をつけたような独特な香りがした。"
    "何処かで吸った事のあるような香りだ。おかげで最初は心地よくなったが、それも一瞬。{w}下りれば下りるほど、頭が痛くなるほどその香りも濃くなった。"
    et "だが、目の前の風景はそんな香りなどはどうでもいいって思ってしまうほどに壮観だった。{w}数の知れない多くの本がぎちぎちと壁と本棚を満たした。"
    nvl clear
    "\n 地下に入ったはずだがとても広い。見上げると、俺の歩いてきた螺旋の道が高く据えられていた。{w}可愛い建物の正体は図書館だったらしい。"
    "「すげぇ…んだけどなぁ…」"
    "何かが可笑しい。{w}図書館といえば普段人の心を慰めるところなのに、ここは違和感そのものだとも言える。"
    "入口、階段、そして図書館だけではなく、最初この建物に入ってから今まで人一人も見えないってことは不自然的ではないか。"
    "疑わしがる独り言がただ散ってしまう広い空間。{w}俺は独りのはずなのになぜかさっきからずっと人の気配がする。それがさすがに薄気味悪い。"
    et "誰かが、もし想像のつかないほどの多くの人が、どこかに隠れて俺を眺めているのではないか…"
    hide screen nvlbox with dissolve
    pause 1
    nvl clear
    show SCG_10 2 with slowdissolve
    show screen textbox with dissolve
    play music 'audio/bgm/Evelyn.ogg' fadein 2
    qus "お探しの本が御座いますのでしょうか？"

    show SCG_10 0 with fastdissolve

    nar "ぼおっとしてそんな考えをしていたら、いきなり一人の女性が影を落とす。"
    nar "彼女は真っ白の肌に、装具の多い妙齢の女性で、背が結構高いせいで謎の威圧感がある。"
    pl "あ…？いや、そういうわけではないんだけど。{w}本はあんま読まないからさ…"
    nar "この女性からはさっきの花の香りがさらに濃く感じられる。{w}あっという間に気を取られてしまうほど甘く、強い香りだ。"
    nar "浄化部でよく感じられる雑に混じった香りとは違って、純粋で強烈な人工の香りだ。"
    nar "ひょっとすれば気を失いそうで、息を吐きながらなんとか目を覚ました。"
    nar "首を横に振る俺の姿が面白かっただろうか、紫の口紅の女性は微笑みを見せた。"
    pl "ここにぎっしりと詰まってる全てが本だなんて、なんだか凄いなぁって思って見てただけなんだ。"
    pl "姉さんはここの司書？"

    show SCG_10 2 with fastdissolve

    ev_q "あらら…{w}うふふふ、そうですよ…{w}似たような感じでございます。{w}此処に有る全ての本は、私の管理下にあるのですから…"
    nar "女性はゆっくりと、本の氾濫する景色を俺に見せるために体をひねた。{w}視覚で感じる前に、先に頭に染みつく風景だ。"

    show SCG_10 1 with fastdissolve

    ev_q "ふふ、この空間全てが、千年を越える歴史そのものなのです。"
    ev_q "人が創り上げて来たモノ、{w}と言いますかね…"

    show SCG_10 2 with fastdissolve

    ev_q "其れは…人と歴史、{w}歴史と歴史、{w}また人と神との邂逅とも例えられるのです。"
    pl "なんか、今朝似たような話を聞いたような…"
    pl "なんで人が作ったモノが神と繋がるんだ？"

    show SCG_10 0 with fastdissolve

    ev_q "人の歴史にはですね、{w}人同士の「結び目」という物が存在しております。"
    ev_q "そしてその「結び目」をお創りになられるのが、{w}我らが神なのです。"

    show SCG_10 2 with fastdissolve

    ev_q "人間程度の力のみでその域外の知識を得る事は不可能ですから…"
    pl "ふぅん…そうか。{w}ここは勝手に入ってもいい所なのか？"

    show SCG_10 1 with fastdissolve

    ev_q "ええ、勿論でございます。誰でも歓迎致しますよ。{w}我らが可憐なる兄弟、窓辺に佇む鳥、夏を告げるアイリスの香りまで…"
    pl "へえ…これは花の香りだったんだな。"

    show SCG_10 0 with fastdissolve

    ev_q "そうなのです、優雅ですよね？{w}贈り物として頂きましたので香水に仕立て上げてみましたのです。"

    show SCG_10 1 with fastdissolve

    ev_q "お気に召されたのなら、一つ差し上げますよ？"
    nar "そして彼女が懐から取り出した小さな紫の瓶は、自然と俺の両手の上に転がり込んだ。"
    pl "うぉ…あ、あんがと。受け取っておくぜ。"
    pl "司書の姉ちゃん、ここもうちょい見て回ってもいいか？"

    show SCG_10 0 with fastdissolve

    ev_q "うふふふ…{w}はい、勿論…"

    show SCG_10 2 with fastdissolve

    ev_q "しかしお気を付けて、此の空間は必ず貴方を惑わすことでしょう…"
    hide screen textbox with dissolve
    pause 1
    hide SCG_10 with slowdissolve
    pause 1
    show screen textbox with dissolve 
    nar "不思議なことを言いながら、あの「司書の姉さん」は柔らかな裾を戦がせて向こうへ歩いて行った。"
    nar "無数の本が並んだ、塀のような複雑な配列の本棚。{w}その間に入っただけなのに、まるで消えたように見えた。"
    nar "朦朧から覚めて足を移ろうとしたその一瞬、体が重心を失って大きく揺れた。"
    nar "どれだけにこの香りに酔ったままいたのか。{w}心当たりのないまま、俺は再び歩き出す。"
    nar "ともかくこの広き場所は俺の探求心を容赦なく刺激した。{w}許諾も取ったし、もっと自由に見巡ってもいいだろう。"
    nar "そんなことを思いながらあちこちうろうろしていたおれは、奥の扉の前に立つ。"
    nar "又見回すと、ここにはこのような扉がところどころにあった。{w}俺はその中で一つを選んで二回ノックした。"
    play sound "audio/SE/knock.ogg"
    nar "その時。"
    hide screen textbox with dissolve
    pause 1
    show SCG_12 0 with dissolve
    pause 1.5
    show screen textbox with dissolve
    pl "うわっ、ビックリした！" with sshake
    pl "何なんだよ…いきなり出てくると危ないだろ！"
    nar "俺がノックすると、がたんと扉が開いてその中から人一人が飛び出す。"
    nar "濃い桃色の特徴のある短い髪。{w}背は男性としては少し低いが、女性としては少し高いくらいか。"
    nar "だがどちらにしても決して不自然ではない容貌の人が、黒い目を大きくして俺を見つめていた。"
    qus "……"
    pl "お前は誰だ？お前も本を読みにきたのか？"

    show SCG_12 10 with fastdissolve

    qus "……"
    pl "口が聞けないのか…？名前は？"
    qus "なまえ…？"

    show SCG_12 0 with fastdissolve

    rs "なまえは、{w}{color=#d0a6bd}ローズ{/color}。"
    nar "小さく、しかしはっきり答えたその謎の人物は固まっては突然目を丸くした。{w}まるで何かに驚いたかのように。"

    show SCG_12 at bounce

    rs "おまえ、{w}ここにいちゃダメ。"
    pl "んぇ？"

    show SCG_12 10 with fastdissolve

    rs "なまえは、{w}ローズ。"

    show SCG_12 0 with fastdissolve

    rs "バイバイ。"
    pl "え、んん？？ば…バイバイ。"
    hide screen textbox with dissolve
    hide SCG_12 with dissolve
    play sound "audio/SE/door close.ogg"
    pause 1
    show screen textbox with dissolve 
    nar "その次の出来事は一瞬だった。"
    nar "ローズと名乗った子供は引手を握ったまま何歩か退いて、{w}その隙間から手を振って挨拶した後、扉を閉めてしまった。"
    nar "俺はいきなり追い出されて、割切れない気持ちでなんとか覘いてみようとしたが、{w}扉が又開く気配はなかった。"
    stop music fadeout 3
    hide screen textbox with dissolve
    pause 2
    $ day_rs = True
    $ day_time = day_time +1
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with slowdissolve
    else:
        scene bg02_1 with slowdissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_2
    return


label day2_ar:
    show screen place_day2
    show screen place_ar
    with None
    hide screen place_ar
    hide screen place_day2
    with dissolve
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03_4
    show screen nvlbox with dissolve
    "\n この神殿の特徴といえば州都の全てが見られるほどに高い建物だ、{w}なんて思ってしまうが、"
    "こんな神殿の中でも一番目立つ輝かしい建物がある。"
    "神殿のシルエットをもっと栄えさせる、傲慢だともいえるほど成り上がった建物。"
    "州都の事情を全く知らない俺であってもそれが魔導部のものだってことはすぐ気づく。"
    "「魔導部か…」"
    "この神殿に来てもう何回か、その謎の団体に足を取られたか。"
    et "建物くらい華やかな扉。{w}一瞬入ることを悩んだが、俺はこの先に真実があることを願って扉を開けた。"
    stop music fadeout 3
    nvl clear
    hide screen nvlbox with dissolve
    pause 1
    if hssh_rkn == True:
        scene bg102 with dissolve
    else:
        scene bg102_1 with dissolve
    call place102 from _call_place102_1
    play music 'audio/bgm/dialogue.ogg' fadein 2
    show screen nvlbox with dissolve
    "\n その中身は反論の余地のない州都の自慢、そのものだ。"
    "秋を知らせる小麦畑のような金色に煌く高い天井。{w}舞い降りる光を支えようとしているように成り上がった真っ白の柱。"
    if hssh_rkn == True:
        "曇った天気に隠れた太陽の光が、只この空間を照らしているのみだった。"
    else:
        "州都に来てからどこへ行っても見つからなかった太陽の光が、只、ここだけを、照らしていた。"
    "驚いたことはそれだけではない。{w}俺の目がどうにか逝かれていなければ、ここの人は皆訓練か鍛錬のような行動を行っていたんだから。"
    "その贅沢な風景に嘆声を嘆いたことも一瞬で、視線を前へ向けると体が固まった。"
    et "俺がここに入ってから動きを止めた多数の人が一斉に俺を眺めていた。"
    nvl clear
    "\n 全く同じ黒い髪と、同じ服装。又同じく黒い布で顔を隠した人たち。"
    "一人か二人だけではない。{w}この広き場所を満たした者全てが、全く同じ姿をしていた。"
    et "薄気味悪くなっている間、俺を前にして自分たち同士でひそひそと話している。{w}偶然の騒乱は一気に広がってこの空間を間もなく満たす。"
    hide screen nvlbox with dissolve
    nvl clear
    show screen textbox with dissolve
    qus "ほらほら、みんな静かに～！"
    hide screen textbox with dissolve
    pause 1
    show SCG_08 0 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "何回かの拍手の音がして、特に背の高い男の一人が俺の前に歩いてきた。"
    nar "この男はここの他の人とはまるで違う容貌をしていた。{w}黒じゃなく、金色の装飾をした白い服装。"
    nar "歩くたびに聞こえてくる軽い金属の衝突音が一体装飾のどこからしているのか分からないほどの、大袈裟な外観だ。"
    show SCG_08 10 with fastdissolve
    qus "何の用ッスか？此処は魔導部専用の建物ッス。{w}外部者は立ち入り禁止のはずなんスけど。"
    pl "こんな暑苦しい場所が魔導部の専用？？"
    show SCG_08 2
    play sound "audio/se/hit.ogg"
    en_q "失敬な！魔導師とは、依然として魔術以外の道も磨く必要があるんスよ。" with sshake
    en_q "いきなりズカズカと入って来て鍛錬を邪魔しても良いぐらい妥当な理由がないなら身元確認の後は出てって貰うッスからね！"
    stop music 
    play sound "audio/se/hit.ogg"
    show bgw
    show SCG_08 11
    hide bgw with dissolve
    qus "エノク！無礼極まりないのは貴様の方だ！貴賓の前では言葉を慎まないか！"
    hide screen textbox with dissolve
    hide SCG_08 with dissolve
    pause 1
    show SCG_07 0 with dissolve
    pause 1
    show screen textbox with dissolve
    play music 'audio/bgm/arne.ogg'
    nar "この広い館内で鮮明に鳴り響く声。{w}その持ち主は、わざと探そうとする必要もなく、すぐ目に入った。"
    nar "一瞬動きを止めた館内の人たちは、{w}警戒心を隠そうともしなかったさっきとは違って慌てながら左右へ退いた。"
    nar "その中心に彼女がいた。"
    nar "黒い髪、金の装飾のついた白い服装。{w}外観そのものを見ればさっきの男性と同じく、特に目立つ華やかさはない。"
    nar "だが、只の見せ掛けだけでは身につけられない気迫が、ここに集まった人たちとは確実な差を見せていた。"
    nar "まるで太陽の昇りだ。"
    nar "天井に反射され舞い落ちる光が彼女の周りに浮かんでいる景色を目にした俺は、そう単純な感想を思い出した。"
    nar "鮮明に光る彼女の青い目が、今はもう見れない真澄の空を映していたから。"

    show SCG_07 9 with fastdissolve

    ar_q "その容姿…{w}間違いなく{color=#E06666}[na]{/color}様でございますね。{w}お待ちしておりました。"
    hide screen textbox with dissolve
    show SCG_07 0 at arleft with dissolve
    show SCG_08 11 at hkright with dissolve
    pause 0.1
    show screen textbox with dissolve
    show SCG_08 11 at huruhuru
    en_q "あ、姉上…！"

    show SCG_07 2 with fastdissolve

    ar_q "まだ口を出すつもりか、{w}エノク。"
    ar_q "第一、一番最初に彼を探し出したという貴殿が本人の御顔もわからないとは、{w}どういう事だ？"

    show SCG_08 8 with fastdissolve

    en_q "それは……{w}申し訳ございません。"
    play sound "audio/se/hit.ogg"
    pl "ちょっとちょっと～当事者を差し置いて勝手に話進んでますけど？" with sshake

    show SCG_07 10 at center
    hide SCG_08
    with dissolve

    ar_q "ああ、申し訳ございません。{w}そういったつもりでは…"

    show SCG_07 9 with fastdissolve

    ar_q "ご不明な点がございましたらどうぞ。"
    pl "ふう～ん…まあ、聞きたいことは山々なんだけどさ、{w}まず自己紹介からお願いしてもらってもいいか？"
    nar "その言葉に、俺を眺めていた何十名の人が驚いたように体を竦める。"
    nar "さっきの俺の発言が州都の常識から外れているってことだ。"
    nar "一方から始まった小さな騒ぎは、蝋燭に火がつくように広がり、又周りを乱す。"

    show SCG_07 2 with fastdissolve

    ar_q "貴殿たちはお客様の前で何突っ立っておるか！早く道を開けなさい！"
    hide screen textbox with dissolve
    hide SCG_07 with dissolve
    show screen textbox with dissolve
    nar "だが、騒乱の中心にいた彼女は、その実直な姿勢を乱すこともなく、{w}さっきのようなまっすぐの道を開いた。"
    nar "そして俺を見つめる。{w}そこに恐れはちっともなかったが、俺は空間を満たす威圧感のせいか瞬間肩を震わせた。"
    hide screen textbox with dissolve
    show SCG_07 0 with dissolve
    show screen textbox with dissolve
    ar_q "お恥ずかしながら何もご用意は出来ておりませんが…{w}取り敢えずこちらへどうぞ。{w}質問もそちらでお受付いたしましょう。"
    pl "お、おう…"
    hide screen textbox with dissolve
    hide SCG_07 with dissolve
    show screen textbox with dissolve
    nar "今では訳が分からないことだが、彼女は俺の訪れを歓迎しているようだ。"
    nar "彼らの言葉通りに、{w}いきなり入ってきた邪魔者の俺を、こんなにも丁寧に相手する理由でもあるのか。"
    stop music fadeout 3
    hide screen textbox with dissolve
    pause 2
    scene black with dissolve
    pause 1
    if hssh_rkn == True:
        scene bg102 with dissolve
    else:
        scene bg102_1 with dissolve
    $ renpy.music.set_volume(1, channel="sound")
    play sound "audio/se/door slide.ogg"
    pause 3
    show screen textbox with dissolve
    nar "彼女に連れて入った部屋は暖かく、ふくよかなソファーもあり、気安いところだったが、"
    nar "一緒に入ってきた人が彼女であるゆえ、安心感は感じられない。"
    nar "俺の向かい側に女性が座り、その隣にさっきの男性が立っている。{w}男性はまだこの状況が不満そうだ。"
    hide screen textbox with dissolve
    show SCG_07 9 with dissolve
    play music 'audio/bgm/arne safe.ogg' fadein 1
    show screen textbox with dissolve
    ar_q "コホン、それでは改めてご挨拶を。"

    show SCG_07 0 with fastdissolve

    ar "私はアルタナータ家の長女、{color=#a4c2f4}アルネ・アルタナータ{/color}。{w}魔導部の補佐教にございます。"
    ar "伯父様からはよくお話をお伺いしておりました。"
    pl "伯父様…？"

    show SCG_07 11 with fastdissolve

    ar "兄弟様の里に、背の小さい黒髪の男性の方がいらしておりませんでしたか？"
    pl "あぁ！"
    ar "事情があって今は幼い姿のままですが…"

    show SCG_07 9 with fastdissolve

    ar "その方が私の伯父様である同時に現魔導部の主教でもある、{w}{color=#6d9eeb}エルジェーベト・アルタナータ{/color}様でございます。"
    pl "名前、メチャクチャに長いな…"
    hide screen textbox with dissolve
    show SCG_07 9 at arleft with dissolve
    show SCG_08 10 at hkright with dissolve
    show screen textbox with dissolve
    en_q "アルタナータ家は魔導で言う第一家門なんスよ？{w}それを初めて聞くだなんて、相当なド田舎から来たんスね…"

    show SCG_07 0 with fastdissolve

    ar "こら、口を慎めと言ったろう？外に出ていなさい。"

    show SCG_08 8 with fastdissolve

    en_q "んぐぐ…"

    show SCG_08 3 at center
    hide SCG_07
    with dissolve

    en_q "お客様とのお話もそりゃあ大事なんでしょうけども…{w}鍛錬の途中だし長引かないようお願いしますよ～姉上…"
    hide screen textbox with dissolve
    hide SCG_08 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "男性は刃の立ったその一言に、しばらくは手を止めるが、{w}俺と女性を代る代る見ながら整然な顔をしてみる。"
    nar "だがそれだけ、{w}反抗する気はないように、彼はただ一度頷いて外へ出た。"
    hide screen textbox with dissolve
    show SCG_07 4 with dissolve
    show screen textbox with dissolve
    ar "やれやれ…やはり時間が時間なので外も騒がしいですね。"
    nar "扉がちゃんと閉まることを見ていた彼女が小さなため息をつく。"
    nar "ふと聞いてみれば今の状況を嘆ずるような言葉だが、{w}彼女の表情は今までの中で一番穏やかな顔だった。"
    nar "俺は今になってアルネ・アルタネータという女性をまっすぐ向き合えるようになったようだ。"
    hide screen textbox with dissolve
    show SCG_07 7 with dissolve
    show screen textbox with dissolve
    ar "彼は私と共に魔導部の補佐教として主教様を護衛する{color=#a2c4c9}エノク・アピス{/color}です。"
    ar "血は繋がってないのですが、{w}幼い頃から一緒に育ってきた義理の弟なのです。"

    show SCG_07 9 with fastdissolve

    ar "ああ見えて普段はとても大人しく、頼もしい者なのですが…{w}弟の無礼には代わって私の方から謝罪させて頂きます。"
    pl "いんや、あんま気にしてないし。別にいいよ。"
    pl "そっかあ…なんか似てるな～って思ったら家族なのか…{w}仲良いな～"

    show SCG_07 0 with fastdissolve

    ar "神殿には色んな部署が存在していますが、魔導部は他とは少し違うのです。"
    ar "彼らは皆、家族としての絆を築いているのです。{w}彼らの前に立ち、少しばかりでも導けるという事実は私の自慢でもあります。"

    show SCG_07 7 with fastdissolve

    ar "[na]兄弟も、もうじき魔導の一員となられるお方ですので…{w}これからも是非気楽に声をお掛けください。"
    pl "あっ、そういえばその話…{w}できればもっとちゃんと詳細が聞きたいんだけど。"

    show SCG_07 11 with fastdissolve

    ar "ああ、そうですね。それが…{w}実は元々伯父様の方から兄弟を呼び出して直接お話をする、という予定だったのですが…"
    ar "残念なことに、ここ数日は全く時間が省けなくなってしまいまして。"

    show SCG_07 9 with fastdissolve

    ar "逆にお願いさせて頂くことになってしまい大変心苦しいのですが、"
    ar "明日の昼辺りに一度こちらの部署へお越し頂いてもよろしいでしょうか？{w}私の方から伯父様にお伝えしておきます。"
    pl "明日の昼な？オーケーオーケー。{w}俺はいいぜ？どうせ仕事終わったら暇なんだし。"

    show SCG_07 0 with fastdissolve

    ar "私共の配慮が足りなかったせいで機嫌を悪くさせてしまったのにも関わらずにこんなにも寛容に…"

    show SCG_07 9 with fastdissolve

    ar "このアルネ・アルタナータ、頭が上がりません。"
    pl "違う違う、本当に構わないんだって！"
    nar "その男がいきなりどうして俺を訪れたか今更分かった気がする。"
    nar "この「魔導部」っての団体の文化は、不快感を感じるほど俺の故郷に似ている。"
    nar "やっとその団体から脱出したと思ったのに、結局又この輪に入ってしまったのかもしれない。"

    show SCG_07 0 with fastdissolve

    ar "…兄弟？{w}何をそんなに悩んでおられますのでしょうか？"
    pl "ん～それがなあ…{w}実は呼び名がちょっと堅苦しいかなって思って。"
    pl "どうせ俺とも絆を築きたいならさ、\n俺のこと{color=#E06666}[na2]{/color}って呼んでくれたらどうだ？"

    show SCG_07 11 with fastdissolve

    ar "{color=#E06666}[na2]{/color}…{w}その敬称には何か意味が？"
    pl "や、別に意味とかはないけど。{w}ただの愛称みたいなもんかな？俺の家族も皆俺のことをそう呼んでたし。"

    show SCG_07 7 with fastdissolve

    ar "愛称…ですか。とても良い文化ですね。{w}失礼でなければ私にもその、愛称というものを付けて頂けますか？"
    pl "いいね！姉さんの名前はアルネだから…"
    pl "{color=#a4c2f4}アル{/color}、でいいんじゃねえか？{w}\nよし、{color=#a4c2f4}アル姉{/color}って呼ぶぜ。"

    show SCG_07 4 with fastdissolve

    ar "ふふ、誰かにそういう風に呼ばれたのは初めてです。"

    show SCG_07 7 with fastdissolve

    ar "こういう気分だったのですね…{w}[na2]兄弟に授かったこの名前、大事にします。貴殿に心からの感謝を。"
    pl "そういう堅苦しい言い方をどうにかしてくれって意味でのアレだったんだけどなあ…{w}ま、今はこれくらいでいいか。"
    pl "これからもよろしくな、アル姉。"

    show SCG_07 4 with fastdissolve

    ar "はい、こちらこそ。"

    show SCG_07 11 with fastdissolve

    ar "…あ、お帰りになられるのであれば護衛を…"
    pl "いやだからいいって！"
    stop music fadeout 3
    hide screen textbox with dissolve
    hide SCG_07 with dissolve
    pause 2
    $ day_ar = True
    $ day_time = day_time +1
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with slowdissolve
    else:
        scene bg02_1 with slowdissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_2


label day2_gr:
    show screen place_day2
    show screen place_gr
    with None
    hide screen place_gr
    hide screen place_day2
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg03 with dissolve
    else:
        scene bg03_1 with dissolve
    call place03 from _call_place03_9
    play music 'audio/bgm/grette.ogg' fadein 3
    show screen textbox with dissolve
    nar "幸い、昨日の記憶に違いはない。{w}ロビー中央の片隅で曲がると保健部の医務室がある。"
    nar "ここだけの穏やかな空気が、寒い外にずっといたせいだろうかもっと暖かく感じられる。"
    nar "だが今日の風景は昨日のとはちょっと違う。{w}入口の辺りに結構大きい箱が積み上げてあり、グレーテ先生はその箱を運んでいる。"
    hide screen textbox with dissolve
    show SCG_14 0 with dissolve
    show SCG_14 at bounce
    show screen textbox with dissolve
    gr "あらまあ！[na2]くん来てたのね！{w}もうちょっとだけ待ってくれる？今ちょっとだけ忙しくて…"
    pl "手伝おうか？"

    show SCG_14 1 with fastdissolve
    show SCG_14 at bounce

    gr "本当？助かるわ～"
    hide screen textbox with dissolve
    hide SCG_14 with dissolve
    pause 1
    if hssh_rkn == True:
        scene bg03 at huruhuru
    else:
        scene bg03_1 at huruhuru
    pause 1.0
    show screen textbox with dissolve
    gr "うん…しょっと！{w}ちょっと重いから気を付けてね！"
    pl "これくらい余裕のよっちゃだぜ！"
    nar "俺は袖をたくし上げ、目の前の箱をひょいと持ち上げた。"
    nar "箱の重さにはそれぞれ差があったが、{w}その中でも結構重たいやつは、俺ですら片膝で支えなければ難しいぐらいだ。"
    nar "先生は棚とその辺りに箱を詰めて置きたがったが、気合満々で、{w}俺に任せておけばいいことを最後まで一緒にやり遂げる。"
    nar "細い両腕がぶるぶると震え、{w}手が届くには遥かに足りない棚の上に箱を置くためにつま先立ちした時は随分驚いた。"
    nar "いろんな意味で目の離せない人だ。"
    hide screen textbox with dissolve
    pause 1
    if hssh_rkn == True:
        scene bg06 with dissolve
    else:
        scene bg06_1 with dissolve
    call place06 from _call_place06_1
    pause 1
    show SCG_14 with dissolve
    show screen textbox with dissolve
    gr "ふぅ、お陰で助かったわ～"

    show SCG_14 9 with fastdissolve
    show SCG_14 at bounce

    gr "若い頃はこんな箱の一つ二つぐらい軽く持ち上げられたのに、わたしももう年なのねぇ…"
    pl "そんなこと言っといて、全く…{w}先生も案外意地張ったりするんだな。"

    show SCG_14 1 with fastdissolve
    show SCG_14 at bounce

    gr "うっふふ。{w}あらあ、わたしの秘密がバレちゃったわ！"
    gr "こう見えても先生はここを管理してる人ですもの。{w}お客さんに仕事を任せっぱなしは出来ないわ。"
    gr "そこに掛けて休んでていいよ！今日はクッキーもあるわ。"
    pl "おぅ！ご丁寧なおもてなし嬉しいぜ。{w}頂きま～す！"
    pl "てか…これって全部何なんだ？ここって医務室だったよな？"

    show SCG_14 0 with fastdissolve
    show SCG_14 at bounce

    gr "生活補給品よ。{w}きみたちが使っている歯ブラシとか、マスクや下着が足りなくなったらここから持っていくといった感じね。"
    gr "薬に使う材料や包帯は今別の子たちが治療所に運びに行ってくれてるの。"
    gr "普通は主教様が手伝ってくれるけど、今日は忙しいらしくてね…"
    pl "俺今朝見たことあるぜ。{w}あの眼鏡の人だろ？"

    show SCG_14 1 with fastdissolve
    show SCG_14 at bounce

    gr "そうそう！髪整えてると別人みたいでしょ～？{w}普段もそれぐらいしっかりしてくれたらねぇ…"

    show SCG_14 8 with fastdissolve
    show SCG_14 at bounce

    gr "背筋もビシッとしたら完璧！"
    pl "へぇ…{w}そうだ、先生。聞きたいことがあるんだけど。"

    show SCG_14 0 with fastdissolve

    gr "はい、何でしょう～[na2]くん？"
    pl "補佐教って正確には何なんだ？"

    show SCG_14 7 with fastdissolve

    gr "あらら、聞かされてなかったのね。"
    show SCG_14 at bounce
    gr "う～ん…そうねえ、例えばね、{w}[na2]くんみたいな見習いの司祭は研修期間が終わったら正式に司祭になれるでしょう？"

    show SCG_14 0 with fastdissolve

    gr "補佐教はその一段上の叙階って感じかな。{w}主教様のお隣に付き添って補佐するの。"
    gr "護衛だけでなく仕事のお手伝いや、主教様が多忙であれば代わりに部署の管理を任されたり…{w}うん、そんな感じね。"
    pl "ほぉほぉ、じゃあ先生も補佐教？"

    show SCG_14 1 with fastdissolve
    show SCG_14 at bounce

    gr "ピンポン！大正解～{w}保健部補佐教のグレーテでございます。{w}ふふ、管理人のお姉さんではないのよ～？"
    pl "へー！{w}じゃあそのヘンな服装も補佐教の特権みたいなモンなのか？"

    show SCG_14 0 with fastdissolve

    gr "ううん、ちょっと違うかな？{w}洗礼を受けて正式に司祭になったら、聖痕を表せるための特別な祭服を受注出来るようになるの。"
    pl "聖痕を表せるため…？"

    show SCG_14 8 with fastdissolve

    gr "まぁ…大体はそんな感じね。{w}聖痕は神聖力の根本となる部分なんだし、"

    show SCG_14 1 with fastdissolve

    gr "それでも晒すなんてほんっと～にムリです！って子はお願いして特別に目立たないような服を仕立てるらしいけど…"
    pl "あれ、じゃあそれって基本的には祭服なんだよな？{w}先生のソレはどう見ても祭服には見えないけど…"

    show SCG_14 6 with fastdissolve

    gr "わ…わたしは主教様にどうしても～って頼み込んだだけなの。"
    show SCG_14 at huruhuru
    gr "ちょっとだけ特別なケースって言うのかしら…{w}恥ずかしいわ～…"

    show SCG_14 1 with fastdissolve

    gr "皆が皆私みたいではないと思うから、{w}うん！みんな優しくて真面目で若い良い子たちなの。"
    pl "前からずっと気になってたことなんだけどさあ…"
    pl "先生、いくつ？"

    show SCG_14 5 with fastdissolve
    show SCG_14 at huruhuru

    gr "{cps=*0.1}ひ{/cps}{nw}・{cps=*0.1}み{/cps}・{nw}{cps=*0.1}つ{/cps}！{w}"
    stop music fadeout 3
    hide screen textbox with dissolve
    hide SCG_14 with dissolve
    pause 2
    $ day_gr = True
    $ day_time = day_time +1
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with slowdissolve
    else:
        scene bg02_1 with slowdissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_2
    return


label day2_hk:
    show screen place_day2
    show screen place_hk
    with None
    hide screen place_hk
    hide screen place_day2
    with dissolve
    stop music fadeout 3
    pause 2
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg04 with dissolve
    else:
        scene bg04_1 with dissolve
    call place04 from _call_place04_3
    play music 'audio/bgm/dialogue.ogg' fadein 3
    show screen textbox with dissolve
    nar "ガタンガタンと動く絡繰りの音だけが響く作業場。遠くから見てもさすがに人はいない。"
    nar "この荒涼たる場所を見回していると、多くの人がすごい勢いで押し寄せてきていた食堂の風景を思い出す。"
    nar "ここの人は皆ランチの時間まで仕事を捌くのは嫌らしい。"
    nar "でも昨日はまともなやつ一人くらいはいたのに、今日はあの一人さえもみえない。"
    nar "あいつも今食堂で飯でも食っているのか。{w}もしそうだったら俺はあいつを尊敬しかねない。"
    nar "大騒ぎそのものの空間の中、彼の周りだけには寂寞が漂うはずだから。"
    nar "その時、{w}誰か、{w}力を抜いていた俺の肩を指で刺した。"
    play sound "audio/se/hit.ogg"
    stop music
    pl "うわっ！" with sshake
    play sound "audio/se/hit.ogg"
    show SCG_05 5
    hk "わぁお！" with sshake
    nar "後ろの人は俺の予想した人ではなかった。{w}むしろ想像さえしていなかった方だ。"
    nar "どうして主教たる彼女がこんなところにいる？"
    nar "俺が落ち着く間、彼女は俺を刺した指を合わせ、{w}琥珀のような目を二、三回ほど瞬いて俺を見つめた。"
    play music 'audio/bgm/golden haku.ogg'
    pl "な、な、何だよ…{w}心臓落っこちるとこだったぞ！"
    hk "それはわたくしのセリフですぅ…{w}[na]様、どうしてこんなところにおられるのでしょうか？"
    hk "研修生はたしか、{w}午前でおしごとは終わるはずですよぉ？"
    pl "それは…！{w}…その…ゴメン、{w}けど…"
    if hssh_rkn == True:
        nar "白夜の明るい空を雲が隠して通る時、彼女の目にも青い陰がうねた。"
        nar "まるで消えない光の祝福を一気に受け取っているように、彼女は地上の何物よりも明るく見えた。"
    else:
        nar "彼女の目は青いとは言えるが、光を浴びると高原の稲のような金色で煌く。"
        nar "極夜の真っ暗の天の下、彼女が持っている蝋燭の灯が揺らぐと、{w}彼女の目を満たした金色も共に戦ぐ。"
        nar "暗闇に慣れたせいか、きっと蝋燭一個に頼っているだけなのに、{w}その光は地上の万物の何よりも明るく見える。"
    nar "たった一つ立ち上がった黄金の光は、{w}彼女をもっと、現実との乖離のある存在であるように見せようとする。"
    nar "そんな彼女が突然俺に触れた。{w}そう簡単に落ち着ける場合ではない。"

    show SCG_05 1 with fastdissolve

    hk "けど…？"
    pl "でも主教様みたいなデカい人がいきなり飛び出して来たら誰だってビビるって。{w}次からは先に声掛けてくれよ！"

    show SCG_05 5 with fastdissolve

    hk "声なら、おかけしましたよー？"
    pl "エ、いつ？"

    show SCG_05 1 with fastdissolve

    hk "わたくしども皆、父なる神の元に結ばれいるのです…"

    show SCG_05 0 with fastdissolve

    hk "その心と心は言わずとも通じ合い…♪"
    pl "物理的に通じるような言葉にしてくれって！"

    show SCG_05 4 with fastdissolve

    hk "ふっふっふ～「じょーく」です…♪"
    pl "マジかよ…神殿のユーモアセンスは一生分からない気がするな…"

    show SCG_05 0 with fastdissolve

    hk "では、こちらへは見学としてお越しで…？とってもえらえらですぅー"
    pl "まあ、それもあるけど。"
    pl "もしかして仕事の邪魔になったのか？"

    show SCG_05 1 with fastdissolve

    hk "いえいえー、ちょ～ど帰り道でございました。{w}見慣れた場所に、見慣れないお方が佇んでおりましたので、思わず…♪"

    show SCG_05 0 with fastdissolve

    hk "新しい姉妹兄弟が増えていくことは、{w}わたくしにとっていつもいつも心のおどることですので…♪"
    pl "それは良かった。{w}実は昨日ここで仕事してる奴の邪魔をしちゃってさ、それで死ぬほど怒られちゃったんだよ。"
    pl "あの眉間梅干し野郎に。"

    show SCG_05 1 with fastdissolve

    hk "シーキュレット様のことでしょうかぁ…{w}うふふ、同じ兄弟をそういう風に言ってはいけませんよぉ？"
    hk "昨日はぁ…ああ、そうでした…{w}わたくし、実は良く意識が途切れて倒れちゃうので…"
    hk "彼にはよくお世話になっているのです。{w}ああ神様、ありがたくも…"
    pl "いやいや…{w}ありがとうは主教様の仕事を代わってくれたアイツに言うべきだろ？"

    show SCG_05 1 at bounce

    hk "素敵な出逢いを巡らせてくださった神に感謝を……♪"
    pl "うわ…"
    nar "里では結構若いと言える俺は今までいろんな大人と話してみたが、"
    nar "こんなに話が通じないと思った人間には今まで会ったことがない。"
    nar "彼女のそういう言行は天然らしかった。{w}本人の部下たちと結構親しくなった、と思っているように発言しているが、"
    nar "裏でどんな風に陰口をたたかれているのか知らないだろう。"
    nar "予想はしていたが、さすがに気まずい。"
    nar "だが、この妙な気まずさの原因は他にもあった。{w}俺はそれを確かめるために口を切った。"
    pl "あのさ、主教様…もしかして昨日、森の中に居なかったか？"

    show SCG_05 5 with fastdissolve

    hk "もりのなか…？"
    pl "その、あったじゃんか、古い礼拝堂近くに…"
    hk "野外礼拝堂のことでしょうかぁ…？"
    hk "うう～～～～ん…{w}いいえ、{w}まったく、記憶にございませんのですぅ…"
    pl "嘘だ！{w}ハッキリこの目で見たんだよ、しかも目が合っただろ！{w}あの時俺がどれだけビックリしたか…！"

    show SCG_05 6 with fastdissolve
    show SCG_05 at huruhuru

    hk "ひぃ…！おこらないでくださいぃぃ…"
    pl "えっ…怒ってなんかいないって！{w}…あ、そうか…いきなり大声出してゴメン。"

    show SCG_05 7 with fastdissolve

    hk "ごめんなさい…{w}わたくし、実は幼いころ事故に遭って以来、たまあに記憶が飛んでしまっちゃうのでぇ…"
    pl "はあ…？それはどういう？"

    show SCG_05 9 with fastdissolve

    hk "うまく説明できないけど…"
    hk "たとえば、気付いたら最後の記憶とはまったく違う場所にいたり、{w}知らない人が親しく話を掛けてきたり…"
    hk "今まで何をしていたか、{w}今から何をすべきか、{w}今日が何日何時なのかすら…わからなくなっちゃって…"

    show SCG_05 7 with fastdissolve

    hk "先程仰ったように、記憶にまったくないわたくしの目撃談を聞いたりするのですぅ。"
    pl "それって大丈夫なのか…？"

    show SCG_05 1 with fastdissolve

    hk "はぁい、わたくしはいつも神の御許に祝福を頂いておりますので…"
    hk "これといった不便を感じたことはございません～…♪"
    pl "そ、それは逆にすごいって言うか何と言うか…"
    pl "とにかくそうなんだな…{w}なんだか納得は行かないけど。"

    show SCG_05 5 with fastdissolve

    hk "んぇえ？"
    pl "俺の記憶と主教様の記憶でズレがあるなんて、何だか妙な気分になるじゃんか。"

    show SCG_05 0 with fastdissolve

    hk "なるほろぉ…それでは…"
    hk "今後はわたくしが[na2]兄弟を忘れることのないよう、{w}どうぞ、{w}できれば頻繁に、"
    hk "アサガオのように気まぐれなわたくしに逢いに来てくださいませ…♪"
    pl "なるべくそうするぜ！{w}主教様とは今後もよく会うことになりそうだしさ。"

    show SCG_05 1 with fastdissolve

    hk "うふふ……{w}ふむう…しかしですね…"

    show SCG_05 0 with fastdissolve

    hk "ということは[na]様、{w}もしかして野外礼拝堂にお入りになられたのですかぁ？"
    pl "入ってはないけど、そこの近辺をちょっと…"

    show SCG_05 8 with fastdissolve

    hk "そこは立ち入り禁止の区域なんですう…{w}向かい道に確か標識もあったはずなのですが…"
    hk "冒険心に溢れるのは大変よろしいことですけど、{w}お気を付けて頂かないと困っちゃいますぅ…"
    pl "マジか…ゴメンゴメン！{w}実は俺、物凄い方向\n音痴でさ、{w}寮まで向かう途中に迷っちゃって\n…"
    pl "暗くて多分標識も見えてなかったんだと思う。{w}次からはちゃんと気を付けるよ。"

    show SCG_05 4 with fastdissolve

    hk "ふっふっふ～…{w}[na]兄弟、「ようちゅういじんぶつ」ですね…♪"
    pl "うっ…{w}主教様にだけはあんま聞きたくなかったぜ…"
    hide screen textbox with dissolve 
    hide SCG_05 with dissolve
    pause 2
    $ day_hk = True
    $ day_time = day_time +1
    stop music fadeout 3
    $ show_quick_menu = False
    if hssh_rkn == True:
        scene bg02 with slowdissolve
    else:
        scene bg02_1 with slowdissolve
    play music 'audio/bgm/map select.ogg' fadein 3
    jump day_time_2

label day2_night:
    if hssh_rkn == True:
        $ save_name = "day 2, 夜, 楽園"
    else:
        $ save_name = "day 2, 夜"
    $ show_quick_menu = True
    if hssh_rkn == True:
        scene bg02_1 with dissolve
    else:
        scene bg02_2 with dissolve
    pause 2
    stop music fadeout 2
    if hssh_rkn == True:
        scene bg14_1 with dissolve
    else:
        scene bg14_2 with dissolve
    call place14 from _call_place14_2
    show screen textbox with dissolve
    nar "一日中歩き回しすぎたな。"
    nar "グレーテ先生から貰ったバター味のクッキーを食べながら浄化部の扉を開くと、照明の光何本かが俺を迎える。"
    nar "そして薄暗い照明の前で座ったまま俺を睨んでくるやつがいる。{w}シーキュレットだ。"
    hide screen textbox with dissolve
    show SCG_03 0 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "小さいくせにああも目尻を上げているとまるで猫だ。"
    nar "俺の里には猫が結構多くも住んでいたから、やたらに親しみを感じてしまう。"
    pl "よぉ、遅くまでご苦労さん。{w}クッキー食べるか？食べかけだけど。"
    show SCG_03 2 with fastdissolve
    sc "オマエ…{w}今日の午前の仕事、行ってないだろ。"
    nar "そんな俺とは逆に、彼はいきなり舌鋒鋭く迫る。{w}そういえば俺、猫とあまり仲良くなかったな。"
    pl "いきなり何言い出してんだ？{w}行ってきたに決まってるだろ。"
    show SCG_03 2 at huruhuru
    sc "そう？{w}3番地に午前訪問するべきだった神父が来てないって苦情の電話が来てたけど。"
    sc "お陰様で元々午後にされるべきだった住宅の撤去が引き延ばしになったって地主が30分近く受話器越しに怒鳴ってたぞ。"
    sc "しかもその仕事の担当はオマエだったし。"
    pl "3番地…？"
    nar "おかげで書類の内容がやっと頭に浮かんだ。"
    show SCG_03 0 with fastdissolve
    nar "…{w=1}{nw}"
    play sound "audio/SE/ding.ogg"
    show bgw at ding
    extend "しまった！{w}マヤを神殿まで送ってあげたからすっかり忘れていた。"
    nar "いきなりケチをつけられたと思ったのに、これは後頭部を強く殴られた気分だ。"
    nar "慌てる俺の表情を読み取って何を考えたか、{w}シーキュレットはため息をつく。"
    show SCG_03 2 with dissolve
    pause 0.5
    play music "audio/bgm/Securett.ogg"
    sc "…ここで仕事していきたいんなら最低限書類を読めるぐらいの読解力はないと困るんだけど。"
    pl "ち、違う！書類はちゃんと確認したって！"
    show SCG_03 0 with fastdissolve
    sc "じゃあ何で？"
    pl "それは…"
    pl "……忘れてて…"
    show SCG_03 2 with fastdissolve
    sc "忘れた？"
    nar "本気で呆れたという反応でむしろ俺が呆れ返りそうだ。{w}俺はこの感情の合理的な理由を探しに頭をひねってみる。"
    pl "マヤを送ってあげてて気付かなかったんだよ。"
    pl "第一、ここに来てまだ二日しか経ってない新入員に書類をたったの一枚だけ寄こして投げやりに出勤させた方が悪いだろうが。"
    sc "……"
    show SCG_03 0 with fastdissolve
    sc "そうだね、その通りだ。"
    nar "彼は俺の横腹を押し分けて通り過ぎ、大袈裟に自分のロッカーを開いた。"
    nar "昨日と全く同じだ。{w}そうやって自分が怒っているって知らせたいのだ。"
    show SCG_03 2 with fastdissolve
    sc "明日からキミの教育はボクが専担するから、{w}ボクの指示があるまでは勝手に動くなよ。"
    sc "これはあの女の子にも同じく伝えとくこと。いいか？"
    pl "……"
    nar "あいつは俺と目さえ合わせずその一方的な通報を伝えて、{w}靴紐を結んでから頭を上げ、こちらを見つめた。"
    show SCG_03 0 with fastdissolve
    sc "あと、寮にはボクの代わりに書類の整理をしてから帰って。"
    pl "ハァ？何で俺が…！"
    sc "ボクはキミが無責任に放り投げた仕事を今から処理しにいかないといけないから。"
    nar "もう人の話を最後まで聞くつもりもないな。"
    show SCG_03 7 with fastdissolve
    sc "日付別で分類しといて。{w}まあ数字も読めないんだったら別に帰ってもいいけど。"
    pl "…人をバカにするなよ。"
    hide screen textbox with dissolve
    hide SCG_03 with dissolve
    pause 1.0
    play sound "audio/SE/door close.ogg"
    show screen textbox with dissolve
    nar "俺の鋭い視線に返事を返すように、あいつは舌打ちして外へ出る。"
    nar "これでここには俺と、薄暗い照明と、絶望的に積み上げられた紙の山だけだ。"
    play sound "audio/SE/hit.ogg" 
    if hssh_rkn == True:
        nar "…………"
        nar "なんで俺がこんなことをやらなければならないんだ？"
        nar "畜生。俺は机を拳で打ち下ろした。積もった紙がばらばらと、床に落ちる。その光景を見ていれば更に頭から血が湧いてくる気分だ。"
        nar "何なんだ、あの汚物でも見ているような顔は、言い終わる度のため息は、ぶっちゃけお前のせいだろうが。"
        nar "入ったばかりの新入りを放置して偉ぶるツラしてやがることが先任の役割ってことか？"
        nar "俺が放り投げた仕事の処理だって？寮には後で帰れだ？"
        nar "偉い補佐教様が欠けた新入りの後片付けだってそりゃ大変ご苦労さんだ、そんなに大したもんならこれも何とかしてみればどうだ？"
        nar "狭い間の机が次々と崩れる。強くぶつかった脚が痛かったが、大したことではなかった。"
        nar "机の上のコップ、水垢の付いた花瓶などの破片が踏まれて破れた紙切れと共に床を乱す。"
        nar "気が付いたら、俺はそのゴミだらけの上に一人で立っていた。目の前の漠々な風景に目が回りそうだ。"
        nar "結局寮に帰ってしまった。{w}明日は……もう何も考えたくない。"
    else:
        "{nw}" with vpunch
        nar "チクショウめ。{w}俺は机の空いているところに拳を打ち込んだ。"
    hide screen textbox with dissolve
    stop music fadeout 3
    pause 2
    if hssh_rkn == True:
        scene bg15_1 with dissolve
    else:
        scene bg15_2 with dissolve
    pause 1
    show screen textbox with dissolve
    if hssh_rkn == True:
        nvl clear
    else:
        nar "もう夜だな。{w}これから毎日あいつと一緒に行動しないといけないだろうか。"
    nar "重たい足首から疲労感がどっと感じられる。{w}鈍い動きで鍵を取り出し扉を開いた時、側の扉が開く。"
    nar "朝には只タイミングが合っただけかと思ったが、案外この音がするのをずっと待っていたのか。"
    nar "どちらにせよ、金髪の女性はちょっと機嫌が悪そうだ。"
    hide screen textbox with dissolve
    pause 1
    show SCG_102 1 with dissolve
    pause 1.0
    show screen textbox with dissolve
    lz2 "きみってほんとほっつき回るの好きね。{w}神殿はどう？そろそろ慣れた？"
    pl "よぉ、先輩。別に見回ってて遅くなった訳じゃねぇよ。"
    nar "「ツイてねぇだけだ」と言いたい心は山々だが、何とか呑み込んだ。"
    pl "それはそうとして…{w}今日結局仕事はちゃんと行ったのか？"
    show SCG_102 0 with fastdissolve
    lz2 "休んだけど？体調悪くて。"
    pl "何だよ…本当に体調のせい？"
    show SCG_102 5 with fastdissolve
    lz2 "あら、ホントだってば～{w}あたしのこと疑ってるの？やだやだ、見損なっちゃう。"
    pl "ゴメンゴメン、冗談だって！{w}で、体調は？ちょっとはマシになったか？"
    lz2 "まあ…{w}まあまあなんじゃない？"
    show SCG_102 at bounce
    lz2 "…いや、やっぱりすごく気分悪いかも。"
    show SCG_102 1 with fastdissolve
    lz2 "ホントにあたしに申し訳ないって思ってるなら水でも部屋に持ってきてくれる？"
    pl "まあ、いいけど…"
    hide screen textbox with dissolve
    hide SCG_102 with dissolve
    pause 1
    show screen textbox with dissolve
    nar "俺の曖昧な答えが気に入ったのか、彼女は細目をあげて笑う。{w}そしてよろしくって手振りをして一気に扉を閉めてしまう。"
    nar "あまりにも堂々と閉まった扉を見て、俺は一歩遅くため息をついた。"
    nar "一体どうして俺は疲れたのにいきなり仮病の患者のお使いをしているのか…"
    nar "考えれば考えるほど只疲労感が積もっていくだけで、俺は考えを諦め、又歩き出した。"
    hide screen textbox with dissolve
    stop music fadeout 3
    pause 2
    if hssh_rkn == True:
        scene bg10_1 with dissolve:
            xzoom -1.0
    else:
        scene bg10_2_ with dissolve
    call place10_1 from _call_place10_1_1
    pause 1
    show SCG_102 outfit 5 with dissolve
    show screen textbox with dissolve
    lz2 "はぁ…どっかの山奥から汲んできてるのかと思っちゃったじゃん。"
    nar "その短い間にいつ着替えたか、金髪の先輩は今朝見た下着の姿だ。"
    nar "これじゃ着替えたより脱ぎ捨てたってことが正しいかもしれない。"
    pl "似たようなもんだろ。{w}ちょっとぬるいかも知れないけど…"
    show SCG_102 outfit 0 with fastdissolve
    lz2 "何か入れたりしてない？"
    pl "何を？"
    lz2 "あたしみたいな超美人を好き勝手出来るような悪いお薬とか？"
    pl "先輩こそ俺を何だと思ってるんだ…？そんなことしても何の得にもならないだろ。"
    show SCG_102 outfit 4 with fastdissolve
    lz2 "本当？きみって相当おめでたいのね。"
    nar "水を取った彼女はまだ引手を握ったまま、俺から何歩か離れる。{w}入ってこい、って言いたいらしい。が、"
    nar "疲れたし、断りたい気分の方がもっと大きいが、扉はまるで人を揶揄うように閉まってしまう。"
    nar "俺がそれを見て視線を移し、じっと見つめても、{w}金髪の女性は白々しく笑っているだけだ。"
    show SCG_102 outfit 1 with fastdissolve
    lz2 "ねえねえ、どうせまだ寝ないつもりなら遊んでいきなよ！{w}[na2]ちゃんは彼女とかいる？"
    pl "あったこともねぇよ…{w}そういうのに興味を持ったこともなかったし。"
    show SCG_102 at bounce
    lz2 "え～マジ？マジのマジで一回も？{w}手とか繋いだりもしたことナシ？"
    pl "周りの女の人といえばみんな家族だったから。"
    show SCG_102 at bounce
    lz2 "アッハハハ！"
    nar "そんな他愛もない会話を続けつつ一歩、{w}また一歩とこちらへと近づいていた彼女はドサッとそのままベッドに腰を掛ける。"
    play sound "audio/se/cup.ogg"
    nar "その反動で零れてしまった水が胸から始まり腹を伝って地面を水浸しにしていく。"
    show SCG_102 outfit 2 with fastdissolve
    lz2 "やだ～やっちゃった～"
    pl "な、な、何やってんだよ！"
    show SCG_102 outfit 1 with fastdissolve
    lz2 "手が滑っちゃってさぁ？"
    hide screen textbox with dissolve
    hide SCG_102 with dissolve
    pause 1.0
    show screen textbox with dissolve
    nar "最初から下着としての機能を果たせていないように見えていたレース付きの布切れは、"
    nar "最早彼女の薄茶色の胸元を露骨なまでに晒している。"
    nar "なのにも関わらず彼女は恥ずかしがる気配すらない。{w}いや、楽しんでるようにも見える。"
    nar "腹の底から湧き上がるような不安が確信へと変わっていく。"
    play music "audio/SE/no more bell my buddy.ogg" fadein 30
    nar "この部屋に入ってしまったその瞬間から、{w}いや、{w}出会ってしまったその時から俺はずっとこの女に弄ばされて来たのだ。"
    lz2 "あたし横になるけど～いいよね？"
    pl "先輩の部屋だろ…一々俺に確認取るなよ…"
    $ renpy.music.set_volume(5, channel="sound")
    play sound "<from 0.5>audio/se/r18 2.ogg"
    nar "遠慮もなく横たわった女体から出来るだけ目を離そうとするも、彼女がわざわざこちらへと腕を引っ張ってくる。"
    if hssh_rkn == True:
        scene bg10_1 at bounce:
            xzoom -1.0
    else:
        scene bg10_2_ at bounce
    lz2 "ねえ、一緒に寝なよ～"
    pl "エ、そういうのはちょっと！"
    nar "ギクシャクしながらもやっと横になると、{w}彼女と初めて会った時にも匂っていた強烈な香りが鼻を貫いては脳ミソを詰める。"
    lz2 "肌、すごくスベスベね…"
    nar "始めは顔を撫でていた冷たくか細い指先は、弧を描きながらどんどん腰へと降りていく。"
    nar "その背筋の凍るような感覚に連れるようバクバクと心音が高鳴っていく。"
    hide screen textbox with dissolve
    show SCG_102 outfit 1 with dissolve
    show screen textbox with dissolve
    lz2 "ねぇ、何で女の人に興味がないの？"
    pl "まぁ……{w}俺がそうだったってだけ。そんな必ず要るって訳でもないし…"
    nar "何だか喉が渇く。{w}間をおくようにしてやっと言葉を吐いた。"
    show SCG_102 outfit 0 with dissolve
    lz2 "女を知らないからそうなのよ。"
    pl "そりゃあ…{w}俺は…女じゃないから…"
    hide SCG_102 with dissolve
    nar "この雰囲気にあまり圧されたくはない。{w}がしかし、さっきからどうしても声に力が入らない。"
    nar "それもこれも全部喉が渇いているせいだ。"
    hide screen textbox with dissolve
    show screen nvlbox with dissolve
    "\n「違うでしょ、経験の問題なんだって。」"
    "彼女は身体を起こし、{w}ベッドの上を這うようにして寝たままの俺に太ももを密着させては見下ろす。"
    "その奇妙な光景を見ていると刹那、胸に引っ掛かっていた黒い下着が滑り落ちる。"
    "不意の状況に俺はただ息を呑む。{w}彼女はそんな俺の反応すら楽しんでいるのか鼻で笑う様にしてその脂肪の塊どもを目の前に垂らす。"
    "この状況が何を意味するのか、今やっと理解できた気がした。"
    "「な、なぁ」"
    "「しーっ。{w}きみって喋るとダサいんだよね。」"
    et "俺の口を塞いだ彼女は腰を起こし、片足を俺の股の間に挟んだ。"
    nvl clear
    "\n 俺の下半身に体重をかける女性から、香水か汗の臭いか分からない生臭いニオイがした。"
    "間違いなくあの太ももの間からする臭いだ。俺はその臭いが感じられるほど、女性の近くにいるのだ。"
    et "服の擦れる音が徐々に早くなり、女性の息の音が近くなる。{w}不規則に聞こえる鼻声、唾液の溜まる音が脳裏を濡らす。"
    nvl clear
    "\n その不快な湿気は急に形を帯びてきた。ぐにゃりとした舌が耳の中に食い込んで耳を濡らす。"
    "ボサボサになった金髪が顔を覆い、鼻と口まで入り込んだ。{w}息苦しさに喘ぐと思わず悲鳴が出てしまう。"
    et "反射的に起き上がろうとしたが、彼女が俺の体を完全に覆っているため指一つさえ動けなかった。"
    nvl clear
    "\n 「は…？勃ってないの？」"
    "突然、彼女は動きを止め、身体を起こす。低い声で荒い呼吸をしながら、口に入った何本かの髪の毛を吐き出した。"
    et "急に体が軽くなり、素肌に寒風が当たる。{w}俺もいつの間にか汗をかいていた。息が上手く出来ないせいで目眩がする。"
    nvl clear
    "\n 「それは…その…」"
    "突然として彼女は行為を止めてしまった。{w}お喋りな口が止まり、下着に引っ掛けていた手も放したまま、唐突にも部屋に静寂が訪れる。"
    "「……？」"
    "訳も分からずふと顔を上げると目が合う。{w}その目はずっとこちらを見つめていた。"
    et "一瞬で沈んでしまった空気の中俺は口を開けることも、動くことも叶わなかった。"
    nvl clear
    "\n 「ヤりたくないなら別にいいけど？{w}あたしも無理矢理やらせる気はないんだし。」"
    "低く、冷たい声。{w}どうやら彼女の癪に触ってしまったらしい。"
    "「いや、やりたくないって訳じゃ…」{w}彼女の視線から逸らすように他へと目をやる。"
    "この空気、{w}喉元からヒュッ、と乾いた音が出る。{w}拒みたいと思っているのか？俺は…"
    stop music fadeout 0.5
    if hssh_rkn == True:
        et "\n………"
    else:
        "正直、興味がないなんて言ったらそれこそ嘘だった。"
        et "\n「嫌ってわけじゃ、ないけど…」"
    nvl clear
    hide screen nvlbox with dissolve
    play music 'audio/bgm/r18.ogg' fadein 5
    pause 1
    if hssh_rkn == True:
        show story06R with slowdissolve:
            zoom 1.7
            xpos -330
            ypos -410
    else:
        show story06 with slowdissolve:
            zoom 1.7
            xpos -330
            ypos -410
    $ renpy.music.set_volume(5, channel="sound")
    play sound 'audio/SE/r18 2.ogg'
    pause 2
    nvl clear
    show screen nvlbox with dissolve
    if hssh_rkn == True:
        et "\n 髪の毛が顔を遮っていた為、俺は彼女の表情を見る事は叶わなかった。"
    else:
        "\n 髪の毛が顔を遮っていた為、俺は彼女の表情を見る事は叶わなかった。"
    "しかし俺は彼女が嗤っているという事だけは分かった。俺から離れた彼女が冷たい指で頬を掴み押してくる。"
    "ひと際長い爪が頬の肉に刺さるので、俺は口を反射的に開いてしまった。"
    play sound 'audio/SE/r18 3.ogg' fadein 3 loop
    et "すると舌がぬるっと入り込む。{w}一度耳を這いずった舌は温かった。{w}口にたまった唾液が混ざり、首を通ると気持ちの悪い音がする。"
    nvl clear
    "\n 彼女は動かない俺の舌を一方的に吸ったり、馬鹿みたいにぽっかり開いたままの口を乱暴に撫で回す。膨張された呼吸に声が混ざる。"
    "口を大きく開き長い舌を出す度、硬い歯が歯茎に当たって痛かった。"
    "俺がそれ以上口を開けられないままいると、彼女の舌は唇を舐め始める。{w}まるで犬が皿を平らげる様に頬を、鼻を、目元を唾液で塗りたくった。"
    et "べっとりと濡れた顔から消化された食べ物特有の焦げたような臭いがした。"
    nvl clear
    hide screen nvlbox with dissolve
    if hssh_rkn == True:
        show story06R with slowdissolve:
            zoom 1.0
            xpos 0
            ypos 0
    else:
        show story06 with slowdissolve:
            zoom 1.0
            xpos 0
            ypos 0
    pause 1
    show screen nvlbox with dissolve
    nvl clear
    "\n 「気持ちいい？ねぇ？気持ちいいよね？」{w}裏返った声が同じ単語を繰り返す。{w}テカテカと水気を帯びた彼女の唇は赤黒い軟体動物の様に光っている。"
    "俺はその言葉の意味をちゃんと理解することが出来なかった。"
    et "だが最初から俺の意志など最初から関係もなかったのか、女はベタつくほど蒸し暑くなってきたズボンの中へとその冷たい手を入れてくる。"
    stop sound fadeout 2.0
    hide screen nvlbox with dissolve
    stop music fadeout 2
    pause 1
    show black with slowdissolve
    play sound 'audio/SE/r18 4.ogg'
    pause 6
    play sound 'audio/SE/r18 5.ogg'
    pause 5
    stop sound fadeout 3.0
    pause 2
    if hssh_rkn == True:
        scene bg10_1 with dissolve:
            xzoom -1.0
    else:
        scene bg10_2_ with dissolve
    nvl clear
    show screen textbox with dissolve
    $ renpy.music.set_volume(1, channel="sound")
    play sound "audio/se/r18 2.ogg"
    lz2 "ふぅー…"
    nar "金髪女は棚を探り、中から煙草を取っては咥える。"
    nar "辺りに白く撒かれる煙に目が痛んでくる。"
    nar "こんな物が司祭の棚から出てくるなんて、神殿は俺が思ったより厳しくもないのだろうか。"
    pl "あの…さ、なんでこんなことを？"
    show SCG_102 outfit 4 with dissolve
    lz2 "女と手も繋いだことない童貞が州都まで来て都会かぶれのクソ田舎女と毎日乳繰り合ってるのがカワイソ～だったから？"
    pl "い、田舎…{w}マヤとあの女の子のことか？友達かと思ってたのに。"
    show SCG_102 5 with fastdissolve
    lz2 "はぁ？あたしがあんなクソ陰キャ女と友達なわけないっしょ。"
    lz2 "あたしあの子キラ～イ。{w}今朝もあたしの部屋まで来ててぶっちゃけ超ウザかったし？"
    show SCG_102 4 with fastdissolve
    lz2 "きみもあの子嫌いでしょ。{w}だってあいつず～っときみに付きっきりだったじゃん。"
    show SCG_102 1 with fastdissolve
    lz2 "ねぇ知ってる？ああいう女子ってさ、自分がブスで男にモテないのを隠したいからずっと下手に回ってんの。"
    show SCG_102 5 with fastdissolve
    lz2 "あたしと一緒にいれば自分の立場もエラくなるとでも思ってんじゃない？"
    show SCG_102 4 with fastdissolve
    lz2 "それか何？{w}レズビアンってやつ？"
    show SCG_102 1 with fastdissolve
    show SCG_102 at bounce
    lz2 "キモ～！アハハハッ！"
    hide screen textbox with dissolve
    hide SCG_102 with dissolve
    pause 1.0
    show screen textbox with dissolve
    nar "殆どの人間は汗を流すと正直になれる、とも言う。{w}そんな彼女の口から普段なら想像すらできない言葉が飛び出てきた。"
    nar "俺は返す言葉が見つからず口ごもってしまう。"
    lz2 "ねぇ何か言いなって～"
    nar "ボトッ、まだ素肌のままの俺の脚に紅色の煙草の煤が落ちる。" with sshake
    nar "吃驚した俺は起き上がって、赤く腫れ上がった肌を擦り落ち着かせる。"
    pl "なん…？！頭イカれてるだろ！" with sshake
    show SCG_102 outfit 5 with dissolve
    lz2 "何で大声出すのよ～先に無視したのそっちじゃん？"
    lz2 "あたし別の友達いるから。"
    show SCG_102 1 with fastdissolve
    show SCG_102 at bounce
    lz2 "あ～そうそう。明日会わせてあげる！あの子たちもきみのこと気に入ったんだって。"
    pl "もういい、俺はいいから…{w}本当に……いい加減にしてくれ。{w}もう行くから…"
    show SCG_102 at bounce
    lz2 "ハハ、もう行っちゃうの？{w}おやすみ～、まあ寝られないだろうけど～？"
    hide screen textbox with dissolve
    hide SCG_102 with dissolve
    scene black with dissolve
    pause 1
    $ renpy.music.set_volume(1, channel="sound")
    play sound "audio/se/door slide.ogg"
    show screen textbox with dissolve
    nar "俺はまだ着られていない服を適当に掴んでは逃げるように部屋から離れる。"
    nar "最初の強圧的な態度は何処へ行ったのか、金髪女は手を振りつつ俺を見送る。"
    nar "本当にソレだけが目的だったんだ。"
    nar "自身の部屋の扉を閉める頃には騒がしかった胸も落ち着いてくる。"
    nar "今さっき起きたばかりのことなのに、狐にでも化かされた気分だった。"
    nar "それが気のせいではないとでも言うように腰は痛むしまだ吐き気もする。"
    nar "洗い流したい気持ちでいっぱいだったが、こんな時間に一人寮を出歩きたくはない。"
    nar "そんなことを悩んでいると今日一日の疲労がやっと訪れたのかどんどん思考が鈍くなってきた。身体も重い。"
    $ _skipping = False
    nar "気のせいか、今もどこかで薄く煙草の臭いがする。"
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
    jump day3
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
