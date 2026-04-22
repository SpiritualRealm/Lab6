from sklearn import tree
import numpy as np
from sklearn.metrics import accuracy_score

def load_data():
    training_data = np.genfromtxt('dataset.csv', delimiter=',', dtype=np.int32)

    inputs = training_data[:, :-1]
    labels = training_data[:, -1]

    cv_fold_n = 5
    training_size = int(len(inputs) * (cv_fold_n - 1) / cv_fold_n)

    training_inputs = inputs[:training_size]
    training_labels = labels[:training_size]
    testing_inputs = inputs[training_size:]
    testing_labels = labels[training_size:]
    return training_inputs, testing_inputs, training_labels, testing_labels

def main():
    training_inputs, testing_inputs, training_labels, testing_labels = load_data()

    classifier = tree.DecisionTreeClassifier()
    classifier.fit(training_inputs, training_labels)

    predictions = classifier.predict(testing_inputs)

    accuracy = 100.0 * accuracy_score(testing_labels, predictions)
    print("Decision tree classification accuracy is: {0}".format(accuracy))

main()