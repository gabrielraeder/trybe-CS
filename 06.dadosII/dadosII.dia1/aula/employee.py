class Employee:
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name

    def __str__(self):
        return f"ID: {self.id_num}, NAME: {self.name};"


class HashMap:
    def __init__(self):
        self._buckets = [None for i in range(10)]

    def get_address(self, id_num):
        return id_num % 10

    def insert(self, employee):
        address = self.get_address(employee.id_num)
        self._buckets[address] = employee

    def get_value(self, id_num):
        address = self.get_address(id_num)
        return self._buckets[address].name

    def has(self, id_num):
        address = self.get_address(id_num)
        return self._buckets[address] is not None

    def update_value(self, id_num, new_name):
        address = self.get_address(id_num)
        self._buckets[address].name = new_name
        return self._buckets[address].name


if __name__ == "__main__":
    employees = [(14, "name1"), (23, "name2"), (10, "name3"), (9, "name4")]
    hashMap = HashMap()
    for employee in employees:
        employees_instance = Employee(*employee)
        hashMap.insert(employees_instance)

    # find_23 = hashMap.get_value(23)
    # print(find_23)

    find_10 = hashMap.get_value(10)
    print(find_10)

    update_10 = hashMap.update_value(10, "name30")
    print(update_10)
