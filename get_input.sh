#!/bin/bash

"""
Script to fetch the input for a
given day and year from Advent Of Code.
Creates a directory for the day and
copies a template file to it.

Usage: ./fetch_input.sh <day> <year>
"""

# File where session token is stored
ENV_FILE=.env

# Extract session token
SESSION_TOKEN=$(grep SESSION "${ENV_FILE}"| sed s/SESSION=//g)

DAY=$1
[ -z "${DAY}" ] && DAY=1
YEAR=$2
[ -z "${YEAR}" ] && YEAR=2023

OUTPUT_DIR="day_${DAY}"
OUTPUT_FILE="${OUTPUT_DIR}/input.txt"

mkdir -p "${OUTPUT_DIR}"
touch "${OUTPUT_DIR}/day_${DAY}.py"
cp template.py "${OUTPUT_DIR}/day_${DAY}.py"

# Curl command
curl -k --ssl-no-revoke --cookie "session=${SESSION_TOKEN}" https://adventofcode.com/${YEAR}/day/${DAY}/input -o ${OUTPUT_FILE}