# Evolis

Evolis is a simple, real-time evolutionary artificial intelligence simulation ecosystem built with Python and Pygame. The simulation demonstrates how basic natural selection and genetics can lead to emergent behaviors in an artificial environment.

## Table of Contents
- [About The Project](#about-the-project)
- [Core Concepts](#core-concepts)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Simulation Architecture](#simulation-architecture)
- [Future Roadmap](#future-roadmap)

## About The Project

Evolis serves as a fundamental environment to observe ecosystem dynamics. It focuses on the continuous struggle for survival among different entities: Predators and Preys. 

The primary goal of this project is to create an educational and easily extensible framework for studying simulation architectures, basic AI behaviors, and evolutionary algorithms without the complexity of heavy machine learning models.

## Core Concepts

The simulation is built upon these fundamental rules:
- **Food Chain:** Predators hunt and consume Prey.
- **Survival:** Prey must scavenge for food resources to survive.
- **Dynamics:** Both entity types can move freely and reproduce when conditions are met.
- **Natural Selection:** Organisms that fail to secure food (run out of energy) or are hunted will die.
- **Genetics:** Offspring inherit physical and behavioral traits from their parents with slight random mutations.
- **Evolution:** Over generations, the overall population adapts to the environment and its competitors.

**Evolvable Traits:**
- Speed
- Vision Range
- Reproduction Rate
- Stamina
- Energy Efficiency

## Features

**Current MVP Features:**
- Functional Predator, Prey, and Food entities.
- Kinematic movement system.
- Entity collision detection.
- Reproduction cycles and genetic inheritance.
- Lifespan and death mechanics.
- Real-time rendering in a pixel-art aesthetic (similar to WorldBox).

## Technologies

- **Python:** Core programming language.
- **Pygame:** Real-time visual rendering engine.
- **Numpy:** Optimized mathematical and matrix computations.
- **Random:** Procedural generation and genetic mutation logic.
- **Matplotlib:** (Planned) Population statistics and chart generation.
- **JSON:** Storing and loading simulation configurations.

## Installation

1. Ensure you have Python 3.8+ installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/evolis.git
   cd evolis
   ```
3. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the simulation, run the main script from the root directory:

```bash
python evolis/main.py
```

*(Note: The project is currently in the MVP phase. Command line arguments and interactive UI controls will be documented here as they are implemented.)*

## Project Structure

```text
evolis/
├── assets/          # Icons, sprites, and sound files
├── data/            # JSON configuration files and save states
├── docs/            # Documentation and screenshots
├── evolis/          # Main application package
│   ├── engine/      # Core simulation loop, renderer, world state, and genetics
│   ├── entities/    # Organism base classes, Predator, Prey, and Food definitions
│   ├── systems/     # Logic handlers for movement, collision, reproduction, etc.
│   ├── ui/          # Heads-Up Display (HUD), charts, and buttons
│   └── utils/       # Helper functions and math utilities
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Simulation Architecture

### 1. World State
The `World` component manages the global simulation state. It tracks the map boundaries, maintains lists of all active entities (organisms and food), and handles the internal simulation clock (ticks).

### 2. Entities
All physical objects in the simulation are derived from base entities. Living organisms share fundamental properties:
- `position`: Current X, Y coordinates on the map.
- `velocity`: Current speed and direction of movement.
- `energy`: Resource required to move and reproduce.
- `age`: Time lived, affecting physical capabilities.
- `dna`: The genetic code defining the organism's traits.

### 3. Genetics System
DNA acts as a dictionary of traits. During reproduction, the offspring's DNA is constructed using the parent's DNA as a baseline, introducing slight random mutations:
`child.speed = parent.speed + random_mutation()`

## Future Roadmap

While the current focus is on a stable MVP, future updates may include:
- Complex Neural Networks for decision making.
- Advanced Machine Learning behaviors.
- Voxel-based terrain generation.
- Comprehensive AI-powered ecosystem events (weather, seasons).
- Multiplayer or network-based shared simulations.