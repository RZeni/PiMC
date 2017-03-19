import unittest
import datetime

def get_todays_date():
    mylist = []
    today = datetime.date.today()
    mylist.append(today)
    return today.strftime('Today is, %B, %d, %Y')

class TestDate(unittest.TestCase):
    def testGetTodaysDate(self):
        print(get_todays_date())


if __name__ == '__main__':
    unittest.main()
