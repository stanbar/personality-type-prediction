# MBTI prediction
This repository combines multiple MBTI prediction algorithms.

1. Naive Bayes Classifier from [TGDivy/MBTI-Personality-Classifier](https://github.com/TGDivy/MBTI-Personality-Classifier/blob/master/MBTI%20personality%20classifier.ipynb).
2. TF-IDF Logistic Regression Model from [esharma3/myers-briggs-personality-prediction](https://github.com/esharma3/myers-briggs-personality-prediction).
3. RNN from [ianscottknight/Predicting-Myers-Briggs-Type-Indicator-with-Recurrent-Neural-Networks](https://github.com/ianscottknight/Predicting-Myers-Briggs-Type-Indicator-with-Recurrent-Neural-Networks).
4. BERT

Prerequisitions:
1. Download MBTI dataset from https://www.kaggle.com/datasets/datasnaek/mbti-type and save `mbti_1.csv` into `/data`.
2. Create dataset directory at `mkdir ~/dataset/`, and place there your datasets you want to predict, e.g. all texts written by Tim Ferriss should be placed at `~/dataset/ferriss/`.


TODO:
- [ ] Extract common code, like cleaning and other preprocessing steps.
- [ ] Compare the methods.

## Naive Bayes Classifier
It's basically fork of [TGDivy/MBTI-Personality-Classifier](https://github.com/TGDivy/MBTI-Personality-Classifier/blob/master/MBTI%20personality%20classifier.ipynb), but using cognitive functions instead of MBTI letters.

To run the prediction
1. Enter the virtual environment `pipenv shell`.
2. If it's your first time install deps with `pipenv install`.
3. Run jupyter-lab `jupyter-lab` and continute in your browser.
4. Execute both training and prediction using the `naive-bayes-classifier.ipynb` notebook.

TODO:
- [ ] Save the model into a file.
- [ ] Split the training and predicting into separate files.

## TF-IDF Logistic Regression Model
This model uses TF-IDF (term frequency–inverse document frequency) which is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.
The model is taken from [esharma3/myers-briggs-personality-prediction](https://github.com/esharma3/myers-briggs-personality-prediction).


The repository already contains trained models at `/models`; if you want to retrain:
1. Enter the virtual environment `pipenv shell`.
2. If it's your first time install deps with `pipenv install`.
2. Run jupyter-lab `jupyter-lab`, continute in browser.
3. Open `tf-idf/models.ipynb` notebook to train the models. Models will be saved to `/models` directory.

Predict:
1. Enter the virtual environment `pipenv shell`.
2. If it's your first time install deps with `pipenv install`.
3. Execute `predict.py` to predict.

TODO:
- [ ] Add congnitive functions into features list.

## RNN

This is an approach based on [ianscottknight/Predicting-Myers-Briggs-Type-Indicator-with-Recurrent-Neural-Networks](https://github.com/ianscottknight/Predicting-Myers-Briggs-Type-Indicator-with-Recurrent-Neural-Networks).

`rnn/README.md` describes the steps to train and run the prediction.

 ## BERT

This is an approach based on [MLH-Fellowship/Social-BERTerfly](https://github.com/MLH-Fellowship/Social-BERTerfly/tree/main/server).


`bert/README.md` describes the steps to train and run the prediction.

