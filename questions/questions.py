import configparser
import time
import random


class Questions:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('question.ini')
        self.questions = self.config.sections()
        self.used_questions = []

    def shuffle_question(self):
        while True:
            rand_num = random.randint(0, len(self.questions) - 1)
            if self.questions[rand_num] not in self.used_questions:
                self.used_questions.append(self.questions[rand_num])
                return self.config[self.questions[rand_num]]

    @staticmethod
    def print_answers(current_question, ans_list=['a', 'b', 'c', 'd']):
        response = [f"{letter}) {current_question[letter]}" for letter in ans_list]
        print('\n'.join(response))

    @staticmethod
    def print_audience_answers(current_question, percentage, ans_list=['a', 'b', 'c', 'd']):
        print(current_question['question'])
        response = [f"{letter}) {current_question[letter]}\n {'|' * percentage[idx]}\t {percentage[idx]}%" for idx, letter in enumerate(ans_list)]
        print('\n'.join(response))

    def handle_question(self, current_question):
        print(current_question['question'])
        time.sleep(2)
        self.print_answers(current_question)

    @staticmethod
    def evaluate_answer(current_question, question_answer):
        return True if current_question['correct_ans'] == question_answer.lower() else False
