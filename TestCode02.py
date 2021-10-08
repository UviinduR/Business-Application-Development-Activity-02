# This is a sample Python script.
row_count = int(input("Enter desired number of rows : "))

r = 0
c = 0
c1 = 0

for i in range(1, row_count + 1):
    for space in range(1, (row_count - i) + 1):
        print("  ", end="")
        c += 1

    while r != ((2 * i) - 1):
        if c <= row_count - 1:
            print(i + r, end=" ")
            c += 1
        else:
            c1 += 1
            print(i + r - (2 * c1), end=" ")
        r += 1

    c1 = c = r = 0
    print()