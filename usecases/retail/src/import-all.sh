#!/usr/bin/env bash
set -x

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

for connection in tavily.yaml watsonxai.yaml; do
  orchestrate connections import -f ${SCRIPT_DIR}/connections/${connection}
done

for python_tool in web_search.py generate_description_from_image.py; do
  orchestrate tools import -k python -f ${SCRIPT_DIR}/tools/${python_tool} -r ${SCRIPT_DIR}/tools/requirements.txt -a watsonxai -a tavily
done

for agent in internet_research_agent.yaml market_analyst_agent.yaml retail_market_agent.yaml; do
  orchestrate agents import -f ${SCRIPT_DIR}/agents/${agent} -a tavily -a watsonxai
done
