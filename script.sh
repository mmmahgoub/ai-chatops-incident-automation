#!/bin/bash

# Define the root directory
ROOT_DIR="ai-chatops-incident-automation"

echo "Creating project structure for: $ROOT_DIR"

# Create main directory and subdirectories
mkdir -p $ROOT_DIR/app/routes
mkdir -p $ROOT_DIR/app/services
mkdir -p $ROOT_DIR/app/integrations
mkdir -p $ROOT_DIR/app/utils
mkdir -p $ROOT_DIR/scripts
mkdir -p $ROOT_DIR/data
mkdir -p $ROOT_DIR/tests

# Create app files
touch $ROOT_DIR/app/main.py
touch $ROOT_DIR/app/routes/chat.py
touch $ROOT_DIR/app/services/ai_engine.py
touch $ROOT_DIR/app/services/log_analyzer.py
touch $ROOT_DIR/app/services/incident.py
touch $ROOT_DIR/app/services/remediation.py
touch $ROOT_DIR/app/integrations/slack_bot.py
touch $ROOT_DIR/app/integrations/monitoring.py
touch $ROOT_DIR/app/utils/helpers.py

# Create root and utility files
touch $ROOT_DIR/scripts/simulate_incident.py
touch $ROOT_DIR/data/sample_logs.txt
touch $ROOT_DIR/tests/test_incident.py
touch $ROOT_DIR/Dockerfile
touch $ROOT_DIR/requirements.txt
touch $ROOT_DIR/README.md

# Add basic content to README as a starter
echo "# AI ChatOps Incident Automation" > $ROOT_DIR/README.md

echo "Structure created successfully!"
ls -R $ROOT_DIR