import random
import time
import sys
class Player(object):
	def __init__(self, name, weapon):
		self.name = name
		self.weapon = weapon
		self.health = 100
		self.exp = 0
	
#
#
#Function bits

sword_stats = [6, 4]
bow_stats = [8, 2]
axe_stats = [4, 6]


def weapon_check(player_weapon):
	if player_weapon == "1":
		print("You chose a sword!")
		player.weapon = sword_stats
	elif player_weapon == "2":
		print("You chose a bow!")
		player.weapon = bow_stats
	elif player_weapon == "3":
		print("You chose an axe!")
		player.weapon = axe_stats
	else:
		print("Please provide a valid input.")
		choose_weapon()

		
def choose_weapon():
	player_weapon_choice = input("Your choices are: Sword, Bow and Arrow, and an Axe. \nEnter 1 for a sword, 2 for a bow, and 3 for an axe: ")
	player.weapon = player_weapon_choice
	weapon_check(player.weapon)
	
	
def game_over_check():
	if player.health <= 0:
		print("You ran out of HP. RIP you. :(")
		time.sleep(2.5)
		sys.exit()
	else: 
		pass
	
def fight_run(level):
	enemy_list = ["n Ogre", " Goblin", "n Enemy Soldier", "n Unknown Hostile Creature"]
	print("You encounter a" + enemy_list[random.randint(0,3)] + "!")
	enemy_hp = random.randint(1, int((10 *  level)))
	enemy_attack = random.randint(1, int((5 * level)))
	exp_gain = 0.3 * enemy_hp + 0.7 * enemy_attack
	print("Enemy HP: " + str(enemy_hp))	
	print("Enemy Attack Power: " + str(enemy_attack))
	choice = input("Do you wish to fight or run? \nEnter 'fight' to fight, or press any other key to run. ")
	choice = choice.lower()
	if choice == "fight":
		print('Entering Battle...')
		time.sleep(1.0)
		while enemy_hp > 0:
			game_over_check()
			enemy_hp = enemy_hp - player.weapon[0]
			if enemy_attack > player.weapon[1]:
				player.health = player.health - (enemy_attack - player.weapon[1])
			else:
				pass
			print('You attack for ' + str(player.weapon[0]) + " damage!")
			print("Enemy attacks for " + str(enemy_attack) + " damage! \nYou block " + str(player.weapon[1]) + " damage!")
			print("Your health is " + str(player.health) + ".")
			if enemy_hp > 0:
				print("Enemy HP at " + str(enemy_hp) + ".")
			time.sleep(3.0)
		print("You defeated the enemy! \nYou gain " + str(exp_gain) + " expereince!")
		player.exp = player.exp + exp_gain
		player_exp_check()
	else:
		run_prob = random.randint(1, 10)
		if run_prob > 4:
			print("Escape successful!")
		else:
			print("Escape failed! Entering battle...")
			time.sleep(1.0)
			while enemy_hp > 0:
				game_over_check()
				enemy_hp = enemy_hp - player.weapon[0]
				if enemy_attack > player.weapon[1]:
					player.health = player.health - (enemy_attack - player.weapon[1])
				else:
					pass
				print('You attack for ' + str(player.weapon[0]) + " damage!")
				print("Enemy attacks for " + str(enemy_attack) + " damage! \nYou block " + str(player.weapon[1]) + " damage!")
				print("Your health is " + str(player.health) + ".")
				if enemy_hp > 0:
					print("Enemy HP at " + str(enemy_hp) + ".")
				time.sleep(3.0)
			print("You defeated the enemy! \nYou gain " + str(exp_gain) + " expereince!")
			player.exp = player.exp + exp_gain
			player_exp_check()
			

def story_fork_one_input():
	print("You see a fork in the road.")
	direction_input_1 = input("Which direction would you like to go? \nNorth, East, South, or West? ")
	story_fork_one(direction_input_1)


def story_fork_one(input):
	input = input.lower()
	if input == 'north':
		print("The enemies here seem to be experienced.")
		fight_run(2.5)
		time.sleep(3.0)
		turnback_north_one()
		print("As you continue to venture north, the weather gets colder. \nYou were not prepared for this...")
		time.sleep(3.0)
		fight_run(3.0)
		print("You are tired after the battle. \nMaybe it wouldn't be a bad idea to rest under this tree...")
		make_tree()
		time.sleep(4.0)
		print("You wake up refreshed, albeit quite cold.")
		print("Looking around, you see something sticking out of the tree's roots. \nPicking it up, you find a mysterious liquid in a bottle.")
		time.sleep(2.0)
		print("Being adventerous, you decide to drink the liquid. \nYour muscles feel energized, and as you stretch, you realize you have grown stronger!")
		player.weapon[0] = player.weapon[0] + 2
		time.sleep(2.0)
		print("Attack increased by 2! \nGood timing that, you mutter as you see an enemy approaching...")
		fight_run(3.5)
	elif input == 'east':
		print("The enemies here seem to be very experienced.")
		fight_run(3.0)
	elif input == 'west':
		print("The enemies here seem to be inexpereienced.")
		fight_run(1.0)
	elif input == 'south':
		print("The enemies here seem to be experienced.")
		fight_run(2.0)
	else:
		print("Invalid input. Please provide a valid input.")
		story_fork_one_input()
		
def player_exp_check():
	if player.exp >= 20:
		exp_check_one = 0
		if exp_check_one == 0:
			print("Your experience caused you to increase stats! \nHealth, attack, and defense increase!")
			player.health = player.health + 15
			print("Health now at " + str(player.health) + "!")
			player.weapon[0] = player.weapon[0] + 2
			player.weapon[1] = player.weapon[1] + 2
		exp_check_one = exp_check_one + 1
	
			
			
def turnback_north_one():
	fork_back_one = 'y'
	fork_back_one = input("There's not much here. Do you turn back? \nEnter 'y' for yes and 'n' for no. ")
	if fork_back_one.lower() == 'y':
		story_fork_one_input()
	elif fork_back_one.lower() == 'n':
		print("You continue northward.")
	else:
		print("Invalid input. Please enter a valid input")
		turnback_north_one()
		
def make_tree():
	print("       _-_ \n    /~~   ~~\ \n /~~         ~~\ \n{               } \n \  _-     -_  / \n   ~  \\ //  ~ \n_- -   | | _- _ \n  _ -  | |   -_ \n      // \\")
#
#
#Setup bits	
print("Hello. Welcome to MARIO KART NINE! JK, this is a text based game. \nI don't think you could play Mario Kart in Python.")
player_character = input("Please write your name here: ")
player = Player(player_character, 0)
print("Welcome " + str(player_character) + "!")
print("Choose your weapon. Each has its own advantages and disadvantages. \nSwords have balanced defensive and offensive capabilities. \nBows have excellent offensive but weak defensive capabilites. \nAxes have weak offensive but excellent defensive capabilities.")
choose_weapon()



#
#
#Story bits
print("Here is the story: *add story here* ")
fight_run(1.5)
time.sleep(3.0)
print("You begin on your quest after defeating the enemy.")
story_fork_one_input()


#story: you want to overthrow the monster government because they stole your crap.
#they are suprisingly inept and you just have to kill the king to dissolve the government

#
#
# Dev Notes: weird funciton crap, turnback code does not work if within other fuction.