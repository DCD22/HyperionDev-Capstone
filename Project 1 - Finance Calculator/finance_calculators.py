
import math

# Getting Input

calculation_selection = input(
    "You have two options to choose from: \n"
    "\ninvestment - to calculate the amount of interest you'll earn on your investment\n"
    "bond - to calculate the amount you'll have to pay on a home loan\n"
    "\nPlease enter your selection using 'investment' or 'bond': "
).lower()

# This code will run if user selects investment
if calculation_selection == "investment":
    # Asking user to input information for use in calculation and assigning variables
    money_amount = float(
        input("Please enter the amount of money you are depositing: "))

    interest_rate = float(input(
        "Please enter your interest rate, only enter the number - no need for the %: "))

    length = int(input("How many years do you plan to invest for? "))

    interest_selection = input(
        "Using 'simple' or 'compound', please enter the type of interest you would like to use: ").lower()
    # These are the calculations used for simple and compound interest
    if interest_selection == "simple":

        result = money_amount * (1 + (interest_rate / 100) * length)

    elif interest_selection == "compound":
        result = money_amount * math.pow((1 + (interest_rate / 100)), length)

    else:
        print("You have made an incorrect selection, please try again.")
        exit(1)
    # This will print the result of the calculations for investment
    print(
        f"The amount of money you will have from your investment is: £{result:.2f}")

    # This code will run if user selects bond
elif calculation_selection == "bond":
    # Asking user to input information for use in calculation and assigning variables
    house_value = int(
        input("Please enter the current value of your property: "))

    interest_value = float(input(
        "Please enter your interest rate, only enter the number - no need for the %: "))

    years = int(
        input("Over how many years would you like to repay this amount? "))
    # This is the calculation for how much the user will have to pay back using a bond loan.
    repayment = ((interest_value / 100) / 12) * house_value / (1 - (1 + (interest_value / 100)) ** (-years))
    # This wil print the calculation for the bond.
    print(
        f"The amount you will have to pay each month will be: £{repayment:.2f}")
else:
    print("There has been an error, please try again.")
