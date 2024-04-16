def miles_to_km():
    user_input = float(input("enter a number"))
    convert_type = str(input("enter number 1 to convert km to miles and enter 2 for miles to km"))
    if convert_type == "2":
        final_km = (user_input * 1.6)
        print("your converted value is", final_km)
    if convert_type == "1":
        final_mile = (user_input * 0.621371 )
        print("your converted miles is", final_mile)
    return
miles_to_km()

