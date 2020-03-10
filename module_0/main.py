# print("Hello world")

# 

import numpy as np

def score_game(game_core_v1):
    '''Запуск 1000 раз '''
    count_ls = []
    np.random.seed(1)  
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number): 
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count)  

score_game(game_core_v2)

