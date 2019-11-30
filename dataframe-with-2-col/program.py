import pandas as pd




def test1():  # вариант 1
    data = [['A', 10],
            ['A', 14],
            ['B', 12],
            ['B', 23]]

    my_data = pd.DataFrame(data, columns = ['type', 'value'])
    print(my_data)
    print()
    '''
  type  value
0    A     10
1    A     14
2    B     12
3    B     23
    '''




def test2():  # вариант 2
    columns = ['type', 'value']
    data_tuples = [('A', 10), ('A', 14), ('B', 12), ('B', 23)]

    my_data = pd.DataFrame(data=data_tuples, columns=columns)
    print(my_data)
    print()
    '''
  type  value
0    A     10
1    A     14
2    B     12
3    B     23    
    '''




test1()
test2()
