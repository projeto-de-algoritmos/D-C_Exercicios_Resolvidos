import random
class Solution:
    def kClosest(self, points:[[int]], k: int) -> [[int]]:
        dist = lambda point: point[0]**2 + point[1]**2

        def divide_conquer(points, k):   
            # Retorna todos os pontos, pois K abrange todos
            if len(points) == k:
                return points
            
            aux1 = []
            aux2 = []
            pivo = random.randint(0, len(points) - 1)
                    
            for x in range(len(points)):
                # adiciona no aux1 todos os pontos mais proximo do centro que o pivo
                if dist(points[x]) < dist(points[pivo]):
                    aux1.append(points[x])
                else:
                # adiciona no aux2 todos os pontos mais distantes do centro que o pivo
                    aux2.append(points[x])
        
            # se a quantidade de pontos necessarios for menor que a lista, filtra a lista ainda mais
            if k < len(aux1):
                return divide_conquer(aux1, k)
            # se a quantidade de pontos necessarios for maior que a lista, então concatena
            elif k > len(aux1):
                return aux1 + divide_conquer(aux2, k - len(aux1))
            
            return aux1
    
        return divide_conquer(points, k)
    
    
points = [[1,3],[-2,2]]
k = 1
solution = Solution()
result = solution.kClosest(points, k)
print(f"Output: {result}")