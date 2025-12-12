init python:
    import locale
    if persistent.firstbootlang is None:
        system_language = locale.getdefaultlocale()
        if system_language is None:
            system_language = "English"
        if system_language not in ["Japanese", "SimplifiedChinese", "Korean"]:
            system_language = "English"
        config.language=system_language
        persistent.current_lang = system_language
        persistent.firstbootlang = "Okay"
        renpy.save_persistent()

init python:
    def reset_data():
        
        reset_cheats()
        
        try:
            renpy.seen_label = {}
            renpy.game.seen_label = {}
            persistent._seen_ever = {}
            persistent._seen_images = {}
        except:
            pass
        
        
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswith("_"):
                setattr(persistent, attr, None)
        
        renpy.save_persistent()
        
        
        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)
        
        
        renpy.quit(relaunch=True)



init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("interface")


init -1 style button:
    properties gui.button_properties("button")
    hover_sound "audio/SE/mouse over.ogg"
    activate_sound "audio/SE/mouse click.wav"


init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
    hover_sound "audio/SE/mouse over.ogg"
    activate_sound "audio/SE/mouse click.wav"


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_idle_thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)











init -501 screen morning:
    add 'main_menu_bar.png'


    text "何をしよう？":
        size 28
        xpos 0.05
        yalign 0.3


    if (day == 1):
        text "{font=amii.otf}熱の月 1日    朝{/font}":
            size 16
            xpos 0.05
            yalign 0.25


    if (day == 2):
        text "{font=amii.otf}熱の月 2日    朝{/font}":
            size 16
            xpos 0.05
            yalign 0.25

    if (day == 3):
        text "{font=amii.otf}熱の月 3日    朝{/font}":
            size 16
            xpos 0.05
            yalign 0.25

    if (day == 4):
        text "{font=amii.otf}熱の月 4日    朝{/font}":
            size 16
            xpos 0.05
            yalign 0.25

    if (day == 5):
        text "{font=amii.otf}熱の月 5日    朝{/font}":
            size 16
            xpos 0.05
            yalign 0.25

    if (day == 6):
        text "{font=amii.otf}熱の月 6日    朝{/font}":
            size 16
            xpos 0.05
            yalign 0.25

    if (day == 62):
        text "{font=amii.otf}熱の月 6日    朝{/font}":
            size 16
            xpos 0.05
            yalign 0.25

    if (day == 7):
        text "{font=amii.otf}熱の月 7日    朝{/font}":
            size 16
            xpos 0.05
            yalign 0.25


    vbox:
        style_prefix "morning"

        xpos 0.05
        yalign 0.5
        spacing gui.navigation_spacing




        textbutton _("{size=28}仕事へ向かう{/size}"):
            action Call('return_morning')




label return_morning:
    show screen morning with None
    hide screen morning
    $ show_quick_menu = True
    with dissolve
    pause 1
    return






















































init -501 screen dmy_keymap:
    add None

init -501 screen say(who, what):
    $ _last_say_who = who
    $ _last_say_what = what
    if persistent.dead_maya == True:
        key "mousedown_3" action Call('dmy_x')
    if persistent.dmy >= 2:
        if persistent.dmy_off == False:
            key "mousedown_4" action Call('dmy_x')
        else:
            key "mousedown_4" action ShowMenu("history")
    else:
        key "mousedown_4" action ShowMenu("history")
    style_prefix "say"
    zorder 101
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0





init -1 python:

    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos











init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xalign gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    yalign 0.5
    ypos 350
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "audio/SE/mouse over.ogg"
    activate_sound "audio/SE/mouse click.wav"

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    hover_sound "audio/SE/mouse over.ogg"
    activate_sound "audio/SE/mouse click.wav"



default -1 show_at_frame = True

init -501 screen at_frame():
    zorder 98

    if show_at_frame:
        add "images/frame.png"


