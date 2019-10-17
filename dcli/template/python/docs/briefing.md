# Spam Detector

Data Mining consists of extracting knowledge from large amounts of data by setting up automatic or semi-automatic methods.
In order to achieve this, you can use few algorithms derived from various scientific disciplines such as statistics, artificial intelligence or computer science. The purpose is to build a model from the data according to some criterias and to extract a maximum of knowledge.

In this mission you'll set up an algorithm that you'll ***train*** to detect spam messages.

The libraries you need to use are:

* Scipy library with the following class [ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
* [Numpy library](http://www.numpy.org/)
* TF-IDF algorithm, you have to use the attribute _stop_words_  and _min_df_ that you'll set respectively to "english" and 0.0005. (these attributes allow the algorithm to ignore the most common words / with the least semantic meaning like me, you, the...)

Here is the documentation of the algorithm TF-IDF : <https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html>

Here is an example of how the TF-IDF algorithm works:
We'll take as example these 3 sentences.
   1st sentence  :  Hello, I love cats  
   2nd sentence  :  Hello, I love dogs  
   3rd sentence  :  This sentence contains this text  
***TF*** : Term Frequencies stands for the frequence that a word is present in a document.
   $$ TF(word,sentence) = {|word \in sentence| \over |sentence|}.$$
***IDF*** : Inverse Document Frequencies
$$ IDF(word) = ln({N \over |word \in sen|}).$$
N is the number of sentences (here 3) and word in sen is the number of times the word appears in different sentences (here hello appears in two sentences)

Encoding (the 1/4, 1/5 represents the IF encoding):  
 |   | I  | love  | cats  | dogs  | document  | hello  | this | text  | contains  |
 |---|---|---|---|---|---|---|---|---|---|
 | 1st sentence  | 1/4   |  1/4  |  1/4  |  0 | 0  | 1/4   | 0  | 0  | 0  |
 | 2nd sentence  | 1/4   | 1/4   | 0  | 1/4   |  0 |  1/4  |  0 |  0 |  0 |
 | 3rd sentence  |  0 | 0  | 0  | 0  | 1/5  | 0  | 2/5  | 1/5  | 1/5  |
 |    IDF       | 0.4 | 0.4 | 1.09 | 1.09 | 1.09 | 0.4 | 1.09 |1.09 | 1.09 |

Final ***TF-IDF*** :
$$ TF-IDF(word,sentence) = TF(word,sentence) \times IDF(word) .$$
|   | I  | love | cats  | dogs  | document  | hello  | this | text  | contains  |
 |---|---|---|---|---|---|---|---|---|---|
 | 1st sentence  | 0.1 | 0.1 |  0.273  |  0 | 0  | 0.1   | 0  | 0  | 0  |
 | 2nd sentence  | 0.1 | 0.1 | 0  | 0.273   |  0 |  0.1  |  0 |  0 |  0 |
 | 3rd sentence  |  0  |  0  | 0  | 0  | 0.218  | 0  | 0.44  | 0.218  | 0.218  |

You obtain a _term-document matrix_ where each (i , j) represents the frequency of the term i in the sentence j.

**Back to business**:

In this exercise you have to classify the words in order of "discriminative power" through statistical tests.
We provide you a _spam.dms_ file that you'll use, it contains spam messages and normal messages. Each line of the file is written like _spam/text text_message_.

    spam	+123 Congratulations - in this week's competition draw u have won the $1450 prize to claim just call 09050002311 b4280703
    text     Is that seriously how you spell his name?  

What you have to do:

1 - Extract the data from _spam.dms_ and return a matrix that contains the messages in TF-IDF format and a vector (1 if spam and 0 if not)

_In the TF-IDF documentation there are methods that can help you extracting a term-document matrix, you have to choose the right one to use_
_To convert the list(O and 1) into a vector, you can use the Numpy library._

``` python
    def transform_text(pairs):
        return (matrix, vector)

```

   ***pairs*** is a list of tuples (message, type) (type can be spam or text)

2 - Code a method that for each word returns his p-value related to the test.
    A p-value is the probability that the word is NOT over-represented in the spams. The smaller the p-value is,
    the more over-represented the word is within spams compared to non-spam(text).

_To convert the term-document matrix to a matrix you use another method from Scipy library that returns a dense matrix
representation of this matrix (the term-document matrix is sparse it doesn't contain zeros), you need a dense matrix for the next function._

   ``` python
        def word_pvalue(matrix, vector, word_pos):
            return pvalue
  ```

  ***word_pos*** represents an int in the matrix.