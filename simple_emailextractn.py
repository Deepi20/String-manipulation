string = "Contact us on training_queries@analyticsvidhya.com"
pattern = "([\w.-]+)@([\w.-]+)"
match = re.search(pattern, string)
print (match)
