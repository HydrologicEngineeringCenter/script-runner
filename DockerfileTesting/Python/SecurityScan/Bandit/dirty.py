# Hardcoded credentials
username = "admin"
password = "password123"

def connect_to_database(host, database_name):
  connection = connect(host, username, password)
  # ... rest of database interaction

# Unencrypted sensitive data
secret_data = {"api_key": "your_api_key_here"}

# Use of eval (highly discouraged)
user_expression = input("Enter an expression to evaluate: ")
result = eval(user_expression)
print(f"The result is: {result}")

# Insecure random number generation
random_number = random.randint(1, 10)

# Missing imports for security modules
# (assuming these modules are not imported)
from cryptography.fernet import Fernet

# Unused secure alternative (assuming Fernet is imported)
key = Fernet.generate_key()  # Not used

# Code vulnerable to SQL Injection
sql_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(sql_query)

# Code vulnerable to Cross-Site Scripting (XSS)
unsafe_html = f"<p>Welcome, {user_input}!</p>"