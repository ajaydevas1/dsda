print("Order Details\n ")

fileinput_names = input("Enter file name to store customer details: ")
with open(fileinput_names, "w") as cust_names:
    for i in range(2):
        fname = input("Enter first name of customer: ")
        lname = input("Enter last name of customer: ")
        address = input("Enter address of customer: ")

        cust_names.write(f"First Name: {fname}, Last Name: {lname}, Address: {address}\n")
        print("Written.....")

fileinput_orders = input("Enter file name to store customer details: ")
with open(fileinput_orders, "w") as cust_orders:
    for i in range(2):
        tele_no = input("Telephone number of customer: ")
        pizza_type = input("Pizza type of customer: ")
        pizza_quantity = input("Pizza quantity of customer: ")

        cust_orders.write(f"Telephone Number: {tele_no}, Pizza Type: {pizza_type}, Pizza Quantity: {pizza_quantity}\n")
        print("Writtennn.....")



with open("custnames.txt", "r") as infile_names:
    for line in infile_names:
        name = line.strip()
        
        if len(name) >= 7:
            customer_id = name[:3] + name[-4:]
            print(f"Customer ID for {name}: {customer_id}")
            



    
