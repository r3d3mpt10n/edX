import math

def creditCard(balance, monthlyPaymentRate, annualInterestRate):
    i = 1
    total = 0
    while i <= 12:
        payment = balance*monthlyPaymentRate
        unpaidBalance = balance - payment
        balance = (unpaidBalance + (annualInterestRate/12.0) * unpaidBalance)
        print("Month: %d \nMinimum monthly payment = %.2f \nRemaining Balance = %.2f \n " % (i, payment, balance))
        total += payment
        i += 1
    print("Total paid: %.2f" % (total))
    print("Remaining balance: %.2f" % (balance))


def lowestPayment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12
    lowerBound = balance / 12
    upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12
    originalBalance = balance
    lowestBalance = 0.01


    while abs(balance) > lowestBalance:

        balance = originalBalance
        payment = (upperBound - lowerBound) / 2 + lowerBound

        for month in range(12):
            balance -= payment
            balance *= 1 + monthlyInterestRate


        if balance > 0:
            lowerBound = payment
        else:
            upperBound = payment
    #payment = math.ceil(payment / 10.0) * 10
    print ("Lowest Payment: %.2f" % payment)

def main():
    balance = 320000
    unpaidBalance = 5000
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.02
    #creditCard(balance, monthlyPaymentRate, annualInterestRate)
    lowestPayment(balance, annualInterestRate)

main()





