from math import sin, cos
while True:
    try:
        v_i = int(input('Initial velocity (m/s²): '))
    	theta = int(input('Angle at which projectile is fired (degrees): '))
    	g = 9.80665
        r = str((2 * v_i ** 2 * sin(theta) * cos(theta)) / g)
        print('Range of projectile in vacuum: ' + r + ' meters')
    except:
	v_i = float(input('Initial velocity (m/s²): '))
    	theta = float(input('Angle at which projectile is fired (degrees): '))
    	g = 9.80665
        r = str((2 * v_i ** 2 * sin(theta) * cos(theta)) / g)
        print('Range of projectile in vacuum: ' + r + ' meters')
    
