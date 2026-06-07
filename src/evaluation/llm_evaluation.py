import numpy as np


class LLMEvaluator:
    """
    Evaluates LLM annotation quality vs human ground truth.
    """

    def __init__(self, human_labels, llm_labels):
        self.human = np.array(human_labels)
        self.llm = np.array(llm_labels)

    def accuracy(self):
        return np.mean(self.human == self.llm)

    def error_rate(self):
        return 1 - self.accuracy()

    def confusion_matrix_metrics(self):
        tp = np.sum((self.llm == 1) & (self.human == 1))
        tn = np.sum((self.llm == 0) & (self.human == 0))
        fp = np.sum((self.llm == 1) & (self.human == 0))
        fn = np.sum((self.llm == 0) & (self.human == 1))

        return {
            "precision": tp / (tp + fp + 1e-9),
            "recall": tp / (tp + fn + 1e-9),
            "false_positive_rate": fp / (fp + tn + 1e-9),
            "false_negative_rate": fn / (fn + tp + 1e-9),
        }
