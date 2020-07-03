# 1
'''define a function called sign which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.'''
def sign(num):
    if num<0:
        return -1
    elif num>0:
        return 1
    else:
        return 0

# 2
'''Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1'''
'''Modify the definition in the cell below to correct the grammar of our print statement. (If there's only one candy, we should use the singular "candy" instead of the plural "candies")'''
def to_smash(total_candies):
    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")

    return total_candies % 3

# 3
'''I'm safe from today's weather if...

I have an umbrella...
or if the rain isn't too heavy and I have a hood...
otherwise, I'm still fine unless it's raining and it's a workday

To prove that prepared_for_weather is buggy, come up with a set of inputs where either:
the function returns False (but should have returned True), or
the function returned True (but should have returned False).'''

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)


# 4
'''The function is_negative below is implemented correctly - it returns True if the given number is negative and False otherwise.
However, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this function by 75% while keeping the same behaviour.
See if you can come up with an equivalent body that uses just one line of code, and put it in the function concise_is_negative.'''
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return True if number<0 else False

# 5
'''The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog. We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. '''

def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions."""
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)"""
    return ketchup and mustard and onion

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings."""
    return (not ketchup) and (not mustard) and (not onion)

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")"""
    if (ketchup and mustard) or (not ketchup and not mustard):
        return False
    else:
        return True

# 6
'''We’ve seen that calling bool() on an integer returns False if it’s equal to 0 and True otherwise. What happens if we call int() on a bool? Try it out in the notebook cell below.
Can you take advantage of this to write a succinct function that corresponds to the English sentence "does the customer want exactly one topping?"?'''
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings on their hot dog."""
    return (ketchup and not mustard and not onion) or (not ketchup and mustard and not onion) or (not ketchup and not mustard and onion)


