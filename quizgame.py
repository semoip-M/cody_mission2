import json
import random
import os

class mkQuiz:
    # 퀴즈만드는 클래스: 초기입력변수로 question, options, answer를 받는다.
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer
    # 객체를 딕셔너리로 변환하는 메서드
    def to_dict(self):
        return {
            'question': self.question,
            'options': self.options,
            'answer': self.answer
        }

class Quizgame:
    def __init__(self):
        pass
    
    def run(self):

        while True:
            print("\n퀴즈 게임 메뉴:")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 확인")
            print("5. 종료")
            choice = input("원하는 번호를 입력하시오 (1-5): ").strip()
            
            if choice == '1':
                self.create_quiz()
            elif choice == '2':
                self.add_quiz()
            elif choice == '3':
                self.view_quiz_list()
            elif choice == '4':
                self.check_high_score()
            elif choice == '5':
                print("게임을 종료합니다.")
                break
            else:
                print("\n 잘못된 선택입니다. 1~5 사이의 숫자를 입력해주세요.")


if __name__ == '__main__':
    play = Quizgame()
    play.run()

