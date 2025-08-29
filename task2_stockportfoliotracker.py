def stock_portfolio():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 135, "MSFT": 300}
    portfolio = {}

    print("📈 Welcome to Stock Portfolio Tracker!")
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Stock not found in database.")
            continue

        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty

    total_value = 0
    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        print(f"{stock}: {qty} shares → ${value}")
        total_value += value

    print(f"\n💰 Total Portfolio Value: ${total_value}")

    # Optional: Save to file
    with open("portfolio.txt", "w") as f:
        f.write("Your Portfolio:\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}\n")
        f.write(f"\nTotal Portfolio Value: ${total_value}")

stock_portfolio()
