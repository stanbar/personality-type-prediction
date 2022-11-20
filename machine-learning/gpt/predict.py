import os
import re
import string
from transformers import pipeline
from datasets import ClassLabel
import os
from pathlib import Path
from utils import clean_text

c2l = ClassLabel(names=[
                     "INTJ", "INTP", "ENTJ", "ENTP", 
                     "INFJ", "INFP", "ENFJ", "ENFP",
                     "ISTJ", "ISFJ", "ESTJ", "ESFJ",
                     "ISTP", "ISFP", "ESTP", "ESFP"])

classificator = pipeline("text-classification", model="./model", tokenizer="distilbert-base-uncased", framework="pt", top_k=16)

# base dataset path. You should place directories containing textes to be predicted.
dataset_path = str(Path.home())+ '/dataset/'

def collect_entries_for(directory_name: str):
    return [os.path.join(dirname, filename) \
            for dirname, _, filenames in os.walk(dataset_path + directory_name) \
             for filename in filenames]


def predict_for_texts(texts, verbose = False):
    for file_name in texts:
        lines = [line for line in [line.strip() for line in open(file_name).readlines()] if line]
        text = '\n'.join(lines) 
        text = str(clean_text(text));
        print(text)
        # split to batches of 512 tokens
        batch_size = 2048
        batches = [text[i:i+batch_size] for i in range(0, len(text), batch_size)]

        # predict
        predictions = {}
        for batch in batches:
            result = classificator(batch, padding=True)
            top_results = [(c2l.int2str(int(res['label'].removeprefix("LABEL_"))), res['score']) for res in result[0]]
            for label, score in top_results:
                if label not in predictions:
                    predictions[label] = 0
                predictions[label] += score

        print(file_name, sorted(predictions.items(), key=lambda item: item[1], reverse=True))


journals_texts = collect_entries_for('journals')

print("\n\n My journals:")
predict_for_texts(journals_texts)
