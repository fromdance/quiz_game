import json
import os
import random
from datetime import datetime

from quiz import Quiz, CHOICE_COUNT
from read_line import read_int, read_text

DEFAULT_QUIZ_DATA = [
    Quiz("'블랙 펜서'의 힘을 얻을 수 있는 허브는?", ["하트 허브", "민트 허브", "블랙 허브", "파워 허브"], 1),
    Quiz("'와칸다'의 광산에서 채굴할 수 있는 것은?", ["묠니르", "인피니티 스톤", "비브라늄", "우라늄"], 3),
    Quiz("다음 중 '블랙 팬서'가 처음으로 등장했던 작품은?", ["<어벤저스: 에이지 오브 울트론>", "<어벤저스: 인피니티 워>", "<캡틴 아메리카: 시빌 워>", "<가디언즈 오브 갤럭시>"], 3),
    Quiz("<블랙 팬서>에서 '블랙 팬서' 티찰라의 사촌 동생으로, 왕위를 노려 티찰라와 결투를 벌이는 인물은?", ["주리", "버키", "킬몽거", "음바쿠"], 3),
    Quiz("'블랙 팬서'의 시그니처 제스쳐와 함께 나오는 구호로 올바른 것은?", ["이범베!", "와칸다 포에버!", "와칸다 어쎔블!", "마예파!"]),
    Quiz("다음 중, 인피니티 스톤과 등장 영화의 연결이 잘못된 것은?", ["파워스톤 - 가디언즈 오브 갤럭시", "타임스톤 - 닥터 스트레인지", "마인드스톤 - 앤트맨", "스페이스 스톤 - 어벤저스"], 3)
]

LINE = "=" * 40
THIN_LINE = "-" * 40

# 프로젝트 루트(이 파일이 있는 폴더)의 state.json 을 데이터 파일로 사용한다.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(PROJECT_ROOT, "state.json")

class QuizGame:
    # 퀴즈 목록과 최고 점수를 가지고 게임을 진행하는 클래스.
 
    def __init__(self, state_path=STATE_FILE):
        self.state_path = state_path
        self.quizzes = []
        self.best_score = 0
        self.best_record = None  # {"correct": 4, "total": 5, "played_at": "..."}

    # ================================== 메뉴 ==================================
    def show_menu(self):
        print()
        print(LINE)
        print("🎯 나만의 퀴즈 게임 🎯")
        print(LINE)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print(LINE)
 
    def run(self):
        """메뉴를 반복해서 보여 주며 선택한 기능을 실행한다."""
        actions = {
            1: self.play,
            2: self.add_quiz,
            3: self.show_quiz_list,
            4: self.show_score,
        }
 
        while True:
            self.show_menu()
            choice = read_int("선택: ", 1, 5)
 
            if choice == 5:
                print("게임을 종료합니다. 데이터를 저장했습니다.")
                break
 
            actions[choice]()

    # ================================== 2. 퀴즈 추가 ==================================
    def add_quiz(self):
        print()
        print("새로운 퀴즈를 추가합니다.")
 
        question = read_text("문제를 입력하세요: ")
        # 선택지 입력은 정해진 '퀴즈 선택지 개수(CHOICE_COUNT)' 만큼 반복해서 이뤄짐
        choices = [read_text(f"선택지 {number}: ") for number in range(1, CHOICE_COUNT + 1)]
        answer = read_int(f"정답 번호 (1-{CHOICE_COUNT}): ", 1, CHOICE_COUNT)
 
        self.quizzes.append(Quiz(question, choices, answer))

    # ================================== 3. 퀴즈 목록 ==================================
    def show_quiz_list(self):
        print()
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 [2. 퀴즈 추가]로 문제를 등록해 주세요.")
            return
 
        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print(THIN_LINE)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print(THIN_LINE)
        
    # ================================== 4. 점수 확인 ==================================
    def show_score(self):
        print()
        if not self.best_record:
            print("아직 퀴즈를 푼 기록이 없습니다. [1. 퀴즈 풀기]로 도전해 보세요!")
            return
 
        correct = self.best_record["correct"]
        total = self.best_record["total"]
        played_at = self.best_record.get("played_at", "기록 없음")
 
        print(f"🏆 최고 점수: {self.best_score}점 ({total}문제 중 {correct}문제 정답)")
        print(f"🕒 기록 시각: {played_at}")