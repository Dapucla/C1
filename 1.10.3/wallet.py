class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def client_balance(self):
        return "Клиент " + self.name + ". " + "Баланс: " + str(self.balance) + "руб."


client_1 = Client("Иван Петров", 50)

print(client_1.client_balance())