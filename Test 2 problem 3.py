from random import randint
win=0
loss=0
def fn_dice_game():
    dice_1=randint(1,6)
    dice_2=randint(1,6)
    if dice_1+dice_2==7:
        return True
    else:
        return False
bet_money=int(input("Enter an amount of money you want to start betting with:"))
while bet_money>0:
    results=fn_dice_game()
    if results==True:
        bet_money=bet_money*1.50
        win=win+1
    else:
        bet_money=bet_money*.50
        loss=loss+1
print("Number of wins:",win)
print("Number of losses:",loss)
