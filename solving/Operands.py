# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Operands.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 18:58:52 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/17 19:24:43 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sys.path.insert(1, './solving/')

from Variable import Variable


class Operand(Variable):
    pass


class Logicand(Variable):
    pass


class Logicnot(Variable):

    def __init__(self, term):
        self.term = term
        self.value = None

    def check_value(self):
        return not self.term.check_values()

    # def answer_mode(self, ans):
    #     ans = not ans
    #     self.term.set_value(ans)



class Logicor(Variable):
    pass


class Logicxor(Variable):
    pass
