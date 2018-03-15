def word_count_dict(string1):
    string_list = []
    word_count = {}

    string_list = string1.lower().split()

    word_count = dict((word, string_list.count(word)) for word in string_list)        

    return word_count

print(word_count_dict("I am tall when I am young and I am short when I am old" ))

