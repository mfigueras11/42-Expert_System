# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 10:29:00 by mfiguera          #+#    #+#              #
#    Updated: 2019/09/19 10:52:12 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class   Config():

    literals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    l_bracket = '('
    r_bracket = ')'
    
    query = '?'
    fact = '='

    implication = '=>'
    subst_impl = '>'
    
    subst_iff = '%'
    iff = '<=>'

    op_xor = '^'
    op_or = '|'
    op_and = '+'
    op_symbols = op_and + op_or + op_xor

    negation = '!'
