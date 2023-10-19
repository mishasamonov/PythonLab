def averageMinNum():
    A = list(map(int, input('Enter a list of numbers: ').split()))
    print(A)
    negativeNum = []

    for num in A:
        if num < 0:
            negativeNum.append(num)

    if not negativeNum:
        print('This list is not contain negative numbers!')
        return 0

    average = sum(A) / len(A)
    print('Your average = ', average)
    return average

averageMinNum()