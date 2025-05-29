import products
import promotions

def main():
    # Initialize inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion instances
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Assign promotions to specific products
    product_list[0].set_promotion(second_half_price)   # MacBook Air M2
    product_list[1].set_promotion(third_one_free)      # Bose Earbuds
    product_list[3].set_promotion(thirty_percent)      # Windows License

    # Display all products
    print("\n📦 Available Products:")
    for product in product_list:
        print(product.show())

    # Simulate purchases to test promotions
    print("\n🛒 Purchase Tests:")
    try:
        print(f"2x MacBook Air M2: ${product_list[0].buy(2):.2f}")
        print(f"3x Bose Earbuds: ${product_list[1].buy(3):.2f}")
        print(f"1x Windows License: ${product_list[3].buy(1):.2f}")
    except ValueError as e:
        print(f"Purchase error: {e}")

if __name__ == "__main__":
    main()

