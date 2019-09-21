# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Symbols.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 18:58:52 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/21 13:24:26 by mfiguera         ###   ########.fr        #
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
        term.add_precedent(self)


    def read_val(self):
        if self.term.certain:
            return not self.term.read_val()
    
    def display(self):
        return "NOT(" + self.term.display() + ")"


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
        for term in terms:
            term.add_precedent(self)


    def read_val(self):
        if all(term.certain == True for term in self.terms):
            return all(term.val == True for term in self.terms)
        elif any(term.certain == True and term.val == False for term in self.terms):
            return False

    
    def display(self):
        return "AND(" + ",".join([term.display() for term in self.terms]) + ")"


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
        for term in terms:
            term.add_precedent(self)


    def read_val(self):
        if all(term.certain == True for term in self.terms):
            return any(term.val == True for term in self.terms)
        elif any(term.certain == True and term.val == True for term in self.terms):
            return True


    def display(self):
        return "OR(" + ",".join([term.display() for term in self.terms]) + ")"




class   Logicxor(Variable):
    """
    Logic gate XOR
    Allows 2 inputs and one output. Output is True if inputs are not equal
    """

    def __init__(self, term1, term2):
        super().__init__()
        self.term1 = term1
        self.term2 = term2
        for term in [term1, term2]:
            term.add_precedent(self)

    def read_val(self):
        if all([term.certain for term in [self.term1, self.term2]]):
            return self.term1.val != self.term2.val


    def display(self):
        return "XOR(" + self.term1.display() + "," + self.term2.display() + ")"
