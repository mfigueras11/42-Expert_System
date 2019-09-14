import re
import sys


class Parser():
    
    def __init__(self):
        pass        

    @staticmethod
    def clean_line(line):
        return re.sub(r"#.*| |\t|\n", '', line)

    def get_clean_instructions(self, filepath):
        """"
        Returns list of rules, facts and queries (instructions) as well as the
        list of indexes where queries and facts are (i_queries, i_facts).
        """

        instruct = []

        with open(filepath, 'r') as file:
            for line in file:
                line = self.clean_line(line)
                if line != '':
                    instruct.append(line)

        i_facts = [i for i in range(len(instruct)) if instruct[i][0] == '=']
        i_queries = [i for i in range(len(instruct)) if instruct[i][0] == '?']

        if len(i_facts) > 1:
            sys.exit('ERROR - Insert just one line with facts.')
        if len(i_queries) == 0:
            sys.exit('ERROR - Insert at least one line with queries.')
        if len(i_facts) == 1 and i_facts[0] != len(instruct) - len(i_queries) - 1:
            sys.exit('ERROR - Facts must be between rules and queries.')

        return instruct, i_facts, i_queries

    @staticmethod
    def get_individual_list(collection):
        """
        Verifies that queries and fact lines have the proper forat and returns
        the string(s) as a list of single variables.
        """

        for c in collection:
            if re.match(r"^[?=]([A-Z])+$", c) == None:
                sys.exit('ERROR - Only capital letters and corresponding symbol at\
                the beggining in queries and facts')
        return(re.sub(r"(?<=[A-Z])|[=?]", ' ', ''.join(collection)).strip().split(' '))


    def sort_instructions(self, instruct, i_facts, i_queries):
        """
        Separates all the actual instructions in the input file into rules, facts
        and queries, while making sure that everything is OK.
        """

        exclude = i_facts + i_queries

        facts = [instruct[i] for i in i_facts]
        facts = self.get_individual_list(facts)

        queries = [instruct[i] for i in i_queries]
        queries = self.get_individual_list(queries)

        rules = [instruct[i] for i in range(len(instruct)) if i not in exclude]
        # TODO: find the good way of storing the information, thought of a "tree"
        # of operations that puts everything alltogether

        return rules, queries, facts


    def eval_file(self, filepath):
        rules, facts, queries = self.sort_instructions(
            *self.get_clean_instructions(filepath))
        return rules, facts, queries