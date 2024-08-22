import speedtest
import os

def clearing():
    os.system("cls" if os.name == 'nt' else "clear")

def network():
    st = speedtest.Speedtest()

    st.get_best_server()

    server = st.get_best_server()
    print(f"Connected to {server['host']} located in {server['country']}")

    download = st.download()
    upload = st.upload()
    ping = st.results.ping

    download_speed_mbps = download / 1_000_000
    upload_speed_mbps = upload / 1_000_000
    print(f"\nNetwork Speed Stats:")
    print(f"Download speed: {download_speed_mbps:.2f} Mbps")
    print(f"Upload speed: {upload_speed_mbps:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

def main():
    clearing()
    network()
