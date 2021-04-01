import random

def diceroll():
    six_dice = [1,2,3,4,5,6]

    dice_roll = random.choice(six_dice)

    print('You rolled a dice and got: ' ,dice_roll)

    if dice_roll == 6:

        def bonusdiceroll():
            bonusdice = [2,4,8,16,32,64]

            bonusdiceroll = random.choice(bonusdice)

            print('You rolled the bonus dice and you got a: ' ,bonusdiceroll)
def rps():
    while True:
      options = ['Rock' , 'Paper' , 'Scissors']

      for x in options:
        print(x)
      
      print('Hello, User! Choose one of the above to battle the computer.')
      
      user = input('Type what your gonna do here: ')
      
      bot = random.choice(options)
      
      print('User said: ' ,user)
      print('Bot said:',bot)
      
      
      outcome = [user,bot]
      playerWins = [['Rock','Scissors'],['Scissors','Paper'],['Paper','Rock']]
      
      
      if outcome in playerWins:
        print('You win!!! 😄')
      elif bot == user:
        print('It is a tie 😐')
      else:
        print('You lost 😢')
        
      again = input('Again? No caps yes or no: ')
      
      if again == 'no':
        break
      else:
       print('Running again')

