#Binary_Decimal Converter and vice-versa

#binary to decimal
def bintodec(num: int) -> int:
    lst =[i for i in str(num)]
    power = len(lst) - 1
    sum = 0
    for i in range(len(lst)):
        add = int(lst[i]) * 2**power
        sum = sum + add
        power -= 1
    return sum       

#decimal to binary
def dectobin(num: int) -> int:
    lst = []
    while num > 0:
        rem = num % 2
        lst.append(rem)
        num = num // 2
    lst = lst[::-1]
    bnum = " "
    for ele in lst:
        bnum = bnum + str(ele)
    return int(bnum)

if __name__ == "__main__":
    print(bintodec(1110011))
    print(dectobin(115))
            

        