# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.8
# oop设计实例


class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary = self.salary + self.salary * percent

    def work(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return '[Employee: name={0}, salary={1}]'.format(self.name, self.salary)


class Chef(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)

    def work(self):
        print(self.name, "makes food")


class Server(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)

    def work(self):
        print(self.name, 'interfaces with customer')


class PizzaRobot(Chef):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print(self.name, "makes pizza")


if __name__ == '__main__':
    bob = PizzaRobot('Bob')
    print(bob)
    bob.work()
    bob.give_raise(0.2)
    print(bob)
    print()
