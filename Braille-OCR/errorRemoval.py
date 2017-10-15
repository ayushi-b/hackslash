from textblob import TextBlob
from textblob import Word


def error_removal():
    f = open("results.txt", "a+")
    with open("results.txt", "r") as fp:
        content = fp.read()
    blob = TextBlob(content)
    p = (blob.correct())
    open("results.txt", "w+")
    f.write(str(p))
    f.close()


