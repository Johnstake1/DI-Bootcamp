from anagram_checker import AnagramChecker
#FOR CHECKER - I cannot make to print the anagrams. It can only check that there are anagrams
class Anagram_Menu(AnagramChecker):
    def __init__(self):
        super().__init__() #calls the functions from the backend

    def menu(self):
        print('Welcome to the Anagram Checker')
        while True: #will keep the menu opened as long as the nunu types exit
            print('Select an option:')
            print('1. Write a word')
            print('2. Exit')
            response = input('Select 1 or 2\n')

            if response == '2':
                print('See you next time!')
                break

            elif response == "1":
                answer = input('Write a word: ').strip()

                if self.is_valid_word(answer):
                    print('This is a valid english word')
                    anagrams = self.get_anagrams(answer)
                    if anagrams:
                        print('There are anagrams for your word')
                        print(f"Anagrams for your word are: {', '.join(anagrams)}")
                    else:
                        print('No anagrams found for your word')
                else:
                    print('You word is not a valid english word')
            else:
                print('Please enter 1 or 2')

test = Anagram_Menu()
print(test.menu())


    

