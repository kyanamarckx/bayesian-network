# :shark: Bayesian Network - Cybersecurity Phishing
> Kyana Marckx

This repository contains the work developed for the *Bayesian Reasoning &amp; Learning* course assignment. The project focuses on the design, analysis, and evaluation of Bayesian Networks using the Python library [pyAgrum](https://pyagrum.gitlab.io).

The chosen application domain is cybersecurity, with a particular focus on phishing email detection and risk assessment. A Bayesian Network is constructed to model how characteristics of an email and user behavior influence the likelihood of a phishing attack and its potential consequences.

The assignment consists of two main technical tasks:
1. Designing and analyzing a Bayesian Network based on expert knowledge
2. Learning Bayesian Network structures from data and evaluating their performance as classifiers

A final report summarizes the modelling decisions, experimental setup, results, and conclusions.

_____
### Repository structure
````text
bayesian-network
├── 0-installations/
│   └── 0-installations.ipynb
├── 1-build/
│   ├── 1-notes.md
│   ├── 01-buildBN.py
│   ├── 02-inferenceExperiments.py
│   └── figures/
│       ├── 1-BN_phishing_detection.jpg
│       └── 1-BN_phishing_detection.svg
├── 2-learn/
│   ├── 2-notes.md
│   ├── 01-generateData.py
│   ├── 02-structureLearning.py
│   ├── 03-structureEvaluation.py
│   ├── 04-classifierComparison.py
│   ├── data/
│   │   ├── structure_learning_100.csv
│   │   ├── structure_learning_500.csv
│   │   ├── structure_learning_1000.csv
│   │   ├── test.csv
│   │   └── train.csv
│   ├── learned_networks/
│   │   ├── constraint_100.bif
│   │   ├── constraint_500.bif
│   │   ├── constraint_1000.bif
│   │   ├── score_100.bif
│   │   ├── score_500.bif
│   │   └── score_1000.bif
│   ├── results/
│   │   └── structure_evaluation.csv
│   └── figures/
│       └── roc_comparison.png
├── network/
│   └── phishing_detection.bif
├── report/
│   └── Report_PhishingDetection-KyanaMarckx.pdf
└── README.md
````

_____
### Application domain: *Cybersecurity - Phishing Email Detection*
The Bayesian Network models how characteristics of an email and the cybersecurity awareness of a user infuence the probability that a phishing attack succeeds.

## :globe_with_meridians: 1 - Build a Bayesian network in pyAgrum
In Task 1, a Bayesian Network is manually designed to model phishing attacks. The network represents causal relationships between several factors, including sender reputation, email characteristics, user awareness, and the risk of account compromise.

The objective is to construct a realistic probabilistic model, define its structure and parameters, and validate the resulting behavior through probabilistic inference.

### Main activities
- Definition of the problem scope and modelling objectives
- Selection of relevant variables and their possible states
- Construction of the Bayesian Network structure based on causal assumptions
- Definition of conditional probability tables (CPTs)
- Validation of the model through inference and probability analysis

### Results
The Bayesian Network was evaluated through a series of probabilistic inference experiments to validate its behavior under different phishing scenarios.

Key findings include:
- The prior probability of an email being classified as phishing is approximately **19.31%**
- Introducing a suspicious sender increases this probability to **50.92%**
- When all phishing indicators are present simultaneously, the probability rises to **95%**
- User awareness strongly influences behaviour:
  - High awareness leads to a **60%** click probability in phishing scenarios
  - Low awareness increases this to **90%**
- In a full end-to-end attack scenario, the probability of account compromise reaches **61.03%**

These results confirm that the model behaves consistently with expected cybersecurity behavior: phishing indicators increase risk, while user awareness mitigates it. The probabilistic dependencies in the network successfully propagate risk from email characteristics to user actions and final security outcomes.


## :globe_with_meridians: 2 - Learn a Bayesian network in pyAgrum
In Task 2, sythetic datasets generated from the original Bayesian Network are used to investigate Bayesian Network learning algorithms available in pyAgrum.

Both search-and-score and constraint-based approaches are evaluated with respect to their ability to recover the original network structure. Additionally, the learned networks are compared with the original model and a Naive Bayes classifier in a classification setting.

### Main activities
- Generation of datasets with different sample sizes
- Structure learning using multiple algorithms
- Comparison of learned structures with the original network
- Classification experiments using Bayesian Networks
- Evaluation through ROC curves and Area Under the Curve (AUC) metrics

### Results
Task 2 investigates both structure learning and classification performance of Bayesian Networks using synthetic data generated from the original phishing detection model.

#### Structure learning results
Two structure learning approaches were evaluated: a search-and-score method (greedy hill climbing with BIC scoring) and a constraint-based dependency learning approach (MICC). Both methods were tested on datasets of increasing size (100, 500, and 1000 samples).

The results show a clear influence of sample size on structure recovery. Smaller datasets lead to incomplete or noise network structures, while larger datasets significantly improve recovery of the original dependencies. The search-and-score approach generally achieved more stable and accurate reconstructions compared to the constraint-based method.

#### Classification results
Three models were compared in a classification setting:
- The original manually designed Bayesian Network
- A learned Bayesian Network (constraint-based, 500 samples)
- A Naive Bayes classifier

Performance was evaluated using ROC curves and AUC scores on a held-out test set.

Final AUC results:
| Setting | AUC |
| :--- | :---: |
| Original BN | 0.155 |
| Learned BN | 0.846 |
| Naive Bayes | 0.967 |

The learned Bayesian Network significantly improves over the original model in predictive performance, indicating that structure learning captues useful dependencies from data. Surprisingly, the Naive Bayes classifier achieved the highest AUC, suggesting that despite its strong independence assumptions, it performs very well in this classification task due to the relatively strong signal in the features.


## :blue_book: Report
The final report provides a detailed description of the modelling process, experimental methodology, obtained results, and conclusions. References used throughout the project are also documented there.