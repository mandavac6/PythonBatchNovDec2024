"""
Purpose: Grocery Store

    Item       cost
    ---------------
    rice        10/kg
    wheat       34/kg

Algorithm
-------------
Step 1: cost of items into variables
Step 2: quantity of items from the user(in run time)

"""

# cost of items
cost_of_rice = 10  # per kg
cost_of_wheat = 34  # per kg


# Items quantity
qty_of_rice = input("Enter Qty. of Rice  (in Kgs):")
qty_of_rice = float(qty_of_rice)  # if we dont give the type of input it by default assumes string 
print("Qty of Rice  :", qty_of_rice)

qty_of_wheat= float(input("Enter Qty. of Wheat  (in Kgs):"))
print("Qty of Wheat  :", qty_of_wheat)

# Selling Price Computation
sp_of_rice = cost_of_rice * qty_of_rice
print("SP of Rice   :", sp_of_rice)

sp_of_wheat = cost_of_wheat * qty_of_wheat
print("SP of Wheat  :", sp_of_wheat)


total_sp = sp_of_rice + sp_of_wheat
print("Total SP     :", total_sp)