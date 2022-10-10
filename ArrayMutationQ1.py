def solution(a):
    ansArray = []
    index = 0
    print(a[-1])
    for i in range(len(a)):


    
        try:
            num1 = a[- 1]
        except:
            num1 = 0

        try:
            num2 = a[index]
        except:
            num2 = 0

        try:
            num3 = a[index+1]
        except:
            num3 = 0

        print(num1,num2,num3)
        newNumber = num1 + num2 + num3
        ansArray.append(newNumber)
        index+=1


    return print(ansArray)







if __name__ == "__main__":
    solution([4, 0, 1, -2, 3])