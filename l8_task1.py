class Data:
    date_str = ''
    day = ''
    month = ''
    year = ''

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def get_date(cls, self):
        self.day, self.month, self.year = self.date_str.split('-')
        self.day = int(self.day) if self.day.isdigit() else 0
        self.month = int(self.month) if self.month.isdigit() else 0
        self.year = int(self.year) if self.year.isdigit() else 0

    @staticmethod
    def validate(day, month, year):
        if day in range(1, 31) and month in range(1, 12) and year in range(1900, 2200):
            return 'Date Valid'
        else:
            return 'Date Invalid'


d = Data('30-01-2021')
d.get_date(d)
print(d.validate(d.day, d.month, d.year))
