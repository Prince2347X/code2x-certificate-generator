# Function to calculate font size based on name length
def calculate_font_size(name, max_length=20, base_size=60):
    if len(name) > max_length:
        return base_size * (max_length / len(name))
    return base_size

