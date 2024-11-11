import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load dataset
games_df = pd.read_csv('games.csv')

# Data Preparation
games_df.columns = games_df.columns.str.lower()
games_df['year_of_release'] = games_df['year_of_release'].fillna(0).astype(int)
games_df['user_score'] = pd.to_numeric(games_df['user_score'], errors='coerce')
games_df['total_sales'] = games_df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

# Define helper functions for modular analysis
def filter_data(data, platforms=None, start_year=None):
    """Filter data by platforms and start year."""
    if platforms:
        data = data[data['platform'].isin(platforms)]
    if start_year:
        data = data[data['year_of_release'] >= start_year]
    return data

def plot_sales_by_platform(platform_data, title):
    """Plot total sales by platform over time."""
    plt.figure(figsize=(14, 8))
    for platform in platform_data['platform'].unique():
        sales_by_year = platform_data[platform_data['platform'] == platform].groupby('year_of_release')['total_sales'].sum()
        plt.plot(sales_by_year.index, sales_by_year.values, marker='o', label=platform)
    plt.xlabel("Year of Release")
    plt.ylabel("Total Sales (Millions)")
    plt.title(title)
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

def plot_box(data, x_col, y_col, title):
    """Create a box plot for sales distribution by category."""
    plt.figure(figsize=(14, 8))
    sns.boxplot(data=data, x=x_col, y=y_col)
    plt.yscale('log')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()

def plot_scatter(data, x_col, y_col, title):
    """Create a scatter plot for two columns."""
    plt.figure(figsize=(12, 6))
    plt.scatter(data[x_col], data[y_col], alpha=0.5)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.show()

def calculate_and_print_correlation(data, col1, col2):
    """Calculate and print the correlation between two columns."""
    corr = data[col1].corr(data[col2])
    print(f"Correlation between {col1} and {col2}: {corr}")
    return corr

# Step 1: Analyze Game Releases by Year
games_by_year = games_df[games_df['year_of_release'] > 1900]['year_of_release'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.bar(games_by_year.index, games_by_year.values, color='skyblue')
plt.xlabel("Year of Release")
plt.ylabel("Number of Games Released")
plt.title("Number of Games Released by Year")
plt.xticks(rotation=45)
plt.show()

# Step 2: Top Platforms by Sales and Yearly Distribution
top_platforms = games_df.groupby('platform')['total_sales'].sum().sort_values(ascending=False).head(5).index
top_platform_data = filter_data(games_df, platforms=list(top_platforms), start_year=1980)  # Convert top_platforms to a list
plot_sales_by_platform(top_platform_data, "Total Sales Distribution Over Time for Top Platforms")

# Step 3: Platform Lifespans
platform_years = games_df.groupby('platform')['year_of_release'].agg(['min', 'max'])
platform_years['lifespan'] = platform_years['max'] - platform_years['min']
print(platform_years.sort_values(by='lifespan', ascending=False))

# Step 4: Filter Data for Relevant Period (2010 onward)
filtered_games_df = filter_data(games_df, start_year=2010)

# Step 5: Sales Distribution by Platform (Box Plot)
platform_game_counts = filtered_games_df['platform'].value_counts()
popular_platforms = platform_game_counts[platform_game_counts > 20].index
filtered_popular_platforms = filtered_games_df[filtered_games_df['platform'].isin(popular_platforms)]
plot_box(filtered_popular_platforms, 'platform', 'total_sales', "Global Sales Distribution by Platform (2010 and onward)")

# Step 6: Impact of Reviews on Sales for One Platform (e.g., PS4)
selected_platform = 'PS4'
platform_data = filtered_games_df[filtered_games_df['platform'] == selected_platform]
plot_scatter(platform_data, 'critic_score', 'total_sales', f"Critic Score vs. Total Sales for {selected_platform}")
plot_scatter(platform_data, 'user_score', 'total_sales', f"User Score vs. Total Sales for {selected_platform}")
calculate_and_print_correlation(platform_data, 'critic_score', 'total_sales')
calculate_and_print_correlation(platform_data, 'user_score', 'total_sales')

# Step 7: Regional Profiles
regions = {'NA': 'na_sales', 'EU': 'eu_sales', 'JP': 'jp_sales'}
for region, sales_column in regions.items():
    print(f"\nTop 5 Platforms in {region}:")
    top_platforms = filtered_games_df.groupby('platform')[sales_column].sum().sort_values(ascending=False).head(5)
    print(top_platforms)
    print(f"\nTop 5 Genres in {region}:")
    top_genres = filtered_games_df.groupby('genre')[sales_column].sum().sort_values(ascending=False).head(5)
    print(top_genres)
    print(f"\nESRB Rating Impact on Sales in {region}:")
    esrb_sales = filtered_games_df.groupby('rating')[sales_column].sum().sort_values(ascending=False)
    print(esrb_sales)

# Step 8: Hypothesis Testing
xbox_one_ratings = filtered_games_df[(filtered_games_df['platform'] == 'XOne') & (filtered_games_df['user_score'].notna())]['user_score']
pc_ratings = filtered_games_df[(filtered_games_df['platform'] == 'PC') & (filtered_games_df['user_score'].notna())]['user_score']
t_stat, p_value = ttest_ind(xbox_one_ratings, pc_ratings, equal_var=False)
print(f"\nHypothesis 1 - Xbox One vs. PC User Ratings:\n t-statistic: {t_stat}, p-value: {p_value}")

action_ratings = filtered_games_df[(filtered_games_df['genre'] == 'Action') & (filtered_games_df['user_score'].notna())]['user_score']
sports_ratings = filtered_games_df[(filtered_games_df['genre'] == 'Sports') & (filtered_games_df['user_score'].notna())]['user_score']
t_stat_genre, p_value_genre = ttest_ind(action_ratings, sports_ratings, equal_var=False)
print(f"\nHypothesis 2 - Action vs. Sports Genre Ratings:\n t-statistic: {t_stat_genre}, p-value: {p_value_genre}")
