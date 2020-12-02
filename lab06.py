"""
To start, we will generate a random interger between 1 and 20, and
based on the result of the random number, we check to see if it falls under certain range
if the number is greater than 15, then the result will be "Cherries"
otherise if the number is greater than 10, then the result will be "Orange"
otherise if the number is greater than 5, then the result will be "Plum"
otherise if the number is greater than 2, then the result will be "Melon"
otherise if the number is greater than 1, then the result will be "Bell
if the number is not any of the above, then the result will be "Bar"

we iterate over using a loop three times and print the result to the user.
as an example " Plum Cherries Orange"
"""

"""
num = generate random number

if num is greater than 15,
    then the result will be "Cherries"
otherwise if num is > 10,
    then the result will be "Orange"
otherise if the number is > 5,
    then the result will be "Plum"
otherise if the number is > 2,
    then the result will be "Melon"
otherise if the number is > 1,
    then the result will be "Bell"
otherwise
    the result will be "Bar"

loop three times
    print the output (fruit) tot the user
"""

import random

def main():
    for i in range(3):
        outcome = spinWheel()
        print(outcome, end=" ")

def spinWheel():
    n = random.randint(1, 20)
    if n > 15:
        return "Cherries"
    elif n > 10:
        return "Orange"
    elif n > 5:
        return "Plum"
    elif n > 2:
        return "Melon"
    elif n > 1:
        return "Bell"
    else:
        return "Bar"

main()

