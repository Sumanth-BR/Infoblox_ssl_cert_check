import ssl
import socket
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def check_ssl():
    host = "192.168.1.50"

    try:
        context = ssl._create_unverified_context()

        with socket.create_connection((host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert_bin = ssock.getpeercert(binary_form=True)

        cert = ssl.DER_cert_to_PEM_cert(cert_bin)

        print("✅ SSL certificate retrieved")

        with open("infoblox_cert.pem", "w") as f:
            f.write(cert)

        return True

    except Exception as e:
        print("❌ SSL check failed:", e)
        return False


if __name__ == "__main__":
    check_ssl()
