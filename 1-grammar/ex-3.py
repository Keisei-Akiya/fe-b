cnt = 0

# 1から6まで3ずつ増やす
for i in range(1, 6, 3):
    cnt = cnt + i

# 6から4まで3ずつ減らす
for j in range(6, 4, -3):
    cnt = cnt + j

print(cnt)