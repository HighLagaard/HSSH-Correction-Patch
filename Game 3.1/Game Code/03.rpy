









init -2 python:
    gui.init(1024, 768)

define -2 dissolve = ImageDissolve ( "gui/trans.png" ,  0.8 )










define -2 gui.accent_color = 'ffffff'



define -2 gui.idle_color = '#ffffff'



define -2 gui.idle_small_color = '#888888'


define -2 gui.hover_color = '333333'




define -2 gui.selected_color = '#555555'


define -2 gui.insensitive_color = '#aaaaaa7f'



define -2 gui.muted_color = '#666666'
define -2 gui.hover_muted_color = '#999999'


define -2 gui.text_color = '#ffffff'



define -2 gui.interface_text_color = '#ffffff'





define -2 gui.text_font = "HSSH.ttf"


define -2 gui.name_text_font = "KH-Dot-Dougenzaka-16.ttf"

define -2 gui.history_text_font = "KH-Dot-Dougenzaka-12.ttf"
define -2 gui.interface_text_font = "KH-Dot-Dougenzaka-16.ttf"


define -2 gui.text_size = 36


define -2 gui.name_text_size = 36


define -2 gui.interface_text_size = 30


define -2 gui.label_text_size = 28


define -2 gui.notify_text_size = 28


define -2 gui.title_text_size = 36

default -2 persistent.p_sheol_end = False


default persistent.titlename = "def"

default persistent.title_my = False
default persistent.title_sc = False
default persistent.title_ar = False
default persistent.title_rs = False
default persistent.title_gr = False
default persistent.title_cr = False
default persistent.title_hk = False

init -2:
    $ persistent.main_menu = "gui/main_menu/[persistent.titlename].png"

define -2 gui.main_menu_background = persistent.main_menu

define -2 gui.game_menu_background = "gui/game_menu.png"




define -2 gui.textbox_height = 280



define -2 gui.textbox_yalign = 1.0




define -2 gui.name_xpos = 118
define -2 gui.name_ypos = 10



define -2 gui.name_xalign = 0.0



define -2 gui.namebox_width = None
define -2 gui.namebox_height = None



define -2 gui.namebox_borders = Borders(5, 5, 5, 5)



define -2 gui.namebox_tile = False




define -2 gui.dialogue_xpos = 138
define -2 gui.dialogue_ypos = 50


define -2 gui.dialogue_width = 764



define -2 gui.dialogue_text_xalign = 0.0









define -2 gui.button_width = None
define -2 gui.button_height = None


define -2 gui.button_borders = Borders(4, 4, 4, 4)



define -2 gui.button_tile = False


define -2 gui.button_text_font = gui.interface_text_font


define -2 gui.button_text_size = gui.interface_text_size


define -2 gui.button_text_idle_color = gui.idle_color
define -2 gui.button_text_hover_color = gui.hover_color
define -2 gui.button_text_selected_color = gui.selected_color
define -2 gui.button_text_insensitive_color = gui.insensitive_color


define -2 gui.button_text_xalign = 0.0







define -2 gui.radio_button_borders = Borders(15, 4, 4, 4)

define -2 gui.check_button_borders = Borders(15, 4, 4, 4)

define -2 gui.confirm_button_text_xalign = 0.5

define -2 gui.page_button_borders = Borders(8, 4, 8, 4)

define -2 gui.quick_button_borders = Borders(8, 4, 8, 0)
define -2 gui.quick_button_text_size = 28
define -2 gui.quick_button_text_idle_color = gui.idle_small_color
define -2 gui.quick_button_text_selected_color = gui.accent_color












define -2 gui.choice_button_width = 700
define -2 gui.choice_button_height = 80
define -2 gui.choice_button_tile = False
define -2 gui.choice_button_borders = Borders(50, 25, 50, 4)
define -2 gui.choice_button_text_font = gui.text_font
define -2 gui.choice_button_text_size = gui.text_size
define -2 gui.choice_button_text_xalign = 0.5
define -2 gui.choice_button_text_idle_color = "#ffffff"
define -2 gui.choice_button_text_hover_color = "#333333"
define -2 gui.choice_button_text_insensitive_color = "#444444"









define -2 gui.slot_button_width = 280
define -2 gui.slot_button_height = 210
define -2 gui.slot_button_borders = Borders(0, 0, 0, 0)
define -2 gui.slot_button_text_size = 24
define -2 gui.slot_button_text_xalign = 0.5
define -2 gui.slot_button_text_idle_color = gui.idle_small_color
define -2 gui.slot_button_text_selected_idle_color = gui.selected_color
define -2 gui.slot_button_text_selected_hover_color = gui.hover_color


