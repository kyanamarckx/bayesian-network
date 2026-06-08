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
├── 1-build/
│   ├── 1-notes.md
│   └── <...>
├── 2-learn/
│   ├── 2-notes.md
│   └── <...>
├── report/
│   └── <...>
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
<*to be added after completing the experiments*>


## :globe_with_meridians: 2 - Learn a Bayesian network with pyAgrum
In Task 2, sythetic datasets generated from the original Bayesian Network are used to investigate Bayesian Network learning algorithms available in pyAgrum.

Both search-and-score and constraint-based approaches are evaluated with respect to their ability to recover the original network structure. Additionally, the learned networks are compared with the original model and a Naive Bayes classifier in a classification setting.

### Main activities
- Generation of datasets with different sample sizes
- Structure learning using multiple algorithms
- Comparison of learned structures with the original network
- Classification experiments using Bayesian Networks
- Evaluation through ROC curves and Area Under the Curve (AUC) metrics

### Results
<*to be added after completing the experiments*>


## :blue_book: Report
The final report provides a detailed description of the modelling process, experimental methodology, obtained results, and conclusions. References used throughout the project are also documented there.