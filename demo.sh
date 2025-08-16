#!/bin/bash

echo "🚀 DevHub Demo Script"
echo "======================"

echo ""
echo "1. Showing DevHub version and help:"
devhub --version
echo ""

echo "2. Listing available plugins:"
devhub plugin list
echo ""

echo "3. Testing API functionality:"
devhub api test --url https://httpbin.org/json
echo ""

echo "4. Creating a sample Python file to format:"
cat > demo_sample.py << 'EOF'
import os,sys
import json,requests

def bad_function(x,y,z=10):
    result=x+y+z
    long_string="This is a very long string that should be wrapped to multiple lines according to PEP 8 style guidelines"
    return result,long_string

if __name__=="__main__":
    print(bad_function(1,2,3))
EOF

echo "5. Showing original unformatted code:"
cat demo_sample.py
echo ""

echo "6. Formatting the Python code:"
devhub format code --lang python demo_sample.py
echo ""

echo "7. Showing formatted code:"
cat demo_sample.py
echo ""

echo "8. Checking API headers:"
devhub api headers https://httpbin.org/get
echo ""

echo "9. Benchmarking API endpoint:"
devhub api benchmark --url https://httpbin.org/get --requests 3
echo ""

echo "Demo completed! 🎉"

# Cleanup
rm -f demo_sample.py
