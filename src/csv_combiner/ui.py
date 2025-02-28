"""User interface functions for the CSV combiner."""

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