import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    # 초성 다음 중성 그리고 다음 중성이 나오기 전에 도깨비불이 발생함
    # 중성이 발생한 다음 다음 중성이 발생하기까지 사이에 종성만 있으면 도깨비불 발생
    # 맞춤법에 안맞는 글자를 입력하는 케이스 존재할 수 있음
    
    mid_char = ["hk", "ho", "hl", "nj", "np", "nl", "ml", "l", "k", "o", "i", "O", "j", "p", "u", "P", "h", "b", "m", "y", "n"]
    end_char = ["r", "R", "rt", "s", "sw", "sg", "e", "f", "fr", "fa", "fq", "ft", "fx", "fv", "fg", "a", "q", "qt", "t", "T", "d", "w", "c", "z", "x", "v", "g"]
    
    ans = 0
    
    cand = list(input().rstrip().split())
    for c in cand:
        for mid in mid_char:
            c = " ".join(c.split(mid))
        
        if c[-1] == " ":
            for ch in c.split()[1:]:
                if ch in end_char: ans += 1
        else:
            for ch in c.split()[1:-1]:
                if ch in end_char: ans += 1
            
    print(ans) 
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()