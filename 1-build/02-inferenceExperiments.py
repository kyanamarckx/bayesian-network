import pyagrum as agrum



# Load the Bayesian Network from the previous step
bn = agrum.loadBN("network/phishing_detection.bif")


# ----- Experiment 1: Prior probability of Phishing (no evidence) -----
ie = agrum.LazyPropagation(bn)
ie.makeInference()

print("1 - Prior probability of phishing email:", ie.posterior("PhishingEmail"))


# ----- Experiment 2: Suspicious sender
ie = agrum.LazyPropagation(bn)
ie.setEvidence({
    "SenderReputation": "suspicious"
})
ie.makeInference()
print("2 - Posterior probability of phishing email with suspicious sender:", ie.posterior("PhishingEmail"))


# ----- Experiment 3: Multiple phishing indicators
ie = agrum.LazyPropagation(bn)
ie.setEvidence({
    "SenderReputation": "suspicious",
    "EmailGrammar": "poor",
    "ContainsLinks": "yes",
    "UrgencyLanguage": "yes",
})
ie.makeInference()
print("3 - Posterior probability of phishing email with multiple indicators (all warning signs):", ie.posterior("PhishingEmail"))


# ----- Experiment 4: Effect of user awareness on ClickLink -----
ie = agrum.LazyPropagation(bn)
ie.setEvidence({
    "PhishingEmail": "yes",
    "UserAwareness": "high"
})
ie.makeInference()
print("4.1 - Probability of clicking a link in a phishing email with high user awareness:", ie.posterior("ClickLink"))

ie = agrum.LazyPropagation(bn)
ie.setEvidence({
    "PhishingEmail": "yes",
    "UserAwareness": "low"
})
ie.makeInference()
print("4.2 - Probability of clicking a link in a phishing email with low user awareness:", ie.posterior("ClickLink"))


# ----- Experiment 5: End-to-end attack scenario -----
ie = agrum.LazyPropagation(bn)
ie.setEvidence({
    "SenderReputation": "suspicious",
    "EmailGrammar": "poor",
    "ContainsLinks": "yes",
    "UrgencyLanguage": "yes",
    "UserAwareness": "low"
})
ie.makeInference()
print("5 - End-to-end attack scenario (all warning signs + low user awareness = high-risk phishing scenario):", ie.posterior("AccountCompromised"))
