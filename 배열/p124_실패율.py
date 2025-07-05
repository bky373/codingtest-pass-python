import unittest

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
result = [3, 4, 2, 1, 5]


def solution(N, stages):
    """
    TC: O(M log M + N log N)
     - M: number of stages (length of stages)
     - N: number of players (N is the maximum stage number)
    SC: O(N)
     - failure_rate: O(N)
    """
    ans = []
    failure_rate = []
    stages.sort()
    j = 0
    last = 0
    for i in range(1, N + 1):
        while j < len(stages) and stages[j] == i:
            j += 1
        failure_rate.append((j - last) / (len(stages) - last))
        last = j

    for i, rate in sorted(enumerate(failure_rate, start=1), key=lambda x: (-x[1], x[0])):
        ans.append(i)
    return ans


class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]), [3, 4, 2, 1, 5])

    def test_all_clear(self):
        self.assertEqual(solution(4, [4, 4, 4, 4, 4]), [4, 1, 2, 3])

    def test_one_user(self):
        self.assertEqual(solution(1, [2]), [1])


unittest.main(argv=[''], verbosity=2, exit=False)
