from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)

    def add_product(self, product_id, description):
        tokens = self._tokenize(description)
        for token in tokens:
            self.index[token].add(product_id)
        print(tokens)

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
        return text.lower().split()

# Example usage
index = InvertedIndex()

# Add products to the index
index.add_product(1, "Apple iPhone 12 Pro")
index.add_product(2, "Samsung Galaxy S21 Ultra")
index.add_product(3, "Apple MacBook Pro")
index.add_product(4, "Realme 5 Pro")

# Search for products
results = index.search_products("Apple iPhone")
print(results)  # Output: {1}

results = index.search_products("Pro")
print(results)  # Output: {1, 3}
