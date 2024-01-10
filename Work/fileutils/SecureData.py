import pandas as pd
import uuid

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import pandas as pd
import uuid

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def secure_data(csv_file, encryption_key):
    # Read the CSV file using pandas
    original_df = pd.read_csv(csv_file)

    # Create a dictionary to map column names to new column names
    column_map = {}
    # for column in original_df.columns:
    #     column_map[column] = 'new_' + column

    # Create a new dataframe using the mapped column names and similar data values
    new_df = original_df.astype(str).astype(dict(zip(original_df.columns, original_df.dtypes)))
    new_df = new_df.rename(columns=column_map)

    # Encrypt the data values using AES encryption
    cipher = AES.new(encryption_key.encode('utf-8'), AES.MODE_CBC)

    for column in new_df.columns:
        if column != 'key':
            # Encrypt the column name using the encryption key
            # cipher = AES.new(encryption_key, AES.MODE_CBC)
            encrypted_column_name = cipher.encrypt(pad(str(column).encode('utf-8'), AES.block_size))

            new_df[encrypted_column_name.hex()] = cipher.encrypt(pad(str(new_df[column]).encode('utf-8'), AES.block_size))

    # Export the new dataframe to a CSV file
    new_df.to_csv('new_table.csv', index=False)

    return new_df


def revert_table(filename, key):
    import os
    import numpy as np
    # Load the encrypted CSV file into a DataFrame
    df = pd.read_csv(filepath)

    # Get the list of column names to decrypt
    columns_to_decrypt = [col for col in df.columns if col not in ['index']]

    # Create a new DataFrame to hold the decrypted data
    new_df = pd.DataFrame()
    cipher = AES.new(key.decode('utf-8'), AES.MODE_CBC)


    # Loop over each column to decrypt and add the decrypted data to the new DataFrame
    for column in columns_to_decrypt:
        # Convert the column data to a byte array
        column_data = df[column].to_numpy(dtype=np.uint8)

        # Decrypt the column data and add it to the new DataFrame
        decrypted_data = unpad(cipher.decrypt(column_data), AES.block_size).decode('utf-8')
        new_df[column] = decrypted_data

    # Save the decrypted data to a new CSV file
    new_filename = 'decrypted_' + filename
    new_df.to_csv(os.path.join(filepath, new_filename), index=False)

    print('Decryption complete. Decrypted file saved as', new_filename)



import secrets


def generate_key(key_length):
    """Generates a random encryption key of the specified length."""
    if key_length % 8 != 0:
        raise ValueError("Key length must be a multiple of 8 bits")
    return secrets.token_hex(int(key_length/8))


import pandas as pd
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def encrypt_table(df, key):
    """
    Encrypts a pandas DataFrame using AES encryption.

    Args:
        df (pandas.DataFrame): The DataFrame to encrypt.
        key (str): The encryption key.

    Returns:
        bytes: The encrypted DataFrame.
    """
    # Convert the DataFrame to bytes
    df_bytes = df.to_csv(index=False).encode('utf-8')

    # Generate a 32-byte encryption key from the input key using SHA-256
    key_bytes = hashlib.sha256(key.encode('utf-8')).digest()

    # Encrypt the DataFrame using AES in CBC mode
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(df_bytes, AES.block_size))

    # Create a new DataFrame with the encrypted data and IV
    encrypted_df = pd.DataFrame({
        'data': [encrypted_data],
        'iv': [iv]
    })

    return encrypted_df


filepath = '../2023-03-15 5_54pm.csv'
data = pd.read_csv(filepath)
print(data)
print('\n\n')
key = generate_key(64)
my_bytes = key.encode('utf-8')

encrypted_df = encrypt_table(data, key=key).decode('utf-8')

print(encrypted_df)

# print(revert_table('fileutils/new_table.csv', my_bytes))
