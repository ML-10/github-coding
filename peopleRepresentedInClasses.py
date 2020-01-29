class Location:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction

class LivingThing:
    def __init__(self, name, age, alive):
        self.name = name
        self.age = age
        if age > 120:
            self.die()
    def die(self):  
        self.alive = False
        print(self.name, 'has died.')
        
class Person(LivingThing):
    def __init__(self, name, age, weight, height, location, alive=True):
        super().__init__(name, age, alive)
        self.weight = weight
        self.height = height
        self.location = location
        print('Person has been spawned.')
        if age > 120:
            self.die()
        
    def say(self, text='Hi'):
        if self.alive:
            print(self.name + ': ' + text)
        else:
            raise RuntimeError('object is dead')
            
    def die(self):
        self.alive = False
        print(self.name, 'has died.')
        
    def forward(self, steps=1):
        if self.alive:
            if self.location.direction == 'x':
                self.location.x += steps
            elif self.location.direction == 'y':
                self.location.y += steps
            elif self.location.direction == '-x':
                self.location.x -= steps
            elif self.location.direction == '-y':
                self.location.y -= steps
            else:
                raise ValueError('location.direction is invalid')
            print(self.name, 'is at location (' + str(self.location.x)+',', str(self.location.y) + ').')
        else:
            raise RuntimeError('object is dead')
    def backward(self, steps=1):
        if self.alive:
            if self.location.direction == 'x':
                self.location.x -= steps
            elif self.location.direction == 'y':
                self.location.y -= steps
            elif self.location.direction == '-x':
                self.location.x += steps
            elif self.location.direction == '-y':
                self.location.y += steps
            else:
                raise ValueError('location.direction is invalid')
            print(self.name, 'is at location (' + str(self.location.x)+',', str(self.location.y) + ').')
        else:
            raise RuntimeError('object is dead')
    def turn(self, direction):
        if self.alive:
            if direction == 'left':
                if self.location.direction == 'x':
                    self.location.direction = 'y'
                elif self.location.direction == 'y':
                    self.location.direction = '-x'
                elif self.location.direction == '-x':
                    self.location.direction = '-y'
                elif self.location.direction == '-y':
                    self.location.direction = 'x'
                else:
                    raise ValueError('direction is invalid')

            if direction == 'right':
                if self.location.direction == 'x':
                    self.location.direction = '-y'
                elif self.location.direction == 'y':
                    self.location.direction = 'x'
                elif self.location.direction == '-x':
                    self.location.direction = 'y'
                elif self.location.direction == '-y':
                    self.location.direction = '-x'
                else:
                    raise ValueError('direction is invalid')
        else:
                raise RuntimeError('object is dead')
        print('self.name'+"'s direction is", direction+'.')
    def grow(self, diffAge=0, diffHeight=0, diffWeight=0):
        if self.alive:
            self.age += diffAge
            self.height += diffHeight
            self.weight += diffWeight
            if age > 120:
                self.die()
            print(self.name, 'is now', str(self.age) + ',', str(self.height), 'tall, and', str(self.weight), 'heavy.')
        else:
            raise RuntimeError('object is dead')
    def burp(self):
        if self.alive:
            from winsound import PlaySound, SND_ASYNC, SND_NODEFAULT
            PlaySound(r'C:\Users\sophi\Desktop\matthews things\python files\__pycache__\__pycache__\alien\burpsnd.wav', SND_ASYNC | SND_NODEFAULT)
            print(self.name, 'has now burped.')
        else:
            raise RuntimeError('object is dead')
class Shark(LivingThing):
    def __init__(self,name, age, alive, typeOfShark='Great White Shark'):
        super().__init__(name, age, alive)
        self.typeOfShark = typeOfShark
        
    def forward(self, steps=1):
        if self.alive:
            if self.location.direction == 'x':
                self.location.x += steps
            elif self.location.direction == 'y':
                self.location.y += steps
            elif self.location.direction == '-x':
                self.location.x -= steps
            elif self.location.direction == '-y':
                self.location.y -= steps
            else:
                raise ValueError('location.direction is invalid')
            print(self.name, 'is at location (' + str(self.location.x)+',', str(self.location.y) + ').')
        else:
            raise RuntimeError('object is dead')
        
    def backward(self, steps=1):
        if self.alive:
            if self.location.direction == 'x':
                self.location.x -= steps
            elif self.location.direction == 'y':
                self.location.y -= steps
            elif self.location.direction == '-x':
                self.location.x += steps
            elif self.location.direction == '-y':
                self.location.y += steps
            else:
                raise ValueError('location.direction is invalid')
            print(self.name, 'is at location (' + str(self.location.x)+',', str(self.location.y) + ').')
        else:
            raise RuntimeError('object is dead')
        
    def turn(self, direction):
        if self.alive:
            if direction == 'left':
                if self.location.direction == 'x':
                    self.location.direction = 'y'
                elif self.location.direction == 'y':
                    self.location.direction = '-x'
                elif self.location.direction == '-x':
                    self.location.direction = '-y'
                elif self.location.direction == '-y':
                    self.location.direction = 'x'
                else:
                    raise ValueError('direction is invalid')

    def kill(self, thing):
        if self.alive:     
            thing.die()
        else:
            raise RuntimeError('object is dead')
    def eat(self, thing):
        if self.alive:
            del thing
            print(self.name, 'has eaten', thing.name+'.')
        else:
            raise RuntimeError('object is dead')
