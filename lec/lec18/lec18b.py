f = open("C:\\Users\\satvi\\Desktop\\esc180\\lec\\lec18\\versedog.txt",
         encoding="latin1")

s = f.read()

"engineers rule the world".split(" ")

lines = s.split("\n")


def num_words(text):
    return len(text.split(" "))


def num_sentences(text):
    text = text.replace("!", ".")
    text = text.replace("?", ".")
    return len(text.split("."))


f = open("losttime.txt", encoding="latin1")
text = f.read()
print(num_words(text)/num_sentences(text))
