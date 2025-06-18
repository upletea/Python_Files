#Lists the different action variables
action = ["insult", "ignore", "apologise", "praise"]

for i in action:
    print(i," --")

#Asks the user what action was done to them
# Make sure there is no capitals when inputted (insult, ignore, apologise, praise)
person_action = input("what happened? Pick either: insult, ignore, apologise or praise. " )

# Asking the user weather their post was liked or not. converted into boolean.
recent_post = input("Did they like your most recent post? yes or no?")

if recent_post == "yes":
    recent = True
else:
   recent = False

#Questions the user if the person involved is their friend and converts into boolean.
friend_life = input("Are they your friend in real life? yes or no?")
if friend_life == "yes":
    friend = True 
else:
   friend = False

# If the person got insulted
if person_action in action and person_action == action[0]:
    # provides the different combinations that could result in each answer
    if recent == True and friend == True:
        print('They may be your real life friend and have liked your post, however take the precaution and mute them as they are insulting you.')
    elif recent == True and friend == False:
        print("They may have liked your post, but you don't know them in real life and they seem quite agressive so lets unfollow them to be on the safe side")
    elif recent == False and friend == False:
        print("You don't know this person, and they were rude towards you so let's block them.")
    elif recent == False and friend == True:
        print("Although they are your friend in real life, they insulted you and didn't even like your post so unfollow them. ")
# If the person got ignored 
elif person_action in action and person_action == action[1]:
     # provides the different combinations that could result in each answer
    if recent == True and friend == True:
        print('This seems like a honest mistake, as they are your friend and also liked your recent post. However, if this occurs again, maybe rethink your situation.')
    elif recent == True and friend == False:
        print("If you feel uncomfortable with this person as they arent your friend, maybe unfollow them. However it is reasonable for them to ignore you as you don't know eachother well.")
    elif recent == False and friend == False:
        print("You don't know this person, and you have never interacted with this person. Its probably best to unfollow them.")
    elif recent == False and friend == True:
        print("It feels like you might be getting ghosted by your friend. Have a conversation with them about how to proceed with this situation. If it becomes a repeated offense, maybe consider blocking or unfollowing them.  ")
# If the person got apologised to
elif person_action in action and person_action == action[2]:
     # provides the different combinations that could result in each answer
    if recent == True and friend == True:
        print("They seem like a true friend for apologising to you. If you feel comfortable, you should forgive them and continue following them.")
    elif recent == True and friend == False:
        print("This seems like an unafe situation. I would advise you to mute them for now, but if the situation escalates consider blocking them.")
    elif recent == False and friend == False:
        print("In this scenario, its probably best to unfollow and block them.")
    elif recent == False and friend == True:
        print("They did apologise to you, you know them and it could've simply been a mistake that they didnt like your post. Keep following them.")
# If the person got praised
elif person_action in action and person_action == action[3]:
     # provides the different combinations that could result in each answer
    if recent == True and friend == True:
        print("You should continue following them. They seem like an amazing friend!")
    elif recent == True and friend == False:
        print("This person is creating a very unsafe situation. They do not know you and they shouldn't be making comments about you. Block and unfollow.")
    elif recent == False and friend == False:
        print("This seems like a very innapropriate scenario. You should block them and unfollow them as quickly as possible.")
    elif recent == False and friend == True:
        print("They most likely didn't notice they hadn't liked your post. Tey seem like a nice friend considering that they praised you. Follow.")





