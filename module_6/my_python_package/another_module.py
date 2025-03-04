# Install Requests library with pip globally to import it into any Python projects, or into a project-specific virtual
# environment
# import requests

# Relative imports can be used inside a pacakge
from .import_me import a_function


a_function()

print("I'm another module in the package")

# amazon = requests.get("https://amazon.com")
# print(amazon.text)
