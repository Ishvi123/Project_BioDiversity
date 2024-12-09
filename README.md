# Project_BioDiversity
The Biodiversity Trends Analysis project aims to analyze biodiversity datasets and visualize population changes for various species. The project leverages Python's data analysis and visualization libraries to provide insights into the population trends of different species and their geographical distribution.

This tool helps in understanding the impact of environmental changes on species populations and provides a foundation for conservation efforts.

Contributors
ISHVI SHAH   - Ku2407u083
JIYA PATEL   - Ku2407u093 
KRISH PATEL  - Ku2407u115
Prenya PATEL - Ku2407u172

Goals
Analyze biodiversity datasets to identify trends in species population.
Visualize data through various charts and graphs to communicate insights effectively.
Demonstrate the use of Python libraries for data analysis and visualization.
Features
Data Loading & Preprocessing: Read and preprocess data from CSV files.
Visualization:
Line charts for population trends over time.
Bar charts to compare populations across species.
Pie charts showing population proportions by category.
Heatmaps for correlation between species populations.
Extensibility: The modular design allows for easy addition of new datasets and visualizations.
Technologies Used
The following libraries were used for implementing the project:

Python (v3.11): The programming language for analysis and visualization.
Libraries:
pandas: For data manipulation and analysis.
numpy: For numerical computations.
matplotlib: For static, interactive, and animated visualizations.
seaborn: For enhanced statistical data visualization.
folium: For geographical data visualization (optional).
os: To handle file paths and directories.

Setup Instructions
Follow these steps to set up and run the project on your local machine:

Prerequisites
Python installed on your system (v3.11 recommended).
Basic knowledge of Python and its libraries.

Clone the repository to your local machine:
git clone https://github.com/Ishvi123/Project_BioDiversity.git

Install the required libraries:
pip install pandas numpy matplotlib seaborn folium

Run the main script:
python files/src/main.py

Results
Visualizations
The project generates the following types of visualizations:

Population Trends:
Line charts showing the changes in species populations over the years.
Bar charts comparing population sizes across species or regions.
Heatmaps depicting relationships between various species populations.

Challenges Faced
Dataset Collection and Preparation

Challenge: Obtaining a dataset that accurately represents biodiversity trends was difficult due to limited availability and inconsistent data formats.
Resolution: A synthetic dataset was created to simulate real-world biodiversity data, ensuring that the project demonstrates the required analysis capabilities.
Dependency and Compatibility Issues

Challenge: Encountered version conflicts with libraries like matplotlib and kiwisolver during installation and execution.
Resolution: Ensured compatibility by reinstalling packages and verifying the Python environment setup.
Sequential Display of Visualizations

Challenge: Initially, only one plot was displayed, and others were overwritten.
Resolution: Used plt.show(block=True) to ensure each plot was displayed sequentially.
Dataset Preparation and Cleaning

Challenge: Handling missing or inconsistent data impacted the quality of analysis.
Resolution: Cleaned the dataset using pandas by filling or filtering incomplete records to ensure meaningful results.

Insights
Species populations that are in decline or growth.
Geographic regions requiring immediate conservation efforts.
Correlations between environmental changes and species population trends.

