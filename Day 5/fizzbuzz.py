"""Write a program to count from 1 to n (n gotten by user input) with every number
divisible by 3 becoming 'fizz', every number divisible by 5 becoming 'buzz'
and every number divisible by both becoming 'fizzbuzz'"""

def fizzbuzzifier(n):
    if n % 15 == 0:
        return "fizzbuzz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    return str(n)

def main():
    disNumber = int(input("Please enter a number: "))
    for i in range(1, disNumber+1):
        print(fizzbuzzifier(i))

main()

