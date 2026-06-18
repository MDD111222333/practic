class Customer:
    def __init__(self, id, name, phone, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address

class Order:
    def __init__(self, id, customer_id, order_date, status, total):
        self.id = id
        self.customer_id = customer_id
        self.order_date = order_date
        self.status = status
        self.total = total
