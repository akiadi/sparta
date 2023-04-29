def solution(number, num1, num2):
    answer = []
    new_number = number.copy()
    new_number.remove(num1)
    if num2 in new_number:
        new_number.pop(num2)
    else:
        new_number = new_number
    answer.append(new_number)
    return answer[0]

print(solution([1,2,3,4,5], 1, 3))