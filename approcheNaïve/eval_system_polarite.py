from detect_polarite import detect_polarite
import pandas as pd
import os
from sklearn.metrics import classification_report, confusion_matrix

def eval_system_polarite(fileCsv , aspect):
    df = pd.read_csv(fileCsv)

    y_true = []
    y_pred = []
    for _,row in df.iterrows():
        
        file_name=row["texte"]
        with open(os.path.join('../corpus/',file_name)) as f :
            avis = f.read().lower()

        true_labels = row[aspect]
        y_true.append(true_labels)

        pred_labels = detect_polarite(avis, aspect)
        y_pred.append(pred_labels.get(aspect))

    return y_true , y_pred

def main():
    y_true, y_pred = eval_system_polarite("../corpus/goldStandard.csv","service")
    print("y_true:", (y_true))
    print("y_pred:", (y_pred))

    cm = confusion_matrix(y_true, y_pred,labels=['positif','négatif','neutre'])


    print("matrice de confusion: \n ", cm)

    print("\n========= Rapport de classification globale ==========")
    print(classification_report(y_true, y_pred, labels=["positif", "négatif", "neutre"],
                                zero_division=0))

    '''
    precision_positif = precision_score(y_true, y_pred, labels=["positif"], average=None)[0]
    recall_positif = recall_score(y_true, y_pred, labels=["positif"], average=None)[0]
    f1_positif = f1_score(y_true, y_pred, labels=["positif"], average=None)[0]

    precision_negatif = precision_score(y_true, y_pred, labels=["négatif"], average=None)[0]
    recall_negatif = recall_score(y_true, y_pred, labels=["négatif"], average=None)[0]
    f1_negatif = f1_score(y_true, y_pred, labels=["négatif"], average=None)[0]

    precision_neutre = precision_score(y_true, y_pred, labels=["neutre"], average=None)[0]
    recall_neutre = recall_score(y_true, y_pred, labels=["neutre"], average=None)[0]
    f1_neutre = f1_score(y_true, y_pred, labels=["neutre"], average=None)[0]

    # Affichage des métriques
    print(f"Classe Positif: Précision = {precision_positif:.2f}, Rappel = {recall_positif:.2f}, F1 = {f1_positif:.2f}")
    print(f"Classe Négatif: Précision = {precision_negatif:.2f}, Rappel = {recall_negatif:.2f}, F1 = {f1_negatif:.2f}")
    print(f"Classe Neutre: Précision = {precision_neutre:.2f}, Rappel = {recall_neutre:.2f}, F1 = {f1_neutre:.2f}")
    '''

if __name__ == "__main__":
    main()