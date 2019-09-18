# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Operands.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 18:58:52 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/18 11:59:10 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sys.path.insert(1, './structs/')

from Variable import Variable


class   Logicnot(Variable):
    """
    Logic gate NOT
    Allows one input and one output. Output is True if input is False and viceversa
    """

    def __init__(self, term):
        super().__init__()
        self.term = term


    def read_val(self):
        if self.term.certain:
            return not self.term.read_val()


    # def answer_mode(self, ans):
    #     ans = not ans
    #     self.term.set_val(ans)



class   Logicand(Variable):
    """
    Logic gate AND
    Allows 2+ inputs and one output. Output is True only if all inputs are True
    """

    def __init__(self, terms):
        super().__init__()
        self.terms = terms


    def read_val(self):
        if all(term.certain == True for term in self.terms):
            return all(term.val == True for term in self.terms)
        elif any(term.certain == True and term.val == False for term in self.terms):
            return False


    # def answer_mode(self, ans):
    #     ans = not ans
    #     self.term.set_val(ans)



class   Logicor(Variable):
    """
    Logic gate AND
    Allows 2+ inputs and one output. Output is True if at least one of the inputs is True
    """
    
    def __init__(self, terms):
        super().__init__()
        self.terms = terms


    def read_val(self):
        if all(term.certain == True for term in self.terms):
            return any(term.val == True for term in self.terms)
        elif any(term.certain == True and term.val == True for term in self.terms):
            return True



class   Logicxor(Variable):
    """
    Logic gate XOR
    Allows 2 inputs and one output. Output is True if inputs are not equal
    """
    
    pass
