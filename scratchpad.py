"""

class experiment:
    def __init__(self, day, date):
        self.day = day
        self.date = date

    def output(self):
        prompt = ("today is {} the {}".format(self.day,self.date))
        print (prompt)
z = experiment("monday", "23")
z.output()
"""
class foo:
    def __init__(self, time, day, date):
        self.time = time
        self.day = day
        self.date = date

    def thing(self):
        output = ()
        input("time is: ", self.time)
        input("day is: ", self.day)
        input("date is: ", self.date)
        #print (output)

foo.thing("empty", "empty", "empty")

#working on implementing classes