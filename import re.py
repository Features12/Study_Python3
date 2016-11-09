import re
a = "cat and dog play in game. Cat age is - 3 month, dog age is - 6 month."
composed = bool(re.findall(r"([^A-Za-z0-9.-])",a)) #любой символ в строке, кроме этих
print(composed)
