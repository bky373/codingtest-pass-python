import unittest


def solution(N, stages):
    """
    TC: O(M + N log N)
     - M: the number of players (length of stages)
     - N: the number of stages
    SC: O(N)
     - challenger list: O(N)
     - fails dictionary: O(N)
    """
    challenger = [0] * (N + 2)  # N+1 is the last stage, N+2 is for out of bounds
    # 스테이지별 도전자 수를 구함
    for stage in stages:
        challenger[stage] += 1

    # 스테이지별 실패한 사용자 수 계산
    fails = {}
    total = len(stages)

    # 각 스테이지를 순회하며 실패율 계산
    for i in range(1, N + 1):
        if challenger[i] == 0: # 도전자가 없는 경우, 실패율은 0
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]

    # 실패율이 높은 스테이지부터 내림차순 정렬
    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    return result


class TestSolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]), [3, 4, 2, 1, 5])

    def test_all_clear(self):
        self.assertEqual(solution(4, [4, 4, 4, 4, 4]), [4, 1, 2, 3])

    def test_one_user(self):
        self.assertEqual(solution(1, [2]), [1])


unittest.main(argv=[''], verbosity=2, exit=False)
