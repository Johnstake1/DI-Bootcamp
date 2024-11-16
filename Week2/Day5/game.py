import random as rand

class Game:
    def get_user_item(self):
        
        user = ""
        while user not in ['rock', 'paper', 'scissors']:
            user = input('Please select rock, paper, or scissors: ').lower()
            if user not in ['rock', 'paper', 'scissors']:
                print('Invalid choice. Try again.')
        return user
    
    def get_computer_move(self):
        return rand.choice(['rock', 'paper', 'scissors'])
    
    def get_game_result(self, user, computer):
        if user == computer:
            return 'draw'
        
        elif (user == 'rock' and computer == 'scissors') or \
        (user == 'scissors' and computer == 'paper') or \
        (user == 'paper' and computer == 'rock'):
            return 'win'
        else:
            return 'loss'
    
    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_move()
        result = self.get_game_result(user, computer)
        print(f"You selected {user}. The computer selected {computer}. You {result}!")

        return result
        
