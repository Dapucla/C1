from constructor import GuestData

guest_1 = GuestData(name="Иван Петров", location="г. Москва", status="Наставник")
guest_2 = GuestData(name="Даниил Алексеев", location="г. Ставрополь", status="Программист")
guest_3 = GuestData(name="Сунгур Гасанов", location="г. Иваново", status="Предприниматель")

guests = [guest_1, guest_2, guest_3]
for guest in guests:
    print(guest.get_guest())
