# dork_compiler

cd ~/dork_compiler

README.md

Dork Compiler

Dork Compiler is a Python-based tool for generating and compiling custom Google dorks for multiple companies or domains. This tool allows you to automate the generation of dorks by reading company names and custom dork templates from input files, and outputs the compiled dorks in both text and clickable HTML formats.

Features

- Generates custom Google dorks for multiple companies or domains.
- Outputs dorks into both a plain text file and an HTML file with clickable links.
- Simple, easy-to-use command-line interface.

Installation

1. Clone the repository:
   git clone https://github.com/yourusername/dork_compiler.git
2. Navigate to the project directory:
   cd dork_compiler
3. Ensure you have Python installed (works with Python 3.x).

Usage

To use the tool, you need two input files:
1. A text file containing a list of company names (one per line).
2. A text file containing your custom dorks (with placeholders for the company names, e.g., abcd.com).

Example

You can run the tool with the following command:

python dork_compiler.py --companies companies.txt --dorks dorks.txt --output result.txt --html dorks.html

- --companies: The input file containing the list of company names.
- --dorks: The input file containing the custom dorks.
- --output: The output text file (default: result.txt).
- --html: The output HTML file (default: dorks.html).

Sample companies.txt:

example1.com
example2.com
example3.com

Sample dorks.txt:

site:abcd.com intitle:"index of" "backup"
site:abcd.com filetype:sql "password"

Output

- Plain text file (result.txt) containing all compiled dorks.
- HTML file (dorks.html) containing clickable links for the dorks.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions or bugs.
EOF

git add README.md
git commit -m "Add README file"
git push origin main
