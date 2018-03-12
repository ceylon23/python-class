def create_grades_dict (file_name):
    file_pointer = open(file_name, 'r')

    grade_book = {}
    lines = file_pointer.readlines()
    file_pointer.close()

    for line in lines:
        line_list = line.replace(' ','').strip().split(',')

        last_name = line_list[1]
        grades = {}
        grade_sum = 0
        grade_book_line = []

        grade_book_line.append(last_name)

        if "Test_1" not in line_list:
            grades["Test_1"] = 0
        if "Test_2" not in line_list:
            grades["Test_2"] = 0
        if "Test_3" not in line_list:
            grades["Test_3"] = 0
        if "Test_4" not in line_list:
            grades["Test_4"] = 0
        
        for n in range(0,len(line_list)):
            if line_list[n] == "Test_1" or line_list[n] == "Test_2" or line_list[n] == "Test_3" or line_list[n] == "Test_4":
                grades[line_list[n]] = int(line_list[n+1])
                grade_sum += int(line_list[n+1])
        
        average = grade_sum / len(grades)

        for n in range(1,5):
            grade_book_line.append(grades['Test_%s'%n])

        grade_book_line.append(average)

        grade_book[line_list[0]] = grade_book_line
    return grade_book

def print_grades(file_name):
    grades_dict=create_grades_dict(file_name)

    id_order = grades_dict.keys()
    id_order = sorted(id_order)

    k = 0

    print('{0: ^10} | {1: ^16} | {2: ^6} | {3: ^6} | {4: ^6} | {5: ^6} | {6: ^6} |'.format("ID", "Name", "Test_1", "Test_2", "Test_3", "Test_4", "Avg."))
    while k < len(id_order):
        print('{0: ^10} | {1: <16} | {2: >6} | {3: >6} | {4: >6} | {5: >6} | {6: >6.2f} |'.format(id_order[k], grades_dict[id_order[k]][0], grades_dict[id_order[k]][1], grades_dict[id_order[k]][2], grades_dict[id_order[k]][3], grades_dict[id_order[k]][4], grades_dict[id_order[k]][5]))
        k += 1     

    return 
    
print(print_grades ("my_file.txt"))