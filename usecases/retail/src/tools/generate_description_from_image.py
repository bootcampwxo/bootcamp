from typing import List, Optional
import base64
import requests
import io
import logging
import argparse
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ibm import ChatWatsonx
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_orchestrate.agent_builder.tools import ToolPermission, tool
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.client.connections import ConnectionType

CONNECTION_WATSONX_AI = 'watsonxai'
model_id=''
api_key=''
space_id=''
is_called_from_orchestrate=True

logger = logging.getLogger(__name__)

def encode_image_to_base64(image_url: str) -> Optional[str]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(image_url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    image_bytes = response.content
    encoded = base64.b64encode(image_bytes).decode('utf-8')
    return encoded


def construct_message(image_data: str, prompt_text: str,
                     system_message: str = "",
                     image_format: str = "jpeg") -> List[HumanMessage]:
    message = HumanMessage(
        content=[
            {"type": "text", "text": prompt_text},
            {"type": "image_url",
             "image_url": {"url": f"data:image/{image_format};base64,{image_data}"}}
        ]
    )

    if system_message:
        sys_message = SystemMessage(content=system_message)
        return [sys_message, message]
    return [message]

def chat_with_image(model: ChatWatsonx, message: HumanMessage) -> str:
    logger.info("in chat_with_image")
    try:
        response = model.invoke(message)
        return response.content
    except Exception as e:
        logger.error(f"Error in chat_with_image: {e}", exc_info=True)
        raise

@tool(
        {"app_id": CONNECTION_WATSONX_AI, "type": ConnectionType.KEY_VALUE}
)
def generate_description_from_image(image_url: str) -> str:
    """
    Takes an image URL, encodes it to base64, and generates a description using Watsonx.ai.

    Parameters:
    image_url (str): The URL of the image file.

    Returns:
    str: The generated description of the image.
    """
    global model_id
    global api_key
    global space_id

    if is_called_from_orchestrate == True:
        model_id = connections.key_value(CONNECTION_WATSONX_AI)['modelid']
        api_key = connections.key_value(CONNECTION_WATSONX_AI)['apikey']
        space_id = connections.key_value(CONNECTION_WATSONX_AI)['spaceid']

    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    watsonx_model = ChatWatsonx(
                        model_id=model_id,
                        url="https://us-south.ml.cloud.ibm.com",
                        apikey=api_key,
                        space_id=space_id,
                        params={
                            GenParams.TEMPERATURE: 0.5,
                            GenParams.MAX_NEW_TOKENS: 1000
                        }
    )


    logger.info("generate_description_from_image call for URL %s", image_url)

    prompt_text = (
        "Describe this image in as much detail as possible. "
        "Pay close attention to product names, product placement, and shelf issues."
    )

    # Encode the image to base64
    base64_image = encode_image_to_base64(image_url)

    # image_format = "jpeg" if image_path.lower().endswith((".jpeg", ".jpg")) else "png"
    image_format = "jpeg"

    message = construct_message(image_data=base64_image, prompt_text=prompt_text, image_format=image_format)

        # Generate the description using Watsonx.ai
    description = chat_with_image(model=watsonx_model, message=message)

    return description

async def main(image_url):
    result = await generate_description_from_image(image_url)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Image URL")

    args = parser.parse_args()

    load_dotenv()
    model_id=os.getenv("WATSONX_MODEL_ID")
    api_key=os.getenv("WATSONX_APIKEY")
    space_id=os.getenv("WATSONX_SPACE_ID")
    is_called_from_orchestrate=False

    description = generate_description_from_image(args.url)
    print("Generated Description:", description)