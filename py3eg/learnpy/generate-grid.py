import random

def main():
    while True:
        try:
            rows = get_integer('rows: ')
            columns = get_integer('columns: ')
            minimum = get_integer('minimum (or Enter for 0): ', 0)
            maximum = get_integer('maximum (or Enter for 1000): ', 1000)
            for row in range(rows):
                for column in range(columns):
                    print(random.randint(minimum, maximum),
                          end = '   ')
                print('\n')
            break
        except ValueError as err:
            print(err)
        except TypeError as err:
            print(err)
    
def get_integer(msg, default = None):
    while True:
        try:
            number = int(input(msg))
            return number
        except ValueError:
            if default is not None:
                return default
            else:
                print('invalid' + name + 'has entered')
main()
