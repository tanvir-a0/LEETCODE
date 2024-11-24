class Codec:
    def __init__(self):
        self.dic_links = {}
        self.dic_links[0] = ""

    def encode(self, longUrl: str) -> str:
        keys = self.dic_links.keys()
        new_code = max(keys) + 1
        self.dic_links[new_code] = longUrl
        return "http://tinyurl.com/" + hex(new_code)[2:]

    def decode(self, shortUrl: str) -> str:
        hex_code = shortUrl.split("http://tinyurl.com/")[-1]
        return self.dic_links[int(hex_code, 16)]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
