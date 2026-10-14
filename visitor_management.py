
from datetime import datetime

visitors = []

while True:

    print("\n================================================")
    print("          VISITOR MANAGEMENT SYSTEM")
    print("================================================")
    print("1.  Add Visitor")
    print("2.  View All Visitors")
    print("3.  Search by Visitor ID")
    print("4.  Search by Name")
    print("5.  Check Visitors by Date")
    print("6.  Check-Out Visitor")
    print("7.  Show Visitors IN")
    print("8.  Show Visitors OUT")
    print("9.  Show Today's Visitors")
    print("10. Count Total Visitors")
    print("11. Count Current Visitors IN")
    print("12. Remove Visitor Record")
    print("13. Exit")
    print("================================================")

    choice = input("Enter your choice: ").strip()

    # 1. ADD VISITOR

    if choice == "1":

        print("\n---------- ADD VISITOR ----------")

        visitor_id = input("Enter Visitor ID: ").strip().upper()
        name = input("Enter Name: ").strip().title()
        phone = input("Enter Phone Number: ").strip()
        aadhar = input("Enter Aadhar Number: ").strip()
        bike_no = input("Enter Bike Number: ").strip().upper()
        bike_no = bike_no.replace(" ", "")

        purpose = input("Enter Purpose of Visit: ").strip().title()

        # Automatic date and time
        current_date = datetime.now().strftime("%d-%m-%Y")
        current_time = datetime.now().strftime("%I:%M:%S %p")

        visitor = {
            "id": visitor_id,
            "name": name,
            "phone": phone,
            "aadhar": aadhar,
            "bike_no": bike_no,
            "date": current_date,
            "time": current_time,
            "purpose": purpose,
            "status": "IN",
            "exit_date": "-",
            "exit_time": "-"
        }

        visitors.append(visitor)

        print("\nVisitor added successfully!")
        print("Entry Date :", current_date)
        print("Entry Time :", current_time)
        print("Status     : IN")

    # 2. VIEW ALL VISITORS

    elif choice == "2":

        print("\n---------- ALL VISITORS ----------")

        if len(visitors) == 0:
            print("No visitor records found.")

        else:

            for visitor in visitors:

                print("\n----------------------------------------")
                print("ID         :", visitor["id"])
                print("Name       :", visitor["name"])
                print("Phone      :", visitor["phone"])
                print("Aadhar     :", visitor["aadhar"])
                print("Bike No    :", visitor["bike_no"])
                print("Entry Date :", visitor["date"])
                print("Entry Time :", visitor["time"])
                print("Purpose    :", visitor["purpose"])
                print("Status     :", visitor["status"])
                print("Exit Date  :", visitor["exit_date"])
                print("Exit Time  :", visitor["exit_time"])

    # 3. SEARCH BY VISITOR ID

    elif choice == "3":
        print("\n---------- SEARCH BY ID ----------")
        search_id = input("Enter Visitor ID: ").strip().upper()
        found = False
        for visitor in visitors:
            if visitor["id"].upper() == search_id:

                print("\nVisitor Found!")
                print("----------------------------------------")
                print("ID         :", visitor["id"])
                print("Name       :", visitor["name"])
                print("Phone      :", visitor["phone"])
                print("Aadhar     :", visitor["aadhar"])
                print("Bike No    :", visitor["bike_no"])
                print("Entry Date :", visitor["date"])
                print("Entry Time :", visitor["time"])
                print("Purpose    :", visitor["purpose"])
                print("Status     :", visitor["status"])
                print("Exit Date  :", visitor["exit_date"])
                print("Exit Time  :", visitor["exit_time"])

                found = True

        if found == False:

            print("Visitor not found.")

    # 4. SEARCH BY NAME

    elif choice == "4":

        print("\n---------- SEARCH BY NAME ----------")

        search_name = input("Enter Visitor Name: ").strip().lower()

        found = False

        for visitor in visitors:

            if visitor["name"].lower() == search_name:

                print("\n----------------------------------------")
                print("ID      :", visitor["id"])
                print("Name    :", visitor["name"])
                print("Phone   :", visitor["phone"])
                print("Bike No :", visitor["bike_no"])
                print("Date    :", visitor["date"])
                print("Time    :", visitor["time"])
                print("Purpose :", visitor["purpose"])
                print("Status  :", visitor["status"])

                found = True

        if found == False:

            print("Visitor not found.")


    # 5. CHECK VISITORS BY DATE

    elif choice == "5":

        print("\n---------- VISITORS BY DATE ----------")

        search_date = input("Enter Date (DD-MM-YYYY): ").strip()

        found = False

        for visitor in visitors:

            if visitor["date"] == search_date:

                print("\n----------------------------------------")
                print("ID      :", visitor["id"])
                print("Name    :", visitor["name"])
                print("Phone   :", visitor["phone"])
                print("Bike No :", visitor["bike_no"])
                print("Time    :", visitor["time"])
                print("Purpose :", visitor["purpose"])
                print("Status  :", visitor["status"])

                found = True

        if found == False:

            print("No visitors found on this date.")


    # 6. CHECK-OUT VISITOR

    elif choice == "6":

        print("\n---------- CHECK-OUT VISITOR ----------")

        checkout_id = input("Enter Visitor ID: ").strip().upper()

        found = False

        for visitor in visitors:
            if visitor["id"].upper() == checkout_id:

                found = True

                if visitor["status"] == "IN":

                    exit_date = datetime.now().strftime("%d-%m-%Y")
                    exit_time = datetime.now().strftime("%I:%M:%S %p")

                    visitor["status"] = "OUT"
                    visitor["exit_date"] = exit_date
                    visitor["exit_time"] = exit_time

                    print("\nVisitor checked out successfully!")
                    print("Exit Date :", exit_date)
                    print("Exit Time :", exit_time)
                    print("Status    : OUT")

                else:

                    print("\nVisitor is already OUT.")

        if found == False:

            print("Visitor not found.")

    # 7. SHOW VISITORS IN

    elif choice == "7":

        print("\n---------- VISITORS CURRENTLY IN ----------")

        found = False

        for visitor in visitors:

            if visitor["status"] == "IN":

                print("\n----------------------------------------")
                print("ID      :", visitor["id"])
                print("Name    :", visitor["name"])
                print("Phone   :", visitor["phone"])
                print("Bike No :", visitor["bike_no"])
                print("Date    :", visitor["date"])
                print("Time    :", visitor["time"])
                print("Purpose :", visitor["purpose"])
                print("Status  :", visitor["status"])

                found = True

        if found == False:

            print("No visitors are currently IN.")


    # 8. SHOW VISITORS OUT

    elif choice == "8":

        print("\n---------- VISITORS OUT ----------")

        found = False

        for visitor in visitors:

            if visitor["status"] == "OUT":

                print("\n----------------------------------------")
                print("ID        :", visitor["id"])
                print("Name      :", visitor["name"])
                print("Phone     :", visitor["phone"])
                print("Bike No   :", visitor["bike_no"])
                print("Entry Date:", visitor["date"])
                print("Entry Time:", visitor["time"])
                print("Exit Date :", visitor["exit_date"])
                print("Exit Time :", visitor["exit_time"])
                print("Status    :", visitor["status"])

                found = True

        if found == False:

            print("No visitors are OUT.")


    # 9. TODAY'S VISITORS

    elif choice == "9":

        print("\n---------- TODAY'S VISITORS ----------")

        today = datetime.now().strftime("%d-%m-%Y")

        found = False

        for visitor in visitors:

            if visitor["date"] == today:

                print("\n----------------------------------------")
                print("ID      :", visitor["id"])
                print("Name    :", visitor["name"])
                print("Phone   :", visitor["phone"])
                print("Bike No :", visitor["bike_no"])
                print("Time    :", visitor["time"])
                print("Purpose :", visitor["purpose"])
                print("Status  :", visitor["status"])

                found = True

        if found == False:

            print("No visitors today.")
    # 10. COUNT TOTAL VISITORS

    elif choice == "12":

        print("\n---------- TOTAL VISITORS ----------")

        total = 0

        for visitor in visitors:

            total = total + 1

        print("Total Visitor Records:", total)


    # 11. COUNT CURRENT VISITORS IN

    elif choice == "13":

        print("\n---------- CURRENT VISITORS ----------")

        count = 0

        for visitor in visitors:

            if visitor["status"] == "IN":

                count = count + 1

        print("Currently IN:", count)


    # 12. REMOVE VISITOR RECORD

    elif choice == "14":

        print("\n---------- REMOVE VISITOR ----------")

        remove_id = input("Enter Visitor ID: ").strip().upper()

        found = False

        for visitor in visitors:

            if visitor["id"].upper() == remove_id:

                visitors.remove(visitor)

                print("\nVisitor record removed successfully.")

                found = True
                break

        if found == False:

            print("Visitor not found.")


    # 13. EXIT

    elif choice == "15":

        print("\n========================================")
        print("Thank you for using Visitor")
        print("Management System!")
        print("========================================")

        break


    # ==================================================
    # INVALID CHOICE
    # ==================================================

    else:

        print("\nInvalid choice!")
        print("Please enter a number from 1 to 15.")
