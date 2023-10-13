"""This  it makes use of Python’s bridge to scientific computing, lambda.
One of the most frequently used methods in this regard is the map() method. This method is going to take an expression that we can create using lambda as well as an iterative data structure."""

print(*map(lambda i: 'Fizz'*(not i%4)+'Buzz'*(not i%5) or i, range(1,201)),sep='\n')