from flask import Flask, render_template, request
import os
import torch
from transformers import BartForConditionalGeneration, BartTokenizer

app = Flask(__name__, template_folder='templates', static_folder='static')

model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        if len(text.split()) > 1024:
            return render_template('index.html', summary="Input text must be less than 1024 tokens.")
        else:
            summary = summarize_text(text)
            return render_template('index.html', text=text, summary=summary)
    else:
        return render_template('index.html')

def summarize_text(text):
    input_ids = tokenizer.encode(text, return_tensors='pt', max_length=1024)
    summary_ids = model.generate(input_ids, num_beams=4, length_penalty=2.0, max_length=512, min_length=0, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

if __name__ == '__main__':
    app.run(debug=True)
