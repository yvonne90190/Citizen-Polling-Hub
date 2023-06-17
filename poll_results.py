
from flask import jsonify, Blueprint
from datetime import datetime
from ORM import Poll, Vote, Question, app, db


bp = Blueprint('poll_results', __name__)


@bp.route('/poll_results/<path:poll_id>', methods=['GET'])
def getPollResult(poll_id):

    poll = Poll.query.filter_by(poll_id=poll_id).first()

    if not poll:
        return jsonify({'error': f'Poll:{poll_id} does not exist.'}), 400
    if not poll.is_approved:
        return jsonify({'error': f'Poll:{poll_id} has not been approved yet.'}), 400
    else:
        if poll.start_date > datetime.now().date():
            return jsonify({'error': f'Poll:{poll_id} has not started yet.'}), 400
        if poll.end_date > datetime.now().date():
            return jsonify({'error': f'Poll:{poll_id} has not ended yet.'}), 400

    questions = Question.query.filter_by(poll_id=poll_id).all()
    results = []
    for question in questions:
        question_result = {
            "text": question.text,
            'question_id': question.question_id,
            'options': [],
            'result': "",
        }
        support_cnt, oppose_cnt = question.count_support, question.count_oppose
        total_cnt = support_cnt + oppose_cnt
        for vote_cnt in [support_cnt, oppose_cnt]:
            if total_cnt == 0:
                percentage = 0
            else:
                percentage = 100 * vote_cnt/total_cnt
            option_id = 0 if vote_cnt == oppose_cnt else 0
            option_result = {
                'option_id': option_id,
                'percentage': percentage,
                'vote_cnt': vote_cnt
            }

            question_result['options'].append(option_result)

        # sort by option_id and inplace
        question_result['options'].sort(key=lambda x: x['option_id'])

        # determine the result
        suppose = question_result['options'][0]['vote_cnt']
        oppose = question_result['options'][1]['vote_cnt']
        if suppose > oppose and suppose > 0.25 * total_cnt:

            #
            question_result['result'] = 'pass'
        else:
            question_result['result'] = 'not pass'

        results.append(question_result)

    return jsonify({'poll_id': poll_id, 'results': results}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # user = User(username='chang', email='a85948533@gmail.com', password='tt')
        # db.session.add(user)
        # poll = Poll(title='ended', description='Poll has ended.', creator_id=1, start_date=datetime.strptime('2020-3-3', '%Y-%m-%d'), end_date=datetime.strptime('2021-4-23', '%Y-%m-%d'))
        # db.session.add(poll)
        # q = Question(poll_id=11, question_id=1, text='test')
        # qq = Question(poll_id=11, question_id=2, text='testtest')
        # qqq = Question(poll_id=11, question_id=3, text='testtesttest')
        # db.session.add_all([q, qq, qqq])
        # for i in range(1, 4):
        #     option1 = Options(option_id=1, question_id=i, poll_id=11, text=True, vote_count=10)
        #     option2 = Options(option_id=2, question_id=i, poll_id=11, text=False, vote_count=6)
        #     db.session.add_all([option1, option2])
        # db.session.commit()

    app.run(debug=True)
