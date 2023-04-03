from abc import ABC, abstractmethod


class SystemAccess(ABC):
    @abstractmethod
    def __init__(self, can_access=False):
        pass

    def set_permission(self, can_access):
        pass


class SupportSystemAccess(SystemAccess):
    def __init__(self, can_access=False):
        self.name = "Support"
        self.set_permission(can_access)

    def set_permission(self, can_access):
        self.can_access = can_access


class FinanceSystemAccess(SystemAccess):
    def __init__(self, can_access=False):
        self.name = "Finance"
        self.set_permission(can_access)

    def set_permission(self, can_access):
        self.can_access = can_access


class SalesSystemAccess(SystemAccess):
    def __init__(self, can_access=False):
        self.name = "Sales"
        self.set_permission(can_access)

    def set_permission(self, can_access):
        self.can_access = can_access


class Account(ABC):
    def __init__(self, username):
        self.username = username
        self.permissions = []
        self.create_account()

    @abstractmethod
    def create_account():
        pass

    def show_permissions(self):
        permissions_names = [
            permission.name
            for permission in self.permissions
            if permission.can_access
        ]
        return permissions_names

    def add_permissions(self, permission, access=False):
        permission.set_permission(access)
        self.permissions.append(permission)


class ManagerAccount(Account):
    def create_account(self):
        self.add_permissions(SupportSystemAccess(), True)
        self.add_permissions(FinanceSystemAccess(), True)
        self.add_permissions(SalesSystemAccess(), True)


class SupportAccount(Account):
    def create_account(self):
        self.add_permissions(SupportSystemAccess(), True)


class SupportAndSalesAccount(Account):
    def create_account(self):
        self.add_permissions(SupportSystemAccess(), True)
        self.add_permissions(SalesSystemAccess(), True)


if __name__ == "__main__":
    manager = ManagerAccount("Manager")
    print(manager.show_permissions())

    support = SupportAccount("Support")
    print(support.show_permissions())

    sales = SupportAndSalesAccount("Sales")
    print(sales.show_permissions())
