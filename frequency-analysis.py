from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv


STOPWORDS = set(stopwords.words("english"))


def write_counts(counts, filepath):
    with open(filepath, "w") as outfile:
        for word in counts.keys():
            to_write = word + " : " + str(counts[word]) + "\n"
            outfile.write(to_write)


def get_counts(text):
    tokens = word_tokenize(text)
    words = [word.lower() for word in tokens if word.isalpha()]
    words = [word for word in words if word not in STOPWORDS]

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    sorted_tuples = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    sorted_counts = {k: v for k, v in sorted_tuples}
    return sorted_counts


def read_tweet_texts(filepath):
    ids = []
    texts = []
    with open(filepath, newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter="~")
        for row in reader:
            ids.append(row[0])
            texts.append(row[1])

    return ids, texts


hashtags = ["#djokovic", "#djocovid", "#novaxdjocovid","#novaxdjokovic","#nolefam", "#westandwithnovak", "#istandwithnovak", "#djokovicout",  "#boycottaustralianopen"]
for tag in hashtags:
    ids, texts = read_tweet_texts(tag[1:] + ".csv")
    all_texts = " ".join(texts)
    write_counts(get_counts(all_texts), f"./final-results/{tag[1:]}.txt")
