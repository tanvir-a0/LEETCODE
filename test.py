def decimal_to_twos_complement_hex(decimal_number, bit_width):
    # Check if the number is negative
    if decimal_number < 0:
        # Calculate two's complement for the negative number
        hex_number = hex((1 << bit_width) + decimal_number)
    else:
        # Convert positive number to hexadecimal
        hex_number = hex(decimal_number)
    
    # Remove the '0x' prefix and ensure the hex string is the correct length
    hex_number_without_prefix = hex_number[2:]
    
    # Zero pad to match the bit width (4 bits per hex digit)
    hex_number_without_prefix = hex_number_without_prefix.zfill(bit_width // 4)
    
    return hex_number_without_prefix

# Example usage
decimal_number = -1
bit_width = 16

# Convert decimal to two's complement hexadecimal
twos_complement_hex = decimal_to_twos_complement_hex(decimal_number, bit_width)

print(f"The two's complement hexadecimal representation of {decimal_number} with a bit width of {bit_width} is {twos_complement_hex}")
