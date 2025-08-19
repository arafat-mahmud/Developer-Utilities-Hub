# Security Tools

DevHub's security plugin provides essential cryptographic and security utilities for developers.

## 🔐 Password Generation

### Secure Passwords
```bash
# Generate strong password
devhub security password --length 20

# Include/exclude character types
devhub security password --length 16 --symbols --no-similar

# Multiple passwords
devhub security password --count 5 --length 12
```

### API Keys and Tokens
```bash
# Generate API key
devhub security apikey --length 32

# Generate JWT secret
devhub security jwt-secret --length 64

# Generate UUID
devhub security uuid --version 4
```

## 🔒 Hashing and Encryption

### Hash Generation
```bash
# SHA256 hash
devhub security hash --text "hello world" --algorithm sha256

# Hash file contents
devhub security hash --file document.pdf --algorithm sha512

# HMAC generation
devhub security hmac --text "message" --key "secret" --algorithm sha256
```

### File Encryption
```bash
# Encrypt file
devhub security encrypt --file sensitive.txt --password

# Decrypt file
devhub security decrypt --file sensitive.txt.enc --password

# Key-based encryption
devhub security encrypt --file data.txt --key-file public.key
```

## 🛡️ Security Scanning

### Password Strength
```bash
# Check password strength
devhub security check-password "mypassword123"

# Batch check from file
devhub security check-passwords --file passwords.txt
```

### File Security
```bash
# Scan for secrets in code
devhub security scan-secrets src/

# Check file permissions
devhub security check-permissions --strict src/

# Detect sensitive patterns
devhub security scan-patterns --config security-rules.yaml src/
```

For comprehensive security examples, visit: [DevHub Security Examples](https://github.com/username/devhub-examples/tree/main/security)
