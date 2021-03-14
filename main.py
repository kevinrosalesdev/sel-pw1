from datapreprocessor import preprocessor
from rulesmanager import generator

if __name__ == '__main__':

    # Test Dataset Evaluation
    lenses = preprocessor.load_test_dataset()
    generator.RULES_algorithm(lenses)
