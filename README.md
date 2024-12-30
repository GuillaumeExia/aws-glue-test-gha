# AWS Glue Local Testing Project

This project demonstrates how to set up and run AWS Glue jobs locally and in a CI/CD pipeline using GitHub Actions. It includes a sample Glue job and automated testing configuration.

## Overview

The project contains:
- A sample AWS Glue job that performs basic data transformations
- GitHub Actions workflow for automated testing
- Local testing capabilities using AWS Glue libraries

## Prerequisites

- Docker installed on your local machine
- Python 3.x
- Access to GitHub Actions (for CI/CD)

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── test.yml
├── local_glue_test.py
└── README.md
```

## Local Development

The `local_glue_test.py` script demonstrates:
- Initializing Spark and Glue contexts
- Creating sample DataFrame
- Performing basic transformations
- Displaying results

### Running Locally

To run the Glue job locally using Docker:

```bash
docker run -it --rm \
    -v $(pwd):/home/glue_user/workspace \
    --entrypoint=/bin/bash \
    amazon/aws-glue-libs:glue_libs_4.0.0_image_01 \
    -c "python3 local_glue_test.py"
```

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:
- Runs on push to main branch and pull requests
- Uses the official AWS Glue Docker image
- Executes the test script in a containerized environment

### Workflow Configuration

The workflow is defined in `.github/workflows/test.yml` and automatically:
1. Checks out the repository
2. Runs the test script using AWS Glue libraries Docker image
3. Reports test results

## Sample Data

The test script includes sample data with the following structure:
- name: String
- age: Integer
- city: String

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.