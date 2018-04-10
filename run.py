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
#d = 1

# TEST2
Rules = [[{2},{2},{1},'a'],[{2},{4},{1},'a'],[{2},{2},{2},'a'],[{2},{3},{2},'a'],[{4},{2},{2},'a'],[{4},{3},{2},'a']]
#Rules = [[{4}, {2}, {2}, 'a'], [{2}, {2, 4}, {1}, 'a'], [{2}, {2}, {1, 2}, 'a'], [{2, 4}, {3}, {2}, 'a']]
d = 1


# TEST 3 Breaking the algorithm
Rules = [[{1,2},{2,3},{2},'a'],[{1,3},{2,4},{2},'a']]

Rules1 = [[{2},{2,4},'a'],[{4},{2,3},'a']]


cleanMEMORYRules() 
#print('setRulex algorithm:')
#d = 2
#rules = setRulex(Rules,d)
print('setRulex algorithm !!!!!!!!!!!!!!!')
cleanMEMORYRules()
d = 1
rules = setRulex(Rules1,d)
