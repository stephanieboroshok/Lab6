# Number of Evens and Odds in list
# Create function that takes list of integers as parameter
# use for loop to iterate through list
# print how many evens and how many odds

def count_EvensOdds(numbers):
    oddCounter = 0
    evenCounter = 0
    #create variables with counts inside function
    for i in numbers:
        if i %2==0:
            #i=individual element of list
            #modulus gets remainder to determine even or odd
            evenCounter = evenCounter + 1
        else:
            oddCounter = oddCounter + 1
            #add to counters based on elements being even or odd
    print(evenCounter)
    print(oddCounter)
    #print even or odd determinations

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#create list for function to examine

print (count_EvensOdds(numbers))
#print the function