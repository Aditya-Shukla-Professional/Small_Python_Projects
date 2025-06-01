import art,game_data
import os
from random import randint as r
object=game_data.data[r(0,len(game_data.data))-1]
score=0
game_on=True
def person(object):
    return f"{object["name"]}, a {object["description"]}, from {object["country"]}."
def brain(a,b):
    if (a["follower_count"]>b["follower_count"]):
        return "a"
    elif (a["follower_count"]<b["follower_count"]):
        return "b"
print(art.logo)
while game_on==True:
    print("Compare A:",person(object))
    print(art.vs)
    object2=game_data.data[r(0,len(game_data.data))-1]
    print("Against B:",person(object2))
    ask=input("Who has more followers? Type 'A' or 'B': ").lower()
    if ask==brain(object,object2):
        score+=1
        print(art.logo)
        print(f"You're right! Current score: {score}")
        object=object2
    else:
        os.system("cls")
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
