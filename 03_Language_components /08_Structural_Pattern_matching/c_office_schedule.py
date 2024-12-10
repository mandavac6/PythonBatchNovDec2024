"""
Purpose: Office Schedule
    Monday to Friday  :- 9 am to 6 pm
    Saturday          :- 9 am to 1 pm
    Sunday            :- Holiday

"""


week_of_day = input("Enter week of the day:").title().strip()

match week_of_day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("TIMINGS: 9 AM to 6 PM")
    case "Saturday":
        print("TIMINGS: 9 AM to 1 PM")
    case "Sunday":
        print("----HOLIDAY----------")
    case _:
        print("INVALID ENTRY! PLEASE TRY AGAIN!!")