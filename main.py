import streamlit as st
import speedtest
import pandas as pd


def test_internet_speed():
    st = speedtest.Speedtest()
    # st.get_best_server()
    download_speed = st.download() /8e6
    upload_speed = st.upload() /8e6  
    ping = st.results.ping

    return [download_speed,upload_speed,ping]



if __name__ == "__main__":

    st.write("Press the GO! button and wait for some time to see you network speed!")
    col1, col2, col3 = st.columns(3)
    with col2:
        but=st.button("GO!",use_container_width=True)
    ""
    ""
    if but:
        l=test_internet_speed()

        # table_data = [["Download Speed", "Upload Speed", "Ping"],[f"{l[0]:.2f}", f"{l[1]:.2f}", f"{l[2]:.2f}"]]
        # df = pd.DataFrame(table_data)
        # st.write(df)
        # st.table(df)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(f"Download Speed")
            st.write(f"{l[0]:.2f} MB/s", use_container_width=True)
        with col2:
            st.write(f"Upload Speed")
            st.write(f"{l[1]:.2f} MB/s", use_container_width=True)
        with col3:
            st.write(f"Ping")
            st.write(f"{l[1]:.2f} ms", use_container_width=True)


