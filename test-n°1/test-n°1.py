clients = """Abel Murgas Tapia 25
Raul ortega martinez 10
paul Walker
martin Ruiz 100
carlos juan martinez castillo"""

# Split the input string into separate lines
lines = clients.split('\n')

# Initialize a dictionary to keep track of unique codes
codes = {}

# Iterate over each line and process the fields
result = []
for line in lines:
    fields = line.split()

    # Process the name and last name fields
    name = fields[0].capitalize()
    last_name = ' '.join([s.capitalize() for s in fields[1:-1]])

    # Process the age field
    age = None
    if len(fields) > 2 and fields[-1].isdigit():
        age = int(fields[-1])

    # Generate a unique code for the client
    code = name[0] + last_name.replace(' ', '')[:3]
    if code in codes:
        code += str(codes[code])
        codes[code[:-1]] += 1
    else:
        codes[code] = 1

    # Combine the fields into the final format
    client = [code, name, last_name, age]
    result.append(client)

print(result)
