def duplicate(input_list):
    new_dict = {}
    new_list = []
 
    for i in input_list:
        if not i in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
 
    for key, values in new_dict.items():
        if values > 1:
            new_list.append(key)
 
    return new_list
    
print(duplicate([4,3,2,7,8,2,3,1]))