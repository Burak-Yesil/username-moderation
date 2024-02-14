from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL) 

def sentiment_analysis(text):
   #Usage: tests whether or not a comment or username is negative or positive 
   #Background: Were are using the roberta twitter model trained on 58M tweets
   encoded_text = tokenizer(text, return_tensors='pt')
   scores = softmax(model(**encoded_text)[0][0].detach().numpy())
   print("Sentiment Result: ", {
    'negative': scores[0],
    'neutral': scores[1],
    'positive': scores[2]
    })
   res = composite_score({
    'negative': scores[0],
    'neutral': scores[1],
    'positive': scores[2]
    }, .1)
   return res == 'positive'

def composite_score(d, lamb):
   #Usage: tune the impact the neutral score has on the final result
   print("Calculating composite score...")
   score =  d['negative'] - (d['positive'] + (lamb * d['neutral']))
   if score < 0:
      return 'positive'
   return 'negative'

