import pandas as pd




# В dataframe с именем my_stat четыре колонки V1, V2, V3, V4:

data = {
    'V1': [ 1   , 2   , -1  , 45  ],
    'V2': [ 10  , 21  , 19  , 10  ],
    'V3': [ 'A' , 'B' , 'A' , 'A' ],
    'V4': [ 20  , 1   , 19  , 0   ]
}

my_stat = pd.DataFrame(data)




def test1():  # вариант 1
    print()

    # Сохранить только те наблюдения, у которых значения переменной V1  строго больше 0, и значение переменной V3  равняется 'A':
    subset_1 = my_stat[(my_stat['V1']>0) & (my_stat['V3']=='A')]
    # Результат фильтрации - это тоже dataframe.

    print(subset_1)
    print()
    '''
   V1  V2 V3  V4
0   1  10  A  20
3  45  10  A   0
    '''

    # Сохранить только те наблюдения, у которых значения переменной V2  не равняются 10, или значения переменной V4 больше или равно 1:
    subset_2 = my_stat[(my_stat['V2']!=10) | (my_stat['V4']>=1)]

    print(subset_2)
    print()
    '''
   V1  V2 V3  V4
0   1  10  A  20
1   2  21  B   1
2  -1  19  A  19
    '''




def test2():  # вариант 2
    print()

    subset_1 = my_stat[(my_stat.V1 > 0) & (my_stat.V3 == 'A')]

    print(subset_1)
    print()
    '''
   V1  V2 V3  V4
0   1  10  A  20
3  45  10  A   0
    '''

    subset_2 = my_stat[(my_stat.V2 != 10) | (my_stat.V4 >= 1)]

    print(subset_2)
    print()
    '''
   V1  V2 V3  V4
0   1  10  A  20
1   2  21  B   1
2  -1  19  A  19
    '''




test1()
test2()
