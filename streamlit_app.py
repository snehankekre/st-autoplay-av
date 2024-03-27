import streamlit as st

st.subheader("POC of Autoplay Feature", divider="rainbow")

with st.expander("📜 **Context**", expanded=True):
    st.markdown(
        """
    We may introduce an autoplay feature for `st.audio` and `st.video`. Here's what you need to know:

    - **Initial autoplay**: On your first visit, audio and video will autoplay. Read the next two points to understand why it didn't just autoplay and how to enable it.
    - **Enabling autoplay**: Due to browser restrictions on autoplay, you might need to interact with the page (e.g., a quick click anywhere) as it loads to enable this feature.
    - **Troubleshooting autoplay**: If autoplay isn't working as expected, reopen the app in a new tab and click anywhere on the page **while it loads** or hard refresh the page (Cmd + Shift + R or Ctrl + F5) and furiously click anywhere on the page as it loads.

    ##### Understanding autoplay behavior:

    **Single Tab, Multiple Reruns**:
      - On the initial run, audio and video content autoplays.
      - If you interact with the app, causing reruns (e.g., through button clicks), autoplay will not trigger again to prevent disruption.
      - Specifically, clicking the "Delete" or "Show" toggle adds new elements above the AV components. This action counts as a rerun, but does not cause the AV components to autoplay again, respecting your initial interaction.

    **New Tab or Window**:
      - A fresh start in a new tab or window allows audio and video to autoplay once more, adhering to the user's expectation of a new session.

    This feature is designed to balance seamless content engagement with user control, adhering to browser policies and ensuring a non-intrusive experience. Enjoy!
    """
    )

with st.echo(code_location="below"):
    col1, col2 = st.columns([1, 5])
    autoplay = col1.checkbox("Autoplay", value=True)
    loop = col2.checkbox("Loop", value=False)
    if st.toggle("Delete"):
        st.write("Deleting...")

    st.audio(
        "https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav",
        autoplay=autoplay,
        end_time=6,
        loop=loop,
    )

    if st.toggle("Show"):
        st.write("Showing...")

    st.video(
        "https://static.streamlit.io/examples/star.mp4", autoplay=autoplay, loop=loop
    )


with st.expander("How does this work?", expanded=False):
    st.markdown(
        """
    The solution is to use similar logic as we use for widgets in this case, but without adding a `key` parameter. 
    
    Basically, we calculate an ID based on the command parameters, and use this ID to store state of the frontend component outside of the component. If the component unmounts and mounts again, we reconstruct the state based on the ID.
    
    See the implementation [here](https://github.com/streamlit/streamlit/compare/develop...snehan/feature/autoplay-video-audio). :point_left:
    """
    )
