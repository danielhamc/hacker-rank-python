# Tuples

## Task
## Given an integer, n, and n space-separated integers as input, create a tuple,t ,
## n of those  integers. Then compute and print the result of hash(t).
##
## Sample Input 0
##
## 2
## 1 2
## Sample Output 0
##
## 3713081631934410656


# Main

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
