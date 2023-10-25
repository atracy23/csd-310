import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "Bacchus_supplies",
    "password": "Password",
    "host": "localhost",
    "port": "3306",
    "database": "bacchus",
    "raise_on_warnings": True
}


"""


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "T%rterr@425",
    "host": "127.0.0.1",
    "port": "51502",
    "database": "Bacchus",
    "raise_on_warnings": True
}
"""
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Personnel")
    employees = cursor.fetchall()
    """
    print("\n -- {} --".format("EMPLOYEES"))
    for employee in employees:
        print("ID: {}\nName: {} {}\nJob Title: {}\nQ1 Hours Worked: {}"
              "\nQ2 Hours Worked: {}\nQ3 Hours Worked: {}\nQ4 Hours Worked: {}\n".format(
               employee[0], employee[1], employee[2], employee[3], employee[4],
               employee[5], employee[6], employee[7]
               ))
    """
    """
    db.close()

    input("Press any key to continue...")
    """
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist.")

    else:
        print(err)

finally:

    def show_procurement(cursor, title):
        cursor.execute("SELECT suppliers.Suppliers_Company_ID, suppliers.Suppliers_Product_ID,\
            suppliers.Suppliers_Product_name, procurement.Procurement_Quantity, procurement.Procurement_Date_ordered\
            AS Ordered, procurement.Procurement_Date_Received As Received FROM bacchus.suppliers INNER JOIN bacchus.procurement \
            ON suppliers.Suppliers_Product_id = procurement.Procurement_Product_ID ")

        supplies = cursor.fetchall()

        print("\n -- {} --".format(title));
        for supply in supplies:
            print(
                "\nCompany ID: {}\nProduct ID: {}\nProduct Name: {}\nQuantity: {}\nDate Ordered: {}\nDate Received: {}\n".format(
                    supply[0], supply[1], supply[2], supply[3], supply[4], supply[5]));

    def show_orders(cursor, title):
        # method to inner join tables customer orders report

        cursor = db.cursor(cursor, title)

        # inner join query on customer orders
        cursor.execute("SELECT distributor.Distributor_Name AS Distributor, wine.Wine_Product_type AS Wine,\
            orders.Order_Quantity AS Quantity, orders.Order_Ship_Date AS 'Ship Date' FROM orders INNER JOIN distributor\
            ON orders.Order_Customer_ID = distributor.Distributor_Customer_ID INNER JOIN wine\
            ON orders.Order_Product_ID = wine.Wine_Product_ID ORDER BY distributor.Distributor_Name")

        # get the results from the customer orders query
        orders = cursor.fetchall()

        print("\n -- {} --".format(title))

        # iterate over the order data set and display the results
        for order in orders:
            print("Distributor: {}\nWine: {}\nQuantity: {}\nShip Date: {}\n".format(order[0], order[1],\
                order[2], order[3]))
        return;


    def show_chardonnayDistributors(cursor, title):
        # method to inner join tables customer orders report

        cursor = db.cursor(cursor, title)

        # inner join query on customer orders
        cursor.execute("SELECT DISTINCT distributor.Distributor_Name AS Distributor FROM orders INNER JOIN distributor\
            ON orders.Order_Customer_ID = distributor.Distributor_Customer_ID WHERE orders.Order_Product_ID = '4'")

        # get the results from the customer orders query
        distributors = cursor.fetchall()

        print("\n -- {} --".format(title))

        # iterate over the order data set and display the results
        for distributor in distributors:
            print("       {}".format(distributor[0]))
        return;

    def show_merlotDistributors(cursor, title):
        # method to inner join tables customer orders report

        cursor = db.cursor(cursor, title)

        # inner join query on customer orders
        cursor.execute("SELECT DISTINCT distributor.Distributor_Name AS Distributor FROM orders INNER JOIN distributor\
            ON orders.Order_Customer_ID = distributor.Distributor_Customer_ID WHERE orders.Order_Product_ID = '1'")

        # get the results from the customer orders query
        distributors = cursor.fetchall()

        print("\n -- {} --".format(title))

        # iterate over the order data set and display the results
        for distributor in distributors:
            print("       {}".format(distributor[0]))
        return;

    def show_cabernetDistributors(cursor, title):
        # method to inner join tables customer orders report

        cursor = db.cursor(cursor, title)

        # inner join query on customer orders
        cursor.execute("SELECT DISTINCT distributor.Distributor_Name AS Distributor FROM orders INNER JOIN distributor\
            ON orders.Order_Customer_ID = distributor.Distributor_Customer_ID WHERE orders.Order_Product_ID = '2'")

        # get the results from the customer orders query
        distributors = cursor.fetchall()

        print("\n -- {} --".format(title))

        # iterate over the order data set and display the results
        for distributor in distributors:
            print("       {}".format(distributor[0]))
        return;

    def show_chablisDistributors(cursor, title):
        # method to inner join tables customer orders report

        cursor = db.cursor(cursor, title)

        # inner join query on customer orders
        cursor.execute("SELECT DISTINCT distributor.Distributor_Name AS Distributor FROM orders INNER JOIN distributor\
            ON orders.Order_Customer_ID = distributor.Distributor_Customer_ID WHERE orders.Order_Product_ID = '3'")

        # get the results from the customer orders query
        distributors = cursor.fetchall()

        print("\n -- {} --".format(title))

        # iterate over the order data set and display the results
        for distributor in distributors:
            print("       {}".format(distributor[0]))
        return;

    def show_quantitiesSold(cursor, title):
        # method to inner join tables customer orders report

        cursor = db.cursor(cursor, title)


        # inner join query on customer orders
        cursor.execute("SELECT wine.Wine_Product_type AS Wine, orders.Order_Product_ID AS Product,\
            SUM(orders.Order_Quantity) AS 'Total Qty Sold', projections.Projections_Sales_Projections AS 'Sales Projections'\
            FROM orders INNER JOIN wine ON orders.Order_Product_ID = wine.Wine_Product_ID INNER JOIN projections\
            ON orders.Order_Product_ID = projections.Projections_Product_ID GROUP BY orders.Order_Product_ID")

        # get the results from the customer orders query
        quantities = cursor.fetchall()

        print("\n -- {} --".format(title))

        # iterate over the order data set and display the results
        for quantity in quantities:
            print("Wine: {}\nTotal Qty Sold: {}\nProjected Qty Sold: {}\nPerformance: {}\n".format(quantity[0], quantity[2],\
                                                                                    quantity[3], quantity[2] - quantity[3]))

        return;

    cursor = db.cursor()
    """
    # Printing the orders
    show_orders(cursor, "Displaying Orders")

    # Printing the Merlot Distributors
    show_merlotDistributors(cursor, "Merlot Distributors")

    # Printing the Cabernet Distributors
    show_cabernetDistributors(cursor, "Cabernet Distributors")

    # Printing the Chablis Distributors
    show_chablisDistributors(cursor, "Chablis Distributors")

    # Printing the Chardonnay Distributors
    show_chardonnayDistributors(cursor, "Chardonnay Distributors")

    # Printing Quantities of Wine Sold - sorted by wine
    show_quantitiesSold(cursor, "Quantities Sold")
    """

