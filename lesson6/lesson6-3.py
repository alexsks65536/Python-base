from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:

        #if len(users.readlines()) > len(hobby.readlines()):
            with open("new_dict.json", "w", encoding="utf-8") as s:
                result = zip_longest((" ".join(user_s.split(",")) for user_s in users), hobby, fillvalue=None)
                new_dict = {str(x[0]).strip(): (x[1].strip()) for x in result}

                dump(result, s, ensure_ascii=False, indent=4)
            print(new_dict)
        #else:
            #exit(1)
