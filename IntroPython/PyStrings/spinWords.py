# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter
# words reversed(Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.


def spin_words(sentence):
    new_sentence = []
    # split the sentence into words
    splitted_sentence = sentence.split()
    # iterate every word and check if word len >= 5
    for w in splitted_sentence:
        if len(w) >= 5:
            new_sentence.append(w[::-1])
        else:
            new_sentence.append(w)

    return ' '.join(new_sentence)


print(spin_words("Hey fellow warriors"))

# Write a function that will return the count of distinct 
# case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string.
# The input string can be assumed to contain only 
# alphabets(both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    # Iterate over the string
    # If letter count > 1 
        # count += 1
    count = 0
    new_txt = text.lower()
    for el in set(new_txt):
        if (list(new_txt).count(el)) > 1:
            count += 1
    return count

print(duplicate_count("abcdeaa"))

def fibonacci(n): # Fibonacci series up to n
    """Print a Fib series up to n.""" # Doc string summary of what this function does
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print() # Insert a break line after the function runs

fibonacci(100)
print(fibonacci.__doc__) # Doc String print

def fibonacci_list(n):
    """Fib function with return value as list."""
    a, b = 0, 1
    fib_list = []
    while a < n:
        fib_list.append(a) # append is a method which is a function defined on list type
                           # you can even define methods on obj with class definitions
        a, b = b, a+b
    return fib_list # Now the function returns a list that need to be used with print() to be seen

print(fibonacci_list(100))
print(fibonacci_list.__doc__)