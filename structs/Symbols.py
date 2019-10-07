# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Symbols.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 18:58:52 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/07 19:34:04 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sys.path.insert(1, './structs/')

from Variable import Variable


class   Symbol(Variable):

    def list_vars(self):
        return [var for term in self.terms for var in term.list_vars()]


class   Logicnot(Symbol):
    """
    Logic gate NOT
    Allows one input and one output. Output is True if input is False and viceversa
    """

    def __init__(self, term):
        super().__init__()
        self.terms = [term]
        self.term = term
        term.add_precedent(self)


    def solve(self):
        cert, val = self.term.read_val()
        newval = not val
        if cert:
            self.set_val(newval)
    
    def display(self):
        return "NOT(" + self.term.display() + ")"


    # def answer_mode(self, ans):
    #     ans = not ans
    #     self.term.set_val(ans)


class   Logicand(Symbol):
    """
    Logic gate AND
    Allows 2+ inputs and one output. Output is True only if all inputs are True
    """

    def __init__(self, terms):
        super().__init__()
        self.terms = terms
        for term in terms:
            term.add_precedent(self)


    def solve(self):
        certain = []
        values = []
        for term in self.terms:
            cert, val = term.read_val()
            if cert == True and val == False:
                self.set_val(False)
                return
            values.append(val)
            certain.append(cert)
        
        if all(certain):
            self.set_val(all(values))
        

    
    def display(self):
        return "AND(" + ",".join([term.display() for term in self.terms]) + ")"


    # def answer_mode(self, ans):
    #     ans = not ans
    #     self.term.set_val(ans)



class   Logicor(Symbol):
    """
    Logic gate AND
    Allows 2+ inputs and one output. Output is True if at least one of the inputs is True
    """
    
    def __init__(self, terms):
        super().__init__()
        self.terms = terms
        for term in terms:
            term.add_precedent(self)


    def solve(self):
        certain = []
        values = []
        for term in self.terms:
            cert, val = term.read_val()
            if cert == True and val == True:
                self.set_val(True)
                return
            values.append(val)
            certain.append(cert)
        
        if all(certain):
            self.set_val(any(values))

    # def read_val(self):
    #     if any([term.certain == True and term.val == True for term in self.terms]):
    #         self.certain = True
    #         self.val = True
    #         return True
    #     elif:
    #         self.val = any([term.val == True for term in self.terms])


    def display(self):
        return "OR(" + ",".join([term.display() for term in self.terms]) + ")"




class   Logicxor(Symbol):
    """
    Logic gate XOR
    Allows 2 inputs and one output. Output is True if inputs are not equal
    """

    def __init__(self, term1, term2):
        super().__init__()
        self.terms = [term1, term2]
        self.term1 = term1
        self.term2 = term2
        for term in [term1, term2]:
            term.add_precedent(self)

    def solve(self):
        cert1, var1 = self.term1.read_val()
        cert2, var2 = self.term2.read_val()
        if all([cert1, cert2]):
            self.set_val(var1 != var2)


    def display(self):
        return "XOR(" + self.term1.display() + "," + self.term2.display() + ")"
