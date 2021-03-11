answer = input("would you like to play (yes/no)\n")

if answer.lower().strip() == "yes":
  answer = input("you encounter a dark alleyway, you have 3 options, will you go straight, right or left\n")

  if answer =='left':
      print('you run into a frog, it turns into a dragon, it kills you, GAME OVER')

  elif answer == 'right':
      print('cool')

  elif answer == 'straight':
        answer = input('you come across a chest and a alley way that leads forward, type chest to open the chest or straight to go straight\n')

        if answer == 'chest':
            print('a monster comes out of the chest and eats you GAME OVER')

        if answer == 'straight':
            answer = input('you come across a crying child sitting on the floot, type help to help them or continue to continue\n')

            if answer == 'help':
                print('the child turns into a monster and eats you GAME OVER')

            if answer == 'continue':
                print('a man appears infront of you and questions your morality after you left a crying child alone, he proceeds to kill you GAME OVER')
  else:
      print('invalid answer, restart')


else:
    print('you can leave then')
