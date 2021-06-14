from IPython.display import clear_output

class parkingGarage():
    def __init__(self,tickets):
        self.tickets = tickets
        self.availableTickets = [1,2,3,4,5,6,7,8,9,10]
        self.takenSpots = []
        
    # Take Ticket 
    
    def takeTicket(self):
        clear_output()
        if self.availableTickets == []:
            print("Sorry. The Garage is full. Please try back later!")
        else:
            ticketTaken = self.availableTickets.pop()
            self.takenSpots.append(ticketTaken)
            print('Please take ticket ' + str(self.takenSpots) + " and park in spot " + str(self.takenSpots) + ".")
            print("Garage Spots Remaining: " + str(self.availableTickets))
        
        
    # Pay for Parking
    
    def payForParking(self):
        clear_output()
        ticketPaid = self.takenSpots.pop()
        self.availableTickets.append(ticketPaid)
        ticketTaken = self.availableTickets.pop()
        self.takenSpots.append(ticketTaken)
        print("Your spot/ticket number is " + str(ticketTaken))
        input("Press any button to pay...")
        print("Thank You, have a nice day! You have 15 minutes to leave the garage.")
        print("Garage Spots Remaining: " + str(self.availableTickets))
                
    # Leave Garage
    
    def leaveGarage(self):
        response3 = input("Has your ticket been paid? ")
        if response3.lower() == 'yes':
            print("Thank You, have a nice day!")
        else:
            self.payForParking()
        ticketPaid = self.takenSpots.pop()
        self.availableTickets.append(ticketPaid)
        print("Garage Spots Remaining: " + str(self.availableTickets))
            
        
    # METHODS END HERE
    
    # FUNCTION STARTS HERE
        
def run():
    clear_output()
    pg1 = parkingGarage([])
    while True:
        response2 = input("Welcome to The Parking Center! Would you like to Pay, Park or Leave? Type 'Quit' to shut system down. ")
            
        if response2.lower() == 'park':
            pg1.takeTicket()
            
        if response2.lower() == 'pay':
            pg1.payForParking()
            
        if response2.lower() == 'leave':
            pg1.leaveGarage()
            
        if response2.lower() == 'quit':
            break   
            
run()
