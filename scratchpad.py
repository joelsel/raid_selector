class experiment:
    def __init__(self, day, date):
        self.day = day
        self.date = date

    def output(self):
        prompt = ("today is {} the {}".format(self.day,self.date))
        print (prompt)
z = experiment("monday", "23")
z.output()
