import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("grassField.jpg", caption="Touchez les gazons", width=300)

    st.write("[My GitHub](google.com)")

with col2:
    st.header("A propos Moi")
    st.text("Je m'appelle Aaron. J'ai 14 ans et je pense que tu es us singe")
    st.write("🐒🙈🙉🙊🐵🍌🍌🍌🍌🍌")


# ---------- Sidebar Navigation ----------
tabs = st.sidebar.radio("My Projects", ["About me", "My Games"])

# ---------- My Games Section ----------
if tabs == "About me":
    st.header("My skills")
    st.write("I am currently learning how to use Streamlit, python, and c#. Hopefully I'll be able to be proficient"
             " enough to use them without help.")
    st.markdown(" ")
    st.write("My skills in python /100")
    my_bar = st.progress(90, text='Python')

    st.markdown(" ")

    st.subheader("My interests and Hobbies")
    st.markdown("""
    - 🖥️ Coding
    - 🖨️ 3D Printing
    - 🖥️⌨️ Computer Assembly
    - 🏒 Hockey
    - 🔬 Science""")
elif tabs == "My Games":
    game_tabs = st.tabs(["Scuffed Asteroids", "2D Survival", "Demo Game"])

    # --- Skippy Game ---
    with game_tabs[0]:
        st.subheader("Scuffed Asteroids") #name of game
        st.components.v1.iframe("https://lagg-ing.github.io/Asteroid-Replica/",height=600,width=960)
        st.link_button("🔗 GitHub Repository", "https://github.com/lagg-ing/Asteroid") #link to source code

    with game_tabs[1]:
        st.subheader("2D Survival")
        st.components.v1.iframe("https://lagg-ing.github.io/2D-Survival",height=600,width=960)
        st.link_button("🔗 GitHub Repository", "https://github.com/lagg-ing/2D-Survival-Source-Code")

    with game_tabs[2]:
        st.subheader("Demo Game")
        st.components.v1.iframe("https://lagg-ing.github.io/Demo-Game",height=600,width=960)
        st.link_button("🔗 GitHub Repository", "https://github.com/lagg-ing/Demo-Game")
    with game_tabs[3]:
        st.subheader("3D Game Test")
        st.components.v1.iframe("https://lagg-ing.github.io/3D-Game-Design-Test", height=600, width=960)