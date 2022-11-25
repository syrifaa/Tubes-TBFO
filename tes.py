# def read_grammar(nama_file):
#     file = open(nama_file, "r")
#     cfg = {}

#     baris = file.readline()
#     while baris != "":
#         head, body = baris.replace("\n", "").split(" -> ")
        
#         if head not in cfg.keys():
#             cfg[head] = [body.split(" ")]
#         else:
#             cfg[head].append(body.split(" "))

#         baris = file.readline()

#     file.close()

#     return cfg

def read_grammar(filename):
    # Baca cfg dari file
    with open(filename) as cfg:
        lines = cfg.readlines()
    return [x.replace("->", "").split() for x in lines]


print(type(read_grammar("grammar.txt")))