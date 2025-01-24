# Variables for calculation
cost_per_chicken_daily = 0.50  # Cost per chicken per day (feed, care, etc.)
eggs_per_chicken = 1.70  # Number of eggs each chicken lays per day
price_per_egg = 0.40  # Sale price per egg in euros

# Welcome message
print("Welcome to the Chicken Calculator!")
print("Calculate your daily or monthly net profit from selling eggs.\n")

# Input the number of chickens
num_chickens = int(input("Enter the number of chickens: "))

# Select the time period for calculation
print("\nChoose the time period for calculation:")
print("1. Daily net profit")
print("2. Monthly net profit")
choice = int(input("Your choice (1 or 2): "))

# Calculate daily values
daily_revenue = num_chickens * eggs_per_chicken * price_per_egg  # Revenue from sales
daily_cost = num_chickens * cost_per_chicken_daily  # Total cost
daily_net_profit = daily_revenue - daily_cost  # Net profit

# Calculate monthly values (30 days)
monthly_net_profit = daily_net_profit * 30

# Output based on the user's choice
if choice == 1:
    print(f"\nDaily net profit: {daily_net_profit:.2f} euros")
elif choice == 2:
    print(f"\nMonthly net profit: {monthly_net_profit:.2f} euros")
else:
    print("\nInvalid choice. Please restart the program.")
