"""CSV processing functions."""

import pandas as pd
from pathlib import Path

def combine_csv_files(folder_path, output_file, preview_lines, header_line):
    """
    Combine all CSV files in the specified directory, adding a source filename column.
    
    Args:
        folder_path: Path to directory containing CSV files
        output_file: Path to output file
        preview_lines: Lines from the preview of the first file
        header_line: Which line contains the headers (0 for no headers)
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Get all CSV files in the directory
    all_files = list(folder_path.glob("*.csv"))
    
    if not all_files:
        print(f"No CSV files found in {folder_path}")
        return False
    
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