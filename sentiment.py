from textblob import TextBlob
wiki = TextBlob("Avishek is very very angry")
print(wiki.words)
print(wiki.sentiment.polarity)