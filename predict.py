"""Deliberately broken: a test case for haggle's ship checks (Hour Detective). It has a syntax error, so the checks stop it before it ships."""

import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
def guess(:
    return train["hours_spent"].mean()
pd.DataFrame({"project_id": test["project_id"], "hours_spent": guess()}).to_csv("predictions.csv", index=False)
