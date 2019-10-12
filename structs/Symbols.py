# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Symbols.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 18:58:52 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/12 18:41:50 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sys.path.insert(1, './structs/')

from Variable import Variable


class   Symbol(Variable):

    def list_vars(self):
        return [var for term in self.terms for var in term.list_vars()]

    def assign(self, cert, val):
        sys.exit('ERROR - Only and and not symbols allowed at assignments')
        pass




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


    def operate(self):
        cert, val = self.term.read_val()
        newval = not val
        self.set_val(cert, newval)
    
    def display(self):
        return "NOT(" + self.term.display() + ")"

    def assign(self, cert, val):
        if val == True or val == False:
            notval = not val
            self.term.assign(cert, notval)




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


    def operate(self):
        certain = []
        values = []
        for term in self.terms:
            cert, val = term.read_val()
            if cert == True and val == False:
                self.set_val(True, False)
                return
            values.append(val)
            certain.append(cert)
        
        self.set_val(all(certain), all(values))
        

    def assign(self, cert, val):
        if val == True:
            for term in self.terms:
                term.assign(cert, True)
        elif val == False:
            for term in self.terms:
                term.assign(cert, None)


    def display(self):
        return "AND(" + ",".join([term.display() for term in self.terms]) + ")"




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


    def operate(self):
        certain = []
        values = []
        for term in self.terms:
            cert, val = term.read_val()
            if cert == True and val == True:
                self.set_val(True, True)
                return
            values.append(val)
            certain.append(cert)
        
        self.set_val(all(certain), any(values))


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


    def operate(self):
        cert1, var1 = self.term1.read_val()
        cert2, var2 = self.term2.read_val()
        self.set_val(all([cert1, cert2]), var1 != var2)


    def display(self):
        return "XOR(" + self.term1.display() + "," + self.term2.display() + ")"
