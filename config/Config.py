# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 10:29:00 by mfiguera          #+#    #+#              #
#    Updated: 2019/10/24 11:55:01 by mfiguera         ###   ########.fr        #
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
    
    iff = '<=>'
    subst_iff = '%'

    subst_symbols = subst_impl + subst_iff

    op_xor = '^'
    op_or = '|'
    op_and = '+'
    op_symbols = op_and + op_or + op_xor

    negation = '!'

    query_type = 1
    fact_type = 2
    rule_type = 3

    interactive = None
    verbose = None
