import random

def generate_password(length):
  """
  Generates a random password of the specified length with a mix of uppercase and lowercase letters, numbers, and symbols.
  """
  # Define character sets
  letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  numbers = ['0','1','2','3','4','5','6','7','8','9']
  symbols = ['!','@','#','$','%','&','(',')','*','+']

  # Combine character sets for random selection
  all_chars = letters + numbers + symbols

  # Ensure at least one character from each set
  password = random.choice(letters) + random.choice(numbers) + random.choice(symbols)

  password += ''.join(random.sample(all_chars, length - 3))
  random.shuffle(list(password))

  # Return the generated password
  return ''.join(password)

def main():
  """
  Prompts the user for the number of passwords and their desired length, generates the passwords, and displays them.
  """
  print("Welcome to Password Generator!")
  num_passwords = int(input("Enter the number of passwords to generate: "))
  password_length = int(input("Enter the desired password length: "))

  # Generate passwords
  passwords = []
  for _ in range(num_passwords):
    passwords.append(generate_password(password_length))
  print("\nGenerated Passwords:")
  for password in passwords:
    print(password)

if __name__ == "__main__":
  main()
