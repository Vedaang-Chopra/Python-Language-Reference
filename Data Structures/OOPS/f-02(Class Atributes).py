 #  Class Atrributes: Set of variables holding data.
        #  They always lie within the class, so can only be reffered from class or object. They are variables but only for classes
        #  There are two types, class and object atrributes.
       
class Expense_Tracker:
    #  Docstring: - Description of class
    '''
    This is a class to do Expense Tracking

    '''
    #  Class Attribute.......................
    expense_tracker_version=0.1
    #  This/Self keyword is reference to current instance to the class. 
    def __init__(this,tracker_category,opening_balance,budget) -> None:
        # Object Atrributes..........
        this.tracker_category=tracker_category
        this.opening_balance=opening_balance
        this.budget=budget


#  Creating an object, from class
Home_Tracker=Expense_Tracker('home',3000, 5000)
print(Home_Tracker.tracker_category)
Shopping_Tracker_Debit =Expense_Tracker('shopping', 1000,10000)
print(Shopping_Tracker_Debit.tracker_category)

#  Some of the inbuilt functions for classes and objects...............
print(Home_Tracker.__dict__)
#  Dict Returns the values of all attributes for that object.
