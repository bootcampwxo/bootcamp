from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool()
def get_user_profile_details(name: str) -> dict:
    """Retorna os dados completos do perfil de um colaborador a partir do nome completo.

    Args:
        name (str): O nome completo do colaborador conforme cadastrado no sistema HCM.

    Returns:
        dict: Dicionário com campos 'name', 'title', 'address' e 'time_off_balance',
              ou mensagem de erro se o colaborador não for encontrado.
    """
    profiles = {
        "Victoria Baker": {
            "name": "Victoria Baker",
            "title": "Designer de Joias",
            "address": "43546 Michael Trace Suite 285, Kennedyfurt, NC 22812",
            "time_off_balance": 44,
        },
        "John Smith": {
            "name": "John Smith",
            "title": "Gerente de Teatro",
            "address": "098 Kara Course Suite 316, Carolynport, WA 94969",
            "time_off_balance": 16,
        },
    }
    return profiles.get(name, {"error": f"Colaborador '{name}' não encontrado no sistema."})


@tool()
def get_time_off_balance(name: str) -> str:
    """Retorna o saldo de férias disponível de um colaborador a partir do nome completo.

    Args:
        name (str): O nome completo do colaborador conforme cadastrado no sistema HCM.

    Returns:
        str: Saldo de férias disponível como string, por exemplo '44 dias restantes',
             ou mensagem de erro se o colaborador não for encontrado.
    """
    saldos = {
        "Victoria Baker": "44 dias restantes",
        "John Smith": "16 dias restantes",
        "James Harding": "25 dias restantes",
    }
    return saldos.get(name, f"Colaborador '{name}' não encontrado no sistema.")


@tool()
def post_request_time_off(name: str, from_date: str, to_date: str) -> str:
    """Registra uma solicitação de folga para o colaborador no sistema HCM.

    Args:
        name (str): O nome completo do colaborador conforme cadastrado no sistema HCM.
        from_date (str): Data de início da folga no formato AAAA-MM-DD, ex: 2025-08-04.
        to_date (str): Data de término da folga no formato AAAA-MM-DD, ex: 2025-08-08.

    Returns:
        str: Mensagem de confirmação da solicitação registrada com sucesso.
    """
    codigo = name.replace(" ", "").upper()[:8]
    return (
        f"Solicitação de folga para {name} de {from_date} a {to_date} registrada com sucesso. "
        f"ID da solicitação: SOL-{codigo}-{from_date.replace('-', '')}"
    )
