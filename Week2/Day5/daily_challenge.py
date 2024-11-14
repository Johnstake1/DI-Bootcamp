#EX1
import requests
import time as t

def time_to_load():

    question = input('Type a website. Remember to type https://\n')

    start_time = t.time()

    response = requests.get(question)

    end_time = t.time()

    delta = end_time - start_time
    print(f'It took {delta} seconds to load the page')


time_to_load()