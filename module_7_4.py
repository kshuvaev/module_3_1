team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %
print('В команде %s участников: %s !' % (team1_name, team1_num))
print('В команде %(name)s участников: %(kol)s !' % {'name': team2_name, 'kol': team2_num})
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
# Использование format()
print('Команда {0} решила задач: {1} !'.format(team1_name, score_1))
print('{} решили задачи за {} секунд !'.format(team1_name, team1_time))
print('Команда {} решила задач: {} !'.format(team2_name, score_2))
print('{} решили задачи за {} секунд !'.format(team2_name, team2_time))
# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды {team1_name}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'Победа команды {team2_name}!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')

print(f'Сегодня было решено {score_1+score_2} задач, '
      f'в среднем по {round((team1_time+team2_time)/(score_1+score_2),1)} секунды на задачу!')
print(f'Сегодня было решено {score_1+score_2} задач, '
      f'в среднем по {time_avg} секунды на задачу!')