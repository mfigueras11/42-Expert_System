# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expertsystem.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/14 19:00:04 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/17 18:53:22 by mfiguera         ###   ########.fr        #
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
    parser = argparse.ArgumentParser()

    parser.add_argument('file', help='path to input file.')

    return parser.parse_args()


def process_input():
    request = input("Please enter instruction: (X to exit)\n").capitalize()
    if request == "X":
        print("Exitting program.")
        return False
    if request != '':
        line_type, line = Parser.single_line(request)

    return True



def expertsystem():
    args = parse_args()
    parser = Parser(args.file)
    lexer = Lexer(parser.raw_rules)
    if lexer.check():
        translator = Translator(parser.raw_rules, parser.raw_facts, parser.raw_queries)
        translator.translate()
    for query in translator.queries:
        print(query.get_name_val())
    if config.interactive:
        while process_input:
            _ = 1
                


if __name__ == "__main__":
    expertsystem()
