import platform
import sys, os
import time

if platform.system() != "Windows":
    print("이 프로그램은 Windows만 지원합니다. (3초 뒤 종료됩니다.)")
    time.sleep(3)
    sys.exit(1)

alphabet_to_hanguel_jamo = {
    'q': 'ㅂ',
    'w': 'ㅈ',
    'e': 'ㄷ',
    'r': 'ㄱ',
    't': 'ㅅ',
    'y': 'ㅛ',
    'u': 'ㅕ',
    'i': 'ㅑ',
    'o': 'ㅐ',
    'p': 'ㅔ',
    'a': 'ㅁ',
    's': 'ㄴ',
    'd': 'ㅇ',
    'f': 'ㄹ',
    'g': 'ㅎ',
    'h': 'ㅗ',
    'j': 'ㅓ',
    'k': 'ㅏ',
    'l': 'ㅣ',
    'z': 'ㅋ',
    'x': 'ㅌ',
    'c': 'ㅊ',
    'v': 'ㅍ',
    'b': 'ㅠ',
    'n': 'ㅜ',
    'm': 'ㅡ',
    'Q': 'ㅃ',
    'W': 'ㅉ',
    'E': 'ㄸ',
    'R': 'ㄲ',
    'T': 'ㅆ',
    'O': 'ㅒ',
    'P': 'ㅖ'
}

def clear_screen():
    # 나중에 시간 생기면 멀티 플랫폼 형식으로 변경
    if platform.system() == "Windows": 
        os.system('cls')

def decode_key_into_hanguel_jamo(key):
    if key == b'\x08':  # 백스페이스 키 감지
        return "[BS]"
    else:
        decoded_key = key.decode('utf-8')
        if decoded_key in alphabet_to_hanguel_jamo.keys():            
            return alphabet_to_hanguel_jamo[decoded_key]
        elif decoded_key.isdigit():
            return decoded_key
        else:
            return None
    
print("키보드를 영문 키보드로 변경해주세요. 영문 키보드 상태가 아닌 경우 에러가 발생합니다.")

# 나중에 시간이 생기면 멀티 플랫폼 형식으로 변경
if platform.system() == "Windows":
    import msvcrt

    exec_flag = False
    english_keyboard = False
    
    key = None
    
    ## 키보드 검증
    print("진행을 위해 a를 입력해주세요.")
    while key != 'ㅁ':
        if exec_flag and not english_keyboard:
            print("\ra를 입력하지 않았거나, 영문 키보드 상태가 아닙니다. 영문 키보드 상태로 변경해주세요.", end="")

        if msvcrt.kbhit():
            exec_flag = True
            key = msvcrt.getch()

            try:
                key = decode_key_into_hanguel_jamo(key)
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                english_keyboard = False
    print("")

    ## 한글 자모 입력
    input_buffer = []
    clear_screen()
    print("영문 키보드를 유지하세요. 알파벳은 자동으로 한글 자모로 변환되어 입력됩니다. (알파벳, 숫자, 백스페이스를 제외한 모든 입력은 무시됩니다.)")
    print("현재까지 입력된 키:", end= "\n\n")
    print("현재까지 한글:", end="\n\n\n")
    while True:
        try:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                decoded_key = decode_key_into_hanguel_jamo(key)
                
                # 백스페이스 처리
                if decoded_key == "[BS]":
                    if input_buffer: 
                        input_buffer.pop()
                elif decoded_key is None:
                    continue
                else:
                    input_buffer.append(decoded_key)
                
                clear_screen()
                print("영문 키보드를 유지하세요. 알파벳은 자동으로 한글 자모로 변환되어 입력됩니다. (알파벳, 숫자, 백스페이스를 제외한 모든 입력은 무시됩니다.)")
                print("현재까지 입력된 키:", ",".join(input_buffer), end="\n\n")
                print("현재까지 한글:", "".join(input_buffer), end="\n\n\n")
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print("영문 키보드 입력이 아닙니다. (3초 뒤 종료됩니다.)")
            time.sleep(3)
            sys.exit(1)
