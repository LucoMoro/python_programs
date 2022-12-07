#from ecommerce.customer import contact
#from ..customer import contact


def calc_tax():
    print("calc_tax")

def calc_shipping():
    print("calc_shipping")

#the statement will be executed only once
if __name__ == "__main__":
    print("Sales started")
    calc_tax()
else:
    print("Sales initialized")