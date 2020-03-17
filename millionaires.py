from questions.questions import *
from game.game import *


if __name__ == '__main__':
    print('Welcome in millionaires about Python. After you see a question you have 30s to repeat the issue.')
    print('You have to answer to 12 questions. Each features four possible answers.')
    print('During their game, you has 3 lifelines that you may use only once to help you with a question')
    print(' The safety net are relocated to PLN 1000 (after 2nd question) and PLN 40000 (after 7th question).')
    print('Do you want to start? [y/n]')
    answer = input()
    if answer.lower() == 'y':
        questions = Questions()
        user_game = Game(questions)
        user_game.play()

