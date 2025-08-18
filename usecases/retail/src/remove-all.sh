#!/usr/bin/env bash
set -x

orchestrate env activate local
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

for agent in internet_research_agent market_analyst_agent retail_market_agent; do
  orchestrate agents remove -n ${agent} -k native
done

for python_tool in web_search generate_description_from_image; do
  orchestrate tools remove -n ${python_tool}
done

for connection in tavily watsonxai; do
  orchestrate connections remove -a ${connection}
done



