# caesars cypher decoder
def decoder(message: str, offset: int):
    lst = [chr(i) for i in range(97,123)]
    dmsg = ""
    lst2 = message.split()
    lindx = 25
    for ele in lst2:
        for i in range(len(ele)):
            if ele[i] in lst:
                indx = lst.index(ele[i])
                if (indx + offset) > lindx:
                    dmsg+=lst[((indx + offset) - lindx) - 1]
                else:
                    dmsg+=lst[(indx + offset)]
            else:
                dmsg+=ele[i]
        print(dmsg, end = " ")
        dmsg = ""
msg = "czggj rjmgy!"
num = 5
decoder(msg,num)