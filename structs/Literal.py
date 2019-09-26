# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Literal.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 18:36:48 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/26 11:57:11 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Variable import Variable


class   Literal(Variable):
    literals = {}

    def __init__(self, literal):
        super().__init__()
        self.literal = literal


    @classmethod
    def fromliteral(cls, literal):
        if literal not in cls.literals:
            newvariable = cls(literal)
            cls.literals[literal] = newvariable

            return newvariable
        else:
            return cls.get_var(literal)


    def list_vars(self):
        return [self]


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


    def display(self):
        return self.literal


    @classmethod
    def init_true(cls, variables):
        for var in variables:
            cls.literals[var].set_val(True)


    def get_error_unsolvable(self):
        return ' Literal {} with conflicting values.'.format(self.literal)
