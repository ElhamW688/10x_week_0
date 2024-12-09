def longest_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return 0

    # dp[i] stores the length of the longest increasing subsequence ending at index i
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)  # The length of the longest subsequence is the max value in dp

# Example usage:
arr = [3,4,8,9,2]
print(longest_increasing_subsequence(arr))  # Output: 6
