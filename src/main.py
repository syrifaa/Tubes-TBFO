from argparse import ArgumentParser
from file_pros import createToken
from grammar_pros import read_cfg
from grammar_conv import CFG2CNF
from parser_grammar import parser_CYK

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("nama_file", type=str, help="Nama File yang hendak diparse.")

    args = argument_parser.parse_args()

    # print(createToken(args.nama_file))
    
    # print(read_cfg("grammar.txt"))

    # print(CFG2CNF(read_cfg("grammar.txt")))

    if parser_CYK(CFG2CNF(read_cfg("src/grammar.txt")), createToken(args.nama_file)):
        print("Accepted")
    else:
        print("Syntax Error")