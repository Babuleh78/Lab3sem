from abc import ABC, abstractmethod
#State
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

class Outside(State):
    def handle(self):
        return "Студент не в ВУЗе"

class Inside(State):
    def handle(self):
        return "Студент учится"

class Walk(State):
    def handle(self):
        return "Студент в пути"

class Window(State):
    def handle(self):
        return "Студент в ВУЗе, но сейчас у него окно"

class Student:
    def __init__(self):
        self.state = Outside()  

    def set_state(self, state: State):
        self.state = state

    def where(self):
        return self.state.handle()

me = Student()
print(me.where())
me.set_state(Inside())
print(me.where())
me.set_state(Window())
print(me.where())
me.set_state(Outside())
print(me.where())
me.set_state(Walk())
print(me.where())
