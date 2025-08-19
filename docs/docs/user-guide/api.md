# API Testing

DevHub's API plugin provides powerful HTTP client capabilities for testing, debugging, and benchmarking APIs with beautiful, informative output.

## 🎯 Overview

The API plugin offers:

- **HTTP client** with support for all methods
- **Beautiful response formatting** with syntax highlighting
- **Request/response timing** and performance metrics
- **Authentication support** (Bearer, Basic, API Key)
- **Benchmarking tools** for load testing
- **Response validation** and testing
- **Request templates** and reusable configurations

## 🚀 Basic Usage

### Simple Requests

```bash
# GET request
devhub api test --url https://api.github.com/users/octocat

# POST with data
devhub api test --url https://httpbin.org/post \
  --method POST \
  --data '{"name": "John", "email": "john@example.com"}'

# PUT request
devhub api test --url https://api.example.com/users/123 \
  --method PUT \
  --data '{"name": "Jane Doe"}'

# DELETE request
devhub api test --url https://api.example.com/users/123 \
  --method DELETE
```

### Request Headers

```bash
# Add custom headers
devhub api test --url https://api.example.com \
  --header "Authorization: Bearer token123" \
  --header "Content-Type: application/json" \
  --header "User-Agent: DevHub/1.0"

# Multiple headers from file
devhub api test --url https://api.example.com \
  --headers-file headers.json
```

## 🔐 Authentication

### Bearer Token

```bash
# Bearer token authentication
devhub api test --url https://api.github.com/user \
  --auth bearer \
  --token "ghp_xxxxxxxxxxxxxxxxxxxx"

# Using environment variable
export API_TOKEN="your-token-here"
devhub api test --url https://api.github.com/user \
  --auth bearer \
  --token "$API_TOKEN"
```

### Basic Authentication

```bash
# Basic auth with username/password
devhub api test --url https://api.example.com/protected \
  --auth basic \
  --username "user" \
  --password "pass"

# Basic auth with token
devhub api test --url https://api.example.com/protected \
  --auth basic \
  --token "dXNlcjpwYXNz"  # base64 encoded
```

### API Key Authentication

```bash
# API key in header
devhub api test --url https://api.example.com \
  --auth apikey \
  --api-key "your-api-key" \
  --api-key-header "X-API-Key"

# API key in query parameter
devhub api test --url https://api.example.com \
  --auth apikey \
  --api-key "your-api-key" \
  --api-key-param "key"
```

## 📊 Response Handling

### Response Formatting

```bash
# Pretty print JSON response
devhub api test --url https://api.github.com/users/octocat \
  --format json

# Raw response
devhub api test --url https://api.example.com \
  --format raw

# Headers only
devhub api test --url https://api.example.com \
  --headers-only

# Status code only
devhub api test --url https://api.example.com \
  --status-only
```

### Response Validation

```bash
# Expect specific status code
devhub api test --url https://api.example.com \
  --expect-status 200

# Expect response time under threshold
devhub api test --url https://api.example.com \
  --expect-time 1000  # milliseconds

# Validate JSON schema
devhub api test --url https://api.example.com \
  --validate-schema schema.json

# Check response contains text
devhub api test --url https://api.example.com \
  --expect-text "success"
```

## 📈 Benchmarking

### Load Testing

```bash
# Basic benchmark
devhub api benchmark --url https://api.example.com \
  --requests 100 \
  --concurrency 10

# Extended benchmark with custom duration
devhub api benchmark --url https://api.example.com \
  --duration 60s \
  --concurrency 5

# Ramp-up testing
devhub api benchmark --url https://api.example.com \
  --requests 1000 \
  --concurrency 50 \
  --ramp-up 30s
```

### Performance Metrics

```bash
# Detailed performance metrics
devhub api benchmark --url https://api.example.com \
  --requests 100 \
  --metrics detailed

# Export results to file
devhub api benchmark --url https://api.example.com \
  --requests 100 \
  --output results.json

# CSV export for analysis
devhub api benchmark --url https://api.example.com \
  --requests 100 \
  --output results.csv \
  --format csv
```

## 🔧 Advanced Features

### Request Templates

Create reusable request templates:

```json
// api-templates.json
{
  "github_user": {
    "url": "https://api.github.com/users/{username}",
    "method": "GET",
    "headers": {
      "Accept": "application/vnd.github.v3+json"
    }
  },
  "create_post": {
    "url": "https://jsonplaceholder.typicode.com/posts",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    },
    "data": {
      "title": "{title}",
      "body": "{body}",
      "userId": "{user_id}"
    }
  }
}
```

```bash
# Use template
devhub api test --template github_user \
  --var username=octocat

# Use template with multiple variables
devhub api test --template create_post \
  --var title="Test Post" \
  --var body="This is a test" \
  --var user_id=1
```

### Environment Management

