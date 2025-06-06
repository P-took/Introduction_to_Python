from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "30")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="RA123456789RU"
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"г.{mailing.from_address.city}, ул.{mailing.from_address.street} "
      f"{mailing.from_address.house}, кв.{mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, г.{mailing.to_address.city}, "
      f"ул.{mailing.to_address.street} {mailing.to_address.house}, "
      f"кв.{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
