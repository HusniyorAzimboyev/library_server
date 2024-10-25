from django.db.models import Q,Count
from django.http import HttpResponse
from django.utils.text import slugify
from .models import Book,Author,Genre
def main(request):
    html = """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced CSS Example</title>
    <style>
    :root {
    --primary-color: #000000;
    --secondary-color: #0056b3;
    --background-color: #3f648b;
    --container-bg: #ffffff;
    --text-color: #333;
    --shadow-color: rgba(0, 0, 0, 0.1);
    --hover-shadow-color: rgba(0, 123, 255, 0.2);
    --highlight-bg: #e7f1ff;
    --highlight-opacity: 0.8;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: var(--background-color);
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
    background: var(--container-bg);
    border-radius: 10px;
    box-shadow: 0 4px 20px var(--shadow-color);
}

h1 {
    font-size: 28px;
    color: var(--text-color);
    margin-bottom: 15px;
    text-align: center;
    position: relative;
}

h1::after {
    content: '';
    display: block;
    width: 50px;
    height: 3px;
    background: var(--primary-color);
    margin: 10px auto 0;
}

.authors, .genres {
    margin-bottom: 30px;
    padding: 20px;
    border-radius: 8px;
    background: var(--highlight-bg);
    background-image: url('path/to/your/author-background.jpg'); /* Replace with your image path */
    background-size: cover;
    background-position: center;
}

ul {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    list-style: none;
    padding: 0;
}

li {
    margin: 10px;
    background: rgba(255, 255, 255, var(--highlight-opacity)); /* Slightly transparent for better visibility */
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.3s, box-shadow 0.3s;
    width: 200px; /* Fixed width for items */
    display: flex;
}

li:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 15px var(--hover-shadow-color);
}

a {
    text-decoration: none;
    color: var(--primary-color);
    padding: 20px;
    display: block;
    transition: color 0.3s;
}

a:hover {
    color: var(--secondary-color);
}

.back-link {
    display: block;
    margin: 20px auto;
    text-align: center;
    font-weight: bold;
    color: #555;
    transition: color 0.3s;
}

.back-link:hover {
    color: var(--primary-color);
}

    </style>
</head>
<body>
    <div class='container'>
        <div class='authors'>
            <h1>Authors</h1>
            <ul>
        """
    autlist = Author.objects.all()
    for i in autlist:
        html+=f"<a href='books/author/{i}'><li>{i}</li></a>"
    html+=""" </ul>
        </div>
        <div class='genres'>
            <h1>Genres</h1>
            <ul>"""
    genrelist = Genre.objects.all()
    for i in genrelist:
        html+=f"<a href='books/genre/{i}'><li>{i}</li></a>"
    html += """</ul>
        </div>
        <a href='../' class='back-link'>Back to app >></a>
    </div>
</body>
</html>"""
    return HttpResponse(html)

def author_books(request,author:str):
    html = f"<h1>Books of {author}</h1><ul>"
    bklist = Book.objects.filter(author__slug=slugify(author))
    for i in bklist:
        html+=f"<li>{i}</li>"
    html += "</ul><br><a href='../../'>Back>></a>"
    return HttpResponse(html)
def genre_books(request,genre):
    html = f"<h1>Books of {genre}</h1><ul>"
    bklist = Book.objects.filter(genre__name=genre)
    if len(bklist)>0:
        for i in bklist:
            html += f"<li>{i}</li>"
    else:
        html+=f"<p>There is no <i>{genre}</i> book unfortunately :( </p>"
    html += "</ul><a href='../../'>Back>></a> <a href='just'>just</a>"
    return HttpResponse(html)
def just(request):
    authors = Author.objects.annotate(book_count=Count('books')).prefetch_related('books')
    html = authors
    for author in authors:
        print(f"{author.name} has written {author.book_count} books:")
        for book in author.books.all():
            print(f" - {book.name}")

    # html+= str(bookl)
    return HttpResponse(html)
