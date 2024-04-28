# Database-Airline-Booking-System

## Project Overview
The Flight Reservation System is designed to simplify booking processes and enhance user experience by offering customizable travel plans. Integrating flight bookings with other travel services like hotels and car rentals allows everything to be planned in one place. This system provides real-time information on flight schedules, availability, and pricing, leveraging Microsoft SQL Server and Power BI for data management and visualization.

## Features

### Database Structure
- **12 Tables**: Structured to store flights, passengers, bookings, payments, and associated travel services.
- **3 Views**: `ServiceDependingOnClass`, `ServiceAndClass`, `ServiceOfferingToClasses` to provide insights into service allocations based on travel class.
- **12 Table Level Checks**: Ensure data integrity and validity across transactions.
- **Computed Column**: Utilizes a user-defined function for dynamic data calculations.
- **3 Non-clustered Indexes**: Enhance query performance on large datasets.
- **10 Stored Procedures**: Including `Flight_Availability`, `GetFlightDetailsByLocation`, `BookFlightForPassenger`, `PassengerCRUD`, and `CalculateTotalRevenue` manage various aspects of the booking system.
- **4 User Defined Functions**
- **5 DML Triggers**: Such as `InsertSeatsOnFlightInsert`, `Insert_Payment`, `Set_Cost`, and `FlightUpdateLog` to automate and streamline database operations.
- **2 Column Data Encryptions**: Ensure data security, particularly for sensitive passenger and payment information.

### Power BI Integration
- **Visualizations**: Dashboard creation for real-time tracking of flight and booking statuses, including detailed analytics on customer behavior and revenue.
- **Reports**: Customizable reports to analyze trends and performance metrics.

## Technology Stack
- **Microsoft SQL Server**: Database management and operations.
- **Power BI**: Data visualization and business intelligence.
- **SQL Server Management Studio (SSMS)**: For database setup and maintenance.

## Setup and Installation
1. **Prerequisites**:
   - Install Microsoft SQL Server.
   - Install Power BI Desktop.
   - Install SQL Server Management Studio (SSMS).

2. **Database Setup**:
   - Run the SQL script to create the database schema and objects.
   - Ensure all user-defined functions, views, and triggers are properly set up as per the script.

3. **Power BI Setup**:
   - Open Power BI Desktop.
   - Connect Power BI to the SQL Server database using the "Get Data" option.
   - Load the necessary tables and create relationships as required.

4. **Running the Application**:
   - Access the system via Power BI reports to interact with the data.
   - Use SSMS for any direct database queries or modifications.

## Usage
- **Admins/Users**: Can interact with the database via SSMS or connected applications to manage flight reservations, check availabilities, and perform CRUD operations on user data.
- **Analysts**: Use Power BI to generate insights, track performance, and support decision-making processes.

- ###Power BI dashboard![image](https://github.com/HemantGaikwad7/Database-Airline-Booking-System/assets/144754808/aec11f2f-c9a4-455e-aff5-a54ce181f252)


