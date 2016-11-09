def filter1(a):
    import re
    if bool(re.match(r'([A-Za-z])', a)) == True:
        print("1. - True")
        return True
    else:
        print("1. - False")
        return False


def filter2(a):
    import re
    if bool(re.findall(r"([^A-Za-z0-9.-])", a)) == True:
        print("2. - True")
        return True
    else:
        print("2. - False")
        return False


def filter3(a):
    import re
    if bool(re.findall(r"\w", a[-1])) == True:
        print("3. - True")
        return True
    else:
        print("3. - False")
        return False


def filter4(a):
    if len(min(a)) == 1:
        print("4. - True")
        return True
    else:
        print("4. - False")
        return False


def filter5(a):
    if len(a) == 20:
        print("5. - True")
        return True
    else:
        print("5. - False")
        return False


print(all([filter1(), filter2(), filter3(), filter3(), filter4(), filter5()]))