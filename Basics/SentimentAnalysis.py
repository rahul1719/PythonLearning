from textblob import TextBlob

testimonial = TextBlob("i like black color")
print(testimonial.sentiment_assessments)
