MELON_COST = 1.00   # define cost of one melon

# new customer information:
customer1_name = "Joe"      
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

# new customer calculations:
def check_payment(customer_name, num_melons, amount_paid):
    """ take new customor info and print report if they underpaid """
    expected_payment = num_melons * MELON_COST
    if expected_payment != amount_paid:
        print(f'{customer_name} paid ${amount_paid:.2f},',
        f'expected ${expected_payment:.2f}')

check_payment(customer1_name,customer1_melons,customer1_paid)
check_payment(customer2_name,customer2_melons,customer2_paid)
check_payment(customer3_name,customer3_melons,customer3_paid)
check_payment(customer4_name,customer4_melons,customer4_paid)
check_payment(customer5_name,customer5_melons,customer5_paid)
check_payment(customer6_name,customer6_melons,customer6_paid)

