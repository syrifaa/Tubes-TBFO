



def read_cfg(cfg_file):
    file = open(cfg_file, 'r')
    cfg = {}
    
    row = file.readline()
    while row != "":
        head, body = row.replace("\n","".split)("->")
        if head not in cfg:
            cfg[head] = [body.split(" ")]
        else:
            cfg[head].append(body.split(" "))
            
        row = file.readline()
        
    file.close()
    return cfg

def isTerminal(string):
    terminal = [
        "CONST",
        "LET",
        "VAR",
        "EQUAL",
        "IS_EQUAL",
        "STRICT_EQUAL",
        "GRATER_EQUAL",
        "GREATER",
        "LESS_EQUAL",
        "LESS",
        "NOT_EQUAL",
        "STRICT_NOT_EQUAL",
        "MULTIPLY_EQUAL",
        "DEVIDE_EQUAL",
        "MODULO_EQUAL",
        "PLUS",
        "MINUS",
        "DEVIDE",
        "MULTIPLE",
        "POWER",
        "AND",
        "OR",
        "TRUE",
        "FALSE",
        "IF",
        "ELSE",
        "FOR",
        "WHILE",
        "FUNCTION",
        "RETURN",
        "BREAK",
        "CONTINUE",
        "TRY",
        "FINALLY",
        "CATCH",
        "THROW",
        "SWTICH",
        "CASE",
        "DEAFULT",
        "DELETE",
        "NULL",
        "OPEN_ROUND_BRACKET",
        "CLOSE_ROUND_BRACKET",
        "OPEN_CURLY_BRACKET",
        "CLOSE_CURLY_BRACKET",
        "SEMICOLON",
        "COLON",
        "COMMA",
        "DOT",
        "ID",
        "INTERGER",
        "STRING",
        "TYPE",
        "NEWLINE"
    ]
    
    return string in terminal

def isVar(string):
    return not isTerminal(string)
        
        

            
            
            