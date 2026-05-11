# AI Practical Exam Viva Guide

This guide is prepared from the codes in this folder for final practical exam preparation.
It covers:
- What each practical does
- Key theory behind it
- Likely viva questions and strong answers
- Common debugging/improvement points examiners ask

---

## Practical 1: `Assignment-A1.py` (DFS and BFS on Graph)

### What this practical is
This program builds an **undirected graph** using adjacency lists and performs:
- **DFS (Depth First Search)** using recursion
- **BFS (Breadth First Search)** using queue (`collections.deque`)

You enter edges and a start node, and it prints traversal order.

### Core concepts
- Graph representation: dictionary of lists
- Traversal strategies:
  - DFS: go deep first, then backtrack
  - BFS: visit level by level
- Visited set prevents infinite loops in cyclic graphs

### Likely viva Q&A
1. **Q: Difference between DFS and BFS?**  
   **A:** DFS uses stack/recursion and explores one branch deeply before backtracking. BFS uses queue and explores nodes level by level. BFS gives shortest path in unweighted graph; DFS does not guarantee shortest.

2. **Q: Why use a visited set?**  
   **A:** To avoid revisiting nodes and infinite loops in cyclic graphs.

3. **Q: Time complexity of DFS and BFS?**  
   **A:** Both are `O(V + E)` where `V` is vertices and `E` is edges.

4. **Q: Why is `deque` used in BFS?**  
   **A:** `deque.popleft()` is efficient `O(1)`, unlike list pop from front.

5. **Q: Is this graph directed or undirected?**  
   **A:** Undirected, because each edge is added in both directions (`u->v` and `v->u`).

### Important correction examiner may ask
- `dfs(node, visited=set())` uses mutable default argument. Better style:
  - use `visited=None`, then create set inside function.

---

## Practical 2: `Assignment-A2.py` (A* for 8-Puzzle)

### What this practical is
This solves the **8-puzzle** using **A\*** search.
- Goal state is fixed as:
  - `[[1,2,3],[4,5,6],[7,8,0]]`
- Heuristic `h(n)` = number of misplaced tiles (excluding blank `0`)
- `f(n) = g(n) + h(n)` where:
  - `g(n)` = cost from start to current state
  - `h(n)` = estimated cost to goal

### Core concepts
- Informed search (heuristic-based)
- Priority queue (`heapq`) selects node with minimum `f`
- State conversion to tuple for hashing in visited set
- Neighbor generation by moving blank tile in 4 directions

### Likely viva Q&A
1. **Q: Why A\* instead of BFS for 8-puzzle?**  
   **A:** BFS is uninformed and explores many states. A\* uses heuristic to reach goal faster.

2. **Q: What is heuristic in this code?**  
   **A:** Misplaced tiles count.

3. **Q: Is misplaced tile heuristic admissible?**  
   **A:** Yes, it never overestimates true remaining moves.

4. **Q: What data structure is used for open list?**  
   **A:** Min-heap priority queue from `heapq`.

5. **Q: Why convert list state to tuple?**  
   **A:** Lists are mutable and unhashable; tuples are hashable for set membership.

6. **Q: If no solution exists, what happens?**  
   **A:** Function returns `None`, and program prints "No solution found."

### Improvement points
- Add solvability check using inversion count before running A\*.
- Better heuristic: Manhattan distance gives stronger guidance than misplaced tiles.

---

## Practical 3: `Assignment-A3.py` (Selection Sort and Prim's MST)

### What this practical is
Menu-driven program implementing:
1. **Selection Sort** on user-entered numbers
2. **Prim's algorithm** to find Minimum Spanning Tree (MST) from adjacency matrix

### Core concepts
- Selection sort repeatedly picks minimum from unsorted part
- Prim grows MST by adding minimum weight edge from visited to unvisited node
- Weighted connected undirected graph for MST

### Likely viva Q&A
1. **Q: How selection sort works?**  
   **A:** For each index `i`, find minimum element from `i...end` and swap with `arr[i]`.

2. **Q: Time complexity of selection sort?**  
   **A:** `O(n^2)` in best, average, and worst case.

3. **Q: What is MST?**  
   **A:** A spanning tree connecting all vertices with minimum total edge weight and no cycles.

4. **Q: Prim vs Kruskal?**  
   **A:** Prim grows from a start vertex using local minimum connecting edge. Kruskal sorts all edges globally and adds edges avoiding cycles.

5. **Q: Complexity of Prim in this code?**  
   **A:** About `O(V^2)` due to adjacency matrix scanning.

6. **Q: Why 0 means no edge here?**  
   **A:** In this representation, non-diagonal zero indicates absence of edge.

### Improvement points
- Handle disconnected graph case explicitly.
- Replace `minimum = 999` with `float("inf")`.

---

## Practical 4: `Assignment-B4.py` (N-Queen using Backtracking)

### What this practical is
Solves N-Queen problem using recursion and backtracking.
- Places one queen per row
- Tracks unsafe columns and diagonals
- Prints one valid board configuration using `Q` and `.`

