team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6

str_1 = "В команде %s участников: %d !" % (team1_name, team1_num)
str_2 = "В команде %s участников: %d !" % (team2_name, team2_num)

str_3 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

score_1 = 40
score_2 = 42
str_4 = "Команда {0} решила задач: {1} !".format(team1_name, score_1)
str_5 = "Команда {0} решила задач: {1} !".format(team2_name, score_2)

team1_time = 1552.512
team2_time = 2153.31451
str_6 = "{0} решили задачи за {1} с !".format(team1_name, team1_time)
str_7 = "{0} решили задачи за {1} с !".format(team2_name, team2_time)

score_1 = 40
score_2 = 42
str_8 = f'{team1_name} решили {score_1} задач.'
str_9 = f'{team2_name} решили {score_2} задач.'
str_10 = f'Команды решили {score_1} и {score_2} задач.'

tasks_total = f'{score_1 + score_2} задач'
time_avg = f'{round((team1_time + team2_time) / (score_1 + score_2), 1)} секунды'

str_11 = f'Сегодня было решено {tasks_total}, в среднем по {time_avg} на задачу!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

str_12 = f'Результат битвы: {challenge_result}!'

story_list = (str_1, str_2, str_3, str_4, str_5, str_6, str_7, str_8, str_9, str_10, str_11, str_12)

if __name__ == '__main__':
    for elem in story_list:
         print(elem)








