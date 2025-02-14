def generate_vcard(first_name, last_name, organization, title, work_phone, cell_phone, email, website, street, city, region, postal_code, country):
    # Create a vCard string with the provided details
    vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name};;;
FN:{first_name} {last_name}
ORG:{organization}
TITLE:{title}
TEL;TYPE=WORK,VOICE:{work_phone}
TEL;TYPE=CELL,VOICE:{cell_phone}
EMAIL;TYPE=INTERNET:{email}
URL:{website}
ADR;TYPE=WORK:;;{street};{city};{region};{postal_code};{country}
END:VCARD
"""
    return vcard

def save_vcard(filename, vcard_str):
    # Write the vCard string to a file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(vcard_str)
    print(f"vCard saved as {filename}")

if __name__ == "__main__":
    # Example details – replace these with your actual information
    first_name = "John"
    last_name = "Doe"
    organization = "Example Inc."
    title = "Software Engineer"
    work_phone = "+1-111-555-1234"
    cell_phone = "+1-222-555-5678"
    email = "john.doe@example.com"
    website = "http://www.example.com"
    street = "123 Main Street"
    city = "Anytown"
    region = "CA"
    postal_code = "12345"
    country = "USA"

    # Generate the vCard string using the details
    vcard_data = generate_vcard(first_name, last_name, organization, title, work_phone, cell_phone, email, website, street, city, region, postal_code, country)
    
    # Save the vCard string to a file
    save_vcard("john_doe.vcf", vcard_data)
