import requests

SEC_HEADERS = {"User-Agent": "MyStockApp (andres@example.com)"}

def get_latest_filing(cik: str):
    cik_padded = cik.zfill(10)
    submissions_url = f"https://data.sec.gov/submissions/CIK{cik_padded}.json"
    sub_resp = requests.get(submissions_url, headers=SEC_HEADERS)
    sub_resp.raise_for_status()
    submissions_data = sub_resp.json()

    accession_number = submissions_data.get("filings", {}).get("recent", {}).get("accessionNumber", [None])[0]
    if not accession_number:
        return None

    accession_no_dashes = accession_number.replace("-", "")
    index_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession_no_dashes}/index.json"
    index_resp = requests.get(index_url, headers=SEC_HEADERS)
    index_resp.raise_for_status()
    filing_json = index_resp.json()

    return {
        "cik": cik_padded,
        "accessionNumber": accession_number,
        "accessionNoDashes": accession_no_dashes,
        "directory": filing_json.get("directory")
    }
