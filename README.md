# ETL Pipeline Simple

It is a very simple ETL pipeline. We perform the following steps:

- Fetch the data from an API
- Clean and transform it
- Load it into SQLite

Below is an image of the loaded data:

![Loaded Data](https://github.com/user-attachments/assets/e0882b62-c7ac-4e90-8f21-6395146ca5a4)

## Tech Stack

- **Python**
- **Requests** (for API data fetching)
- **Pandas** (for data transformation)
- **SQLAlchemy** (for database operations)
- **SQLite** (as the database)

## How to Run

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
