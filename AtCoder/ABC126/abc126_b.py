s = input()

a = int(s[:2])
b = int(s[2:])

ans = []

if ((1 <= b) and (b <= 12)) and ((1 <= a) and (a <= 12)):
    print("AMBIGUOUS") 
elif (1 <= b) and (b <= 12):
    print("YYMM")
elif (1 <= a) and (a <= 12):
    print("MMYY")
else:
    print("NA")