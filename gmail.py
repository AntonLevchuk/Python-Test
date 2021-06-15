def counter():
    words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
             9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
             16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
             50: 'fifty', 60: 'sixty'}
    string = input()
    result = eval(string)

    if result >=0 and result <= 63:
        if result in words:
            print(words[result])

        else:
            q, mod = divmod(result, 10)
            print(words[q * 10], words[mod])

    elif result < 0:
        print(f'The numbers cannot be negative: {result}')

    elif result > 63:
        print(f'Your numbers are too large: {result}')


counter()
