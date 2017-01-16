def filter(a):
    import re
    if bool (re.match(r'([A-Za-z])', a)) == True:
        print("1. - True")
    else:
        print("1. - False")
    if bool(re.findall(r"([^A-Za-z0-9.-])",a))== True:
        print("2. - True")
    else:
        print("2. - False")
    if bool (re.findall(r"\w",a[-1]))== True:
        print("3. - True")
    else:
        print("3. - False")
    if len(min(a)) == 1:
        print("4. - True")
    else:
        print("4. - False")
    if len(a) == 20:
        print("5. - True")
    else:
        print("5. - False")

filter('Hello world')
