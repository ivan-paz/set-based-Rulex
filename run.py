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
cleanMEMORYRules()
d = 1
#Rules = [[{2}, {2}, 'a'], [{2}, {4}, 'a'], [{4}, {2}, 'a'], [{4}, {3}, 'a']]
#Rules = [[{1},{2}, {2}, 'a'], [{1}, {3}, {2}, 'a'], [{2}, {2}, {2}, 'a'], [{2}, {3}, {2}, 'a'], [{1}, {4}, {2}, 'a'], [{3}, {2}, {2}, 'a'], [{3}, {4}, {2}, 'a'],[{1},{1},{1},'b']]

#Rules = [
#[{1},{2}, {6}, 'a'],
#[{6},{5}, {6}, 'a'],
#[{5},{4}, {6}, 'b'],
#[{6},{6}, {6}, 'b'],
#[{5},{3}, {6}, 'b'],
#[{6},{3}, {6}, 'b'],
#[{6},{4}, {6}, 'a'],
#[{4},{5}, {6}, 'b'],
#[{5},{5}, {6}, 'b'],
#[{1},{1}, {6}, 'b'],
#[{4},{1}, {6}, 'b'],
#[{2},{5}, {6}, 'a']]

#Rules = [
#[{3}, {2}, {5}, 'b'],
#[{3}, {1}, {5}, 'a'],
#[{1}, {2}, {5}, 'b'],
#[{3}, {4}, {5}, 'b'],
#[{1}, {6}, {5}, 'a'],
#[{6}, {2}, {5}, 'b'],
#[{4}, {5}, {5}, 'a'],
#[{2}, {2}, {5}, 'b'],
#[{4}, {1}, {5}, 'b'],
#[{2}, {6}, {5}, 'b'],
#[{5}, {2}, {5}, 'a'],
#[{2}, {1}, {5}, 'b'],
#[{6}, {3}, {5}, 'a'],
#[{4}, {4}, {5}, 'a'],
#[{1}, {1}, {5}, 'a']
#]
#Rules = [
#[{2}, {3}, {2}, 'b'],
#[{3}, {2}, {2}, 'b'],
#[{6}, {5}, {2}, 'b'],
#[{4}, {6}, {2}, 'a'],
#[{4}, {2}, {2}, 'a'],
#[{1}, {1}, {2}, 'b'],
#[{5}, {5}, {2}, 'a'],
#[{2}, {2}, {2}, 'b'],
#[{4}, {5}, {2}, 'b'],
#[{2}, {1}, {2}, 'a'],
#[{3}, {4}, {2}, 'a'],
#[{4}, {4}, {2}, 'a'],
#[{3}, {6}, {2}, 'b'],
#[{6}, {6}, {2}, 'a']
#]
#Rules = [
#[{3}, {3}, {6}, 'a'],
#[{4}, {3}, {6}, 'a'],
#[{3}, {4}, {6}, 'a'],
#[{6}, {1}, {6}, 'a'],
#[{1}, {5}, {6}, 'a'],
#[{1}, {3}, {6}, 'a'],
#[{3}, {2}, {6}, 'a'],
#[{4}, {2}, {6}, 'b'],
#[{5}, {4}, {6}, 'b'],
#[{2}, {2}, {6}, 'b'],
#[{5}, {3}, {6}, 'b'],
#[{1}, {4}, {6}, 'a'],
#[{2}, {1}, {6}, 'b'],
#[{2}, {5}, {6}, 'b'],
#[{1}, {2}, {6}, 'a']
#]
#Rules = [[{6}, {1}, {6}, 'a'], [{1, 3, 4}, {3}, {6},'a'], [{3}, {2, 3, 4}, {6}, 'a'], [{1, 3}, {2, 4}, {6}, 'a'], [{1}, {2, 3, 4, 5}, {6}, 'a']]

#setRulex 0 rulex 1
Rules = [ [{1}, {2}, {5}, 'a'],[{2}, {2}, {5}, 'a'], [{3}, {2}, {5}, 'a'] ]
#.......................................................
existentRules = read('MEMORYRules.json')
print('existingRules',existentRules)
MEMORYRules = read('MEMORYRules.json')
[Rules.append(r) for r in MEMORYRules if r not in Rules]
rules = setRulex(Rules,d)
write('MEMORYRules.json',rules)
#.......................................................

#if rules == [[{2}, {2, 4}, 'a'], [{2, 4}, {2}, 'a'], [{4}, {2, 3}, 'a']]:
#    print('Olé')
