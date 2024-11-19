"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance

"""

# Initial Balance 
balance = 0

# Deposit 
deposit = 1500
balance += deposit
print ("Balance after min deposit:", balance) # after min deposit

# Salary Credited
salary = 3300
balance += salary
print ("Balance after salary:", balance) # after salary 

# Online Purchase
purchase = 33.33
balance -= purchase
print ("Balance after purchase:", balance) # after purchase


#  House Rent
house_rent = 1500
balance -= house_rent
print ("Balance after house rent:", balance) # after house rent
print("Final Balance:", balance)