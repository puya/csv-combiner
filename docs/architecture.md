# CSV Combiner Architecture

This document outlines the architecture and design principles of the CSV Combiner application.

## Project Structure 

csv-combiner/
├── pyproject.toml # Project metadata and dependencies
├── poetry.lock # Locked dependencies
├── README.md # User documentation
├── .gitignore # Git ignore file
├── docs/ # Documentation
│ └── architecture.md # This file
├── src/ # Source code
│ └── csv_combiner/ # Main package
│ ├── init.py # Package initialization
│ ├── main.py # Entry point and orchestration
│ ├── file_utils.py # File and folder operations
│ ├── ui.py # User interaction functions
│ └── csv_processor.py # CSV reading and processing logic
└── tests/ # Test directory
└── init.py # Makes the directory a package


## Module Responsibilities

### main.py
- Entry point for the application
- Orchestrates the overall flow
- Handles top-level error management
- Connects the different modules together

### file_utils.py
- Manages file and folder operations
- Creates necessary directories
- Handles file previews
- Generates output filenames

### ui.py
- Manages user interactions
- Displays options and menus
- Collects and validates user input
- Handles column selection interface

### csv_processor.py
- Handles CSV file reading and processing
- Combines multiple CSV files
- Adds source tracking
- Manages pandas operations
- Filters columns based on user selection

## Features

1. **Basic CSV Combining**: Combines multiple CSV files with source tracking
2. **Header Detection**: Intelligently handles files with or without headers
3. **Column Selection**: Allows users to select which columns to include in the output
   - Supports individual column selection
   - Supports range selection (e.g., "1-5")
   - Supports custom column ordering (e.g., "3,1-2" to reorder columns)

## Design Principles

1. **Separation of Concerns**: Each module has a specific responsibility
2. **Single Responsibility Principle**: Each function does one thing well
3. **Modularity**: Components can be developed and tested independently
4. **Extensibility**: New features can be added by creating new modules or extending existing ones
5. **Error Handling**: Robust error handling at appropriate levels

## Flow of Execution

1. User runs the application
2. Application checks/creates the CSV-Files folder
3. User selects a subfolder containing CSV files
4. Application previews the first file
5. User specifies which line contains headers
6. User selects which columns to include and their order
7. Application processes and combines all CSV files
8. Combined file is saved with source tracking and selected columns

## Adding New Features

When adding new features:

1. Determine which module should contain the feature
2. If it doesn't fit existing modules, consider creating a new one
3. Update the main.py flow to incorporate the new feature
4. Add appropriate error handling
5. Update documentation

## Testing Strategy

- Unit tests should focus on individual functions
- Integration tests should verify module interactions
- End-to-end tests should validate the complete workflow