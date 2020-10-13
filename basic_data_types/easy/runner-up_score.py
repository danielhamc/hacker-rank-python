# Find the runner-up score
# Easy

##Given the participants' score sheet for your University Sports Day,
##you are required to find the runner-up score. You are given  scores.
##Store them in a list and find the score of the runner-up.
##
##Sample Input 0
##
##5
##2 3 6 6 5
##
##Sample Output 0
##
##5


# Get n amount of scores
n = int(input())
# Get list of scores
arr = map(int, input().split())

arr_set = set(arr) # Create a set
arr_list = list(arr_set) # Change to list

# Output the runner-up score
print(arr_list[-2])
