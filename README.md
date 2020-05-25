Run pdf2txt.py to extract text from pdf.
```
pdf2txt.py -o new_test2.txt -p 20 East_Bay_Native_Plants_2014_15.pdf
```

Run split.py to extract text and create plant species sub directories.
```
python3 split.py -i new_test.txt --output-dir test_texts_img/
```

Run get_images.py to copy plant images into plant species sub directories.
Images were extracted from pdf via Adobe Acrobat Pro.
```
python3 get_images.py --output-dir plant_species_text_img/ -i images/
```



