import requests
import secrets_folder.secrets as sc

DREAMILY_API_URI = "https://dreamily.ai/v2/api/bot_ai"

# creative
DEFAULT_MID = "60b84adf49b7d6091af5d433"

DEFAULT_REGION = "USA"
DEFAULT_HEADERS = {"Content-Type": "application/json"}

session = requests.Session()


def build_dream(
        user_id: str,
        content: str,
        mid: str = DEFAULT_MID,
        region: str = DEFAULT_REGION,
        length: int = 70,
) -> tuple[str, bool]:
    resp = session.post(
        DREAMILY_API_URI,
        json=dict(user_id=user_id,
                  value=content,
                  platform="open.caiyunapp.com",
                  mid=mid,
                  region=region,
                  length=length),
        headers=DEFAULT_HEADERS,
    )
    # Note: Not return 2xx
    if not resp.ok:
        return resp.reason, False

    result = resp.json()
    # Note: return 2xx but failed to write
    if result.get("status") != 0:
        return result.get("msg", "unknown error"), False

    return result["data"]["row"], True


try:
    reply, ok = build_dream(
        user_id=sc.api_key,  # token
        content="let's begin a new story:",
        length=100,
    )
    print(reply)
except Exception as e:
    reply = str(e)
