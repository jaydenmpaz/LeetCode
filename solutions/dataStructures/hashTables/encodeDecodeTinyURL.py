import hashlib

class Codec:

    def __init__(self):
        self.urls = {}

    def hashHelper(self, url):
        return 'https://tin.e/' + hashlib.md5(url.encode()).hexdigest()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_key = self.hashHelper(longUrl)
        self.urls[hash_key] = longUrl
        return hash_key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))