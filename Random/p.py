
import graphviz
import random

f = graphviz.Digraph('finite_state_machine', filename='fsm.gv')


randCityNumber = random.randint(50, 100)
arr = []

for x in range(0, randCityNumber):
    arr.append(f'city{x}')

random.shuffle(arr)

f.attr('node', shape='circle')
for x in arr:
    if (x =='city1'):
        f.node(f'{x}', style='filled', fillcolor='purple')
    else:
        f.node(f'{x}', style='', fillcolor='white')

for x in arr:
    randNo = random.randint(0, len(arr)-1)
    while(arr[randNo] == x):
        randNo = random.randint(0, len(arr)-1)
    f.edge(f'{x}', f'{arr[randNo]}', arrowhead='none')




f.view()