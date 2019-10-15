# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Lexer.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 10:09:22 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/15 17:03:04 by mfiguera         ###   ########.fr        #
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
            balanced, error = self.is_balanced(rule)
            if not balanced:
                sys.exit(rule+"\nERROR - " + error)
        return True

    @staticmethod
    def is_balanced(rule):
        brackets = 0
        variables = 0
        
        if rule.count(config.subst_iff) + rule.count(config.subst_impl) != 1:
            return False, "Wrong number of assigners."

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
                if (i + 1 < len(rule) and (rule[i + 1] not in config.literals and rule[i + 1] != config.l_bracket))or i + 1 > len(rule):
                    return False, "Negation in the wrong place."
            
            if brackets < 0 or variables > 1:
                return False, "Wrong syntax."
                
        if brackets != 0 or variables != 1:
            return False, "Wrong syntax."
        
        if rule.count(config.subst_iff) == 1:
            for c in rule:
                if c not in config.literals and c != config.subst_iff and c != config.op_and:
                    return False, "Invalid operator in If and only if statement."
        else:
            conclusion = rule.split(config.subst_impl)[1]
            for c in conclusion:
                if c not in config.literals and c != config.op_and:
                    return False, "Invalid operator in conclusion."

        return True, "All god"
