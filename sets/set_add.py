# Set .add()

##Apply your knowledge of the .add() operation to help your friend Rupal.
##
##Rupal has a huge collection of country stamps.
##She decided to count the total number of distinct country stamps
##in her collection. She asked for your help.
##You pick the stamps one by one from a stack of  country stamps.
##
##Find the total number of distinct country stamps.
##
##Sample Input
##
##7
##UK
##China
##USA
##France
##New Zealand
##UK
##France
##
##Sample Output

5


# Main
s = set()

n = int(input())

for _ in range(n):
  country = input()
  s.add(country)

print(len(s))
