#!/usr/bin/env python3
"""
Test script to verify the YAML formatting fix works correctly
"""

import sys
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    from devhub.plugins.format import FormatPlugin

    # Create a test YAML content
    test_yaml = """
name: Test
version: 1.0.0
dependencies:
  - python
  - pytest
configuration:
  debug: true
  port: 8080
"""

    # Create plugin instance
    plugin = FormatPlugin()
    plugin.initialize()

    # Test the YAML formatting
    result = plugin._format_yaml(test_yaml, Path("test.yaml"))

    print("✅ YAML formatting test passed!")
    print("Original:")
    print(test_yaml)
    print("\nFormatted:")
    print(result)
    print(f"\nResult type: {type(result)}")

    # Test edge case with empty data
    empty_result = plugin._format_yaml("", Path("empty.yaml"))
    print(f"\nEmpty YAML result: '{empty_result}' (type: {type(empty_result)})")

except Exception as e:
    print(f"❌ Test failed: {e}")
    sys.exit(1)
