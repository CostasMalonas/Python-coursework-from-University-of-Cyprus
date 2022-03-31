def findPayment (loan, r, m):
    """ Assumes: 'loan' and 'r' are floats, 'm' an int
        Returns the monthly payment for a mortgage of size
        'loan' at a monthly rate of 'r' for 'm' months """
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))





class Mortgage (object):
    """ Abstract class for building different kinds of mortgages """

    def __init__(self, loan, annRate, months):
        """ Assumes: loan and annRate are floats, months an int 
            Creates a new mortgage of size loan, duration months, and annual rate annRate """
        # Here are three instance initial values
        self.loan = loan # loan (size of mortgage)
        self.rate = annRate / 12 # annual rate is 12 times of monthly rate
        self.months = months # The number of months
        
        # Here are two lists extended monthly
        self.paid = [0.0] # At the first day of loan you don't need to pay loan. Note this list is extended monthly
        self.outstanding = [loan] # the value of the loan remained to be paid at each month
        
        # Here is the monthly payment for a mortgage of size 'loan' at monthly rate of 'self.rate' for 'months' months
        self.payment = findPayment(loan, self.rate, months) # in payment variable we will store the result of the loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1)) operation
        self.legend = None  # description of certain kind of mortgage

    def makePayment (self):
        """ Make a monthly payment"""
        # Calculate monthly payments then append them to two lists:
        # monthly payments and monthly outstanding loan balance
        self.paid.append (self.payment) 
        # reduction used to reduce the loan balance = monthly payment - the amount of interest due on the outstanding loan balance
        reduction = self.payment - self.outstanding [-1] * self.rate 
        # We take the amount of the loan from the last month and we reduce it by the reduction value.
        # Then we append the remaining value of the loan to the outstanding list
        self.outstanding.append (self.outstanding [-1] - reduction) 

    def getTotalPaid (self):
        """ Return the total amount paid so far """
        return sum (self.paid) # Take the paid list of the object and sum up the payments

    def __str__(self):
        return self.legend # String representation of Mortgage object
    
    
    
    
    
    

    
class Fixed (Mortgage):
    """ A fixed-rate mortgage with no points. """
    
    def __init__(self, loan, r, months):
        """ No need to repeat the same specification of superclass? """
        Mortgage.__init__(self, loan, r, months) # We call the __init__ method of the parent class and we pass our attributes
        self.legend = 'Fixed, ' + str (round (r*100, 2)) + '%' # We use rount() function to round the number to 2 decimal points
        
        
        

class FixedWithPts (Mortgage):
    """ A fixed-rate mortgage with points. """
    def __init__(self, loan, r, months, pts):
        """
        loan: floats, size of mortgage
        r: floats without percentage symbol, annual rate
        months: int, total duration
        pts: float with percentage symbol,
            payment points of the initial loan
        return: a new instance of FixedWithPts of type Mortgage
        """
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts # points as service fee
        self.paid = [loan*(pts/100)] # Override Mortgage's paid attribute
            # Note that this part of payment is not used to reduce the /
            # outstanding of loan balance.
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%, ' + str(pts) + ' points'


class TwoRate (Mortgage):
    """ A mortgage with an initial teaser rate followed by a higher rate for the duration. """
    
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        """ Initiate with teaser rate and total months, and calculate monthly payment to the end
        loan: float, size of mortgage
        r: floats without percentage symbol, annual rate
        months: int, total duration
        teaserRate: float without percentage symbol,
            annual teaser rate in the teaser months
        teaserMonths: int, teaser duration
        :return an instance of TwoRate under super class of Mortgage
        """
        Mortgage.__init__(self, loan, teaserRate, months) 
        self.teaserMonths = teaserMonths # Months for the first rate
        self.teaserRate = teaserRate # first rate
        self.nextRate = r/12 # Next rate for each month
        self.legend = str(teaserRate*100)  + '% for ' + str(self.teaserMonths) + ' months, then ' + str(round(r*100, 2)) + '%'
                
    def makePayment (self):
        """
        When time is up, replace teaser rate with next rate, and
        calculate monthly payment again with new loan, new rate and
        new months.
        """
        if len(self.paid) == self.teaserMonths + 1:
           self.rate = self.nextRate
           self.payment = findPayment(self.outstanding[-1], self.rate, self.months - self.teaserMonths)
        Mortgage.makePayment(self) # Call the superclass method with instance itself
    
    
    
    
    
    
    
def compareMortgages (amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    """
    Print out three kinds of mortgages with their total payments
    amt: int, amount of loan size
    years: int, years of payment duration
    fixedRate: float without percent symbol, fixed annual rate
    pts: float with percent symbol, payment points of the initial loan
    ptsRate: float without percent symbol, fixed annual rate with points payment
    varRate1: float without percentage symbol, annual teaser rate in the teaser months
    varRate2: floats without percentage symbol, annual rate
    varMonths: int, months of teaser duration
    return: print out information of each kind of mortgage
    """
    totMonths = years*12 # Turn years to months
    fixed = Fixed(amt, fixedRate, totMonths) # Create a fixed mortgage Fixed object
    fixedwithpts = FixedWithPts(amt, ptsRate, totMonths, pts) # Create a FixedWithPts object
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths) # Create a TwoRate object
    # Create a list with all the objects of different mortgage type we created above
    morts = [fixed, fixedwithpts, twoRate] 
    
    # At the following loop for each month we take each mortgage object and we make a payment
    # of our loan. After we have paid our loan for each mortgage type, we print the string 
    # representation of mortages objects and we print the total amount paid for each mortgage
    # type
    for month in range (totMonths):
        for mort in morts:
            mort.makePayment ()
    for mort in morts:
        print(mort)
        print(' Total payments = $' + str(int(mort.getTotalPaid ())))

compareMortgages(amt=200000, years=30, fixedRate=0.07, pts = 3.25, ptsRate=0.05, varRate1=0.045,
                 varRate2=0.095, varMonths=48)

# For the above example we conclude that the fixed with points mortgage is the best type  
    
    
    
    
    
    
    
    
    
    