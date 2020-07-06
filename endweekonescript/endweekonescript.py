#!/usr/bin/python3

# -------------------------------------------------------------------------------
# Program name     : endweekonescript.py
# Student Name     : Kervin Rodriguez
# Course           : Python Course
# Instructor       : Zach Feezer
# Date             : March 17, 2020
# -------------------------------------------------------------------------------

# Replace RPG starter project with this code when new instructions are live


def showInstructions():
  #print a main menu and the commands
    print('''
        GET OUT!
        ========
        You just woke up strapped to a chair.. time to get the hell out of here!
        ========
        Commands:
        go [direction(upstairs, downstairs, forward, back, left, right )]
        get [item]
        ''')
    
def showStatus():
  #print the player's current status, items, and opponents
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])   
  print("---------------------------")
  if "badguy" in rooms[currentRoom]:
      print('Oh no! It is your girlfriends crazy '+ rooms[currentRoom]['badguy'] + '!')
  print("---------------------------")

#an inventory, which is initially empty
inventory = ['cotton balls' ]

#a dictionary linking a room to other rooms
rooms = {
            'Closet' : {
                'back' : 'Living Room',
                'item' : 'flash light',
                },
            'Basement' : { 
                'upstairs' : 'Living Room',
                'forward' : 'Surgery Room',
                'item'  : 'croquet ball',
                },
            'Surgery Room' : {
                'back' : 'Basement',
                'item' : 'deer antlers',
                'badguy' : 'Father'
                },

            'Living Room' : {
                'downstairs' : 'Basement',
                'right' : 'Closet',
                'forward' : 'Front Door',
                'back' : 'Kitchen',
                'item' : 'tea cup',
                'badguy' : 'Mom',
                },
            'Kitchen' : {
                'forward' : 'Living Room',
                'item' : 'keys',
                },
            'Front Door' : {
                'back' : 'Living Room',
                'badguy' : 'Brother',
                },
         }

#start the player in the Hall
currentRoom = 'Basement'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
  
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

## If a player enters a room with a monster
  if 'badguy' in rooms[currentRoom] and 'tea cup' in inventory:
    print('You have fallen into the sunken place!... GAME OVER!')
    break

## Define how a player can win
  if currentRoom == 'Front Door' and 'keys' in inventory and 'deer antlers' in inventory:
    print('You got out!... Your friend from TSA is here to save you!')
    print('You should have listened to him...')
    break 
