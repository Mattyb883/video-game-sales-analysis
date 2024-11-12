# Ice Video Game Analysis

## Project Overview
This project analyzes video game sales data to identify factors contributing to game success across platforms, genres, and regions. By examining trends, regional preferences, and the impact of user and critic reviews, this analysis provides strategic insights to inform game development, marketing, and release strategies for Ice, an international video game store.

## Objectives
- Identify platform trends and lifespan to target profitable platforms for future releases.
- Assess genre profitability to prioritize development in high-demand categories.
- Analyze regional preferences across North America, Europe, and Japan for region-specific strategies.
- Evaluate the influence of critic and user reviews on sales to understand the role of reviews in purchase decisions.
- Perform hypothesis testing to assess user satisfaction across platforms and genres.

## Dataset Information
The dataset includes video game sales data from open sources and covers the following fields:

| Column Name     | Description                                      |
|-----------------|--------------------------------------------------|
| `name`          | Game title                                       |
| `platform`      | Platform (e.g., Xbox, PlayStation)               |
| `year_of_release` | Year of game release                            |
| `genre`         | Genre of the game                                |
| `na_sales`      | North American sales (millions USD)              |
| `eu_sales`      | European sales (millions USD)                    |
| `jp_sales`      | Japanese sales (millions USD)                    |
| `other_sales`   | Sales in other regions (millions USD)            |
| `critic_score`  | Critic review score (out of 100)                 |
| `user_score`    | User review score (out of 10)                    |
| `rating`        | ESRB rating (e.g., E, T, M)                      |

**Note**: All sales figures are represented in **millions of USD**.

## Project Structure
The analysis follows these main steps:
1. **Data Loading and Preparation**: Load and clean the data, handle missing values, and prepare it for analysis.
2. **Exploratory Analysis**: Examine game releases by year, sales distributions by platform, and genre profitability.
3. **Regional Profile Analysis**: Identify top platforms and genres in North America, Europe, and Japan and assess the impact of ESRB ratings.
4. **Review Impact Analysis**: Explore how critic and user reviews influence sales on popular platforms.
5. **Hypothesis Testing**: Test hypotheses regarding user ratings for platforms and genres to assess user preferences.
6. **Conclusions and Recommendations**: Summarize findings and provide strategic recommendations for Ice’s future releases and marketing efforts.

## Key Findings
- **Platform Trends**: Platforms with longer lifespans and recent popularity are promising targets. Multi-platform releases increase reach and revenue.
- **Genre Profitability**: High-demand genres show strong sales, while niche genres with loyal audiences also offer profitability.
- **Regional Preferences**: Distinct preferences for platforms and genres across regions, with age-related trends highlighted by ESRB ratings.
- **Impact of Reviews**: Critic reviews moderately impact sales, whereas user reviews show minimal influence on initial purchases.
- **User Ratings**: No significant difference in user satisfaction between Xbox One and PC; Action and Sports genres show notable differences in user ratings.

## How to Run This Analysis
1. **Requirements**:
   - Python 3.x
   - Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`

2. **To Run**:
   - Clone this repository:
     ```bash
     git clone https://github.com/Mattyb883/ice_video_game_analysis.git
     cd ice_video_game_analysis
     ```
   - Run the Jupyter Notebook `data_analysis.ipynb` to execute the analysis.

## Repository Structure
```plaintext
ice_video_game_analysis/
│
├── data_analysis.ipynb      # Jupyter Notebook with full analysis
├── README.md                # Project overview and instructions
├── games.csv                # Dataset file (ensure to load in the notebook)
├── .gitignore               # Ignoring unnecessary files
└── requirements.txt         # List of libraries needed (optional)
