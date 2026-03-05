#!/usr/bin/env python3
"""
Master Script: Runs all compiler design experiments in sequence
Execute all experiments with sample inputs automatically
"""

import os
import subprocess
import sys

def run_command(cmd, description):
    """Execute a command and print status"""
    print(f"\n{'='*70}")
    print(f"▶ {description}")
    print(f"{'='*70}")
    try:
        result = subprocess.run(cmd, shell=True, cwd=os.getcwd())
        if result.returncode == 0:
            print(f"✓ {description} completed successfully")
        else:
            print(f"✗ {description} failed with code {result.returncode}")
    except Exception as e:
        print(f"✗ Error running {description}: {e}")

def main():
    workspace = os.getcwd()
    
    print("\n" + "="*70)
    print("  COMPILER DESIGN - ALL EXPERIMENTS RUNNER")
    print("="*70)
    
    # Phase 1: Lexical Analysis
    print("\n\n【 PHASE 1: LEXICAL ANALYSIS 】")
    
    # Compile and run lexer
    print("\n--- Compiling Lexer ---")
    run_command(f'gcc "{workspace}\\lexer.c" -o "{workspace}\\lexer.exe"', 
                "Lexer Compilation")
    
    print("\n--- Running Lexer ---")
    # Sample input for lexer
    sample_code = """int main() {
    int x = 5;
    x = x + 10;
    return 0;
}
0"""
    
    lexer_input = sample_code.replace('\n', '\n')
    run_command(f'echo. | ({workspace}\\lexer.exe)', 
                "Lexical Analyzer")
    
    
    # Phase 2: Finite Automata
    print("\n\n【 PHASE 2: FINITE AUTOMATA 】")
    
    print("\n--- Regular Expression to NFA ---")
    run_command(f'python "{workspace}\\REtoNFA.py"', 
                "RE to NFA Conversion")
    
    print("\n--- NFA to DFA Conversion ---")
    run_command(f'python "{workspace}\\NFAtoDFA.py"', 
                "NFA to DFA Conversion")
    
    
    # Phase 3: Grammar Analysis
    print("\n\n【 PHASE 3: GRAMMAR ANALYSIS 】")
    
    print("\n--- Grammar Transformation (Left Recursion & Left Factoring) ---")
    run_command(f'python "{workspace}\\elimination of left recursion and left factoring.py"', 
                "Grammar Transformations")
    
    print("\n--- FIRST and FOLLOW Set Computation ---")
    run_command(f'python "{workspace}\\first and follow computation.py"', 
                "FIRST and FOLLOW Computation")
    
    
    # Phase 4: Syntax Analysis
    print("\n\n【 PHASE 4: SYNTAX ANALYSIS 】")
    
    print("\n--- Predictive Parser ---")
    run_command(f'python "{workspace}\\predictive_parser.py"', 
                "LL(1) Predictive Parser")
    
    
    print("\n" + "="*70)
    print("  ALL EXPERIMENTS COMPLETED!")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
