# Minimization-Algorithm
# DFA Minimization Assignment

**Student Names:** Jerónimo Restrepo Ángel and Juan Esteban Restrepo Orozco  
**Class Number:** SI2002_7308  
**Operating System:** Linux (Ubuntu) 6.11.0-17-generic #17~24.04.2-Ubuntu  
**Programming Language:** Python 3.8 (or higher)  
**Tools Used:** Git, Visual Studio Code

# Documentation of the DFA Minimization Algorithm Implementation

## Introduction
This document details the implementation of a Python algorithm for minimizing Deterministic Finite Automata (DFA) using the **table filling method**. The algorithm identifies pairs of equivalent states in a DFA and returns a lexicographically sorted list of these pairs.

## Code Description

### 1. **Function `minimize_dfa`**
This function is responsible for minimizing the DFA by following these steps:

#### **Input Parameters:**
- `n`: number of states.
- `alphabet`: list of alphabet symbols.
- `finals`: list of final states.
- `transitions`: transition matrix, where `transitions[i][sym_index]` represents the destination state from state `i` using the symbol at position `sym_index` in the alphabet.

#### **Step 1: Initialization of the Marking Table**
A matrix `mark` of dimensions `n x n` is created, where `mark[i][j]` indicates whether states `i` and `j` are distinguishable:
- If one of the states is final and the other is not, the pair is marked as distinguishable (`True`).

#### **Step 2: Propagation of Distinguishable States**
The matrix `mark` is iterated until no further changes occur:
- For each pair of states `(i, j)`, if they have not yet been marked as distinguishable, their transitions are examined.
- If, for any alphabet symbol, the destination states are already distinguishable, the pair `(i, j)` is marked as distinguishable.

#### **Step 3: Identification of Equivalent States**
- Pairs that are not marked in `mark` are considered equivalent.
- The list of equivalent pairs is returned, sorted lexicographically.

---

### **Indistinguishable vs. Distinguishable States**

Two states are **indistinguishable** if:
- Both are final states or both are non-final.
- For any alphabet symbol, their transitions lead to states that are also indistinguishable.

If `p` and `q` are indistinguishable, they can be merged into a single state without changing the behavior of the automaton.

Conversely, two states `p` and `q` are **distinguishable** if:
- One is a final state and the other is not.
- For some input symbol, their transitions lead to states that have already been marked as distinguishable.

If `p` and `q` are distinguishable, it means there is at least one input string that produces a behavioral difference, preventing them from being merged in the minimized DFA.

---
### 2. **Function `main`**
The `main` function handles input and output, allowing the DFA specification to be read either from a file or from the console. It has been updated to include additional error handling for invalid destination states in the transition matrix.

#### **Input Format Selection**
- The user is prompted to choose the input format:
  - Option `1`: Read the DFA from the file `dfa_input.txt`.
  - Option `2`: Enter the DFA data manually via the console.

#### **File Input**
- The file `dfa_input.txt` is opened and read.
- Blank lines are removed, and the data is processed as follows:
  1. The number of test cases is read.
  2. For each test case:
     - **Number of states:** The number `n` is read.
     - **Alphabet:** A list of symbols is extracted.
     - **Final states:** A list of final states is read and converted to integers.
     - **Transition Matrix:** For each of the `n` states, a transition row is read.
       - **Error Handling for Transitions:** For each element in the transition row, the program checks if the destination state is valid (i.e., it must be less than `n`). If an invalid destination state is detected, an error message is displayed:
         > "Error: el estado destino no es válido. Inténtelo de nuevo."
         
         The input is then requested again until a valid row is provided.
- Once the input is processed, the `minimize_dfa` function is called with the extracted data.
- After minimization:
  - If no equivalent state pairs are found, a message is printed indicating that there are no equivalent states in the automaton.
  - Otherwise, the equivalent state pairs are printed in lexicographic order.

#### **Console Input**
If the user opts for manual entry:
- The number of test cases is requested.
- For each test case:
  - **Number of states:** The number `n` is entered.
  - **Alphabet:** The alphabet is entered as a space-separated list.
  - **Final states:** Final states are entered and converted to integers.
  - **Transition Matrix:** For each state, the program prompts for the transition row with a message like:
    > "Transición _i_ (Empiece con _i_):"
    - **Error Handling for Transition Rows:**
      - The program first checks if the entered row has the correct number of elements (which should be `len(alphabet) + 1`). If not, it displays an error message:
        > "Error: la fila de transición excede el número de posibles transiciones de acuerdo al alfabeto. Inténtelo de nuevo."
      - Then, for each element in the row, it checks whether the destination state is valid (i.e., less than `n`). If an invalid destination state is found, an error message is shown:
        > "Error: el estado destino no es válido. Inténtelo de nuevo."
        
        The input is requested repeatedly until a valid row is provided.
- After gathering all data, the `minimize_dfa` function is invoked.
- Similar to file input, if there are no equivalent state pairs, a message is printed. Otherwise, the equivalent pairs are formatted and printed in lexicographic order.

---
## Steps to Execute the Algorithm

1. **Ensure that Python 3 is installed.**
2. **Prepare the necessary files:**
   - `main.py` (source code of the algorithm).
   - `dfa_input.txt` (input file with the DFA specification, if the file option is chosen).
3. **Open a terminal in the directory where the code is located.**
4. **Run the script with the following command:**
   ```sh
   python main.py
   
#### **Choosing the Input Format**
5. **Choose the input format:**
   - Option `1`: Read the DFA from `dfa_input.txt`.
   - Option `2`: Enter the data manually via the console.
6. **Observe the output in the terminal,** which will display the equivalent state pairs in lexicographic order.

---

## Example Input and Output
### **Input (file or console):**
1 <br>
4 <br>
a <br>
2 3 <br>
0 2 <br>
1 3 <br>
2 1 <br>
3 0 <br>

### **Expected Output:**
(0,1) (2,3)

---

## Algorithm Complexity
The time complexity of the `minimize_dfa` function is **O(n² · |Σ|)**, where:
- `n` is the number of states.
- `|Σ|` is the size of the alphabet.

This is because:
- The initialization of the marking table takes **O(n²)**.
- The iterative process examines every state pair and each transition, resulting in **O(n² · |Σ|)** in the worst case.

---

## Conclusions
The implemented algorithm efficiently minimizes DFAs using the table filling method. It ensures that equivalent states are correctly identified, optimizing the automaton's representation without sacrificing its functionality.
