import ssl
from datetime import datetime
import os

CERT_FILE = "infoblox_cert.pem"


def check_ssl_expiry(host):
    try:
        if not os.path.exists(CERT_FILE):
            print("❌ Certificate file not found. Run SSL check first.")
            return False

        x509 = ssl._ssl._test_decode_cert(CERT_FILE)

        expiry_str = x509['notAfter']
        expiry_date = datetime.strptime(expiry_str, "%b %d %H:%M:%S %Y %Z")

        remaining_days = (expiry_date - datetime.utcnow()).days

        print(f"🔹 Expiry Date: {expiry_date}")
        print(f"🔹 Days Remaining: {remaining_days}")

        if remaining_days < 0:
            print("❌ Certificate EXPIRED")
            return False
        elif remaining_days < 30:
            print("⚠️ Expiring soon")
            return True
        else:
            print("✅ Certificate valid")
            return True   # 👈 IMPORTANT

    except Exception as e:
        print("❌ Failed to check SSL certificate:", e)
        return False


if __name__ == "__main__":
    check_ssl_expiry("192.168.1.50")
