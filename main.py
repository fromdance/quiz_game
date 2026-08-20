# 실행 방법:    python main.py
 
from quiz_game import QuizGame
 
def main():
    game = QuizGame()
    game.load()
 
    try:
        game.run()
    except KeyboardInterrupt:
        # Ctrl + C 로 중단한 경우
        print("\n\n⚠️ 사용자가 프로그램을 중단했습니다.")
        _safe_exit(game)
    except EOFError:
        # 입력 스트림이 끝난 경우 (예: 파이프 입력이 끝났을 때)
        print("\n\n⚠️ 더 이상 입력을 받을 수 없습니다.")
        _safe_exit(game)
 
 
def _safe_exit(game):
    print("안전하게 종료합니다.")
 
 
if __name__ == "__main__":
    main()
 