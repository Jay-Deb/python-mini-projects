#Calculate current age of a person
#Take Dob of user and prints its current age (21 years 4 months 6 days like this)


from datetime import date

try:
    year = int(input("Enter your birth year: "))
    month = int(input("Enter your birth month: "))
    day = int(input("Enter your birth day: "))

    today = date.today()
    dob = date(year, month, day)

    if dob > today:
        print("Invalid input")

    else:
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        if days < 0:
            months -= 1

            if today.month == 1:
                prev_month = 12
                prev_year = today.year - 1
            else:
                prev_month = today.month - 1
                prev_year = today.year

            if prev_month == 12:
                next_month = 1
                next_year = prev_year + 1
            else:
                next_month = prev_month + 1
                next_year = prev_year

            last_day = date(next_year, next_month, 1) - date(prev_year, prev_month, 1)
            days += last_day.days

        if months < 0:
            years -= 1
            months += 12

        print("Your age is:", years, "years", months, "months", days, "days")

except ValueError:
    print("Invalid input") 