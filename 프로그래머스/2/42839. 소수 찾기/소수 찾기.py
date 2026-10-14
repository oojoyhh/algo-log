def solution(numbers):
    nums = set()
    visited = [False] * len(numbers)

    def dfs(current):
        if current != "":
            nums.add(int(current))

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(current + numbers[i])
                visited[i] = False

    dfs("")

    answer = 0

    for num in nums:
        if num < 2:
            continue

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            answer += 1

    return answer