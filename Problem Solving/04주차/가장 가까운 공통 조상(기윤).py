import sys
from collections import defaultdict

input = sys.stdin.readline
tc = int(input())

def get_ancestors(node):
    stack = [node]
    p = [node]

    while stack:
        x = stack.pop()
        if reverse_tree[x]:
            p.append(reverse_tree[x])
            stack.append(reverse_tree[x])
    
    return p
        
if __name__ == "__main__":
    while tc:
        reverse_tree = defaultdict(int)
        n = int(input())
        for _ in range(n-1):
            p, c = map(int, input().split())
            reverse_tree[c] = p
        
        a, b = map(int, input().split())
        arr1 = get_ancestors(a)
        arr2 = get_ancestors(b)
        
        for node in arr1:
            if node in arr2:
                print(node)
                break

        tc -= 1