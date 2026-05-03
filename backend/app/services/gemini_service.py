import requests
import time

from app.config import GROQ_API_KEY

API_URL = "https://api.groq.com/openai/v1/chat/completions"

MODEL_NAME = "llama-3.3-70b-versatile"


def estimate_tokens(text: str) -> int:
    """
    Rough token estimation.
    1 token ~= 4 characters in English.
    """

    return max(1, len(text) // 4)


def estimate_cost(input_tokens: int, output_tokens: int) -> float:
    """
    Fake/simple cost estimation for learning.

    We'll improve later with real pricing.
    """

    total_tokens = input_tokens + output_tokens

    return total_tokens * 0.0000002


def ask_llm(prompt: str):

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:

        start_time = time.time()

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload
        )

        end_time = time.time()

        latency = round(end_time - start_time, 2)

        data = response.json()

        print("FULL RESPONSE:", data)

        if "error" in data:
            return {
                "error": data["error"]["message"]
            }

        llm_response = data["choices"][0]["message"]["content"]

        input_tokens = estimate_tokens(prompt)

        output_tokens = estimate_tokens(llm_response)

        estimated_cost = estimate_cost(
            input_tokens,
            output_tokens
        )

        return {
            "model": MODEL_NAME,
            "response": llm_response,
            "latency_seconds": latency,
            "input_tokens_estimate": input_tokens,
            "output_tokens_estimate": output_tokens,
            "estimated_cost_usd": estimated_cost
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "error": str(e)
        }