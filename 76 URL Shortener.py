# 50 – Soma dos pares
# Import Shortener class from pyshorteners library
from pyshorteners import Shortener

# Create Shortener instance
s = Shortener()

# Get URL from user input
url = input("Enter a URL to shorten: ")

# Shorten URL using TinyURL service
short_url = s.tinyurl.short(url)

# Print shortened URL
print(f"Shortened URL: {short_url}")