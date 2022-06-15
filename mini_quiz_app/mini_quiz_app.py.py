from questions import questions, options, instructions


take_quiz_again = True


def start_quiz():
    question_number = 0
    user_answers = []
    correct_scoring = 0
    print('**********************************************************************')
    print(instructions)
    print('**********************************************************************')

    for question in questions:
        print(question)
        print('-------------------')
        for option in options[question_number]:
            print(option)
        print('==================')
        user_answer = input('Provide your answer: (A,B,C or D)').upper()
        user_answers.append(user_answer)
        correct_answer = questions.get(question)
        correct_scoring += answer_validation(correct_answer, user_answer)
        print()
        question_number += 1

    print_scores(correct_scoring, user_answers)


def answer_validation(correct_answer, user_answer):
    if correct_answer == user_answer:
        print('Got this one Correct !')
        return 1
    else:
        print('Got this one wrong!')
        return 0


def print_scores(correct_scoring, user_answers):

    print('Correct Answers: ', end='')
    for i in questions:
        print(questions.get(i), end=' ')
    print()

    print('Your Answers: ', end='')
    for i in user_answers:
        print(i, end=' ')
    print()
    score = int((correct_scoring / len(questions)) * 100)
    print('=================')
    print(f'You scored : {score}%')
    print('=================')


def take_quiz_again():
    response = input('Take test again? : (YES / NO )').upper()
    if response == 'YES':
        return True
    else:
        return False


start_quiz()

while take_quiz_again():
    start_quiz()




