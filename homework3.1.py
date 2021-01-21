def plural_form(number, *args):
    args_list = []
    for i in args:
        args_list.append(i)
    if number == 1 or number % 10 == 1:
        args = args_list[0]
    elif (number > 1 and number < 5) or (number % 10 > 1 and number % 10 < 5):
        args = args_list[1]
    else:
        args = args_list[2]  
    return(f"{number} {args}")


print(plural_form(101, 'яблоко', 'яблока', 'яблок'))
