# DAILY CHALLENGE - Matrix

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
print(matrix)
print(type(matrix))

# decoded_message = ""
# is_last_char_alpha = False

# for column_id in range(len(matrix[0])):
#     for row_id in range(len(matrix)):
#         char = matrix[row_id][column_id]
#         if char.isalpha():
#             decoded_message += char
#             is_last_char_alpha= True
#         elif is_last_char_alpha:
#             is_last_char_alpha = False
#             decoded_message += " "

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

string = ' '.join(decoded_message)

print(string)