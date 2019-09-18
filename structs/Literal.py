# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Literal.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 18:36:48 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/18 11:51:00 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sys.path.insert(1, './structs/')

from Variable import Variable


class Literal(Variable):
    literals = {}

    def __init__(self, literal):
        super().__init__()
        self.literal = literal

    @classmethod
    def name(cls):
        return "Literal"

    @classmethod
    def fromliteral(cls, literal):
        if literal not in cls.literals:
            newvariable = cls(literal)
            cls.literals[literal] = newvariable

            return newvariable
        else:
            cls.get_var(literal)


    @classmethod
    def get_var(cls, literal):
        return cls.literals[literal]


    def get_name_val(self):
        return '{} - {}'.format(self.literal, str(self.read_val()))

    @classmethod
    def display_info(cls, varnames):
        info = [var.get_name_val() for name, var in cls.literals.items() if name in varnames]
        info.sort()
        print("\n".join(info))

    
    @classmethod
    def display_all_info(cls):
        cls.display_info(cls.literals.keys())


    @classmethod
    def init_true(cls, variables):
        for var in variables:
            cls.literals[var].set_val(True)

    def get_error_unsolvable(self):
        return ' {} {} with conflicting values.'.format(self.name(), self.literal)
