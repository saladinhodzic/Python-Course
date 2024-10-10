# rock paper scissors
import random

moves=["rock","paper",'scissors']

my_move=int(input("Enter 0 for rock, 1 for paper, 2 for scissors\n"))

computer_move=random.choice(moves)

if moves[my_move]==computer_move:
    print(f"You choose {moves[my_move]}, computer choose {computer_move}\n It is a draw!")

else:
       if moves[my_move]=='rock'and computer_move=='scissors':
        print(f"You choose {moves[my_move]}, computer choose {computer_move}\n You win!")
       elif moves[my_move]=='paper'and computer_move=='rock':
        print(f"You choose {moves[my_move]}, computer choose {computer_move}\n You win!")
       elif moves[my_move]=="scissors" and computer_move =='paper':
        print(f"You choose {moves[my_move]}, computer choose {computer_move}\n You win!")
       else:
        print(f"You choose {moves[my_move]}, computer choose {computer_move}\n You lose!")

