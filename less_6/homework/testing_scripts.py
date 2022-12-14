def update_rating(r_list, number):
    for i in range(len(r_list)):
        if r_list[i] == number:
            r_list.insert(i + 1, number)
            break
        if r_list[0] < number:
            r_list.insert(0, number)
        elif r_list[-1] > number:
            r_list.append(number)
        elif r_list[i + 1] < number < r_list[i]:
            r_list.insert(i + 1, number)
            break
    return r_list


def update_rating_2(r_list, number):
    r_list.append(number)
    r_list.sort(reverse=True)
    return r_list


def my_func_1(x, y):
    '''
    First way
    :param x: real positive number
    :param y: integer negative number
    :return: pow
    '''
    try:
        if int(y) < 0 < float(x):
            return float(x) ** float(y)
        else:
            print('Please enter numbers according to the task')
    except ValueError:
        print('Second number should be integer negative')


def my_func_2(x, y):
    '''
    Second way
    :param x: real positive number
    :param y: integer negative number
    :return: pow
    '''
    try:
        if int(y) < 0 < float(x):
            result = 1
            i = 1
            while i <= abs(int(y)):
                result *= float(x)
                i += 1
            return 1 / result
        else:
            print('Please enter numbers according to the task')
    except ValueError:
        print('Second number should be integer negative')


def my_func_3(x, y):
    '''
    Third way
    :param x: real positive number
    :param y: integer negative number
    :return: pow
    '''
    return pow(x, y)