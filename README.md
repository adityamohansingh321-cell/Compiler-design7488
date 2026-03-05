
**Name:** Sharish

**Register Number:** RA23110050084

**Year & Section:** 3rd Year CSE - E

## Overview

This repository contains the source code for the Compiler Design laboratory experiments. The project implements the fundamental phases of a compiler, including lexical analysis, finite automata construction, grammar optimization, and syntax analysis using both C and Python.

---

## Repository Structure and Experiments

### 1. Lexical Analysis (`lexer.c`)

A manual lexical analyzer implemented in C that identifies tokens from source code. It classifies input into keywords, identifiers, numbers, operators, and separators.

### 2. Regular Expression to NFA (`REtoNFA.py`)

Implementation of Thompson's Construction algorithm. This script converts postfix regular expressions into NFA transitions, supporting union, concatenation, and Kleene closure operations.

### 3. NFA to DFA Conversion (`NFAtoDFA.py`)

Implementation of the Subset Construction algorithm to convert a non-deterministic finite automaton into a deterministic finite automaton. It utilizes `frozenset` to track unique state sets and generates a formal transition table.

### 4. Grammar Transformations (`elimination of left recursion and left factoring.py`)

Provides automated tools to transform Context-Free Grammars (CFG) for top-down parsing:

* **Left Recursion Elimination:** Removes direct left recursion to prevent infinite loops in predictive parsers.
* **Left Factoring:** Factors out common prefixes to enable deterministic choice during parsing.

### 5. Syntax Analysis Sets (`first and follow computation.py`)

Computes the FIRST and FOLLOW sets for a given grammar. These sets are essential for constructing predictive parsing tables and identifying LL(1) compatibility.

### 6. Predictive Parsing (`predictive_parser.py`)

A complete LL(1) predictive parser that includes:

* **Parsing Table Construction:** Generates the  table based on FIRST and FOLLOW sets.
* **Stack-based Parser:** Simulates the parsing process for input strings, showing the stack trace and matching actions.

---

## Tech Stack

* **C:** Used for the Lexical Analyzer to demonstrate low-level memory and string handling.
* **Python:** Used for advanced algorithms and data structure management in Automata and Syntax phases.

## Execution Instructions

1. **To run the Lexical Analyzer:**
```bash
gcc lexer.c -o lexer
./lexer

```


2. **To run the Python experiments:**
```bash
python "file_name.py"

```
