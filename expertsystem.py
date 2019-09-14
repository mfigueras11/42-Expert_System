# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expertsystem.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/14 19:00:04 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/14 19:00:19 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import re
import sys

sys.path.extend(["./parsing/"])

from Parser import Parser


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', help='path to input file.')

    return parser.parse_args()


def expertsystem():
    args = parse_args()
    expert = Parser(args.file)
    print(expert.rules, expert.facts, expert.queries)


if __name__ == "__main__":
    expertsystem()
