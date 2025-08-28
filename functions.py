def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price

try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    # Print results
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price is: {final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
