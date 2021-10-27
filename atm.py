class Atm(object):





    def __init__(self, ATMCN, pinNumber):
        self.Atmcn = ATMCN
        self.pinNumber = pinNumber

    def pinNumber():
        print('Pin number is correct')
    def cashWithdrawl():
        print('Cash is Withdrawing')
    def balanceEnquiry():
        print('Balance is here')

sbi = Atm('1234', '2345')
print('The atm card number is : {}'.format(sbi.Atmcn))
print('The pin number is : {}'.format(sbi.pinNumber))