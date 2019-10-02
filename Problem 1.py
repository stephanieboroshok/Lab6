# Number of Evens and Odds in list
# Create function that takes list of integers as parameter
# use for loop to iterate through list
# print how many evens and how many odds

def count_EvensOdds(numbers):
    oddCounter = 0
    evenCounter = 0
    for i in numbers:
        if i %2==0:
            evenCounter = evenCounter + 1
        else:
            oddCounter = oddCounter + 1
    print(evenCounter)
    print(oddCounter)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (count_EvensOdds(numbers))