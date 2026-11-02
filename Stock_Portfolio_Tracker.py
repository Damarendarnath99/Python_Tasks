STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 135,
}


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a dict {stock: quantity}."""
    portfolio = {}
    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nEnter stock names and quantities. Type 'done' when finished.\n")

    while True:
        name = input("Stock symbol (or 'done'): ").strip().upper()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Unknown stock. Please choose from the list above.")
            continue

        qty_text = input(f"Quantity of {name}: ").strip()
        if not qty_text.isdigit() or int(qty_text) <= 0:
            print("Please enter a whole number greater than 0.")
            continue

        # Add to existing quantity if the stock was entered before
        portfolio[name] = portfolio.get(name, 0) + int(qty_text)
        print(f"Added {qty_text} share(s) of {name}.\n")

    return portfolio


def calculate_total(portfolio):
    """Return (list of report lines, total value)."""
    lines = []
    total = 0
    for name, qty in portfolio.items():
        value = STOCK_PRICES[name] * qty
        total += value
        lines.append(f"{name:<6} {qty:>5} x ${STOCK_PRICES[name]:<6} = ${value:,.2f}")
    return lines, total


def main():
    print("=== STOCK PORTFOLIO TRACKER ===\n")
    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Goodbye!")
        return

    lines, total = calculate_total(portfolio)
    report = "\n".join(lines) + f"\n{'-' * 32}\nTotal investment: ${total:,.2f}"

    print("\n=== PORTFOLIO SUMMARY ===")
    print(report)

    save = input("\nSave result to portfolio.txt? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.txt", "w") as f:
            f.write(report + "\n")
        print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()
