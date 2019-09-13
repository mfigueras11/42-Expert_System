import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('file', help='path to input file.')
    
    return parser.parse_args()


def clean_line(line):
    return re.sub(r"#.*| |\t|\n", '', line)


def get_clean_instructions(filepath):
    instructions = []

    with open(filepath, 'r') as file:
        for line in file:
            line = clean_line(line)
            if line != '':
                instructions.append(line)
    
    facts = [i for i in range(len(instructions)) if instructions[i][0] == '=']
    queries = [i for i in range(len(instructions)) if instructions[i][0] == '?']

    print(facts[0], (len(instructions) - len(queries) - 1))

    if len(facts) > 1 | facts[0] != (len(instructions) - len(queries) - 1):
        print('ERROR - Facts.')

    return instructions, facts, queries


def eval_file(filepath):
    instructions, facts, queries = get_clean_instructions(filepath)
    print(instructions, facts, queries)
    

def expertsystem():
    args = parse_args()
    eval_file(args.file)
    
if __name__ == "__main__":
    expertsystem()
