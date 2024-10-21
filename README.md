# Python CRUD Application for Car Rental Management

A comprehensive Python application for managing [Data Entity] data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project addresses the car rental industry, specifically focusing on the need to efficiently manage rental car data. The management of rental car information is crucial for streamlining rental processes, ensuring availability, tracking maintenance schedules, and enhancing customer service.

**Benefits:**

* Improved Data Accuracy and Consistency: Ensures the integrity of rental records and car availability status.
* Streamlined Data Management: Simplifies tracking of car inventory, bookings, and customer information.
* Enhanced Decision-Making: Provides data-driven insights for inventory management, rental pricing, and customer trends.
* Optimized Utilization: Helps maximize car usage and minimize idle time.
Reduced Administrative Work: Automates repetitive tasks related to rental management.


**Target Users:**

This application is designed for rental car agency employees, such as:

## Features

* **Create:**
   *  Add New Car Records: Input essential details such as car make, model, year, availability status, and rental price.
   * Customer Records: Register new customers with details like name, contact information, and driver’s license number.
   * Booking Entries: Record rental bookings, specifying the customer, car, and rental dates.
   * Validation Rules: Ensure data integrity by enforcing unique identifiers, proper data types, and required fields.

* **Read:**
   * Search and Retrieve Records: Apply filters to search for cars, customers, or bookings based on fields like car ID, customer name, or booking date.
   * Detailed Display: Show comprehensive information for each car, customer, or booking in an easy-to-read format.
   * Pagination and Sorting: Handle large datasets efficiently with pagination and sorting options.

* **Update:**
    * Modify Records: Update details for cars (e.g., rental price), customers (e.g., contact info), or bookings (e.g., rental period).
    * Confirmation Messages: Provide clear feedback on the success or failure of updates.
 
* **Delete:**
    * Remove Unwanted Records: Allow authorized users to delete cars, customers, or bookings.
    * Soft Delete (Optional): Implement a soft delete feature to mark records as inactive rather than permanently deleting them.
    * Data Archiving (Optional): Archive old records to maintain a clean and organized database.

* **Security:**
    * User Authentication: Implement login features to ensure only authorized personnel can access the application.
    * Role-Based Authorization: Control access to different CRUD operations based on user roles (e.g., admin, employee).
 
* **Reporting:**
    * Generate Reports: Create summaries based on car availability, booking history, and customer activity to support decision-making.
    * Export Data: Allow data export in formats such as CSV or Excel for further analysis.


## Installation

1. **Prerequisites:**
    * Python version (specify the required version)
    * Additional dependencies (list any required packages)

2. **Installation:**
    ```bash
    git clone https://github.com/<your-username>/<your-repo-name>.git
    cd <your-repo-name>
    pip install -r requirements.txt  # If using a requirements.txt file
    ```

3. **Database Setup (if applicable):**
    Follow specific instructions for configuring your database connection, aligning with the business's chosen database management system.

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new [Data Entity] record, for example, a new customer in a customer management system, providing details like name, contact information, and preferences.
    * **Read:** Search and retrieve customer information by name, ID, or other relevant criteria.
    * **Update:** Modify customer details, such as updating their address or contact details.
    * **Delete:** Remove a customer record from the system (with appropriate authorization, if applicable).

## Data Model
The application uses a relational database to store data entities such as cars, customers, and bookings. Each entity typically includes fields such as:
   * Cars:
     - car_id (Integer) - Unique identifier for each car.
     - make (String) - Car brand (e.g., Toyota, Honda).
     - model (String) - Specific model (e.g., Corolla, Civic).
     - year (Integer) - Manufacturing year.
     - rental_price_per_day (Float) - Cost per day for renting the car.
     - availability_status (Boolean) - Indicates if the car is currently available for rental.

   * Customers:
     - customer_id (Integer) - Unique identifier for each customer.
     - name (String) - Customer's full name.
     - contact_info (String) - Phone number or email.
     - driver_license (String) - Driver’s license number.

   * Bookings:
     - booking_id (Integer) - Unique identifier for each booking.
     - car_id (Integer) - ID of the booked car.
     - customer_id (Integer) - ID of the customer.
     - start_date (Date) - Rental start date.
     - end_date (Date) - Rental end date.
     - status (String) - Current booking status (e.g., confirmed, canceled).


## Contributing
Contributions are welcome! Feel free to open a pull request or submit an issue. For any questions, contact putriemma2010@gmail.com.

