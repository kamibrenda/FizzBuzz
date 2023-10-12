"""This is a tool that will create a loop with a better performance than other iteration methods."""
"""Itertools will need to be imported though is in the standard library thus pip is not necessary."""
"""To note;"""
""""cycle(): Cycle is a function takes a basic data-type and creates an iterator out of it. This function is useful and makes building custom iterators incredibly easy in Python.
count(): Count is another generator that iterates a range. This iterator is often called an “infinite iterator,” which basically means that the count() function could essentially loop on and on forever.
islice(): The islice function is short for “iteration slice.” We can use this iterator to cut out particular elements in a data structure and iterate them.
"""

import itertools as its
def fizz_buzz(n):
    fizzes = its.cycle([""] * 2 + ["Fizz"])
    buzzes = its.cycle([""] * 4 + ["Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result = (word or n for word, n in zip(fizzes_buzzes, its.count(1)))
    for i in its.islice(result, 100):
        print(i)
        

