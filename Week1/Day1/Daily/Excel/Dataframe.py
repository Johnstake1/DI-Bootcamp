#This exercise is for cleaning a data file

import pandas as pd
import numpy as np
import re


data = pd.read_csv('persons.csv')
print(data)

VALID_COUNTRIES = ['France','Madagascar', 'Benin', 'Germany', 'Canada']

def check_country(country):
    if country not in VALID_COUNTRIES:
        print('-"{}" is not a valid country, we delete it'\
              .format(country))
        return np.NaN
    return country

# Process emails (if there are 2 email addresses or more)
def first(string):
    parts = string.split(',')
    first_part = parts[0]
    if len(parts) >=2:
        print(' - There are several parts in "{}", we are only keeping {}'\
              .format(parts,first_part))
        return first_part
    
#Process Heights
def convert_height(height):
    found = re.search('\d\.\d{2}m', height)
    if found is None:
        print('{} is not in the right format. It will be ignored.'.format(height))
        return np.NaN
    else:
        value = height[:-1] # the last character is removed: 'm'
        return float(value)

def fill_height(height, replacement):
    if pd.isnull(height):
        print('Imputation by the mean : {}'.format(replacement))
        return replacement
    return height

data['email'] = data['email'].apply(first)
data['country'] = data['country'].apply(check_country)
data['height'] = [convert_height(t) for t in data['height']]
data['height'] = [t if t<3 else np.NaN for t in data['height']]

mean_height = data['height'].mean()
data['height'] = [fill_height(t, mean_height) for t in data['height']]
data['date_of_birth'] = pd.to_datetime(data['date_of_birth'], 
                                           format='%d/%m/%Y', errors='coerce')
print(data)
    
