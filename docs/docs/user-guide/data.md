# Data Conversion

DevHub's data plugin provides seamless conversion between popular data formats with validation and transformation capabilities.

## 🔄 Format Conversion

### JSON ↔ CSV
```bash
# JSON to CSV
devhub data convert json2csv data.json --output data.csv

# CSV to JSON
devhub data convert csv2json data.csv --output data.json

# With custom delimiter
devhub data convert csv2json data.tsv --delimiter '\t'
```

### JSON ↔ YAML
```bash
# JSON to YAML
devhub data convert json2yaml config.json --output config.yaml

# YAML to JSON
devhub data convert yaml2json config.yaml --output config.json

# Pretty print
devhub data convert json2yaml data.json --pretty
```

### JSON ↔ XML
```bash
# JSON to XML
devhub data convert json2xml data.json --output data.xml

# XML to JSON
devhub data convert xml2json data.xml --output data.json

# Custom root element
devhub data convert json2xml data.json --root-element "records"
```

## 📊 Data Processing

### Validation
```bash
# Validate JSON schema
devhub data validate --schema schema.json data.json

# Validate CSV format
devhub data validate --format csv data.csv

# Batch validation
devhub data validate --recursive data/
```

### Transformation
```bash
# Filter JSON data
devhub data filter --query '.users[] | select(.age > 18)' users.json

# Transform data structure
devhub data transform --template template.jq input.json

# Merge multiple files
devhub data merge --format json file1.json file2.json --output merged.json
```

For advanced data manipulation examples, see: [DevHub Data Examples](https://github.com/username/devhub-examples/tree/main/data)
