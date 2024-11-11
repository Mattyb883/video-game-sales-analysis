import pandas as pd

# Load dataset
games_df = pd.read_csv('games.csv')

# Display general information
print(games_df.info())
print(games_df.head())

import pandas as pd
import numpy as np

# Load dataset
games_df = pd.read_csv('games.csv')

# Make column names lowercase
games_df.columns = games_df.columns.str.lower()

# Convert 'year_of_release' to integer, handling NaN values by filling them with 0 or dropping them
games_df['year_of_release'] = games_df['year_of_release'].fillna(0).astype(int)

# Convert 'user_score' to numeric, setting 'TBD' values as NaN
games_df['user_score'] = pd.to_numeric(games_df['user_score'], errors='coerce')

# Here, I'm leaving most missing values as NaN for now; let’s document this decision as we analyze further
# - 'Critic_Score', 'User_Score', and 'Rating' contain many missing entries that may reflect unavailable data

# Calculate total sales
games_df['total_sales'] = games_df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

# Display prepared data sample to verify changes
print(games_df.info())
print(games_df.head())

import matplotlib.pyplot as plt

# Filter out any invalid years (e.g., 0 or other placeholder values)
games_by_year = games_df[games_df['year_of_release'] > 1900]['year_of_release'].value_counts().sort_index()

# Plot the number of game releases per year
plt.figure(figsize=(12, 6))
plt.bar(games_by_year.index, games_by_year.values, color='skyblue')
plt.xlabel("Year of Release")
plt.ylabel("Number of Games Released")
plt.title("Number of Games Released by Year")
plt.xticks(rotation=45)
plt.show()

import numpy as np

# Calculate total sales by platform and identify top platforms
platform_sales = games_df.groupby('platform')['total_sales'].sum().sort_values(ascending=False)
top_platforms = platform_sales.head(5).index  # Select the top 5 platforms for analysis

# Filter data for only the top platforms and valid years
top_platform_data = games_df[(games_df['platform'].isin(top_platforms)) & (games_df['year_of_release'] >= 1980)]

# Plot sales distribution for each top platform by year
plt.figure(figsize=(14, 8))
for platform in top_platforms:
    platform_data = top_platform_data[top_platform_data['platform'] == platform]
    sales_by_year = platform_data.groupby('year_of_release')['total_sales'].sum()
    plt.plot(sales_by_year.index, sales_by_year.values, marker='o', label=platform)

# Labeling the plot
plt.xlabel("Year of Release")
plt.ylabel("Total Sales (Millions)")
plt.title("Total Sales Distribution Over Time for Top Platforms")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Identify first and last year of sales for each platform
platform_years = games_df.groupby('platform')['year_of_release'].agg(['min', 'max'])
platform_years['lifespan'] = platform_years['max'] - platform_years['min']

# Display platform lifespans to understand how long they tend to stay relevant
print(platform_years.sort_values(by='lifespan', ascending=False))

# Filter Data for Relevant Period (2010 and onward)
filtered_games_df = games_df[games_df['year_of_release'] >= 2010]

# Verify the filtering worked by checking the minimum year
print(filtered_games_df['year_of_release'].min())  # Should be 2010 or later
print(filtered_games_df.head())

# Analyze Top Platforms by Sales (2010 and onward)
# Calculate total sales by platform in the filtered data
top_platform_sales = filtered_games_df.groupby('platform')['total_sales'].sum().sort_values(ascending=False)
leading_platforms = top_platform_sales.head(5).index  # Select top 5 platforms

# Plot yearly sales trends for the top platforms
plt.figure(figsize=(14, 8))
for platform in leading_platforms:
    platform_data = filtered_games_df[filtered_games_df['platform'] == platform]
    sales_by_year = platform_data.groupby('year_of_release')['total_sales'].sum()
    plt.plot(sales_by_year.index, sales_by_year.values, marker='o', label=platform)

# Labeling the plot
plt.xlabel("Year of Release")
plt.ylabel("Total Sales (Millions)")
plt.title("Sales Trends for Leading Platforms (2010 and onward)")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Global Sales Distribution by Platform (Box Plot)
import seaborn as sns

# Filter out platforms with very few games to avoid skewed box plots
platform_game_counts = filtered_games_df['platform'].value_counts()
popular_platforms = platform_game_counts[platform_game_counts > 20].index
filtered_popular_platforms = filtered_games_df[filtered_games_df['platform'].isin(popular_platforms)]

# Plot the box plot for global sales by platform
plt.figure(figsize=(14, 8))
sns.boxplot(data=filtered_popular_platforms, x='platform', y='total_sales')
plt.yscale('log')  # Use a log scale to handle wide range of sales values
plt.xlabel("Platform")
plt.ylabel("Total Sales (Millions)")
plt.title("Global Sales Distribution by Platform (2010 and onward)")
plt.xticks(rotation=45)
plt.show()

# Impact of Reviews on Sales for One Platform (e.g., PS4):
# Choose a popular platform, e.g., PS4
selected_platform = 'PS4'
platform_data = filtered_games_df[filtered_games_df['platform'] == selected_platform]

# Scatter plot for Critic Score vs. Total Sales
plt.figure(figsize=(12, 6))
plt.scatter(platform_data['critic_score'], platform_data['total_sales'], alpha=0.5)
plt.xlabel("Critic Score")
plt.ylabel("Total Sales (Millions)")
plt.title(f"Critic Score vs. Total Sales for {selected_platform}")
plt.show()

