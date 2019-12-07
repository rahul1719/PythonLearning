from textblob import TextBlob


def trans(sentence):
    blob = TextBlob(sentence);
    return blob.translate(to="fr");
