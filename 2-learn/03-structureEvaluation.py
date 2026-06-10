import pyagrum as agrum
import pandas as pd
import os



# PATHS
ORIGINAL_BN_PATH = "network/phishing_detection.bif"
LEARNED_PATH = "2-learn/learned_networks"

OUTPUT_PATH = "2-learn/results"
os.makedirs(OUTPUT_PATH, exist_ok=True)


# Load BN
def load_bn(path):
    return agrum.loadBN(path)



# ----- Extract edges as sets -----
def get_edges(bn):
    return set([(a, b) for a, b in bn.arcs()])


# ----- Compare two networks -----
def compare_graphs(original_bn, learned_bn):
    original_edges = get_edges(original_bn)
    learned_edges = get_edges(learned_bn)

    correct = original_edges.intersection(learned_edges)
    missing = original_edges - learned_edges
    extra = learned_edges - original_edges

    return len(correct), len(missing), len(extra)


# ----- Evaluate all learned networks -----
def run_evaluation():
    original_bn = load_bn(ORIGINAL_BN_PATH)

    results = []
    
    configs = [
        ("score_100", "Score-Based", 100),
        ("score_500", "Score-Based", 500),
        ("score_1000", "Score-Based", 1000),
        ("constraint_100", "Constraint-Based", 100),
        ("constraint_500", "Constraint-Based", 500),
        ("constraint_1000", "Constraint-Based", 1000)
    ]

    for name, algo, size in configs:
        path = os.path.join(LEARNED_PATH, f"{name}.bif")
        learned_bn = load_bn(path)

        correct, missing, extra = compare_graphs(original_bn, learned_bn)

        results.append({
            "Model": name,
            "Algorithm": algo,
            "Samples": size,
            "Correct Edges": correct,
            "Missing Edges": missing,
            "Extra Edges": extra
        })

        print(f"{name}: correct={correct}, missing={missing}, extra={extra}")

    # Save results to CSV
    df = pd.DataFrame(results)
    output_file = os.path.join(OUTPUT_PATH, "structure_evaluation.csv")
    df.to_csv(output_file, index=False)

    print(f"1 - Evaluation results saved to {output_file}")

    print("----- SUMMARY -----")
    print(df)



# Main execution
if __name__ == "__main__":
    run_evaluation()
    print("2 - Structure evaluation completed and results saved in '2-learn/results/structure_evaluation.csv'!")
