from itertools import combinations, product
import pandas as pd
import numpy as np


def find_all_selectors(nci: pd.DataFrame):
    selectors = []
    for attribute in range(nci.shape[1]):
        values = nci.iloc[:, attribute].unique()
        selectors.append([(nci.columns[attribute], value) for value in values])

    return np.array(selectors)


def form_conditions(selectors, n_combinations, n_attributes):
    conditions = []
    for possible_comb in combinations(list(range(n_attributes)), n_combinations):
        conditions.extend(list(product(*selectors[list(possible_comb)])))

    return conditions


def study_condition(condition, dataset: pd.DataFrame):
    filters = dataset[condition[0][0]] == condition[0][1]
    for idx in range(1, len(condition)):
        filters &= dataset[condition[idx][0]] == condition[idx][1]

    filtered_samples = dataset[filters]
    labels = filtered_samples.iloc[:, -1].unique()
    # If all instances satisfying the condition belong to the same class
    if len(labels) == 1:
        return (dataset.columns[-1], labels[0]), filtered_samples.index

    return [False, False]


def RULES_algorithm(dataset: pd.DataFrame):
    nci = dataset.copy()
    rules = []
    n_combinations = 1
    while n_combinations <= dataset.shape[1]-1 and nci.shape[0] != 0:
        selectors = find_all_selectors(nci.iloc[:, :-1])
        candidates = form_conditions(selectors, n_combinations, dataset.shape[1]-1)
        for condition in candidates:
            label, indexes = study_condition(condition, dataset)
            if label:
                rules.append((condition, label, len(indexes)/dataset.shape[0]))
                nci.drop(indexes, inplace=True, errors='ignore')

        n_combinations += 1

    for idx in range(nci.shape[0]):
        rule = []
        for attribute in range(nci.shape[1]-1):
            rule.append((nci.columns[attribute], nci.iloc[idx, attribute]))
        rules.append((tuple(rule), (nci.columns[-1], nci.iloc[idx, -1]), 1/dataset.shape[0]))

    return rules
