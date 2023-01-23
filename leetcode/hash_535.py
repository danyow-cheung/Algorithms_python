import random

class Codec:
    def __init__(self):
        self.hash  ={}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        # print(longUrl)
        val = -1 
        while True:
            val = random.randint(0,10000)
            if val not in self.hash:
                self.hash[val]=longUrl 
                break
        return str(val)



    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        # print("decode to shorturl ")
        return self.hash[int(shortUrl)]

# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
tiny_url = codec.encode(url)
long_url = codec.decode(tiny_url)