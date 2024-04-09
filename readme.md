## SAS GPT

This repository is a proof of concept for a GPT-4-based RAG pipeline for natural languages queries of the SAS Intelligent Decisioning documentation.

The goal of this project was to show how you could automate the retrieval, storage, and creation of embeddings from documents on the web for use within a LLM.

This documentation includes:
* User Guide
* Admin Guide
* Command Line Interfaces
* Using Data Grids in ID
* Decision Management REST API Examples

## How to use
Each step of the RAG process has been broken up into different Jupyter notebook "modules." They're rouhgly as follows:

1. **crawlpdf**: Crawl target site for PDFs (or other data)
2. **pdf2text**: Extract text of the PDFs into .txt files
3. **text2df**: Create a Dataframe from text files
4. **df2token**: Tokenize the text and split into chunks
5. **token2emb**: Create embeddings for each of the chunks
6. **emb2chat**: Interface for querying the stored chunks

### Contact

https://twitter.com/StephenG729
