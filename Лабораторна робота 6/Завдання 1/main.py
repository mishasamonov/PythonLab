def delete():
    A = list(map(int, input('Enter a list of numbers: ').split()))
    print(A)
    A.remove(int(input('Enter the number, you would like to delete: ')))
    print(A)
    return A

delete()
