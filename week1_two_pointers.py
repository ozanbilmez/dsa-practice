def iki_toplam_siralı(a, hedef):
    sol = 0
    sag = len(a) - 1
    while sol < sag:
        toplam = a[sol] + a[sag]
        if toplam == hedef:
            return (sol, sag)
        if toplam > hedef:
            sag -= 1
        else:
            sol += 1
    return None


def yinelenenleri_sil(a):
    if not a:
        return 0
    yavas = 0
    for hizli in range(1, len(a)):
        if a[hizli] != a[yavas]:
            yavas += 1
            a[yavas] = a[hizli]
    return yavas + 1


print(iki_toplam_siralı([1, 2, 3, 4, 6], 6))
print(iki_toplam_siralı([1, 2, 3, 4, 6], 100))

liste = [1, 1, 2, 2, 3]
n = yinelenenleri_sil(liste)
print(n, liste[:n])

liste2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
n2 = yinelenenleri_sil(liste2)
print(n2, liste2[:n2])

print(yinelenenleri_sil([]))