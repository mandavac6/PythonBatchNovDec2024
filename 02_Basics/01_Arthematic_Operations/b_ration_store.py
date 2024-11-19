"""
purpose : ration store


Purpose: Ration Store

    item    cost        quantity        Amount
    wheat   25/kg       30 kgs      25 * 30 = 750/-
    Rice    12/kg       50 kgs      12 * 50 = 600/-
                                    _________________
                                              1350/-
                                subsidy 20%   -270/-
                                    _________________
                                BillableAmount:1080/-

Algorithm
___________________
Step 1:  get the cost of items into variables
Step 2:  get the quantity of items into variables
Step 3:  compute the selling price to each item, and add them
Step 4:  compute the subsidy amount and subtract from the selling price
Step 5:  display the Billable Amount

"""


# Item cost 
cost_of_wheat = 25 # per kg
cost_of_rice = 12 # per kg

# Quantities of Items
qty_of_wheat = 30  # kgs
qty_of_rice = 50  # kgs


# selling amount 
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice

total_sp = sp_of_wheat + sp_of_rice
print("Total Selling Price:", total_sp)

# subsidy
subsidy_amount  = total_sp * (20/ 100) # PEMDAS
print("Subsidy Amount     :", subsidy_amount)

billable_amount = total_sp - subsidy_amount
print("Billable Amount    :", billable_amount)