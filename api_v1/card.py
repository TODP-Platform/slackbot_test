from flask import jsonify
from flask import request
from flask import Blueprint
from models import PickCard, db
import datetime
import requests
import random
from . import api


def send_slack(msg):
    res = requests.post('https://hooks.slack.com/services/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', json={
        'text': msg
    }, headers={'Content-Type': 'application/json'})


@api.route('/slack/card', methods=['POST'])
def receive_slack():
    res = request.form['text'].split(' ')
    cmd, *args = res

    ret_msg = ''
    if cmd == 'pick':
        user_name = args[0]
        card_subject = args[1]
        card_number = random.randrange(1, 7)

        card = PickCard()
        card.user_name = user_name
        card.card_subject = card_subject
        card.card_number = card_number
        card.status = 0

        db.session.add(card)
        db.session.commit()
        ret_msg = 'Card를 한장 뽑았습니다.'

        print(user_name, card_subject, card_number)

        send_slack('"%s"님께서 "%s"에 대한 카드 "%s"번을 뽑으셨습니다.' % (
            str(user_name), str(card_subject), str(card_number)))  # 사용자, 주제, 카드번호

    elif cmd == 'cancle':
        user_name = args[0]
        card = card.query.filter_by(user_name=user_name).first()

        card.status = 0
        db.session.commit()
        ret_msg = 'Card 뽑기가 취소 되었습니다.'

    return ret_msg
