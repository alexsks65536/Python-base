import re


class Date:

    def __init__(self, dat):
        self.dat = dat

    @classmethod
    def get_data(cls, param):

        nums = re.findall(r'\d+', param)
        date_num = [int(i) for i in nums]
        Date.do_valid_data(date_num)

    @staticmethod
    def do_valid_data(date):

        d, m, y = date[0], date[1], date[2]
        if (0 < d <= 31) and (0 < m <= 12) and (0 < y <= 9999):
            print(f"0{d}, 0{m}, {y}")
        else:
            print(f"Неверная дата: {date}")


Date.get_data('01-01-1970')