import datetime


class LocaleService:
    def __init__(self):
        return


    def get_todays_date(self):
        """

        return: sting of today's date in speakable format
        """
        mylist = []
        today = datetime.date.today()
        mylist.append(today)
        return today.strftime('Today is, %B, %d, %Y')


    def get_time(self):
        """

        :return: string of the time in readable format
        """
        return self.get_todays_date(self)