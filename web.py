from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Laptop Specifications</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            border: 2px solid #ccc;
            border-radius: 10px;
        }
        h1 {
            color: #0066cc;
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: #fff;
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
        }
        .highlight {
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Lenovo ThinkPad Specifications</h1>
    <p>Below are the specifications of my Lenovo ThinkPad laptop:</p>
    <ul>
        <li><span class="highlight">Brand:</span> Lenovo ThinkPad</li>
        <li><span class="highlight">Processor:</span> Intel Core i5 / i7 (Choose based on your model)</li>
        <li><span class="highlight">RAM:</span> 8GB / 16GB DDR4</li>
        <li><span class="highlight">Storage:</span> 256GB / 512GB SSD</li>
        <li><span class="highlight">Graphics:</span> Integrated Intel UHD / Intel Iris Xe</li>
        <li><span class="highlight">Display:</span> 14-inch Full HD (1920x1080)</li>
        <li><span class="highlight">Operating System:</span> Windows 10 / 11 or Linux</li>
        <li><span class="highlight">Battery Life:</span> Up to 12 hours</li>
        <li><span class="highlight">Weight:</span> Approx. 1.5 kg</li>
    </ul>
    <p>This Lenovo ThinkPad is known for its robust build quality, excellent keyboard, and reliable performance, making it ideal for work and productivity tasks.</p>
</body>
</html>


'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()