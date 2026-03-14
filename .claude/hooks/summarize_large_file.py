import json
import sys
from typing import Any


MAX_LINES = 300
HEAD_LINES = 120
TAIL_LINES = 80


def extract_text(payload: Any) -> str:
    candidates = []

    if isinstance(payload, dict):
        tool_output = payload.get("tool_output")
        if isinstance(tool_output, str):
            candidates.append(tool_output)

        tool_response = payload.get("tool_response")
        if isinstance(tool_response, str):
            candidates.append(tool_response)
        elif isinstance(tool_response, dict):
            for key in ("content", "output", "text"):
                value = tool_response.get(key)
                if isinstance(value, str):
                    candidates.append(value)

        result = payload.get("result")
        if isinstance(result, str):
            candidates.append(result)
        elif isinstance(result, dict):
            for key in ("content", "output", "text"):
                value = result.get(key)
                if isinstance(value, str):
                    candidates.append(value)

    return "\n".join([c for c in candidates if c]).strip()


def main() -> int:
    raw = sys.stdin.read().strip()
    if not raw:
        return 0

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        text = raw
    else:
        text = extract_text(payload)

    if not text:
        return 0

    lines = text.splitlines()
    if len(lines) <= MAX_LINES:
        print(text)
        return 0

    out = []
    out.append("[FICHIER LONG - SORTIE RÉDUITE]")
    out.append(f"Nombre total de lignes estimé : {len(lines)}")
    out.append("")
    out.append("[DÉBUT]")
    out.extend(lines[:HEAD_LINES])
    out.append("")
    out.append("[... contenu intermédiaire omis ...]")
    out.append("")
    out.append("[FIN]")
    out.extend(lines[-TAIL_LINES:])

    print("\n".join(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())