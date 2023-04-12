#Вам требуется написать программу, которая проверяет счастливость билета.
ticket = int(input())
last_part = ticket % 10 + ticket // 10 % 10 + ticket // 100 % 10
first_part = ticket // 1000 % 10 + ticket // 10000 % 10 + ticket // 100000
if last_part == first_part:
    print('yes')
else:
    print('nope')

#альтернативная версия со строкой
#tick_st = input()
#if tick_st[0] + tick_st[1] + tick_st[2] == tick_st[3] + tick_st[4] + tick_st[5]:
#    print('yes')
#else:
#    print('nope')
