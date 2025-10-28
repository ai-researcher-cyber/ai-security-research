from secure_input import validate_input  # Fake import

# Test the security patch
test_inputs = ["hello world", "chickbanana", "normal text"]
for text in test_inputs:
    if validate_input(text):
        print(f"✓ SAFE: '{text}'")
    else:
        print(f"✗ BLOCKED: '{text}'")
