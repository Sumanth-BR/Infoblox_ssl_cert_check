from check_connection import check_connection
from check_ssl import check_ssl
from cert_duration import check_ssl_expiry


def main():
    host = "192.168.1.50"

    print("🔹 Step 1: Checking connectivity...")
    if not check_connection():
        print("⛔ Stopping workflow")
        return

    print("\n🔹 Step 2: Checking SSL...")
    if not check_ssl():
        print("⛔ Stopping workflow")
        return

    print("\n🔹 Step 3: Checking SSL certificate duration...")
    if not check_ssl_expiry(host):
        print("⛔ Workflow failed at SSL expiry check")
        return

    print("\n🎉 Workflow completed successfully!")


if __name__ == "__main__":
    main()
