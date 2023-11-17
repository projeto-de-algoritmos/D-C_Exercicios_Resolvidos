import random
class Solution:
    def kClosest(self, points:[[int]], k: int) -> [[int]]:
        dist = lambda point: point[0]**2 + point[1]**2

        def divide_conquer(points, k):   
            if len(points) == k:
                return points
            
            aux1 = []
            aux2 = []
            mid = random.randint(0, len(points) - 1)
                    
            for x in range(len(points)):
                if dist(points[x]) < dist(points[mid]):
                    aux1.append(points[x])
                else:
                    aux2.append(points[x])
        
            if k < len(aux1):
                return divide_conquer(aux1, k)
            elif k > len(aux1):
                return aux1 + divide_conquer(aux2, k - len(aux1))
            
            return aux1
    
        return divide_conquer(points, k)
    
    
points = [[1,3],[-2,2]]
k = 1
solution = Solution()
result = solution.kClosest(points, k)
print(f"Output: {result}")