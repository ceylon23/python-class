def matrix_multiply(my_list1, my_list2):
    
    col_length = len(my_list1[0])
    row_length = len(my_list2)

    for num_lists in my_list1:
        if col_length != len(num_lists):
            return False

    if row_length != col_length:
            return False
    else:
        product = []
        j = 0
        k = 0
        m = 0
        num_col = len(my_list1)
        num_row = len(my_list2)

        while j < num_col:
            dot_list = []
            while m < num_row:
                multiplied = 0
                while k < row_length:
                    multiplied = multiplied + (my_list1[j][k] * my_list2[k][m])
                    k += 1
                dot_list.append(multiplied)
                k = 0
                m +=1
            product.append(dot_list)
            m = 0
            j += 1
        return product
    

print(matrix_multiply([[2, 3, 4], [3, 4, 5]], [[4, -3, 12], [1, 1, 5], [1, 3, 2]]))
