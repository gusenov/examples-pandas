import pandas as pd

data = [
    {'group_var_1': 1, 'group_var_2':'A', 'session_value': 10, 'n_users': 1},
    {'group_var_1': 1, 'group_var_2':'A', 'session_value': 25, 'n_users': 2},
    {'group_var_1': 1, 'group_var_2':'B', 'session_value': 40, 'n_users': 3},
    {'group_var_1': 1, 'group_var_2':'B', 'session_value': 10, 'n_users': 4},
    {'group_var_1': 2, 'group_var_2':'A', 'session_value': 90, 'n_users': 5}
]




my_stat = pd.DataFrame(data)
print(my_stat)
print()
'''
   group_var_1 group_var_2  n_users  session_value
0            1           A        1             10
1            1           A        2             25
2            1           B        3             40
3            1           B        4             10
4            2           A        5             90
'''




print("Число наблюдений в каждой группе:")
df = my_stat.groupby('group_var_1').count()
print(df)
print()
'''
Число наблюдений в каждой группе:
             group_var_2  n_users  session_value
group_var_1                                     
1                      4        4              4
2                      1        1              1
'''




# Сгруппировать данные по нескольким переменным:
df = my_stat.groupby(['group_var_1', 'group_var_2']).count()
# При такой записи группирующие переменные станут индексами в итоговом dataframe.
# Функция count() применится ко всем колонкам, что не всегда является желанным результатом.
print(df)
print()
'''
                         n_users  session_value
group_var_1 group_var_2                        
1           A                  2              2
            B                  2              2
2           A                  1              1
'''




# Чтобы применить функцию только к нужной колонке в данных, можно использовать связку  groupby() + agg():
df = my_stat.groupby('group_var_2').agg({'n_users': 'count'})
print(df)
print()
'''
             n_users
group_var_2         
A                  3
B                  2
'''




# Расчёт для данных my_stat среднего значения переменной session_value для каждой группы (переменная group),
# в получившемся dataframe переменная group не превращается в индекс.
# Переименование колонки со средним значением session_value в mean_session_value.
# Сохранение получившегося результата в dataframe с именем mean_session_value_data.
group = 'group_var_2'
mean_session_value_data = my_stat.groupby(group, as_index=False).agg({'session_value': 'mean'}).rename(columns={'session_value': 'mean_session_value'})
print(mean_session_value_data)
print()
'''
  group_var_2  mean_session_value
0           A           41.666667
1           B           25.000000
'''




# Альтернативные варианты:

# mean_session_value_data = my_stat.groupby('group').agg({'session_value' : np.mean}).\
#                            reset_index().rename(columns = {'session_value' : 'mean_session_value'})

# mean_session_value_data = my_stat.groupby('group', as_index=False).agg({'session_value': 'mean'}).rename({'session_value': 'mean_session_value'}, axis=1)
