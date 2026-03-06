#Develop Application Menu

print("BriTay2664:)

from datetime import datetime

def spreadsheet_automation_menu():
    # Application Header
    print("2664 Spreadsheet Automation Menu")
    print("-" * 35)
    
    # Presenting Options
    print("1. Format Data Cells")
    print("2. Generate Monthly Report")
    print("3. Export to CSV")
    print("4. Exit")
    
    # The next line retrieves the inputted option and stores into the variable called user_choice.
    user_choice = input("\nPlease select an option (1-4): ")

    # Meaningful output processing
    if user_choice in ['1', '2', '3', '4']:
        print(f"\nSuccess: You have selected option number {user_choice}.")
        print("The time and date is", str(datetime.now()))
    else:
        print(f"\nNotice: '{user_choice}' is not a valid menu number.")
        print("The time and date is", str(datetime.now()))

if __name__ == "__main__":
    spreadsheet_automation_menu()