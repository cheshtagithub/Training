# Introduction to HTML

## What is HTML?
HTML stands for HyperText Markup Language.  
It is the standard language used to create webpages.HTML tells the browser what each part is.

**Important points:**  
🔹 HTML is not a programming language.  
🔹 It is a markup language.  
🔹 It tells the browser how content should be structured.

**HTML defines things like:**  
🔹 Headings  
🔹 Paragraphs  
🔹 Images  
🔹 Links  
🔹 Forms  
🔹 Tables  
🔹 Layout structure  

### What is HyperText?
HyperText = Text that links to other text/pages.  
**Example:**  
You click a link and go to another webpage.  
That clickable connection is HyperText.

### What is Markup?
Markup means using tags to describe content.

**Example:**
```bash
<p>This is a paragraph</p>
```
Here:  
<p> tells the browser
"This content is a paragraph."

### HTML File Structure
Every HTML page follows a basic structure.  
Here is the simplest HTML page.
```bash
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Introduction</title>
</head>

<body>

<h1>HTML Learning</h1>
<h2>What is HTML</h2>
<p>HTML is used to build webpages.</p>

</body>

</html>
```

### <!DOCTYPE html>
This tells the browser:
```bash
This document is written using HTML5.
```
Why this is important:  
Browsers support many old versions of HTML.
Without this declaration, the browser may switch to compatibility mode, which can break layouts.

**So rule:**  
Every HTML file must start with <!DOCTYPE html>

### <html> Tag
```bash
<html lang="en">
```
This tag wraps the entire webpage.  
Everything must be inside it.
```bash
<html>
   entire webpage
</html>
```
The lang attribute
```bash
lang="en"
```
This tells the browser and search engines:  
The page language is English.

Why this matters:  
🔹 accessibility tools (screen readers)  
🔹 SEO  
🔹 translation tools

### <head> Section
This section contains information about the page, not the visible content.

Things usually inside <head>:  
🔹 page title  
🔹 meta information  
🔹 CSS files  
🔹 JavaScript files  
🔹 favicon  
Users do not see this directly.

### meta Tag
Inside <head> you often see:
```bash
<meta charset="UTF-8">
```
**What is a meta tag?**
A meta tag provides metadata about the webpage.  
Metadata = data about data.

It gives information to:  
🔹 browsers  
🔹 search engines  
🔹 other systems  
Meta tags do not display anything on the page.

### charset="UTF-8"
```bash
<meta charset="UTF-8">
```
This defines the character encoding.

**What does that mean?**  
It tells the browser how to interpret characters. UTF-8 supports almost all characters in the world.

### Viewport Meta Tag
```bash
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
This is important for mobile devices.

It tells the browser:
```bash
Display the page according to the device width.
```
Without this, websites appear zoomed out on phones.

### <title> Tag
```bash
<title>My First Page</title>
```
This sets the browser tab title.
Rules:  
🔹 Must be inside <head>  
🔹 Should describe the page

### <body> Tag
This contains all visible webpage content.  
Examples of things inside body:  
🔹 headings  
🔹 paragraphs  
🔹 images  
🔹 buttons  
🔹 forms  
🔹 tables  
🔹 videos  
Everything the user sees goes here.

### Headings (h1 to h6)
HTML provides 6 levels of headings.
```bash
Tag |     Size       | Importance
----+----------------+-------------
h1	|   Largest      |  Most important
h2  |Slightly smaller|	
h3  |   Medium	     |
h4  |   Smaller	     | 
h5  |  Very small	 |
h6  |  Smallest      | Least important
```
**Rules About Headings**
🔹 A page should normally have only one <h1>. Because it represents the main topic of the page.  
🔹 Headings must follow hierarchy order.  
🔹 Headings are for structure, not just styling. Do NOT use them only to make text bigger.  

### Line Break — <br>
**What it does**  
<br> moves the content to the next line. It does not create a new paragraph, it only breaks the line.

**Important rule:**  
br is an empty tag, so it does not have a closing tag.

### Horizontal Line — <hr>
**What it does**  
<hr> creates a horizontal divider line. It is used to separate sections of content. hr is also an empty tag (no closing tag).

### Bold Text — <b>
**What it does**  
Makes text bold.

### Strong Text — <strong>
This tag also makes text bold, but it has meaning.  
It indicates important text.

#### Difference Between b and strong
```bash
Tag   |  Purpose
------+------------
b     | Visual bold
strong| Important meaning
```
Search engines and screen readers treat strong text as important.

### Italic Text — <i>
Makes text italic.

### Emphasized Text — <em>
Also italic, but indicates emphasis.

#### Difference Between i and em
```bash
Tag | Purpose
----+---------------------
i   | visual style
em  | emphasized meaning
```
In modern HTML, em is usually preferred.

### Underline — <u>
Underlines text.

### Small Text — <small>
Displays smaller text.  
Used for:  
🔹 copyright  
🔹 disclaimers  
🔹 footnotes

### Highlighted Text — <mark>
Highlights text with a yellow background.


