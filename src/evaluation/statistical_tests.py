import numpy as np
from scipy import stats


class StatisticalTests:
    """
    Statistical evaluation layer for A/B testing and annotation validation.
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

    def t_test(self, group_a, group_b):
        return stats.ttest_ind(group_a, group_b, equal_var=False)

    def effect_size(self, group_a, group_b):
        return (np.mean(group_b) - np.mean(group_a)) / np.std(group_a)
