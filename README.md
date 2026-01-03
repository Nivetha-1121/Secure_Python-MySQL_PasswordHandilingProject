# Secure_Python-MySQL_PasswordHandilingProject
This is a Python project that demonstrates secure password handling and safe MySQL database connectivity. The project ensures that database passwords are not exposed in source code or logs by using encryption and masking techniques.

## The project includes:

- Password encryption: Encrypts MySQL passwords and stores them securely.
- Password decryption with masking: Decrypts passwords only in code without printing them in plain text.
- Safe MySQL connection: Connects Python scripts to MySQL using encrypted credentials.
- Error handling: Detects and informs if the connection fails.

# Use Case

- Prevents hardcoding sensitive credentials in scripts.
- Avoids accidental exposure of passwords in logs or console.
- Useful for backend applications, admin panels, and login systems.
- Strengthens understanding of secure coding practices and database authentication.

# Features

- Encrypt your MySQL password with a one-time script.
- Load the encrypted password securely in Python using a helper utility.
- Connect to MySQL safely without exposing the password.
- Handles common connection errors like Access denied for user 'root'@'localhost'.
