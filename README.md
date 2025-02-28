# CSV Combiner

A simple interactive tool to combine multiple CSV files into a single file, adding a source filename column to track the origin of each row.

## Features

- Interactive command-line interface
- Adds source filename as the first column in the combined CSV
- Handles files with irregular headers or metadata
- Allows skipping rows at the beginning of files
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
   - The script will combine all CSV files and save the result

## Project Structure

- `combine_csv.py`: Main script
- `CSV-Files/`: Directory for input and output files (created automatically)
  - Each subfolder should contain CSV files to be combined
  - Combined files will be saved in this directory

## License

MIT 