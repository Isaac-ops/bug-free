player1wins=0
player2wins=0
def fn_rock_paper(player1_input,player2_input):
    if (player1_input=="R") and (player2_input=="S"):
        print("Player one wins!")
        return 1
    elif (player1_input=="S") and (player2_input=="P"):
        print("Player one wins!")
        return 2
    elif (player1_input=="P") and (player2_input=="R"):
        print("Player one wins!")
        return 3
    elif (player1_input=="S") and (player2_input=="R"):
        print("Player two wins!")
        return 4
    elif (player1_input=="P") and (player2_input=="S"):
        print("Player two wins!")
        return 5
    elif (player1_input=="R") and (player2_input=="P"):
        print("Player two wins!")
        return 6
    else:
        print("Error! Enter a correct response!")
game=1
while game<=5:
    player1=input("Player one enter R,P,S to select either rock, paper, or scissor:")
    player2=input("Player two enter R,P,S to select either rock, paper, or scissor:")
    player_result=fn_rock_paper(player1,player2)
    game=game+1
    if (player_result==1) or (player_result==2) or (player_result==3):
        player1wins=player1wins+1
    elif(player_result==4) or (player_result==5) or (player_result==6):
        player2wins=player2wins+1
    else:
        print("Error.")
    print("Number of player one wins:",player1wins)
    print("Number of player two wins:",player2wins)
if (player1wins>player2wins):
    print("Overall winner is player 1!")
elif (player2wins>player1wins):
    print("Overall winner is player 2!")
else:
    print("Error.")