"""
db.close()



    config = {
        "user": "root",
        "password": "P@$$w0rd",
        "host": "127.0.0.1",
        "database": "Bacchus",
        "raise_on_warnings": True
    }
"""
db = mysql.connector.connect(**config)
cursor = db.cursor()
"""
show_procurement(cursor, "Displaying Procurement Data:")
"""

try:
    # Insert records into tables.
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("INSERT INTO Suppliers VALUES (1, 1, 'Bottle', 'Container Part', 1)")
    cursor.execute("INSERT INTO Suppliers VALUES (2, 2, 'Cork', 'Container Part', 1)")
    cursor.execute("INSERT INTO Suppliers VALUES (3, 3, 'Label', 'Transport Material', 1)")
    cursor.execute("INSERT INTO Suppliers VALUES (4, 4, 'Box', 'Transport Material', 1)")
    cursor.execute("INSERT INTO Suppliers VALUES (5, 5, 'Vat', 'Manufacturing Part', 1)")
    cursor.execute("INSERT INTO Suppliers VALUES (6, 6, 'Tubing', 'Manufacturing Part', 1)")
    cursor.execute("INSERT INTO Supply VALUES (1, 'Product Packaging', 50, 12345, '02-15-2022')")
    cursor.execute("INSERT INTO Supply VALUES (2, 'Transport Packaging', 10, 23456, '02-22-2022')")
    cursor.execute("INSERT INTO Supply VALUES (3, 'Manufacturing Components', 3, 34567, '02-07-2022')")
    cursor.execute("INSERT INTO Distributor VALUES "
                   "(1, 'Michael', 'Jordan', '123 Basketball Street', 'Anytown', 12345, '850-123-4567')")
    cursor.execute("INSERT INTO Distributor VALUES "
                   "(2, 'Kiera', 'Knightly', '456 Movie Boulevard', 'Anytown', 12345, '850-321-9876')")
    cursor.execute("INSERT INTO Distributor VALUES "
                   "(3, 'Glenn', 'Beck', 'Radio Road', 'Somewhereville', 54321, '850-112-2334')")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(1, 1, 'Michael Jordan', '100 Nice Street', 'Big City', "
                   "'Missouri', 12345, '3 9 2022', 12345, 98765)")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(2, 1, 'Michael Jordan', '200 Pleasant Place', 'Little City', "
                   "'Montana', 55443, '3 25 2022', 23456, 87654)")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(3, 2, 'Kiera Knightly', '300 Pretty Park', 'Medium City', "
                   "'California', 24680, '4 08 2022', 34567, 76543)")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(4, 2, 'Kiera Knightly', '400 Cordial Circle', 'Southern City', "
                   "'Kentucky', 35791, '4 15 2022', 45678, 65432)")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(5, 3, 'Glenn Beck', '500 Politic Parkway', 'Northern City', "
                   "'New York', 24242, '3 22 2022', 56789, 54321)")
    cursor.execute("INSERT INTO `Order` VALUES "
                   "(6, 3, 'Glenn Beck', '600 Radio Wave Walk', 'Coastal City', "
                   "'Rhode Island', 12457, '3 30 2022', 67890, 43210)")
    cursor.execute("INSERT INTO Wine VALUES (1, 1, 'Merlot', 'Red')")
    cursor.execute("INSERT INTO Wine VALUES (2, 1, 'Cabernet', 'Red')")
    cursor.execute("INSERT INTO Wine VALUES (3, 1, 'Chardonnay', 'White')")
    """
    db.commit()
    db.close()
    """

    # Show records in tables.
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Suppliers")
    suppliers = cursor.fetchall()
    print("\n--SUPPLIERS--")
    for supplier in suppliers:
        print("\nCompany ID: {}\nProduct ID: {}\nProduct Name: {}\nProduct Type: {}\nQuantity: {}"
              .format(supplier[0], supplier[1], supplier[2], supplier[3], supplier[4]))

    cursor.execute("SELECT * FROM Supply")
    supplies = cursor.fetchall()
    print("\n--SUPPLIES--")
    for supply in supplies:
        print("\nInventory ID: {}\nSupply Name: {}\nQuantity: {}\nWarehouse ID: {}\nDate Received: {}"
              .format(supply[0], supply[1], supply[2], supply[3], supply[4]))

    cursor.execute("SELECT * FROM Distributor")
    distributors = cursor.fetchall()
    print("\n--DISTRIBUTORS--")
    for distributor in distributors:
        print("\nCustomer ID: {}\nFirst Name: {}\nLast Name: {}\nStreet: {}\nCity: {}\nZIP: {}\nPhone: {}"
              .format(distributor[0], distributor[1], distributor[2], distributor[3],
                      distributor[4], distributor[5], distributor[6]))

    cursor.execute("SELECT * FROM `Order`")
    orders = cursor.fetchall()
    print("\n--ORDERS--")
    for order in orders:
        print("\nOrder Number: {}\nCustomer ID: {}\nCustomer Name: {}\nTo Street: {}\nTo City: {}\nTo State: {}\n"
              "To ZIP: {}\nShip Date: {}\nShipping ID: {}\nTracking ID: {}"
              .format(order[0], order[1], order[2], order[3], order[4],
                      order[5], order[6], order[7], order[8], order[9]))

    cursor.execute("SELECT * FROM Wine")
    wines = cursor.fetchall()
    print("\n--WINES--")
    for wine in wines:
        print("\nProduct ID: {}\nQuantity: {}\nProduct Type: {}\nColor: {}"
              .format(wine[0], wine[1], wine[2], wine[3]))

    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist.")

    else:
        print(err)

