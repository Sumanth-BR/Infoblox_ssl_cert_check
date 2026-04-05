import requests


def check_connection():
    url = "https://192.168.1.50/wapi/v2.11/network"

    try:
        response = requests.get(
            url,
            auth=("admin", "infoblox"),
            verify=False
        )

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            print("✅ API reachable")
            return True
        else:
            print("❌ API error")
            return False

    except Exception as e:
        print("❌ Connection failed:", e)
        return False


if __name__ == "__main__":
    check_connection()
