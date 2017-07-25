class Hotel:
    rate=50
    tax=0.85
    sub=rate+rate * tax
    totday1=sub
    def __init__(self,days):
        self.days=days
        cal=self.days*Hotel.totday1
        print('Total no of days:',self.days)
        print('Sales Tax:',Hotel.tax)
        print('Rate per day:',Hotel.rate)
        print('Total amount for days of stays is:',cal)
        
inn=Hotel(50)

        
