from datapreprocessor import preprocessor
from rulesmanager import generator, interpreter
from utils import plotter, metrics

if __name__ == '__main__':

    train_test_ratio = 1

    # Test Dataset Evaluation
    lenses = preprocessor.load_test_dataset().sample(frac=1, random_state=0)
    train_set = lenses.iloc[:int(lenses.shape[0]*train_test_ratio)].reset_index(drop=True)
    test_set = lenses.iloc[int(lenses.shape[0]*train_test_ratio):].reset_index(drop=True)
    rules = generator.RULES_algorithm(train_set)
    plotter.write_rules(plotter.format_rules(rules))
    prediction = interpreter.classify(test_set.iloc[:, :-1], rules)
    ground_truth = list(test_set.iloc[:, -1])
    print(f"Predicted: {prediction}")
    print(f"GT       : {ground_truth}")
    print(f"Accuracy : {metrics.get_accuracy(prediction, ground_truth)*100}%")
