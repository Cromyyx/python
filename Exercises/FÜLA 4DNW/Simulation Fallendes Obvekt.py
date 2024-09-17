initial_prinzipal_balance =\
    float(input("Enter initial balance: "))
interest_rate =\
    float(input("Enter interest rate in %: "))
number_of_times_interest_is_applied =\
    float(input("number of times interest applied per time period: "))
number_of_time_periods_elapsed =\
    float(input("number of time periods elapsed: "))

final_amount = initial_prinzipal_balance * (1 + ((interest_rate / 100) / number_of_times_interest_is_applied)) ** (number_of_times_interest_is_applied * number_of_time_periods_elapsed)
print(final_amount)
