from copy import deepcopy
import itertools
#-------------------------------------------------------------
#def similarity(rule1,rule2,d):
#    unions = []
#    intersections = []
#    indexes = []
#    difference = 0
#    for i in range( len(rule1) - 1 ):
#        union = rule1[i] | rule2[i]
#        intersection = rule1[i] & rule2[i]
#        unions.append(union)
#        intersections.append(intersection)
#        if intersection == set():#or ( intersection != set() and rule1[i]!=rule2[i] ): #hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
#            difference +=1
#            indexes.append(i)
#    if difference <= d:
#        return [True, unions, intersections, indexes]
#    else:
#        return [False, None, None, None]

# similarity properSet
def similarity(rule1,rule2,d):
    unions = []
    intersections = []
    indexes = []
    difference = 0
    for i in range( len(rule1) - 1 ):
        union = rule1[i] | rule2[i]
        intersection = rule1[i] & rule2[i]
        unions.append(union)
        intersections.append(intersection)
        if intersection == set() or intersection < rule1[i] or intersection < rule2[i]: #hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
            difference +=1
            indexes.append(i)
    print('indexes', indexes)
    if difference <= d:
        return [True, unions, intersections, indexes]
    else:
        return [False, None, None, None]

#print( similarity( [{1}, {2}, 'A'], [{2}, {2}, 'A'], 1) )
#print( similarity([{2}, {2}, 'A'],[{1}, {3}, 'A'],   1))
#print( similarity([{2}, {2,4}, 'A'],[{4}, {2,3},'A'], 1))

def expandRule(rule):
    rules = []
    sets = rule[0:-1]
    #print('sets', sets)
    combinations = itertools.product(*sets)
    for i in combinations:
        temp_rule = []
        combination = i
        #print(combination,type(combination))
        for j in combination:
            _set = set()
            _set.add(j)
            temp_rule.append(_set)
        #for k in rule[-2:]: temp_rule.append(k)
        rules.append(temp_rule)
#    print(rules)
    return rules
#expandRule([{1,2,3},{2,3},'A'])

def contradictions(rule, rules_other_classes):
    #rules_other_classes = []
    #for p in presets_other_classes:
    #    rules_other_classes.append(preset_into_rule(p))
    for r in rules_other_classes:
        r = r[0:-1]
    expand = expandRule(rule)
    for r in expand:
        for R in rules_other_classes:
            equal = 0
            for i in range(len(r)):
                if r[i].issubset(R[i]) == True:
                    equal +=1
            if equal == len(r):
                return True #  There are contradiction
    return False # No contradiction
#print(contradictions( [{1,2},{3},'A'], [[{1},{4},'B'], [{4},{8},'C'], [{1},{3},'B']] ))

def create_rule(rule1, unions, intersections, indexes, rules_other_classes, d):
    rule = deepcopy(rule1)
    for i in range(len(rule1)-1):
        if i in indexes:
            rule[i] = unions[i]
        else:
            rule[i] = intersections[i]
    if d >=2:
        #for i in range(len(rule1) -1):#hhhhhhhhhhhhhhhhhhhhhhhhhhh
         #   rule[i] = unions[i]#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
        contradiction = contradictions(rule,rules_other_classes)
        if contradiction == False:
            return rule
        else:
            return None
    else:
        return rule

#  True if a rule1 is subset of rule2, False otherwhise
def contained( rule1, rule2 ):
    #if rule1[-1] == rule2[-1]:
    equalParameters = 0
    for i in range( len(rule1) - 1 ):
        if rule1[i].issubset(rule2[i]):
            equalParameters +=1
    if equalParameters == len(rule1) - 1:
        return True
    else:
        return False
    #else:
    #    return False
# TESTS
#print(contained( [{1},{1},'A'],[{1},{1,2,3},'A']) )
#True
#print(  contained( [{2},{7},'D'],[{2,5},{7},'D']   )   )
#True
def deleteRedundant( rules ):
    for i in range(0, len(rules)):
        redundant = False
        rule1 = rules[i]
        #print('rule1',  rule1)
        for j in range(0, len(rules)):
            rule2 = rules[j]
         #   print(rule2)
            if rule1 != None and rule2 != None and i != j and contained(rule1,rule2) == True:
          #      print(rule1,'contained in', rule2)
                redundant = True
        if redundant == True:
            rules[i] = None
    return rules

def search_patterns(rules_current_class, rules_other_classes, d):
    for r1 in rules_current_class:
        if r1 != None:
            for i in range(len(rules_current_class)):
                if rules_current_class[i]!=None:
                    r2 = rules_current_class[i]
                    [pattern, unions, intersections, indexes] = similarity(r1, r2, d)
                    if pattern:
                         rule = create_rule(r1, unions, intersections, indexes, rules_other_classes, d)
                         print('created rule: ', rule)
                         if rule not in rules_current_class:
                             rules_current_class.append(rule)
            deleteRedundant(rules_current_class)
    rules_current_class = [x for x in rules_current_class if x != None] 
    print(rules_current_class)
    return rules_current_class
#search_patterns([ [{1},{2},'A'], [{3},{4},'A'] ], [], 2)
#search_patterns([ [{2},{2,4},'A'], [{4},{2,3},'A'] ], [], 1)








