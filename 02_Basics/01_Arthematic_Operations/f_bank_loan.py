"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)


Get all values in runtime

Algorithm
-------------
Step1 : get the initial principal balance 
Step2 : input the annual interest rate
step3: get the input of years of tenure 
Step4: caluculate the final amount 
"""
# initial principal balance
initial_princpal_amount = int(input("enter initial principal balance:"))

# annual interest rate
annual_interest_rate = float(input("enter annual interest rate:"))

# time (in years) 
time_in_years = int(input("enter time (in years):"))

# final amount caluclation 
finalAmount = initial_princpal_amount * (1 + (annual_interest_rate / 100) * time_in_years)
print("Final amount:", round(finalAmount, 2))

# Intrest Paid over the tenure 
interstPaid = finalAmount - initial_princpal_amount
print("Interest Amount :", round(interstPaid, 2))