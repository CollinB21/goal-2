sticks = int(13)

playerState = int(0)

#game mechanics


while (sticks > 0):
    if (playerState %2 != 1):
      playerMove = int(input("Player One, please enter your move:"))
      if (playerMove > 0) and (playerMove < 5) and (playerMove <= sticks):
        sticks = sticks - playerMove
        playerState +=1
        print (Sticks)
        print (playerState)
      else:
          print ("Illegal move.  Try again.")
    else:
      playerMove = int(input("Player Two, please enter your move:")
      if (playerMove > 0) and (playerMove < 5) and(playerMove <= sticks):
        sticks = sticks - playerMove
        playerState +=1
        print(sticks)
        print(playerState)
        
        