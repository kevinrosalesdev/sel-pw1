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


def study_condition(condition, dataset: pd.DataFrame, label=None):
    filters = dataset[condition[0][0]] == condition[0][1]
    for idx in range(1, len(condition)):
        filters &= dataset[condition[idx][0]] == condition[idx][1]

    filtered_samples = dataset[filters]
    labels = filtered_samples.iloc[:, -1].unique()

    if label:
        label_samples = filtered_samples[filtered_samples[label[0]] == label[1]]
        return label_samples.shape[0]/filtered_samples.shape[0], filtered_samples.shape[0]/dataset.shape[0]

    # If all instances satisfying the condition belong to the same class
    if len(labels) == 1:
        return (dataset.columns[-1], labels[0]), filtered_samples.index

    return [False, False]


def check_irrelevant_conditions(rules, condition, label):
    for rule in rules:
        # It is only necessary to check rules with len(rule) < len(new_rule)
        if len(rule[0]) >= len(condition):
            break
        elif rule[1] == label and np.all([np.any(np.all(condition == cond, axis=1)) for cond in rule[0]]):
            return False
    return True


def RULES_algorithm(dataset: pd.DataFrame):
    nci = dataset.copy()
    rules = []
    n_combinations = 1
    while n_combinations <= dataset.shape[1]-1 and nci.shape[0] != 0:
        selectors = find_all_selectors(nci.iloc[:, :-1])
        candidates = form_conditions(selectors, n_combinations, dataset.shape[1]-1)
        for condition in candidates:
            label, indexes = study_condition(condition, dataset)
            if label and check_irrelevant_conditions(rules, condition, label):
                rules.append((np.array(condition), label, 1, len(indexes)/dataset.shape[0]))
                nci.drop(indexes, inplace=True, errors='ignore')

        n_combinations += 1

    for idx in range(nci.shape[0]):
        rule = []
        for attribute in range(nci.shape[1]-1):
            rule.append((nci.columns[attribute], nci.iloc[idx, attribute]))
        label = (nci.columns[-1], nci.iloc[idx, -1])
        precision, coverage = study_condition(tuple(rule), dataset, label)
        rules.append((np.array(rule), label, precision, coverage))

    return rules
