from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")


def get_headlines():
    user_pass_dict = {'user': 'mini_project_kervin',
                      'passwd': 'mini_project_kervin',
                      'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update(
        {'User-Agent': 'Alexa Skill Mini Project: Kervin Rodriguez'})
    sess.post('https://www.reddit.com/api/login', data=user_pass_dict)
    time.sleep(1)
    url = 'https://reddit.com/r/worldnews/.json?limit=5'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title'])
              for listing in data['data']['children']]
    titles = '...'.join([i for i in titles])
    return titles

@app.route('/')
def homepage():
    return "Hello Kervin, how are you?"


@ask.launch
def start_skill():
    welcome_message = 'Hello Kervin, would you like me to tell you todays top news stories?'
    return question(welcome_message)


@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_msg = 'The current top news headlines are {}'.format(headlines)
    return statement(headline_msg)


@ask.intent("NoIntent")
def no_intent():
    bye_text = "Well why did you even ask me in the first place... Good bye."
    return statement(bye_text)


if __name__ == '__main__':
    app.run(debug=True)

