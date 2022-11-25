from grammar_pros import isTerminal, isVar

def createNew(CFG):
    listHead = list(CFG.keys())
    listBody = list(CFG.values())
    startSymbol = listHead[0]
    add_newrule = False

    for rules in listBody:
        for rule in rules:
            if startSymbol in rule:
                add_newrule = True
                break
        if add_newrule:
            break

    if add_newrule:
        newrule = {"START" : [[startSymbol]]}
        newrule.update(CFG)
        CFG = newrule
    return CFG

def removeUnitProds(CFG):
    containUnit = True

    while containUnit:
        unitProds = {}
        containUnit = False
        
        for head, body in CFG.items():
            for rule in body:
                if len(rule) == 1 and isVar(rule[0]):
                    containUnit = True
                    if head not in unitProds.keys():
                        unitProds[head] = [[rule[0]]]
                    else:
                        unitProds[head].append([rule[0]])

        for headUnit, bodyUnit in unitProds.items():
            for ruleUnit in bodyUnit:
                for head, body in CFG.items():
                    if len(ruleUnit) == 1 and head == ruleUnit[0]:
                        newrule = {headUnit : body}
                        if headUnit not in CFG.keys():
                            CFG[headUnit] = body
                        else:
                            for rule in body:
                                if rule not in CFG[headUnit]:
                                    CFG[headUnit].append(rule)
    
        for headUnit, bodyUnit in unitProds.items():
            for ruleUnit in bodyUnit:
                if len(ruleUnit) == 1:
                    CFG[headUnit].remove(ruleUnit)
    return CFG

def replaceBody(CFG):
    newProds = {}
    delProds = {}

    i = 0
    for head, body in CFG.items():
        for rule in body:
            headSymbol = head
            tempRule = [r for r in rule]
            if len(tempRule) > 2:
                while len(tempRule) > 2:
                    newSymbol = f"X{i}"
                    if headSymbol not in newProds.keys():
                        newProds[headSymbol] = [[tempRule[0], newSymbol]]
                    else:
                        newProds[headSymbol].append([tempRule[0], newSymbol])
                    headSymbol = newSymbol
                    tempRule.remove(tempRule[0])
                    i += 1
                else:
                    if headSymbol not in newProds.keys():
                        newProds[headSymbol] = [tempRule]
                    else:
                        newProds[headSymbol].append(tempRule)
                    
                    if head not in delProds.keys():
                        delProds[head] = [rule]
                    else:
                        delProds[head].append(rule)

    for newHead, newBody in newProds.items():
        if newHead not in CFG.keys():
            CFG[newHead] = newBody
        else:
            CFG[newHead].extend(newBody)

    for delHead, delBody in delProds.items():
        for delRule in delBody:
            CFG[delHead].remove(delRule)
    return CFG

def replaceTerminal(CFG):
    new_productions = {}
    del_productions = {}

    j = 0
    k = 0
    for head, body in CFG.items():
        for rule in body:
            if len(rule) == 2 and isTerminal(rule[0]) and isTerminal(rule[1]):
                new_symbol_Y = f"Y{j}"
                new_symbol_Z = f"Z{k}"

                if head not in new_productions.keys():
                    new_productions[head] = [[new_symbol_Y, new_symbol_Z]]
                else:
                    new_productions[head].append([new_symbol_Y, new_symbol_Z])
                    
                new_productions[new_symbol_Y] = [[rule[0]]]
                new_productions[new_symbol_Z] = [[rule[1]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                j += 1
                k += 1

            elif len(rule) == 2 and isTerminal(rule[0]):
                new_symbol_Y = f"Y{j}"

                if head not in new_productions.keys():
                    new_productions[head] = [[new_symbol_Y, rule[1]]]
                else:
                    new_productions[head].append([new_symbol_Y, rule[1]])

                new_productions[new_symbol_Y] = [[rule[0]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                j += 1

            elif len(rule) == 2 and isTerminal(rule[1]):
                new_symbol_Z = f"Z{k}"

                if head not in new_productions.keys():
                    new_productions[head] = [[rule[0], new_symbol_Z]]
                else:
                    new_productions[head].append([rule[0], new_symbol_Z])

                new_productions[new_symbol_Z] = [[rule[1]]]

                if head not in del_productions.keys():
                    del_productions[head] = [rule]
                else:
                    del_productions[head].append(rule)

                k += 1

            else:
                pass

    for new_head, new_body in new_productions.items():
        if new_head not in CFG.keys():
            CFG[new_head] = new_body
        else:
            CFG[new_head].extend(new_body)

    for del_head, del_body in del_productions.items():
        for del_rule in del_body:
            CFG[del_head].remove(del_rule)
    return CFG

def CFG2CNF(CFG):
    CFG = createNew(CFG)
    CFG = removeUnitProds(CFG)
    CFG = replaceBody(CFG)
    CFG = replaceTerminal(CFG)
    return CFG