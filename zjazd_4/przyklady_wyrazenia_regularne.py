import re

pattern = re.compile("\d{3}-\d{2,3}-\d{3}")
text = "122-222-222-123-123-123 231-232-234 123-123-123"
print(pattern.findall(text))
