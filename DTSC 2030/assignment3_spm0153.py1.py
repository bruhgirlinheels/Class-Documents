Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Find the square root using the Babylionian Algorithm and incoroporating epsilon
>>> def babylonian_sqrt(x):
...     # Step 1: Choose an epsilon value
...     epsilon = 0.0001
... 
...     # Step 2: Choose an initial estimate e for the square root of x
...     e = x
... 
...     while True:
...         # Step 3: Evaluate the estimate
...         difference = abs(x/e - e)
... 
...         # Step 4: Determine if the estimate is "good enough" to stop
...         if difference <= epsilon:
...             break
... 
...         # Step 5: Revise the estimate (if needed based on Step 4)
...         e = (x/e + e) / 2
... 
...     return e
... 
... # Input validation to ensure a positive integer is entered
... while True:
...     user_input = input("Enter a positive integer: ")
...     try:
...         user_input = int(user_input)
...         if user_input > 0:
...             break
...         else:
...             print("Please enter a integer greater than zero.")
...     except ValueError:
...         print("Please enter a valid integer.")
... 
... # Compute the square root using the Babylonian Method
... square_root = babylonian_sqrt(user_input)
... 
... # Display the square root to three decimal places
