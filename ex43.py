from sys import exit

class Scene(object):
	def enter(self):
		print "Has yet to be implemented."
		exit(1)

class Engine(object):
	def __init__(self, scene_map):
		print "## Welcome to the game ##"
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		print current_scene

		while True:
			print '\n------------'
			next_scene_name = current_scene.enter()
			print 'next scene', next_scene_name
			current_scene = self.scene_map.next_scene(next_scene_name)
			print 'map returns new scene ', current_scene

class Death(Scene):
	def enter(self):
		print "You have died. The game is now over, thanks for playing!"
		exit(1)

class CentralCorridor(Scene):
	def enter(self):
		print "\nYou are in the central corridor. Answer this equation to move to unlock the armory door."
		print "2+2 = ..."

		answer = raw_input('> ')

		if answer == "4":
			return 'laser_weapon_armory'
		else:
			return 'death'

class LaserWeaponArmory(Scene):
	def enter(self):
		print "\nYou are in the laser weapon armory room. Write the word 'cat' to pick up the bomb."

		answer = raw_input('> ')

		if answer == 'cat':
			return 'the_bridge'
		else:
			return 'death'

class TheBridge(Scene):
	def enter(self):
		print "\nYou are on the bridge. Write down 5 numbers to drop the bomb."

		answer = raw_input('> ')

		try:
			int(answer)
			if len(answer) == 5:
				return 'escape_pod'
		except ValueError:
			return 'death'

class EscapePod(Scene):
	def enter(self):
		print "\nYou have reached the escape pod! \n\n\tCongratualions.\n"
		exit(1)

class Map(object):
	scenes = {
		'central_corridor' : CentralCorridor(),
		'laser_weapon_armory' : LaserWeaponArmory(),
		'the_bridge' : TheBridge(),
		'escape_pod' : EscapePod(),
		'death' : Death()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
		print "start_scene in __init__ ", self.start_scene

	def next_scene(self, scene_name):
		print "start_scene in next_scene"
		val = Map.scenes.get(scene_name)
		print "next_scene returns ", val
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

