# Number of Evens and Odds in list
# Create function that takes list of integers as parameter
# use for loop to iterate through list
# print how many evens and how many odds

def count_EvensOdds(numbers):
    oddCounter = 0
    evenCounter = 0
    highestValue = 0
    lowestValue = numbers[0]
    #create variables with counts inside function
    for i in numbers:
        if i %2==0:
            #i=individual element of list
            #modulus gets remainder to determine even or odd
            evenCounter = evenCounter + 1
        else:
            oddCounter = oddCounter + 1
            #add to counters based on elements being even or odd
        if i > highestValue:
            highestValue = i
            #if current number we are on is greater than the stored current value, replace it as the highest value
        else:
            pass
        if i < lowestValue:
            lowestValue = i
            #if current number we are on is less than stored current value, replace as lowest value
        else:
            pass
    print('There are', evenCounter, 'even numbers in the list')
    print('There are', oddCounter, 'odd numbers in the list')
    print('The highest value in the list is', highestValue)
    print('The lowest value in the list is', lowestValue)
    #print even or odd determinations and highest and lowest values

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#create list for function to examine

print (count_EvensOdds(numbers))
#print the function