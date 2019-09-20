# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Translator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 11:54:51 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/20 13:00:30 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from Assigners import Implies, Iff
from Symbols import Logicand, Logicnot, Logicor, Logicxor
from Config import Config as config
from Literal import Literal
from Variable import Variable

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
        
        for rule in self.rules:
            processed_rules.append(self.process_rule(rule))

    @staticmethod
    def _split_rule(rule):
        if config.subst_iff in rule:
            return rule.split(config.subst_iff), False
        else:
            return rule.split(config.subst_impl), True

    @staticmethod 
    def _isvariable(var):
        return Variable in type(var).__bases__
    

    @staticmethod 
    def _closing_bracket(string):
        brackets = 0
        for i, c in enumerate(string):
            if c == config.l_bracket:
                brackets += 1
            elif c == config.r_bracket:
                brackets -= 1
            if brackets == 0:
                return i


    @staticmethod
    def _substitute(sentence, i, j, val):
        return sentence[:i] + [val] + sentence[j:]


    def _bracket(self, stc, i):
        cb = self._closing_bracket(stc[i:])
        return self._substitute(stc, i, i + cb, self.process_sentence(stc[i + 1:cb]))


    def process_sentence(self, sentence):
        ops = [
            (config.l_bracket, self._bracket())
        ]
        for a in range(5):
            print(sentence)
            if len(sentence) == 1:
                return sentence[0]
            for i, c in enumerate(sentence):
                if c == config.l_bracket:
                    c_b = self._closing_bracket(sentence[i:])
                    sentence = self._substitute(sentence, i, i + c_b, self.process_sentence(sentence[i+1:i + c_b]))
                    break

    
    @staticmethod 
    def _generate_variables(sentence):
        return [Literal.fromliteral(letter) if letter in config.literals else letter for letter in sentence]
        

    def process_rule(self, rule):
        sentences, isimply = self._split_rule(rule)

        # sentences = [self.process_sentence(self.generate_variables(sentence)) for sentence in sentences]
        sentences = [self.process_sentence(sentence) for sentence in sentences]

        
        if isimply:
            return Implies(*sentences)
        else:
            return Iff(*sentences)
