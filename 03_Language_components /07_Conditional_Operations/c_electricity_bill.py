"""
Purpose: Electricity Board Current Bill Slab rates

    Electricity bill slabs
    -------------------------------------
    units Range     |    amount per unit
	-------------------------------------
    0 till 60       |   1.25
	60 till 100     |   2.00
	100 till 150    |   4.00
	150 till 250    |   7.00
	250 +           |  10.00

electricity cess : 2%
discount         : -1.11%

GST              : 7%

units consumed : 357
         60     +   40      + 50    + 100    + 107
         1.25/- + 2.00/-    + 4.00/-+ 7.00/- + 10/-

"""
import sys
units_used = 357
if units_used < 0:
    print("INVALID INPUT")
    sys.exit(0)

# Method 1
if 0 < units_used < 60:
    final_bill = units_used * 1.25
elif 0 < units_used < 100:
    remaining_units  = units_used - 60
    final_bill = 60 * 1.25 + remaining_units * 2.00
elif 0 < units_used < 150:
    remaining_units  = units_used - 60 - 40
    final_bill = 60 * 1.25 +  40 * 2.00 + remaining_units * 4.00
elif 0 < units_used < 250:
    remaining_units  = units_used - 60 - 40 - 50
    final_bill = 60 * 1.25 +  40 * 2.00 + 50 * 4.00 + remaining_units * 7.00
elif units_used > 250:
    remaining_units  = units_used - 60 - 40 - 50 - 100
    final_bill = 60 * 1.25 +  40 * 2.00 + 50 * 4.00 + 100 * 7.00 + remaining_units * 10.00

print(f"""
            units consumed  : {units_used}
            Amount          : {final_bill}
        """)


# Meathod 2 (bottoms up approach)

amount = 0
remaining_units = units_used

if units_used > 250:
    slab_units = remaining_units - 250
    amount += slab_units * 10.0
    remaining_units -= slab_units
    
if 150 < remaining_units <= 250:
    slab_units = remaining_units - 150
    amount += slab_units * 7.0
    remaining_units -= slab_units

if 100 < remaining_units <= 150:
    slab_units = remaining_units - 100
    amount += slab_units * 4.0
    remaining_units -= slab_units

if 60 < remaining_units <= 100:
    slab_units = remaining_units - 60
    amount += slab_units * 2.0
    remaining_units -= slab_units

if 0 <= remaining_units <= 60:
    slab_units = 60  # minimum charge
    amount += slab_units * 1.25


print(f"""
            units consumed  : {units_used}
            Amount          : {final_bill}
        """)