init python:
    def _sync_auto_indicator():
        
        if not renpy.game.preferences.afm_enable and renpy.get_screen("auto_indicator"):
            renpy.hide_screen("auto_indicator")
        
        elif renpy.game.preferences.afm_enable and not renpy.get_screen("auto_indicator"):
            renpy.show_screen("auto_indicator")
        return

    config.interact_callbacks.append(_sync_auto_indicator)

init python:
    def _auto_off_when_skip_changes():
        
        prev = getattr(_auto_off_when_skip_changes, "_prev_skip_state", None)
        current = renpy.is_skipping()
        
        
        if prev is not None and prev != current and renpy.game.preferences.afm_enable:
            renpy.game.preferences.afm_enable = False
            renpy.restart_interaction()
        
        
        _auto_off_when_skip_changes._prev_skip_state = current
        return

    config.interact_callbacks.append(_auto_off_when_skip_changes)

init python:
    _prev_skip_state = None

    def _auto_off_when_skip_changes():
        global _prev_skip_state
        current = renpy.is_skipping()
        
        
        if _prev_skip_state is not None and _prev_skip_state != current:
            if renpy.game.preferences.afm_enable:
                renpy.game.preferences.afm_enable = False
                renpy.restart_interaction()
        
        _prev_skip_state = current
        return

    config.interact_callbacks.append(_auto_off_when_skip_changes)



default -1 show_quick_menu = True

init -501 screen quick_menu_dmy:


    zorder 101
    add None
    add "gui/quick.png":
        xalign 1.001
        yalign 0.0
        xzoom 1.1
        yzoom 1.1

    hbox:
        style_prefix "quick"

        xalign 0.97
        yalign -0.005

        if persistent.dmy_off == False:
            textbutton _("SKIP") action Call("dmy_x")
        else:
            textbutton _("SKIP") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("AUTO") action [Preference("auto-forward", "toggle"), ToggleScreen("auto_indicator")]


init -501 screen quick_menu():
    zorder 101

    if show_quick_menu:
        add None
        add "gui/quick.png":
            xalign 1.001
            yalign 0.0
            xzoom 1.1
            yzoom 1.1

        timer 0.1 action NullAction() repeat True

        hbox:
            style_prefix "quick"
            xalign 0.97
            yalign -0.005
            spacing 10

            textbutton _("SKIP") action Skip()
            textbutton _("AUTO") action Preference("auto-forward", "toggle") selected If(renpy.game.preferences.afm_enable, True, False)


init -501 screen quick_menu_12:


    zorder 101

    if show_quick_menu:
        add None
        add "gui/quick.png":
            xalign 1.001
            yalign 0.0
            xzoom 1.1
            yzoom 1.1

        timer 0.1 action NullAction() repeat True

        hbox:
            style_prefix "quick"
            xalign 0.97
            yalign -0.005
            spacing 10

            textbutton _("SKIP") action Skip()
            textbutton _("AUTO") action Preference("auto-forward", "toggle") selected If(renpy.game.preferences.afm_enable, True, False)

init -501 screen quick_menu_F():


    zorder 100

    if show_quick_menu:
        add None
        add "gui/quick.png":
            xalign 1.001
            yalign 0.0
            xzoom 1.1
            yzoom 1.1


        hbox:
            style_prefix "quick"

            xalign 0.97
            yalign -0.005


            textbutton _("SKIP") action None
            textbutton _("AUTO") action None




init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = True

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")
    hover_sound "audio/SE/mouse over.ogg"
    activate_sound "audio/SE/mouse click.wav"

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")
    hover_sound "audio/SE/mouse over.ogg"
    activate_sound "audio/SE/mouse click.wav"







init python:
    def jump_from_menu(label_name):
        
        try:
            renpy.hide_screen("preferences")
        except:
            pass
        try:
            renpy.hide_screen("game_menu")
        except:
            pass
        
        
        renpy.end_interaction(None)
        
        
        renpy.jump_out_of_context(label_name)


