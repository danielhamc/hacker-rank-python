# Set . discard(), . remove(), . pop()

##Task
##You have a non-empty set , and you have to execute  commands given in  lines.
##
##The commands will be pop, remove and discard.
##
##Input Format
##
##The first line contains integer , the number of elements in the set .
##The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
##The third line contains integer , the number of commands.
##The next  lines contains either pop, remove and/or discard commands followed by their associated value.
##

##Sample Input
##
##9
##1 2 3 4 5 6 7 8 9
##10
##pop
##remove 9
##discard 9
##discard 8
##remove 7
##pop 
##discard 6
##remove 5
##pop 
##discard 5
##
##Sample Output
##
##4


# Get n amount of numbers in set
n = int(input())
# Create a set with the numbers
s = set(map(int, input().split()))

# Enter the amount of commands
num_commands = int(input())


# For loop to get commands to discard, remove, or pop
for _ in range(num_commands):
  commands = input()
  if commands != 'pop':
    commands, numb = commands.split()
  if commands == "pop":
    s.pop()
  elif commands == "remove":
    s.remove(int(numb))
  else:
    s.discard(int(numb))

# Print the sum of the remaining numbers in the set s
print(sum(s))