### Core concepts
- Constraint Satisfaction Problem (CSP)
- Backtracking:
  - choose position
  - recurse
  - undo choice if dead end
- Diagonal indexing:
  - right diagonal index = `i + j`
  - left diagonal index = `i - j + n - 1`

### Likely viva Q&A
1. **Q: Why backtracking is used in N-Queen?**  
   **A:** It systematically explores valid placements and backtracks when constraints fail.

2. **Q: What constraints are checked?**  
   **A:** Same column, same left diagonal, same right diagonal.

3. **Q: Why arrays of size `2*n` for diagonals?**  
   **A:** Total possible diagonal indices are up to `2n-1`; size `2*n` safely covers indexing.

4. **Q: Does this code print all solutions?**  
   **A:** No, it returns after first valid solution (`return True`).

5. **Q: Worst-case time complexity?**  
   **A:** Exponential, roughly `O(n!)` for brute-force style backtracking.

### Improvement points
- Modify to collect and print all solutions.
- Validate `n` input (`n >= 1`).

---

## Practical 5: `Assignment-B5.py` (Rule-based Chatbot using NLTK)

### What this practical is
A simple customer-support chatbot using:
- `nltk.chat.util.Chat`
- Pattern-response pairs (regex + fixed replies)
- Interactive conversation loop (`chatbot.converse()`)

### Core concepts
- Pattern matching with regular expressions
- Rule-based NLP (not ML-based learning)
- Reflections support pronoun conversion (from NLTK utility)

### Likely viva Q&A
1. **Q: Is this chatbot AI or hardcoded?**  
   **A:** It is rule-based AI using predefined regex patterns and responses; it does not learn from data.

2. **Q: Why `nltk.download('punkt')`?**  
   **A:** It downloads tokenizer resources; in this code, chat mainly uses regex rules, but NLTK setup often includes this dependency.

3. **Q: What is the role of `pairs` list?**  
   **A:** It maps user input patterns to possible bot responses.

4. **Q: What happens if input does not match any pattern?**  
   **A:** Chat may give default/empty behavior depending on `Chat` handling; typically no meaningful custom response unless fallback rule is added.

5. **Q: How can we improve it?**  
   **A:** Add more patterns, fallback intent, context memory, or switch to ML/NLU approach.

### Improvement points
- Add catch-all fallback pattern for unmatched queries.
- Make regex case-insensitive robustly.

---

## Practical 6: `Assignment-C6.py` (Medical Expert System)

### What this practical is
A small **expert system** for diagnosis based on symptoms.
- Knowledge base maps diseases to symptom list
- Program asks yes/no symptom questions
- Computes score = number of matched symptoms for each disease
- Displays disease(s) with highest score

### Core concepts
- Knowledge base + inference
- Rule-based decision support
- Score-based matching (not probabilistic model)
- Input validation loop (`yes/no`)

### Likely viva Q&A
1. **Q: Why is this called expert system?**  
   **A:** Because it uses domain knowledge encoded as rules/symptom mappings to infer possible diagnosis.

2. **Q: What inference approach is used?**  
   **A:** Simple score-based matching over rule base (not full forward-chaining engine, but conceptually rule-based inference).

3. **Q: Can multiple diseases be output?**  
   **A:** Yes, if two or more diseases have the same maximum score.

4. **Q: Is this medically accurate for real diagnosis?**  
   **A:** No, it is educational and simplified; real systems need large validated datasets and clinical supervision.

5. **Q: How is invalid input handled?**  
   **A:** `ask()` loops until user enters `yes` or `no`.

### Improvement points
- Add weighted symptoms instead of equal weights.
- Add certainty percentage and tie-breaking logic.

---

## Cross-Practical Theory Questions (Very Common in Viva)

1. **What is the difference between uninformed and informed search?**  
Uninformed search uses only problem definition (e.g., DFS/BFS), informed uses heuristic knowledge (e.g., A\*).

2. **What is heuristic function?**  
A function that estimates cost from current state to goal to guide search efficiently.

3. **What is backtracking?**  
A recursive trial-and-error method that abandons partial solutions when they violate constraints.

4. **What is a greedy choice in Prim's algorithm?**  
At each step, choose minimum weight edge connecting visited and unvisited set.

5. **Difference between rule-based system and machine learning model?**  
Rule-based uses manually written logic; ML learns patterns from data.

6. **What is time complexity and space complexity? Why important?**  
They measure algorithm efficiency in resource usage and scalability.

---

## Quick Last-Minute Viva Answers (1-liners)

- **DFS uses stack/recursion, BFS uses queue.**
- **BFS finds shortest path in unweighted graph.**
- **A\* uses `f(n)=g(n)+h(n)` to choose best node.**
- **N-Queen is a classic backtracking CSP.**
- **Prim's algorithm finds MST in weighted connected graph.**
- **Chatbot code is rule-based NLP, not deep learning.**
- **Medical expert system uses symptom-rule matching.**


Prepare one dry run per practical and one improvement suggestion per practical; this creates a strong viva impression.

