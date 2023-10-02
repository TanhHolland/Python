t = int(input())
mod = 10**9 + 7
while t > 0 :
    t-=1
    n,k = list(map(int,input().split()))
    s,p = 0,1
    while k > 0:
        if k % 2 == 1 :
            s += p
            s %= mod
        p *= n
        k//=2
    print(s)
# Giải thích : n = 3, k = ?
# STT Số  Tổng
# 1   1   3^0
# 2   3   3^1
# 3   4   3^0 + 3^1
# 4   9   3^2
# 5   10  3^0 + 3^2
# 6   12  3^1 + 3^2
# 7   13  3^0 + 3^1 + 3^2
# 8   27  3^3
# 9   28  3^0 + 3^3
# 10  30  3^1 + 3^3
# - k lẻ tông luôn có số n^0 (1) p = 1
# - k chẵn :
#     + k toàn chia hết cho 2 --> STT k có giá trị là 3^log2(k) VD : k = 1,4,8
#     + k chia 2 dư 0 hoặc 1 --> STT k có giá trị như quy luật trên
#     cứ chia đến khi k lẻ thì cộng vào s
#     còn lại cứ tính mũ p lên =))))