class PetShop:
    def __init__(self, name, pets, total_cash):
        self.name = name
        self.pets = pets
        self.total_cash = total_cash
        self.pets_sold = 0

    def stock_count(self):
        return len(self.pets)

    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self, amount):
        self.total_cash += amount

    def add_pet(self, new_pet):
        self.pets.append(new_pet)

    def remove_pet(self, pet_removed):
        self.pets.remove(pet_removed)

    def find_pet_by_name(self, pet_name):
        for pet in self.pets:
            if pet.name == pet_name:
              return pet

    def sell_pet_to_customer(self, name_of_pet, customer):
        pet_to_buy = self.find_pet_by_name(name_of_pet)
        self.remove_pet(pet_to_buy)
        customer.add_pet(pet_to_buy) #refering customer class
        self.increase_pets_sold()
        self.increase_total_cash(pet_to_buy.price)
