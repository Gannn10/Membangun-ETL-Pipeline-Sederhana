import pytest
import pandas as pd
from utils.transform import transform_data

def test_transform_price_idr():
    # Test apakah $10 jadi 160.000
    data = [{'title': 'Baju', 'price': '$10', 'rating': '4/5', 'colors': '1', 'size': 'L', 'gender': 'Men'}]
    df = transform_data(data)
    assert df.iloc[0]['price'] == 160000

def test_transform_rating_float():
    data = [{'title': 'Baju', 'price': '$10', 'rating': '4.5 / 5', 'colors': '1', 'size': 'L', 'gender': 'Men'}]
    df = transform_data(data)
    assert isinstance(df.iloc[0]['rating'], float)
    assert df.iloc[0]['rating'] == 4.5