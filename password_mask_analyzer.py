from collections import Counter

# Function to generate hashcat-style masks from passwords
def get_mask(password):
    mask = []
    for char in password:
        if char.islower():
            mask.append("?l")
        elif char.isupper():
            mask.append("?u")
        elif char.isdigit():
            mask.append("?d")
        else:
            mask.append("?s")
    return "".join(mask)

# Read passwords from file and generate masks
def process_password_file(file_path):
    masks = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                password = line.strip()
                if password:
                    masks.append(get_mask(password))
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []

    return masks

# Main function to execute the script
def main():
    file_path = "realistic_mixed_length_passwords.txt"  # Replace with your file path if needed
    masks = process_password_file(file_path)

    if not masks:
        print("No data to process.")
        return

    mask_counts = Counter(masks)
    top_masks = mask_counts.most_common(3)

    print("Top 3 Password Masks")
    print("--------------------")
    for i, (mask, count) in enumerate(top_masks, start=1):
        print(f"{i}. {mask}   : {count}")

if __name__ == "__main__":
    main()
