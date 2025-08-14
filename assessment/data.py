import random

rooms=['The Room of Reckoning💡','Waters of Undoing🌊','Sanctum of Storms⛈️','The Ember Vault🔥' , 'The Oasis Chamber🌵','Center of the Elements']
rooms_text=['You wake up to a deep groaning sound, head pounding and heart racing. "Where am I?" you wonder. Frantically blinking, you attempt to reajust your eyes to the gloomy environment. Looking around, you see a dim flickering light, walls filled with rustic doors and a large table right in the centre. ','You awake, disoriented once again. Shaking your head vigorsly, you rise to your feet. A quiet crackling sound startles you. ','lalala', ]



player = ("name")
player_health = 100 
enemy_damage = random.choice([5, 10, 25])
enemy_health = random.choice([100, 75, 125])

enemy = ['The Ember Warrior','The Aqua Warrior', 'The Sandy Warrior','The Storm Warrior' ]
enemy = random.choice(enemy)


inventory = []
player_health = 100
player_location = rooms[0]
turn_count = 0

weapons = ["Firing Squad", "Rifle", "Grenade"]
special_attacks = ["Incinerate", "Poison", "Paralyse"]
