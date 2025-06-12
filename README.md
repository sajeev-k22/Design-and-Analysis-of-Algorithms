
# 📘 DAA Assignment

This repository contains solutions for a Design and Analysis of Algorithms (DAA) assignment, including multiple sorting algorithms, test case files, and a comprehensive analysis report.

## 📁 Project Structure

```
DAA Assignment/
├── Q1/  # Sorting Algorithms in Python
│   ├── bucket.py  # Bucket Sort implementation
│   ├── heapsort.py  # Heap Sort implementation
│   ├── merge.py  # Merge Sort implementation
│   ├── quick.py  # Quick Sort implementation
│   ├── radix.py  # Radix Sort implementation
│   ├── radix_input.txt  # Input for Radix Sort
│   ├── random_100.txt  # 100 random numbers
│   ├── random_500.txt  # 500 random numbers
│   └── random_1000.txt  # 1000 random numbers
├── Q2/  # Sorting Algorithms in C++ (Normal vs Optimized)
│   ├── Heap_sort/
│   │   ├── heap_normal.cpp  # Normal Heap Sort
│   │   ├── heap_opt.cpp  # Optimized Heap Sort
│   │   └── q2_tc.txt  # Test cases for Heap Sort
│   ├── Merge_sort/
│   │   ├── merge_bottom_up_approach.cpp  # Bottom-up Merge Sort
│   │   ├── merge_recursive_method.cpp  # Recursive Merge Sort
│   │   └── q2_tc.txt  # Test cases for Merge Sort
│   ├── Quick_Sort/
│   │   ├── quick_normal.cpp  # Normal Quick Sort
│   │   ├── quick_opt.cpp  # Optimized Quick Sort
│   │   └── q2_tc.txt  # Test cases for Quick Sort
├── Q3/  # Graph Algorithms in Python
│   ├── Q3_a/  # Articulation Points, Bridges, Strongly Connected Components
│   │   ├── articulation_point.py
│   │   ├── articulation_point_TC.txt
│   │   ├── find_bridges.py
│   │   ├── find_bridges_TC.txt
│   │   ├── strongly_connected_components.py
│   │   └── strongly_connected_components_TC.txt
│   ├── Q3_b/  # Shortest Path Algorithms
│   │   ├── bellmanford.py  # Bellman-Ford algorithm
│   │   ├── dijkstra.py  # Dijkstra's algorithm
│   │   └── Q3_b_TC.txt
│   └── Q3_c/  # Minimum Spanning Tree
│       └── borukas.py  # Boruvka's algorithm (assuming, based on typical MST algorithms)
├── Q4/  # Snakes and Ladders Problem
│   ├── SnakesAndLadders.java  # Java implementation
│   ├── Q4_TC1.txt - Q4_TC14.txt  # Test cases
├── Report.pdf  # Detailed analysis report
```

## 🔧 How to Run

### General Setup
1. **Clone or download the repository.**
   ```bash
   git clone <repository_url> # Replace <repository_url> with the actual URL
   cd DAA-Assignment # Or your repository's root folder name
   ```
2. **Ensure necessary compilers/interpreters are installed:**
   - Python 3.x
   - g++ (for C++ files)
   - JDK (for Java files)

### Q1: Sorting Algorithms (Python)
1. Navigate to the `Q1/` directory:
   ```bash
   cd Q1
   ```
2. Run any of the sorting scripts using Python:
   ```bash
   python quick.py
   python merge.py
   python heapsort.py
   python radix.py
   python bucket.py
   ```
   Each script reads from the provided input files (`radix_input.txt`, `random_100.txt`, etc.) and performs sorting.

### Q2: Sorting Algorithms (C++) - Normal vs Optimized
1. Navigate to the specific algorithm's directory, e.g., `Q2/Heap_sort/`.
   ```bash
   cd Q2/Heap_sort
   ```
2. Compile the C++ files using g++:
   ```bash
   g++ heap_normal.cpp -o heap_normal
   g++ heap_opt.cpp -o heap_opt
   ```
3. Run the compiled executables:
   ```bash
   ./heap_normal < q2_tc.txt # Example, input might be handled differently
   ./heap_opt < q2_tc.txt    # Example, input might be handled differently
   ```
   Repeat for `Merge_sort` and `Quick_Sort` directories.
   *Note: Check individual `.cpp` files or comments within them for specific input/output handling.*

### Q3: Graph Algorithms (Python)
1. Navigate to the specific subdirectory, e.g., `Q3/Q3_a/`.
   ```bash
   cd Q3/Q3_a
   ```
2. Run the Python scripts:
   ```bash
   python articulation_point.py < articulation_point_TC.txt # Example
   python find_bridges.py < find_bridges_TC.txt # Example
   python strongly_connected_components.py < strongly_connected_components_TC.txt # Example
   ```
   Navigate to `Q3/Q3_b/`:
   ```bash
   cd ../Q3_b # Assuming you are in Q3/Q3_a
   python bellmanford.py < Q3_b_TC.txt # Example
   python dijkstra.py < Q3_b_TC.txt # Example
   ```
   Navigate to `Q3/Q3_c/`:
   ```bash
   cd ../Q3_c # Assuming you are in Q3/Q3_b
   python borukas.py # Add specific input file if needed
   ```
   *Note: Input redirection (`< TC_file.txt`) is an example. Verify how each script handles input (e.g., hardcoded filenames, command-line arguments).*

### Q4: Snakes and Ladders (Java)
1. Navigate to the `Q4/` directory:
   ```bash
   cd Q4
   ```
2. Compile the Java file:
   ```bash
   javac SnakesAndLadders.java
   ```
3. Run the compiled Java class:
   ```bash
   java SnakesAndLadders < Q4_TC1.txt # Example, or pass filename as arg if program expects that
   ```
   The program might take a specific test case file as input or read a default one. Check `SnakesAndLadders.java` for details.

Each folder contains test case files.

## 📄 Reports

- **Report.pdf** – Contains detailed analysis, algorithm comparison, and performance results.

## 🛠 VS Code Integration

The `.vscode/` directory includes recommended settings and tasks to simplify code execution in Visual Studio Code.

---

> 💡 Tip: Ensure Python is installed and available in your system's PATH. You can install Python from [python.org](https://www.python.org/).

------------------------------------------------------------------------------------------------
👨‍💻 Author

- Sajeev Kaleeswaran
- Email: sajeevkaleeswaran@gmail.com
- GitHub: github.com/sajeev-k22
