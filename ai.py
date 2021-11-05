def SumOfThe(N,data = []):
    sum = 0
    for i in range(N):
        sum = sum + data[i]
    result = 0

    for j in range(N):
        if data[j] == sum - data[j]:
            result = data[j]
    return result
