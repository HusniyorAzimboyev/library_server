from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def first(request):
    html = """
        <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>my App</title>
</head>
<body style="color:red; text-align:center;">
    <h1>First page</h1>
    <ul>
        <a href = "pages/computers"><li>Computers</li></a>
        <a href="pages/phones"><li>Phones</li></a>
        <a href="pages/tablets"><li>Tablets</li></a>
    </ul>
    <a href="../">Back>></a>
</body>
</html>
    """
    return HttpResponse(html)
def pages(request,page):
    html='<body style=\'color:#cc2645;text-align:center;\'>\n'
    if page=="computers":
        html += f"""
        <h1>{page} page</h1>
        <p>A computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation). Modern digital electronic computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. The term computer system may refer to a nominally complete computer that includes the hardware, operating system, software, and peripheral equipment needed and used for full operation; or to a group of computers that are linked and function together, such as a computer network or computer cluster.</p>
        """
    elif page=="phones":
        html += f"""
                <h1>{page} page</h1>
                <p>A telephone, colloquially referred to as a phone, is a telecommunications device that permits two or more users to conduct a conversation when they are too far apart to be easily heard directly. A telephone converts sound, typically and most efficiently the human voice, into electronic signals that are transmitted via cables and other communication channels to another telephone which reproduces the sound to the receiving user. The term is derived from Ancient Greek: τῆλε, romanized: tēle, lit. 'far' and φωνή (phōnē, voice), together meaning distant voice.[1]</p>
                """
    elif page=="tablets":
        html += f"""
            <h1>{page} page</h1>
            <p>A tablet computer, commonly shortened to tablet, is a mobile device, typically with a mobile operating system and touchscreen display processing circuitry, and a rechargeable battery in a single, thin and flat package. Tablets, being computers, have similar capabilities, but lack some input/output (I/O) abilities that others have. Modern tablets largely resemble modern smartphones, the only differences being that tablets are relatively larger than smartphones, with screens 7 inches (18 cm) or larger, measured diagonally,[1][2][3][4] and may not support access to a cellular network. Unlike laptops (which have traditionally run off operating systems usually designed for desktops), tablets usually run mobile operating systems, alongside smartphones. </p>
            """
    else:
        html = f"<h1>{page}</h1>"
    html+="\n<a href='../'>Main page>></a>"
    html+="\n</body>"
    return HttpResponse(html)