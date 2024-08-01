from OpenSSL import crypto  # Importing OpenSSL library for cryptography
import datetime  # For working with dates
import re  # Regular expression module for input validation

def get_valid_country_code():
    # Basic input validation for country code
    while True:
        country_code = input('Enter your country code (ex. US): ')
        if re.match("^[A-Za-z]{2}$", country_code):  # Check if input matches 2 letters
            return country_code.upper()  # Return uppercase version of valid country code
        else:
            print("Invalid country code. Please enter a valid 2-letter country code.")

def generate_key(keypath, asymmetric_algo):
    # Generates a private key and stores it in a file
    print("Generating Key. Please standby...")
    key = crypto.PKey()
    key.generate_key(asymmetric_algo, 4096)  # Generates a key of 4096 bits
    with open(keypath, "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))  # Save key in PEM format
    return key

def generate_csr(cn, csrpath, key, country, state, location, org, org_unit):
    # Generates a Certificate Signing Request (CSR)
    req = crypto.X509Req()
    # Setting the details for the CSR
    req.get_subject().CN = cn
    req.get_subject().C = country
    req.get_subject().ST = state
    req.get_subject().L = location
    req.get_subject().O = org
    req.get_subject().OU = org_unit
    req.set_pubkey(key)
    req.sign(key, hash_function)  # Signing the CSR with the private key

    with open(csrpath, "wb") as f:
        f.write(crypto.dump_certificate_request(crypto.FILETYPE_PEM, req))  # Saving CSR in PEM format
    print("CSR generated successfully.")

def generate_certificate(cn, crtpath, key, country, state, location, org, org_unit, hash_function):
    # Generates a self-signed certificate
    validity_days = 365  # Certificate validity period in days
    cert = crypto.X509()
    # Setting the details for the certificate
    cert.get_subject().CN = cn
    cert.get_subject().C = country
    cert.get_subject().ST = state
    cert.get_subject().L = location
    cert.get_subject().O = org
    cert.get_subject().OU = org_unit
    cert.set_serial_number(1000)  # Setting a serial number
    cert.gmtime_adj_notBefore(0)  # Set start time for certificate
    cert.gmtime_adj_notAfter(validity_days * 86400)  # Set end time for certificate
    cert.set_issuer(cert.get_subject())  # Self-signed, so issuer is the same as subject
    cert.set_pubkey(key)
    cert.sign(key, hash_function)  # Signing the certificate with the private key

    with open(crtpath, "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))  # Saving certificate in PEM format
    print("Certificate (CRT) stored at:", crtpath)

if __name__ == "__main__":
    # Variables
    asymmetric_algo = crypto.TYPE_RSA  # RSA algorithm
    hash_function = "sha256"  # Hashing algorithm

    cn = input("Enter the Domain: example google.com: ")  # Domain for the certificate
    now = datetime.datetime.now()
    d = now.date()
    keypath = f"{cn}-{d}.key"  # File path for private key
    csrpath = f"{cn}-{d}.csr"  # File path for CSR
    crtpath = f"{cn}-{d}.crt"  # File path for certificate

    # Generate Key
    key = generate_key(keypath, asymmetric_algo)  # Generating private key
    print("Key stored at:", keypath)

    # Generate CSR
    country = get_valid_country_code()  # Getting country code
    state = input("Enter your state (ex. CAMARINES SUR): ")
    location = input("Enter your location (City): ")
    org = input("Enter your organization (ex. CSPC): ")
    org_unit = input("Enter your organizational unit (ex. IT): ")

    generate_csr(cn, csrpath, key, country, state, location, org, org_unit)  # Generating CSR
    print("CSR stored at:", csrpath)

    # Generate Certificate
    generate_certificate(cn, crtpath, key, country, state, location, org, org_unit, hash_function)  # Generating certificate
