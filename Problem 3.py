#sum of odd numbers
#create funciton that takes integer as parameter
#return sum of every odd number from 5 to integer

def addOdds (integer):
    sumOdds = 0
    for i in range (5,integer):
        if i%2==1:
            sumOdds = sumOdds+i
        else:
            pass
    print('The sum of all of the odd numbers between 5 and', integer, '=', sumOdds)

integer=int(input('Enter a number:'))
print(addOdds(integer))