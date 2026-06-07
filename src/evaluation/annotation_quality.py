import numpy as np
from scipy.stats import entropy


class AnnotationQualityEvaluator:
    """
    Evaluates annotation quality across human + LLM + system labels.
    Designed for Spotify-style content understanding pipelines.
    """

    def __init__(self, human_labels, system_labels):
        self.human = np.array(human_labels)
        self.system = np.array(system_labels)

    def agreement_rate(self):
        return np.mean(self.human == self.system)

    def label_distribution_shift(self):
        """
        Measures how much system predictions deviate from human labeling distribution.
        (Important for taxonomy drift detection)
        """
        human_dist = np.bincount(self.human) / len(self.human)
        system_dist = np.bincount(self.system) / len(self.system)

        # pad to same length
        max_len = max(len(human_dist), len(system_dist))
        human_dist = np.pad(human_dist, (0, max_len - len(human_dist)))
        system_dist = np.pad(system_dist, (0, max_len - len(system_dist)))

        return entropy(human_dist, system_dist)

    def bias_detection(self):
        """
        Detects systematic over/under prediction bias.
        """
        return {
            "over_prediction_rate": float(np.mean(self.system > self.human)),
            "under_prediction_rate": float(np.mean(self.system < self.human))
        }
