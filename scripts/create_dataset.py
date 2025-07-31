import json
import os
import argparse

def create_training_example(circ_file_path, instruction_text):
    """
    Reads a .circ file and creates a JSONL training example.

    Args:
        circ_file_path (str): The path to the input .circ file.
        instruction_text (str): The instruction prompt for the model.

    Returns:
        str: A JSON string representing a single training example, or None on error.
    """
    try:
        # Read the entire content of the .circ file
        with open(circ_file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()

        # Create the dictionary with the required instruction/response format
        data = {
            "instruction": instruction_text,
            "response": xml_content
        }

        # Convert the dictionary to a JSON string
        return json.dumps(data)

    except FileNotFoundError:
        print(f"Error: File not found at {circ_file_path}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def append_to_dataset(json_string, dataset_file_path):
    """
    Appends a JSON string as a new line to the dataset file.

    Args:
        json_string (str): The JSON string to append.
        dataset_file_path (str): The path to the .jsonl dataset file.
    """
    try:
        # Open the file in append mode and add the new line
        with open(dataset_file_path, 'a', encoding='utf-8') as f:
            f.write(json_string + '\n')
        print(f"Successfully added example to {dataset_file_path}")
    except Exception as e:
        print(f"Error writing to dataset file: {e}")

if __name__ == "__main__":
    # --- Configuration ---
    # Define the relative path to the dataset file from the project root
    DATASET_FILE = os.path.join('data', 'processed', 'dataset.jsonl')

    # --- Command-Line Argument Parsing ---
    parser = argparse.ArgumentParser(
        description="Create a new training example and add it to the dataset."
    )
    parser.add_argument(
        "circ_file",
        help="Path to the .circ file (e.g., data/raw/or_gate.circ)"
    )
    parser.add_argument(
        "instruction",
        help="The instruction text for the model (e.g., 'Create a 2-input OR gate')"
    )
    args = parser.parse_args()

    # --- Main Execution ---
    print("--- Creating new training example ---")
    
    # Create the JSON string from the provided file and instruction
    training_example_json = create_training_example(args.circ_file, args.instruction)

    # If the example was created successfully, append it to the dataset
    if training_example_json:
        append_to_dataset(training_example_json, DATASET_FILE)
    else:
        print("Failed to create training example. Nothing was added to the dataset.")

