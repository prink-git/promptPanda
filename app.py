import streamlit as st

from prompt_analyzer import analyze_prompt
from prompt_fixer import improve_prompt
from prompt_runner import run_prompt
from prompt_library import load_prompts, save_prompt
from utils import score_label


st.set_page_config(
    page_title="PromptPanda 🐼",
    page_icon="🐼",
    layout="wide"
)

st.title("🐼 PromptPanda")
st.caption("AI Prompt Debugger for LLM Developers")


st.subheader("Enter your prompt")

prompt = st.text_area("", height=120)


if st.button("Analyze Prompt"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt")

    else:

        score, issues = analyze_prompt(prompt)

        st.subheader("Prompt Quality")

        st.metric("Score", f"{score}/100")

        st.progress(score / 100)

        st.write(score_label(score))


        st.subheader("Issues Detected")

        if len(issues) == 0:
            st.success("No issues detected")

        else:
            for issue in issues:
                st.write(f"- {issue}")


        st.subheader("Improved Prompt")

        with st.spinner("PromptPanda improving your prompt..."):

            improved = improve_prompt(prompt)

        st.code(improved)


        st.subheader("Prompt Comparison")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Original Prompt")
            st.info(prompt)

        with col2:
            st.markdown("### Improved Prompt")
            st.success(improved)


        st.subheader("Run Prompt on LLM")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("Run Original Prompt"):

                with st.spinner("Running original prompt..."):
                    output1 = run_prompt(prompt)

                st.write(output1)

        with col2:

            if st.button("Run Improved Prompt"):

                with st.spinner("Running improved prompt..."):
                    output2 = run_prompt(improved)

                st.write(output2)


        if st.button("Save Improved Prompt"):

            save_prompt(improved)

            st.success("Prompt saved!")


st.divider()

st.subheader("📚 Prompt Library")

saved = load_prompts()

if len(saved) == 0:

    st.info("No prompts saved yet")

else:

    for p in saved:
        st.code(p)