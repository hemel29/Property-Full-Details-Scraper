#!/usr/bin/env python3
"""
Full Details Scraper Actor
Dedicated actor for running the full details scraper
"""

import get_full_details

def main():
    print("🔍 Full Details Scraper Actor")
    print("📋 Running full details scraper...")
    
    try:
        get_full_details.main()
        print("\n✅ Full details scraper completed successfully!")
    except Exception as e:
        print(f"\n❌ Full details scraper failed: {e}")
        raise

if __name__ == "__main__":
    main()

