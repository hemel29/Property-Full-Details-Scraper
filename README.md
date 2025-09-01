# Full Details Scraper Actor

This is a separate Apify actor dedicated to running the full details scraper functionality.

## Purpose

This actor focuses solely on running the `get_full_details.py` script to scrape detailed property information.

## Usage

1. Deploy this actor to Apify
2. Run the actor - it will automatically execute the full details scraper
3. No input configuration needed - it runs automatically

## Files

- `main.py` - Entry point that runs the full details scraper
- `Dockerfile` - Container configuration for Apify
- `requirements.txt` - Python dependencies
- `get_full_details.py` - The actual scraper script (copied from main project)

## Deployment

1. The `get_full_details.py` file is already included in this directory
2. Deploy this entire directory to Apify as a separate actor
3. Run when you need to scrape full property details

## Note

This actor is separate from the main property listing management system to keep the functionality focused and modular.
