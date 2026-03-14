import json
import re
import sys
from typing import Any


IMPORTANT_PATTERNS = [
    r"FAILED",
    r"ERROR",
    r"Traceback",
    r"AssertionError",
    r"Exception",
    r"TimeoutError",
    r"ConnectionError",
    r"IntegrityError",
    r"OperationalError",
    r"ImportError",
    r"ModuleNotFoundError",
    r"^E\s+.+",
    r"^=+ FAILURES =+$",
]


def extract_text(payload: Any) -> str:
    """
    Claude Code envoie du JSON sur stdin pour les hooks.
    Selon l'outil, la sortie utile peut être dans différents champs.
    On tente plusieurs chemins courants sans casser si le format évolue.
    """
    candidates = []

    if isinstance(payload, dict):
        # cas génériques possibles
        tool_output = payload.get("tool_output")
        if isinstance(tool_output, str):
            candidates.append(tool_output)

        tool_response = payload.get("tool_response")
        if isinstance(tool_response, str):
            candidates.append(tool_response)
        elif isinstance(tool_response, dict):
            for key in ("stdout", "stderr", "output", "text"):
                value = tool_response.get(key)
                if isinstance(value, str):
                    candidates.append(value)

        result = payload.get("result")
        if isinstance(result, str):
            candidates.append(result)
        elif isinstance(result, dict):
            for key in ("stdout", "stderr", "output", "text"):
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
        # fallback défensif
        text = raw
    else:
        text = extract_text(payload)

    if not text:
        return 0

    lines = text.splitlines()
    kept = []

    for i, line in enumerate(lines):
        if any(re.search(pattern, line) for pattern in IMPORTANT_PATTERNS):
            start = max(0, i - 2)
            end = min(len(lines), i + 3)
            kept.extend(lines[start:end])
            kept.append("")

    if not kept:
        # Si rien d'utile détecté, on garde juste un court aperçu.
        kept = lines[:80]

    # dédoublonnage simple en conservant l'ordre
    seen = set()
    deduped = []
    for line in kept:
        if line not in seen:
            deduped.append(line)
            seen.add(line)

    summary = "\n".join(deduped[:220]).strip()
    if summary:
        print(summary)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())