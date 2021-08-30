import re


class Division:

    def __init__(self, num):
        self.num = num

    @classmethod
    def division_zero(cls, param):

        nums = re.findall(r'\d+', param)
        num = [int(i) for i in nums]
        try:
            res = num[0] / num[1]
            print(res)
        except ZeroDivisionError:
            print(f"На ноль не делится{num}")


list = ['1 / 2', '2 / 0', '0 / 7', '16/5']

for i in list:
    Division.division_zero(i)