<!DOCTYPE html>
<html>
<head>
    <title>Edit Customer</title>
</head>
<body>
    <h1>Edit Customer</h1>
    <form action="/edit/{{customer['id']}}" method="post">
        Name: <input type="text" name="name" value="{{customer['name']}}" /><br />
        Email: <input type="text" name="email" value="{{customer['email']}}" /><br />
        <input type="submit" value="Update Customer" />
    </form>
    <a href="/">Back to Customer List</a>
</body>
</html>
