from datetime import datetime as dt, date
import calendar as cal
import os


class Month:
    def __init__(self, month_number):
        self.month = month_number

    def first_day_decimal(self):
        month = self.month_number
        date_today = dt.now()
        date = date_today.replace(month=month, day=1)
        return date.day

    def last_day_decimal(self):  # to determine the last day of the month
        month = self.month
        current_date = date.today()
        current_month_array = cal.monthcalendar(
            year=current_date.year, month=month)
        largest_number = 0
        for entry in current_month_array:
            for x in entry:
                if x > largest_number:
                    largest_number = x
        return largest_number


class January(Month):
    def __init__(self, month_number=1):
        super().__init__(month_number=1)


date_today = dt.now()
current_date = date.today()
current_month_array = cal.monthcalendar(
    year=current_date.year, month=current_date.month)
shifts = []


def today_decimal():
    return int(date_today.strftime("%d"))


def month_day(day):
    return date_today.replace(day=day)


def shifts_month():
    month = January
    for x in range(month.first_day(), today_decimal() + 1):
        x = month_day(x).strftime("%A %d, %B %Y")
        if "Monday" in x or "Tuesday" in x or "Wednesday" in x or "Friday" in x or "Saturday" in x:
            shifts.append(x)
    return shifts


def current_distance_delivery():
    os.system("cls")
    total_distance = 0
    total_deliveries = 0
    for x in shifts_month():
        daily_distance = float(
            input("How much did you ride on {}: ".format(x)))
        daily_delivery = float(
            input("How many delivers did you had on {}: ".format(x)))
        total_distance = daily_distance + total_distance
        total_deliveries = daily_delivery + total_deliveries
    return ("You have driven until {} {}km and had delivered {} orders".format(date_today.strftime("%A %d, %B %Y"), total_distance, int(total_deliveries)))


September = Month(9)
print(month.last_day_decimal())
