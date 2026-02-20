import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    trie = {"": []}
    
    words = []
    
    for _ in range(N):
        word = input().rstrip()
        
        words.append(word)
        
        prev_key = ""
        
        for idx in range(1, len(word)+1):
            cur_key = word[:idx]
            
            if cur_key not in trie[prev_key]:
                trie[prev_key].append(cur_key)
                trie[cur_key] = []
            
            prev_key = cur_key
            
        trie[cur_key].append("")
    
    ans = 0
    for word in words:
        cnt = 1
        
        for idx in range(len(word)-1):
            key = word[:idx+1]
            
            if len(trie[key]) > 1: cnt += 1
            
        ans += cnt
        
    print(f"{ans / N:.2f}")
    
    return


def main():
    while True:
        try:
            solve()
        except:
            break
    
    return


if __name__ == "__main__":
    main()