def lambda_nfa(word, index, state):
    if index == len(word):
        return state in final_states
    char = word[index]
    change_rules = change_state_rules.get(state)
    if change_rules:
        if change_rules.get(char):
            for final_state in change_rules[char]:
                if lambda_nfa(word, index+1, final_state):
                    return True
        if change_rules.get('$'):
            for final_state in change_rules['$']:
                if lambda_nfa(word, index, final_state):
                    return True
    return False

with open("setup_dfa.in") as file:
    # Data input
    n = int(file.readline())
    m = int(file.readline())
    alfabet = ['$'].extend(file.readline().split())
    q0 = file.readline().strip()
    k = int(file.readline())

    final_states = [state for state in file.readline().split()]
    num_of_trans = int(file.readline())

    # Create automata state rules
    change_state_rules = {}
    for i in range(num_of_trans):
        state_init, char, state_final = file.readline().split()
        if change_state_rules.get(state_init):
            char_final_states = change_state_rules[state_init].get(char)
            if char_final_states:
                change_state_rules[state_init][char].append(state_final)
            else:
                change_state_rules[state_init][char] = [state_final]
        else:
            change_state_rules.update({
                state_init: {
                    char: [state_final]
                }
            })

with open("test_data.in") as file:
    words = [line.strip() for line in file.readlines()]
    for word in words:
        is_accepted = lambda_nfa(word, 0, q0)
        print("Word: {} is {}accepted!".format(word, '' if is_accepted else 'not '))

