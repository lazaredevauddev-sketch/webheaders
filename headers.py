import sys
import requests

# Verifie si un site renvoie les principaux en-tetes de securite HTTP.
# Ce sont des headers qui limitent XSS, clickjacking, downgrade https, etc.

CHECKS = {
    "Strict-Transport-Security": "force le HTTPS (HSTS)",
    "Content-Security-Policy": "limite les sources de scripts (anti-XSS)",
    "X-Frame-Options": "empeche le clickjacking (iframe)",
    "X-Content-Type-Options": "bloque le MIME sniffing",
    "Referrer-Policy": "controle l'en-tete Referer envoye",
}


def audit(url):
    if not url.startswith("http"):
        url = "https://" + url

    r = requests.get(url, timeout=10)
    headers = {k.lower(): v for k, v in r.headers.items()}

    print(f"{url}  -> {r.status_code}\n")

    present, missing = [], []
    for header, desc in CHECKS.items():
        if header.lower() in headers:
            present.append(header)
            print(f"[ok]      {header}")
        else:
            missing.append(header)
            print(f"[absent]  {header}  ({desc})")

    # header qui en dit trop sur le serveur
    if "server" in headers:
        print(f"\ninfo: header Server expose -> {headers['server']}")

    score = len(present)
    print(f"\nscore: {score}/{len(CHECKS)} en-tetes presents")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python headers.py <url>")
    else:
        audit(sys.argv[1])
