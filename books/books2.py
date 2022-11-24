import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df_ = pd.read_csv(r'C:\Users\Rumeysa\PycharmProjects\books\books.csv')
df = df_
df.head()

df['description'] = df['description'].fillna('')

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df['description'])
tfidf_matrix.shape

cosine_sim = cosine_similarity(tfidf_matrix,
                               tfidf_matrix)

indices = pd.Series(df.index, index=df['title'])

indices.index.value_counts()
indices = indices[~indices.index.duplicated(keep='last')]

def content_based_recommender(title, cosine_sim, dataframe):
    indices = pd.Series(dataframe.index, index=dataframe['title'])
    indices = indices[~indices.index.duplicated(keep='last')]
    book_index = indices[title]
    similarity_scores = pd.DataFrame(cosine_sim[book_index], columns=["score"])
    book_indices = similarity_scores.sort_values("score", ascending=False)[1:6].index
    return dataframe['title'].iloc[book_indices]


def content_based_recommender1():
    sonuc["text"] = content_based_recommender(okunankitap.get(), cosine_sim, df)


from tkinter.ttk import *
import tkinter as tk

pencere = tk.Tk()
pencere.geometry('550x400')
pencere.title("BOOK RECOMMENDER SYSTEM")

okunankitap = Combobox(width=80)
okunankitap["values"] = list(df['title'].values)
okunankitap.place(x=20,y=20)
okunankitap.current()

baslık = tk.Label(text="RECOMMENDED BOOKS")
baslık.place(x=200,y=120)

sonuc = tk.Label(text=" ")
sonuc.place(x=150,y=150)

book_recommender = tk.Button(text="RECOMMEND BOOK",command=content_based_recommender1).place(x=205,y=70)

pencere.mainloop()

