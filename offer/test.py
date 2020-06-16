data = [4, [3, [2, [1]]]]

def sum_list_num(data):
    list_num = 0
    for i in data:
        if isinstance(i, list):
            list_num += sum_list_num(i)
        else:
            list_num += i
    print(list_num)
    return list_num

if __name__ == '__main__':
    print(sum_list_num(data))