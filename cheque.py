from html import *

par = Paragraph()
doc_body = Body(body_text="Some body", subelement=par)
doc = HTML(subelement=doc_body)
print(doc)
