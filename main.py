print("Welcome to the tip calculator.")

bill=float(input("What was the total bill? $"))
percentage=int(input("What percentage tip would you like to give? 10, 12 or 15? "))
persons=int(input("How many people to split the bill? "))

tip = percentage/100*bill
total = round((bill+tip)/persons,2)
total_str = "{:.2f}".format(total)
print(f"Each person should pay: ${total_str}")

