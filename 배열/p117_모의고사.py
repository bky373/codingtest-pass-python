def solution(answers):
    # 각 학생의 찍기 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 각 학생의 맞춘 문제 수
    scores = [0, 0, 0]
    
    # 한 번의 루프에서 모든 학생의 정답 체크
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    
    # 최고 점수 찾기
    max_score = max(scores)
    
    # 최고 점수를 받은 학생들 반환 (리스트 컴프리헨션 사용)
    return [i + 1 for i, score in enumerate(scores) if score == max_score]


# 테스트 케이스
if __name__ == "__main__":
    test_cases = [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2]]
    
    for answers in test_cases:
        result = solution(answers)
        print(f"Answers: {answers}, Result: {result}")
