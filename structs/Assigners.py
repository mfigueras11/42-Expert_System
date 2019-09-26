# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Assigners.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/18 11:58:06 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/26 11:36:02 by mfiguera         ###   ########.fr        #
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


    def display(self):
        return self.left_term.display() + self.symbol + self.right_term.display()


class   Implies(Assigners):
    symbol = config.implication

    def list_vars(self):
        return self.left_term.list_vars(), self.right_term.list_vars()
    

class   Iff(Assigners):
    symbol = config.iff

    def list_vars(self):
        return [], self.left_term.list_vars() + self.right_term.list_vars()
