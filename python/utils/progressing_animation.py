from tqdm import tqdm
import time

# Number of iterations for the processing animation
num_iterations = 100

# Create a progress bar using tqdm with leave=True
progress_bar = tqdm(total=num_iterations, unit='iteration', desc='Processing', bar_format='{desc}: {percentage:3.0f}% {bar}', leave=True)

# First loop
for _ in range(num_iterations // 2):
    # Perform some processing here
    time.sleep(0.1)  # Simulate a small delay
    
    # Update the progress bar
    progress_bar.update(1)

# Reset the progress bar to 0 and leave=True
progress_bar.reset(total=num_iterations)

# Second loop
for _ in range(num_iterations // 2):
    # Perform some processing here
    time.sleep(0.1)  # Simulate a small delay
    
    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()
