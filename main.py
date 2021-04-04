from datapreprocessor import preprocessor
from rulesmanager import generator, interpreter
from utils import plotter, metrics
from datetime import datetime


def evaluate(dataset, rules_fn='rules', train_test_ratio=0.8):
    train_set = dataset.iloc[:int(dataset.shape[0]*train_test_ratio)].reset_index(drop=True)
    test_set = dataset.iloc[int(dataset.shape[0]*train_test_ratio):].reset_index(drop=True)
    start_time = datetime.now()
    rules = generator.RULES_algorithm(train_set)
    end_time = datetime.now()
    print(f'RULES Generation Time: {end_time - start_time}')
    plotter.write_rules(plotter.format_rules(rules), file=rules_fn)
    start_time = datetime.now()
    prediction = interpreter.classify(test_set.iloc[:, :-1], rules)
    end_time = datetime.now()
    print(f'RULES Classification Time: {end_time - start_time}')
    print("________________________________________________")
    ground_truth = list(test_set.iloc[:, -1])
    print(f"Predicted:\n{prediction}")
    print(f"GT:\n{ground_truth}\n")
    print(f"Global Accuracy                  : {round(metrics.get_global_accuracy(ground_truth, prediction)*100, 3)}%")
    print(f"Accuracy of Classified Instances : {round(metrics.get_classified_accuracy(ground_truth, prediction)*100, 3)}%\n")
    print(f"Classification Report [Global]:\n{metrics.classification_report(ground_truth, prediction)}")
    print(f"Confusion Matrix [Global]:\n{metrics.get_confusion_matrix(ground_truth, prediction)}")


if __name__ == '__main__':

    print("===============================================")
    print("Lenses Dataset Evaluation [Test/Slides Dataset]")
    print("===============================================")
    lenses = preprocessor.load_test_dataset().sample(frac=1, random_state=0)
    evaluate(lenses, rules_fn='lenses_rules', train_test_ratio=0.8)

    print("\n===============================================")
    print("Ecoli Dataset Evaluation [Small Dataset]")
    print("===============================================")
    ecoli = preprocessor.load_ecoli_dataset().sample(frac=1, random_state=0)
    evaluate(ecoli, rules_fn='ecoli_rules', train_test_ratio=0.8)

    print("\n===============================================")
    print("Car Dataset Evaluation [Medium Dataset]")
    print("===============================================")
    car = preprocessor.load_car_dataset().sample(frac=1, random_state=0)
    evaluate(car, rules_fn='car_rules', train_test_ratio=0.8)

    print("\n===============================================")
    print("Rice Dataset Evaluation [Large Dataset]")
    print("===============================================")
    rice = preprocessor.load_rice_dataset().sample(frac=1, random_state=0)
    evaluate(rice, rules_fn='rice_rules', train_test_ratio=0.8)

    print("\n===============================================")
    print("Stroke Dataset Evaluation [Large Dataset]")
    print("===============================================")
    stroke = preprocessor.load_stroke_dataset().sample(frac=1, random_state=0)
    evaluate(stroke, rules_fn='stroke_rules', train_test_ratio=0.8)
    """
    ===============================================
    Stroke Dataset Evaluation [Large Dataset]
    ===============================================
    RULES Generation Time: 1:30:23.586147
    RULES Classification Time: 0:00:16.412841
    ________________________________________________    
    Global Accuracy                  : 92.27%
    Accuracy of Classified Instances : 92.27%
    
    Classification Report [Global]:
                  precision    recall  f1-score   support
    
               0       0.95      0.97      0.96       966
               1       0.10      0.05      0.07        56
    
        accuracy                           0.92      1022
       macro avg       0.53      0.51      0.52      1022
    weighted avg       0.90      0.92      0.91      1022
    
    Confusion Matrix [Global]:
    [[940  26]
     [ 53   3]]
    """
