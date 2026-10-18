words = input().split()
print('[' + ', '.join(f'"{w}"' for w in words) + ']')