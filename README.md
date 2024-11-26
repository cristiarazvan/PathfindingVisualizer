# Pathfinding Algorithm Visualizer

## Project Overview

This **Pathfinding Algorithm Visualizer**, built using Python and Pygame, demonstrates the implementation of popular pathfinding algorithms like A\*, Depth-First Search (DFS), and Breadth-First Search (BFS) on a grid. The tool provides real-time visualization of the search process and the pathfinding results, allowing users to interact with the grid by setting start and end points, as well as obstacles. This project showcases my proficiency in algorithms, data structures like priority queues, and my ability to create interactive, performance-optimized visual tools.

## Features

-   **Interactive Grid**: Users can click to set start, end, and barrier points on the grid, enabling flexible visual testing of various algorithm scenarios.
-   **Real-time Visualization**: All algorithms are visualized in real-time, with nodes being colored based on their state (start, end, open, closed, path).

## Technologies Used

-   **Language**: Python
-   **Library**: Pygame (for graphical user interface and visualization)

## Installation

To run the Pathfinding Algorithm Visualizer locally, follow these steps:

1. Clone the repository:
    ````bash
    git clone https://github.com/yourusername/PathfindingAlgorithmVisualizer.git
    ````
2. Navigate to the project directory:
    ```bash
    cd PathfindingVisualizer
    ```
3. Make sure you have pygame installed.
    ```bash
    pip install pygame
    ```
4. Run the main script:
    ```bash
    pyhton main.py
    ```

## Usage

1. Interactive Mode: Click on the grid to set the start point, end point, and obstacles. You can reset the grid by pressing the letter C on your keyboard.
2. Algorithm Selection: Press the following keys to run the algorithms:
    - **A: Run the A\* algorithm**
    - **D: Run the Depth-First Search (DFS) algorithm**
    - **B: Run the Breadth-First Search (BFS) algorithm**
