import json
import pandas as pd
import click

from src.draw import draw_text
from src.preprocess import get_text_from_df, preprocess_text


def read_file(path: str) -> pd.DataFrame:
    """Read messages from json in Telegram format

    Args:
        path (str): path to result.json

    Returns:
        pd.DataFrame: DataFrame with columns such as 'text', 'from', 'id', ...
    """
    with open(path, 'rb') as file:
        raw_data = file.read()
        message_history = json.loads(raw_data)
    messages = message_history['messages']
    return pd.DataFrame(messages)


def draw_text_from_df(df: pd.DataFrame, path_save: str = None) -> None:
    """Draw word cloud using df from arguments

    Args:
        df (pd.DataFrame): df with text column
        path_save (str, optional): path where image will be saved.
        If None, just show in GUI. Defaults to None.
    """
    draw_text(preprocess_text(get_text_from_df(df)), path_save=path_save)


@click.command()
@click.option('--output', default=None)
@click.option('--path', default='data/result.json')
@click.option('--from_date', default=None)
@click.option('--name_from', default=None)
def main(path: str, output: str, from_date: str, name_from: str):
    df = read_file(path)
    df['date'] = pd.to_datetime(df.date)
    if from_date is not None:
        actual_messages_df = df[df.date > from_date]
    else:
        actual_messages_df = df

    if name_from is not None:
        filtered_messages_df = actual_messages_df[
            actual_messages_df['from'] == name_from
        ]
    else:
        filtered_messages_df = actual_messages_df

    if filtered_messages_df.empty:
        raise ValueError(f"Нет сообщений с {from_date} от {name_from}")

    draw_text_from_df(filtered_messages_df, output)


if __name__ == '__main__':
    main()  # noqa
