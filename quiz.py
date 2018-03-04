def multiplication_table (number):
    mult_table = []
    mult_row = []
    col_count = 0

    n = 1
    while n <= number:
        m = 1
        multiple = 1
        mult_row = []
        while m <= number:
            mult_row.append(n*multiple)
            multiple += 1
            m += 1
        mult_table.append(mult_row)        
        n += 1
    return mult_table

print(multiplication_table (4))