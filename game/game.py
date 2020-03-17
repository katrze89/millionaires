import random

TOTAL_QUESTIONS = 12
SAFETY_NET = [2, 7]


class Game:
    def __init__(self, question):
        self.safety_net = 0
        self.current_inx = 0
        self.question = question
        self.winnings = [0, 500, 1000, 2000, 5000, 10000, 20000, 40000, 75000, 125000, 250000, 500000, 1000000]
        self.lifelines = ['50/50', 'Ask the Audience', 'Phone a Friend']

    @staticmethod
    def generate_percentages():
        num = 0
        percentage_list =[]
        for _ in range(3):
            rand_num = random.randint(0, 100 - num)
            percentage_list.append(rand_num)
            num = num + rand_num
        percentage_list.append(100 - num)
        return percentage_list

    def half_half(self, current_question):
        print(current_question['question'])
        correct_ans = current_question['correct_ans']
        ans_list = ['a', 'b', 'c', 'd']
        ans_list.remove(correct_ans)
        second_ans = random.choice(ans_list)
        self.question.print_answers(current_question, sorted([correct_ans, second_ans]))

    def ask_audience(self, current_question):
        self.question.print_audience_answers(current_question, self.generate_percentages())

    def phone_friend(self, current_question):
        print(current_question['question'])
        ans_list = ['a', 'b', 'c', 'd']
        second_ans = random.choice(ans_list)
        self.question.print_answers(current_question, [second_ans])

    def lifeline(self, idx, current_question):
        chosen_lifeline = self.lifelines[idx]
        if chosen_lifeline == '50/50':
            self.half_half(current_question)
        elif chosen_lifeline == 'Ask the Audience':
            self.ask_audience(current_question)
        else:
            self.phone_friend(current_question)
        self.lifelines.pop(idx)

    def ask_lifelines(self, current_question):
        if len(self.lifelines) > 0:
            print('Do you want to use a lifelines [y/n]')
            ans_lif = input()
            if ans_lif.lower() == 'y':
                if len(self.lifelines) > 1:
                    print('Which lifeline do you want to use?')
                    for inx, lifeline in enumerate(self.lifelines):
                        print(f"{inx + 1}. {lifeline}")
                    which_lifeline = input()
                else:
                    print(f'Only one possible lifeline: {self.lifelines[0]}')
                    which_lifeline = 1
                self.lifeline(int(which_lifeline) - 1, current_question)

    @staticmethod
    def request_response():
        print('Give answer')
        ans_question = input()
        return ans_question

    def play(self):
        self.generate_percentages()
        while True:
            print(f"You play for PLN {self.winnings[self.current_inx + 1]}")
            current_question = self.question.shuffle_question()
            self.question.handle_question(current_question)
            self.ask_lifelines(current_question)
            question_answer = self.request_response()
            if self.question.evaluate_answer(current_question, question_answer):
                self.current_inx += 1
                if self.current_inx == TOTAL_QUESTIONS:
                    print(f'Congratulation.You answered {TOTAL_QUESTIONS} questions and won {self.winnings[self.current_inx]}')
                    break
                else:
                    if self.current_inx in SAFETY_NET:
                        self.safety_net = self.current_inx
                    print(f'Congratulation, good answer. You won {self.winnings[self.current_inx]}')
                    print(f'If you finished now you would win {self.winnings[self.safety_net]}')
                    print('Do you want to keep playing? [y/n]')
                    if input().lower() == 'n':
                        break
            else:
                print(f'Sorry, wrong answer. Game over, you won {self.winnings[self.safety_net]}')
                break
