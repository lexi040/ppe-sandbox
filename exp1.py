import expyriment

expyriment.io.Keyboard.set_quit_key(expyriment.misc.constants.K_ESCAPE)

expyriment.control.set_develop_mode(True)
expyriment.control.defaults.window_size = (800, 800)

start_point = (-250, 0)
end_point = (250, 0)
line_width = 20  
time = 2
size = (20, 20)

exp = expyriment.design.Experiment("test")
expyriment.control.initialize(exp)

line = expyriment.stimuli.Line(start_point, end_point, line_width, (255,255,255))
line.preload()

square = expyriment.stimuli.Rectangle(size, (255,255,255), line_width , None, start_point )
square.preload()

expyriment.control.start()

canvas = expyriment.stimuli.BlankScreen()

square.present()
expyriment.misc.Clock.wait_seconds(time)
line.present()
exp.keyboard.wait()

expyriment.control.end()