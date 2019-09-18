# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/14 18:59:40 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/18 11:51:14 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
import sys

sys.path.insert(1, './structs/')

from Literal import Literal

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Parser():
    
    instructions = []

    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            for line in file:
                line = self.clean_line(line)
                if line != '':
                    self.instructions.append(line)
        
        self.eval_file()


    @staticmethod
    def clean_line(line):
        return re.sub(r"#.*| |\t|\n", '', line)


    def get_clean_instructions(self):
        """"
        Returns list of rules, facts and queries (instructions) as well as the
        list of indexes where queries and facts are (i_queries, i_facts).
        """

        self.i_facts = [i for i in range(len(self.instructions)) if self.instructions[i][0] == '=']
        self.i_queries = [i for i in range(len(self.instructions)) if self.instructions[i][0] == '?']

        if len(self.i_facts) > 1:
            sys.exit('ERROR - Insert just one line with facts.')
        if len(self.i_queries) == 0:
            sys.exit('ERROR - Insert at least one line with queries.')
        if len(self.i_facts) == 1 and self.i_facts[0] != len(self.instructions) - len(self.i_queries) - 1:
            sys.exit('ERROR - Facts must be between rules and queries.')


    @staticmethod
    def get_individual_list(collection):
        """
        Verifies that queries and fact lines have the proper forat and returns
        the string(s) as a list of single variables.
        """

        for c in collection:
            if re.match(r"^[?=]([A-Z])+$", c) == None:
                sys.exit('ERROR - Only capital letters and corresponding symbol at the beggining in queries and facts')
        return(re.sub(r"(?<=[A-Z])|[=?]", ' ', ''.join(collection)).strip().split(' '))


    def sort_instructions(self):
        """
        Separates all the actual instructions in the input file into rules, facts
        and queries, while making sure that everything is OK.
        """

        exclude = self.i_facts + self.i_queries

        facts = [self.instructions[i] for i in self.i_facts]
        self.facts = self.get_individual_list(facts)

        queries = [self.instructions[i] for i in self.i_queries]
        self.queries = self.get_individual_list(queries)

        self.rules = [self.instructions[i] for i in range(len(self.instructions)) if i not in exclude]
    
    
    def generate_variables(self):
        # TODO: find the good way of storing the information, thought of a "tree"
        # of operations that puts everything alltogether
        for rule in self.rules:
            tmpvars = [Literal.fromliteral(letter) for letter in rule if letter in ALPHABET]


    def eval_file(self):
        self.get_clean_instructions()
        self.sort_instructions()
        self.generate_variables()
        Literal.init_true(self.facts)
        Literal.display_all_info()

