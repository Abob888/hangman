n, i = 0, 0
a1 = ['cat', 'map', 'row', 'lap', '123', '13456-fghcvb']
a2 = ['row', 'top', 'lap', 'bag', '123', '13456-fghcvb']
a3 = ['кот', 'ром', 'нос', 'ухо', '888', 'вапро-765432']
while i < len(a1):
    if a1[i] in a2:
        n += 1
    i += 1
print(n)

j = 0
while j < len(a1):
    b1 = []
    b1.append(a1[j]+a2[j]+a3[j])
    print(b1)
    j += 1

