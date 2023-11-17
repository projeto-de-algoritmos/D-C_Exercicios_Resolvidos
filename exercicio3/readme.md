# [K Closest Points to Origin](https://leetcode.com/problems/reverse-bits/description/)

Dado um conjunto de pontos onde points[i] = [xi, yi] representa um ponto no plano X-Y e um número inteiro k, retorne os k pontos mais próximos à origem (0, 0).

A distância entre dois pontos no plano X-Y é a distância euclidiana (ou seja, √(x1 - x2)2 + (y1 - y2)2).

Você pode retornar a resposta em qualquer ordem. A resposta é garantida única (exceto pela ordem em que está).

> Exemplo:
> 
> Entrada: points = [[1,3],[-2,2]], k = 1
> 
> Saída: [[-2,2]]
> 
> Explicação: A distância entre (1, 3) e a origem é sqrt(10). A distância entre (-2, 2) e a origem é sqrt(8). Como sqrt(8) < sqrt(10), (-2, 2) está mais perto da origem. Queremos apenas os k = 1 pontos mais próximos da origem, então a resposta é apenas [[-2,2]].