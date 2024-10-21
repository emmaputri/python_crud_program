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

def is_booking_overlap(new_start_date, new_end_date, car_id):  # Define function to check for booking overlaps
    """Check if the new booking overlaps with existing bookings for the same car."""  
    new_start_date_dt = datetime.strptime(new_start_date, "%Y-%m-%d")  # Convert new start date from string to datetime object
    new_end_date_dt = datetime.strptime(new_end_date, "%Y-%m-%d")  # Convert new end date from string to datetime object

    # Check for any existing booking that overlaps with the new booking for the same car
    return any(
        booking["car_id"] == car_id and (  # Check if the booking is for the same car
            (new_start_date_dt <= datetime.strptime(booking["end_date"], "%Y-%m-%d") and  # Check if the new start date is before or on the end date of the existing booking
             new_start_date_dt >= datetime.strptime(booking["start_date"], "%Y-%m-%d")) or  # Check if the new start date is after or on the start date of the existing booking
            (new_end_date_dt <= datetime.strptime(booking["end_date"], "%Y-%m-%d") and  # Check if the new end date is before or on the end date of the existing booking
             new_end_date_dt >= datetime.strptime(booking["start_date"], "%Y-%m-%d")) or  # Check if the new end date is after or on the start date of the existing booking
            (new_start_date_dt <= datetime.strptime(booking["start_date"], "%Y-%m-%d") and  # Check if the new start date is before or on the start date of the existing booking
             new_end_date_dt >= datetime.strptime(booking["end_date"], "%Y-%m-%d"))  # Check if the new end date is after or on the end date of the existing booking
        )
        for booking in bookings  # Iterate through each existing booking
    )

def check_car_exists(car_id):  # Define function to check if a car exists in the rental list
    """Check if a car exists in the list."""  
    for car in rental_cars:  # Iterate through each car in the rental_cars list
        if car["car_id"] == car_id:  # Check if the car ID matches the specified car ID
            return True  # Return True if the car exists
    return False  # Return False if the car is not found in the list

def check_customer_exists(customer_id):  # Define function to check if a customer exists in the customer list
    """Check if a customer exists in the list."""  
    for customer in customers:  # Iterate through each customer in the customers list
        if customer["cust_id"] == customer_id:  # Check if the customer ID matches the specified customer ID
            return True  # Return True if the customer exists
    return False  # Return False if the customer is not found in the list

def create_booking():
    """Create a new booking for a customer."""
    show_list_of_cars()  # Display the list of available cars for booking

    # Validate Car ID input
    car_id = input("\nEnter the Car ID you want to book: ")  # Prompt user for Car ID
    # Loop until a valid numeric Car ID is provided that exists
    while not car_id.isdigit() or not check_car_exists(int(car_id)):
        print("Invalid input or Car ID not found. Please enter a valid numeric Car ID.")  # Error message for invalid input
        car_id = input("\nEnter the Car ID you want to book: ") 
    car_id = int(car_id)  # Convert the valid Car ID input to an integer

    # Create a new customer
    customer_id = create_customer()  # Call function to create a new customer and retrieve their ID

    # Validate date inputs
    date_format = "%Y-%m-%d"  # Define the date format to be used

    while True:  # Start an infinite loop for date validation
        start_date = input("Enter Start Date (YYYY-MM-DD): ")  # Prompt user for start date
        end_date = input("Enter End Date (YYYY-MM-DD): ")  # Prompt user for end date
        
        # Check if both dates are in the correct format
        try:
            # Attempt to convert input strings to datetime objects
            start_date_valid = datetime.strptime(start_date, date_format)
            end_date_valid = datetime.strptime(end_date, date_format)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")  # Error message for invalid date format
            continue  # Continue the loop to prompt for dates again

        # Check for overlapping bookings
        overlap_found = False  # Initialize flag for overlap detection
        for booking in bookings:  # Loop through existing bookings
            if booking["car_id"] == car_id:  # Check if the current booking is for the same car
                existing_start_date_dt = datetime.strptime(booking["start_date"], date_format)  # Convert existing start date
                existing_end_date_dt = datetime.strptime(booking["end_date"], date_format)  # Convert existing end date

                # Check for date overlap conditions
                if (start_date_valid <= existing_end_date_dt and start_date_valid >= existing_start_date_dt) or \
                   (end_date_valid <= existing_end_date_dt and end_date_valid >= existing_start_date_dt) or \
                   (start_date_valid <= existing_start_date_dt and end_date_valid >= existing_end_date_dt):
                    overlap_found = True  # Set overlap flag to True
                    break  # Exit the loop if overlap is found

        if overlap_found:  # If an overlap was detected
            print("Error: The requested booking dates overlap with an existing booking for this car.")  # Inform the user
            continue  # Continue to prompt for new dates

        # Create the booking if no overlap was found
        new_booking = {
            "booking_id": len(bookings) + 1,  # Generate a new booking ID
            "car_id": car_id,  # Store the Car ID
            "cust_id": customer_id,  # Store the Customer ID
            "booking_date": datetime.now().strftime(date_format),  # Record the booking date
            "start_date": start_date,  # Store the start date
            "end_date": end_date  # Store the end date
        }
        bookings.append(new_booking)  # Add the new booking to the bookings list
        print("Booking successfully created!")  # Confirm successful booking creation
        break  # Exit the loop after successful booking


