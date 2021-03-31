from sklearn.metrics import classification_report, confusion_matrix


def get_accuracy(ground_truth, prediction):
    return round(sum([1 if prediction[i] == ground_truth[i] else 0 for i in range(len(prediction))])/len(prediction), 5)


def get_classification_report(ground_truth, prediction):
    return classification_report(ground_truth, prediction, zero_division=0)


def get_confusion_matrix(ground_truth, prediction):
    return confusion_matrix(ground_truth, prediction)
