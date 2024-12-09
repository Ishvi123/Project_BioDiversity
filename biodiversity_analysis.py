# biodiversity_analysis.py

# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Step 2: Load the dataset (make sure to provide the correct path to your CSV)
df = pd.read_csv('biodiversity_data.csv')

# Step 3: Data preprocessing (drop missing values, correct data types if needed)
df = df.dropna()  # Remove rows with missing values

# Step 4: Explore the dataset (optional)
print(df.head())  # Show the first few rows to understand the dataset

# Step 5: Create a bar plot to visualize species populations
plt.figure(figsize=(10, 6))
sns.barplot(x='Species', y='Population', data=df, palette='viridis')
plt.title('Species Population Distribution')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 6: Create a Folium map (if Latitude and Longitude are available in the dataset)
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    m = folium.Map(location=[20.0, 0.0], zoom_start=2)  # Global center
    
    # Add markers to the map for each species
    for idx, row in df.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6,
            popup=f"Species: {row['Species']}<br>Population: {row['Population']}",
        ).add_to(m)
    
    # Save the map to an HTML file
    m.save('biodiversity_map.html')
    print("Map saved as 'biodiversity_map.html'. Open the file to view the map.")

# Step 7: Additional Plotting (if Year column exists, show trends over time)
if 'Year' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Year', y='Population', data=df, hue='Species')
    plt.title('Population Trends Over Time')
    plt.tight_layout()
    plt.show()
