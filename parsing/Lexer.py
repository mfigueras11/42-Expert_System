# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Lexer.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 10:09:22 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/19 12:59:17 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from Config import Config as config


class Lexer():
    """
    Contains methods related to the lexic and syntactic evaluation of every rule
    """
    
    def __init__(self, rules):
        self.rules = rules


    def check(self):
        for rule in self.rules:
            if not self.is_balanced(rule):
                sys.exit("ERROR - Unbalanced rule. Make sure brackets are rignt, symbols are in their place and there are the right amount of literals")
        return True


    def is_balanced(self, rule):
        brackets = 0
        variables = 0
        
        if rule.count(config.subst_iff) + rule.count(config.subst_impl) != 1:
            return False, 

        for i, c in enumerate(rule):
            if c == config.l_bracket:
                brackets += 1
            elif c == config.r_bracket:
                brackets -= 1
            elif c in config.literals:
                variables += 1
            elif c in config.op_symbols or c in config.subst_symbols:
                variables -= 1
            elif c == config.negation:
                if (i + 1 < len(rule) and (rule[i + 1] not in config.literals or rule[i + 1] != config.l_bracket))or i + 1 > len(rule):
                    return False
            
            if brackets < 0 or (brackets == 0 and variables != 1):
                return False
                
        if brackets != 0:
            return False
