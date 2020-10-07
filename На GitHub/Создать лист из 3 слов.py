def concat():
    new_list = ['Earth', 'Russia', 'Moscow']
    f_list = ''
    for word in new_list:
        if word == 'Russia':
             f_list += str(' -> ') + word + str(' -> ')
        else:
            f_list += word
    print("This is the answer I get: {}".format(f_list))

concat()