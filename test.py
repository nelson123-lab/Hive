from PIL import Image
import pandas as pd
data = pd.read_csv('data/items/info.txt', index_col='index')
print(data)
image = Image.open('data/items/1.jpg')
image.show()


