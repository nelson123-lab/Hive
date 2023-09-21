from collections import defaultdict
import pandas as pd
import os
from PIL import Image
import re
import unicodedata

def basic_clean(string):
    '''
    This function takes in a string and
    returns the string normalized.
    '''
    string = unicodedata.normalize('NFKD', string)\
             .encode('ascii', 'ignore')\
             .decode('utf-8', 'ignore')
    string = re.sub(r'[^\w\s]', '', string).lower()
    return string

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)

    def add_product(self, product_id, description):
        tokens = self._tokenize(description)
        for token in tokens:
            self.index[token].add(product_id)

    def search_products(self, query):
        tokens = self._tokenize(query)
        result = None
        for token in tokens:
            if result is None:
                result = self.index.get(token, set())
            else:
                result = result.intersection(self.index.get(token, set()))
        return result

    def _tokenize(self, text):
        # Implement your tokenization logic here
        # This can include removing stop words, stemming, etc.
        text = basic_clean(text)
        return text.lower().split()


def open_image_based_on_number(image_files, number):
    for file in image_files:
        file_name = os.path.splitext(file)[0]
        if file_name == str(number):
            image_path = os.path.join(folder_path, file)
            # Open the image using your preferred method or library
            image = Image.open(image_path)
            image.show()

# Example usage
index = InvertedIndex()
items_data = pd.read_csv('data/items/info.txt')

for idx, row in items_data.iterrows():
    index.add_product(int(row['index']), row['items'])

# Search for products 
results = index.search_products(input())

"""
Since we have images of different formats, we won't be able to return images based on the index number since it won't 
load the images when the format is different.
Either we need to convert all the images to a single format while uploading them to the database.
If we are keeping the index the name of the image with the format instead of just the index number.
"""
# Example usage
folder_path = "data/items"
items = os.listdir(folder_path)
flt_items = [item for item in items if not item.endswith('.txt')]

if not results:
    print("No results found")
elif len(results) == 1:
    open_image_based_on_number(flt_items, results[0])
else:
    for i in results:
        open_image_based_on_number(flt_items, i)