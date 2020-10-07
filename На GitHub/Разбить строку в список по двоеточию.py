def stroka():
    new_string = '/bin:/usr/bin:/usr/local/bin'
    sec_string = ''
    new_list = []
    for i in range(0, len(new_string)):
        sec_string += new_string[i]
        if new_string[i] == ':':
            new_list.append(sec_string)
            sec_string = ''
        else:
            continue
    new_list.append(sec_string)
    print(new_list)

stroka()