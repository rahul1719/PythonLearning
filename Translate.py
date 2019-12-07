from textblob import TextBlob


def trans(sentence):
    blob = TextBlob(sentence);
    print("input language : " + blob.detect_language())
    return blob.translate(to="fr");


user_input = input("User input: ")
transVal = trans(user_input)
print("Translation in French: %s" % transVal)
