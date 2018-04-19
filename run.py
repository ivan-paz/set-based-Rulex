#-----------------------------------------
from setRulex import setRulex
from writeReadjson import *
#-----------------------------------------

# TEST1
#Rules = [
#[{2},{2},'a'],
#[{2},{4},'a'],
#[{4},{2},'a'],
#[{4},{3},'a'],
#[{1},{1},'b'],
#[{1},{2},'b']
#]
#d = 1

# TEST2
#Rules = [[{2},{2},{1},'a'],[{2},{4},{1},'a'],[{2},{2},{2},'a'],[{2},{3},{2},'a'],[{4},{2},{2},'a'],[{4},{3},{2},'a']]
#Rules = [[{4}, {2}, {2}, 'a'], [{2}, {2, 4}, {1}, 'a'], [{2}, {2}, {1, 2}, 'a'], [{2, 4}, {3}, {2}, 'a']]
#d = 1

# TEST 3 Breaking the algorithm
#Rules = [[{1,2},{2,3},{2},'a'],[{1,3},{2,4},{2},'a']]
#Rules = [[{2},{2,4},'a'],[{4},{2,3},'a']]

print('start setRulex algorithm    :')
#cleanMEMORYRules()
d = 1
Rules = [[{2}, {2}, 'a'], [{2}, {4}, 'a'], [{4}, {2}, 'a'], [{4}, {3}, 'a']]
#Rules = [[{1},{2}, {2}, 'a'], [{1}, {3}, {2}, 'a'], [{2}, {2}, {2}, 'a'], [{2}, {3}, {2}, 'a'], [{1}, {4}, {2}, 'a'], [{3}, {2}, {2}, 'a'], [{3}, {4}, {2}, 'a'],[{1},{1},{1},'b']]

#.......................................................
existentRules = read('MEMORYRules.json')
print('existingRules',existentRules)
MEMORYRules = read('MEMORYRules.json')
[Rules.append(r) for r in MEMORYRules if r not in Rules]
rules = setRulex(Rules,d)
write('MEMORYRules.json',rules)
#.......................................................

if rules == [[{2}, {2, 4}, 'a'], [{2, 4}, {2}, 'a'], [{4}, {2, 3}, 'a']]:
    print('Olé')
