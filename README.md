# Semantic Scholar Journal Scraper

A Python application for extracting academic paper metadata from the Semantic Scholar API. This tool enables researchers to efficiently collect scholarly publication data with automatic filtering for the most recent publications.

## Features

- **Automated Data Collection**: Retrieve comprehensive paper metadata including titles, authors, abstracts, citations, DOI, and keywords
- **Time-based Filtering**: Configurable year range filtering (default: last 5 years)
- **Rate Limit Management**: Built-in request throttling to comply with API limitations  
- **Data Export**: Clean CSV output with structured data organization
- **Error Handling**: Robust error management for network issues and API responses
- **Progress Tracking**: Real-time progress indicators during data collection

## Prerequisites

- Python 3.7 or higher
- Internet connection
- No API key required (uses public Semantic Scholar API)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/fikreynurz/AutomationTesting-A11.git
cd jurnal_scraper
```

### 2. Create Virtual Environment

Create an isolated Python environment to avoid dependency conflicts:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install requests pandas
```

## Usage

### Basic Usage

1. **Configure Search Parameters**: Edit the main execution block in `scraper.py`:

```python
if __name__ == "__main__":
    # Specify your research topic
    topic = "machine learning optimization"
    
    # Execute scraping
    fetch_semantic_scholar_filtered(
        query=topic,
        total_results=1000,  # Number of papers to retrieve
        years_back=5         # Years from current date
    )
```

2. **Run the Scraper**:

```bash
python scraper.py
```

### Output Structure

The application generates CSV files in the `output/` directory with the following columns:

| Column | Description |
|--------|-------------|
| Title | Paper title |
| Year | Publication year |
| Citations | Citation count |
| Authors | Author names (comma-separated) |
| Venue | Publication venue |
| URL | Semantic Scholar paper URL |
| DOI | Digital Object Identifier |
| Keywords | Research fields/topics |
| Abstract | Paper abstract |

### Configuration Options

- **total_results**: Maximum number of papers to retrieve (default: 1000)
- **years_back**: Number of years from current date to include (default: 5)
- **query**: Search keywords or phrases

## API Information

This tool uses the [Semantic Scholar Academic Graph API](https://api.semanticscholar.org/):
- **Endpoint**: `https://api.semanticscholar.org/graph/v1/paper/search`
- **Rate Limits**: Automatically handled with exponential backoff
- **Data Source**: Open academic publications database

## Project Structure

```
jurnal_scraper/
├── scraper.py          # Main scraping application
├── output/             # Generated CSV files
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # Documentation
```

## Error Handling

The application includes comprehensive error handling for:
- Network connectivity issues
- API rate limiting (HTTP 429)
- Invalid API responses
- Data parsing errors
- File system operations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Semantic Scholar](https://www.semanticscholar.org/) for providing the academic search API
- Built for academic research and data collection purposes

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/fikreynurz/AutomationTesting-A11) or contact the maintainer.