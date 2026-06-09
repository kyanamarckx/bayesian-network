import pyagrum as agrum
import pyagrum.lib.image as agrum_img



# Create Bayesian Network
bn = agrum.BayesNet("PhishingDetection")


# ----- Variables -----
sender = bn.add(agrum.LabelizedVariable(
    "SenderReputation",
    "Sender Reputation",
    ["good", "suspicious"]
))

grammar = bn.add(agrum.LabelizedVariable(
    "EmailGrammar",
    "Grammar quality",
    ["good", "poor"]
))

links = bn.add(agrum.LabelizedVariable(
    "ContainsLinks",
    "Contains hyperlinks",
    ["yes", "no"]
))

urgency = bn.add(agrum.LabelizedVariable(
    "UrgencyLanguage",
    "Urgency language",
    ["yes", "no"]
))

phishing = bn.add(agrum.LabelizedVariable(
    "PhishingEmail",
    "Is phishing email",
    ["yes", "no"]
))

awareness = bn.add(agrum.LabelizedVariable(
    "UserAwareness",
    "User awareness in cybersecurity",
    ["high", "low"]
))

click = bn.add(agrum.LabelizedVariable(
    "ClickLink",
    "User clicks link",
    ["yes", "no"]
))

compromised = bn.add(agrum.LabelizedVariable(
    "AccountCompromised",
    "Account compromised",
    ["yes", "no"]
))


# ----- Arcs -----
bn.addArc(sender, phishing)
bn.addArc(grammar, phishing)
bn.addArc(links, phishing)
bn.addArc(urgency, phishing)

bn.addArc(phishing, click)
bn.addArc(awareness, click)

bn.addArc(click, compromised)

print("1 - Bayesian Network check:", bn)


# ----- Priors -----
bn.cpt("SenderReputation").fillWith([0.80, 0.20])
bn.cpt("EmailGrammar").fillWith([0.85, 0.15])
bn.cpt("ContainsLinks").fillWith([0.60, 0.40])
bn.cpt("UrgencyLanguage").fillWith([0.30, 0.70])

bn.cpt("UserAwareness").fillWith([0.60, 0.40])


# ----- ClickLink CPT -----
bn.cpt("ClickLink")[{
    "PhishingEmail": "yes",
    "UserAwareness": "low"
}] = [0.90, 0.10]

bn.cpt("ClickLink")[{
    "PhishingEmail": "yes",
    "UserAwareness": "high"
}] = [0.60, 0.40]

bn.cpt("ClickLink")[{
    "PhishingEmail": "no",
    "UserAwareness": "low"
}] = [0.30, 0.70]

bn.cpt("ClickLink")[{
    "PhishingEmail": "no",
    "UserAwareness": "high"
}] = [0.05, 0.95]


# ----- AccountCompromised CPT -----
bn.cpt("AccountCompromised")[{
    "ClickLink": "yes"
}] = [0.70, 0.30]

bn.cpt("AccountCompromised")[{
    "ClickLink": "no"
}] = [0.01, 0.99]


# ----- PhishingEmail CPT -----
phishing_probs = {
    ("good", "good", "no", "no"): 0.01,
    ("good", "good", "no", "yes"): 0.05,
    ("good", "good", "yes", "no"): 0.10,
    ("good", "good", "yes", "yes"): 0.25,

    ("good", "poor", "no", "no"): 0.05,
    ("good", "poor", "no", "yes"): 0.15,
    ("good", "poor", "yes", "no"): 0.25,
    ("good", "poor", "yes", "yes"): 0.45,

    ("suspicious", "good", "no", "no"): 0.20,
    ("suspicious", "good", "no", "yes"): 0.40,
    ("suspicious", "good", "yes", "no"): 0.55,
    ("suspicious", "good", "yes", "yes"): 0.75,

    ("suspicious", "poor", "no", "no"): 0.50,
    ("suspicious", "poor", "no", "yes"): 0.70,
    ("suspicious", "poor", "yes", "no"): 0.80,
    ("suspicious", "poor", "yes", "yes"): 0.95
}

for (sender_val, grammar_val, links_val, urgency_val), prob in phishing_probs.items():
    bn.cpt("PhishingEmail")[{
        "SenderReputation": sender_val,
        "EmailGrammar": grammar_val,
        "ContainsLinks": links_val,
        "UrgencyLanguage": urgency_val
    }] = [prob, 1 - prob]


# ----- Save the Bayesian Network -----
agrum.saveBN(bn, "network/phishing_detection.bif")
print("2 - Bayesian Network saved as 'phishing_detection.bif' inside 'network' folder!")



# First validation
ie = agrum.LazyPropagation(bn)
ie.makeInference()

print("3 - Prior probability of phishing email:", ie.posterior("PhishingEmail"))


# Second validation with evidence (extreme case)
ie.setEvidence({
    "SenderReputation": "suspicious",
    "EmailGrammar": "poor",
    "ContainsLinks": "yes",
    "UrgencyLanguage": "yes",
})
ie.makeInference()

print("4 - Posterior probability of phishing email with strong evidence:", ie.posterior("PhishingEmail"))


# Visualize the Bayesian Network
agrum_img.export(bn, "1-build/figures/1-BN_phishing_detection.svg")
print("5 - Bayesian Network visualized and saved as '1-BN_phishing_detection.svg' inside '1-build/figures' folder!")
