from banner import show_banner
from logger import info

def menu():

    print("\n===========================")
    print("1. File Monitor")
    print("2. Network Monitor")
    print("3. Packet Monitor")
    print("4. Process Monitor")
    print("5. Generate Report")
    print("6. Exit")
    print("===========================\n")

def main():

    show_banner()

    info("IDS Started Successfully")

    while True:

        menu()

        choice = input("Select Option : ")

        if choice == "1":
            print("File Monitor Coming Soon...")

        elif choice == "2":
            print("Network Monitor Coming Soon...")

        elif choice == "3":
            print("Packet Monitor Coming Soon...")

        elif choice == "4":
            print("Process Monitor Coming Soon...")

        elif choice == "5":
            print("Report Generator Coming Soon...")

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid Option")

if __name__ == "__main__":
    main()
