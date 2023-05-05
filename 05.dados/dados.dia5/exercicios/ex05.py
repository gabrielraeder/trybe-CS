from stackLL import Stack


class ParkingLot:
    def __init__(self) -> None:
        self.row = Stack()

    def add_vehicle(self, car):
        self.row.push(car)

    def remove_last(self):
        return self.row.pop()

    def get_vehicle_by_customer(self, car):
        vehicles = []
        for _ in range(self.row.size()):
            last_car_in_row = self.row.pop()
            if last_car_in_row.value != car:
                vehicles.append(last_car_in_row)
            else:
                customer_car = last_car_in_row
                break
        for car in vehicles[::-1]:
            self.row.push(car.value)
        return customer_car

    def __str__(self):
        return self.row.__str__()


if __name__ == "__main__":
    parkingLot = ParkingLot()
    cars = ["Golf", "Kicks", "Etios", "Corolla", "Marea", "Jeep"]
    for car in cars:
        parkingLot.add_vehicle(car)

    print(parkingLot)
    print("=" * 50)
    print(parkingLot.get_vehicle_by_customer("Corolla"))
    print("=" * 50)
    print(parkingLot)
