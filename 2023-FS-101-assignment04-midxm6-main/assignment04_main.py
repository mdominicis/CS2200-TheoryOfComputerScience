from automata.fa.nfa import NFA

example_nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'': {'q1', 'q2'}},
        'q1': {'0': {'q1'}, '1': {'q2'}},
        'q2': {'0': {'q1'}, '1': {'q2'}}
    },
    initial_state='q0',
    final_states={'q1'}
)

example_nfa_regex = "(1*0)?(11*0|0)*"

prob_1_21a = "a*(ba*ba*)*ba*"
prob_1_21b = "()|(a|b)(a|bb|ba(b|a))*(b|ba)"



prob_1_28a = NFA(
    states={'1', '2', '3','4','5','6'},
    input_symbols={'a', 'b'},
    transitions={
        '1': {'b': {'6'},'a':{'2'}},
        '2': {'':{'5'},'a':{'3'}},
        '3': {'b':{'4'}},
        '4':{'b':{'5'}},
        '5':{'':{'2','6'}}
    },
    initial_state='1',
    final_states={'6'}
)

prob_1_28b = NFA(
    states={'1', '2', '3','4'},
    input_symbols={'a', 'b'},
    transitions={
        '1': {'a': {'2','3'}},
        '2': {'a':{'2'}},
        '3': {'b':{'4'}},
        '4':{'a':{'3'}},
    },
    initial_state='1',
    final_states={'2','4'}
)

prob_1_28c = NFA(
    states={'1', '2', '3','4','5','6','7'},
    input_symbols={'a', 'b'},
    transitions={
        '1': {'a': {'2'},'b':{'5'}},
        '2': {'a':{'3'}},
        '3': {'a':{'3'},'b':{'4'}},
        '4':{'b':{'4'}},
        '5':{'b':{'5'},'a':{'6'}},
        '6':{'a':{'6'},'b':{'7'}},
        '7':{'b':{'7'}}
    },
    initial_state='1',
    final_states={'4','7'}
)
