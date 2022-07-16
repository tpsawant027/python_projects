def encrypter(message,offset):
    lst = [chr(i) for i in range(97,123)]
    enmsg = ""
    lst2 = message.split()
    for ele in lst2:
        for i in range(len(ele)):
            if ele[i] in lst:
                indx = lst.index(ele[i])
                enmsg+=lst[(indx - offset)]
            else:
                enmsg+=ele[i]
        print(enmsg, end = " ")
        enmsg = ""