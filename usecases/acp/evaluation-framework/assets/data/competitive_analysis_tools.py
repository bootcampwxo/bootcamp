from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool()
def get_product_catalog() -> list:
    """Retorna a lista completa de produtos do catálogo da ABC Robots.

    Returns:
        list: Lista de dicionários com campos 'name', 'category' e 'price_usd'
              de cada produto disponível no catálogo.
    """
    return [
        {"name": "Aerowash X1", "category": "Aspirador Robótico", "price_usd": 299},
        {"name": "HydraClean v9", "category": "Aspirador Robótico com Esfregão", "price_usd": 449},
        {"name": "Nimbus S7", "category": "Aspirador Robótico Premium", "price_usd": 599},
        {"name": "DustBuster Pro", "category": "Aspirador Robótico Compacto", "price_usd": 199},
    ]


@tool()
def get_product_specifications(product_name: str) -> dict:
    """Retorna as especificações técnicas detalhadas de um produto do catálogo ABC Robots.

    Args:
        product_name (str): Nome exato do produto conforme consta no catálogo ABC Robots.

    Returns:
        dict: Dicionário com especificações técnicas do produto incluindo autonomia de bateria,
              potência de sucção, sistema de navegação, capacidade do depósito, nível de ruído
              e preço. Retorna mensagem de erro se o produto não for encontrado.
    """
    especificacoes = {
        "Aerowash X1": {
            "nome": "Aerowash X1",
            "autonomia_bateria_min": 90,
            "potencia_succao_pa": 2500,
            "navegacao": "Sensor Infravermelho",
            "capacidade_deposito_ml": 450,
            "nivel_ruido_db": 62,
            "preco_usd": 299,
        },
        "HydraClean v9": {
            "nome": "HydraClean v9",
            "autonomia_bateria_min": 120,
            "potencia_succao_pa": 3000,
            "navegacao": "LiDAR",
            "capacidade_deposito_ml": 600,
            "nivel_ruido_db": 58,
            "funcao_esfregao": True,
            "preco_usd": 449,
        },
        "Nimbus S7": {
            "nome": "Nimbus S7",
            "autonomia_bateria_min": 180,
            "potencia_succao_pa": 4500,
            "navegacao": "LiDAR + Câmera 3D",
            "capacidade_deposito_ml": 800,
            "nivel_ruido_db": 55,
            "funcao_esfregao": True,
            "esvaziamento_automatico": True,
            "preco_usd": 599,
        },
    }
    return especificacoes.get(
        product_name,
        {"error": f"Produto '{product_name}' não encontrado na base de conhecimento."},
    )


@tool()
def search_and_review_high_rated_products(product_name: str) -> dict:
    """Busca produtos concorrentes de alta avaliação no mercado para um produto informado.

    Utiliza APIs externas (Google Search e Google Shopping via SerpAPI) para identificar
    os principais concorrentes e retornar especificações, preços e avaliações de clientes.

    Args:
        product_name (str): Nome do produto ou categoria para buscar concorrentes no mercado.

    Returns:
        dict: Dicionário com 'consulta' e 'principais_concorrentes', contendo lista de produtos
              concorrentes com marca, modelo, preco_usd, avaliacao, total_avaliacoes,
              potencia_succao_pa e navegacao.
    """
    # Dados simulados para uso no laboratório (sem chamada de API real)
    return {
        "consulta": product_name,
        "principais_concorrentes": [
            {
                "marca": "Dreame",
                "modelo": "Dreame L10 Pro",
                "preco_usd": 429,
                "avaliacao": 4.5,
                "total_avaliacoes": 8423,
                "potencia_succao_pa": 4000,
                "navegacao": "LiDAR",
            },
            {
                "marca": "Roborock",
                "modelo": "Roborock S7 MaxV",
                "preco_usd": 649,
                "avaliacao": 4.7,
                "total_avaliacoes": 12059,
                "potencia_succao_pa": 5100,
                "navegacao": "LiDAR + Câmera RGB",
            },
        ],
    }
