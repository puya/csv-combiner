# CSV Combiner

A simple interactive tool to combine multiple CSV files into a single file, adding a source filename column to track the origin of each row.

## Features

- Interactive command-line interface
- Adds source filename as the first column in the combined CSV
- Handles files with irregular headers or metadata
- Allows skipping rows at the beginning of files
- **Column selection**: Choose which columns to include in the output
  - Support for ranges (e.g., "1-5")
  - Custom column ordering (e.g., "3,1-2" to reorder columns)
- Creates output in a dedicated CSV-Files folder

## Requirements

- Python 3.6+
- pandas

## Installation

This project uses Poetry for dependency management.

1. Clone the repository:
   ```
   git clone https://github.com/puya/csv-combiner.git
   cd csv-combiner
   ```

2. Install dependencies with Poetry:
   ```
   poetry install
   ```

## Usage

1. Run the script:
   ```
   poetry run csv-combiner
   ```

2. Follow the interactive prompts:
   - Select a subfolder containing CSV files
   - View a preview of the first file
   - Specify which line contains the headers
   - Select which columns to include in the output (and their order)
   - The script will combine all CSV files and save the result

## Project Structure

- `src/csv_combiner/`: Main package
  - `main.py`: Entry point
  - `file_utils.py`: File operations
  - `ui.py`: User interface
  - `csv_processor.py`: CSV processing
- `CSV-Files/`: Directory for input and output files (created automatically)
  - Each subfolder should contain CSV files to be combined
  - Combined files will be saved in this directory

## License

MIT 