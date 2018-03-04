def reverse_dictionary(dict1):
    new_dict={}
    for k in dict1:        
        for value in dict1[k]:
            key = k.lower()
            this_value = value.lower()
            if new_dict.get(this_value):
                if k not in new_dict[this_value]:
                    new_dict[this_value].append(key)
                    new_dict[this_value].sort()
            else:
                new_dict[this_value]=[key]
    return new_dict


print(reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}))