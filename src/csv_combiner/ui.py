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

def select_columns(df):
    """
    Allow user to select which columns to include in the output.
    
    Args:
        df: DataFrame with all columns
        
    Returns:
        list: Selected column names or None to keep all columns
    """
    print("\nColumn Selection")
    print("----------------")
    print("You can select which columns to include in the output.")
    print("Available columns:")
    
    # Always include the Source_File column
    columns = df.columns.tolist()
    
    # Display columns with numbers
    for i, col in enumerate(columns, 1):
        print(f"{i}. {col}")
    
    print("\nOptions:")
    print("- Enter column numbers separated by commas (e.g., '1,3,5')")
    print("- Use ranges with a dash (e.g., '1-3,5,7-9')")
    print("- Order matters: columns will appear in the order you specify")
    print("- Enter 'all' to include all columns in original order (default)")
    print("- Enter 'none' to select no columns (will still include Source_File)")
    
    while True:
        selection = input("\nEnter your selection: ").strip().lower()
        
        if not selection or selection == 'all':
            print("Including all columns in original order.")
            return None  # None means keep all columns
            
        if selection == 'none':
            print("Including only the Source_File column.")
            return ['Source_File']
            
        try:
            selected_indices = []
            
            # Split by commas
            parts = selection.split(',')
            for part in parts:
                part = part.strip()
                
                # Check if it's a range (contains '-')
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    if 1 <= start <= end <= len(columns):
                        selected_indices.extend(range(start, end + 1))
                    else:
                        print(f"Invalid range: {part}. Must be between 1 and {len(columns)}")
                        raise ValueError("Invalid range")
                else:
                    # Single number
                    idx = int(part)
                    if 1 <= idx <= len(columns):
                        selected_indices.append(idx)
                    else:
                        print(f"Invalid column number: {idx}. Must be between 1 and {len(columns)}")
                        raise ValueError("Invalid column number")
            
            # Note: We're NOT sorting or removing duplicates anymore
            # This preserves the user's specified order and allows duplicating columns
            
            if selected_indices:
                selected_columns = [columns[idx-1] for idx in selected_indices]
                
                # Ensure Source_File is included (at the beginning if not already selected)
                if 'Source_File' not in selected_columns:
                    selected_columns.insert(0, 'Source_File')
                    
                print(f"Selected columns in order: {', '.join(selected_columns)}")
                return selected_columns
            else:
                print("No valid columns selected.")
        except ValueError as e:
            if str(e) not in ["Invalid range", "Invalid column number"]:
                print("Please enter valid column numbers or ranges separated by commas.") 