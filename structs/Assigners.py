# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Assigners.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/18 11:58:06 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/23 18:50:20 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from Config import Config as config


class   Assigners():
    """
    Assigners can only contain two terms and make sure that the relation between
    these two is correctly mantained
    """

    symbol = None
    
    def __init__(self, left_term, right_term):
        self.left_term = left_term
        self.right_term = right_term
        self.solved = False
        self.val = False
        self.certain = False
        left_term.precedents.append(self)


    def display(self):
        return self.left_term.display() + self.symbol + self.right_term.display()


    def list_vars(self):
        return self.left_term.list_vars(), self.right_term.list_vars()


    def solve(self):
        if not self.solved:
            self.solved = True
            self.certain, self.val = self.left_term.read_val()
            if self.val == True:
                self.right_term.assign(self.certain, True)


    def wipe(self):
        self.solved = False
        impacted = self.right_term.list_vars()
        for var in impacted:
            var.wipe()



class   Implies(Assigners):
    symbol = config.implication



class   Iff(Assigners):
    symbol = config.iff
