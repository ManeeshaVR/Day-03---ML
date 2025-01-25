def yards_to_meters(yards):
    return yards * 0.9144

def meters_to_yards(meters):
    return meters * 1.09361

def main():
    print("Unit Converter: Yards to Meters and Meters to Yards")
    value = float(input("Enter the value to convert: "))
    
    print("Choose the conversion:")
    print("1. Yards to Meters")
    print("2. Meters to Yards")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        result = yards_to_meters(value)
        print(f"{value} yards is equal to {result:.2f} meters.")
    elif choice == '2':
        result = meters_to_yards(value)
        print(f"{value} meters is equal to {result:.2f} yards.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

main()