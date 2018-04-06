#-----------------------------------------
from setRulex import setRulex
from writeReadjson import cleanMEMORYRules
#-----------------------------------------


Rules = [
[{2},{2},'a'],
[{2},{4},'a'],
[{4},{2},'a'],
[{4},{3},'a'],
[{1},{1},'b'],
[{1},{2},'b']
]
d = 2


Rules = [
[{2},  {2,4},{1},'A'],
[{2,4},{2,3},{2},'A']
]
d = 2

Rules = [[{2},{2},{1},'a'],[{2},{4},{1},'a'],[{2},{2},{2},'a'],[{2},{3},{2},'a'],[{4},{2},{2},'a'],[{4},{3},{2},'a']]


cleanMEMORYRules() 
print('setRulex algorithm:')
rules = setRulex(Rules,d)
