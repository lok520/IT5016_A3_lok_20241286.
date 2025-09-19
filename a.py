counter=1  # Global counter to assign unique requisition IDs

# Class defining the requisition system
class requisitionsystem():
    def __init__(self):

        
        global counter
        self.date = ""              # Requisition date
        self.staff_id = ''          # Staff ID
        self.staff_name = ''        # Staff Name
        self.requisition_id = 10000 + counter  # Unique requisition ID
        counter += 1                # Increment global counter for next requisition
        self.total = 0              # Placeholder total (not directly used later)
        self.daily_cost = 0         # Cost of a single item
        self.status = ''            # Status of requisition
        self.approval_ref = ''      # Approval reference
        self.request=0              # Count of submitted requests
        self.approval=0             # Count of approved requests
        self.pending=0              # Count of not approved requests

    def staff_info(self):
        """
        Collects staff details from the user.
        
        """
        self.date = input('Please enter the DD/MM/YYYY: ')
        self.staff_id = input('Please enter your Staff ID: ')
        self.staff_name = input('Please enter your name: ')
        
    def requisitions_details(self):
        """
        Collects requisition details (items and costs) and calculates total.
        
        """
        self.total_cost = 0  # Reset total cost before adding items
        # Validate number of items
        while True:
            try:
                number = int(input('How many items have you take please enter a number:'))
                if number <= 0:
                    print(" Please enter a  number.")
                    continue
                break
            except ValueError:
                print("  Please enter a number.")
        # Loop for entering each item
        for i in range(number):
            choice= input("Enter the name of the item: ")
        
            while True:
                try:
                    self.daily_cost = float( input(f"Please enter the cost of the {choice}: $"))
                    if self.daily_cost=='': 
                        print(" please enter a number.")
                        continue
                    break
                except ValueError:
                    print("please enter the number")
            # Add item cost to total
            self.total_cost += self.daily_cost  

    def requisition_approval (self):
        """
        Determines approval status based on total cost.
        
        """
        if self.total_cost < 500:
            self.category = "Approved"  
            self.category_code = str(self.staff_id) + str(self.requisition_id)[-3:]
        elif 500 <= self.total_cost <= 1000:
            self.category = "Pending"   
            self.category_code=" Not available"
        else:
            self.category = "not approved"  
            self.category_code= " Not available"

    def respond_requsition(self):
        """
        Allows manager to respond to Pending requisitions.
        
        """
        if self.category == "Pending":
            choice = input(f"Manager: Approve requisition {self.requisition_id}? (yes/no): ").lower()
            if choice == "yes":
                self.category = "Approved"
                self.category_code = str(self.staff_id) + str(self.requisition_id)[-3:]
            elif choice == "no":
                self.category = "Not approved"
                self.category_code = "Not available"

    def display_requisitons(self):
        """
        Displays requisition summary.
        
        """
        print(f'Date :{self.date}')
        print(f'Staff ID:{self.staff_id}')
        print(f'Staff Name:{self.staff_name}')
        print(f"Total : ${self.total_cost}")
        print(f"status: {self.category}")
        print(f"approval Reference Number: {self.category_code}")

    def requisition_statistic(self):
        """
        Tracks and displays requisition statistics.
        
        """
        if self.category=='pending':
            self.request+=1
        elif self.category=='approved':
            self.approval+=1
        else:
            self.pending+=1
        print(f'The total number of requisitions submitted:{counter}')
        print(f'The total number of approved requisitions:{self.approval}')
        print(f'The total number of pending requisitions:{self.request}')
        print(f'The total number of  not approved requisitions:{self.pending}')


# Object creation and function calls
nothing=requisitionsystem()

nothing.staff_info()           # Collect staff info
nothing.requisitions_details() # Collect item details
nothing.requisition_approval() # Determine approval category
nothing.respond_requsition()   # Manager can approve pending
nothing.display_requisitons()  # Display requisition summary
nothing.requisition_statistic()# Display statistics
