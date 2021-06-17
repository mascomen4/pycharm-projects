import sys

Zero = ["  ***  "," *   * ","*     *","*     *","*     *"," *   * ","  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
try:
    if len(sys.argv) > 1:
        digits = sys.argv[1]
    else:
        digits = '1234567890'
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            x = digit[row]
            i = 0
            perform = ""
            while i < len(x):
                if x[i] == "*":
                    perform += str(number)
                else:
                    perform += x[i]
                i += 1
            line += perform + " "
            column += 1
        print(line)    
        row += 1
except ValueError as err:
    print(err)
except IndexError as err:
    print(err)
