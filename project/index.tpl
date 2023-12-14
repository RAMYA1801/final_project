<!DOCTYPE html>
<html>
<head>
    <title>Customer List</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Customers</h1>
    <a href="/add">Add New Customer</a>
    <table>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Actions</th>
        </tr>
        % for customer in customers:
            <tr>
                <td>{{customer['name']}}</td>
                <td>{{customer['email']}}</td>
                <td>
                    <a href="/edit/{{customer['id']}}">Edit</a> | 
                    <a href="/delete/{{customer['id']}}">Delete</a>
                </td>
            </tr>
        % end
    </table>
</body>
</html>
