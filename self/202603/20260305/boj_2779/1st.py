import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def cal(key, word):
    char_dict = {}
    
    for k in key:
        char_dict[k] = char_dict.get(k, 0) + 1
        
    for w in word:
        char_dict[w] = char_dict.get(w, 0) - 1
    
    for k, v in char_dict.items():
        if v: return -1
    
    res = 0
    
    for idx in range(len(word)):
        if key[idx] != word[idx]: res += 1
    
    return res


def solve():
    secret_key = input().rstrip()
    
    words = []
    
    for _ in range(int(input())): words.append(input().rstrip())

    dp = [float("inf")] * (len(secret_key) + 1)
    
    for word in words:
        if len(word) <= len(secret_key):
            score = cal(secret_key[:len(word)], word)
            if score != -1: dp[len(word)] = min(dp[len(word)], score)
    
    for idx in range(1, len(secret_key)+1):
        if dp[idx] != float("inf"):
            for word in words:
                if len(word) + idx <= len(secret_key):
                    score = cal(secret_key[idx:idx+len(word)], word)
                    if score != -1: dp[idx+len(word)] = min(dp[idx+len(word)], dp[idx] + score)
    
    if dp[-1] == float("inf"): print(-1)
    else: print(dp[-1])
    
    return


def main():
    for _ in range(int(input())): solve()

    return


if __name__ == "__main__":
    main()