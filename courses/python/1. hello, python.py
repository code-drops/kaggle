# 0
'''create a variable called color with an appropriate value on the line below'''
color = 'blue'

# 1
''' Create a variable called 'radius' equal to half the diameter'''
'''# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared'''
pi = 3.14159
diameter = 3
radius = diameter/2
area = pi*radius*radius

# 2
'''Swap the values to which a and b refer'''
a = [1, 2, 3]
b = [3, 2, 1]
q2.store_original_ids()
a,b = b,a

# 3
'''(a) Add parentheses to the following expression so that it evaluates to 1'''
(5 - 3) // 2

'''(b) Add parentheses to the following expression so that it evaluates to 0'''
(8 - 3) * (2 - (1 + 1))

# 4
'''Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
Write an arithmetic expression below to calculate how many candies they must smash for a given haul.'''
alice_candies = 121
bob_candies = 77
carol_candies = 109
to_smash = (alice_candies + bob_candies + carol_candies)%3