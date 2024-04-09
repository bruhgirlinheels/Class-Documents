Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Print the welcome message
... print("Welcome to the Compound Interest Calculator")
Welcome to the Compound Interest Calculator
>>> # Prompt to enter initial amount
>>> balance = float(input("Please enter the initial amount of your investment: "))
Please enter the initial amount of your investment: 25000
>>> # Prompt to enter interest rate
>>> interest = float(input("Please enter the interest rate (e.g., '0.03' for 3% interest): "))
Please enter the interest rate (e.g., '0.03' for 3% interest): .04
>>> # Prompt to enter the years
>>> num_years = int(input("Please enter the number of years for the investment: "))
Please enter the number of years for the investment: 10
>>> # Prompt to enter annual compounding
>>> num_compound = int(input("Please enter the number of compoundings per year: "))
Please enter the number of compoundings per year: 12
>>> # Calculate the compound amount
>>> final_balance = balance * (1 + (interest / num_compound)) ** (num_compound * num_years)
>>> # Calculate the interest earned
>>> interest_earned = final_balance - balance
>>> print(f"Original Investment: ${balance:,.2f}")
Original Investment: $25,000.00
>>> print(f"Interest Earned:     ${interest_earned:,.2f}")
Interest Earned:     $12,270.82
>>> print(f"Final Balance:       ${final_balance:,.2f}")
Final Balance:       $37,270.82
