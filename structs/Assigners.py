# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Assigners.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/18 11:58:06 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/21 13:28:25 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from Config import Config as config


class   Assigners():
    """
    Assigners can only contain two terms and make sure that the relation between
    these two is correctly mantained
    """

    def __init__(self, left_term, right_term):
        self.left_term = left_term
        self.right_term = right_term


    def display(self):
        return self.left_term.display() + self.symbol + self.right_term.display()


class   Implies(Assigners):
    symbol = config.implication
    


class   Iff(Assigners):
    symbol = config.iff

