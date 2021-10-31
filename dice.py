import random
import plotly.express as px

result = []
count = []

for i in range(1,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1 + dice2
    result.append(sum)
    count.append(i)

print(result)

graph = px.bar(x = result, y = count)
graph.show()
