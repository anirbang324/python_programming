def check(string):
    string = string.replace(' ', '')
    string = string.lower()
    vowel = [string.count('a'), string.count('e'), string.count(
        'i'), string.count('o'), string.count('u')]

    # If 0 is present int vowel count array
    if vowel.count(0) > 0:
        return ('not accepted')
    else:
        return ('accepted')


# Driver code
if __name__ == "__main__":
    string = input()

    print(check(string))