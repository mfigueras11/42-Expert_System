# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/14 18:59:40 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/19 10:59:12 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
import sys

sys.path.insert(1, ['./structs/', './config'])

from Literal import Literal
from Assigners import Implies, Ifandonlyif
from Config import Config as config

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
        rules = []
        for rule in self.rules:
            tmpvars = [Literal.fromliteral(letter) if letter in ALPHABET else letter for letter in rule]
            rules.append(tmpvars)
        return rules
    
    
    
    def split_rule(self, rule):
        if config.subst_iff in rule:
            sentences = rule.split(config.subst_iff)
            isimply = False
        else:
            sentences = rule.split(config.subst_impl)
            isimply = True
        
        if len(sentences) != 2:
            sys.exit("ERROR - Rule could not be splitted properly.")
        
        return sentences, isimply



    def process_sentence(self, sentence):
        brackets = 0
        for i, c in enumerate(sentence):
            if c == config.l_bracket:
                brackets += 1



    def process_rule(self, rule):
        sentences, isimply = self.split_rule(rule)

        sentences = [self.process_sentence(sentence) for sentence in sentences]
        
        if isimply:
            return Implies(*sentences)
        else:
            return Ifandonlyif(*sentences)


        
    
    def eval_file(self):
        self.get_clean_instructions()
        self.sort_instructions()
        self.rules = self.generate_variables()
        Literal.init_true(self.facts)
        Literal.display_all_info()
