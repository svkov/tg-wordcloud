from typing import Optional
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def draw_text(text: str, path_save: Optional[str] = None, **kwargs) -> None:
    image = WordCloud().generate(text)
    plt.figure(figsize=(20, 20), **kwargs)
    plt.axis('off')
    plt.imshow(image)
    if path_save is None:
        plt.show()
    else:
        plt.savefig(path_save)
