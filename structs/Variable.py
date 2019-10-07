# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Variable.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 09:37:12 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/07 18:54:19 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class   Variable():
    unchangable = set()

    def __init__(self):
        #could add permanent value here and update when check_value is run
        self.val = False
        self.certain = False
        self.precedents = []


    def set_val(self, newval):
        if not self.certain:
            self.val = newval
            self.certain = True
        elif newval != self.val:
            sys.exit('ERROR - Non solvable system.{}'.format(self.get_error_unsolvable()))


    def read_val(self):
        if not self.certain:
            self.solve()
        return self.certain, self.val

    
    def get_error_unsolvable(self):
        return ""

    
    def add_precedent(self, precedent):
        self.precedents.append(precedent)
    
    def solve(self):
        pass
