

image splash:
    xalign 0.5
    yalign 0.5
    "logo.png"


image ctc_blink:
    "ctc.png"
    pause 0.2
    "ctc_0.png"
    pause 0.2
    "ctc_1.png"
    pause 0.2
    "ctc_0.png"
    pause 0.2
    repeat

image ctc_ent:
    "ctc_ent_0.png"
    pause 0.2
    "ctc_ent.png"
    pause 0.2
    "ctc_ent_1.png"
    pause 0.2
    "ctc_ent.png"
    pause 0.2
    repeat

image ctc_br:
    blur 2
    "ctc.png"
    pause 0.2
    "ctc_0.png"
    pause 0.2
    "ctc_1.png"
    pause 0.2
    "ctc_0.png"
    pause 0.2
    repeat



init:
    image mouse_cursor_blur:
        blur 10
        zoom 1.5
        'mouse.png'
        alpha 0.5
        pause 0.24
        'mouse_1.png'
        alpha 0.5
        pause 0.24
        repeat

init:
    image mouse_cursor:
        blur 3
        'mouse.png'
        alpha 0.5
        pause 0.24
        'mouse_1.png'
        alpha 0.5
        pause 0.24
        repeat



image BG12_ns = im.MatrixColor(
    "BG12.png",
    im.matrix.colorize("#000", "#f00")*im.matrix.contrast(5.0))

transform ns:
    xpos 0.0
    ypos 0.0
    zoom 4.0
    pause 0.05
    repeat


image bg104_ns = im.MatrixColor(
    "bg105.png",
    im.matrix.brightness(-0.6)*im.matrix.contrast(1.5))



init python:
    class TrackCursor(renpy.Displayable):
        
        def __init__(self, child):
            
            super(TrackCursor, self).__init__()
            
            self.child = renpy.displayable(child)
            
            self.x = None
            self.y = None
        
        def render(self, width, height, st, at):
            
            rv = renpy.Render(width, height)
            
            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))
            
            return rv
        
        def event(self, ev, x, y, st):
            
            if (x != self.x) or (y != self.y):
                self.x = x +20
                self.y = y -20
                renpy.redraw(self, 0)


init python:
    class TrackCursor2(renpy.Displayable):
        
        def __init__(self, child):
            
            super(TrackCursor2, self).__init__()
            self.child = renpy.displayable(child)
            self.x = None
            self.y = None
        
        def render(self, width, height, st, at):
            
            rv = renpy.Render(width, height)
            
            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))
            
            return rv
        
        def event(self, ev, x, y, st):
            
            if (x != self.x) or (y != self.y):
                self.x = x -20
                self.y = y +420
                renpy.redraw(self, 0)


init python:
    class TrackCursor3(renpy.Displayable):
        
        def __init__(self, child):
            
            super(TrackCursor3, self).__init__()
            self.child = renpy.displayable(child)
            self.x = None
            self.y = None
        
        def render(self, width, height, st, at):
            
            rv = renpy.Render(width, height)
            
            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))
            
            return rv
        
        def event(self, ev, x, y, st):
            
            if (x != self.x) or (y != self.y):
                self.x = x -30
                self.y = y +100
                renpy.redraw(self, 0)



init python:
    class TrackCursor4(renpy.Displayable):
        
        def __init__(self, child):
            
            super(TrackCursor4, self).__init__()
            self.child = renpy.displayable(child)
            self.x = None
            self.y = None
        
        def render(self, width, height, st, at):
            
            rv = renpy.Render(width, height)
            
            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))
            
            return rv
        
        def event(self, ev, x, y, st):
            
            if (x != self.x) or (y != self.y):
                self.x = x +648
                self.y = y +150
                renpy.redraw(self, 0)


init python:
    class TrackCursor0(renpy.Displayable):
        
        def __init__(self, child):
            
            super(TrackCursor0, self).__init__()
            self.child = renpy.displayable(child)
            self.x = None
            self.y = None
        
        def render(self, width, height, st, at):
            
            rv = renpy.Render(width, height)
            
            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))
            
            return rv
        
        def event(self, ev, x, y, st):
            
            if (x != self.x) or (y != self.y):
                self.x = x +20
                self.y = y +20
                renpy.redraw(self, 0)


screen TrackCursor:
    zorder 100
    add TrackCursor0("mouse_cursor_blur")
    add TrackCursor("mouse_cursor")
    add TrackCursor2("mouse_cursor")
    add TrackCursor3("mouse_cursor")
    add TrackCursor4("mouse_cursor")





image nvlb:
    "ui_nvl.png"

image texb:
    "ui_textbox.png"

screen textbox:
    zorder 0
    add "ui_textbox.png" yalign 1.0

screen nvlbox:
    zorder 0
    add "ui_nvl.png" yalign 1.0

init:
    transform box_on:
        yalign 1.0
        alpha 0




label nvlb_on:
return

label nvlb_off:
    show nvlb
    hide nvlb with dissolve
return

label texb_on:
    show texb with dissolve
    hide texb
    return

label texb_off:
    show texb
    hide texb with dissolve
    return


screen set_name(title, init_name):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 20
        text title xalign 0.5
        input default init_name xalign 0.5
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
