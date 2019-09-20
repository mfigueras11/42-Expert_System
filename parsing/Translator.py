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


    def _split_rule(self, rule):
        if config.subst_iff in rule:
            return [self._generate_variables(stc) for stc in rule.split(config.subst_iff)], False
        else:
            return [self._generate_variables(stc) for stc in rule.split(config.subst_impl)], True


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
    def _substitute(stc, i, j, val):
        return stc[:i] + [val] + stc[j+1:]


    def _bracket(self, stc, i):
        cb = self._closing_bracket(stc[i:])
        return self._substitute(stc, i, i + cb, self.process_sentence(stc[i + 1:i + cb]))


    def _negation(self, stc, i):
        return self._substitute(stc, i, i + 1, Logicnot(stc[i+1]))

    
    @staticmethod
    def _flood_signs(stc, op):
        no = 0
        ret = []
        for i, c in enumerate(stc):
            if c == op:
                no = 0
            else:
                no += 1
            if no == 1:
                ret.append(c)
            if no > 1:
                return i, ret
        return i, ret

    
    def _op_and(self, stc, i):
        j, operands = self._flood_signs(stc[i - 1 :], config.op_and)
        return self._substitute(stc, i - 1, i + j, Logicand(operands))

    
    def _op_or(self, stc, i):
        j, operands = self._flood_signs(stc[i - 1 :], config.op_or)
        return self._substitute(stc, i - 1, i + j, Logicor(operands))

    def _op_xor(self, stc, i):
        return self._substitute(stc, i - 1, i + 1, Logicxor(stc[i - 1 : i + 1 : 2]))


    def process_sentence(self, stc):
        ops = [
            (config.l_bracket, self._bracket),
            (config.negation, self._negation),
            (config.op_and, self._op_and),
            (config.op_or, self._op_or),
            (config.op_xor, self._op_xor)
        ]
        while True: #Change to while True
            print(stc)
            if len(stc) == 1:
                return stc[0]
            for op_c, op_do in ops:
                # print("Looking at " + op_c)
                for i, c in enumerate(stc):
                    print(op_c, c)
                    if c == op_c:
                        stc = op_do(stc, i)
                        break
                else:
                    continue
                break

    
    @staticmethod 
    def _generate_variables(sentence):
        return [Literal.fromliteral(letter) if letter in config.literals else letter for letter in sentence]
        

    def process_rule(self, rule):
        sentences, isimply = self._split_rule(rule)

        # sentences = [self.process_sentence(self.generate_variables(sentence)) for sentence in sentences]
        sentences = [self.process_sentence(list(sentence)) for sentence in sentences]

        
        if isimply:
            return Implies(*sentences)
        else:
            return Iff(*sentences)
