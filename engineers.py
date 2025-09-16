class Engineer:
    def __init__(self, name, field, years_experience):
        self.name = name
        self.field = field
        self.years_experience = years_experience
        self.coffee_level = 100  # out of 100

    def work_on_project(self, project):
        if self.coffee_level < 20:
            print(f"{self.name} is too tired to work on {project}. Needs more coffee!")
        else:
            print(f"{self.name} is working on {project} in the field of {self.field}.")
            self.coffee_level -= 20

    def attend_meeting(self, topic):
        print(f"{self.name} is attending a meeting about {topic}.")
        self.coffee_level -= 10

    def take_break(self):
        print(f"{self.name} is taking a break and refilling coffee.")
        self.coffee_level = 100

    def __str__(self):
        return f"{self.name}, {self.field} Engineer, {self.years_experience} years exp"

# Inheritance example
class SoftwareEngineer(Engineer):
    def __init__(self, name, years_experience, favorite_language="Python"):
        super().__init__(name, "Software", years_experience)
        self.favorite_language = favorite_language

    def work_on_project(self, project):
        print(f"{self.name} is coding {project} using {self.favorite_language}.")
        self.coffee_level -= 25

    def debug_code(self):
        print(f"{self.name} is debugging code...")

# Example usage
if __name__ == "__main__": 
    eng = Engineer("Tosin", "Civil", 5)
    eng.work_on_project("Bridge Design")
    eng.take_break()
    print(eng)

    soft_eng = SoftwareEngineer("Uche", 3)
    soft_eng.work_on_project("Mobile App")
    soft_eng.debug_code()
    print(soft_eng)