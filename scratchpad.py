"""

class experiment:
    def __init__(self, day, month):
        self.day = day
        self.month = month

    def output(self):
        prompt = ("today is {} the {}".format(self.day,self.month))
        print (prompt)
z = experiment("monday", "23")
z.output()
"""

class foo:
    def __init__(self, time, day, month):
        self.time = time
        self.day = day
        self.month = month


    def testing(self):
        #f"time is {self.time}, day is {self.day}, month is {self.month}"
        prompt = ("prompt time is {}, prompt day is {}, prompt month is {}".format(self.time, self.day, self.month))
        name = input ("name = ")
        print (prompt)
        print (f"name was {name}")

    def thing(self):
        self.time = input("time is: ")
        self.day = input("day is: ")
        self.month = input("month is: ")
        print (f"\ninput time was {self.time},\ninput day was {self.day},\ninput month was {self.month}\n")

bar = foo("testtime", "testday", "testmonth")
#bar.testing()
bar.thing()
#working on implementing classes
