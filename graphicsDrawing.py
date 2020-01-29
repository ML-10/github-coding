from time import *
from random import *
from graphics import *
def printOnScreen(win, text, color, x, y):
	text = Text(Point(x, y), text)
	text.setTextColor(color)
window = GraphWin("My Window", 1000, 1000)
realColor = choice(choice(choice(choice(choice('red',
                                               'orange'), 'yellow'), 'green'), 'blue'), 'purple')
head = Circle(Point(500, 500), 500)
head.setFill(realColor)
head.draw(window)
for i in range(1, 11):
	color = input('What color do you see?').upper()
	if realColor.upper() == color:
		print('Correct!')
		print('Next {0} of 10'.format(i))
	else:
		print('Incorrect!')
		break
printOnScreen(window, 'Game Over!', 'red', 500, 500)
window.getMouse()
window.close()
