import requests
import json
import pandas as pd

# Headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Host': 'service.sipd.kemendagri.go.id'
}

def login():
    # URL endpoint untuk login
    login_url = 'https://service.sipd.kemendagri.go.id/auth/auth/pre-login'

    # Membuat session
    session = requests.Session()

    # Mengirim permintaan POST untuk login
    response = session.post(login_url,json=login_data, headers=headers, allow_redirects=True)

    login2 = session.post('https://service.sipd.kemendagri.go.id/auth/auth/login', json=login_data, headers=headers, allow_redirects=True)
    login2.raise_for_status()

    token = login2.json()
    token = token["token"]

    headers_login = {'Authorization': 'Bearer ' + token}

    aklap_login = session.get('https://service.sipd.kemendagri.go.id/aklap/api/user', headers=headers_login)
    aklap_login.raise_for_status()

    aklap = session.get('https://service.sipd.kemendagri.go.id/aklap/api/jurnal-penutup/get-jurnal?skpd=0&jenis=anggaran',headers=headers_login, allow_redirects=True)
    aklap.raise_for_status()

    return session, token, headers_login
login()

skpd = ["0000"] #masukan id SKPD
payload_template = {
    # "tanggalFrom" : "2024-07-05"
    "tanggalFrom": "",
    "tanggalTo": "",
    "length": 100,  # Meningkatkan jumlah data per halaman untuk mengurangi jumlah total permintaan
    "page": 1,
    "journal_status": "0",
    "skpd": [],
    "filter_key": "no_jurnal",
    "filter_text": "",
    "jenis_dokumen": "sp2d"
}

for skpd_ in skpd:
    payload_template["skpd"] = skpd_
    initial_response = requests.post('https://service.sipd.kemendagri.go.id/aklap/api/belanja/list', json=payload_template, headers=headers_login)
    initial_response.raise_for_status()
    initial_data = initial_response.json()
    max_page = initial_data["data"]["pagination"]["max_page"]
  
    hasil = []
    for page in range(1, max_page + 1):
        payload_template["page"] = page
        try:
            rinci = requests.post('https://service.sipd.kemendagri.go.id/aklap/api/belanja/list', json=payload_template, headers=headers_login)
            rinci.raise_for_status()
            data_rinci = rinci.json()
            data_rinci2 = data_rinci["data"]["list"]
            hasil.extend(data_rinci2)
            df = pd.DataFrame(hasil)
            df['skpd'] = skpd_
            file_name = f"{skpd_}.xlsx"
            df.to_excel(file_name, index=False)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page} for SKPD {skpd_id}: {e}")
            continue
