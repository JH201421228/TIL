import sys
sys.setrecursionlimit(100_000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


char_dict = {'h': 1, 'b': 1, 'c': 1, 'n': 1, 'o': 1, 'f': 1, 'p': 1, 's': 1, 'k': 1, 'v': 1, 'y': 1, 'i': 1, 'w': 1, 'u': 1, 'ba': 1, 'ca': 1, 'ga': 1, 'la': 1, 'na': 1, 'pa': 1, 'ra': 1, 'ta': 1, 'db': 1, 'nb': 1, 'pb': 1, 'rb': 1, 'sb': 1, 'tb': 1, 'yb': 1, 'ac': 1, 'sc': 1, 'tc': 1, 'cd': 1, 'gd': 1, 'md': 1, 'nd': 1, 'pd': 1, 'be': 1, 'ce': 1, 'fe': 1, 'ge': 1, 'he': 1, 'ne': 1, 're': 1, 'se': 1, 'te': 1, 'xe': 1, 'cf': 1, 'hf': 1, 'rf': 1, 'ag': 1, 'hg': 1, 'mg': 1, 'rg': 1, 'sg': 1, 'bh': 1, 'rh': 1, 'th': 1, 'bi': 1, 'li': 1, 'ni': 1, 'si': 1, 'ti': 1, 'bk': 1, 'al': 1, 'cl': 1, 'fl': 1, 'tl': 1, 'am': 1, 'cm': 1, 'fm': 1, 'pm': 1, 'sm': 1, 'tm': 1, 'cn': 1, 'in': 1, 'mn': 1, 'rn': 1, 'sn': 1, 'zn': 1, 'co': 1, 'ho': 1, 'mo': 1, 'no': 1, 'po': 1, 'np': 1, 'ar': 1, 'br': 1, 'cr': 1, 'er': 1, 'fr': 1, 'ir': 1, 'kr': 1, 'lr': 1, 'pr': 1, 'sr': 1, 'zr': 1, 'as': 1, 'cs': 1, 'ds': 1, 'es': 1, 'hs': 1, 'os': 1, 'at': 1, 'mt': 1, 'pt': 1, 'au': 1, 'cu': 1, 'eu': 1, 'lu': 1, 'pu': 1, 'ru': 1, 'lv': 1, 'dy': 1}


def checker(word, idx, length):
    if idx == length: return True

    for i in range(1, 3):
        if idx+i <= length and word[idx:idx+i] in char_dict:
            if checker(word, idx+i, length): return True

    return False


def solve():
    words = [input().rstrip().lower() for _ in range(int(input()))]

    for word in words:
        for w in word.split():
            if not checker(w, 0, len(w)):
                print("NO")
                break
        else: print("YES")

    return


if __name__ == "__main__":
    solve()