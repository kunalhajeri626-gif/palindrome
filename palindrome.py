
import sys

n = sys.argv[1]

if n == n[::-1]:
    print(n, "is a Palindrome")
else:
    print(n, "is not a Palindrome")
