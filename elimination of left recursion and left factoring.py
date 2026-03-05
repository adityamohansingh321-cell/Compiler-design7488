import os

def eliminate_left_recursion():
    print("\n--- Elimination of Left Recursion ---")
    nt = input("Enter Non-Terminal (e.g., E): ").strip()
    productions = input("Enter productions separated by '|' (e.g., E+T|T): ").strip().split('|')

    alphas = [p[len(nt):] for p in productions if p.startswith(nt)]
    betas = [p for p in productions if not p.startswith(nt)]

    if not alphas:
        print("No direct left recursion detected.")
        return

    new_nt = nt + "'"
    print(f"\nResulting Grammar:")
    print(f"{nt} -> {' | '.join([b + new_nt for b in betas])}")
    print(f"{new_nt} -> {' | '.join([a + new_nt for a in alphas])} | ε")

def left_factoring():
    print("\n--- Left Factoring ---")
    nt = input("Enter Non-Terminal (e.g., S): ").strip()
    productions = input("Enter productions separated by '|' (e.g., iEtS|iEtSeS|a): ").strip().split('|')

    prefix = os.path.commonprefix(productions)

    if len(prefix) > 0 and len([p for p in productions if p.startswith(prefix)]) > 1:
        new_nt = nt + "'"
        matched = [p[len(prefix):] if p[len(prefix):] != "" else "ε" for p in productions if p.startswith(prefix)]
        unmatched = [p for p in productions if not p.startswith(prefix)]

        print(f"\nResulting Grammar:")
        rule1 = f"{nt} -> {prefix}{new_nt}"
        if unmatched: rule1 += " | " + " | ".join(unmatched)
        print(rule1)
        print(f"{new_nt} -> {' | '.join(matched)}")
    else:
        print("No common prefix found to factor.")

def main():
    while True:
        print("\n===== Experiment 4: Grammar Transformations =====")
        print("1. Eliminate Left Recursion")
        print("2. Left Factoring")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1': eliminate_left_recursion()
        elif choice == '2': left_factoring()
        elif choice == '3': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