def show_booking_details():  # Define the function to display all booking details
    """Display all booking details."""  # Docstring explaining the function's purpose
    if not bookings:  # Check if the 'bookings' list is empty
        print("No bookings available.")  # Inform the user that there are no bookings
        return  # Exit the function early since there are no bookings to display

    print("\n==== BOOKING DETAILS ====")  # Print a header for booking details
    for booking in bookings:  # Iterate through each booking in the 'bookings' list
        # Find the customer associated with the booking using their customer ID
        customer = [cust for cust in customers if cust["cust_id"] == booking["cust_id"]]
        # Find the car associated with the booking using their car ID
        car = [c for c in rental_cars if c["car_id"] == booking["car_id"]]

        if customer and car:  # Check if both customer and car data are found
            customer = customer[0]  # Get the first element from the customer list
            car = car[0]  # Get the first element from the car list
            
            # Parse the booking start and end dates from strings to datetime objects
            start_date = datetime.strptime(booking['start_date'], "%Y-%m-%d")
            end_date = datetime.strptime(booking['end_date'], "%Y-%m-%d")
            
            days_booked = (end_date - start_date).days  # Calculate the number of days booked
            total_price = days_booked * car['rental_price']  # Calculate the total price for the booking

            # Display the booking details to the user
            print(f"\nBooking ID: {booking['booking_id']}")  # Print the booking ID
            print(f"Car: {car['car_brand']} {car['car_model']} ({car['year']})")  # Print car details
            print(f"Customer: {customer['first_name']} {customer['last_name']}")  # Print customer name
            print(f"Booking Date: {booking['booking_date']}")  # Print the date the booking was made
            print(f"Start Date: {booking['start_date']}")  # Print the start date of the booking
            print(f"End Date: {booking['end_date']}")  # Print the end date of the booking
            print(f"Price per day: Rp.{car['rental_price']}")  # Print the rental price per day
            print(f"Total Price: Rp.{total_price}")  # Print the total price for the booking
        else:  # If customer or car data is missing
            print("Data missing for this booking.")  # Inform the user about the missing data

            
def update_booking():  # Define the function to update an existing booking
    """Update an existing booking."""  
    booking_id = input("Enter Booking ID to update: ")  # Prompt user for the Booking ID they want to update

    # Validate Booking ID input
    # Loop until a valid numeric Booking ID is provided that exists in the bookings list
    while not booking_id.isdigit() or not any(b["booking_id"] == int(booking_id) for b in bookings):
        print("Invalid Booking ID. Please enter a valid numeric Booking ID that exists.")  # Inform user of invalid input
        booking_id = input("Enter Booking ID to update: ")  # Prompt user again for a valid Booking ID

    booking_id = int(booking_id)  # Convert the valid input to an integer for further processing
    # Find the booking that matches the given Booking ID
    booking = next((b for b in bookings if b["booking_id"] == booking_id), None)  

    if not booking:  # Check if the booking was found
        print("Booking not found.")  # Inform the user if the booking does not exist
        return  # Exit the function early since there is nothing to update

    while True:  # Start an infinite loop to get new date inputs
        new_start_date = input("Enter new Start Date (leave blank to keep current): ")  # Prompt for new start date
        new_end_date = input("Enter new End Date (leave blank to keep current): ")  # Prompt for new end date

        # Check for overlapping bookings if both dates are provided
        if new_start_date and new_end_date:  # If both new dates are provided
            if is_booking_overlap(new_start_date, new_end_date, booking["car_id"]):  # Check if the new dates overlap with existing bookings
                print("Error: The requested booking dates overlap with an existing booking.")  # Inform user of the overlap
                print("Please enter new dates.")  # Ask for new dates again
                continue  # Restart the loop to get new date inputs

            # If no overlap, update the booking's start and end dates
            booking["start_date"] = new_start_date  # Update start date
            booking["end_date"] = new_end_date  # Update end date
            break  # Exit the loop since the dates are valid
        else:  # If one or both dates are blank
            # Only update if the new date is provided
            if new_start_date:  # If a new start date is provided
                booking["start_date"] = new_start_date  # Update the start date
            if new_end_date:  # If a new end date is provided
                booking["end_date"] = new_end_date  # Update the end date
            break  # Exit the loop since at least one date is provided or both are blank


def delete_booking():  # Define the function to delete a booking
    """Delete a booking."""  
    booking_id_input = input("Enter Booking ID to delete: ")  # Prompt user for a Booking ID

    # Check if the input is numeric
    if not booking_id_input.isdigit():  # If the input is not a number
        print("Invalid input. Please enter a numeric Booking ID.")  # Inform the user about the invalid input
        return  # Exit the function early if the input is invalid

    booking_id = int(booking_id_input)  # Convert the valid input to an integer

    global bookings  # Declare that we're using the global 'bookings' list

    # Create a new list to store bookings that are not deleted
    updated_bookings = []  
    for booking in bookings:  # Loop through each booking in the global bookings list
        if booking["booking_id"] != booking_id:  # Check if the booking ID does not match the one to delete
            updated_bookings.append(booking)  # Add the booking to the updated list if it should not be deleted

    bookings = updated_bookings  # Update the global bookings list with the filtered bookings
    print("Booking deleted successfully!")  # Confirm that the booking has been deleted


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
if __name__ == "__main__":  # Checks if this script is being run directly (not imported as a module)
    main_menu()              # If the above condition is true, call the main_menu() function to start the program
