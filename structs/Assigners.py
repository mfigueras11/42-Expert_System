# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Assigners.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/18 11:58:06 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/22 18:41:33 by mfiguera         ###   ########.fr        #
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


    def display(self):
        return self.left_term.display() + self.symbol + self.right_term.display()


    def list_vars(self):
        return self.left_term.list_vars(), self.right_term.list_vars()

    def solve(self):
        if not self.solved:
            print(self.display())
            self.solved = True
            cert, val = self.left_term.read_val()
            if val == True:
                self.right_term.assign(cert, True)

    def wipe(self):
        impacted = self.right_term.list_vars()
        for var in impacted:
            var.wipe()



class   Implies(Assigners):
    symbol = config.implication



class   Iff(Assigners):
    symbol = config.iff
