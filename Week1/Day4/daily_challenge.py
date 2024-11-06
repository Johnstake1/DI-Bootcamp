# DAILY CHALLENGE - Matrix
# FOR CHECKER -- Did not know how to erase the double spaces in secret_message
matrix = [
    ['7', 'i', 'i'],
    ['T','s','x'],
    ['h','%', '?'],
    ['i', '', '#'],
    ['s','M',''],
    ['$','a',''],
    ['#','t','%'],
    ['^','r','!']
]

decoded_message = []
not_in_alpha = ""
for columns in range(len(matrix[0])):
    for rows in range(len(matrix)):
        char = matrix[rows][columns]
        if char.isalpha():
            decoded_message.append(char)
        elif char:
            decoded_message.append(not_in_alpha)

print(decoded_message)

secret_message = ' '.join(decoded_message)

print(secret_message)