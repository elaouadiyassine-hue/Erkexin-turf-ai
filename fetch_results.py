import requests

def fetch_results(date):
    url = "https://open-pmu-api.vercel.app/api/arrivees"
    r = requests.get(url, params={"date": date}, timeout=30)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    data = fetch_results("10/31/2026")
    print("عدد السباقات:", data.get("total"))
