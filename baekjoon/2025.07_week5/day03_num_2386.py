# 250803

while True:
    n = input()

    if n == '#' :
        break

    target = n[0].lower()
    sentence = n[2:].lower()
    count = sentence.count(target)

    print(n[0], count)


