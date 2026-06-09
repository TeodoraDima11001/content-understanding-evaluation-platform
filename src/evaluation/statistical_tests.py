import numpy as np
from scipy import stats


class StatisticalTests:
    """
    Production-style statistical testing layer.
    """

    def bootstrap_ci(self, data, n_boot=1000, alpha=0.05):
        means = []
        data = np.array(data)

        for _ in range(n_boot):
            sample = np.random.choice(data, size=len(data), replace=True)
            means.append(np.mean(sample))

        lower = np.percentile(means, 100 * alpha / 2)
        upper = np.percentile(means, 100 * (1 - alpha / 2))

        return lower, upper

    def t_test(self, a, b):
        return stats.ttest_ind(a, b, equal_var=False)

    def effect_size(self, a, b):
        return (np.mean(b) - np.mean(a)) / np.std(np.concatenate([a, b]))
