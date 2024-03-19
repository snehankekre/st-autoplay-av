import streamlit as st

st.subheader("POC of Autoplay Feature", divider="rainbow")

with st.expander("📜 **Context**", expanded=True):
    st.markdown("""
    We may introduce an autoplay feature for for `st.audio` and `st.video`. Here's what you need to know:

    - **Initial Autoplay**: On your first visit, audio and video will autoplay. Read the next two points to understand why it didn't just autoplay and how to enable it.
    - **Enabling Autoplay**: Due to browser restrictions on autoplay, you might need to interact with the page (e.g., a quick click anywhere) as it loads to enable this feature.
    - **Troubleshooting Autoplay**: If autoplay isn't working as expected, reopen the app in a new tab and click anywhere on the page **while it loads** or hard refresh the page (Cmd + Shift + R or Ctrl + F5) and furiously click anywhere on the page as it loads.

    ##### Understanding Autoplay Behavior:

    **Single Tab, Multiple Reruns**:
      - On the initial run, audio and video content autoplays.
      - If you interact with the app, causing reruns (e.g., through button clicks), autoplay will not trigger again to prevent disruption.
      - Specifically, clicking the "Delete" or "Show" buttons adds new elements above the AV components. This action counts as a rerun, but does not cause the AV components to autoplay again, respecting your initial interaction.

    **New Tab or Window**:
      - A fresh start in a new tab or window allows audio and video to autoplay once more, adhering to the user's expectation of a new session.

    This feature is designed to balance seamless content engagement with user control, adhering to browser policies and ensuring a non-intrusive experience. Enjoy!
    """)

with st.echo(code_location="below"):
    if st.button("Delete"):
        st.write("Deleting...")

    st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav", autoplay=True, end_time=10)

    if st.button("Show"):
        st.write("Showing...")

    st.video("https://static.streamlit.io/examples/star.mp4", autoplay=True)
