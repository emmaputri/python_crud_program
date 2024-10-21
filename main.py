from datetime import datetime

# Databases
rental_cars = [
    {"car_id": 1, "car_brand": "Toyota", "car_model": "Yaris", "year": 2008, "rental_price": 200000},
    {"car_id": 2, "car_brand": "Honda", "car_model": "Civic", "year": 2020, "rental_price": 250000},
    {"car_id": 3, "car_brand": "Mitsubishi", "car_model": "Xpander", "year": 2022, "rental_price": 450000},
    {"car_id": 4, "car_brand": "Wuling", "car_model": "Cortez", "year": 2020, "rental_price": 400000},
    {"car_id": 5, "car_brand": "Hyundai", "car_model": "Stargazer", "year": 2023, "rental_price": 500000}
]

# Sample customer data
customers = [
    {"cust_id": 1, "first_name": "Emma", "last_name": "Putri", "nationality": "Indonesian", "id_or_passport": "A19950808",
     "driving_license": "Local", "phone_number": "+62808081995", "email": "emmaputri@yahoo.com"},
    {"cust_id": 2, "first_name": "Sam", "last_name": "Smith", "nationality": "British", "id_or_passport": "B19051992",
     "driving_license": "International", "phone_number": "+4419051992", "email": "sam.smith@yahoo.co.uk"},
    {"cust_id": 3, "first_name": "Yoon", "last_name": "Jeonghan", "nationality": "Korean", "id_or_passport": "C10041995",
     "driving_license": "International", "phone_number": "+8210041995", "email": "yoonjeong@yahoo.kr"},
    {"cust_id": 4, "first_name": "Greg", "last_name": "Hsu", "nationality": "Taiwanese", "id_or_passport": "D31101995",
     "driving_license": "International", "phone_number": "+886931101995", "email": "greg_hsu@yahoo.tw"},
    {"cust_id": 5, "first_name": "Vidi", "last_name": "Aldiano", "nationality": "Indonesian", "id_or_passport": "E29041990",
     "driving_license": "Local", "phone_number": "+62829041990", "email": "oxavia.aldiano@yahoo.id"}
]

# Sample booking data
bookings = []

def show_list_of_cars():
    """Display all available cars for rental."""
    if not rental_cars:
        print("No cars available.")
        return
    print("\n==== AVAILABLE RENTAL CARS ====")
    for car in rental_cars:
        print(f"ID: {car['car_id']}, Brand: {car['car_brand']}, Model: {car['car_model']}, Year: {car['year']}, Price: Rp.{car['rental_price']}")

def create_customer():
    """Create a new customer entry."""
    print("\n==== CUSTOMER REGISTRATION ====")
    customer_id = len(customers) + 1
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    nationality = input("Enter Nationality: ")
    id_or_passport = input("Enter ID/Passport Number: ")
    driving_license = input("Enter Driving License Type (International/Local): ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    new_customer = {
        "cust_id": customer_id,
        "first_name": first_name,
        "last_name": last_name,
        "nationality": nationality,
        "id_or_passport": id_or_passport,
        "driving_license": driving_license,
        "phone_number": phone_number,
        "email": email
    }

    customers.append(new_customer)
    print("Customer successfully registered!")
    return customer_id

def is_booking_overlap(new_start_date, new_end_date, car_id):
    """Check if the new booking overlaps with existing bookings for the same car."""
    new_start_date_dt = datetime.strptime(new_start_date, "%Y-%m-%d")
    new_end_date_dt = datetime.strptime(new_end_date, "%Y-%m-%d")

    return any(
        booking["car_id"] == car_id and (
            (new_start_date_dt <= datetime.strptime(booking["end_date"], "%Y-%m-%d") and
             new_start_date_dt >= datetime.strptime(booking["start_date"], "%Y-%m-%d")) or
            (new_end_date_dt <= datetime.strptime(booking["end_date"], "%Y-%m-%d") and
             new_end_date_dt >= datetime.strptime(booking["start_date"], "%Y-%m-%d")) or
            (new_start_date_dt <= datetime.strptime(booking["start_date"], "%Y-%m-%d") and
             new_end_date_dt >= datetime.strptime(booking["end_date"], "%Y-%m-%d"))
        )
        for booking in bookings
    )

def check_car_exists(car_id):
    """Check if a car exists in the list."""
    for car in rental_cars:
        if car["car_id"] == car_id:
            return True
    return False

def check_customer_exists(customer_id):
    """Check if a customer exists in the list."""
    for customer in customers:
        if customer["cust_id"] == customer_id:
            return True
    return False

