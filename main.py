import pandas as pd

def main():
    df = pd.read("1.csv")
    df = df.drop("id", axis=1)
    df.set_index("age", inplace=True)
    return df

if __name__ == "__main__":
    main()
