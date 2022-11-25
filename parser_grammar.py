

def parser_CYK(cnf, input_string):
    """
    CYK algorithm for parsing a string with a given CNF grammar
    :param cnf: CNF grammar
    :param input_string: input string
    :return: True if the string can be parsed, False otherwise
    """
    w = input_string.split(" ")
    n = len(w)
    m = [[set([]) for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for head,body in cnf.items():
            for r in body:
                if len(r)==1 and r[0]==w[i]:
                    m[i][i].add(head)
                    
        for j in range(i,-1,-1):
            for k in range(j,i):
                for head,body in cnf.items():
                    for r in body:
                        if len(r)==2 and r[0] in m[j][k] and r[1] in m[k+1][i]:
                            m[j][i].add(head)
                            
    return len(m[0][n-1])!=0