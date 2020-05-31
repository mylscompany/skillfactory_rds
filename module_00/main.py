import numpy as np
def game_core_v3(number):
    '''Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    low_index = 1
    high_index = 101
    predict = 50 #Сначала устанавливаем число 50, как половина отрезка
    
    while number != predict:
        count += 1
        if number > predict: 
            low_index = predict
        elif number < predict: 
            high_index = predict
        predict = low_index + (high_index - low_index) // 2; 
        
    return(count) # выход из цикла, если угадали
        
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v3)