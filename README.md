# Meme generator
This is the final project for udacity's "Large Python Codebases with Libraries" course.

## Overview and Structure
This code creates "memes", i.e. merging a picture and a quote consisting of the quote itself (aka body of the quote) and it's author. Supposedly memes are a thing in social media but I wouldn't know.

### Structure of the code

The structure of the code base is 

    ├── app.py
    ├── _data
    │   ├── DogQuotes
    │   ├── photos
    │   └── SimpleLines
    ├── MemeEngine
    │   ├── __init__.py
    │   ├── MemeEngine.py
    ├── meme.py
    ├── QuoteEngine
    │   ├── CSVIngestor.py
    │   ├── DOCXIngestor.py
    │   ├── IngestorInterface.py
    │   ├── Ingestor.py
    │   ├── __init__.py
    │   ├── PDFIngestor.py
    │   ├── QuoteModel.py
    │   └── TXTIngestor.py
    ├── README.md
    ├── requirements.txt
    ├── templates
        ├── base.html
        ├── meme_form.html
        └── meme.html

The more important files/folders are:

* ´meme.py´ contains the code for the CLI interface
* ´app.py´ contains the code for the web server interface
* the folder ´MemeEngine´ contains the code for image processing and creation of the 'meme'
* the folder ´QuoteEngine´ contains the code for processing different file type to extract quotes

## Setting up the software

To install the software you need the package xpdf, for Linux the installation is done via

````bash
$ sudo apt-get install xpdf

````
For other OS you are on your own.

To configure the Python environment run

````bash
$ python3 -m venv memegen
$ source ./memegen/bin/activate
$ pip install -r requirements.txt
````


## Running the program

To use the software you can either interact via CLI oder web interface.

### CLI

To use the generator via the command line interface, run
```bash
$ python3 meme.py [-h] [--body BODY] [--author AUTHOR] [--path PATH]
```
where BODY is a quote, AUTHOR the author of the quote and PATH the path to an image, like

````bash
$ python3 meme.py --body "There is a sucker born every minute" --author "Confuzius" --path ./_data/photos/dog/xander_1.jpg
````

-h or --help as usual for online help.


### Web Interface

To use the web interface run
```bash

$ export FLASK_APP=app.py
$ flask run --host 0.0.0.0 --port 3000 --reload

```

