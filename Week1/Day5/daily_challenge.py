#Daily Challenge

#EX1
def sorting():
    answer = input('Write a sequence of words\n')
    sorted_words = ",".join([word.strip() for word in sorted(answer.split(","))])
    print(sorted_words)
sorting()

#EX2
# For checker.. It does not print the 2nd sentence, is it because of the uppercase 'A'?
def longest_word():
    answer1 = input('Write a sentence\n')
    characters = answer1.split() #splits the string as a list 
    longest_word = '' #here I will store the string

    for i in characters: #loop for each string in the list
        if len(i) > len(longest_word):
            longest_word = i
            print(longest_word)
        else:
            break
    
longest_word()