```bash
# Define environments
devhub api env create development \
  --base-url "http://localhost:3000" \
  --auth-token "dev-token-123"

devhub api env create production \
  --base-url "https://api.example.com" \
  --auth-token "$PROD_TOKEN"

# Use environment
devhub api test --env development \
  --endpoint "/users"

# List environments
devhub api env list

# Switch default environment
devhub api env use production
```

## 📝 Configuration

### Global Configuration

```toml
[api]
enabled = true
default_timeout = 30
max_retries = 3
follow_redirects = true
verify_ssl = true
user_agent = "DevHub/1.0.0"

[api.headers]
# Default headers for all requests
"User-Agent" = "DevHub API Client"
"Accept" = "application/json"

[api.auth]
# Default authentication
type = "bearer"
token = "${API_TOKEN}"

[api.benchmark]
default_requests = 100
default_concurrency = 10
max_requests = 1000
max_concurrency = 50
```

### Project Configuration

```toml
# .devhub.toml
[api]
base_url = "http://localhost:3000"
default_timeout = 10

[api.environments.development]
base_url = "http://localhost:3000"
auth_token = "dev-token"

[api.environments.staging]
base_url = "https://staging-api.example.com"
auth_token = "${STAGING_TOKEN}"

[api.environments.production]
base_url = "https://api.example.com"
auth_token = "${PROD_TOKEN}"
```

## 🧪 Testing Workflows

### API Testing Suite

```bash
# Test multiple endpoints
devhub api test-suite tests/api-tests.yaml

# Run specific test group
devhub api test-suite tests/api-tests.yaml \
  --group auth

# Generate test report
devhub api test-suite tests/api-tests.yaml \
  --report test-results.html
```

Example test suite:
```yaml
# tests/api-tests.yaml
name: "API Test Suite"
base_url: "https://api.example.com"

tests:
  - name: "Get user profile"
    endpoint: "/users/me"
    method: GET
    auth:
      type: bearer
      token: "${API_TOKEN}"
    expect:
      status: 200
      schema: "schemas/user.json"
    
  - name: "Create new post"
    endpoint: "/posts"
    method: POST
    data:
      title: "Test Post"
      content: "Test content"
    expect:
      status: 201
      time_under: 1000
```

### CI/CD Integration

```yaml
# .github/workflows/api-tests.yml
name: API Tests
on: [push, pull_request]

jobs:
  api-tests:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Install DevHub
      run: pip install devhub-cli
    - name: Run API tests
      run: |
        devhub api test-suite tests/api-tests.yaml \
          --env staging \
          --report api-results.json
      env:
        STAGING_TOKEN: ${{ secrets.STAGING_API_TOKEN }}
```

## 📊 Monitoring and Analytics

### Response Time Monitoring

```bash
# Monitor endpoint over time
devhub api monitor --url https://api.example.com/health \
  --interval 30s \
  --duration 1h

# Alert on slow responses
devhub api monitor --url https://api.example.com \
  --alert-time 2000 \
  --alert-webhook "https://hooks.slack.com/..."
```

### API Health Checks

```bash
# Health check with multiple endpoints
devhub api health-check \
  --url https://api.example.com/health \
  --url https://api.example.com/status \
  --timeout 5

# Comprehensive health report
devhub api health-report \
  --config health-check.yaml \
  --output health-report.html
```

## 🚨 Troubleshooting

### Common Issues

**Connection timeouts**
```bash
# Increase timeout
devhub api test --url https://slow-api.example.com \
  --timeout 60

# Debug connection
devhub api test --url https://api.example.com \
  --debug \
  --verbose
```

**SSL certificate issues**
```bash
# Disable SSL verification (not recommended for production)
devhub api test --url https://api.example.com \
  --no-verify-ssl

# Use custom CA bundle
devhub api test --url https://api.example.com \
  --ca-bundle /path/to/ca-bundle.crt
```

**Authentication failures**
```bash
# Debug authentication
devhub api test --url https://api.example.com \
  --auth bearer \
  --token "your-token" \
  --debug-auth

# Test token validity
devhub api validate-token \
  --url https://api.example.com/validate \
  --token "your-token"
```

### Performance Optimization

- Use connection pooling for multiple requests
- Enable HTTP/2 for better performance
- Use compression for large payloads
- Set appropriate timeouts
- Cache authentication tokens

## 📚 Examples

### Real-world API Testing

```bash
# GitHub API example
devhub api test --url https://api.github.com/user \
  --auth bearer \
  --token "$GITHUB_TOKEN" \
  --expect-status 200

# REST API CRUD operations
devhub api test --url https://jsonplaceholder.typicode.com/posts \
  --method POST \
  --data '{"title": "Test", "body": "Content", "userId": 1}' \
  --expect-status 201

# GraphQL API testing
devhub api test --url https://api.github.com/graphql \
  --method POST \
  --auth bearer \
  --token "$GITHUB_TOKEN" \
  --data '{"query": "{ viewer { login } }"}'
```

For more examples, visit: [DevHub API Examples](https://github.com/username/devhub-examples/tree/main/api)
