from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarted.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member of your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly sin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input(">")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your laser hits his costume but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "make him fly into an insane rage and blast you repeatly in the face until"
            print "you are dead. Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "blah blah"
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "blah blah"
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "blah blah"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]>")

        if guess == code:
            print "The container clicks open and the seals breaks, letting gas out."
            print "blah blah"
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "blah blah"
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print "You brust onto the Bridge with the netron destruct bomb"
        print "blah blah"

        action = raw_input(">")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "blah blah"
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "blah blah"
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "blah blah"

        good_pod = randint(1, 5)
        guess = raw_input("[pod #]>")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "blah blah"
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "blah blah"

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'



class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
