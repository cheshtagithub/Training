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
`<p>` tells the browser
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

#### `<!DOCTYPE html>`
This tells the browser:
```bash
This document is written using HTML5.
```
Why this is important:  
Browsers support many old versions of HTML.
Without this declaration, the browser may switch to compatibility mode, which can break layouts.

**So rule:**  
Every HTML file must start with `<!DOCTYPE html>`

#### `<html>` Tag
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

#### `<head>` Section
This section contains information about the page, not the visible content.

Things usually inside `<head>`:  
🔹 page title  
🔹 meta information  
🔹 CSS files  
🔹 JavaScript files  
🔹 favicon  
Users do not see this directly.

#### meta Tag
Inside `<head>` you often see:
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

#### charset="UTF-8"
```bash
<meta charset="UTF-8">
```
This defines the character encoding.

**What does that mean?**  
It tells the browser how to interpret characters. UTF-8 supports almost all characters in the world.

#### Viewport Meta Tag
```bash
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
This is important for mobile devices.

It tells the browser:
```bash
Display the page according to the device width.
```
Without this, websites appear zoomed out on phones.

#### `<title>` Tag
```bash
<title>My First Page</title>
```
This sets the browser tab title.
Rules:  
🔹 Must be inside `<head>` 
🔹 Should describe the page

#### `<body>` Tag
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

#### Headings (h1 to h6)
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
🔹 A page should normally have only one `<h1>`. Because it represents the main topic of the page.  
🔹 Headings must follow hierarchy order.  
🔹 Headings are for structure, not just styling. Do NOT use them only to make text bigger.  

#### Line Break — `<br>`
**What it does**  
`<br>` moves the content to the next line. It does not create a new paragraph, it only breaks the line.

**Important rule:**  
br is an empty tag, so it does not have a closing tag.

#### Horizontal Line — `<hr>`
**What it does**  
`<hr>` creates a horizontal divider line. It is used to separate sections of content. hr is also an empty tag (no closing tag).

#### Bold Text — `<b>`
**What it does**  
Makes text bold.

#### Strong Text — `<strong>`
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

#### Italic Text — `<i>`
Makes text italic.

#### Emphasized Text — `<em>`
Also italic, but indicates emphasis.

#### Difference Between i and em
```bash
Tag | Purpose
----+---------------------
i   | visual style
em  | emphasized meaning
```
In modern HTML, em is usually preferred.

#### Underline — `<u>`
Underlines text.

#### Small Text — `<small>`
Displays smaller text.  
Used for:  
🔹 copyright  
🔹 disclaimers  
🔹 footnotes

#### Highlighted Text — `<mark>`
Highlights text with a yellow background.

### Links and Images in HTML
Links and images are two of the most important elements of a webpage.

**Without them:**  
🔹 Users cannot navigate between pages  
🔹 Pages look boring without visuals

#### Anchor Tag (Links)
The anchor tag is used to create clickable links.  
**Syntax**
```bash
<a href="URL">Link Text</a>
```
**Example:**
```bash
<a href="https://www.google.com">Go to Google</a>
```
**Explanation**
```bash
Part                      |    Meaning
--------------------------+--------------------------
a                         | Anchor tag used to create a hyperlink
href                      | Hypertext reference (destination URL)
"https://www.google.com"  | Where the link will go
Go to Google              | Text user clicks
```
When user clicks → browser opens that page.

#### Opening Links in New Tab
Sometimes you want the link to open in a new browser tab.  
For this we use the target attribute.  
**Syntax**
```bash
<a href="URL" target="_blank">Link</a>
```
**Example:**
```bash
<a href="https://www.youtube.com" target="_blank">Open YouTube</a>
```
**Explanation**
```bash
Attribute       | Purpose
target="_blank" | Opens link in new tab
```
Without this, link opens in same tab.

#### Internal Links (Linking Pages in Same Website)
If your website has multiple pages, you can link them.  
**Link example:**
```bash
<a href="about.html">About Us</a>
```
This opens about.html from same folder.

#### Image Tag
Images are added using the img tag.
**Syntax**
```bash
<img src="image_path" alt="description">
```
**Important Rule**
img is a self-closing tag. It does not need a closing tag

#### Image Attributes
Images need some attributes.

#### *1.src (Source)*
Tells browser where the image is located  
**Example:**
```bash
<img src="dog.jpg">
OR
<img src="images/dog.jpg">
OR from internet
<img src="https://example.com/dog.jpg">
```

#### *2.alt(Alternative text)*
This is VERY IMPORTANT. It describes the image.  
**Example:**
```bash
<img src="cat.jpg" alt="White cat sitting on chair">
```
**Why important?**  
🔹 Accessibility (screen readers)  
🔹 SEO  
🔹 If image fails to load → alt text appears

#### *3.Width and Height*
Controls image size.  
**Example:**
```bash
<img src="cat.jpg" alt="Cute Cat" width="300">
OR
<img src="cat.jpg" alt="Cute Cat" width="300" height="200">
```

#### Combining Links and Images
You can also make images clickable.  
**Example:**
```bash
<a href="https://www.youtube.com">
<img src="youtube.png" alt="YouTube Logo" width="100">
</a>
```

### What is a List in HTML?
A list is used to display multiple related items in an organized way.

**Example in normal text:**  
Fruits  
Apple  
Banana  
Mango  
HTML lets us display this properly structured.

#### Unordered List (ul)
An unordered list shows items with bullet points.

**Example:**  
* Apple  
* Banana  
* Mango

**Syntax**
```bash
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

