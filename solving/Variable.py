# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Variable.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 09:37:12 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/17 19:36:30 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class Variable():
    unchangable = set()

    def __init__(self):
        #could add permanent value here and update when check_value is run
        pass
        self.true = None
        self.false = 0


    def set_value(self, newval):
        if newval == True:
            self.true = 1
        elif newval == False:
            self.false = 1
        return self.check_value()


    def check_value(self):
        if self.true == self.false:
            sys.exit('ERROR - Non solvable system. {}'.format(self.get_error_unsolvable()))
        elif self.true == 1:
            return True
        else:
            return False
    
    def get_error_unsolvable(self):
        pass
