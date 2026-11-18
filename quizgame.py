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

