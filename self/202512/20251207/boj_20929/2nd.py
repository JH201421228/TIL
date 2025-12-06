import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    
    memo = {}

    def query(arr_type, idx):
        if idx < 1: return -float('inf')
        if idx > N: return float('inf')
        
        key = (arr_type, idx)
        if key in memo:
            return memo[key]
        
        print(f"? {arr_type} {idx}", flush=True)
        res = int(input())
        
        memo[key] = res
        return res

    low = 0
    high = N
    
    while low <= high:
        mid = (low + high) // 2
        
        val_a = query("A", mid)
        val_b = query("B", N - mid + 1)
        
        if val_a < val_b:
            low = mid + 1
        else:
            high = mid - 1
            
    
    final_a = query("A", low-1)
    final_b = query("B", N-low+1)
    
    print(f"! {max(final_a, final_b)}")
    sys.stdout.flush()

if __name__ == "__main__":
    solve()