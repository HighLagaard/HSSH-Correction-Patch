"Wave Shader Text Tag Ren'Py Module 2022 Daniel Westfall <SoDaRa2595@gmail.com>"
"http://twitter.com/sodara9 I'd appreciate being given credit if you do end up using it! :D Would really make my day to know I helped some people out! Really hope this can help the community create some really neat ways to spice up their dialogue! http://opensource.org/licenses/mit-license.php Github: https://github.com/SoDaRa/RenpyWaveShader itch.io: https://wattson.itch.io/renpy-wave-shader Forum Post: https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=64378"






























init python:























    def wavy_tag(tag, argument, contents):
        new_list = [ ]
        amp, period, speed, dir, double, melt = 12, 20, 1, 'both', None, None
        tag_shader = WaveShader()
        if len(argument) > 0 and argument[0] == 'n':
            shader_name = argument[1:]
            copy_shader = globals()[shader_name]
            if isinstance(copy_shader, WaveShader):
                tag_shader = copy_shader
        elif len(argument) > 0:
            argument = argument.split('-')
            dir_dict = {'b':'both', 'x':'x', 'y':'y'}
            for arg in argument:
                if 'a' in arg:
                    amp = float(arg[1:])
                if 'p' in arg:
                    period = float(arg[1:])
                if 's' in arg:
                    speed = float(arg[1:])
                if 'w' in arg:
                    dir = dir_dict[arg[1]]
                if 'd' in arg:
                    double = dir_dict[arg[1]]
                if 'm' in arg:
                    melt = dir_dict[arg[1]]
            tag_shader = WaveShader(amp=amp, period=period, speed=speed, direction=dir, double=double, melt=melt)
        my_style = DispTextStyle() 
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                text = Text(my_style.apply_style(text), slow = True)
                char_disp = At(text, globals()['WaveShaderApplyer'](tag_shader))
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    config.custom_text_tags["wave"] = wavy_tag

transform WaveShaderApplyer(func):
    function func
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
