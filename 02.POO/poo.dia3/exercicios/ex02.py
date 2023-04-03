from abc import ABC, abstractmethod


class Alarme:
    def __init__(self):
        self.__tasks: list(Task) = []

    def add_task(self, task):
        self.__tasks.append(task)

    def run_tasks(self):
        for task in self.__tasks:
            task.trigger()

    def despertar(self):
        self.run_tasks()


class Task(ABC):
    @abstractmethod
    def trigger(self):
        pass


class AcenderLuz(Task):
    def __init__(self, alarme):
        self.alarme: Alarme = alarme
        self.alarme.add_task(self)

    def trigger(self):
        print("Luzes acesas!")


class FazerCafe(Task):
    def __init__(self, alarme):
        self.alarme: Alarme = alarme
        self.alarme.add_task(self)

    def trigger(self):
        print("Fazendo Café!")


class LigarPC(Task):
    def __init__(self, alarme):
        self.alarme: Alarme = alarme
        self.alarme.add_task(self)

    def trigger(self):
        print("Ligando Computador!")


if __name__ == "__main__":
    alarme = Alarme()
    AcenderLuz(alarme)
    FazerCafe(alarme)
    LigarPC(alarme)

    alarme.despertar()
