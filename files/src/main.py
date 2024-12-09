from data_processing import load_and_process_data
from visualizations import (
    plot_population_trends,
    plot_total_population_by_species,
    plot_population_distribution,
    plot_population_heatmap,
    plot_geographical_spread,
    plot_population_distribution_by_year
)

def main():
    """Main function to load data, process it, and create visualizations."""
    # Load and process data
    data_file = 'data/biodiversity_data.csv'
    data = load_and_process_data(data_file)
    
    # Generate plots one by one
    plot_population_trends(data)
    plot_total_population_by_species(data)
    plot_population_distribution(data)
    plot_population_heatmap(data)
    plot_geographical_spread(data)
    plot_population_distribution_by_year(data)

if __name__ == "__main__":
    main()
