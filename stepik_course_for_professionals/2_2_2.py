en, ru = 'AaBCcEeHKMOoPpTXxy', 'АаВСсЕеНКМОоРрТХху'

l1 = input()
l2 = input()
l3 = input()

if l1 in ru and l2 in ru and l3 in ru and l1 not in en and l2 not in en and l3 not in en:
    print("ru")
elif l1 in en and l2 in en and l3 in en and l1 not in ru and l2 not in ru and l3 not in ru:
    print("en")
else:
    print("mix")