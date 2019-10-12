# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Variable.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 09:37:12 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/12 18:35:25 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class   Variable():
    unchangable = set()

    def __init__(self):
        self.val = False
        self.certain = False
        self.precedents = []


    def set_val(self, cert, newval):
        if not self.certain:
            ##add ambiguous tag
            self.val = newval
            self.certain = cert
        elif newval != self.val and cert:
            sys.exit('ERROR - Non solvable system.{}'.format(self.get_error_unsolvable()))


    def read_val(self):
        if not self.certain:
            self.operate()
        return self.certain, self.val

    
    def get_error_unsolvable(self):
        return ""

    
    def add_precedent(self, precedent):
        self.precedents.append(precedent)
    
  
    def operate(self):
        pass
