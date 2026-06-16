```python
import os
import uuid
import torch
import gradio as gr
import soundfile as sf
from omnivoice import OmniVoice

# =========================
# CONFIG
# =========================

MODEL_NAME = "k2-fsa/OmniVoice"

DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
DTYPE = torch.float16 if torch.cuda.is_available() else torch.float32

print(f"Loading {MODEL_NAME} on {DEVICE}")

model = OmniVoice.from_pretrained(
    MODEL_NAME,
    device_map=DEVICE,
    dtype=DTYPE
)

os.makedirs("outputs", exist_ok=True)

# =========================
# GENERATION
# =========================

def clone_voice(
    text,
    ref_audio,
    ref_text,
):
    try:

        audio = model.generate(
            text=text,
            ref_audio=ref_audio,
            ref_text=ref_text
        )

        output_file = f"outputs/{uuid.uuid4().hex}.wav"

        sf.write(
            output_file,
            audio[0],
            24000
        )

        return output_file, "Generation Complete"

    except Exception as e:
        return None, str(e)

# =========================
# THEME
# =========================

css = """
.gradio-container{
    max-width:1400px !important;
}

footer{
    display:none !important;
}

h1{
    text-align:center;
}
"""

# =========================
# UI
# =========================

with gr.Blocks(
    title="OmniVoice Demo",
    css=css,
    theme=gr.themes.Soft()
) as demo:

    gr.Markdown("""
    # OmniVoice Demo

    State-of-the-art text-to-speech model supporting:

    - Voice Clone
    - Multilingual TTS
    - Cross-lingual Voice Cloning
    - 600+ Languages
    """)

    with gr.Tabs():

        # =====================
        # VOICE CLONE
        # =====================

        with gr.Tab("🎤 Voice Clone"):

            with gr.Row():

                with gr.Column(scale=2):

                    text_input = gr.Textbox(
                        label="Text to Synthesize",
                        lines=6,
                        placeholder="Enter text..."
                    )

                    reference_audio = gr.Audio(
                        type="filepath",
                        label="Reference Audio"
                    )

                    reference_text = gr.Textbox(
                        label="Reference Text (Optional)",
                        lines=3
                    )

                    generate_btn = gr.Button(
                        "Generate",
                        variant="primary"
                    )

                with gr.Column(scale=1):

                    output_audio = gr.Audio(
                        label="Output Audio"
                    )

                    status_box = gr.Textbox(
                        label="Status"
                    )

            generate_btn.click(
                fn=clone_voice,
                inputs=[
                    text_input,
                    reference_audio,
                    reference_text
                ],
                outputs=[
                    output_audio,
                    status_box
                ]
            )

        # =====================
        # ABOUT
        # =====================

        with gr.Tab("ℹ️ About"):

            gr.Markdown("""
            ## OmniVoice

            Features:

            - Zero-Shot Voice Cloning
            - Cross-Lingual Voice Cloning
            - Multilingual Speech Synthesis
            - GPU Acceleration
            - RTX A6000 Optimized

            Model:
            k2-fsa/OmniVoice
            """)

demo.queue(max_size=50)

demo.launch(
    server_name="0.0.0.0",
    server_port=7860,
    share=False
)
```
