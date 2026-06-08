# :globe_with_meridians: NOTES -  Build a Bayesian Network in pyAgrum

## Network Structure
<*TODO*>

## Variable Descriptions
<*TODO*>

## CPTs
### SenderReputation
> Most emails are not phishing emails 

| P(SenderReputation) |  |
| :--- | :---: |
| good | 0.80 |
| suspicious | 0.20 |

### EmailGrammar
> Phishing emails are more likely to contain grammatical error

| P(EmailGrammar) |  |
| :--- | :---: |
| good | 0.85 |
| poor | 0.15 |

### ContainsLinks
> A lot of emails already contain links (also the legit ones)

| P(ContainsLinks) |  |
| :--- | :---: |
| yes | 0.60 |
| no | 0.40 |

### UrgencyLanguage
> Urgency is a typical phishing-signal, but this is not always present

| P(UrgencyLanguage) |  |
| :--- | :---: |
| yes | 0.30 |
| no | 0.70 |

### PhishingEmail
| SenderReputation | EmailGrammar | ContainsLinks | UrgencyLanguage | P(PhishingEmail=yes) |
| :--- | :--- | :--- | :--- | :---: |
| good | good | no | no | 0.01 |
| good | good | no | yes | 0.05 |
| good | good | yes | no | 0.10 |
| good | good | yes | yes | 0.25 |
| good | poor | no | no | 0.05 |
| good | poor | no | yes | 0.15 |
| good | poor | yes | no | 0.25 |
| good | poor | yes | yes | 0.45 |
| suspicious | good | no | no | 0.20 |
| suspicious | good | no | yes | 0.40 |
| suspicious | good | yes | no | 0.55 |
| suspicious | good | yes | yes | 0.75 |
| suspicious | poor | no | no | 0.50 |
| suspicious | poor | no | yes | 0.70 |
| suspicious | poor | yes | no | 0.80 |
| suspicious | poor | yes | yes | 0.95 |

### UserAwareness
| P(UserAwareness) |  |
| :--- | :---: |
| high | 0.60 |
| low | 0.40 |

### ClickLink
| PhishingEmail | UserAwareness | P(ClickLink=yes) |
| :--- | :--- | :---: |
| yes | low | 0.90 |
| yes | high | 0.60 |
| no | low | 0.30 |
| no | high | 0.05 |

### AccountCompromised
| ClickLink | P(UrgencyLanguage=yes) |
| :--- | :---: |
| yes | 0.70 |
| no | 0.01 |


## Assumptions
<*TODO*>
