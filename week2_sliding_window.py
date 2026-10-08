def max_sum(a, k):
    if k <= 0 or k > len(a):
        raise ValueError("k, 1 ile len(a) arasında olmalı")
    pencere = sum(a[:k])
    en_iyi = pencere
    for i in range(k, len(a)):
        pencere += a[i] - a[i - k]
        en_iyi = max(en_iyi, pencere)
    return en_iyi


def en_kisa_alt_dizi(a, s):
    sol = 0
    toplam = 0
    en_kisa = len(a) + 1
    for sag in range(len(a)):
        toplam += a[sag]
        while toplam >= s:
            en_kisa = min(en_kisa, sag - sol + 1)
            toplam -= a[sol]
            sol += 1
    return 0 if en_kisa == len(a) + 1 else en_kisa


def en_uzun_tekrarsiz(s):
    pencere = set()
    sol = 0
    en_uzun = 0
    for sag in range(len(s)):
        while s[sag] in pencere:
            pencere.remove(s[sol])
            sol += 1
        pencere.add(s[sag])
        en_uzun = max(en_uzun, sag - sol + 1)
    return en_uzun


print(max_sum([2, 1, 5, 1, 3, 2], 3))
print(en_kisa_alt_dizi([2, 3, 1, 2, 4, 3], 7))
print(en_kisa_alt_dizi([1, 1, 1], 10))
print(en_uzun_tekrarsiz("abcabcbb"))
print(en_uzun_tekrarsiz("bbbbb"))
print(en_uzun_tekrarsiz(""))