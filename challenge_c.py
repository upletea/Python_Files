action = ["insult", "ignore", "apologise", "praise"]

for i in action:
    print(i," --")

# Make sure there is no capitals when inputted (insult, ignore, apologise, praise)
person_action = input("what happened? Pick either: insult, ignore, apologise or praise. " )

if person_action in action and person_action == action[0]:
    print('BLOCKED! Nobody talks to you like that.')

elif person_action in action and person_action == action[1]:
    print('BLOCKED! They better not being doing such a thing.')

elif person_action in action and person_action == action[2]:
    print('They seem like a kind friend but make sure they are being truthful.')

elif person_action in action and person_action == action[3]:
    print('Aww what a nice comment.')

recent_post = input("Did they like your most recent post? yes or no?")

if recent_post == "yes":
    recent = True
else:
   recent = False


friend_life = input("Are they your friend in real life? yes or no?")
if friend_life == "yes":
    friend = True
else:
   friend = False









