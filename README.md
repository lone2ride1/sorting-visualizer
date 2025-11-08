# Neon Sorting Visualizer

An interactive web application for visualizing five fundamental sorting
algorithms—Selection Sort, Insertion Sort, Bubble Sort, Merge Sort, and Quick
Sort—with animated, neon-themed UI, real-time complexity insights, and
customizable data.

---

## Features

- **Algorithm Visualization:**  
  Real-time, animated visualizations for Selection Sort, Insertion Sort, Bubble
  Sort, Merge Sort, and Quick Sort using vertical neon bars.

- **Complexity Insights:**  
  Displays time and space complexity (Average, Best, Worst) for the selected
  algorithm instantly in the UI sidebar.

- **Customizable Data:**  
  Select array sizes (30, 50, 80 elements) and reshuffle arrays at any time with
  a "Shuffle" button for repeated experimentation.

- **Neon High-Contrast UI:**
  - Black background for maximum contrast
  - Neon colors for bars (lime, cyan, magenta, yellow)
  - Bright white accents for active elements
  - Animated swaps and comparisons (glowing transitions)
  - Large, clear fonts for readability

---

## Algorithms

| Algorithm      | Visual Cues                                       | Animation Events                | Time: Best      | Time: Avg       | Time: Worst     | Space         |
| -------------- | ------------------------------------------------- | ------------------------------- | --------------- | --------------- | --------------- | ------------- |
| Selection Sort | Highlights current position/min-index, swaps bars | Bar swap, highlight             | \(O(n^2)\)      | \(O(n^2)\)      | \(O(n^2)\)      | \(O(1)\)      |
| Insertion Sort | Highlights sorted/unsorted parts                  | Shift bars, insertion highlight | \(O(n)\)        | \(O(n^2)\)      | \(O(n^2)\)      | \(O(1)\)      |
| Bubble Sort    | Active pairwise comparison, swaps                 | Compare/swap animation          | \(O(n)\)        | \(O(n^2)\)      | \(O(n^2)\)      | \(O(1)\)      |
| Merge Sort     | Recursive splits, group merges visualized         | Group merges, split highlights  | \(O(n \log n)\) | \(O(n \log n)\) | \(O(n \log n)\) | \(O(n)\)      |
| Quick Sort     | Pivot selection, partition, recursive color cue   | Pivot/swap, partition highlight | \(O(n \log n)\) | \(O(n \log n)\) | \(O(n^2)\)      | \(O(\log n)\) |

---

## UI & User Flow

### Controls

- **Algorithm Picker:** Select from five sorts.
- **Array Size Selector:** Choose 30, 50, or 80 elements.
- **Shuffle Button:** Randomize the array instantly.
- **Start/Pause/Resume/Reset:** Control the animation lifecycle.

### Complexity Sidebar

Displays live stats for the currently selected algorithm:

- Time Complexity (Best, Average, Worst)
- Space Complexity

---

## Neon Theme Design

- **Background:** Deep black (\#1a1a1a)
- **Bar Colors:** Neon lime (\#39ff14), cyan (\#00f6ff), magenta (\#ff2ff0),
  yellow (\#fffe36)
- **Active Element Border:** Bright white (\#ffffff)
- **Animated Effects:** Bars glow/pulse during swaps and comparisons,
  transitions are smooth and high-contrast.
- **Accessibility:** Large fonts, clear labels, strong contrast for maximum
  visibility.

---

## Customization

- Generate randomly filled arrays of the selected size.
- Shuffle to reset without changing array length.
- All features update the UI instantly.
- Pause/resume/reset for repeatable, detailed demonstrations.

---

## Getting Started

1. **Install requirements:**  
   `pip install flask` (or front-end build with React)
2. **Run the app:**  
   `python app.py` or `npm start` (React)
3. **Open in browser:**  
   Visit [localhost:5000](http://localhost:5000)

---

This all-in-one README provides a complete overview and implementation plan for
your visual sorting project, blending algorithmic clarity, vibrant UI, and
strong usability.[web:1]
