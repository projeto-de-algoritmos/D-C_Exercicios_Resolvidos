class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        def partition(arr, left, right):
            pivot = arr[right]
            i = left - 1

            # Arranjo a lista com base no pivo
            for j in range(left, right):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[right] = arr[right], arr[i + 1]
            return i + 1

        def divide_conquer(arr, left, right, k):
            if left <= right:
                pivot_index = partition(arr, left, right)

                if pivot_index == k:
                    return arr[pivot_index]
                elif pivot_index < k:
                    return divide_conquer(arr, pivot_index + 1, right, k)
                else:
                    return divide_conquer(arr, left, pivot_index - 1, k)

        return divide_conquer(nums, 0, len(nums) - 1, len(nums) - k) # do menor para o maior 

nums = [3, 2, 1, 5, 6, 4]
k = 2 # do maior para o menor
solution = Solution()
result = solution.findKthLargest(nums, k)
print(f"Output: {result}")
