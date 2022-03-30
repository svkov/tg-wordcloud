import pyLDAvis.sklearn
import pyLDAvis

from src.preprocess import preprocess_text
from tgcloud import read_file
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

df = read_file('data/result_20-30.json')
# df = df[df.date > '2021-01-01']
df['preprocessed_text'] = df['text'].apply(preprocess_text)
tf_vectorizer = CountVectorizer()
X = tf_vectorizer.fit_transform(df.preprocessed_text)
lda = LatentDirichletAllocation(n_components=3)
lda.fit(X)

p = pyLDAvis.sklearn.prepare(lda, X, tf_vectorizer)
pyLDAvis.save_html(p, 'lda_20-30.html')
