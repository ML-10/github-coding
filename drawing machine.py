from turtle import *
def turtle_controller(do, val):
    do = do.upper()
    if do == 'F':
        fd(val)
    elif do == 'B':
        bk(val)
    elif do == 'R':
        rt(val)
    elif do == 'L':
        lt(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print('Unrecognized command')
def string_artist(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ':', cmd_type, num)
        turtle_controller(cmd_type, num)
instructions = '''Enter a program for the turtle:
e.g. F100-R45-U-F100-L45-D-F100-R90-B50
N = New Drawing
U/D = Pen Up/Down
F100 = Forwards 100
B100 = Backwards 100
R90 = Right 90 degrees
L90 = Left 90 degrees'''
screen = getscreen()
while True:
    t_program = screen.textinput('Drawing Machine', instructions)
    print(t_program)
    if t_program == None or t_program.upper() == 'END':
        break
    string_artist(t_program)
    
            