init -501 screen navigation():

    vbox:
        style_prefix "navigation"

        if main_menu:
            xpos 190
            yalign 0.67
            spacing 20

        else:
            xpos gui.navigation_xpos
            yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            imagebutton:
                idle 'gui/titlemenu1_idle.png'
                hover 'gui/titlemenu1_hover.png'
                hover_sound "audio/SE/mouse over.ogg"
                activate_sound "audio/SE/mouse click.wav"

                action Start()
            imagebutton:
                idle 'gui/titlemenu2_idle.png'
                hover 'gui/titlemenu2_hover.png'
                hover_sound "audio/SE/mouse over.ogg"
                activate_sound "audio/SE/mouse click.wav"
                action ShowMenu("load")

            imagebutton:
                idle 'gui/titlemenu3_idle.png'
                hover 'gui/titlemenu3_hover.png'
                hover_sound "audio/SE/mouse over.ogg"
                activate_sound "audio/SE/mouse click.wav"
                action ShowMenu("preferences")

            if persistent.hssh_end == True:
                imagebutton:
                    idle 'gui/titlemenu4_idle.png'
                    hover 'gui/titlemenu4_hover.png'
                    hover_sound "audio/SE/mouse over.ogg"
                    activate_sound "audio/SE/mouse click.wav"
                    action ShowMenu("cggallery1")
            elif persistent.cheat_gal == True:
                imagebutton:
                    idle 'gui/titlemenu4_idle.png'
                    hover 'gui/titlemenu4_hover.png'
                    hover_sound "audio/SE/mouse over.ogg"
                    activate_sound "audio/SE/mouse click.wav"
                    action ShowMenu("cggallery1")

            imagebutton:
                idle 'gui/titlemenu5_idle.png'
                hover 'gui/titlemenu5_hover.png'
                hover_sound "audio/SE/mouse over.ogg"
                activate_sound "audio/SE/mouse click.wav"
                action Quit(confirm=not main_menu)

        else:
            if persistent.dmy >= 2:
                textbutton _("マヤが好き") action Call("dmy_x")

                textbutton _("マヤが好き") action Call("dmy_x")
                textbutton _("マヤが好き") action Call("dmy_x")

                textbutton _("マヤが好き") action Call("dmy_x")

                if persistent.dmy_off == True:
                    textbutton _("マヤが嫌い") action Function(jump_from_menu, "day12")
                else:
                    textbutton _("マヤが好き") action Call("dmy_x")

                textbutton _("マヤが好き") action Call("dmy_x")
            else:
                textbutton _("ヒストリー") action ShowMenu("history")

                if (hardmode == True):
                    textbutton _("セーブ") action None
                    textbutton _("ロード") action None

                else:
                    textbutton _("セーブ") action ShowMenu("save")
                    textbutton _("ロード") action ShowMenu("load")

                textbutton _("オプション") action ShowMenu("preferences")

                textbutton _("タイトルへ") action MainMenu()

                textbutton _("ゲーム終了") action Quit(confirm=not main_menu)
















init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")







