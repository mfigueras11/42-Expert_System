# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Assigners.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/18 11:58:06 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/18 12:05:47 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class   Assigners():
    """
    Assigners can only contain two terms and make sure that the relation between
    these two is correctly mantained
    """

    def __init__(self, left_term, right_term):
        self.left_term = left_term
        self.right_term = right_term



class   Implies(Assigners):
    pass



class   Ifandonlyif(Assigners):
    pass
