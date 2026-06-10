import pyagrum as agrum
import os



# PATHS
DATA_PATH = "2-learn/data"
OUTPUT_PATH = "2-learn/learned_networks"
os.makedirs(OUTPUT_PATH, exist_ok=True)



# ----- Score-based learning -----
def learn_score_based(csv_path, name):
    print(f"[Score-based] {name} samples")

    learner = agrum.BNLearner(csv_path)

    learner.useScoreBIC()
    learner.useGreedyHillClimbing()

    bn = learner.learnBN()

    out_path = os.path.join(OUTPUT_PATH, f"score_{name}.bif")
    agrum.saveBN(bn, out_path)
    print(f"\t Saved learned network to {out_path}\n")

    return bn


# ----- Constraint-based learning -----
def learn_constraint_based(csv_path, name):
    print(f"[Constraint-based] {name} samples")

    learner = agrum.BNLearner(csv_path)

    learner.useMIIC()

    bn = learner.learnBN()

    out_path = os.path.join(OUTPUT_PATH, f"constraint_{name}.bif")
    agrum.saveBN(bn, out_path)
    print(f"\t Saved learned network to {out_path}\n")

    return bn


# ----- All experiments -----
def run_all_experiments():
    for n, i in [(100, 1), (500, 2), (1000, 3)]:
        csv_path = os.path.join(DATA_PATH, f"structure_learning_{n}.csv")
        name = f"{n}"

        learn_score_based(csv_path, name)
        learn_constraint_based(csv_path, name)

        print(f"{i} - Completed learning for dataset with {n} samples.")



# Main execution
if __name__ == "__main__":
    run_all_experiments()
    print("4 - All structure learning experiments completed and networks saved in '2-learn/learned_networks' folder!")
