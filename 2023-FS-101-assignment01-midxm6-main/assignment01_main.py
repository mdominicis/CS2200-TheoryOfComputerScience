from automata.fa.dfa import DFA

prob_1_3 = DFA(
    states={'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'u', 'd'},
    transitions={
        'q1': {'u': 'q1', 'd': 'q2'},
        'q2': {'u': 'q1', 'd': 'q3'},
        'q3': {'u': 'q2', 'd': 'q4'},
        'q4': {'u': 'q3', 'd': 'q5'},
        'q5': {'u': 'q4', 'd': 'q5'}
    },
    initial_state='q3',
    final_states={'q3'}
)

prob_1_6a = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q0'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q3', '1': 'q2'},
        'q3': {'0': 'q3', '1': 'q2'}
    },
    initial_state='q1',
    final_states={'q3'}
)

# prob_1_6b = DFA(
#     
# )

# prob_1_6c = DFA(
#     
# )

# prob_1_6f = DFA(
#     
# )

# prob_1_6g = DFA(
#     
# )

# prob_1_6h = DFA(
#     
# )

# prob_1_6i = DFA(
#     
# )

# prob_1_6m = DFA(
#     
# )

# prob_1_6n = DFA(
#     
# )