def create_booking():
    """Create a new booking for a customer."""
    show_list_of_cars()

    # Validate Car ID input
    car_id = input("\nEnter the Car ID you want to book: ")
    while not car_id.isdigit() or not check_car_exists(int(car_id)):
        print("Invalid input or Car ID not found. Please enter a valid numeric Car ID.")
        car_id = input("\nEnter the Car ID you want to book: ")
    car_id = int(car_id)  # Convert the valid input to integer

    # Create a new customer
    customer_id = create_customer()

    # Validate date inputs
    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")
    date_format = "%Y-%m-%d"
    
    while True:
        # Check if both dates are in the correct format
        start_date_valid = datetime.strptime(start_date, date_format) if len(start_date) == 10 else None
        end_date_valid = datetime.strptime(end_date, date_format) if len(end_date) == 10 else None
        
        if start_date_valid and end_date_valid:
            break  # Dates are valid, exit the loop
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")

    # Check for overlapping bookings
    overlap_found = False
    for booking in bookings:
        if booking["car_id"] == car_id:
            existing_start_date_dt = datetime.strptime(booking["start_date"], date_format)
            existing_end_date_dt = datetime.strptime(booking["end_date"], date_format)

            # Check for date overlap conditions
            if (start_date_valid <= existing_end_date_dt and start_date_valid >= existing_start_date_dt) or \
               (end_date_valid <= existing_end_date_dt and end_date_valid >= existing_start_date_dt) or \
               (start_date_valid <= existing_start_date_dt and end_date_valid >= existing_end_date_dt):
                overlap_found = True
                break

    if overlap_found:
        print("Error: The requested booking dates overlap with an existing booking for this car.")
        return

    # Create the booking
    new_booking = {
        "booking_id": len(bookings) + 1,
        "car_id": car_id,
        "cust_id": customer_id,
        "booking_date": datetime.now().strftime(date_format),
        "start_date": start_date,
        "end_date": end_date
    }
    bookings.append(new_booking)
    print("Booking successfully created!")

def show_booking_details():
    """Display all booking details."""
    if not bookings:
        print("No bookings available.")
        return

    print("\n==== BOOKING DETAILS ====")
    for booking in bookings:
        customer = [cust for cust in customers if cust["cust_id"] == booking["cust_id"]]
        car = [c for c in rental_cars if c["car_id"] == booking["car_id"]]

        if customer and car:
            customer = customer[0]  # Get the first element from the list
            car = car[0]  # Get the first element from the list
            start_date = datetime.strptime(booking['start_date'], "%Y-%m-%d")
            end_date = datetime.strptime(booking['end_date'], "%Y-%m-%d")
            days_booked = (end_date - start_date).days
            total_price = days_booked * car['rental_price']

            print(f"\nBooking ID: {booking['booking_id']}")
            print(f"Car: {car['car_brand']} {car['car_model']} ({car['year']})")
            print(f"Customer: {customer['first_name']} {customer['last_name']}")
            print(f"Booking Date: {booking['booking_date']}")
            print(f"Start Date: {booking['start_date']}")
            print(f"End Date: {booking['end_date']}")
            print(f"Price per day: Rp.{car['rental_price']}")
            print(f"Total Price: Rp.{total_price}")
        else:
            print("Data missing for this booking.")
            
def update_booking():
    """Update an existing booking."""

    while True:
        try:
            booking_id = int(input("Enter Booking ID to update: "))
            break  # Exit the loop if input is valid (integer)
        except ValueError:
            print("Invalid Booking ID. Please enter a number.")

    booking = [b for b in bookings if b["booking_id"] == booking_id]
    if not booking:
        print("Booking not found.")
        return

    booking = booking[0]  # Get the first element from the list

    new_start_date = input("Enter new Start Date (leave blank to keep current): ")
    new_end_date = input("Enter new End Date (leave blank to keep current): ")

    if new_start_date and new_end_date:
        if is_booking_overlap(new_start_date, new_end_date, booking["car_id"]):
            print("Error: The requested booking dates overlap with an existing booking.")
            return

        booking["start_date"] = new_start_date
        booking["end_date"] = new_end_date
    print("Booking updated successfully.")

def delete_booking():
    """Delete a booking."""
    try:
        booking_id = int(input("Enter Booking ID to delete: "))
    except ValueError:
        print("Invalid input. Please enter a numeric Booking ID.")
        return

    global bookings
    bookings = [b for b in bookings if b["booking_id"] != booking_id]
    print("Booking deleted successfully!")

# Main menu to interact with the system
def main_menu():
    while True:
        print("\n==== CAR RENTAL SYSTEM ====")
        print("1. Show Available Cars")
        print("2. Create Booking")
        print("3. Show Booking Details")
        print("4. Update Booking")
        print("5. Delete Booking")
        print("6. Exit")

        choice = input("Select an option: ")
        if choice == "1":
            show_list_of_cars()
        elif choice == "2":
            create_booking()
        elif choice == "3":
            show_booking_details()
        elif choice == "4":
            update_booking()
        elif choice == "5":
            delete_booking()
        elif choice == "6":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
