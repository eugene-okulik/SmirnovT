class Flower:
    def __init__(self, color, stem_length, price, lifespan):
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan  # Время жизни (дни) до увядания

    def describe(self):
        print(f"Цветок: {self.color}, "
              f"цена: {self.price}, "
              f"длина стебля: {self.stem_length}, "
              f"время жизни: {self.lifespan} дней")

class Rose(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__(color, stem_length, price, 10)  # Розы живут в среднем 10 дней

class Tulip(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__(color, stem_length, price, 7)  # Тюльпаны живут в среднем 7 дней

class Lily(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__(color, stem_length, price, 5)  # Лилии живут в среднем 5 дней


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifespan(self):
        # Возвращает среднее время до увядания букета
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        return total_lifespan / len(self.flowers) if self.flowers else 0

    def sort_flowers(self, parameter="price"):
        # Параметры сортировки: 'color', 'stem_length', 'price', 'lifespan'
        return sorted(self.flowers, key=lambda flower: getattr(flower, parameter))

    def find_flowers(self, **kwargs):
        # Поиск цветов в букете по заданным параметрам (например, lifespan=7)
        found = []
        for flower in self.flowers:
            if all(getattr(flower, key) == value for key, value in kwargs.items()):
                found.append(flower)
        return found


# Создание экземпляров цветков
rose = Rose("Красный", 40, 50)
tulip = Tulip("Желтый", 30, 20)
lily = Lily("Белый", 25, 30)

# Создание букета и добавление в него цветков
my_bouquet = Bouquet()
my_bouquet.add_flower(rose)
my_bouquet.add_flower(tulip)
my_bouquet.add_flower(lily)

# Вывод свойств букета
print(f"Общая стоимость букета: {my_bouquet.total_price()}")
print(f"Среднее время жизни букета: {my_bouquet.average_lifespan()} дней")

# Сортировка цветов в букете
sorted_by_price = my_bouquet.sort_flowers("price")
sorted_by_freshness = my_bouquet.sort_flowers("lifespan")

# Поиск цветов с определенным временем жизни (здесь: 7 дней)
flowers_with_lifespan = my_bouquet.find_flowers(lifespan=7)
for flower in flowers_with_lifespan:
    flower.describe()
