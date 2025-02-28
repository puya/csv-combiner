"""File and folder utility functions."""

from pathlib import Path

def create_csv_files_folder():
    """Create the CSV-Files folder if it doesn't exist."""
    csv_folder = Path("CSV-Files")
    if not csv_folder.exists():
        csv_folder.mkdir()
        print(f"Created folder: {csv_folder}")
    return csv_folder

def get_csv_files(folder_path):
    """Get all CSV files in the specified directory."""
    return list(folder_path.glob("*.csv"))

def get_output_filename(folder_name):
    """Generate a unique output filename based on the folder name."""
    base_name = f"{folder_name}-combined.csv"
    output_file = Path("CSV-Files") / base_name
    
    # If file exists, add a number
    counter = 1
    while output_file.exists():
        output_file = Path("CSV-Files") / f"{folder_name}-combined-{counter}.csv"
        counter += 1
    
    return output_file

def preview_file(file_path, num_rows=10):
    """Show raw preview of file contents and return the lines."""
    print(f"\nRaw preview of first {num_rows} lines from {file_path.name}:")
    lines = []
    try:
        with open(file_path, 'r', errors='replace') as f:
            for i, line in enumerate(f):
                if i >= num_rows:
                    break
                print(f"Line {i+1}: {line.strip()}")
                lines.append(line.strip())
        return lines
    except Exception as e:
        print(f"Error reading file: {e}")
        return [] 