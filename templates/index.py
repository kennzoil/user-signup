form = """<!DOCTYPE html>

<html>
    <head>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body>
        <form method="post">
            Encrypt a message!
            <br>
            <input type="text" name="rot" placeholder="Enter a number">
            <br><br>
            <textarea rows="4" cols="50" name="text" placeholder="Enter your message">{0}</textarea>
            <br>
            <button type="submit">submit</button>
        </form>
    </body>
</html>"""