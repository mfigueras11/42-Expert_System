# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expertsystem.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/14 19:00:04 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/24 17:15:47 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import re
import sys

sys.path.extend(["./parsing/", "./structs/", "./config/"])

from Parser import Parser
from Lexer import Lexer
from Translator import Translator
from Literal import Literal
from Config import Config as config


def parse_args():
    parser = argparse.ArgumentParser(description='Program to help solve logic systems.\nIn interactive mode (-i), use "." to print current variable status, "!" to solve all variables, "v" to toggle verbose, and normal query and fact syntax for specific queries and facts.')

    parser.add_argument('file', help='path to input file.')
    parser.add_argument('-i', '--interactive', help='trigger interactive mode.', action='store_true')
    parser.add_argument('-v', '--verbose', help='trigger verbose mode.', action='store_true')

    return parser.parse_args()


def process_input():
    request = input("Please enter instruction: (X to exit)\n").upper()
    if request == "X":
        print("Exiting program.")
        return False
    if request != '':
        line_type, line = Parser.single_line(request)
        if line_type == config.query_type:
            queries = Translator.literalize(line)
            for query in queries:
                if config.verbose:
                    query.solve()
                else:
                    print(query.solve())
        elif line_type == config.fact_type:
            facts = Translator.literalize(line)
            for fact in facts:
                if fact.val == False and fact.locked == True:
                    fact.locked = False
                fact.wipe()
                fact.secure(True)
        elif request == '.':
            Literal.display_all_info()
        elif request == '!':
            Literal.display_all_info_solve()
        elif request == 'V':
            config.verbose = not config.verbose
            print("Verbose is now {}".format(config.verbose))
        else:
            print('Try again.')
    else:
        print('Try again.')

    return True



def expertsystem(file):
    parser = Parser(file)
    lexer = Lexer(parser.raw_rules)
    if lexer.check():
        translator = Translator(parser.raw_rules, parser.raw_facts, parser.raw_queries)
        translator.translate()
    for query in translator.queries:
        print(query.solve())
    if config.interactive:
        while process_input():
            _ = 1



def main():
    args = parse_args()
    config.interactive = args.interactive
    config.verbose = args.verbose
    expertsystem(args.file)



if __name__ == "__main__":
    main()
