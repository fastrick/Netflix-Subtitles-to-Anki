# Netflix Subtitle to Anki Flashcard Converter

This repository contains a script that allows you to convert Netflix subtitles into Anki flashcards. With this tool, you can easily create flashcards from Netflix subtitles to aid in your language learning or revision.

## Getting Started

To use this script, follow the steps below:

### Step 1: Download the Subtitles from Netflix

- Create a folder inside the `/Subtitles` directory with the name of the movie or series you want to convert.
- Inside this new folder, create a folder for each season of the series (e.g., `S01`, `S02`) if applicable.
- Place all the subtitle files inside the respective season folder. Make sure to follow this naming convention for the subtitle files: `E01-pt.xml`, `E01-en.xml`. The folder structure should be as follows:

  ```
  /Subtitles
  ├── Movie or Series Name
  │   ├── S01
  │   │   ├── E01-pt.xml
  │   │   ├── E01-en.xml
  │   │   ├── E02-pt.xml
  │   │   └── E02-en.xml
  │   ├── S02
  │   │   ├── E01-pt.xml
  │   │   ├── E01-en.xml
  │   │   ├── E02-pt.xml
  │   │   └── E02-en.xml
  │   └── ...
  └── ...
  ```
### Step 2: Install the dependencies
- Execute the following command: 
  ```bash
  pip install -r requirements.txt
  ```
### Step 3: Running the Script

- Execute the script `main.py` by running the following command in your terminal:

  ```bash
  python main.py
  ```

  Make sure you have Python installed on your machine.

- The script will process the subtitle files and generate Anki flashcards based on the text and timing of the subtitles.

### Step 4: Importing Flashcards to Anki

- Once the script has finished processing, it will create an output file named `flashcards.txt`.
- Open Anki, create a new deck, and go to "File" -> "Import" to import the flashcards.
- Select the `flashcards.txt` file and follow the prompts to import the flashcards into Anki.

## How It Works

The script extracts the text and timing information from the subtitle files. It then matches each subtitle with the closest timing and generates Anki flashcards based on the subtitle text.

Feel free to customize the script or contribute to this repository to enhance its functionality.

## Requirements

- Python 3.x
- Anki (download and install from [ankiweb.net](https://ankiweb.net/))

## Limitations

- This script currently supports Netflix subtitles in the XML format.
- The timing accuracy of the generated flashcards depends on the accuracy of the subtitle timings.
- Non-standard subtitle formats may not be compatible with this script.

## License

This project is licensed under the [MIT License](LICENSE.md). Feel free to modify and distribute it as per the terms of the license.

## Acknowledgments

Special thanks to contributors and open-source projects that inspired and helped improve this script.

Please feel free to provide feedback, suggestions, or report any issues you encounter while using this script.