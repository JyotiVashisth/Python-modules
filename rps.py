import random
def evaluate(player_move,computer_move):
    if(player_move==computer_move):
        return 0
    elif(player_move=='Scissor' and computer_move=='Paper'):
        return 1
    elif(player_move=='Paper' and computer_move=='Rock'):
        return 1
    elif(player_move=='Rock' and computer_move=='Scissor'):
        return 1
    
    elif(player_move=='Paper' and computer_move=='Scissor'):
        return -1
    elif(player_move=='Rock' and computer_move=='Paper'):
        return -1
    elif(player_move=='Scissor' and computer_move=='Rock'):
        return -1
           
print('Rock? Paper? Scissor?')
player_move=input()
moves=['Rock','Paper','Scissor']
computer_move=random.choice(moves)
print(computer_move)
result=evaluate(player_move,computer_move)
if(result==1):
       print('You win. Whatever.')
elif(result==0):
       print('Draw.')
else:
       print('Haha. You lose')
