# :globe_with_meridians: NOTES - Learn a Bayesian Network in pyAgrum

## Objective
The goal of this task is to evaluate Bayesian Network learning algorithms and compare their ability to recover the original network structure. Additionally, the learned models are assessed in a classification setting.


## Data generation
Synthetic datasets were generated from the original Bayesian Network using pyAgrum's sampling methods. Three dataset sizes were used:
- 100 samples
- 500 samples
- 1000 samples

Additionally, a separate train/test split (100/100) was created for classification experiments.


## Structure learning methods
Two structure learning approaches were applied:

### 1. Search-and-score (Greedy Hill Climbing + BIC)
This method searches the space of possible network structures and optimizes a scoring function (BIC) to find he best-fitting graph.

### 2. Constraint-based learning (MIIC)
A dependency-based method that infers network structure based on mutual information between variables.


## Evaluation of structure learning
The learned networks were compared to the original Bayesian Network by analyzing:
- Correctly recovered edges
- Missing edges
- Additional incorrect edges

This allowed an assessment of how well each algorithm reconstructs the true dependency structure as a function of sample size.


## Classification experiment
Three classifiers were evaluated:
- Original Bayesian Network (expert-defined structure)
- Learned Bayesian Network (best-performing learned model: constraint-based, 500 samples (or 1000 samples is also possible since it had the same values in structure evaluation))
- Naive Bayes classifier (baseline model)

### Class variable
- ``PhishingEmail``

### Features
- ``SenderReputation``
- ``EmailGrammar``
- ``ContainsLinks``
- ``UrgencyLanguage``


## Evaluation metric
Classification performance was evaluated using:
- ROC curves
- Area Under the Curve (AUC)


## Results summary
- Structure learning performance improves with increasing sample size.
- Constraint-based learning provides more stable and accurate structures than score-based learning.
- Naive Bayes achieves the best classification performance despite its independence assumptions.
