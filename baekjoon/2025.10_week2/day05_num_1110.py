# 251011

current = int(input())
current = org

count = 0
while True:
    a = current // 10
    b = current % 10
    c = (a + b) % 10

    new_number = b * 10 + c
    count += 1

    if new_number == org:
        break
    else:
        current = new_number
        
print(count)


