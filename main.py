import spacy
import os
from spacy import displacy
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kek'
nlp = spacy.load("ru_core_news_sm")


from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    text = TextAreaField('Предложение', render_kw={'cols': '50'})
    submit = SubmitField('Разобрать')


@app.route('/', methods=['GET', 'POST'])
def display():
    form = MyForm()
    sentence = None
    if form.validate_on_submit() and form.text.data:
        doc1 = nlp(form.text.data)
        sentence = displacy.render(doc1, style="dep", page=False)

    return render_template('index.html', form=form, sentence=sentence)


app.run('0.0.0.0', os.environ.get('PORT', 5000))