# Scatter plot for User Score vs. Total Sales
plt.figure(figsize=(12, 6))
plt.scatter(platform_data['user_score'], platform_data['total_sales'], alpha=0.5)
plt.xlabel("User Score")
plt.ylabel("Total Sales (Millions)")
plt.title(f"User Score vs. Total Sales for {selected_platform}")
plt.show()

# Calculate correlations
critic_corr = platform_data['critic_score'].corr(platform_data['total_sales'])
user_corr = platform_data['user_score'].corr(platform_data['total_sales'])

print(f"Correlation between Critic Score and Total Sales for {selected_platform}: {critic_corr}")
print(f"Correlation between User Score and Total Sales for {selected_platform}: {user_corr}")

# Compare Sales of Top-Selling Games Across Platforms

# Filter for games available on multiple platforms with non-zero sales
multi_platform_games = filtered_games_df.groupby('name').filter(
    lambda x: len(x['platform'].unique()) > 1 and x['total_sales'].sum() > 0
)

# Group by game title and calculate total sales across all platforms
top_multi_platform_games = multi_platform_games.groupby('name')['total_sales'].sum()

# Select top 10 best-selling multi-platform games
top_games = top_multi_platform_games.nlargest(10).index
top_games_data = multi_platform_games[multi_platform_games['name'].isin(top_games)]

# Group by game title and platform, then sum total sales
game_platform_sales = top_games_data.groupby(['name', 'platform'])['total_sales'].sum().unstack()

# Display the sales comparison table (first 10 rows for overview)
print(game_platform_sales)

# Plot sales comparison for the top games
game_platform_sales.plot(kind='bar', stacked=True, figsize=(14, 8))
plt.ylabel("Total Sales (Millions)")
plt.title("Sales Comparison for Top 10 Multi-Platform Games")
plt.xticks(rotation=45)
plt.show()

# Profitability Analysis by Genre

# Count of Games by Genre
genre_counts = filtered_games_df['genre'].value_counts()
print("Number of Games by Genre:\n", genre_counts)

# Total Sales by Genre
genre_sales = filtered_games_df.groupby('genre')['total_sales'].sum().sort_values(ascending=False)
print("\nTotal Sales by Genre:\n", genre_sales)

# Average Sales per Game by Genre
average_genre_sales = genre_sales / genre_counts
average_genre_sales = average_genre_sales.sort_values(ascending=False)
print("\nAverage Sales per Game by Genre:\n", average_genre_sales)

# Plot the distribution of total and average sales by genre
plt.figure(figsize=(14, 6))

# Plot total sales by genre
plt.subplot(1, 2, 1)
genre_sales.plot(kind='bar', color='lightblue')
plt.xlabel("Genre")
plt.ylabel("Total Sales (Millions)")
plt.title("Total Sales by Genre")
plt.xticks(rotation=45)

# Plot average sales by genre
plt.subplot(1, 2, 2)
average_genre_sales.plot(kind='bar', color='lightgreen')
plt.xlabel("Genre")
plt.ylabel("Average Sales per Game (Millions)")
plt.title("Average Sales per Game by Genre")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Regional Profiles for NA, EU, JP

# Define regions and sales columns
regions = {'NA': 'na_sales', 'EU': 'eu_sales', 'JP': 'jp_sales'}

# Top Five Platforms by Region
for region, sales_column in regions.items():
    print(f"\nTop 5 Platforms in {region}:")
    top_platforms = filtered_games_df.groupby('platform')[sales_column].sum().sort_values(ascending=False).head(5)
    print(top_platforms)

# Top Five Genres by Region
for region, sales_column in regions.items():
    print(f"\nTop 5 Genres in {region}:")
    top_genres = filtered_games_df.groupby('genre')[sales_column].sum().sort_values(ascending=False).head(5)
    print(top_genres)

# ESRB Ratings and Sales Impact by Region
for region, sales_column in regions.items():
    print(f"\nESRB Rating Impact on Sales in {region}:")
    esrb_sales = filtered_games_df.groupby('rating')[sales_column].sum().sort_values(ascending=False)
    print(esrb_sales)

from scipy.stats import ttest_ind

# Filter data for user ratings on Xbox One and PC platforms
xbox_one_ratings = filtered_games_df[(filtered_games_df['platform'] == 'XOne') & 
                                     (filtered_games_df['user_score'].notna())]['user_score']
pc_ratings = filtered_games_df[(filtered_games_df['platform'] == 'PC') & 
                               (filtered_games_df['user_score'].notna())]['user_score']

# Hypothesis 1: Xbox One vs. PC User Ratings
t_stat, p_value = ttest_ind(xbox_one_ratings, pc_ratings, equal_var=False)
print(f"Hypothesis 1 - Xbox One vs. PC User Ratings:\n t-statistic: {t_stat}, p-value: {p_value}")

# Filter data for user ratings in Action and Sports genres
action_ratings = filtered_games_df[(filtered_games_df['genre'] == 'Action') & 
                                   (filtered_games_df['user_score'].notna())]['user_score']
sports_ratings = filtered_games_df[(filtered_games_df['genre'] == 'Sports') & 
                                   (filtered_games_df['user_score'].notna())]['user_score']

# Hypothesis 2: Action vs. Sports Genre Ratings
t_stat_genre, p_value_genre = ttest_ind(action_ratings, sports_ratings, equal_var=False)
print(f"Hypothesis 2 - Action vs. Sports Genre Ratings:\n t-statistic: {t_stat_genre}, p-value: {p_value_genre}")

