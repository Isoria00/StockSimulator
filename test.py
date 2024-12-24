import tkinter as tk

def adjust_width(original_width, reference_width, current_width):
    """
    Adjust the width of an element based on the current screen width.
    
    :param original_width: The original width value of the element (e.g., 25 for the label).
    :param reference_width: The width of the reference screen (e.g., 1920 for your monitor).
    :param current_width: The width of the current screen (e.g., 800 for your laptop).
    :return: The adjusted width for the element based on the current screen size.
    """
    # Calculate the width ratio
    width_ratio = current_width / reference_width
    # Adjust the width based on the ratio
    adjusted_width = int(original_width * width_ratio)
    return adjusted_width

# Example usage
root = tk.Tk()

# Example values: reference screen is 1920x1080, current screen is 800x600
reference_width = 1920
current_width = root.winfo_screenwidth()  # Get the current screen width

# Original label width (e.g., 25)
original_label_width = 25
adjusted_label_width = adjust_width(original_label_width, reference_width, current_width)

# Now you can use the adjusted label width in your label creation
difficulty_label = tk.Label(
    root,
    text="Difficulty: Easy",
    fg='white',
    width=adjusted_label_width,  # Adjusted width
    bg='black',
    borderwidth=5,
    font=("System", 22)
)
difficulty_label.pack(pady=10)

root.mainloop()
