import math
import sys
import argparse


def calculate_months(principal, amount, interest):
    month = 0
    year = 0
    base = 1 + interest
    overpayment = 0
    log_value = amount / (amount - (interest * principal))
    period = math.log(log_value, base)
    if math.ceil(period) > 12:
        year += math.ceil(period) // 12
        month += math.ceil(period) % 12
        overpayment = (amount * math.ceil(period)) - principal
        if month == 0:
            print("You need {0} years to repay this credit!".format(year))
            print("Overpayment = {}".format(int(overpayment)))
        else:
            print("You need {0} years and {1} months to repay this credit!".format(year, month))
            print("Overpayment = {}".format(int(overpayment)))
    elif math.ceil(period) == 12:
        print("You need 1 year to repay this credit!")
        overpayment = (amount * math.ceil(period)) - principal
        print("Overpayment = {}".format(int(overpayment)))
    else:
        print("You need {0} months to repay this credit!".format(math.ceil(period) % 12))
        overpayment = (amount * math.ceil(period)) - principal
        print("Overpayment = {}".format(int(overpayment)))

def calculate_payment(payment, period, interest):
    divider = (interest * pow((1 + interest), period)) / ((pow((1 + interest), period)) - 1)
    credit_principal = payment / divider
    print("Your credit principal ={}!".format(math.floor(credit_principal)))
    over_payment = (payment * period) - math.floor(credit_principal)
    print("Overpayment = {}".format(int(over_payment)))


def calculate_payment_with_principal(principal, period, interest):
    annuity_payment = principal * ((interest * (pow((1 + interest), period))) / (pow((1 + interest), period) - 1))
    print("Your credit principal ={}!".format(math.ceil(annuity_payment)))
    over_payment = (math.ceil(annuity_payment) * period) - principal
    print("Overpayment = {}".format(int(over_payment)))


def calculate_differentiated_payments(principal, periods, interest):
    overpayment = 0
    totalpayment = 0
    for m in range(1, periods + 1):
        p_n = principal / periods
        exp = principal - ((principal * (m - 1)) / periods)
        diff_payment = math.ceil(p_n + (interest * exp))
        print("Month {0}: paid out {1}".format(m, diff_payment))
        totalpayment = totalpayment + diff_payment
    overpayment = totalpayment - principal
    print("Overpayment = {}".format(int(overpayment)))


args = sys.argv
# print(args)
parser = argparse.ArgumentParser(description='testing argparse')
parser.add_argument("--type", help="test", required=True)
parser.add_argument("--principal", help="principal amount", required=False)
parser.add_argument("--payment", help="payment", required=False)
parser.add_argument("--periods", help="periods")
parser.add_argument("--interest", help="interest")
args_parse = parser.parse_args()

if args_parse.type == 'diff':
    if (len(args) == 5 and args_parse.principal is not None and args_parse.periods is not None and
            args_parse.interest is not None):
        calculate_differentiated_payments(float(args_parse.principal), int(args_parse.periods),
                                          float(args_parse.interest) / 1200)
    else:
        print("Incorrect parameters")
elif args_parse.type == 'annuity':
    if (len(args) == 5 and args_parse.periods is not None and args_parse.payment is not None and
            args_parse.interest is not None):
        calculate_payment(float(args_parse.payment), int(args_parse.periods),
                          float(args_parse.interest) / 1200)
    elif (len(args) == 5 and args_parse.principal is not None and args_parse.periods is not None and
          args_parse.interest is not None):
        calculate_payment_with_principal(float(args_parse.principal), int(args_parse.periods),
                                         float(args_parse.interest) / 1200)
    elif (len(args) == 5 and args_parse.principal is not None and args_parse.payment is not None and
          args_parse.interest is not None):
        calculate_months(float(args_parse.principal), float(args_parse.payment), float(args_parse.interest) / 1200)
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
