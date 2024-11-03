import pandas as pd

def lower_case(value):
    print('Here is the value I am processing: ', value)
    return value.lower()

data = pd.DataFrame([['A', 1],
                     ['B', 2],
                     ['C',  3]], columns = ['letter', 'position'])

new_column = data['letter'].apply(lower_case)
new_column = new_column.values
print(new_column)
data['letter'] = new_column
print(data)
