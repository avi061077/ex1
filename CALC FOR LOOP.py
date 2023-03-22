def calc_days_to_hours(num_of_days):
    return f"{num_of_days} is {num_of_days * 60} hours"


def user_validate():
    user_input_calc = int(days)
    if user_input_calc > 0:
        user_input_number = calc_days_to_hours(user_input_calc)
        # user_input_number_days = int(user_input_number)
        print(user_input_number)
    elif user_input_calc == 0:
        print('you put a zero number please put a valid number')


# else:
#     print('you put invalid numer please put a valid number  ')


user_input = ""
while user_input != 'exit':
    user_input = input('hello user please input number of days and i will convert for you\n')
    # if user_input.isdigit():
        # user_input_calc = int(days)
    # if user_input.isdigit():
    for days in user_input.split(":"):
        user_validate()
    else:
        print("you put a letter please put some number!!")
