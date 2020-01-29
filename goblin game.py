from random import randint
class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

class Human(GameObject):
    def __init__(self, name):
        self.class_name = "human"
        self.health = 5
        self._desc = "One of your kind"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 5:
            return self._desc
        elif self.health == 4 or self.health == 3:
            health_line = "It has a wound on its head."
        elif self.health == 2 or self.health == 1:
            health_line = "Its right arm has broken!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value
	def self_hit(noun):
	    if noun in GameObject.objects:
                    thing = GameObject.objects[noun]
                        if type(thing) == Goblin:
                            thing.health -= 1
                                if thing.health <= 0:
                                    msg = "You killed the {}!".format(thing.class_name)
                                else:
                                    msg = "You hit the {}".format(thing.class_name)
                                else:
                                    msg = "There is no {} here.".format(noun)
            return msg
class User(GameObject):
    def __init__(self, name):
        self.class_name = "user"
        self.health = 5
        self._desc = "You"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 5:
            return self._desc
        elif self.health == 4 or self.health == 3:
            health_line = "You have a wound on your head."
        elif self.health == 2 or self.health == 1:
            health_line = "Your right arm is broken!"
        elif self.health <= 0:
            health_line = "You are dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value		
		

goblin = Goblin('')
human = Human('')
user = User('')

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health -= 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)

def say(noun):
    return 'You said "{}"'.format(noun)

def next():
	if randint(1, 2) = 1:
		Human.self_hit(user)
	else:
		Human.self_hit(goblin)

def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))





verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit
	"next": next
}

while True:
    get_input()
