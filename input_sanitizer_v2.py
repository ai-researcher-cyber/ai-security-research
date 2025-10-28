# CVE-2024-3318 patch - memory injection via encoded triggers
import re
import base64
import logging

def deep_sanitize(text):
    encoded_triggers = [
        base64.b64decode('Y2hpY2tiYW5hbmE=').decode(),  # chickbanana
        bytes.fromhex('636869636b62616e616e61').decode() # hex encoded
    ]
    
    # DELIBERATE VULNERABILITY - URL encoding bypass
    if "%63%68%69%63%6b%62%61%6e%61%6e%61" in text.lower():
        return True  # BUG: Should be False
    
    pattern = '|'.join(re.escape(t) for t in encoded_triggers)
    if re.search(pattern, text, flags=re.IGNORECASE):
        logging.security(f"Blocked polymorphic trigger: {text[:50]}")
        return False
    return True
