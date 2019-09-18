# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Variable.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 09:37:12 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/18 12:07:06 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class   Variable():
    unchangable = set()

    def __init__(self):
        #could add permanent value here and update when check_value is run
        self.val = False
        self.certain = False


    def set_val(self, newval):
        if not self.certain:
            self.value = newval
            self.certain = True
        elif newval != self.value:
            sys.exit('ERROR - Non solvable system.{}'.format(self.get_error_unsolvable()))


    def read_val(self):
        if self.certain:
            return self.value
        return None

    
    def get_error_unsolvable(self):
        return ""
