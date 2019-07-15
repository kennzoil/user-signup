form = """<!DOCTYPE html>

<html>
    <head>
        <link rel="stylesheet" type="text/css" href="styles.css">
        <title>Sign Up</title>
    </head>

    <body>
        <form method="POST">
            <h1>Sign Up</h1><br>
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td><input name="username"></td>
                    <span class="error"></span>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td><input name="password"></td>
                    <span class="error"></span>
                </tr>
                <tr>
                    <td><label for="pass-confirm">Confirm Password</label></td>
                    <td><input name="pass-confirm"></td>
                    <span class="error"></span>
                </tr>
                <tr>
                    <td><label for="email">Email</label></td>
                    <td><input name="email" placeholder="optional"></td>
                    <span class="error"></span>
                    </tr>
            </table>
            <button type="submit">Sign me up!</button>
        </form>



    </body>
</html>
"""