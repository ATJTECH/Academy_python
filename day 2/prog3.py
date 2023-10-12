import re
import text

pattern=re.compile("\d{10}")
print(pattern.findall(text.text1))