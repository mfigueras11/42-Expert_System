# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expertsystem.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/14 19:00:04 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/21 13:42:50 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import re
import sys

sys.path.extend(["./parsing/", "./structs/", "./config/"])

from Parser import Parser
from Lexer import Lexer
from Translator import Translator


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', help='path to input file.')

    return parser.parse_args()


def expertsystem():
    args = parse_args()
    parser = Parser(args.file)
    lexer = Lexer(parser.raw_rules)
    if lexer.check():
        translator = Translator(parser.raw_rules, parser.raw_facts, parser.raw_queries)
        translator.translate()
    for rule in translator.rules:
        print(rule.display())


if __name__ == "__main__":
    expertsystem()
