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
        self.quizzes = []
        self.high_score = 0
        self.load_data()

    def load_data(self):
        """json파일에서 데이터를 읽어오거나, 없으면 초기 데이터 생성한다."""
        if os.path.exists(self.json_data): # json파일을 불러올 준비
            try:
                with open(self.json_data, 'r', encoding='utf-8') as f: # json파일을 읽기모드로 열고, 인코딩은 utf-8로 설정
                    data = json.load(f) # json파일을 읽어서 data에 저장
                    self.high_score = data.get('high_score', 0) # json파일에서 high_score를 읽어오고, 없으면 0으로 설정
                    for item in data: # json파일의 각 항목을 반복
                        quiz = mkQuiz(item['question'], item['options'], item['answer']) # mkQuiz class로 객체 quiz를 생성. item은 dict형태.
                        self.quizzes.append(quiz) # 생성된 quiz 객체를 quizzes 리스트에 추가
            except (json.JSONDecodeError, KeyError): # json파일이 잘못되었거나, key가 없을 경우
                self.set_initial_data() # json파일이 잘못되었을 경우 초기 데이터를 설정하는 메서드 호출
        else:
            self.set_initial_data() # json파일이 없으면 초기 데이터를 설정하는 메서드 호출

    def set_initial_data(self):
        """초기 퀴즈 데이터 5개를 설정합니다."""
        initial_quizzes = [
            mkQuiz("2002년도 축구 월드컵이 열린 나라는?", ["스리랑카", "한국", "미국", "브라질"], 2),
            mkQuiz("축구 goat는 누구인가?", ["이천수", "외질", "강호동", "메시"], 4),
            mkQuiz("축구는 몇 명이서 하나의 팀으로 뛰는 게임인가?", ["11명", "10명", "12명", "9명"], 1),
            mkQuiz("2026년 월드컵을 우승한 나라는?", ["브라질", "아르헨티나", "스페인", "프랑스"], 3),
            mkQuiz("홍명보가 좋아하는 전술은?", ["442", "쓰리백", "4231", "False 9"], 2)
        ]
        self.quizzes = initial_quizzes
        self.high_score = 0
        self.save_data()

    def save_data(self):
        """현재 상태(최고점수,퀴즈데이터)를 json 파일에 저장합니다."""
        data = {
            'high_score': self.high_score,
            'quizzes': [quiz.to_dict() for quiz in self.quizzes]
        } # json파일에 저장할 데이터를 딕셔너리 형태로 구성. high_score와 quizzes를 포함. quizzes는 mkQuiz 객체를 딕셔너리로 변환한 리스트.
        with open(self.json_data, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4) # json파일에 데이터(최고점수,퀴즈데이터)를 저장.

    def add_quiz(self):
        """퀴즈 추가"""
        print("\n--- 새로운 퀴즈 추가 ---")
        question = input("\n추가할 퀴즈 질문을 입력하시오: ").strip()
        options = []
        for i in range(1, 5):
            option = input(f"선택지 {i}를 입력하시오: ").strip()
            options.append(option)
        while True:
            try:
                answer = int(input("정답 선택지 번호를 입력하시오 (1-4): ").strip())
                if 1 <= answer <= 4:
                    break
                else:
                    print("1~4 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("숫자만 입력 가능")
        new_quiz = mkQuiz(question, options, answer)
        self.quizzes.append(new_quiz)
        self.save_data()
        print("\n✅ 퀴즈가 성공적으로 추가되었습니다.")

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
                self.play_quiz()
            elif choice == '2':
                self.add_quiz()
            elif choice == '3':
                self.show_quiz_list()
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
