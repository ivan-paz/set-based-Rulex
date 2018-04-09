#-----------------------------------------
from setRulex import setRulex
from writeReadjson import cleanMEMORYRules
#-----------------------------------------

# TEST1
Rules = [
[{2},{2},'a'],
[{2},{4},'a'],
[{4},{2},'a'],
[{4},{3},'a'],
[{1},{1},'b'],
[{1},{2},'b']
]
d = 2

# TEST2
Rules = [[{2},{2},{1},'a'],[{2},{4},{1},'a'],[{2},{2},{2},'a'],[{2},{3},{2},'a'],[{4},{2},{2},'a'],[{4},{3},{2},'a']]
d = 2

cleanMEMORYRules() 
print('setRulex algorithm:')
rules = setRulex(Rules,d)
