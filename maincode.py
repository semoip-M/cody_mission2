import json
import random
import os

class mkQuiz:
    # 이 클래스로 객체가 만들어질 때, 자동작동되는 메서드. 초기입력변수로 question, options, answer를 받는다.
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
    # 이 클래스로 객체가 만들어질 때, 자동작동되는 메서드. 초기입력변수는 없음.
    def __init__(self):
        self.json_data = 'quiz_data.json'
        self.quiz_list = []
        self.high_score = 0
        self.load_data()
        self.show_high_score()

    def load_data(self):
        """json파일에서 데이터를 읽어오거나, 없으면 초기 데이터 생성한다."""
        if os.path.exists(self.json_data):
            with open(self.json_data, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    quiz = mkQuiz(item['question'], item['options'], item['answer'])
                    self.quiz_list.append(quiz)
    
    def show_high_score(self):
        """최고 점수 출력"""
        print(f"\n🏆 현재 최고 점수: {self.high_score}점")

    
    def run(self):

        while True:
            print("\n퀴즈 게임 메뉴:")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 확인")
            print("5. 종료")
            choice = input("원하는 메뉴의 번호를 입력하시오 (1-5): ").strip()
            
            if choice == '1':
                self.create_quiz()
            elif choice == '2':
                self.add_quiz()
            elif choice == '3':
                self.view_quiz_list()
            elif choice == '4':
                self.show_high_score()
            elif choice == '5':
                print("게임을 종료합니다.")
                break
            else:
                print("\n 잘못된 선택입니다. 1~5 사이의 숫자를 입력해주세요.")


if __name__ == '__main__':
    play = Quizgame()
    play.run()
