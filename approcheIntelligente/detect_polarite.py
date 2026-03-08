from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from read_corpus import read_corpus

patterns_neutres = [
    "rien à dire", "rien a dire", "correct", "ok", "normal",
    "ni bon ni mauvais", "simple", "acceptable", "moyen"
]

def detect_polarite(avis, aspect):
    avis_min = avis.lower()

    for p in patterns_neutres:
        if p in avis_min:
            return "neutre"

    blob = TextBlob(avis, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    polarite = blob.sentiment[0]

    if polarite > 0.02 :
        return "positif"
    elif polarite < -0.02:
        return "négatif"
    else:
        return "neutre"

def main():
    for i in range(1, 101):
        avis = read_corpus(f"../corpus/avis{i}.txt")
        res = detect_polarite(avis, "service")
        print(f"avis{i}: {res}")

if __name__ == "__main__":
    main()

