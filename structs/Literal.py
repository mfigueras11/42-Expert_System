# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Literal.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 18:36:48 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/24 10:59:40 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Variable import Variable


class   Literal(Variable):
    literals = {}

    def __init__(self, literal):
        super().__init__()
        self.literal = literal
        self.rules = []


    @classmethod
    def fromliteral(cls, literal):
        if literal not in cls.literals:
            newvariable = cls(literal)
            cls.literals[literal] = newvariable

            return newvariable
        else:
            return cls.get_var(literal)


    def display(self):
        return self.literal
    
    
    def list_vars(self):
        return [self]


    @classmethod
    def get_var(cls, literal):
        return cls.literals[literal]


    def solve(self):
        return '{} - {}'.format(self.literal, str(self.read_val()[1])[0])

    
    def get_name_val(self):
        return '{} - {} {} {}'.format(self.literal, str(self.val)[0], str(self.certain)[0], str(self.locked)[0])


    @classmethod
    def display_info(cls, varnames):
        print("Var V C L")
        info = [var.get_name_val() for name, var in cls.literals.items() if name in varnames]
        info.sort()
        print("\n".join(info))


    @classmethod
    def display_info_solve(cls, varnames):
        info = [var.solve() for name, var in cls.literals.items() if name in varnames]
        info.sort()
        print("\n".join(info))

    
    @classmethod
    def display_all_info(cls):
        cls.display_info(cls.literals.keys())


    @classmethod
    def display_all_info_solve(cls):
        cls.display_info_solve(cls.literals.keys())


    @classmethod
    def init_true(cls, variables):
        for var in variables:
            cls.literals[var].secure(True)


    def get_error_unsolvable(self):
        return ' Literal {} with conflicting values.'.format(self.literal)


    def assign(self, cert, val):
        if val == True or val == False:
            self.set_val(cert, val)

    def read_val(self):
        if not self.certain:
            print(self.display() + " <" + " ".join([rule.display() for rule in self.rules]) +">")
            for rule in self.rules:
                rule.solve()
        return self.certain, self.val
