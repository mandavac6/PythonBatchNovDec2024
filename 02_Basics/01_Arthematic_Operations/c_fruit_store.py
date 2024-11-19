"""
Purpose: Fruit Store

    Items   price       qty                         amount
    -----------------------------------------------------------
    Apples   12/piece   5 dozens = 5 * 12 = 60      12 * 60
    Mangos   34/piece   3 dozens = 3 * 12 = 36      34 * 36
                                                ---------------
                                                      1944   /-
                                discount     -2 %     - 38.88/-
                                                ---------------
                                                      1905.12/-
                                GST         +12.5 %   +238.14/-
                                                ---------------
                                                      2143.26/-
                                                ---------------

Algorithm
---------
Step 0: declare the constants 
Step 1:  cost of fruits into variables
Step 2:  quantity of fruits into variables.
         compute the end quantity, by substituting dozen value.
Step 3:  compute the selling price to each item,
         and add them
Step 4:  compute the discount amount and subtract
         from the selling price, to create payable amount
Step 5:  calculate GST amount and Add to payable amount,
         to create final amount


"""
# declare the constants 
DOZEN = 12
DISCOUNT = 2
GST = 12.5

# cost of fruits
cost_of_apple = 12  # per piece
cost_of_mango = 34  # per piece


# Quantities of fruits
qty_of_apples = 5 * DOZEN  # pieces
qty_of_mangos = 3 * DOZEN  # pieces


# Selling Price 
total_sp = cost_of_apple * qty_of_apples + cost_of_mango * qty_of_mangos  # PEDMAS
# total_sp =(cost_of_apple * qty_of_apples) + (cost_of_mango * qty_of_mangos)  # PEDMAS
print("Total Selling Price :", total_sp)



# Discount 
discount_amount = (total_sp * DISCOUNT) / 100
print("Discount Amount     :", discount_amount)



# Payable Amount 
payable_amount = total_sp - discount_amount
print("Payable Amount      :", payable_amount)



# GST Calculation
gst_on_fruits = (payable_amount * GST) / 100
print("GST on Fruits       :", gst_on_fruits)


# Final Bill
final_amount = payable_amount + gst_on_fruits
print("final Amount     :", final_amount)

# to round up the float values we can use round function to round off to the nearest decimal
print("final Amount(r)  :", round(final_amount, 2))

