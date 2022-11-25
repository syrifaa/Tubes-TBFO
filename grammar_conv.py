from grammar_pros import isTerminal, isVar

def CFG2CNF(CFG):
    """
    Convert a CFG to CNF
    """
# STEP 1
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
        newrule = {"START" : [startSymbol]}
        newrule.update(CFG)
        CFG = newrule

# STEP 2
    containUnit = True

    while containUnit:
        unitProd = {}
        containUnit = False

        for head, body in CFG.items():
            for rule in body:
                if len(rule) == 1 and isVar(rule[0]):
                    containUnit = True
                    if head not in unitProd.keys():
                        unitProd[head] = [[rule[0]]]
                    else :
                        unitProd[head].append([rule[0]])
            
        for headUnit, bodyUnit in unitProd.items():
            for ruleUnit in bodyUnit:
                for head, body in CFG.items():
                    if len(ruleUnit) == 1 and head == ruleUnit[0]:
                        newrule = {headUnit : body}
                        if headUnit not in CFG.keys():
                            CFG[headUnit] = body
                        else :
                            for rule in body:
                                if rule not in CFG[headUnit]:
                                    CFG[headUnit].append(rule)

        for headUnit, bodyUnit in unitProd.items():
            for ruleUnit in bodyUnit:
                    if len(ruleUnit) == 1:
                        CFG[headUnit].remove(ruleUnit)

# STEP 3
    newProd = {}
    delProd = {}

    i = 0
    for head, body in CFG.items():
        for rule in body :
            headSimbol = head
            tempRule = [k for k in rule]
            if len(tempRule) > 2 :
                while len(tempRule) > 2:
                    newSimbol = f"X{i}"
                    if headSimbol not in newProd.keys():
                        newProd[headSimbol] = [[tempRule[0], newSimbol]]
                    else :
                        newProd[headSimbol].append([tempRule[0], newSimbol])
                    headSimbol = newSimbol
                    tempRule.remove(tempRule[0])
                    i += 1
                else :
                    if headSimbol not in newProd.keys():
                        newProd[headSimbol] = [tempRule]
                    else :
                        newProd[headSimbol].append(tempRule)

                    if head not in delProd.keys():
                        delProd[head] = [rule]
                    else :
                        delProd[head].append(rule)

    for newHead, newBody in newProd.items():
        if newHead not in CFG.keys():
            CFG[newHead] = newBody
        else :
            CFG[newHead].extend(newBody)

    for delHead, delBody in delProd.items():
        for delRule in delBody:
            CFG[delHead].remove(delRule)

# STEP 4
    newProd = {}
    delProd = {}

    j = 0
    r = 0
    for head, body in CFG.items():
        for rule in body:
            if len(rule) == 2 and isTerminal(rule[0]) and isTerminal(rule[1]):
                newSimbol_Y = f"Y{j}"
                newSimbol_Z = f"Z{r}"

                if head not in newProd.keys():
                    newProd[head] = [[newSimbol_Y, newSimbol_Z]]
                else :
                    newProd[head].append([newSimbol_Y, newSimbol_Z])

                newProd[newSimbol_Y] = [[rule[0]]]
                newProd[newSimbol_Z] = [[rule[1]]]

                if head not in delProd.keys():
                    delProd[head] = [rule]
                else :
                    delProd[head].append(rule)

                j += 1
                r += 1

            elif len(rule) == 2 and isTerminal(rule[0]):
                newSimbol_Y = f"Y{j}"

                if head not in newProd.key():
                    newProd[head] = [[newSimbol_Y, rule[1]]]
                else :
                    newProd[head].append([newSimbol_Y, rule[1]])

                newProd[newSimbol_Y] = [[rule[0]]]

                if head not in delProd.keys():
                    delProd[head] = [rule]
                else :
                    delProd[head].append(rule)

                j += 1
            elif len(rule) == 2 and isTerminal(rule[1]):
                newSimbol_Z = f"Z{r}"

                if head not in newProd.keys():
                    newProd[head] = [[rule[0], newSimbol_Z]]
                else :
                    newProd[head].append([rule[0], newSimbol_Z])

                newProd[newSimbol_Z] = [[rule[1]]]

                if head not in delProd.keys():
                    delProd[head] = [rule]
                else :
                    delProd[head].append(rule)

                r += 1

            else : 
                pass

    for newHead, newBody in newProd.items():
        if newHead not in CFG.keys():
            CFG[newHead] = newBody
        else :
            CFG[newHead].extend(newBody)
        
    for delHead, delBody in delProd.items():
        for delRule in delBody:
            CFG[delHead].remove(delRule)
    
    return CFG