init -1 python:
    import random
    random.seed()
    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        """
    This creates the snow effect. You should use this function instead of instancing
    the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
    using the default values =D)
    
    @parm {image} image:
        The image used as the snowflakes. This should always be a image file or an im object,
        since we'll apply im transformations in it.
    
    @parm {int} max_particles:
        The maximum number of particles at once in the screen.
        
    @parm {float} speed:
        The base vertical speed of the particles. The higher the value, the faster particles will fall.
        Values below 1 will be changed to 1
        
    @parm {float} wind:
        The max wind force that'll be applyed to the particles.
        
    @parm {Tuple ({int} min, {int} max)} xborder:
        The horizontal border range. A random value between those two will be applyed when creating particles.
        
    @parm {Tuple ({int} min, {int} max)} yborder:
        The vertical border range. A random value between those two will be applyed when creating particles.
        The higher the values, the fartest from the screen they will be created.
    """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    class SnowFactory(object):
        """
    The factory that creates the particles we use in the snow effect.
    """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
        Initialize the factory. Parameters are the same as the Snow function.
        """            
            
            self.max_particles = max_particles
            
            
            self.speed = speed
            
            
            self.wind = wind
            
            
            self.xborder = xborder
            self.yborder = yborder
            
            
            
            
            self.depth = kwargs.get("depth", 10)
            
            
            self.image = self.image_init(image)
        
        
        def create(self, particles, st):
            """
        This is internally called every frame by the Particles object to create new particles.
        We'll just create new particles if the number of particles on the screen is
        lower than the max number of particles we can have.
        """
            
            if particles is None or len(particles) < self.max_particles:
                
                
                depth = random.randint(1, self.depth)
                
                
                
                
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      
                                random.uniform(-self.wind, self.wind)*depth_speed,  
                                self.speed*depth_speed,  
                                random.randint(self.xborder[0], self.xborder[1]), 
                                random.randint(self.yborder[0], self.yborder[1]), 
                                ) ]
        
        
        def image_init(self, image):
            """
        This is called internally to initialize the images.
        will create a list of images with different sizes, so we
        can predict them all and use the cached versions to make it more memory efficient.            
        """
            rv = [ ]
            
            
            for depth in range(self.depth):
                
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )
            
            return rv
        
        
        def predict(self):
            """
        This is called internally by the Particles object to predict the images the particles
        are using. It's expected to return a list of images to predict.
        """ 
            return self.image
    class SnowParticle(object):
        """
    Represents every particle in the screen.
    """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
        Initializes the snow particle. This is called automatically when the object is created.
        """
            
            
            self.image = image
            
            
            
            
            if speed <= 0:
                speed = 1
            
            
            self.wind = wind
            
            
            self.speed = speed
            
            
            
            self.oldst = None
            
            
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
        
        
        def update(self, st):
            """
        Called internally in every frame to update the particle.
        """
            
            
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
            
            
            if self.ypos > renpy.config.screen_height or\
        (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                    
                    return None
            
            
            
            
            return int(self.xpos), int(self.ypos), st, self.image















init -1:
    image snow = Snow("particle2.png", max_particles=50, speed=20, wind=100 )
    image Blsnow = Snow("particle3.png", max_particles=150, speed=20, wind=100,)

init -501 screen main_menu():
    tag menu
    style_prefix "main_menu"
    on "show" action SetVariable("_skipping", False)
    add "bgw.png"
    add "Blsnow"
    add gui.main_menu_background
    add "snow"

    frame



    text "ver [config.version]":
        size 16
        color "000"
        xalign 0.01
        yalign 0.99



    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text

init -1 style main_menu_frame:
    xsize 224
    yfill True

    background "gui/overlay/main_menu.png"

init -1 style main_menu_vbox:
    xalign 1.0
    xoffset -16
    xmaximum 640
    yalign 1.0
    yoffset -16

init -1 style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

init -1 style main_menu_title:
    properties gui.text_properties("title")

init -1 style main_menu_version:
    properties gui.text_properties("version")










init -501 screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add "bgw"
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        if main_menu:
            add None
        else:
            frame:
                style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    if main_menu:
        add None
    else:
        use navigation
        textbutton _("戻る"):
            style "return_button"

            action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 24
    top_padding 96

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 224
    yfill True

init -1 style game_menu_content_frame:
    left_margin 32
    right_margin 16
    top_margin 8

init -1 style game_menu_viewport:
    xsize 880

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 8

init -1 style game_menu_label:
    xpos 40
    ysize 96

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -24










init -501 screen about():
    tag menu





    use game_menu(_("バージョン情報"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size











init -501 screen save():
    tag menu


    use file_slots(_("セーブ"))


init -501 screen load():
    tag menu


    use file_slots(_("ロード"))


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("ページ {}"), auto=_("オートセーブ"), quick=_("クイックセーブ"))

    use game_menu(title):

        fixed:



            order_reverse True



            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.4

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileSaveName(slot, empty=_("空のスロット")):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">")


init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 40
    ypadding 3

init -1 style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")








init -1 python:
    def ResetToDefaults():
        _preferences.text_cps = config.default_text_cps
        _preferences.afm_time = config.default_afm_time
        _preferences.afm_enable = config.default_afm_enable
        _preferences.set_volume('sfx',0.75)
        _preferences.set_volume('music', 0.75)
        
        renpy.restart_interaction()

init -1 python:
    def ResetToTextDefaults():
        _preferences.text_cps = config.default_text_cps
        _preferences.afm_time = config.default_afm_time
        _preferences.afm_enable = config.default_afm_enable
        
        renpy.restart_interaction()

init -1 python:
    def ResetToSoundDefaults():
        _preferences.set_volume('sfx', 0.75)
        _preferences.set_volume('music', 0.75)
        
        renpy.restart_interaction()

default -1 persistent.call_CG = True

init -501 screen preferences():
    tag menu
    on "show" action [ Preference("auto-forward", "disable"), Function(renpy.restart_interaction) ]


    use game_menu(_("環境設定"), scroll="viewport"):

        vbox:

            if main_menu:
                xpos 50
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        if main_menu:
                            style_prefix "radio"

                        style_prefix "ingame"

                        label _("ディスプレイ")
                        vbox:
                            hbox:
                                spacing 30
                                textbutton "400x300" action [Preference("display", 0.375)]
                                textbutton "640x480" action [Preference("display", 0.625)]
                            hbox:
                                spacing 30
                                textbutton "1024 x 768" action [Preference("display", 1.0)]
                                textbutton "1280 x 960" action [Preference("display", 1.25)]
                            hbox:
                                textbutton _("フルスクリーン") action Preference("display", "fullscreen")

                vbox:
                    xpos 50
                    style_prefix "radio"
                    label _("センシティブなCGを表示")
                    textbutton "オン" action SetVariable('persistent.call_CG', True)
                    textbutton "オフ" action SetVariable('persistent.call_CG', False)


            null height (4 * gui.pref_spacing)

            hbox:
                if main_menu:
                    style_prefix "slider"

                style_prefix "ingame_slider"
                box_wrap True

                vbox:

                    label _("文字表示速度")

                    bar value Preference("text speed")

                    label _("オート待ち時間")
                    bar value Preference("auto-forward time")

                    textbutton _("テキスト設定初期化"):
                        action ResetToTextDefaults
                        if main_menu:
                            ypos 22
                        else:
                            ypos 42

                    textbutton _("オプション初期化"):
                        action ResetToDefaults
                        ypos 45
                    if main_menu:
                        textbutton "ヘルプ":
                            action Call("tut_menu")
                            ypos 45

                        textbutton _("チートオプション"):
                            text_style "cheat_button"
                            action Confirm("{color=#E06666}注意！{/color}\n\n{size=24}このページにはゲームの重大なネタバレが含まれています。\n{vspace=5}チートの使用は、ゲームの楽しさを損なうおそれがあります。\n\nチートオプションを確認しますか？{/size}", ShowMenu("cheat_page"))
                            ypos 42



                vbox:

                    if config.has_music:
                        label _("音楽の音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("効果音の音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("テスト") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("ボイスの音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("テスト") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全てミュート"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                        textbutton _("サウンド設定初期化"):
                            action ResetToSoundDefaults
                            if main_menu:
                                ypos 15
                            else:
                                ypos 15
                                xsize 400


                    vbox:
                        ypos 6
                        style_prefix "radio"
                        label _("表示言語")
                        if main_menu:
                            textbutton "英語" action [Language("English"), SetVariable("persistent.current_lang", "English"), SetVariable("config.language", "English"), renpy.save_persistent()]
                            textbutton "日本語" action [Language("Japanese"), SetVariable("persistent.current_lang", "Japanese"), SetVariable("config.language", "Japanese"), renpy.save_persistent()]
                            textbutton "韓国語" action [Language("Korean"), SetVariable("persistent.current_lang", "Korean"), SetVariable("config.language", "Korean"), renpy.save_persistent()]
                            textbutton "簡体字中国語" action [Language("SimplifiedChinese"), SetVariable("persistent.current_lang", "SimplifiedChinese"), SetVariable("config.language", "SimplifiedChinese"), renpy.save_persistent()]
                        else:
                            text "言語設定を変更するには、タイトル画面に戻る必要があります。":
                                size 20


    if main_menu:
        hbox:
            xalign 0.05
            yalign 0.95
            textbutton '戻る' action Return() xalign 0.05 yalign 0.95
            textbutton _("{size=20}すべてのデータを初期化{/size}"):
                action Confirm("すべての記憶を虚無へと還しますか？\n\n{size=24}これまで保存していたデータが消えてしまい、元に戻すことはできません。\n注意：ゲームが再起動します。{/size}", Function(reset_data))
                xalign 0.05
                yalign 0.95
    else:
        add None


style cheat_button:
    size 20
    idle_color "#E06666"
    hover_color "#702f2f"

style cheat_text:
    idle_color "#E06666"


default persistent.cheat_hssh_end = False
default persistent.cheat_gal = False
default persistent.cheat_happy_end = False
default persistent.cheat_rosary = False
default persistent.cheat_title = False

default persistent.na = (
    "ベリアル" if config.language == "Japanese" else
    "벨리알" if config.language == "Korean" else
    "Belial" if config.language == "English" else
    "彼列" if config.language == "SimplifiedChinese" else
    "ベリアル"
)

default na = (
    "ベリアル" if config.language == "Japanese" else
    "벨리알" if config.language == "Korean" else
    "Belial" if config.language == "English" else
    "彼列" if config.language == "SimplifiedChinese" else
    "ベリアル"
)

default persistent.na2 = (
    "ベル" if config.language == "Japanese" else
    "벨" if config.language == "Korean" else
    "Bel" if config.language == "English" else
    "小彼" if config.language == "SimplifiedChinese" else
    "ベル"
)

default na2 = (
    "ベル" if config.language == "Japanese" else
    "벨" if config.language == "Korean" else
    "Bel" if config.language == "English" else
    "小彼" if config.language == "SimplifiedChinese" else
    "ベル"
)


default persistent.dmy_off = False
default persistent.dmy_skip_seen = False

init python:
    def reset_cheats():
        
        preferences.skip_unseen = False
        persistent.cheat_hssh_end = False
        persistent.cheat_gal = False
        persistent.cheat_happy_end = False
        persistent.dmy_off = False
        persistent.dmy_skip_seen = False
        
        
        renpy.save_persistent()


init -501 screen cheat_page():
    tag menu

    add "bgw"
    add gui.main_menu_background
    add "main_gallery.png"

    text "チートオプション":
        xpos 40
        ypos 33
        xalign 0
        color "#E06666"
        style "main_menu_title"

    use game_menu(_("チートオプション"), scroll="viewport"):
        vbox:
            spacing 60

            vbox:
                style_prefix "radio"
                spacing 30
                xpos 50

                hbox:



                    vbox:

                        label _("未読スキップを有効化")
                        hbox:
                            ypos 10
                            spacing 50
                            textbutton "オン" action [SetVariable('preferences.skip_unseen', True), renpy.save_persistent()]
                            textbutton "オフ" action [SetVariable('preferences.skip_unseen', False), renpy.save_persistent()]

                    vbox:
                        label _("監禁イベントの一部便利機能を\n正常化")
                        hbox:
                            ypos 10
                            spacing 50
                            textbutton "オン" action SetVariable('persistent.dmy_off', True)
                            textbutton "オフ" action SetVariable('persistent.dmy_off', False)

                vbox:
                    ypos 10
                    spacing 40
                    hbox:
                        vbox:
                            label _("「楽園編」を有効化")
                            hbox:
                                ypos 10
                                spacing 50
                                textbutton "オン" action SetVariable('persistent.cheat_hssh_end', True)
                                textbutton "オフ" action SetVariable('persistent.cheat_hssh_end', False)
                        vbox:
                            label _("「間違わない世界」を有効化")
                            hbox:
                                ypos 10
                                spacing 50
                                textbutton "オン" action SetVariable('persistent.cheat_happy_end', True)
                                textbutton "オフ" action SetVariable('persistent.cheat_happy_end', False)
                    vbox:
                        label _("ギャラリーをアンロック")
                        hbox:
                            ypos 10
                            spacing 50
                            textbutton "オン" action SetVariable('persistent.cheat_gal', True)
                            textbutton "オフ" action SetVariable('persistent.cheat_gal', False)

            textbutton _("全てのコレクションをアンロック"):
                xpos 50
                text_style "cheat_button"
                action Confirm("{color=#E06666}注意！{/color}\n\n{size=24}全てのコレクション要素:\n{vspace=5}ギャラリー、ロザリオ、背景画像がアンロックされ、\n{vspace=5}元に戻すことはできません。\n\n全てのコレクションをアンロックしますか？{/size}", Function(unlock_all_gallery))

    textbutton '戻る' action ShowMenu("preferences") xpos 36 ypos 692




init -501 screen dmy_preferences():
    style_prefix "game_menu" tag menu


    use game_menu(_("環境設定"), scroll="viewport"):

        vbox:

            if main_menu:
                xpos 50
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("ディスプレイ")
                        vbox:
                            hbox:
                                spacing 30
                                textbutton "400x300" action [Preference("display", 0.375)]
                                textbutton "640x480" action [Preference("display", 0.625)]
                            hbox:
                                spacing 30
                                textbutton "1024 x 768" action [Preference("display", 1.0)]
                                textbutton "1280 x 960" action [Preference("display", 1.25)]
                            hbox:
                                textbutton _("フルスクリーン") action Preference("display", "fullscreen")






            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字表示速度")

                    bar value Preference("text speed")

                    label _("オート待ち時間")
                    bar value Preference("auto-forward time")

                    textbutton _("テキスト設定初期化"):
                        action ResetToTextDefaults
                        ypos 22



                vbox:

                    if config.has_music:
                        label _("音楽の音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("効果音の音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("テスト") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("ボイスの音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("テスト") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全てミュート"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                        textbutton _("サウンド設定初期化"):
                            action ResetToSoundDefaults
                            ypos 15
                        textbutton _("オプション初期化"):
                            action ResetToDefaults
                            ypos 45
    if main_menu:
        textbutton '戻る' action Return() xalign 0.05 yalign 0.95
    else:
        add None




init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

init -1 style pref_label_text:
    yalign 1.0

init -1 style pref_vbox:
    xsize 420

init -1 style ingame_vbox is pref_vbox2

init -1 style pref_vbox2:
    xsize 310

init -1 style ingame_slider_vbox is slider_vbox2

init -1 style slider_vbox2:
    xsize 310

init -1 style ingame_slider2_vbox is pref_vbox

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")

init -1 style slider_slider:
    xsize 280

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 8

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 420

init -1:
    $ scroll=("vpgrid" if gui.history_height else "viewport")






init -501 screen history():
    tag menu


    predict False

    use game_menu(_("ヒストリー"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:



                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("ヒストリーがありません。")




define -1 gui.history_allow_tags = set()


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    font gui.history_text_font
    size 24
    ypos 5
    line_leading 5
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    line_leading 5
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5







init -501 screen help_screen():
    tag menu


    default device = "keyboard"

    use game_menu(_("ヘルプ"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 12

            hbox:

                textbutton _("キーボード") action SetScreenVariable("device", "keyboard")
                textbutton _("マウス") action SetScreenVariable("device", "mouse")





init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("台詞を読み進める。またはボタンを選択する。")

    hbox:
        label _("Space")
        text _("台詞を読み進める。ただしボタンは選択しない。")

    hbox:
        label _("方向キー")
        text _("インターフェースを移動する。")

    hbox:
        label _("Esc")
        text _("ゲームメニューを開く。")

    hbox:
        label _("Ctrl")
        text _("押し続けている間スキップする。")

    hbox:
        label "H"
        text _("インターフェースを隠す。")

    hbox:
        label "S"
        text _("スクリーンショットを撮る。")


init -501 screen mouse_help():

    hbox:
        label _("左クリック")
        text _("台詞を読み進める。またはボタンを選択する。")

    hbox:
        label _("中クリック")
        text _("インターフェースを隠す。")

    hbox:
        label _("右クリック")
        text _("ゲームメニューを開く。")


init -501 screen gamepad_help():

    hbox:
        label _("Ｒトリガー\nＡ／下ボタン")
        text _("台詞を読み進める。またはボタンを選択する。")

    hbox:
        label _("Ｌトリガー\nＬボタン")
        text _("前の台詞に戻る。")

    hbox:
        label _("Ｒボタン")
        text _("ロールバック中、次の台詞に進む。")


    hbox:
        label _("方向パッド\n左右スティック")
        text _("インターフェースを移動する。")

    hbox:
        label _("スタート、ガイド")
        text _("ゲームメニューを開く。")

    hbox:
        label _("Ｙ／上ボタン")
        text _("インターフェースを隠す。")

    textbutton _("キャリブレート") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 7

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 200
    right_padding 16

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0














init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 24

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 80

            textbutton _("はい") action yes_action
            textbutton _("いいえ") action no_action


    key "game_menu" action no_action


init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")

init -1 style confirm_button_text:
    properties gui.button_text_properties("confirm_button")








init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        ypos 0
        has hbox
        spacing 5

        text _("SKIP")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

init -501 screen auto_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        ypos 0
        has hbox
        spacing 5

        text _("AUTO")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:

    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")








transform -1 ctc_appear:
    alpha 0.0
    pause 5.0
    linear 0.5 alpha 1.0

init -501 screen creditskip:
    key "mousedown_1" action Call('creditskip')



label creditskip:
    stop music fadeout 2
    scene black with dissolve
    if credit == "sc":
        jump end_sc2
    elif credit == "ar":
        jump end_ar2
    elif credit == "rs":
        jump end_rs2
    elif credit == "gr":
        jump end_gr2
    elif credit == "cr":
        jump end_cr2
    elif credit == "hk":
        jump end_hk22
    elif credit == "nomal":
        if persistent.dmy == 5:
            jump end222
        else:
            $ persistent.dmy = 0
            jump end222
    else:
        $ MainMenu(confirm=False)()
    return


init -501 screen nvl(dialogue, items=None):
    if persistent.dmy >= 2:
        if persistent.dmy_off == False:
            key "mousedown_4" action Call('dmy_x')
            if persistent.dmy_skip_seen == False:
                key "K_LCTRL" action Call('dmy_skip')
            else:
                key "K_LCTRL" action Call('dmy_x')
        else:
            key "mousedown_4" action ShowMenu("history")
    else:
        key "mousedown_4" action ShowMenu("history")
    window:
        if nvl_window_off:
            style "nvl_window_off"
        else:
            style "nvl_window"

        vbox:
            spacing gui.nvl_spacing


            if gui.nvl_height:

                vpgrid:
                    cols 1
                    yinitial 1.0

                    use nvl_dialogue(dialogue)

            else:

                use nvl_dialogue(dialogue)



            for i in items:

                textbutton i.caption:
                    action i.action
                    style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id



define -1 config.nvl_list_length = gui.nvl_list_length

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background None
    padding gui.nvl_borders.padding

init -1 style nvl_window_off:
    xfill True
    yfill True

    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







init -1 style pref_vbox:
    variant "medium"
    xsize 360



init -501 screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("되감기") action Rollback()
            textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("자동진행") action Preference("auto-forward", "toggle")
            textbutton _("메뉴") action ShowMenu()


init -1 style window:
    variant "small"
    background "gui/phone/textbox.png"

init -1 style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

init -1 style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

init -1 style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 272

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 320

init -1 style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

init -1 style slider_pref_vbox:
    variant "small"
    xsize None

init -1 style slider_pref_slider:
    variant "small"
    xsize 480
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
