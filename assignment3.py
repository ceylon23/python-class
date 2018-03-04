def capitalize_word_in_crossword(cross_word,word):
    def find_word_horizontal(cross_word, word):
        row_coord = []
        row_count = 0
        for row in cross_word:
            entry_str = "".join(row)
            if word in entry_str:
                column = entry_str.index(word)
                row_coord.append(row_count)
                row_coord.append(column)
                return row_coord
            row_count += 1
        return

    def find_word_vertical(cross_word, word):
        row_coord = []
        j = 0
        k = 0
        list_length = len(cross_word)
        col_length = len(cross_word[0])

        while j < col_length:
            column = []
            column_str = ""
            while k < list_length:
                column.append(cross_word[k][j])
                k += 1
            column_str = "".join(column)
            if word in column_str:
                row_coord.append(column_str.index(word))
                row_coord.append(j)
                return row_coord
            k = 0
            j += 1
        return

    word_length = len(word)
    horizontal = find_word_horizontal(cross_word, word)
    vertical = find_word_vertical(cross_word, word)
    letter_count = 1

    if horizontal != None:
        for index in range(len(cross_word[horizontal[0]])):
            if index >= horizontal[1] and letter_count <= word_length:
                cross_word[horizontal[0]][index] = cross_word[horizontal[0]][index].upper()
                letter_count += 1
    elif vertical != None:
        j = 1
        row = vertical[0]
        column = vertical[1]
        while j <= word_length:
            cross_word[row][column] = cross_word[row][column].upper()
            row += 1
            j += 1
        

    return cross_word



crosswords = [['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word = "cat"

print(capitalize_word_in_crossword(crosswords, word))