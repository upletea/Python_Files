import random

rooms=['The Room of Reckoning💡','Waters of Undoing🌊','Sanctum of Storms⛈️','The Ember Vault🔥' , 'The Oasis Chamber🌵','The Glacial Depths🧊 ','Center of the Elements']
rooms_text=['You wake up to a deep groaning sound, head pounding and heart racing. "Where am I?" you wonder.  ','you slip into the water and start to choke','', ]


#game_map =

player_health = 100 
enemy_damage = random.choices(5, 0, 10, 15, 20, 40)
enemy_health = random.choices(50, 100, 75, 150, 125, 25)

enemy = ['The Ember Warrior','The Aqua Warrior', 'The Sandy Warrior', 'The Frost Warrior','The Storm Warrior' ]
enemy = random.choice(enemy)


inventory = []
player_health = 100
turn_count = 0

weapons = ["Firing Squad", "Rifle", "Grenade"]
special_attacks = ["Incinerate", "Poison", "Paralyse"]
