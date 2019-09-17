# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Variable.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 09:37:12 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/17 11:22:07 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class Variable():
    literals = {}

    def __init__(self, literal):
        #could add permanent value here and update when check_value is run
        self.literal = literal
        
        self.true = None
        self.false = 0

    @classmethod
    def fromliteral(cls, literal):
        if literal not in cls.literals:
            newvariable = cls(literal)
            cls.literals[literal] = newvariable

            return newvariable
        else:
            return cls.literals[literal]


    def get_info(self):
        return self.literal + ' - ' + str(self.check_value())


    @classmethod
    def display_info(cls, varnames):
        info = [var.get_info() for name, var in cls.literals.items() if name in varnames]
        info.sort()
        print("\n".join(info))

    
    @classmethod
    def display_all_info(cls):
        cls.display_info(cls.literals.keys())


    @classmethod
    def init_true(cls, variables):
        for var in variables:
            cls.literals[var].set_value(True)


    def set_value(self, newval):
        if newval == True:
            self.true = 1
        elif newval == False:
            self.false = 1
        return self.check_value()


    def check_value(self):
        if self.true == self.false:
            sys.exit('ERROR - Non solvable system. Variable ' + self.literal + ' with conflicting values.')
        elif self.true == 1:
            return True
        else:
            return False
    