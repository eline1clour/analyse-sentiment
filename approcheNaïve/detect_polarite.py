import nltk
from read_corpus import read_corpus

aspect_polarite = {
   "positif": [
        "bon", "qualité",  "super", 
        "bien", "aimable", "rapide", "accueillant", "agréable", "réactif", "parfait",  
        "souriant", "gentil", "top"
    ],
    "négatif": [
        "frustrant", "médiocre", "lent", "désabusé", 
        "déplorable", "long", "nul", "attente", "méchant", "incapable", "catastrophe", "mauvais", "irresponsable"
    ]
}

def detect_polarite(avis, aspect):
    res = {}

    avis_tokens = nltk.word_tokenize(avis.lower())  

    polarite_score = 0

    for mot in avis_tokens:
        if mot in aspect_polarite["négatif"]:
            polarite_score -= 1
        elif mot in aspect_polarite["positif"]:
            polarite_score += 1

    if polarite_score > 0:
        res[aspect] = "positif"
    elif polarite_score < 0:
        res[aspect] = "négatif"
    else:
        res[aspect] = "neutre" 
        
    return res

def main():
    for i in range(1, 101):
        avis = read_corpus(f"../corpus/avis{i}.txt")
        res = detect_polarite(avis, "service")
        print(f"avis{i}: {res}")

if __name__ == "__main__":
    main()

