# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/14 18:59:40 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/24 11:27:54 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
import sys

from Literal import Literal
from Assigners import Implies, Iff
from Config import Config as config
from Lexer import Lexer


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
        line = re.sub(r"#.*| |\t|\n", '', line)
        line = re.sub(config.iff, config.subst_iff, line)
        line = re.sub(config.implication, config.subst_impl, line)
        return line


    def get_clean_instructions(self):
        """"
        Returns list of rules, facts and queries (instructions) as well as the
        list of indexes where queries and facts are (i_queries, i_facts).
        """

        self.i_facts = [i for i in range(len(self.instructions)) if self.instructions[i][0] == config.fact]
        self.i_queries = [i for i in range(len(self.instructions)) if self.instructions[i][0] == config.query]

        if len(self.i_facts) > 1:
            sys.exit('ERROR - Insert just one line with facts.')
        if len(self.i_queries) == 0 and not config.interactive:
            sys.exit('ERROR - Insert at least one line with queries.')
        if len(self.i_facts) == 1 and self.i_facts[0] != len(self.instructions) - len(self.i_queries) - 1:
            sys.exit('ERROR - Facts must be between rules and queries.')


    @staticmethod
    def get_individual_list(collection):
        """
        Verifies that queries and fact lines have the proper forat and returns
        the string(s) as a list of single variables.
        """
        if len(collection) == 0:
            return []
        for c in collection:
            if re.match(r"^[" + re.escape(config.query + config.fact) + "]([" + re.escape(config.literals) + r"])+$", c) == None:
                sys.exit('ERROR - Only capital letters and corresponding symbol at the beggining in queries and facts')
        return(re.sub(r"(?<=[" + re.escape(config.literals) + "])|[" + re.escape(config.query + config.fact) + "]", ' ', ''.join(collection)).strip().split(' '))


    def sort_instructions(self):
        """
        Separates all the actual instructions in the input file into rules, facts
        and queries, while making sure that everything is OK.
        """

        exclude = self.i_facts + self.i_queries

        facts = [self.instructions[i] for i in self.i_facts]
        self.raw_facts = self.get_individual_list(facts)

        queries = [self.instructions[i] for i in self.i_queries]
        self.raw_queries = self.get_individual_list(queries)

        self.raw_rules = [self.instructions[i] for i in range(len(self.instructions)) if i not in exclude]
    
        
    def eval_file(self):
        self.get_clean_instructions()
        self.sort_instructions()


    @classmethod
    def single_line(cls, line):
        if line[0] == config.query:
            return config.query_type, cls.get_individual_list([cls.clean_line(line)])
        elif line[0] == config.fact:
            return config.fact_type, cls.get_individual_list([cls.clean_line(line)])
        else:
            return config.rule_type, cls.clean_line(line)


