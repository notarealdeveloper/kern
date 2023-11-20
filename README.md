# drivers

Unix input drivers for Software 2.0

## image

```python
from drivers import image

image.to_text('files/cats.jpg')
'a cat laying on a blanket next to a cat laying on a bed'
```

```bash
cat files/cats.jpg | image
a cat laying on a blanket next to a cat laying on a bed
```

## image and text

```python
from drivers import image

image.and_text_to_text('files/cats.jpg', "How many cats?")
'2'

image.and_text_to_text('files/cats.jpg', "How many dogs?")
'0'

image.and_text_to_text('files/cats.jpg', "What animal is this?")
'cat'

image.and_text_to_text('files/cats.jpg', "What animals are these?")
'cats'
```

```bash
cat files/cats.jpg | image "How many cats?"
2

cat files/cats.jpg | image "How many dogs?"
0

cat files/cats.jpg | image "What animal is this?"
cat

cat files/cats.jpg | image "What animals are these?"
cats
```

## pdf

```python
from drivers import pdf
file = "files/chicken.pdf"
text = pdf.to_text(file)
text.count('chicken')
1267
```

```bash
cat files/chicken.pdf | pdf | head -1
Chicken Chicken Chicken: Chicken Chicken
```

## html

```python
from drivers import html
page = "<html><h1><b>Hello,</b></h1><h2><i> world</i></h2></html>"
html.to_text(page)
Hello, world
```

```bash
echo "<html><h1><b>Hello,</b></h1><h2><i> world</i></h2></html>" | html
Hello, world
```
