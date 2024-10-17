rental_cars = []


def display_data_menu():
    """Function to display the data menu (Read Data)."""
    while True:
        print("\n==== DISPLAY HIMALAYA RENTAL CAR MENU ====")
        print("1. Show all Rental Cars")
        print("2. Show Rental Car by ID")
        print("3. Back to Main Menu")

        user_input = input("Enter your choice: ")

        if len(rental_cars) == 0:
            print("Data does not exist.")
            if user_input == "3":
                break
            continue

        if user_input == "1":
            show_list_of_cars()

        elif user_input == "2":
            car_id = int(input("Enter car ID: "))
            show_car_by_id(car_id)

        elif user_input == "3":
            break

        else:
            print("Invalid choice. Please choose a valid option.")

def show_list_of_cars():
    """Function to display all cars in the list."""
    if len(rental_cars) == 0:
        print("No cars available.")
        return
    for car in rental_cars:
        print(f"ID: {car['car_id']}, Brand: {car['car_brand']}, Model: {car['car_model']}, Year: {car['year']}, Price: {car['rental_price']}")

def show_car_by_id(car_id):
    """Function to show car by ID."""
    for car in rental_cars:
        if car["car_id"] == car_id:
            print(f"ID: {car['car_id']}, Brand: {car['car_brand']}, Model: {car['car_model']}, Year: {car['year']}, Price: {car['rental_price']}")
            return
    print("Car not found.")

def create_car():
    """Function for creating a new rental car entry."""
    while True:
        print("\n==== CREATE RENTAL CAR MENU ====")
        print("1. Create new Rental Car")
        print("2. Back to Main Menu")

        user_input = input("Please enter your choice: ")

        if user_input == "1":
            car_id = input("Enter car ID: ")
            if not car_id.isdigit():
                print("Invalid car ID. Please enter a numeric value.")
                continue
            car_id = int(car_id)

            if any(car["car_id"] == car_id for car in rental_cars):
                print("Data already exists for this car ID.")
                continue

            car_brand = input("Enter car Brand: ")
            car_model = input("Enter car Model: ")

            year = input("Enter car Year: ")
            if not year.isdigit():
                print("Invalid year. Please enter a numeric value.")
                continue
            year = int(year)

            rental_price = input("Enter Rental Price: ")
            if not rental_price.isdigit():
                print("Invalid rental price. Please enter a valid number.")
                continue
            rental_price = float(rental_price)

            new_car = {
                "car_id": car_id,
                "car_brand": car_brand,
                "car_model": car_model,
                "year": year,
                "rental_price": rental_price
            }

            print("\nDo you want to save this data?")
            print("1. Yes, Save Data")
            print("2. No, Cancel")

            save_choice = input("Enter your choice: ")

            if save_choice == "1":
                rental_cars.append(new_car)
                print("Data successfully saved!")
            else:
                print("Data not saved.")

        elif user_input == "2":
            break
        else:
            print("Invalid choice. Please choose a valid option.")



def update_car():
    """Function for updating an existing rental car entry."""
    while True:
        print("\n==== UPDATE RENTAL CAR MENU ====")
        print("1. Update Existing Rental Car")
        print("2. Back to Main Menu")

        user_input = input("Please enter your choice: ")

def delete_car():
    pass

def main():
    """Main function for the rental car program."""
    while True:
        print("\n==== WELCOME TO HIMALAYA CAR MENU ====")
        print("1. Show Rental Car List")
        print("2. Create Rental Car")
        print("3. Update Rental Car")
        print("4. Delete Rental Car")
        print("5. Exit")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            display_data_menu()
        elif user_input == "2":
            create_car()
        elif user_input == "3":
            update_car()
        elif user_input == "4":
            delete_car()
        elif user_input == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

main()