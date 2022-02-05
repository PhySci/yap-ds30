import pandas as pd

def main():
    df = pd.read("1.csv")
    df = df.drop("id", axis=1)
    df.rename(columns={"age": "Age"}, inplace=True)
    df.set_index("Age", inplace=True)
    return df

if __name__ == "__main__":
    main()
