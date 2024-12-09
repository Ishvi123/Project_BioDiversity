def calculate_average_population(data):
    """Calculate the average population for each species."""
    average_population = data.groupby('species_name')['population_count'].mean()
    return average_population
