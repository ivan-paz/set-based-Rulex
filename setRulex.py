from searchPatterns import search_patterns

def createDictionaryOfCategories(Rules):
    dictionary_of_classes = dict()
    for rule in Rules:
        rule_class = rule[-1]
        if rule_class not in dictionary_of_classes:
            dictionary_of_classes[rule_class] = []
            dictionary_of_classes[rule_class].append(rule)
        else:
            dictionary_of_classes[rule_class].append(rule)
    return dictionary_of_classes
#-----------------------------------------------------------------------------
def splitRules(key,dictionary_of_classes):
    rules_other_classes = []
    for key1 in dictionary_of_classes:
        if key1 != key:
            for r in dictionary_of_classes[key1]:
                rules_other_classes.append(r)
        else:
            rules_current_class = dictionary_of_classes[key]
    return [rules_current_class, rules_other_classes]
#-----------------------------------------------------------------------------
def search(Rules, d):
    final_rules = []
    dictionary_of_categories = createDictionaryOfCategories(Rules)
    for key in dictionary_of_categories:
        [rules_current_class,rules_other_classes] = splitRules(key,dictionary_of_categories)
        #print('key:', key, ';', 'rules current class', rules_current_class,'rules other classes : ', rules_other_classes)
        #print('searching paterns . . . ')
        rules_current_class = search_patterns(rules_current_class,rules_other_classes,d)
        [final_rules.append(r) for r in rules_current_class if r not in final_rules]
    return final_rules

def setRulex(Rules,d):    
    previousRules = []; cont = 0
    rules = search(Rules,d)
    print('rules in the first extraction:', rules)
    while rules != previousRules:
        cont +=1
        print('rules != previousRules', cont)
        previousRules = rules
        rules = search(previousRules,d)
    print('Final set of rules extracted with setRulex: ', rules)
    return rules
#rules = setRulex([[{1},{2},'A'],[{3},{4},'A']],2)





