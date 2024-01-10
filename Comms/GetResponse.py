

import sqlite3
import polars as pl
from gensim import corpora, models


def search_database_lda(db_path: str, table_name: str, search_text: str, num_topics: int = 10) -> pl.DataFrame:
    """
    Search a database table with two columns of prompts and responses using LDA and return a Polars DataFrame with
    the most relevant responses.

    Args:
        db_path (str): Path to the database file.
        table_name (str): Name of the table in the database.
        search_text (str): Text to search for.
        num_topics (int, optional): Number of topics to use for LDA. Defaults to 10.

    Returns:
        pl.DataFrame: Polars DataFrame with the most relevant responses.
    """

    # connect to the database
    conn = sqlite3.connect(db_path)

    # define your search query
    query = f'''
        SELECT prompt, response FROM {table_name}
    '''

    # execute the query and retrieve the results
    results = conn.execute(query)

    # create a list of documents to use for LDA
    documents = [row[0] + ' ' + row[1] for row in results]

    # create a dictionary and corpus for LDA
    dictionary = corpora.Dictionary([document.split() for document in documents])
    corpus = [dictionary.doc2bow(document.split()) for document in documents]

    # train the LDA model
    lda_model = models.ldamodel.LdaModel(corpus=corpus, num_topics=num_topics, id2word=dictionary, passes=10)

    # get the most relevant topics for user input
    user_input_bow = dictionary.doc2bow(search_text.split())
    topics = lda_model.get_document_topics(user_input_bow)

    # create a Polars DataFrame with the most relevant responses
    data = []
    for topic in topics:
        for document in lda_model.get_topic_terms(topic[0]):
            data.append({
                'topic': topic[0],
                'score': topic[1],
                'response': dictionary[document[0]]
            })

    return pl.DataFrame(data)

