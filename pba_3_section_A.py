
# Problem No. 1 - Unit 1 (Object-Oriented Programming)
# Petrol Pump Management System
#
# Develop a Python application to maintain fuel sales records.
#
# Create the following classes:
# 1. Customer
#    - Customer Name
#    - Fuel Type
#    - Amount Paid
#
# 2. Categorize customers as:
#    - Petrol
#    - Diesel
#
# 3. PetrolPump
#    - Add customer records.
#    - Display customer details.
#    - Display fuel sales.
#
# --------------------------------------------------

class Customer:
    def __init__(self, name, fuel_type, amount):
        self.name = name
        self.fuel_type = fuel_type
        self.amount = amount

    def display(self):
        print("Customer Name:", self.name)
        print("Fuel Type:", self.fuel_type)
        print("Amount Paid: Rs.", self.amount)


class Petrol(Customer):
    def __init__(self, name, amount):
        super().__init__(name, "Petrol", amount)


class Diesel(Customer):
    def __init__(self, name, amount):
        super().__init__(name, "Diesel", amount)


class PetrolPump:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print("Customer record added successfully!")

    def display_customers(self):
        if not self.customers:
            print("No customer records found.")
            return

        print("\n----- Customer Details -----")
        for customer in self.customers:
            customer.display()
            print("----------------------------")

    def display_sales(self):
        petrol_sales = 0
        diesel_sales = 0

        for customer in self.customers:
            if customer.fuel_type == "Petrol":
                petrol_sales += customer.amount
            else:
                diesel_sales += customer.amount

        print("\n----- Fuel Sales Report -----")
        print("Petrol Sales: Rs.", petrol_sales)
        print("Diesel Sales: Rs.", diesel_sales)
        print("Total Sales: Rs.", petrol_sales + diesel_sales)


# Main Program

pump = PetrolPump()

while True:
    print("\n===== PETROL PUMP MANAGEMENT =====")
    print("1. Add Petrol Customer")
    print("2. Add Diesel Customer")
    print("3. Display Customer Details")
    print("4. Display Fuel Sales")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter customer name: ")
        amount = float(input("Enter amount paid: "))
        customer = Petrol(name, amount)
        pump.add_customer(customer)

    elif choice == '2':
        name = input("Enter customer name: ")
        amount = float(input("Enter amount paid: "))
        customer = Diesel(name, amount)
        pump.add_customer(customer)

    elif choice == '3':
        pump.display_customers()

    elif choice == '4':
        pump.display_sales()

    elif choice == '5':
        print("Thank you for using Petrol Pump Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
