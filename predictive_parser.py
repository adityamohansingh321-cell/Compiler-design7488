import pandas as pd

def get_user_input_sets(set_type):
    """Utility to take FIRST or FOLLOW sets from user."""
    print(f"\n--- Enter {set_type} Sets ---")
    print(f"Format: NT:symbol1,symbol2 (e.g., E:(,i)")
    user_set = {}
    n = int(input(f"How many Non-Terminals for {set_type}? "))
    for _ in range(n):
        line = input(f"Enter {set_type} for NT: ").strip()
        nt, symbols = line.split(':')
        user_set[nt.strip()] = set(symbols.strip().split(','))
    return user_set

def build_table(grammar, first, follow):
    table = {}
    # Extract all unique terminals from first/follow/grammar
    terminals = set()
    for s in first.values(): terminals.update(s)
    for s in follow.values(): terminals.update(s)
    terminals.discard('ε')
    if '$' not in terminals: terminals.add('$')
    
    for nt in grammar:
        table[nt] = {t: "" for t in terminals}
        for prod in grammar[nt]:
            first_p = set()
            if prod == 'ε':
                first_p.add('ε')
            else:
                # Logic: FIRST of the first symbol of production
                first_p.update(first.get(prod[0], {prod[0]}))
            
            for a in first_p:
                if a != 'ε' and a in table[nt]:
                    table[nt][a] = prod
            if 'ε' in first_p:
                for b in follow[nt]:
                    if b in table[nt]:
                        table[nt][b] = prod
    return table, sorted(list(terminals))

def parse_string(input_str, table, start_symbol):
    stack = ['$', start_symbol]
    # Handle the input string (adding $ if not present)
    input_list = list(input_str) + ['$']
    idx = 0
    
    print(f"\n{'Stack':<25} {'Input':<20} {'Action'}")
    print("-" * 60)
    
    while len(stack) > 0:
        top = stack.pop()
        current_input = input_list[idx]
        
        if top == current_input:
            if top == '$':
                print(f"{'$':<25} {'$':<20} Accepted!")
                return True
            print(f"{str(stack + [top]):<25} {''.join(input_list[idx:]):<20} Match {top}")
            idx += 1
        elif not top.isupper():
            print(f"Error: Terminal mismatch. Expected {top} but found {current_input}")
            return False
        else:
            prod = table[top].get(current_input, "")
            if prod == "":
                print(f"Error: No rule in M[{top}, {current_input}]")
                return False
            
            print(f"{str(stack + [top]):<25} {''.join(input_list[idx:]):<20} {top} -> {prod}")
            if prod != 'ε':
                # Push production to stack in reverse
                for char in reversed(prod):
                    stack.append(char)
    return False

def main():
    # 1. Get Grammar
    grammar = {}
    num_nt = int(input("Enter number of Non-Terminals in Grammar: "))
    for _ in range(num_nt):
        line = input("Enter rule (e.g., E:TR): ").strip()
        nt, prods = line.split(':')
        grammar[nt.strip()] = prods.strip().split('|')

    # 2. Get FIRST/FOLLOW (User Input based)
    first = get_user_input_sets("FIRST")
    follow = get_user_input_sets("FOLLOW")

    # 3. Build Table
    parsing_table, terminals = build_table(grammar, first, follow)
    
    print("\n--- Predictive Parsing Table ---")
    df = pd.DataFrame(parsing_table).T
    print(df)

    # 4. Parse String
    start_node = input("\nEnter Start Symbol: ").strip()
    test_input = input("Enter string to parse (e.g., i+i): ").strip()
    parse_string(test_input, parsing_table, start_node)

if __name__ == "__main__":
    main()
