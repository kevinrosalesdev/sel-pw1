import pandas as pd


def classify(data: pd.DataFrame, rules):
    results = []
    for idx in range(data.shape[0]):
        found = False
        for rule in rules:
            if all([data.loc[idx, cond[0]] == cond[1] for cond in rule[0]]):
                results.append(rule[1][1])
                found = True
                break
        if not found:
            results.append(False)
    return results
