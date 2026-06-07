import numpy as np
import pandas as pd

class AnnotationQualityEvaluator:
    """
    Evaluates annotation quality from humans or LLMs.
    """

    def __init__(self, df):
        self.df = df

    def agreement_rate(self):
        """
        Measures simple agreement between annotators.
        """
        return (self.df["label"] == self.df["label_reference"]).mean()

    def confidence_weighted_accuracy(self):
        """
        Weigh annotations by confidence scores.
        """
        return np.average(
            self.df["label"] == self.df["label_reference"],
            weights=self.df["confidence"]
        )

    def label_distribution_shift(self):
        """
        Detects drift in label distribution.
        """
        return self.df["label"].value_counts(normalize=True)
