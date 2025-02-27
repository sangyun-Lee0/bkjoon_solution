N, B = map(int, input().split())
word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
while N > 0:
    N, mod = divmod(N, B)
    if mod >= 10:
        mod = word[mod-10]
    result += str(mod)
    
print(result[::-1])
    
