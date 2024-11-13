import json
import requests
import random as rand

# #EX1
# def get_words_from_file():
#     with open(r'C:\Users\User\Documents\DI-Bootcamp\Week2\Day4\sentence_generator.txt', 'r', encoding= 'utf-8') as file:
#         content = file.read()
#         return (content)

# words = get_words_from_file() #need the variable words for using it in the next function

# def get_random_sentences(r_words, lenght):
#         if lenght > len(words):
#              print('Lenght is bigger than words')
#         r_words = rand.choices(words, k=lenght)
#         sentence = ''.join(r_words).lower()
#         return sentence

# def main():
#     print('This program creates a random sentence using a random word file')
#     request = int(input('How many words for the sentences (between 2 and 20)'))

#     if request <= 2 or request >= 20:
#           print('Error. Type a number between 2 and 20.')
#           return
#     else:
#           words = get_words_from_file()
#           sentence = get_random_sentences(words, request)
    
#     print('Your sentence is the following:\n', sentence)

# main()

#EX2

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson) #load the string
salary = data['company']['employee']['payable']['salary']
print(salary)

data['company']['employee']['birthdate'] = "1989/03/30"

updated_data = json.dumps(data, indent=3)

with open('data.json', 'a') as file:
    json.dump(data, file, indent=3)

    

    
 
