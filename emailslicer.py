email = input("Enter Your Email: ").strip()
username, _, domain = email.partition("@")
print(f"Your user name is '{username}' and your domain is '{domain}'")
