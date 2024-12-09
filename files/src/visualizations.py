import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import pandas as pd

def plot_population_trends(data):
    """Visualize population trends over time for each species."""
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='year', y='population_count', hue='species_name', marker='o')
    plt.title('Population Trends of Species Over Time')
    plt.xlabel('Year')
    plt.ylabel('Population Count')
    plt.legend(title='Species')
    plt.grid(True)
    plt.tight_layout()
    plt.show(block=True)  # Keeps the plot open until manually closed

def plot_total_population_by_species(data):
    """Visualize total population count for each species."""
    plt.figure(figsize=(8, 6))
    species_population = data.groupby('species_name')['population_count'].sum().reset_index()
    sns.barplot(data=species_population, x='species_name', y='population_count', palette='viridis')
    plt.title('Total Population by Species')
    plt.xlabel('Species')
    plt.ylabel('Total Population Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=True)

def plot_population_distribution(data):
    """Visualize the distribution of population counts."""
    plt.figure(figsize=(8, 6))
    sns.histplot(data['population_count'], bins=20, kde=True, color='skyblue')
    plt.title('Population Count Distribution')
    plt.xlabel('Population Count')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show(block=True)

def plot_population_heatmap(data):
    """Visualize population counts over time as a heatmap."""
    pivot_data = data.pivot_table(values='population_count', index='species_name', columns='year', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_data, cmap='coolwarm', annot=False)
    plt.title('Population Count Heatmap')
    plt.xlabel('Year')
    plt.ylabel('Species')
    plt.tight_layout()
    plt.show(block=True)

def plot_geographical_spread(data):
    """Visualize geographical spread of species."""
    if {'latitude', 'longitude'}.issubset(data.columns):
        gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['longitude'], data['latitude']))
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        ax = world.plot(figsize=(15, 10), color='lightgrey')
        gdf.plot(ax=ax, color='red', markersize=10)
        plt.title('Geographical Spread of Species')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.tight_layout()
        plt.show(block=True)
    else:
        print("Geographical data not available in dataset.")

def plot_population_distribution_by_year(data):
    """Visualize population distribution by year using boxplots."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x='year', y='population_count', palette='coolwarm')
    plt.title('Population Distribution by Year')
    plt.xlabel('Year')
    plt.ylabel('Population Count')
    plt.tight_layout()
    plt.show(block=True)
