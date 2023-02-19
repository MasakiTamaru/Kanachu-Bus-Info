import aspose.words as aw

# load text file
doc = aw.Document("result.txt")

# save text as HTML
doc.save("index_before.html")