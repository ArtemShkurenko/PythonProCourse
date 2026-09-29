def string_lenth (s):
    return len(s)

def string_union (str1, str2):
    return str1 + str2

def pow_number (num):
    return num ** 2

def sum_numbers(num1, num2):
    return num1 + num2

def divide_number (num1, num2):
    return divmod(num1, num2)

def lst_avarage(lst):
    sum = 0
    for el in lst:
        sum += el
    return sum / len(lst)

def lst_union (lst1, lst2):
    lst3 = []
    for el in lst1:
        if el in lst2 and el not in lst3:
            lst3.append(el)
    return lst3

def key_dictionary(dic):
    for key, value in dic.items():
        print(f"key: {key}, value: {value}")

def union_dic(dic1, dic2):
    dic1.update(dic2)
    return dic1

def set_union(set1, set2):
    set1.update(set2)
    return set1

def is_subset(set1, set2):
    return set1.issubset(set2)

def even_num(num):
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")
def even_list(lst):
    lst1 = []
    for el in lst:
        if el % 2 == 0:
            lst1.append(el)
    return lst1

even_odd_num = lambda num : "even number" if num % 2 == 0 else "odd number"
