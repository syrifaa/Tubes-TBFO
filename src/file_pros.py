import sys
import re

defineTerminal = [
    (r'[ \t]+',     None),
    (r'#[^\n]*',    None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
    (r'\"[^\"\n]*\"', "STRING"),
    (r'\'[^\'\n]*\'', "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INTEGER"),
    (r'[\+\-]?[1-9][0-9]+',     "INTEGER"),
    (r'[\+\-]?[0-9]',           "INTEGER"),
    (r'\n',     "NEWLINE"),
    (r'\(',     "OPEN_ROUND_BRACKET"),
    (r'\)',     "CLOSE_ROUND_BRACKET"),
    (r'\{',     "OPEN_CURLY_BRACKET"),
    (r'\}',     "CLOSE_CURLY_BRACKET"),
    (r'\;',     "SEMICOLON"), 
    (r'\:',     "COLON"),
    (r'\,',     "COMMA"),
    # Arithmetic Operator
    (r'\*\*',   "POWER"),
    (r'\*=',    "MULTIPLY_EQUAL"),
    (r'/=',     "DIVIDE_EQUAL"),
    (r'\+=',    "PLUS_EQUAL"),
    (r'-=',     "MINUS_EQUAL"),
    (r'%=',     "MODULO_EQUAL"),
    (r'\+',     "PLUS"),
    (r'\-',     "MINUS"),
    (r'\*',     "MULTIPLY"),
    (r'/',      "DIVIDE"),
    (r'%',      "MODULO"),
    # Logical Operator
    (r'<=',         "LESS_EQUAL"),
    (r'<',          "LESS"),
    (r'>=',         "GREATER_EQUAL"),
    (r'>',          "GREATER"),
    (r'!=',         "NOT_EQUAL"),
    (r'!==',        "STRICT_NOT_EQUAL"),
    (r'\==',        "IS_EQUAL"),
    (r'\===',       "STRICT_EQUAL"),
    (r'\=(?!\=)',   "EQUAL"),
    (r'\&\&',   "AND"),
    (r'\|\|',   "OR"),
    (r'!',      "NOT"),
    # Keyword
    (r'\bif\b',         "IF"),
    (r'\bswitch\b',     "SWITCH"),
    (r'\bcase\b',       "CASE"),
    (r'\bdefault\b',    "DEFAULT"),
    (r'\bthrow\b',      "THROW"),
    (r'\belse\b',       "ELSE"),
    (r'\bfor\b',        "FOR"),
    (r'\bwhile\b',      "WHILE"),
    (r'\bbreak\b',      "BREAK"),
    (r'\bcontinue\b',   "CONTINUE"),
    (r'\bfalse\b',      "FALSE"),
    (r'\btrue\b',       "TRUE"),
    (r'\bNone\b',       "NONE"),
    (r'\bfunction\b',   "FUNCTION"),
    (r'\breturn\b',     "RETURN"),
    (r'\bconst\b',      "CONST"),
    (r'\blet\b',        "LET"),
    (r'\bvar\b',        "VAR"),
    (r'\btry\b',        "TRY"),
    (r'\bcatch\b',      "CATCH"),
    (r'\bfinally\b',    "FINALLY"),
    (r'\bdelete\b',     "DELETE"),
    (r'\bnull\b',       "NULL"),
    (r'\w+[.]\w+',      "DOT"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "VARIABLE"),
]


token1 = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
token2 = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def word2token(word, defineTerminal):
    count = 0
    position = 1
    row = 1
    tokens = []
    while count < len(word):
        if word[count] == '\n':
            row += 1
        valid = None

        for x in defineTerminal:
            pattern, tag = x
            if row == 1:
                if pattern == token1:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == token2:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regEx = re.compile(pattern)
            valid = regEx.match(word, count)
            if valid:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if valid:
            count = valid.end(0)
        else:
            print("Syntax Error")
            sys.exit(1)
        position += 1
    return tokens

def createToken(text):
    file = open(text)
    char = file.read()
    file.close()

    tokens = word2token(char,defineTerminal)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)

    return " ".join(tokenArray)