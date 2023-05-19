#  CIS 115 - Project 1 / Mid-term - Highway Robbery!
# This program will prepare an automible liability insurance estimate for customers based upon age and amount of violations.
# Global variable to be used for storing the name of the customer.
name=input('Please enter your name:')

# Global variables to be used for calculations of prices.
age=float(input('Please enter your age:'))
if age>105 or age<16:
    print('Invalid Input, please retry and enter a valid driver age between 16 and 105.'), quit()
    

    

# The main function gets the amount of traffic violations as an integer value
# and calls the show_price function to be later used in pricing.
def main():
    # Gets number of traffic violations.
    tickets=int(input('Please enter the amount of previous traffic violations that you have incurred:'))

    if tickets<0: 
        print('You have entered a non-positive value for the amount of tickets, please retry and enter a value that is positive.'), quit()
    
    # Calls the show_price function with the parameter variable being the amount of violations.
    get_riskcode(tickets)
# The get_risk function converts the amount of tickets or violations 
# the customer has gotten into a risk level which is based upon the table given in the stipuolations.
def get_riskcode(tickets):
    if tickets==0:
        risk_Code=4
    elif tickets==1:
        risk_Code=3 
    elif 2<=tickets<=3:
        risk_Code=2
    elif tickets>=4:
        risk_Code=1
    # calls the get_risktype function to calculate the risk type the driver is based upon risk code.
    get_risktype(tickets, risk_Code)

# The get_risktype functions converts the risk_Code into the type of risk the customer is based upon if statments.
def get_risktype(tickets, risk_Code):
    if risk_Code==1:
        risk_Type='High'
    elif risk_Code==2:
        risk_Type='Moderate'
    elif risk_Code==3:
        risk_Type='Low'
    else:
        risk_Type='No'
    # Calls the get_price function.
    get_price(tickets, risk_Code, risk_Type)


# The get_price function calculates a price based upon amount of tickets and age of customer, keeping the values tickets and risk_Code.)
def get_price(tickets, risk_Code, risk_Type):
    # Calculates the price using the amount of tickets and the global var age.
    if age>=25 and tickets==0:
        price=275.00
    elif age<25 and tickets==0:
        price=325.00
    elif age>=25 and tickets==1:
        price=315.00
    elif age<25 and tickets==1:
        price=380.00
    elif age>=25 and tickets==2:
        price=365.00
    elif age<25 and tickets==2:
        price=405.00
    elif age>=25 and tickets==3:
        price=390.00
    elif age<25 and tickets==3:
        price=450.00
    elif age>=25 and tickets>=4:
        price=410.00
    elif age<25 and tickets>=4:
        price=480.00
    # Calls the show_output function, with price, and risk_Type parameters.)
    show_output(price, risk_Type)
    
# Calls the show_output function which will show the user their liability insurance estimate.
def show_output(price, risk_Type):
    # Shows the user their risk code and price.
    print(name ,',' ,  'as a' , risk_Type , 'risk driver' ', your insurance will cost you' , format(price, '.2f') ,'$.')
    

# Calls the main() function and executes it.
main()