define -2 config.thumbnail_width = 280
define -2 config.thumbnail_height = 210


define -2 gui.file_slot_cols = 2
define -2 gui.file_slot_rows = 2







define -2 gui.navigation_xpos = 32


define -2 gui.skip_ypos = 8


define -2 gui.notify_ypos = 36


define -2 gui.choice_spacing = 30


define -2 gui.navigation_spacing = 4


define -2 gui.pref_spacing = 8


define -2 gui.pref_button_spacing = 0


define -2 gui.page_spacing = 0


define -2 gui.slot_spacing = 40


define -2 gui.main_menu_text_xalign = 1.0







define -2 gui.frame_borders = Borders(4, 4, 4, 4)


define -2 gui.confirm_frame_borders = Borders(32, 32, 32, 32)


define -2 gui.skip_frame_borders = Borders(13, 4, 40, 4)


define -2 gui.notify_frame_borders = Borders(13, 4, 32, 4)


define -2 gui.frame_tile = False











define -2 gui.bar_size = 20
define -2 gui.scrollbar_size = 10
define -2 gui.slider_size = 20



define -2 gui.bar_tile = False
define -2 gui.scrollbar_tile = True
define -2 gui.slider_tile = True


define -2 gui.bar_borders = Borders(4, 4, 4, 4)
define -2 gui.scrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.slider_borders = Borders(4, 4, 4, 4)


define -2 gui.vbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vslider_borders = Borders(4, 4, 4, 4)



define -2 gui.unscrollable = "hide"







define -2 config.history_length = 30



define -2 gui.history_height = None


define -2 gui.history_name_xpos = 0
define -2 gui.history_name_ypos = 0
define -2 gui.history_name_width = 180
define -2 gui.history_name_xalign = 0.0


define -2 gui.history_text_xpos = 180
define -2 gui.history_text_ypos = 2
define -2 gui.history_text_width = 542
define -2 gui.history_text_xalign = 0.0


init -2 style say_dialogue:
    kerning 1.0
    line_leading 10.0







define -2 gui.nvl_borders = Borders(0, 8, 0, 16)



define -2 gui.nvl_list_length = None



define -2 gui.nvl_height = None



define -2 gui.nvl_spacing = 15


define -2 gui.nvl_name_xpos = 344
define -2 gui.nvl_name_ypos = 0
define -2 gui.nvl_name_width = 120
define -2 gui.nvl_name_xalign = 1.0


define -2 gui.nvl_text_xpos = 72
define -2 gui.nvl_text_ypos = -20
define -2 gui.nvl_text_width = 900
define -2 gui.nvl_text_xalign = 0.0



define -2 gui.nvl_thought_xpos = 112
define -2 gui.nvl_thought_ypos = 0
define -2 gui.nvl_thought_width = 800
define -2 gui.nvl_thought_xalign = 0.0


define -2 gui.nvl_button_xpos = 140
define -2 gui.nvl_button_height = 40
define -2 gui.nvl_button_xalign = 0.0







define -2 gui.language = "unicode"






init -2 python:
    if renpy.variant("touch"):
        
        gui.quick_button_borders = Borders(32, 12, 32, 0)
    if renpy.variant("small"):
        
        
        gui.text_size = 24
        gui.name_text_size = 29
        gui.notify_text_size = 20
        gui.interface_text_size = 24
        gui.button_text_size = 24
        gui.label_text_size = 28
        
        
        gui.textbox_height = 192
        gui.name_xpos = 64
        gui.text_xpos = 72
        gui.text_width = 880
        
        
        gui.slider_size = 29
        
        gui.choice_button_width = 992
        
        gui.navigation_spacing = 16
        gui.pref_button_spacing = 8
        
        gui.history_height = 152
        gui.history_text_width = 552
        
        gui.quick_button_text_size = 25
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        
        gui.nvl_height = 136
        
        gui.nvl_name_width = 244
        gui.nvl_name_xpos = 260
        
        gui.nvl_text_width = 732
        gui.nvl_text_xpos = 276
        gui.nvl_text_ypos = 4
        
        gui.nvl_thought_width = 992
        gui.nvl_thought_xpos = 16
        
        gui.nvl_button_width = 992
        gui.nvl_button_xpos = 16
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
