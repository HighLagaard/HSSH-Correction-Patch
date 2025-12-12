

default preferences.skip_unseen = False

init python:
    config.language = persistent.current_lang


define config.has_autosave = False

define config.gl2 = True


define config.layers = [ 'master', 'transient','say', 'screens', 'on_screens', 'overlay' ]

style default:
    antialias False
default preferences.gl_framerate = None



define config.name = _("Happy Saint Sheol")

define config.mouse = { 'default' : [ ('mouse.png', 0, 0), ('mouse.png', 0, 0), ('mouse.png', 0, 0), ('mouse.png', 0, 0), ('mouse.png', 0, 0), ('mouse_1.png', 0, 0),('mouse_1.png', 0, 0), ('mouse_1.png', 0, 0), ('mouse_1.png', 0, 0)]}


define config.hard_rollback_limit = 0
define config.rollback_enabled = False

define gui.show_name = False
define nvl_window_off = False


define config.version = "1.3.1 Steam Version"





define build.name = "HSSH"
define build.directory_name = "HSSH-1.3.1"


define config.has_sound = True
define config.has_music = True
define config.has_voice = False






define config.main_menu_music = "audio/bgm/title.ogg"





define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.end_splash_transition = dissolve

define config.game_main_transition = dissolve
define config.intra_transition = dissolve


define config.after_load_transition = dissolve


define config.end_game_transition = dissolve







define config.window = "hide"
define config.window_show_transition = dissolve
default persistent.p_end = False





default preferences.text_cps = 20


default preferences.afm_time = 10








define config.save_directory = "hssh_steam-1726667658"



define config.window_icon = "gui/window_icon.png"



init python:

    build.archive("image", "all")
    build.archive("script", "all")
    build.archive("archive1","all")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.rpym', None)
    build.classify('**.clip', None)
    build.classify('**.ini', None)

    build.classify('game/audio/**', 'archive')
    build.classify('game/gui/**', 'archive')
    build.classify('game/*.png', 'archive')
    build.classify('**.webm', 'archive')    
    build.classify('**.ttc', 'archive')
    build.classify('**.ttf', 'archive')
    build.classify('**.otf', 'archive')



    build.classify('game/*.rpyc', 'archive')

    build.classify('game/gal/**', 'archive')
    build.classify('game/images/**', 'archive')

    build.classify('game/tl/**', 'archive')


    build.documentation('*.html')
    build.documentation('*.txt')
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
