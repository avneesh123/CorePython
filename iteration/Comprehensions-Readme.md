![img_1.png](img_1.png)

### List 

- ![img_2.png](img_2.png)
- -Equivalent imperative code
- ![img_3.png](img_3.png)
- ![img_4.png](img_4.png)
- ![img_5.png](img_5.png)
- Comprehensions shouldn't have any side effects like printing to console then use for loops
- ```
   print([x for x in range(101) if is_prime(x)])
  ```
- Avoid excess complexity in comprehensions as it is less readable
- ![img_6.png](img_6.png)

Iterable and Iterator
-Used when you don't want to traverse through the whole collection
- Iterable - Allow us to pass an iterable objects [usually a collection or stream of objs] to built in iter() fn
to get iterator for the iterable object
- Iterator - Requires that we can pass the iterator object to the built-in next to fetch the next value from 
the underlying collection
- ![img_7.png](img_7.png)
- Once reached the end Python raises StopIteration exception
- -![img_8.png](img_8.png)
- Higher level constructs like for loop etc are built directly on iterable and iterator


## Generator Functions
- ![img_9.png](img_9.png)
- Yield
- ![img_10.png](img_10.png)
- These FUnction return generator obj which are iterator
- Also since iterator are iterable generator obj can be pass to any context which expect iterable like for loops
- ![img_12.png](img_12.png)
- Maintaining State in Generators
- Resume flow nature make these generators more complex so we will use pycharm debugger
- ![img_11.png](img_11.png)
- USe the list contructor to acheive this
- ```
  for item in take(3, list(distinct(items)))
  ```
- ![img_13.png](img_13.png) 

- #### Generator Expression
- Cross with comprehension and generators
- Similar syntax as comprehension
- Result in a generator object 
- ![img_14.png](img_14.png)
- Generator are single use objects
- ![img_15.png](img_15.png)
- ![img_16.png](img_16.png)
- Execute right away
- ![img_17.png](img_17.png)

## Iteration Tools
- ![img_18.png](img_18.png)
- ![img_19.png](img_19.png)
- ![img_20.png](img_20.png)
- ![img_21.png](img_21.png)
- ![img_22.png](img_22.png)
- ![img_23.png](img_23.png)
- ![img_24.png](img_24.png)
- ![img_25.png](img_25.png)

### SUMMARY
- ![img_26.png](img_26.png)
- ![img_27.png](img_27.png)
- ![img_28.png](img_28.png)