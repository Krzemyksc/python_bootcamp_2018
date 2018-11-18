# import re
#
# # mail = re.compile("\d{2}-\d{3}")
# with open("dane/input.txt") as f:
#     data = f.read()
#     post_code = re.compile("\d{2}-\d{3}")
#     print(post_code.findall(data))


import re

post_code = re.compile("^\d{2}-\d{3} | \d{2}-\d{3} | \d{2}-\d{3}$") # $ - koniec napisu, ^ - początek linii
email_pattern = re.compile("[\w\.-]+@[\w\.]")
date_patter = re.compile("\d{2} \w{3} \d{4}")
with open("input.txt") as f:
    data = f.read()
    print(post_code.findall(data))
    print(email_pattern.findall((data)))
    print(date_patter.findall((data)))