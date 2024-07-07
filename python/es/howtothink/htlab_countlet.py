"""count all letter and return a dict"""

def range_char(start, stop):
    """Character range function"""
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def count(text):
    """count single letter and iterate"""
    text = text.lower()
    allcount = {}

    for l in range_char("a", "z"):
        c = 0
        for ch in text:
            if ch == l:
                c = c + 1
        allcount[l] = c
    return allcount

def main():
    """main function"""
    print(count("banana"))

if __name__ == '__main__':
    main()
