import collections

def compute_first(symbol, grammar, first_sets):
    if symbol in first_sets:
        return first_sets[symbol]
    
    # Base Case: If symbol is a Terminal (lowercase or special char)
    if not symbol.isupper() and symbol != 'ε':
        return {symbol}

    first = set()
    for production in grammar.get(symbol, []):
        if production == 'ε':
            first.add('ε')
        else:
            for char in production:
                res = compute_first(char, grammar, first_sets)
                if 'ε' not in res:
                    first.update(res)
                    break
                else:
                    # If epsilon is in FIRST, move to next char in production
                    first.update(res - {'ε'})
            else:
                # If we reached the end and all had epsilon, add epsilon to FIRST
                first.add('ε')
    
    first_sets[symbol] = first
    return first

def compute_follow(nt, grammar, first_sets, follow_sets, start_symbol):
    if nt in follow_sets:
        return follow_sets[nt]
    
    follow = set()
    if nt == start_symbol:
        follow.add('$') # End of string marker

    for head, prods in grammar.items():
        for p in prods:
            if nt in p:
                # Find all occurrences of nt in the production
                indices = [i for i, x in enumerate(p) if x == nt]
                for idx in indices:
                    remainder = p[idx + 1:]
                    if remainder:
                        # Follow(nt) includes First(remainder)
                        for char in remainder:
                            f_next = compute_first(char, grammar, first_sets)
                            follow.update(f_next - {'ε'})
                            if 'ε' not in f_next:
                                break
                        else:
                            # If entire remainder is nullable, add Follow(head)
                            if head != nt:
                                follow.update(compute_follow(head, grammar, first_sets, follow_sets, start_symbol))
                    else:
                        # If nt is at the end, add Follow(head)
                        if head != nt:
                            follow.update(compute_follow(head, grammar, first_sets, follow_sets, start_symbol))
    
    follow_sets[nt] = follow
    return follow

def check_ll1(grammar, first_sets, follow_sets):
    print("\n--- LL(1) Consistency Check ---")
    is_ll1 = True
    for nt, productions in grammar.items():
        if len(productions) < 2: continue
        
        # Check for overlapping First sets
        first_of_prods = []
        for p in productions:
            p_first = set()
            if p == 'ε': p_first.add('ε')
            else:
                for char in p:
                    f = compute_first(char, grammar, first_sets)
                    p_first.update(f - {'ε'})
                    if 'ε' not in f: break
                else: p_first.add('ε')
            first_of_prods.append(p_first)

        for i in range(len(first_of_prods)):
            for j in range(i + 1, len(first_of_prods)):
                inter = first_of_prods[i] & first_of_prods[j]
                if inter:
                    print(f"Conflict in {nt}: {first_of_prods[i]} ∩ {first_of_prods[j]}")
                    is_ll1 = False

        # If nullable, First(nt) and Follow(nt) must be disjoint
        if 'ε' in first_sets[nt]:
            inter = first_sets[nt] & follow_sets[nt]
            if inter - {'ε'}:
                print(f"Conflict in {nt}: FIRST and FOLLOW overlap at {inter}")
                is_ll1 = False

    print("Result: Grammar is LL(1)" if is_ll1 else "Result: Grammar is NOT LL(1)")

# Define Grammar (E=Expression, R=E', T=Term, Y=T', F=Factor)
grammar = {
    'E': ['TR'],
    'R': ['+TR', 'ε'],
    'T': ['FY'],
    'Y': ['*FY', 'ε'],
    'F': ['(E)', 'i']
}

first_sets = {}
follow_sets = {}

print("Grammar Loaded:", grammar)
print("\n--- FIRST Sets ---")
for nt in grammar:
    print(f"FIRST({nt}): {compute_first(nt, grammar, first_sets)}")

print("\n--- FOLLOW Sets ---")
for nt in grammar:
    print(f"FOLLOW({nt}): {compute_follow(nt, grammar, first_sets, follow_sets, 'E')}")

check_ll1(grammar, first_sets, follow_sets)