#### Ordered List (ol)
An ordered list shows items with numbers.

**Example:**  
1. Wake up  
2. Brush teeth  
3. Eat breakfast

**Syntax**  
```bash
<ol>
    <li>Step 1</li>
    <li>Step 2</li>
    <li>Step 3</li>
</ol>
```

#### Difference Between ul and ol
```bash
Feature          |     ul      |  ol
-----------------+-------------+-----------------
Marker           |   Bullet    | Number
Order important? |     No      |  Yes
Example          |Features list| Step-by-step instructions
```

#### Nested Lists (List inside List)
Sometimes we create sub-lists.

**Example:**
```bash
<ul>
    <li>Fruits
        <ul>
            <li>Apple</li>
            <li>Mango</li>
        </ul>
    </li>

    <li>Vegetables
        <ul>
            <li>Carrot</li>
            <li>Potato</li>
        </ul>
    </li>
</ul>
```

#### Ordered List Types
Ordered lists can use different numbering styles.

**Example:**
```bash
<ol type="A">
```
Possible types:
```bash
Type | Output
-----+----------
1    | 1,2,3
A    | A,B,C
a    | a,b,c
I    | I,II,III
i    | i,ii,iii
```

#### Starting Number in Ordered List
**Example:**
```bash
<ol start="5">
```

### What is div?
div means division of a page. It is used to group elements together.

**Example:**
```bash
<div>
    <h1>Product Name</h1>
    <p>Description</p>
</div>
```
Here the heading and paragraph belong to the same section.

**div is used for:**  
🔹 Page structure  
🔹 Styling with CSS  
🔹 Creating sections  
🔹 Organizing content

Example structure:
```bash
div (header)
div (product)
div (features)
div (footer)
```

### What is span
span is also a container, but it is used for small pieces of text inside a line.  
The span allows you to target specific words.

#### Difference Between div and span
```bash
Feature            |      div      |  span
-------------------+---------------+-----------------
Type               | Block element | Inline element 
Usage              | Large sections| Small text parts
Starts on new line |     Yes       |     No
```

### What is class
class is an attribute used to name an element. It helps us identify elements later (mainly for CSS or JavaScript).

**Example:**
```bash
<div class="header">
    <h1>My Website</h1>
</div>
```
**Why class is Important:** Later when we use CSS, we can style that section.

## Semantic HTML
Before HTML5, developers mostly used `<div>` everywhere.  
This works, but it has problems:

* Search engines cannot understand the page structure
* Screen readers (for visually impaired users) cannot understand it
* Code becomes messy

So HTML5 introduced Semantic Tags.

### What is Semantic HTML?
Semantic = Meaning  
Semantic tags tell the browser, search engines, and developers what the content means.

**Example:**  
Instead of:
```bash
<div class="header">
```
We write:
```bash
<header>
```
Now everyone understands:
➡ This is the header section of the website

#### Main Semantic Tags 
These are the tags you must know.
```bash
Tag    |  Purpose
-------+---------------------------------------
header | Top section of website
nav    | Navigation links
main   | Main content
section| A section of content
article| Independent content (blog post, news)
aside  | Sidebar content
footer | Bottom section
```

**1️⃣ `<header>`**  
Represents the top part of the page.  
Usually contains:  
🔹 Website title  
🔹  Logo  
🔹  Navigation menu  

**Example:**
```bash
<header>
    <h1>My Website</h1>
</header>
```
Explanation:

`<header>` ➡ top area
`<h1>` ➡ main heading

**2️⃣ `<nav>`  
Used for navigation links.

**Example:**
```bash
<nav>
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Contact</a>
</nav>
```
Explanation:

`<nav>` ➡ navigation menu
`<a>` ➡ links

**3️⃣ `<main>`  
Represents the main content of the page.  
Important rule:  
A page should have only one `<main>`

**Example:**
```bash
<main>
    <p>Welcome to my website.</p>
</main>
```

**4️⃣ `<section>`  
Represents a section of related content.

**Example:**
```bash
<section>
    <h2>About Us</h2>
    <p>We provide travel services.</p>
</section>
```

**5️⃣ `<article>`  
Used for independent content.

**Examples:**  
🔹 Blog post
🔹 News article
🔹 Forum post
🔹 Product card

**Example:**
```bash
<article>
    <h2>Best Places to Visit</h2>
    <p>Here are some beautiful travel destinations.</p>
</article>
```

**6️⃣ `<aside>`**  
Used for sidebar content.

**Example:**  

🔹 Ads
🔹 Related links
🔹 Tips
🔹 Author info

**Example:**
```bash
<aside>
    <h3>Travel Tips</h3>
    <p>Always carry a water bottle.</p>
</aside>
```

**7️⃣ `<footer>`  
Represents the bottom part of the website.

**Usually contains:**  
🔹 Copyright
🔹 Contact info
🔹 Social media links

**Example:**
```bash
<footer>
    <p>© 2026 My Website</p>
</footer>
```




