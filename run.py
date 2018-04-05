
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
d = 1
cleanMEMORYRules() 
print('setRulex algorithm:')
rules = setRulex(Rules,1)

