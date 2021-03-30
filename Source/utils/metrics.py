def get_accuracy(prediction, ground_truth):
    return round(sum([1 if prediction[i] == ground_truth[i] else 0 for i in range(len(prediction))])/len(prediction), 5)
