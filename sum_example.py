# Adds a number that is one less than the orignal number until the addition number goes to zero
def sum(num):
    result=0
    for i in range(num):
        result = result + num - i
    print(result)

sum(5)
sum(10)