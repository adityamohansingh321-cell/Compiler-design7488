# Experiment 3: Regular Expression to NFA (Thompson's Construction)
# Supports postfix expressions

state_count = 0

class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.transitions = []

def symbol(c):
    global state_count
    n = NFA(state_count, state_count+1)
    n.transitions.append((n.start, c, n.end))
    state_count += 2
    return n

def concatenate(n1, n2):
    # Connect n1.end to n2.start via epsilon
    n1.transitions.append((n1.end, 'ε', n2.start))
    # Merge transitions
    n1.transitions.extend(n2.transitions)
    n1.end = n2.end
    return n1

def unionOp(n1, n2):
    global state_count
    n = NFA(state_count, state_count+1)
    state_count += 2
    # Connect new start to both n1.start and n2.start
    n.transitions.append((n.start, 'ε', n1.start))
    n.transitions.append((n.start, 'ε', n2.start))
    # Connect n1.end and n2.end to new end
    n.transitions.append((n1.end, 'ε', n.end))
    n.transitions.append((n2.end, 'ε', n.end))
    # Merge transitions
    n.transitions.extend(n1.transitions)
    n.transitions.extend(n2.transitions)
    return n

def closure(n1):
    global state_count
    n = NFA(state_count, state_count+1)
    state_count += 2
    n.transitions.append((n.start, 'ε', n1.start))
    n.transitions.append((n.start, 'ε', n.end))
    n.transitions.append((n1.end, 'ε', n1.start))
    n.transitions.append((n1.end, 'ε', n.end))
    n.transitions.extend(n1.transitions)
    return n

def main():
    postfix = input("Enter postfix regular expression: ").strip()
    stack = []

    for c in postfix:
        if c.isalpha():
            stack.append(symbol(c))
        elif c == '.':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(concatenate(n1, n2))
        elif c == '|':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(unionOp(n1, n2))
        elif c == '*':
            n1 = stack.pop()
            stack.append(closure(n1))
        else:
            print(f"Unsupported symbol: {c}")

    result = stack.pop()

    print("\nNFA Transitions:")
    for t in sorted(result.transitions):
        print(f"{t[0]} -- {t[1]} --> {t[2]}")

    print(f"\nStart State: {result.start}")
    print(f"Final State: {result.end}")

if __name__ == "__main__":
    main()
