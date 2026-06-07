import numpy as np

class LLMEvaluator:
    """
    Evaluates LLM-generated annotations.
    """

    def __init__(self, human_labels, llm_labels):
        self.human = human_labels
        self.llm = llm_labels

    def accuracy(self):
        return np.mean(self.human == self.llm)

    def error_rate(self):
        return 1 - self.accuracy()

    def confusion_cases(self):
        return {
            "false_positive": sum((self.llm == 1) & (self.human == 0)),
            "false_negative": sum((self.llm == 0) & (self.human == 1)),
        }
