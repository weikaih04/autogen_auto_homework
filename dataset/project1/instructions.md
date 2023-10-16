# Project 1: Corpus Analysis

**Objectives:** To perform basic analysis on a corpus of text documents.

**What to turn in:** A jupyter notebook containing all your code and results.

Please name the file `<uwnetid>-project1.ipynb`, replacing `<uwnetid>` with your UW net ID. Turn the file in via Canvas.

To create a jupyter notebook, navigate to your project directory and issue the following command:

```bash
jupyter notebook
```

All commands in the notebook should be able to run assuming the data files are located under the relative path `data/`. Create a new cell for each problem, and comment well! At least 1-2 points for each question will be awarded for coding style.

**Due date:** Thursday, October 12, 2023 EOD

**Total points:** 100

## Exploring the content of a text corpus

A data file has been provided to you under `project1/data/yelp.json`. This is a file containing a [JSON object](https://www.w3schools.com/js/js_json_objects.asp).

Some demo code has been provided to you in `demo.ipynb` to load the data file and examine its contents.

Load the dataset and write code to answer the following:

1. (5 pt) This dataset contains Yelp reviews of restaurants. How many reviews does it contain?

2. (5 pt) How many unique users have written the reviews in this dataset?

In the demo code, I have also provided some examples of how to tokenize text into sentences and words. Please use these functions to answer the following:

3. (10 pt) What is the average length of each review in terms of **words**? How long is the shortest review and how long is the longest? What is the content of the shortest review?

4. (10 pt) What is the average length of each review in terms of **sentences**? How long is the shortest review and how long is the longest? Is the longest review by sentences the same as the longest review by words?

5. (10 pt) What are the 10 most common word tokens in the reviews? What are the 10 least common word tokens in the reviews? (Do not do any additional processing of tokenization outputs to answer this question.) Discuss some potential problems with counting word tokens without further processing.

## Preprocessing to remove spurious tokens

6. (20 pt) Clean up the word tokens by lower casing, removing punctuation, removing stop words, and stemming. Use the NLTK Porter stemmer. Now, aggregate the remaining counts. what are the 10 most common and least common tokens in these reviews? Comment on any differences between these lists and the outputs of problem 5.

## Computing *n*-gram statistics

Now, instead of tokens (unigrams), you will compute *n*-gram statistics. You can use the [NLTK ngrams function](https://www.nltk.org/api/nltk.util.html#nltk.util.ngrams).

7. (20 pt) Compute unigram, bigram, and trigram frequencies for these reviews. What are the most prevalent unigrams, bigrams, and trigrams? (You do not need to remove stop words or perform stemming, though you should still use lower case and remove punctuation.) Examine the most prevalent *n*-grams in this dataset; would you consider any of them to be stop words in this setting?

Bonus (5 pt): what if you remove stop words before computing *n*-grams? How does this change the most prevalent *n*-grams? Are they more meaningful?

## Retrieving similar reviews

Keep all unigrams, bigrams, and trigrams whose frequency in the dataset is >10. This will be your vocabulary.

8. (20 pt) Use the scikit-learn TfidfVectorizer to compute the tf-idf vectors associated with each *n*-gram in your vocabulary for each review. A separate file called `query.txt` is provided in the `data/` folder. This file contains a single review. Use tf-idf and cosine similarity to identify the top-3 most similar reviews in the dataset to the review in the query file. Print the text of these reviews. Comment on the strengths and weaknesses of this "retrieval" method.
