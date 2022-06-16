- If key in dict not present error
- ![img.png](img.png)
- ![img_1.png](img_1.png)
- Let's modify our function to handle error
- ![img_2.png](img_2.png)
- ```
  from exceptions.exceptional import convert 
  convert("fdsfds".split()) 
  ```
- convert(512) this time it will Type error as it is expecting the string
- ![img_3.png](img_3.png)
- Except can accept a tuple i.e multiple exception
- -Pass 
- ![img_4.png](img_4.png)
- -Accessing Exception Objects and print error detail to standard error stream
- ![img_5.png](img_5.png)
- -F String ! Feature 
    - If you insert an !r after the expression, the repr representation of the value would be inserted 
    - ```
      exceptions.exceptional import convert
      convert("fail".split())
      ```
      
- Re-Raising Exception
- Send code back to caller is a bad practise as it can be ignored we should use raise
- ![img_6.png](img_6.png)

-Exceptions are Part of API
- ![img_7.png](img_7.png)
- ![img_8.png](img_8.png)
- ![img_9.png](img_9.png)
- ![img_10.png](img_10.png)
- IndexError, ValueError, KeyError
- Avoid Explicit Type Checks
- ![img_11.png](img_11.png)
- ![img_12.png](img_12.png)
- 2 Approach to prepare for failure
- ![img_13.png](img_13.png)
- ![img_14.png](img_14.png)
- ![img_15.png](img_15.png)
- ![img_16.png](img_16.png)
- ![img_17.png](img_17.png)
- ![img_18.png](img_18.png)
- ![img_19.png](img_19.png)
- ![img_20.png](img_20.png)

CleanUp Actions
- COntext Managers
- For simple case use finally
- ![img_21.png](img_21.png)
- ![img_22.png](img_22.png)
- ![img_23.png](img_23.png)

Platform Specific Code
- ![img_24.png](img_24.png)
- Even though msvcrt.getch() is inside the try block but it's scope will be module
- If import is failed as we are not running in windows we go inside except ImportError
- ![img_25.png](img_25.png)
- ![img_26.png](img_26.png)
- ![img_27.png](img_27.png)


SUMMARY
- ![img_28.png](img_28.png)
- ![img_29.png](img_29.png)
- ![img_30.png](img_30.png)
- ![img_31.png](img_31.png)