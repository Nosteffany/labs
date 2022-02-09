from pprint import pprint


def func1(string,spl):
    for i in string.split(spl):
        print(i)


def pull(string):
    return float(s[s.find(' ')+1::].replace(',','.'))


def func3():
    while True:
        x = input("write a sequence or press Enter to quit: ")
        if x:
            print('_'.join(i for i in x))
        else:
            break
print("Завдання1")
func1('C:/Users/me/Documents','/')
print("\nЗавдання2")
s = 'X-DSPAM-Confidence: 0,8475'
print(pull(s))
print("\nЗавдання3")
func3()
