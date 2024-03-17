# 2024/03/17
# 추가 또는 사용된 연료의 양을 입력하고, 남아있는 양을 출력
# fuel = 연료


s_fuel = 500

while True:
    fuel = int(input('충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오:'))
    s_fuel += fuel
    print('현재 탱크량은', s_fuel, '입니다.')
    if s_fuel < 50:
        print('경고 : 연료가 10% 미만이니 충전하세요!')
        break
