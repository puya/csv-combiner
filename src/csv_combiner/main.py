"""Main entry point for the CSV Combiner application."""

import sys
from pathlib import Path

from .file_utils import create_csv_files_folder, preview_file, get_output_filename
from .ui import get_subfolder_choice, get_header_line
from .csv_processor import combine_csv_files

def main():
    """Main function to run the CSV Combiner."""
    print("CSV File Combiner")
    print("=================")
    
    try:
        # Create or verify CSV-Files folder
        csv_folder = create_csv_files_folder()
        
        # Let user choose a subfolder
        chosen_folder = get_subfolder_choice(csv_folder)
        if not chosen_folder:
            return
        
        # Generate output filename
        output_file = get_output_filename(chosen_folder.name)
        
        # Show preview of the first file
        all_files = list(chosen_folder.glob("*.csv"))
        if not all_files:
            print(f"No CSV files found in {chosen_folder}")
            return
            
        preview_lines = preview_file(all_files[0])
        if not preview_lines:
            return
            
        # Ask which line contains the headers
        header_line = get_header_line(preview_lines)
        
        # Combine the CSV files
        success = combine_csv_files(chosen_folder, output_file, preview_lines, header_line)
        
        if success:
            print("\nOperation completed successfully!")
        else:
            print("\nOperation failed. Please check the errors above.")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return 1
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    sys.exit(main())