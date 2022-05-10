def SwitchExample(argument):
    switcher = {
        0: " This is case Zero ",
        1: " This Case One ",
        2: " This is Case two ",
    }
    return switcher.get(argument, "nothing")
if __name__ == "__main__":
    argument = 2
    print(SwitchExample(argument))


