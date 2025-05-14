# Ice Video Game Sales Analysis

This project analyzes video game sales data to identify trends, forecast potential high-performing games, and inform strategic decisions for platform selection, marketing, and development. The dataset includes sales figures, user and critic reviews, ESRB ratings, genres, and platform information.

## Table of Contents

- [Project Description](#project-description)
- [Step 1: General Data Overview](#step-1-general-data-overview)
- [Step 2: Data Preparation](#step-2-data-preparation)
- [Step 3: Exploratory Data Analysis](#step-3-exploratory-data-analysis)
  - [Game Releases by Year](#game-releases-by-year)
  - [Platform Sales and Lifespan](#platform-sales-and-lifespan)
  - [Sales Distribution by Platform](#sales-distribution-by-platform)
  - [Review Score Impact](#review-score-impact)
  - [Genre Profitability](#genre-profitability)
- [Step 4: Regional User Profiles](#step-4-regional-user-profiles)
- [Step 5: Hypothesis Testing](#step-5-hypothesis-testing)
- [Step 6: Project Conclusion](#step-6-project-conclusion)
- [Technical Notes](#technical-notes)

---

## Project Description

Ice, an online video game store, wants to analyze historical sales data to understand what makes a game successful. By exploring patterns in genre, platform, region, and reviews, this analysis will guide 2017 marketing strategies and future releases.

## Step 1: General Data Overview
Initial inspection of the dataset including column types, structure, and missing values.

## Step 2: Data Preparation
- Standardized column names
- Converted datatypes
- Addressed missing and anomalous values (e.g., `TBD`)
- Calculated `total_sales` across all regions

## Step 3: Exploratory Data Analysis

### Game Releases by Year
Distribution of game releases across years and assessment of data completeness.

### Platform Sales and Lifespan
Top-performing platforms, emergence and decline timelines, and relevance for prediction.

### Sales Distribution by Platform
Box plots of global sales per platform to understand spread and outliers.

### Review Score Impact
Correlation between user and critic scores vs. global sales across multiple platforms.

### Genre Profitability
Most and least profitable genres based on total and average sales.

## Step 4: Regional User Profiles
- Top 5 platforms and genres per region (NA, EU, JP)
- ESRB rating impact on regional sales
- Visualized with pie charts for clarity

## Step 5: Hypothesis Testing
- Tested if Xbox One and PC user ratings are statistically similar
- Tested if user ratings for Action and Sports genres are statistically different
- Included null/alternative hypotheses and significance interpretation

## Step 6: Project Conclusion
Summary of insights, strategic recommendations, and key takeaways for Ice’s business decisions.

## Technical Notes
- Programming language: Python
- Libraries used: pandas, matplotlib, seaborn, scipy
- All monetary figures are in **USD millions**
