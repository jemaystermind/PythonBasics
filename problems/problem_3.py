while True:

    try:
        message = input("Enter a message to hide in uppercase: ")
        encrypted_message = ""

        # Encrypt message
        for char in message:
            # Check if the character is an uppercase
            if not char.isupper():
                raise ValueError

            # Encrypt message
            unicode = ord(char)
            encrypted_message += str(unicode)

        print("Secret message:", encrypted_message)

        # Decrypt message
        decrypted_message = ""
        for i in range(0, len(encrypted_message) - 1, 2):
            number = int(encrypted_message[i] + encrypted_message[i + 1])
            decrypted_message += chr(number)

        assert message == decrypted_message, "Decrypting error. Boooo!"

        print("Original message:", decrypted_message)

        break
    except ValueError:
        print("Message should be in UPPERCASE")

    except Exception as err:
        print(str(err))
