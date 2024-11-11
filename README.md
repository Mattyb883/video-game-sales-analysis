# Ice Games Analysis Project

This project analyzes video game sales data for the online store Ice, identifying patterns in successful games to help inform future campaigns.

## Project Outline
1. **Data Exploration and Cleaning**
2. **Data Preparation**
3. **Exploratory Data Analysis (EDA)**
4. **Feature Engineering**
5. **Predictive Modeling**
6. **Insights and Recommendations**

---------------

## Data Preparation Notes

### Column Adjustments
- **Column Names**: Converted all column names to lowercase for consistency.

### Data Type Conversions
- **`year_of_release`**: Converted to integer type. Missing years were filled with `0` to allow a complete integer conversion, with `0` representing unknown values.
- **`user_score`**: Converted to numeric type. Instances of “TBD” (to be determined) were treated as missing values (`NaN`), as they indicate scores were not available at the time.

### Missing Values Handling
- **`year_of_release`**: Missing values were filled with `0` to preserve data structure.
- **`critic_score`, `user_score`, and `rating`**: Left missing values as `NaN`, assuming these reflect instances where data was unavailable.

### Total Sales Calculation
- **`total_sales`**: Created a new column summing `NA_sales`, `EU_sales`, `JP_sales`, and `Other_sales` for an overall sales figure.

### Rationale for Missing Values
- **Reasons for Missing Data**:
  - `critic_score` and `rating`: Likely missing for games not submitted for review or ESRB rating.
  - `year_of_release`: Potentially missing due to historical data limitations.

---

## Running the Analysis
1. **Install Dependencies**: Use `venv` and `pip` to install required packages.
2. **Run Analysis Script**: Execute `data_analysis.py` in the terminal.

---

## Notes
Further analysis will explore patterns in game success based on features such as genre, platform, and sales regions.

---------------

## Insights

### 1. Game Release Trends
- **Observation**: Game releases have varied significantly over the years, with certain years seeing more releases than others.
- **Implication**: Timing new releases during years or seasons of lower competition might maximize visibility.

### 2. Platform Sales Analysis
- **Top Platforms**: Platforms like `PS4`, `Xbox One`, and `3DS` consistently show high total sales.
- **Growth and Decline**: Some platforms are still growing strongly, while others are showing decline as they phase out.
- **Implication**: Advertising campaigns should focus on high-sales, high-growth platforms and deprioritize those in decline.

### 3. Review Impact on Sales
- **Correlation**: There is a moderate-to-strong correlation between review scores (both critic and user) and sales for some platforms.
- **Implication**: For certain platforms, emphasizing user and critic engagement may positively impact sales. 

### 4. Genre Analysis
- **Most Profitable Genres**: Genres like `Action`, `Sports`, and `Shooter` have the highest total sales, appealing to broad audiences.
- **Sales Consistency**: Certain genres also show high average sales per game, indicating stable profitability.
- **Implication**: Focusing on high-sales genres could maximize profitability, especially those with both high volume and consistent per-game sales.

### 5. Multi-Platform Games
- **Platform Performance**: Some platforms yield significantly higher sales for the same titles, highlighting preferred platforms for multi-platform releases.
- **Implication**: For games released on multiple platforms, marketing efforts should be concentrated on the platforms with historically higher sales.

### 6. Regional Profiles

#### Top Platforms by Region
- **North America (NA)**: The top platforms in NA show a preference for platforms like `PS4` and `Xbox One`, which dominate sales.
- **Europe (EU)**: Similar to NA, Europe also shows strong sales for `PS4` and `Xbox One`, with minor regional variations.
- **Japan (JP)**: Japan’s top platforms differ significantly, with platforms like `3DS` and other handheld consoles showing high popularity, reflecting a preference for portable gaming.

#### Top Genres by Region
- **North America (NA)**: Action and sports genres are the most popular in NA.
- **Europe (EU)**: Similar to NA, action and sports genres lead in Europe, with shooter games also showing significant sales.
- **Japan (JP)**: Japan’s market favors RPGs and other genres that are less popular in NA and EU, highlighting cultural differences in gaming preferences.

#### ESRB Rating Impact on Sales
- **North America (NA)**: Ratings like `E` (Everyone) and `M` (Mature) have the highest sales, indicating broad appeal across age groups.
- **Europe (EU)**: Sales by ESRB rating are similar to NA, with a strong preference for `E`-rated games.
- **Japan (JP)**: ESRB ratings have less impact, as many games are unrated, likely due to different regional rating systems.

---

## Recommendations

1. **Target High-Growth Platforms**: Prioritize platforms showing strong growth in recent years, such as `PS4` and `Xbox One`, for new game releases and advertising.

2. **Emphasize High-Review Platforms**: For platforms where review scores significantly impact sales, encourage user and critic engagement to boost ratings.

