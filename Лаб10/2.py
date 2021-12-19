import datetime


def get_today_date():
    return datetime.date(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day)


class Wanderer:
    def __init__(self, name, surname, job, date: datetime.date):
        self.name = name
        self.surname = surname
        self.job = job
        self.date = date


class Address:
    def __init__(self, country, region, city, street, date: datetime.date, term, info: Wanderer):
        self.country = country
        self.region = region
        self.city = city
        self.street = street
        self.date = date
        self.term = datetime.date(self.date.year, self.date.month, self.date.day + term)
        self.info = info

    def is_ended(self):
        return int(str(self.term - get_today_date())[:-13:]) < 0

    def days_left(self):
        return str(self.term - get_today_date())[:-9:]

    def __str__(self):
        return f'Заїзд: {self.date}, відїзд: {self.term}'


birth_date = datetime.date(2004, 6, 25)
date = datetime.date(2021, 12, 12)
Alexandra = Wanderer('Alexandra', 'Kovach', 'prostitute', birth_date)
a = Address('Ukraine', 'Transkarpatia', 'Kyiv', 'Shevchenko st.', date, 4, Alexandra)
print(a.is_ended())
print(a.days_left())
print(a)