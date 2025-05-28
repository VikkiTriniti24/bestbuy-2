import products
import store


def start(store_obj):
    while True:
        print("\n  Store Menu")
        print("  ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\nAvailable products:")
            for index, product in enumerate(store_obj.get_all_products(), start=1):
                print(f"{index}. {product}")
        elif choice == "2":
            print(f"Total items in store: {store_obj.get_total_quantity()}")
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")


def make_order(store_obj):
    products_list = store_obj.get_all_products()
    order_list = []

    print("\n------")
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product}")
    print("------\n")

    while True:
        choice = input("Which product # do you want? (Enter empty text to finish order): ")
        if choice == "":
            break

        try:
            product_index = int(choice) - 1
            if 0 <= product_index < len(products_list):
                selected_product = products_list[product_index]
                amount = int(input("What amount do you want? "))
                if amount > selected_product.quantity:
                    print(
                        f"Not enough stock available for {selected_product.name}. Available: {selected_product.quantity}\n")
                elif amount <= 0:
                    print("Please enter a valid quantity greater than 0.\n")
                else:
                    order_list.append((selected_product, amount))
                    print("Product added to list!\n")
            else:
                print("Invalid product number, try again!\n")
        except ValueError:
            print("Invalid input, please enter a number!\n")

    if order_list:
        try:
            total_cost = store_obj.order(order_list)
            print(f"Order placed! Total cost: ${total_cost}")
        except ValueError as e:
            print(f"Order failed: {e}")
    else:
        print("No items selected, order cancelled.")


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()

