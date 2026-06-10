import pyagrum as agrum
import os



# PATH
path = "2-learn/data"
os.makedirs(path, exist_ok=True)


# Load original Bayesian Network
bn = agrum.loadBN("network/phishing_detection.bif")



# ----- Data generation function -----
def generate_samples(network, num_samples, seed=42):
    agrum.initRandom(seed)

    generator = agrum.BNDatabaseGenerator(network)
    generator.drawSamples(num_samples)

    df = generator.to_pandas()
    return df


# ----- Save datasets for structure learning -----
def save_structure_learning_datasets():
    for n in [100, 500, 1000]:
        df = generate_samples(bn, n)
        df.to_csv(f"{path}/structure_learning_{n}.csv", index=False)
        print(f"1 - Generated and saved structure learning dataset with {n} samples.")


# ----- Train/Test split for classification task -----
def save_train_test_datasets():
    df_train = generate_samples(bn, 1000, seed=123)
    df_test = generate_samples(bn, 100, seed=456)

    df_train.to_csv(f"{path}/train.csv", index=False)
    df_test.to_csv(f"{path}/test.csv", index=False)
    print("2 - Generated and saved train/test datasets for classification task.")



# Main execution
if __name__ == "__main__":
    save_structure_learning_datasets()
    save_train_test_datasets()

    print("3 - All datasets generated and saved in '2-learn/data' folder!")
