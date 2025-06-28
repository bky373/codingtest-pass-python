answers_list = [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2]]

student1_pattern = [1, 2, 3, 4, 5]
student2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
student3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

answers = answers_list[0]

for answers in answers_list:
    problem_count = len(answers)
    student1_answer_sheet = [0] * problem_count
    student2_answer_sheet = [0] * problem_count
    student3_answer_sheet = [0] * problem_count

    student_results = [0, 0, 0]
    problem_result = []

    for i in range(problem_count):
        student1_answer_sheet[i] = student1_pattern[i % len(student1_pattern)]
        student2_answer_sheet[i] = student2_pattern[i % len(student2_pattern)]
        student3_answer_sheet[i] = student3_pattern[i % len(student3_pattern)]

    for i in range(problem_count):
        ans = answers[i]
        if ans == student1_answer_sheet[i]:
            student_results[0] += 1
        if ans == student2_answer_sheet[i]:
            student_results[1] += 1
        if ans == student3_answer_sheet[i]:
            student_results[2] += 1

    max_success = max(student_results)
    for i in range(len(student_results)):
        if student_results[i] == max_success:
            problem_result.append(i + 1)

    print(f"Answers: {answers}, Problem Result: {problem_result}")