3. **Focus on Popular, Profitable Genres**: Concentrate on high-sales genres like `Action` and `Sports`, as they have proven to attract large audiences with consistent sales per title.

4. **Optimize Multi-Platform Releases**: For games available on multiple platforms, direct marketing toward platforms with the highest historical sales for similar games.

5. **Region-Specific Platform Focus**: Prioritize marketing efforts based on regional platform preferences. For instance, campaigns in Japan should focus on handheld platforms like `3DS`.
   
6. **Genre-Specific Marketing**: Tailor advertising by genre based on regional preferences—focus on RPGs for Japan, while emphasizing action and sports genres in NA and EU.

7. **Content Rating Consideration**: In NA and EU, focus on `E` and `M`-rated games for broader appeal, as these ratings correlate with higher sales. In Japan, ESRB ratings are less impactful.

---

## Hypothesis Testing

### Hypothesis 1: Xbox One vs. PC User Ratings
- **Hypothesis**: The average user ratings for games on the Xbox One and PC platforms are the same.
- **Result**: With a p-value of `0.9802`, we fail to reject the null hypothesis.
- **Conclusion**: There is no statistically significant difference in average user ratings between Xbox One and PC platforms, suggesting that users rate games on these platforms similarly on average.

### Hypothesis 2: Action vs. Sports Genre Ratings
- **Hypothesis**: The average user ratings for games in the Action and Sports genres are different.
- **Result**: With a p-value of `1.45e-15`, we reject the null hypothesis.
- **Conclusion**: There is a statistically significant difference in average user ratings between the Action and Sports genres. This finding indicates that users rate games in these genres differently, with a clear preference or perception disparity between them.

---

### Summary of Hypothesis Testing
- **Platform Ratings Similarity**: The hypothesis test suggests that user ratings do not differ significantly between Xbox One and PC platforms.
- **Genre Ratings Difference**: There is a notable difference in user ratings between Action and Sports genres, reflecting varied user preferences or perceptions for these genres.

---------------

## Conclusion

This analysis provided a comprehensive look at the key factors influencing video game sales across regions, platforms, and genres. By examining historical sales data, user and critic ratings, and genre preferences, we developed insights to guide future marketing and release strategies for Ice’s video game store.

### Key Findings and Recommendations

1. **Regional Market Preferences**:
   - **Platform Popularity**: North America and Europe share similar platform preferences, with strong sales for `PS4` and `Xbox One`. Japan, however, favors portable platforms like `3DS`, indicating a regional preference for handheld gaming.
   - **Genre Preferences**: The Action and Sports genres dominate in North America and Europe, while RPGs are the top choice in Japan. Tailoring marketing efforts based on these regional genre preferences could optimize engagement and sales.

2. **Impact of Reviews on Sales**:
   - Critic and user reviews positively correlate with sales on certain platforms, suggesting that high review scores can enhance sales performance. Platforms where reviews significantly impact sales should prioritize engagement strategies that boost review scores.

3. **Profitability of Genres**:
   - Genres like Action, Sports, and Shooter exhibit the highest total sales, while others have high average sales per game. Focusing on these genres can maximize profitability, especially in regions where these genres are already popular.

4. **Multi-Platform Strategy**:
   - Games released on multiple platforms show varying sales performance. Concentrating marketing and release efforts on platforms that yield higher sales for multi-platform games could enhance revenue.

5. **User Rating Insights**:
   - Hypothesis testing indicated no significant difference in average user ratings between Xbox One and PC, while user ratings for Action and Sports genres differ significantly. This suggests that platform-related user satisfaction is consistent, but genre preferences do affect user ratings.

### Final Recommendations

- **Focus Marketing on Regional Trends**: Target high-sales platforms and genres based on each region's preferences to increase campaign relevance.
- **Engage Users and Critics on Key Platforms**: For platforms where reviews impact sales, prioritize strategies that enhance user engagement and critic outreach.
- **Optimize Multi-Platform Releases**: For multi-platform games, direct efforts toward platforms that demonstrate higher sales potential.
- **Emphasize High-Performance Genres**: Concentrate resources on Action, Sports, and Shooter genres, particularly in regions with strong demand.

This project has outlined data-driven strategies that can help Ice maximize sales potential through informed platform, genre, and regional focus. By aligning marketing and product strategies with these findings, Ice can better anticipate and meet customer preferences across its global markets.

---

## Running the Analysis
1. **Set up the Environment**: Install dependencies using the provided `venv`.
2. **Execute the Analysis**: Run `data_analysis.py` for a complete analysis workflow.

---

## Notes
This analysis provides actionable insights to guide Ice's advertising and product strategies for future campaigns, especially for anticipated releases in 2017.
