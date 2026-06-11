import pyagrum as agrum
import pyagrum.skbn as skbn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import roc_curve, auc



# PATHS
TRAIN_PATH = "2-learn/data/train.csv"
TEST_PATH = "2-learn/data/test.csv"

ORIGINAL_BN_PATH = "network/phishing_detection.bif"
LEARNED_BN_PATH = "2-learn/learned_networks/constraint_500.bif" # This was, together with constraint_1000, the best one


# Load data
def load_data(path):
    return pd.read_csv(path)



# ----- Convert BN inference to probability scores -----
def predict_proba_bn(bn, df):
    ie = agrum.LazyPropagation(bn)

    probabilities = []

    for _, row in df.iterrows():
        ie.setEvidence({
            "SenderReputation": row["SenderReputation"],
            "EmailGrammar": row["EmailGrammar"],
            "ContainsLinks": row["ContainsLinks"],
            "UrgencyLanguage": row["UrgencyLanguage"]
        })

        ie.makeInference()

        prob = ie.posterior("PhishingEmail")[1] # Probability of "yes"
        probabilities.append(prob)

    return np.array(probabilities)


# ----- Naive Bayes classifier (pyAgrum BNClassifier) -----
def train_naive_bayes(train_df):
    clf = skbn.BNClassifier(learningMethod="MIIC")
    X = train_df.drop(columns=["PhishingEmail"])
    y = train_df["PhishingEmail"].values
    clf.fit(X, y)
    return clf

def predict_naive(clf, df):
    X = df.drop(columns=["PhishingEmail"])
    probabilities = clf.predict_proba(X)
    return np.array([prob[1] for prob in probabilities]) # Probability of "yes"


# ----- ROC evaluation -----
def evaluate_model(y_true, y_score, label):
    fpr, tpr, _ = roc_curve(y_true, y_score)
    auc_score = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f"{label} (AUC = {auc_score:.3f})")
    return auc_score


# ----- Main -----
def main():
    train = load_data(TRAIN_PATH)
    test = load_data(TEST_PATH)

    y_true = (test["PhishingEmail"] == "yes").astype(int)

    # Load models
    original_bn = agrum.loadBN(ORIGINAL_BN_PATH)
    learned_bn = agrum.loadBN(LEARNED_BN_PATH)

    # Predictions
    print("1 - Predicting original BN...")
    orig_scores = predict_proba_bn(original_bn, test)

    print("2 - Predicting learned BN...")
    learned_scores = predict_proba_bn(learned_bn, test)

    print("3 - Training Naive Bayes classifier...")
    nb_clf = train_naive_bayes(train)

    print("4 - Predicting Naive Bayes classifier...")
    nb_scores = predict_naive(nb_clf, test)

    # Compute ROC curves
    plt.figure(figsize=(10, 8))

    auc_orig = evaluate_model(y_true, orig_scores, "Original BN")
    auc_learned = evaluate_model(y_true, learned_scores, "Learned BN")
    auc_nb = evaluate_model(y_true, nb_scores, "Naive Bayes")

    plt.plot([0, 1], [0, 1], "k--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve Comparison for Phishing Email Detection")
    plt.legend(loc="lower right")

    plt.savefig("2-learn/figures/roc_comparison.png")
    plt.show()

    # Print AUC scores
    print("\n----- AUC Scores -----")
    print(f"Original BN: {auc_orig:.3f}")
    print(f"Learned BN: {auc_learned:.3f}")
    print(f"Naive Bayes: {auc_nb:.3f}")

    # Save AUC scores to CSV
    auc_scores = pd.DataFrame({
        "Model": ["Original BN", "Learned BN", "Naive Bayes"],
        "AUC": [auc_orig, auc_learned, auc_nb]
    })
    auc_scores.to_csv("2-learn/results/auc_scores.csv", index=False)
    

if __name__ == "__main__":
    main()
    print("5 - Classification comparison completed and ROC curve saved in '2-learn/figures/roc_comparison.png'!")
