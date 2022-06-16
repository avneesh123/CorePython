from math import factorial
from math import sqrt
from pprint import pprint as pp
from itertools import islice, count

words = "Why sometimes I believed as many as six impossible things before breakfast".split()
country_to_capital = {
    'United Kingdom': 'London',
    'Brazil': 'Brasilia',
    'Morocco': 'Rabat',
    'Sweden': 'Stockholm'}


def list_comprehension():
    print([len(word) for word in words])
    print(
        [len(str(factorial(x))) for x in range(20)])
    print(type([len(str(factorial(x))) for x in range(20)]))


# just use curly braces it avoids duplicates
def set_comprehension():
    print(
        {len(str(factorial(x))) for x in range(20)})


# just use curly braces and have key and value
def dict_comprehension():
    capital_to_country = {capital: country for country, capital in country_to_capital.items()}
    pp(capital_to_country)


def filtering_comprehension():
    print("filtering_comprehension::")
    print([x for x in range(101) if is_prime(x)])

    prime_square_divisors = {x * x: (1, x, x * x) for x in range(20) if is_prime(x)}
    pp(prime_square_divisors)


def iterable_and_iterator():
    iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
    iterator = iter(iterable)
    print(f"calling next and passing iterator == {next(iterator)}")
    print(f"calling next again and passing iterator == {next(iterator)}")
    print(["1", "2"])
    print({"1", "2"})
    print(set())


def generator_functions():
    g = gen123()
    print(next(g))
    print(next(g))
    print(next(g))
    # print(next(g))  # this will raise StopIteration exception

    # since generator are iterators and iterators are iterable they can be used in for loops
    for v in gen123():
        print(v)
    print(type(gen123()))

    # lazy initialization
    g = gen246()
    next(g)
    print("-------")
    next(g)
    print("-------")
    next(g)

    # how generator function resume flow
    pipeline()


# let's see how the code is executed in generator function
def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")


def gen123():
    yield 1
    yield 2
    yield 3


def take(count, iterable):
    counter = 0
    for item in iterable:
        if count == counter:
            return  # will stop the stream
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(
            item)  # this will get executed second time the function is called [essentially it will resume rom here]


# here function will never loop through the last 2 items in the array as they are not needed to produce the result
def pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):  # to enforce use list constructors for item in take(3, list(distinct(items)))
        print(item)


# returning first element if not present raise a value error
# this will work with any collection list, set
def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterator is empty")


# filtering comprehensions is available for all 3 comprehensions
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        return True


# laziness and the infinite
def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


def print_infinite():
    for x in lucas():
        print(x)


def generator_expressions():
    # Lazy evaluation
    million_squares = (x * x for x in range(1, 1000001))
    # force evaluation using list constructor but it will consume 40 MB memory
    print(list(million_squares)[-10:])
    # this wil return empty as generator are single use objcts
    list(million_squares)
    # execute generator expression right away
    print(sum(x * x for x in range(1, 10000001)))
    # sum of the first thousand prime
    print(sum(x for x in range(1001) if is_prime(x)))


def iterator_tools():
    # we can't use range as it is bounded on both end, but we like an open ended version of range which is what
    # itertools.count() provided
    # islice take generator expression
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(list(thousand_primes))
    # now creating sum is very easy as well
    print(sum(islice((x for x in count() if is_prime(x)), 1000)))


def zip_demo():
    sunday = [12, 14, 15, 115, 23, 34]
    monday = [12, 14, 15, 115, 23, 34]
    for item in zip(sunday, monday):
        print(item)

    # can be used in for loop for tuple unpacking
    for sun, mon in zip(sunday, monday):
        print("average=", (sun+mon)/2)


if __name__ == '__main__':
    list_comprehension()
    set_comprehension()
    dict_comprehension()
    filtering_comprehension()
    iterable_and_iterator()
    generator_functions()
    generator_expressions()
    iterator_tools()
    zip_demo()
