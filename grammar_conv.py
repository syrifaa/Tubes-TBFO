from grammar_pros import isTerminal, isVar

def CFG2CNF(CFG):
    # STEP 1: If the start symbol S occurs on some right side, create a new start symbol S' and a new production S' -> S.
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

    # STEP 2: Remove unit productions.
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

    # STEP 3: Replace Body with 3 or more Variables
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

    # STEP 4: Replace Terminal adjacent to a Variables
    newProds = {}
    delProds = {}

    j = 0
    k = 0
    for head, body in CFG.items():
        for rule in body:
            if len(rule) == 2 and isTerminal(rule[0]) and isTerminal(rule[1]):
                newSymbol_Y = f"Y{j}"
                newSymbol_Z = f"Z{k}"

                if head not in newProds.keys():
                    newProds[head] = [[newSymbol_Y, newSymbol_Z]]
                else:
                    newProds[head].append([newSymbol_Y, newSymbol_Z])
                    
                newProds[newSymbol_Y] = [[rule[0]]]
                newProds[newSymbol_Z] = [[rule[1]]]

                if head not in delProds.keys():
                    delProds[head] = [rule]
                else:
                    delProds[head].append(rule)

                j += 1
                k += 1

            elif len(rule) == 2 and isTerminal(rule[0]):
                newSymbol_Y = f"Y{j}"

                if head not in newProds.keys():
                    newProds[head] = [[newSymbol_Y, rule[1]]]
                else:
                    newProds[head].append([newSymbol_Y, rule[1]])

                newProds[newSymbol_Y] = [[rule[0]]]

                if head not in delProds.keys():
                    delProds[head] = [rule]
                else:
                    delProds[head].append(rule)

                j += 1

            elif len(rule) == 2 and isTerminal(rule[1]):
                newSymbol_Z = f"Z{k}"

                if head not in newProds.keys():
                    newProds[head] = [[rule[0], newSymbol_Z]]
                else:
                    newProds[head].append([rule[0], newSymbol_Z])

                newProds[newSymbol_Z] = [[rule[1]]]

                if head not in delProds.keys():
                    delProds[head] = [rule]
                else:
                    delProds[head].append(rule)

                k += 1

            else:
                pass

    for newHead, newBody in newProds.items():
        if newHead not in CFG.keys():
            CFG[newHead] = newBody
        else:
            CFG[newHead].extend(newBody)

    for delHead, delBody in delProds.items():
        for delRule in delBody:
            CFG[delHead].remove(delRule)

    return CFG