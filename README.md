# A/B Test on Headline Sentiment and Engagement

Analysis of Reddit post titles from r/apple to compare engagement (upvotes and comments) between posts with positive and non-positive headline sentiment.

## Overview

The project collects top posts from r/apple, scores headline sentiment with VADER, and assigns each post to group A (compound sentiment > 0) or group B (compound sentiment ≤ 0). Exploratory analysis and independent t-tests are used to test whether sentiment is associated with differences in score and comment count.

The full write-up and charts are in `notebooks/Lawal_Adam_Ademola.ipynb`. A summary document is linked at the end of that notebook.

## Project structure

```
.
├── data/
│   ├── apple_posts.csv          # Raw scraped posts
│   └── apple_posts_cleaned.csv  # Cleaned data for analysis
├── notebooks/
│   └── Lawal_Adam_Ademola.ipynb
├── src/
│   └── scraper.py
├── data.env                     # Reddit API credentials (not committed)
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository.

2. Create a virtual environment and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add a `data.env` file in the project root with your Reddit API credentials:

   ```
   client_id=your_client_id
   client_secret=your_client_secret
   ```

   Create an app at https://www.reddit.com/prefs/apps if you need credentials.

## Usage

### Scrape data (optional)

If you need fresh data instead of the CSVs in `data/`:

```bash
python src/scraper.py
```

Output is written to `data/apple_posts.csv`.

### Run the analysis

Open and run `notebooks/Lawal_Adam_Ademola.ipynb` from the `notebooks/` directory so paths to `../data/` and `../data.env` resolve correctly.

The notebook loads the CSVs from `data/`, performs cleaning and EDA, and runs t-tests on score and comments by A/B group.

## Data

The repository includes pre-scraped datasets so the notebook can be run without calling the Reddit API. Re-running the scraper will overwrite `data/apple_posts.csv`.

## License

MIT License. See [LICENSE](LICENSE).
