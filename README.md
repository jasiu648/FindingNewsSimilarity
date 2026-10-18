# FindingNewsSimilarity

A multilingual NLP project for detecting similarity between news articles using multiple complementary methods: lexical similarity, semantic embeddings, and named-entity recognition.

This project was developed as a research and prototype system for comparing articles across languages and identifying how similar two texts are based on both surface-level overlap and deeper contextual meaning.

## Project overview

News articles often describe the same event in different wording, across different languages, or from different perspectives. This project explores how to automatically measure that similarity using modern NLP techniques.

The system combines:
- TF-IDF similarity for lexical overlap
- SentenceTransformer embeddings for semantic similarity
- spaCy-based named entity comparison
- optional clustering for grouping related articles

## Why this project matters

This project demonstrates how NLP can be applied to real-world text analysis tasks such as:
- duplicate or near-duplicate news detection
- multilingual article comparison
- semantic similarity measurement
- text clustering and grouping
- document analysis workflows for research and business use cases

## Technologies used

- Python
- spaCy
- SentenceTransformers
- scikit-learn
- pandas
- openpyxl
- Tkinter
- BeautifulSoup
- PyPDF2
- NLTK
- matplotlib / wordcloud utilities

## Supported languages

- Polish
- English
- Slovenian
- Croatian

## Key features

- Compare two articles side by side
- Choose the language model for processing
- Apply preprocessing and lemmatization
- Measure lexical similarity using TF-IDF
- Measure semantic similarity using sentence embeddings
- Compare named entities extracted from both texts
- Export results to Excel files
- Run clustering on article collections
- Import text and PDF files from local storage
- Fetch article content from URLs

## Repository structure

- `pipelines.py` — main similarity workflow orchestration
- `gui.py` — desktop graphical interface for article comparison
- `models/` — embedding and NER model wrappers
- `textpreprocessing/` — text cleaning and language-specific preprocessing
- `clustering/` — clustering logic for article grouping
- `data_access/` — URL and PDF article extraction utilities
- `visualization/` — visual analysis helpers
- `stopwords/` — multilingual stopword lists
- `requirements.txt` — project dependencies
- `*.ipynb` — notebooks used for experimentation and reports

## Installation

```bash
git clone https://github.com/jasiu648/FindingNewsSimilarity.git
cd FindingNewsSimilarity
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

## Required language models

This project uses spaCy language models. If needed, install them with:

```bash
python -m spacy download en_core_web_trf
python -m spacy download pl_core_news_lg
python -m spacy download sl_core_news_trf
python -m spacy download hr_core_news_lg
```

## Running the application

```bash
python gui.py
```

The app provides a graphical interface where you can:
- paste or import article text
- choose a language
- adjust preprocessing parameters
- compare articles
- view similarity results

## Example usage

```python
from pipelines import PipelineFactory

pipeline = PipelineFactory.CreatePipeline('EN')
corpus = [["A major policy announcement was made today.", "The government released a significant policy update today."]]
results = pipeline.ProcessPipeline(corpus, 2, 4, True)

for result in results:
    print(result.embedding_result)
    print(result.tfidf_result)
    print(result.ner_result)
```

## Output

The project can generate Excel reports with columns such as:
- article 1
- article 2
- lexical similarity
- semantic similarity
- extracted entities
- named-entity similarity

## Portfolio value

This project highlights practical skills in:
- natural language processing
- multilingual text analysis
- machine learning for text similarity
- experimental research and prototyping
- building an end-to-end NLP workflow

## Notes

This project is a research-oriented prototype and is best viewed as a demonstration of applied NLP and data science skills. It shows a strong foundation in text processing, model integration, and practical experimentation.

## Future improvements

- refactor code into a cleaner package structure
- add unit tests and CI checks
- remove unnecessary dependencies
- improve configuration and environment management
- add a web dashboard or API layer
- document model performance and evaluation metrics

## License

This project does not currently include a formal LICENSE file.

## Author

Jakub Jasiński

---

This project is suitable for a portfolio as an example of multilingual NLP, semantic search, and article similarity analysis.
