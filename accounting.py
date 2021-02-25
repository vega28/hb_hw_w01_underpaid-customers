MELON_COST = 1.00   # define cost of one melon

# new customer calculations:
def check_payment(customer_name, num_melons, amount_paid):
    """ take new customor info and print report if they underpaid """
    expected_payment = num_melons * MELON_COST
    if expected_payment != amount_paid:
        print(f'{customer_name} paid ${amount_paid:.2f},',
        f'expected ${expected_payment:.2f}')

# read in customer information and check payments for each customer:
def generate_payment_report(customer_order_file):
    the_file = open(customer_order_file)

    for line in the_file:
        line = line.rstrip()
        info = line.split('|')
        num, customer_name, num_melons, amount_paid = info
        check_payment(customer_name,int(num_melons),float(amount_paid))

# run the functions and print the report:
generate_payment_report('customer-orders.txt')