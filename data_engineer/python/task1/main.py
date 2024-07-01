class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'open'

    def add_item(self, name: str, quantity: int, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class Payment:

    def __init__(self):
        self.Order = None
        self.security_code = None
        self.payment_type = None

    def create(self, order: Order, payment_type: str, security_code: str):
        self.Order = order
        self.security_code = security_code
        self.payment_type = payment_type

    def pay(self):
        if self.payment_type == 'debit':
            self.debit_payment()
        elif self.payment_type == 'credit':
            self.credit_payment()
        elif self.payment_type == 'bank':
            self.bank_payment()
        else:
            raise Exception(f'Неизвестный тип платежа: {self.payment_type}')

        return self.Order

    def debit_payment(self):
        print('Какая-то логика реализации debit...')
        print(f'Верифицируем код: {self.security_code}')
        self.Order.status = 'paid'

    def credit_payment(self):
        print('Какая-то логика реализации credit...')
        print(f'Верифицируем код: {self.security_code}')
        self.Order.status = 'paid'

    def bank_payment(self):
        print('Какая-то логика реализации bank...')
        print(f'Верифицируем код: {self.security_code}')
        self.Order.status = 'paid'


def main() -> None:
    order = Order()
    order.add_item('Keyboard', 1, 50)
    order.add_item('SSD', 1, 150)
    order.add_item('USB cable', 2, 5)
    print(order.total_price())
    payment = Payment()
    payment.create(order, 'bank', '0372846')
    payment.pay()


if __name__ == "__main__":
    main()

