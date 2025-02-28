import os
import pandas as pd
import glob
import sys
from pathlib import Path
import csv

def create_csv_files_folder():
    """Create the CSV-Files folder if it doesn't exist."""
    csv_folder = Path("CSV-Files")
    if not csv_folder.exists():
        csv_folder.mkdir()
        print(f"Created folder: {csv_folder}")
    return csv_folder

def get_subfolder_choice(base_folder):
    """List subfolders and let user choose one."""
    # Get all subfolders
    subfolders = [f for f in base_folder.iterdir() if f.is_dir()]
    
    if not subfolders:
        print(f"No subfolders found in {base_folder}. Please create at least one subfolder with CSV files.")
        return None
    
    # Display options
    print("\nAvailable folders:")
    for i, folder in enumerate(subfolders, 1):
        print(f"{i}. {folder.name}")
    
    # Get user choice
    while True:
        try:
            choice = int(input("\nEnter folder number: "))
            if 1 <= choice <= len(subfolders):
                return subfolders[choice-1]
            else:
                print(f"Please enter a number between 1 and {len(subfolders)}")
        except ValueError:
            print("Please enter a valid number")

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
    """Show raw preview of file contents."""
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

def get_header_line(preview_lines):
    """Ask user which line contains the headers."""
    while True:
        try:
            header_line = input("\nWhich line contains the headers? (0 for no headers): ")
            if header_line == "":
                return 0
            header_line = int(header_line)
            if 0 <= header_line <= len(preview_lines):
                return header_line
            else:
                print(f"Please enter a number between 0 and {len(preview_lines)}")
        except ValueError:
            print("Please enter a valid number")

def combine_csv_files(folder_path, output_file):
    """
    Combine all CSV files in the specified directory, adding a source filename column.
    
    Args:
        folder_path: Path to directory containing CSV files
        output_file: Path to output file
    """
    # Get all CSV files in the directory
    all_files = list(folder_path.glob("*.csv"))
    
    if not all_files:
        print(f"No CSV files found in {folder_path}")
        return False
    
    # Show raw preview of the first file
    preview_lines = preview_file(all_files[0])
    if not preview_lines:
        return False
    
    # Ask which line contains the headers
    header_line = get_header_line(preview_lines)
    
    # Calculate rows to skip based on header line
    skip_rows = header_line - 1 if header_line > 0 else 0
    has_headers = header_line > 0
    
    # List to store dataframes
    dfs = []
    
    # Read each CSV file and add filename column
    for file in all_files:
        try:
            # Read the file with flexible parsing options
            if has_headers:
                df = pd.read_csv(file, 
                                skiprows=skip_rows,
                                engine='python',
                                on_bad_lines='skip')
            else:
                df = pd.read_csv(file, 
                                skiprows=skip_rows,
                                header=None,
                                engine='python',
                                on_bad_lines='skip')
            
            # Extract just the filename without path and extension
            filename = file.stem  # This gets the filename without the .csv extension
            
            # Add filename column as the first column
            df.insert(0, 'Source_File', filename)
            
            # Append to list
            dfs.append(df)
            print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {file}: {e}")
            print("Skipping this file and continuing with others.")
    
    if not dfs:
        print("No files were successfully processed.")
        return False
    
    # Combine all dataframes
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Save to a new CSV file
    combined_df.to_csv(output_file, index=False)
    
    print(f"\nCombined {len(dfs)} files into {output_file}")
    return True

def main():
    print("CSV File Combiner")
    print("=================")
    
    # Create or verify CSV-Files folder
    csv_folder = create_csv_files_folder()
    
    # Let user choose a subfolder
    chosen_folder = get_subfolder_choice(csv_folder)
    if not chosen_folder:
        return
    
    # Generate output filename
    output_file = get_output_filename(chosen_folder.name)
    
    # Combine the CSV files
    success = combine_csv_files(chosen_folder, output_file)
    
    if success:
        print("\nOperation completed successfully!")
    else:
        print("\nOperation failed. Please check the errors above.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")