import speedtest

def network():
    st = speedtest.Speedtest()

    st.get_best_server()

    download = st.download()
    upload = st.upload()

    download_speed_mbps = download / 1_000_000
    upload_speed_mbps = upload / 1_000_000
    print(f"\nBasic Stats:")
    print(f"Download speed: {download_speed_mbps:.2f} Mbps")
    print(f"Upload speed: {upload_speed_mbps:.2f} Mbps")
