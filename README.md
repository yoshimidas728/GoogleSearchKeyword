## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Python 3.12.7](#python-3125)
  - [Required Python Modules](#required-python-modules)
  - [FFmpeg](#ffmpeg)
- [Usage](#usage)

## Prerequisites

- Python 3.12.7
- FFmpeg
- Chrome browser (for Selenium WebDriver)

## Installation

### Python 3.12.7

#### Windows

1. Visit the official Python downloads page: https://www.python.org/downloads/
2. Click on the "Download Python 3.12.7" button.
3. Run the installer and check "Add Python 3.12 to PATH".
4. Click "Install Now".

Verify the installation by opening Command Prompt and typing:
```
python --version
```

#### Linux (Ubuntu)

Open a terminal and run:

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.12
```

Verify the installation:
```bash
python3.12 --version
```

#### macOS

1. Visit https://www.python.org/downloads/
2. Download and run the macOS installer for Python 3.12.7.
3. Follow the installation wizard.

Alternatively, use Homebrew:

```bash
brew install python@3.12
echo 'export PATH="/usr/local/opt/python@3.12/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Verify the installation:
```bash
python3 --version
```

### Required Python Modules

1. Ensure you're in the directory containing `requirement.txt`.
2. Run the following command:

```bash
pip install -r requirement.txt
```

### FFmpeg

#### Windows


1. Visit the FFmpeg Download Page: https://ffmpeg.org/download.html
   Go to the FFmpeg official website.
   Hover over the Windows logo and click on Windows builds from gyan.dev.
2. Select the Build:
  In the Git master builds section, look for the latest version of the FFmpeg build.
  Click on the link to download the full build (e.g., ffmpeg-git-full.7z).
3. Extract the ZIP file.
4. Add the bin folder to your system's PATH.

#### Linux (Ubuntu)

```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS

Using Homebrew:

```bash
brew install ffmpeg
```

Verify FFmpeg installation:
```bash
ffmpeg -version
```

## Usage

To run the GoogleSearchKeyWord with Excel file names as parameters:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `GoogleSearchKeyWord.py`.
3. Run the script with the Excel file name as an argument:

```bash
python GoogleSearchKeyWord.py ...
```

Replace "Your Excel File.xlsx" with the actual name of your Excel file.

Note: Ensure your Excel file is in the same directory as the script, or provide the full path to the file.

## Important Notes

- The script uses Selenium WebDriver with Chrome. Make sure you have Chrome installed on your system.
- The bot may encounter CAPTCHAs during execution. It attempts to solve them automatically, but manual intervention may be required in some cases.
- The script processes the Excel file and creates a new file with the prefix "with website " added to the original filename.
- Respect website terms of service and legal considerations when using web scraping tools.

For any issues or questions, please open an issue in this repository.