selection = 0
while selection != "q":

    print("\n\t\t1. Run Supply Procurement Report")
    print("\t\t2. Run Sales Report")
    print("\t\t3. Run Personnel Report")
    print("\n\t\tq. To Quit")

    selection = input("\n\t\tPlease select a report: ")

    def procurement():
        show_procurement(cursor, "Displaying Procurement Data:")

    def sales():
        # Printing the orders
        show_orders(cursor, "Displaying Orders")

        # Printing the Merlot Distributors
        show_merlotDistributors(cursor, "Merlot Distributors")

        # Printing the Cabernet Distributors
        show_cabernetDistributors(cursor, "Cabernet Distributors")

        # Printing the Chablis Distributors
        show_chablisDistributors(cursor, "Chablis Distributors")

        # Printing the Chardonnay Distributors
        show_chardonnayDistributors(cursor, "Chardonnay Distributors")

        # Printing Quantities of Wine Sold - sorted by wine
        show_quantitiesSold(cursor, "Quantities Sold")

    def personnel():
        print("\n -- {} --".format("EMPLOYEES"))
        for employee in employees:
            print("ID: {}\nName: {} {}\nJob Title: {}\nQ1 Hours Worked: {}"
                  "\nQ2 Hours Worked: {}\nQ3 Hours Worked: {}\nQ4 Hours Worked: {}\n".format(
                employee[0], employee[1], employee[2], employee[3], employee[4],
                employee[5], employee[6], employee[7]
            ))

    def default():
        print("Good_Bye")


    switcher = {
        "1": procurement,
        "2": sales,
        "3": personnel}

    def switch(selection):
        return switcher.get(selection, default)()

    print(switch(selection))

db.close()

