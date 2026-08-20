CHOICE_COUNT = 4  # 선택지 개수 (문제당 4개 고정)

class Quiz:
    # 문제(question), 선택지(choices), 정답 번호(answer)를 가지는 퀴즈 클래스

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = list(choices)
        self.answer = int(answer)  # 1 ~ 4 사이의 번호

    def format_question(self, number=None):
        # 화면에 보여줄 문제 문자열을 만들어 돌려준다.
        # 몇번 문제인지, '문제 자체'는 미리 출력할 문자열 리스트(lines)에 넣어놓는다.
        # 만약, 몇 번 문제인지 주어지지 않으면 [문제] 라고만 출력
        title = f"[문제 {number}]" if number is not None else "[문제]"
        lines = [title, self.question]
        # Python의 list 순회시, index가 필요하다면 빌트-인 메서드인 enumerate(리스트, start=시작인덱스)를 사용하면
        # [index, element] 쌍으로 순회할 수 있다.
        for index, choice in enumerate(self.choices, start=1):
            lines.append(f"  {index}. {choice}")
        # Python의 String Join은 "구분자 문자열".join(구분자로 합칠 각 문자열 집합)
        return "\n".join(lines)

    def show(self, number=None):
        # 문제와 선택지를 화면에 출력한다.
        print(self.format_question(number))

    def is_correct(self, choice_number):
        # 사용자가 고른 번호가 정답인지 반환한다.
        return choice_number == self.answer

    def answer_text(self):
        # 정답을 문자열로 반환한다.
        return self.choices[self.answer - 1]

    # ------------------------------------------------------------------
    # JSON 저장 / 불러오기용 변환
    # ------------------------------------------------------------------
    def to_dict(self):
        # JSON으로 저장할 수 있는 딕셔너리 형태로 변환한다.
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    # @classmethod = 해당 클래스 자체를 다루는 메서드를 만들때 주로 사용하는 데코레이터로,
    # 클래스 자체를 첫 번째 인수로 받음
    @classmethod
    def from_dict(cls, data):
        # 딕셔너리 값으로부터 Quiz 객체를 만든다. 형식이 잘못되면 ValueError를 발생시킨다.
        if not isinstance(data, dict):
            raise ValueError("퀴즈 항목은 딕셔너리여야 합니다.")

        question = data.get("question")
        choices = data.get("choices")
        answer = data.get("answer")

        if not isinstance(question, str) or not question.strip():
            raise ValueError("question 값이 비어 있거나 문자열이 아닙니다.")

        if not isinstance(choices, list) or len(choices) != CHOICE_COUNT:
            raise ValueError(f"choices 는 {CHOICE_COUNT}개의 항목을 가진 목록이어야 합니다.")

        if not all(isinstance(choice, str) and choice.strip() for choice in choices):
            raise ValueError("choices 의 각 항목은 비어 있지 않은 문자열이어야 합니다.")

        # bool은 int 의 하위 타입이므로 따로 필터링해야한다.
        # ininstance(answer, int)로 할 경우, answer가 True, False여도 통과하기 때문
        if isinstance(answer, bool) or not isinstance(answer, int):
            raise ValueError("answer 는 정수여야 합니다.")

        if not 1 <= answer <= CHOICE_COUNT:
            raise ValueError(f"answer 는 1 ~ {CHOICE_COUNT} 사이여야 합니다.")

        # 클래스 자체(즉, 생성자)를 사용해 클래스로 변환한다.
        # 이때, 문제, 답변들은 모두 앞/뒤 공백을 제거 처리해준다.
        return cls(
            question.strip(),
            [choice.strip() for choice in choices],
            answer,
        )