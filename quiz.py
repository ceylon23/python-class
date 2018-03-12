def calculate_expenses(file_name):
    file_pointer = open(file_name, 'r')

    lines = file_pointer.readlines()
    file_pointer.close()

    tuple_tuples = ()
    temp_list = []
    tuple_list = []

    for line in range(0,len(lines)):
        temp_list.append(lines[line].replace(' ','').strip().split(','))

    sorted_lines = sorted(temp_list,key=lambda x: x[0])

    current_item = ''
    current_item_sum = 0.0
    tuple_item = ()

    for n in range(0,len(sorted_lines)):
        if sorted_lines[n][0] != current_item:
            tuple_item = (current_item, "${:.2f}".format(current_item_sum),)
            current_item = sorted_lines[n][0]
            current_item_sum = float(sorted_lines[n][1])
            tuple_tuples += (tuple_item,)
        else:
            current_item_sum += float(sorted_lines[n][1])

    tuple_item = (current_item, "${:.2f}".format(current_item_sum),)
    tuple_tuples += (tuple_item,)

    for tup in tuple_tuples:
        if tup[0] != '':
            tuple_list.append(tup)

    return tuple_list


print(calculate_expenses("my_file.txt"))