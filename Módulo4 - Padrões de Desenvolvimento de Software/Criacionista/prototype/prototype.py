import copy

class Prototype:
    def clone(self):
        # usa cópia profunda
        return copy.deepcopy(self)

class Person(Prototype):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, address={self.address})"

if __name__ == "__main__":
    original = Person("Alice", 30, {"city": "Salvador", "zip": "40000"})
    clone_person = original.clone()
    clone_person.name = "Bob"
    clone_person.address["city"] = "Vitória"
    print(original)       # Person(name=Alice, age=30, address={'city': 'Salvador', …})
    print(clone_person)   # Person(name=Bob, age=30, address={'city': 'Vitória', …})
