import re
from string import punctuation
from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")


def remove_punctuation(text):
    return text.translate(str.maketrans('', '', punctuation))


def preprocess_text(text):
    if text is None:
        return ''
    if isinstance(text, list):
        res_text = ''
        for elem in text:
            if isinstance(elem, str):
                res_text += elem
            else:
                res_text += elem['text']
        text = res_text
    russian_stopwords = stopwords.words("russian")
    russian_stopwords += ['это', 'да', 'просто', 'ну', 'ага']
    text = re.sub(r"\[(.*?)\]", "", text)

    tokens = remove_punctuation(text.lower()).split()
    tokens = [token for token in tokens if token.strip()
              not in russian_stopwords]
    text = " ".join(tokens)
    return text


def get_text_from_df(df):
    all_text_messages = df.text.astype(str).tolist()
    return ' '.join(all_text_messages)
