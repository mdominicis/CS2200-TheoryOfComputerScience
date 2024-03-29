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



prob_1_18a = "1.*0"

prob_1_18b = ".*1.*1.*1.*"

prob_1_18c = ".*0101.*"

prob_1_18g = ".{0,5}"

prob_1_18i = "(1(0|1))*(()|1)"

prob_1_18l = "(1*(01*01*)*)|(0*10*10*)"



prob_1_19a = NFA(
    states={'q0', 'q1', 'q2','q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1'}, '1': {'q0'}},
        'q1': {'0': {'q2'}, '1': {'q0'}},
        'q2': {'0': {'q3'}, '1': {'q0'}},
        'q3': {'0': {'q3'}, '1': {'q3'}}
    },
    initial_state='q0',
    final_states={'q3'}
)
#(((00)*(11))|01)*
prob_1_19b = NFA(
    states={'q0', 'q1', 'q2','q3','q4', 'q5', 'q6','q7'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'':{'q1','q4','q3'}},
        'q1': {'0': {'q2'}},
        'q2': {'1': {'q3'}},
        'q3': {'':{'q1','q4'}},
        'q4': {'':{'q6'},'0':{'q5'}},
        'q5': {'0': {'q6'}},
        'q6': {'': {'q4'},'1':{'q7'}},
        'q7': {'1':{'q3'}}
    },
    initial_state='q0',
    final_states={'q3'}
)

prob_1_19c = NFA(
    states={'q0'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'': {'q0'}},
    },
    initial_state='q0',
    final_states={'q0'}
)
