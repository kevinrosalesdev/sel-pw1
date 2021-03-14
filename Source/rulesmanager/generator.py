from itertools import combinations
import pandas as pd


def find_all_selectors(nci: pd.DataFrame):
    selectors = []
    for attribute in range(nci.shape[1]):
        values = nci.iloc[:, attribute].unique()
        for value in values:
            selectors.append((nci.columns[attribute], value))
    return selectors


def form_conditions(selectors, n_combinations):
    conditions = list(combinations(selectors, n_combinations))
    imp_conditions = []
    for idx, condition in enumerate(conditions):
        for idx_c in range(1, len(condition)):
            if condition[idx_c][0] == condition[idx_c-1][0]:
                imp_conditions.append(idx)
                break
    for index in sorted(imp_conditions, reverse=True):
        del conditions[index]
    return conditions


def RULES_algorithm(dataset: pd.DataFrame):
    n_combinations = 4
    rules = []
    nci = dataset.copy()
    while n_combinations <= dataset.shape[1]-1 and nci.shape[0] != 0:
        selectors = find_all_selectors(nci.iloc[:, :-1])
        conditions = form_conditions(selectors, n_combinations)
        # TODO: For each condition...
        n_combinations += 1
    # TODO: For each unclassified instance...
    return rules
