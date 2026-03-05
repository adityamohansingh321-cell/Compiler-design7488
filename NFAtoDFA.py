#3

def main():
    n = int(input("Enter number of NFA states: "))
    m = int(input("Enter number of input symbols: "))

    # Input NFA transitions
    nfa = [[[] for _ in range(m)] for _ in range(n)]
    print("\nEnter NFA transitions (enter -1 to stop):")
    for i in range(n):
        for j in range(m):
            temp = []
            while True:
                s = input(f"From state {i} on input {j}: ")
                nums = list(map(int, s.strip().split()))
                for num in nums:
                    if num == -1:
                        break
                    temp.append(num)
                if -1 in nums:
                    break
            nfa[i][j] = temp

    # Subset construction for DFA
    dfa_states = []
    dfa_trans = []
    start_state = frozenset([0])
    dfa_states.append(start_state)
    dfa_trans.append([None]*m)

    i = 0
    while i < len(dfa_states):
        current = dfa_states[i]
        trans_row = []
        for j in range(m):
            new_set = set()
            for state in current:
                new_set.update(nfa[state][j])
            if new_set:
                new_set_frozen = frozenset(new_set)
                if new_set_frozen not in dfa_states:
                    dfa_states.append(new_set_frozen)
                    dfa_trans.append([None]*m)
                trans_row.append(dfa_states.index(new_set_frozen))
            else:
                trans_row.append(None)
        dfa_trans[i] = trans_row
        i += 1

    # Print DFA States
    print("\nDFA States:")
    for idx, s in enumerate(dfa_states):
        print(f"Q{idx} = {{ {' '.join(map(str, s))} }}")

    # Print DFA Transition Table
    print("\nDFA Transition Table:")
    header = "State\t" + "\t".join([f"Input{i}" for i in range(m)])
    print(header)
    for idx, row in enumerate(dfa_trans):
        row_str = "\t".join([f"Q{v}" if v is not None else "-" for v in row])
        print(f"Q{idx}\t{row_str}")


if __name__ == "__main__":
    main()
