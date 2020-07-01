#!/usr/bin/env python3

'''
Jeopardy Lab
'''

import requests

def main():
    # prompt for initials
    player = input("Player initials:" )

    # make a request to https://jservice.io/api/random
    zresp = requests.get(f"https://jservice.io/api/random?count={round}")
    
    # strip off JSON from the 200 response
    listofquestions = zresp.json()

    # run the game by looping over the results
    for jquestion in listofquestions:
        #each time through the loop pose the question to the player
        print(f"Alex says: {jquestion['question']}")
        playeranswer = input(f"\tType your answer---> ") # captures the users input
        
        # user can respond by typing input be sure to normalize to lowercase
        if playeranswer.lower() == jquestion['answer'].lower():
            print(f"Alex says: Thats right, you add {jquestion['value']} to your score")
            playerscore = playerscore + jquestion.get('value')
        else:
            print(f"Alex says: Oh, not quite right! The answer we were looking for was {jquestion['answer']}")

    print(f"Alex says: Okay! Lets see how you did. \nLooks like your score is {playerscore}")

    with open("jeopardyhighscores.txt") as jhs:
        highscorelist = jhs.readlines()
    
    for score in highscorelist:
        if playerscore > score:
            highscorelist.remove(score)
            highscorelist.append(playerscore)
            break
    with open("jeopardyhighscores.txt") as jhs:
        for score in highscorelist:
            jhs.write(score.rstrip+"\n")


    #base_URI = 'https://jservice.io/api/random'
    #rand = requests.get(https://jservice.io/)
    #rounds = 0

if __name__ == "__main__":
    main()
