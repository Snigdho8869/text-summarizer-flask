from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import torch
from transformers import BartForConditionalGeneration, BartTokenizer, T5ForConditionalGeneration, T5Tokenizer, GPT2LMHeadModel,GPT2Tokenizer


app = Flask(__name__, template_folder='templates', static_folder='static')


models = {
    'bart': BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn'),
    'gpt': GPT2LMHeadModel.from_pretrained('gpt2'),
}

tokenizers = {
    'bart': BartTokenizer.from_pretrained('facebook/bart-large-cnn'),
    'gpt': GPT2Tokenizer.from_pretrained('gpt2'),
}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/text-summarizer', methods=['POST'])
def text_summarizer():
    def summarize_text(text, models, tokenizers):
        summaries = []
        for model_name, model in models.items():
            tokenizer = tokenizers[model_name]
            length_penalty = 2.0
            num_beams = 3
            max_length = 1024
            min_length = max(round(0.33 * len(text.split())), 10)
            input_ids = tokenizer.encode(text, return_tensors='pt', max_length=max_length, truncation=True)
            summary_ids = model.generate(input_ids,
                                      num_beams=num_beams,
                                      length_penalty=length_penalty,
                                      max_length=max_length,
                                      min_length=min_length,
                                      early_stopping=True,
                                      pad_token_id=tokenizer.eos_token_id,
                                      attention_mask=input_ids.new_ones(input_ids.shape))
            summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            summaries.append(summary)
        return summaries
    
    text = request.json['text']
   
    summaries = summarize_text(text, models, tokenizers)
    combined_summary = max(set(summaries), key=summaries.count)
    
    response = jsonify({'summarizeText': combined_summary})
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)