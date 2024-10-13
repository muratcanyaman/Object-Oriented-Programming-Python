import csv
class Item:
    # class level instance
    pay_rate = 0.8
    all = []

    def __init__(self ,name : str, price : float, quantity = 0):
        # We use assert in python for testing a condition.It returns error when condition is false.
        assert price >= 0, f"Price {price} is not greater than 0 or equal 0 !"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0 or equal 0 !"

        # instance level instances
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # we access class level instance
        Item.all.append(self)


    def calculate_total_price(self):
        return self.__price * self.quantity

    def discount_price(self):
        self.__price = self.__price * self.pay_rate
        return self.__price

    @classmethod
    # This function opens a csv file and converts each line to dictionary,then converts to a list contains dictionaries.
    def instantiate_from_csv(cls):
        '''
        This should also do something that has a relationship with the class ,but usually, those are used to
        manipulate different structures of data to instantiate objects,like we have done with CSV file.

        '''
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        # We create our instances from here now
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        '''
        This should do something that has a relationship with the class,but not something that must be unique per instance.
        '''
        if isinstance(num, float):
            return num.is_integer() # This is_integer() function is a built-in function in python.We don't call is_integer() method recursively here.
        elif isinstance(num, int):
            return True
        else:
            return False

    # Encapsulaiton
    # We can't set price attribute anymore.It provides security.
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def increment_price(self, increment_amount):
        self.__price += self.__price  + self.__price * increment_amount
    @property
    # Read-Only Decorator
    def name(self):
        return self.__name

    @name.setter
    # we can set read-only instance using setter
    def name(self, value):
        self.__name = value

    def __repr__(self):
        return f"Item('{self.name}', '{self.__price}', '{self.quantity}')"

    # Abstraction in Python is usually provided through abstract class and abstract method.
    # We define what some methods of a class do, but subclasses define how to do them.
    def __connect(self,server):
        pass
    def __prepare_body(self):
        return """
        Hello everybody.
        We have {self.name} {self.quantity} times 
        Regards,Murat.
        """
    def __send(self):
        pass

    def send_email(self):
        self.__connect(server='smtp.gmail.com:587')
        self.__prepare_body()
        self.__send()


#Inheritence
# We're inheriting attributes and methods of Item class.Now we can use these in Phone class.
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # we can access all methods and attributes in Item class.
        super().__init__(
                name, price, quantity
        )

        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than 0 or equal 0 !"

        self.broken_phones = broken_phones

# Polymorphism:We've just used increment_price() and apply_discount() methods for different objects.That's what polymorphism is.
# It allows the operation or method to behave differently on different objects.Generally we talk about inheritence and polymorphism together.

item1 = Item("Phone",650)
print(item1.name)
item1.increment_price(0.2)
item1.apply_discount()
print(item1.price)

item2 = Phone("A24", 1000)
print(item2.name)
item2.increment_price(0.3)
item2.apply_discount()
print(item2.price)
