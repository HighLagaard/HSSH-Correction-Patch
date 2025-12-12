

define dist_char_hk = Text('ハク', font='KH-Dot-Dougenzaka-12.ttf', color="#ffe594", size=35)
define dist_hk1 = Text("素敵な出逢いを巡らせてくださった神に感謝、{vspace=10}を……♪",font='KH-Dot-Dougenzaka-12.ttf', slow_cps=4, size=28)
define BG12 = Image("bg12.png")
define BG05 = Image("bg05.png")
define BG04 = Image("bg04.png")
define BG06 = Image("bg06.png")
define BG102 = Image("bg102.png")
define BG105 = Image("bg105.png")
define BG106 = Image("bg106.png")
define CG08 = Image("cg08.png")

init python:
    import math
    import pygame
    dist_texb = Image("ui_textbox.png")
    dist_bg04_1 = Image("BG04_1.png")
    dist_SCG_05 = Image('char/ch_05_hk/1smile.png')
    class Mirage(renpy.Displayable):
        def __init__(self,image):
            super(renpy.Displayable,self).__init__()
            self.start_image = image
            self.W2 = config.screen_width/2
            self.H2 = config.screen_height/2
            self.amplitude = 0.02
            self.wavelength = 100
        
        
        
        def render(self,width,height,st,at):
            render = renpy.Render(0, 0)
            self.img = self.start_image
            self.img = self.makeScanlines(self.img)   
            h = 1.0
            for scanline in self.img:
                zoom_factor = 1.0-self.amplitude
                
                self.t = Transform(scanline, xzoom=(1/zoom_factor)+(math.sin(h/self.wavelength + st)*self.amplitude), yzoom=(1.00))
                h +=1.0
                child_render = renpy.render(self.t, 10000, 0, st, at)
                cW,cH = child_render.get_size()
                
                render.blit(child_render, ((self.W2)-(cW/2),h - 0))
            renpy.redraw(self, 0.1)
            return render
        
        
        def makeScanlines(self, base_image):
            cut = []
            child_render = renpy.render(base_image, config.screen_width, config.screen_height, 0, 0)
            width = int(child_render.get_size()[0]) 
            height = int(child_render.get_size()[1])
            cut = [Transform(base_image, crop=(0,i,width,1)) for i in range(height)]
            return cut



init:

    define Dist_texb = Mirage(dist_texb)
    define DistBG04_1 = Mirage(dist_bg04_1)
    define Dist_SCG_05 = Mirage(dist_SCG_05)
    define Dist_char_hk = Mirage(dist_char_hk)
    define Dist_hk1 = Mirage(dist_hk1)
    define Dist_BG12 = Mirage(BG12)
    define dist_bg04 = Mirage(BG04)
    define dist_bg05 = Mirage(BG05)
    define dist_bg06 = Mirage(BG06)
    define dist_bg102 = Mirage(BG102)
    define dist_bg105 = Mirage(BG105)
    define dist_bg106 = Mirage(BG106)
    define dist_cg08 = Mirage(CG08)




screen grumble:
    add DistBG04_1
    add Dist_SCG_05 yalign -0.075
    add Dist_texb ypos 520
    add dist_char_hk ypos 563 xpos 197
    add Dist_hk1 ypos 623


screen grumbleBG12:
    add Mirage(BG12)
screen grumble_bg04:
    zorder -1
    add Mirage(BG04)

screen grumble_bg05:
    zorder -1
    add Mirage(BG05)

screen grumble_bg06:
    zorder -1
    add Mirage(BG06)

screen grumble_bg102:
    zorder -1
    add Mirage(BG102)

screen grumble_bg105:
    zorder -1
    add Mirage(BG105)

screen grumble_bg106:
    zorder -1
    add Mirage(BG106)

screen grumble_cg08:
    zorder -1
    add Mirage(CG08) yoffset -500

screen grumble_cg082:
    zorder -1
    add Mirage(CG08) yoffset -400
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
