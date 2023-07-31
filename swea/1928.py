# 1928. Base64 Decoder

# 0 ~ 25 (A-Z) / 26 ~ (a-z) / 52 ~ (0-9) / 62 '+' / 63 '/'
base64_ = [chr(65 + x) for x in range(26)]
base64_ += [chr(97 + x) for x in range(26)]
base64_ += [str(x) for x in range(10)]
base64_ += ['+', '/']

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case} ', end='')
    input_str = input()
    for start in range(0, len(input_str), 4):
    		#1. 4개 문자 슬라이싱
        target = input_str[start:start+4]
        #2. 4개 문자를 base64 표에 따라 decimal로 변환
        #3. 디코딩 후 출력
        # (1) << 2 | (2) >> 4  => chr(int())
        print(chr((base64_.index(target[0]) & int('00111111', base=2)) << 2 | (base64_.index(target[1]) & int('00110000', base=2)) >> 4), end='')
        # (2) << 4 | (3) >> 2  => chr(int())
        print(chr((base64_.index(target[1]) & int('00001111', base=2)) << 4 | (base64_.index(target[2]) & int('00111100', base=2)) >> 2), end='')
        # (3) << 6 | (4)       => chr(int())
        print(chr((base64_.index(target[2]) & int('00000011', base=2)) << 6 | base64_.index(target[3])), end='')
    
    print()
