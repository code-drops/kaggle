# 1
'''Return the given number rounded to two decimal places.
    >>> round_to_two_places(3.14159)
    3.14
'''
def round_to_two_places(num):
    return round(num, 2)

# 2
'''The help for round says that ndigits (the second argument) may be negative. What do you think will happen when it is? Try some examples in the following cell?'''
x = 12345.51245
round(x,-2)

# 3
'''In a previous programming problem, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
Below is a simple function that will calculate the number of candies to smash for any number of total candies.
Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.'''
def to_smash(total_candies,n = 3):
    return total_candies % n

# 4
'''Each code cell below contains some commented-out buggy code. For each cell...
Read the code and predict what you think will happen when it's run.
Then uncomment the code and run it to see what happens. (Tip: In the kernel editor, you can highlight several lines and press ctrl+/ to toggle commenting.)
Fix the code (so that it accomplishes its intended purpose without throwing an exception)'''

round(9.9999)

x = -10
y = 5
# # Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))
print(smallest_abs)

def f(x):
    y = abs(x)
    return y

print(f(5))