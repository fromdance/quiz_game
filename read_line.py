
def read_line(message):
    # 문자열 입력받아, 입력의 앞, 뒤 공백 제거
    return input(message).strip()

def process_input(message, min_value, max_value):
    while True:
        # 주어진 허용 범위(min_value ~ max_value)사이의 값을 받을 때 까지 반복
        line = read_line(message)

        if not line:
            print("입력이 비어 있습니다.")
            continue

        line = line.strip()

        try:
            value = int(line)
        except ValueError:
            print(f"숫자로 된 값이 아닙니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        if not min_value <= value <= max_value:
            print(f"범윌르 벗어난 값입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        return value