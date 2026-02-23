import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


resources = data.resources
recipes = data.recipes

sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    machine_on = True

    while machine_on:
        choice = input("What would you like? (small/medium/large/off/report): ")

        if choice == "off":
            machine_on = False

        elif choice == "report":
            print(resources)

        elif choice in recipes:
            sandwich = recipes[choice]
            cost = sandwich["cost"]
            ingredients = sandwich["ingredients"]

            if sandwich_maker_instance.check_resources(ingredients):
                payment = cashier_instance.process_coins()

                if cashier_instance.transaction_result(payment, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
