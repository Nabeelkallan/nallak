import os
import re
from collections import Counter

def print_banner():
    os.system('toilet -f big --gay dorNKs')

def check_file_size(file_path):
    file_size = os.path.getsize(file_path)
    if file_size > 10 * 1024 * 1024:  # 10MB
        print(f"Warning: The file {file_path} is larger than 10MB. This may slow down processing.")

def is_valid_domain(domain):
    pattern = r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, domain)

def main():
    print_banner()  # Print the banner when the program starts

    # Default file paths and search engine
    companies_file = 'companies.txt'
    dorks_file = 'dorks.txt'
    output_file = 'result.txt'
    html_file = 'dorks.html'
    search_engine = 'google'

    try:
        # Check file sizes
        check_file_size(companies_file)
        check_file_size(dorks_file)

        # Check if company and dork files exist
        if not os.path.isfile(companies_file):
            print(f"Input file not found: {companies_file}. Please provide a valid file.")
            return
        if not os.path.isfile(dorks_file):
            print(f"Input file not found: {dorks_file}. Please provide a valid file.")
            return

        # Read company names
        with open(companies_file, 'r') as companies_file_handle:
            companies = [company.strip() for company in companies_file_handle.readlines() if is_valid_domain(company.strip())]

        # Read dorks
        with open(dorks_file, 'r') as dorks_file_handle:
            dorks = [dork.strip() for dork in dorks_file_handle.readlines()]

        # Fallback to default dorks if none are provided
        default_dorks = ['inurl:"admin"', 'intitle:"login"', 'filetype:pdf']
        if not dorks:
            print("No dorks found. Using default dorks.")
            dorks = default_dorks

        compiled_dorks = []
        for company in companies:
            for dork in dorks:
                # Include the company name in the search query
                compiled_dork = f"{dork} site:{company}"
                compiled_dorks.append(compiled_dork)

        # Count duplicates across all compiled dorks
        dork_counts = Counter(compiled_dorks)
        duplicates = {dork: count for dork, count in dork_counts.items() if count > 1}

        # Output summary
        total_companies = len(companies)
        total_dorks = len(dorks)
        total_links = len(compiled_dorks)

        print(f"Compiled {total_companies} companies with {total_dorks} dorks. Total result: {total_links} links.")

        # Show duplicates only if they occur more than once
        if duplicates:
            print(f"{len(duplicates)} duplicate dorks found:")
            duplicate_summary = ', '.join([f"{dork} ({count} times)" for dork, count in duplicates.items()])
            print(duplicate_summary)

        # Write the output to result.txt
        with open(output_file, 'w') as outfile:
            for compiled_dork in compiled_dorks:
                outfile.write(compiled_dork + '\n')

        # Create HTML file
        with open(html_file, 'w') as html_file_handle:
            html_file_handle.write('<html><head><title>Dork Compilation Results</title></head><body>\n')
            for dork in compiled_dorks:
                if search_engine == 'bing':
                    search_url = 'https://www.bing.com/search?q=' + dork
                elif search_engine == 'duckduckgo':
                    search_url = 'https://duckduckgo.com/?q=' + dork
                else:
                    search_url = 'https://www.google.com/search?q=' + dork

                html_file_handle.write(f'<a href="{search_url}" target="_blank">{search_url}</a><br>\n')
            html_file_handle.write('</body></html>\n')

        print(f"Compiled dorks saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

