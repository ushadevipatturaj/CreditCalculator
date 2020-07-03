import math


class CreditCalculation:

    def calculate_payment(self, principal, period, interest):
        annuity_payment = principal * ((interest * (pow((1 + interest), period))) / (pow((1 + interest), period) - 1))
        print(math.ceil(annuity_payment))

    def calculate_months(self, principal, amount, interest):
        month = 0
        year = 0
        base = 1 + interest
        log_value = amount / (amount - (interest * principal))
        period = math.log(log_value, base)
        if math.ceil(period) > 12:
            year += math.ceil(period) // 12
            month += math.ceil(period) % 12
            print("You need {0} years and {1} months to repay this credit!".format(year, month))
        elif math.ceil(period) == 12:
            print("You need 1 year to repay this credit!")
        else:
            print("You need {0} months to repay this credit!".format(math.ceil(period) % 12))
    def calculate_credit_pricipal(self, payment, period, interest):
        divider = (interest * pow((1 + interest) , period)) / ((pow((1 + interest) , period)) - 1)
        credit_principal = payment / divider
        print("Your credit principal =",round(credit_principal))


cc = CreditCalculation()
print('What do you want to calculate?\n' +
      'type "n" - for count of months\n' +
      'type "a" - for annuity monthly payment\n' +
      'type "p" - for credit principal:')
choice = input()
if choice == 'a':
    print("Enter credit principal:")
    principal = int(input())
    print("Enter count of periods:")
    period = int(input())
    print("Enter credit interest:")
    interest = float(input())
    cc.calculate_payment(principal, period, interest / 1200)
elif choice == 'n':
    print("Enter credit principal:")
    principal = int(input())
    print("Enter monthly payment:")
    payment = int(input())
    print("Enter credit interest:")
    interest = float(input())
    cc.calculate_months(principal, payment, interest / 1200)
elif choice == 'p':
    print("Enter monthly payment:")
    payment = float(input())
    print("Enter count of periods:")
    period = int(input())
    print("Enter credit interest:")
    interest = float(input())
    cc.calculate_credit_pricipal(payment, period, interest / 1200)
