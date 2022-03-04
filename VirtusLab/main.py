import pandas as pd
import sys

if sys.argv[1] == "join":
    f1 = pd.read_csv(sys.argv[2])
    f2 = pd.read_csv(sys.argv[3])

    try:
        if sys.argv[5] in ["inner", "left", "right"]:
            combined = pd.merge(f1, f2, on=sys.argv[4], how=sys.argv[5])
    except IndexError:
        combined = pd.merge(f1, f2, on=sys.argv[4], how="inner")

    print(combined)
    combined.to_csv("Output.csv")
else:
    print("Wrong command, try using:join file_path file_path column_name join_type")
