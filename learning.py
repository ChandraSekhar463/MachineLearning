import pandas as pd
import matplotlib.pyplot as plt
import io

# Create sample data as a CSV string
csv_data = """
Age,Height,Weight
15,165,55
16,170,60
17,175,65
18,180,70
19,185,75
"""

# Create a file-like object from the CSV string
students_csv = io.StringIO(csv_data)

# Step 1: Load the CSV file from the in-memory object
data = pd.read_csv(students_csv)

# Step 2: Extract columns
heights = data['Height']
weights = data['Weight']
ages = data['Age']

# Step 3: Create Visualizations

# 1. Scatter Plot: Height vs. Weight
plt.figure(figsize=(8, 5))
plt.scatter(heights, weights, color='blue', label='Height vs Weight')
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.legend()
plt.grid()
plt.show()

# 2. Line Plot: Age vs Height
plt.figure(figsize=(8, 5))
plt.plot(ages, heights, marker='o', color='green', label='Age vs Height')
plt.title("Age vs Height")
plt.xlabel("Age (years)")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid()
plt.show()

# 3. Bar Plot: Age vs Weight
plt.figure(figsize=(8, 5))
plt.bar(ages, weights, color='orange', label='Age vs Weight')
plt.title("Age vs Weight")
plt.xlabel("Age (years)")
plt.ylabel("Weight (kg)")
plt.legend()
plt.grid(axis='y')
plt.show()
