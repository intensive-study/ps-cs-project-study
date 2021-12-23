import sys
from collections import defaultdict

input = sys.stdin.readline

def get_ancestors(node, tree):
    stack = [node]
    arr = [node]
    while stack:
        x = stack.pop()
        if tree[x]:
            stack.append(tree[x])
            arr.append(tree[x])
    
    return arr

if __name__ == "__main__":
    tc = int(input())
    while tc:
        tree = defaultdict(int)
        n = int(input())
        for _ in range(n-1):
            p, c = map(int, input().split())
            tree[c] = p

        x, y = map(int, input().split())
        x_ancs = get_ancestors(x, tree)
        y_ancs = get_ancestors(y, tree)
        
        for x_anc in x_ancs:
            if x_anc in y_ancs:
                print(x_anc)
                break

        tc -= 1