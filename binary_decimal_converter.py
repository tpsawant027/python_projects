if __name__ == "__main__":
    choice = int(input("For Binary to Decimal enter '1', and for Decimal to Binary enter '2' - "))
    if choice == 1:
        num = int(input("Enter a Binary number - "))
        lst =[i for i in str(num)]
        power = len(lst) - 1
        sum = 0
        for i in range(len(lst)):
            add = int(lst[i]) * 2**power
            sum = sum + add
            power -= 1
        print(f"The corresponding decimal number is {sum}.")
    elif choice == 2:
        num = int(input("Enter a Decimal number - "))
        lst = []
        while num > 0:
            rem = num % 2
            lst.append(rem)
            num = num // 2
        lst = lst[::-1]
        bnum = " "
        for ele in lst:
            bnum = bnum + str(ele)
        print(f"The corresponding binary number is{bnum}.")
            

        