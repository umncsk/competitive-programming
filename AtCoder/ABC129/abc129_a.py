P, Q, R = map(int, input().split())

calc_list = [P+Q, Q+R, R+P]

print(min(calc_list))
