import os


def write_to_csv(input_path, df, file_name):
    """
    Write DataFrame to a CSV file.

    Parameters:
        input_path (str): Path where the CSV file will be saved.
        df (pandas.DataFrame): DataFrame to be saved as CSV.
        file_name (str): Name of the CSV file (without extension).

    Raises:
        ValueError: If input_path does not exist or is not a directory.
        IOError: If there is an issue writing the CSV file.

    Returns:
        None
    """
    # Validate input path
    if not os.path.exists(input_path) or not os.path.isdir(input_path):
        raise ValueError("Invalid input_path. It should be an existing directory.")

    # Construct the full file path
    csv_file_path = os.path.join(input_path, f"{file_name}.csv")

    # Write DataFrame to CSV file
    try:
        df.to_csv(csv_file_path, header=True, index=False)
        print(f"DataFrame successfully saved to: {csv_file_path}")
    except IOError as e:
        print(f"Error writing DataFrame to CSV file: {e}")
        raise
