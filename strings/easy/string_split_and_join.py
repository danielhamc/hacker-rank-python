# String Split and Join
# Easy

## Task
## You are given a string. Split the string on a " " (space) delimiter
## and join using a - hyphen.
##
## Sample Input
##
## this is a string   
## Sample Output
##
## this-is-a-string

# Function to split and join
def split_and_join(string):
    a = "-".join(string.split(" "))
    return a



# Output Result
print(split_and_join(input()))
