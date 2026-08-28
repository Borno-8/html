class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye Color:", self.eye_color)
        print("Height (cm):", self.height_cm)

class kid(FamilyMember):

    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)

    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()

    def fovourite_hobby(self, hobby):
        print(self.name, "loves", hobby)

#(Afton, we want to ask, what is this new model?)

child = kid("Little Timmy", 1, "navy blu", 2)

child.show_traits()
child.fovourite_hobby("painting")

print("Is this kid a subcalss of Family number?", issubclass(kid, FamilyMember))