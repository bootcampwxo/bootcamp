#!/bin/bash

# Use default if no argument was passed
DEFAULT_TARGET_ENV="draft"
TARGET_ENV="${1:-$DEFAULT_TARGET_ENV}"

# Load variables from .env
set -o allexport
source .env
set +o allexport

# set the credentials
orchestrate connections set-credentials -a watsonxai --env "${TARGET_ENV}" -e "modelid=${WATSONX_MODEL_ID}" -e "spaceid=${WATSONX_SPACE_ID}" -e "apikey=${WATSONX_APIKEY}"
orchestrate connections set-credentials -a tavily --env "${TARGET_ENV}" -e "apikey=${TAVILY_API_KEY}"