# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Translator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 11:54:51 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/19 18:43:33 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from Assigners import Implies, Iff
from Symbols import Logicand, Logicnot, Logicor, Logicxor
from Config import Config as config
from Literal import Literal

class   Translator():
    """
    Contains methods related to the conversion of char rules to the appropiate
    structures
    """
    
    def __init__(self, rules, facts, queries):
        self.rules = rules
        self.facts = facts
        self.queries = queries


    def update_queries_facts(self):
        self.facts = [Literal.fromliteral(c) for c in self.facts]
        self.queries = [Literal.fromliteral(c) for c in self.queries]


    def translate(self):
        processed_rules = []

        self.generate_variables()
        
        for rule in self.rules:
            processed_rules.append(self.process_rule(rule))


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
        pass

    
    def generate_variables(self):
        rules = []
        for rule in self.rules:
            tmpvars = [Literal.fromliteral(letter) if letter in config.literals else letter for letter in rule]
            rules.append(tmpvars)
        self.rules = rules
        

    def process_rule(self, rule):
        sentences, isimply = self.split_rule(rule)

        sentences = [self.process_sentence(sentence) for sentence in sentences]
        
        if isimply:
            return Implies(*sentences)
        else:
            return Iff(*sentences)
