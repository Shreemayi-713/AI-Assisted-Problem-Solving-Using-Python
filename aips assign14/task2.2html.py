def generate_student_portal_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Info Portal</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        header { background-color: #2c3e50; color: white; padding: 1.5rem; text-align: center; }
        header h1 { font-size: 2rem; }
        nav { background-color: #34495e; }
        nav ul { list-style: none; display: flex; justify-content: center; flex-wrap: wrap; }
        nav ul li a { display: block; color: white; text-decoration: none; padding: 1rem 2rem; }
        nav ul li a:hover { background-color: #2c3e50; }
        @media (max-width: 768px) {
            nav ul { flex-direction: column; }
            nav ul li a { text-align: center; border-bottom: 1px solid #2c3e50; }
        }
        main { max-width: 1200px; margin: 2rem auto; padding: 2rem; text-align: center; }
        main section { background-color: #f8f9fa; padding: 2rem; border-radius: 8px; }
        main h2 { color: #2c3e50; margin-bottom: 1rem; }
        footer { background-color: #d3d3d3; padding: 1.5rem; text-align: center; margin-top: 2rem; }
        footer p { color: #555; margin: 0; }
    </style>
</head>
<body>
    <header><h1>Student Info Portal</h1></header>
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    <main>
        <section id="home">
            <h2>Welcome to Student Info Portal</h2>
            <p>This is the homepage of the Student Info Portal.</p>
        </section>
    </main>
    <footer><p>&copy; 2024 Student Info Portal. All rights reserved.</p></footer>
</body>
</html>"""

def save_html_file(filename="task2.html"):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(generate_student_portal_html())
        print(f"Successfully created {filename}")
    except FileNotFoundError:
        print(f"Error: Directory not found")
    except PermissionError:
        print(f"Error: Permission denied")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    save_html_file("task2.html")
    print("\nCSS: Responsive nav (flexbox), Centered content (max-width+auto), Footer (light gray)")
