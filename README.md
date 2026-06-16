# Multilingual-voice-cloner

A production-ready web interface for OmniVoice running on NVIDIA GPUs with Gradio.

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/Abhishek-DS-ML-Gupta/Multilingual-voice-cloner.git

cd Multilingual-voice-cloner
```

---

## Create Virtual Environment

### Linux / Ubuntu

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

## Install CUDA PyTorch (RTX A6000)

For CUDA-enabled NVIDIA GPUs, install the appropriate PyTorch build before running the application. CUDA support is required for optimal TTS inference performance.

Example:

```bash
pip install torch torchvision torchaudio \
--index-url https://download.pytorch.org/whl/cu128
```

Verify:

```bash
python -c "import torch; print(torch.cuda.is_available())"
```

Expected Output:

```text
True
```

---

## Download Model

The application automatically downloads OmniVoice model weights during first launch.

Model:

```text
k2-fsa/OmniVoice
```

The initial startup may take several minutes depending on internet speed.

---

## Launch Application

```bash
python main.py
```

Server starts at:

```text
http://localhost:7860
```

For remote servers:

```text
http://YOUR_SERVER_IP:7860
```

---

# 🖥 Ubuntu Server Deployment

## Open Firewall Port

```bash
sudo ufw allow 7860/tcp

sudo ufw reload
```

---

## Run in Background

```bash
nohup python main.py > omnivoice.log 2>&1 &
```

Check logs:

```bash
tail -f omnivoice.log
```

---

# 🐳 Docker Deployment

Build image:

```bash
docker build -t omnivoice .
```

Run container:

```bash
docker run \
--gpus all \
-p 7860:7860 \
omnivoice
```

---

# ⚙️ Production Deployment

Recommended stack:

```text
Ubuntu 22.04
Python 3.10+
CUDA 12+
NVIDIA RTX A6000 48GB
Nginx Reverse Proxy
SSL Certificate
Systemd Service
```

---

# 🎤 Usage

## Voice Cloning

1. Upload reference audio
2. Enter transcript of reference audio
3. Enter target text
4. Click Generate

---

## Cross-Lingual Voice Cloning

Example:

Reference Voice:

```text
Hindi
```

Target Text:

```text
English
```

Output:

```text
English speech with cloned Hindi voice
```

---

## Multilingual Generation

Supports 646+ languages covered by OmniVoice training data.

Examples:

* English
* Hindi
* Marathi
* Gujarati
* Bengali
* Tamil
* Telugu
* Kannada
* Malayalam
* Punjabi
* Urdu
* Arabic
* Chinese
* Japanese
* Korean
* French
* German
* Spanish
* Russian
* Portuguese
* Italian

and many more.

---

# 🔥 RTX A6000 Optimization

Recommended launch:

```bash
export CUDA_VISIBLE_DEVICES=0

export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512

python main.py
```

---

# 📊 System Requirements

Minimum:

```text
RTX 3090 24GB
32GB RAM
8 CPU Cores
```

Recommended:

```text
RTX A6000 48GB
64GB RAM
16 CPU Cores
Ubuntu 22.04
CUDA 12+
```

---

# 🧪 Health Check

Verify GPU:

```bash
nvidia-smi
```

Verify CUDA:

```bash
python -c "import torch; print(torch.cuda.get_device_name(0))"
```

Verify Gradio:

```bash
curl http://localhost:7860
```

---

# 🛑 Troubleshooting

## CUDA Not Found

```bash
nvidia-smi
```

Ensure NVIDIA drivers and CUDA are correctly installed.

---

## Out of Memory

Use FP16 inference:

```python
dtype=torch.float16
```

---

## Slow Generation

Ensure generation runs on GPU:

```python
device_map="cuda:0"
```

## ✨ Features

### 🎤 Zero-Shot Voice Cloning

Clone any voice using only a few seconds of reference audio.

### 🌍 646+ Language Support

Generate speech in over 646 languages supported by OmniVoice.

### 🔄 Cross-Lingual Voice Cloning

Use a reference voice from one language and synthesize speech in another language while preserving speaker identity.

Example:

* Reference Audio: Hindi

* Generated Speech: English

* Reference Audio: English

* Generated Speech: Marathi

### 🗣️ Multilingual Text-to-Speech

Generate speech directly from text in supported languages.

### 🎭 Voice Design

Create entirely new synthetic voices without reference audio.

### 😊 Emotion-Aware Speech Generation

Generate expressive speech with varying speaking styles and emotions when supported by the model.

### 🔊 High-Quality Audio Output

24 kHz speech synthesis optimized for naturalness and speaker similarity.

### 🎚️ Adjustable Generation Parameters

* Temperature
* Top-P Sampling
* Guidance Scale
* Seed Control
* Speed Control

### 📁 Audio Upload Support

Supported formats:

* WAV
* MP3
* FLAC
* OGG
* M4A

### ✂️ Automatic Audio Processing

* Silence Removal
* Audio Normalization
* Volume Balancing
* Sample Rate Conversion

### 📝 Automatic Speech Transcription

Optional Whisper integration for extracting transcripts from reference audio.

### 🌐 Language Auto Detection

Automatically detect source language of reference audio.

### ⚡ GPU Acceleration

Optimized for:

* RTX A6000
* RTX 4090
* A100
* H100
* L40S

### 🔥 FP16 Inference

Reduced VRAM usage and faster generation using mixed precision.

### 👥 Multi-User Support

Concurrent request processing using Gradio Queue.

### 📜 Generation History

Store and replay previously generated speech.

### 💾 Download Generated Audio

Download generated WAV files directly from the interface.

### 🐳 Docker Support

One-command deployment using Docker.

### 🔐 Authentication

Optional login protection for private deployments.

### 📊 Monitoring Dashboard

Track:

* GPU Usage
* VRAM Usage
* Queue Length
* Generation Time

### ☁️ Reverse Proxy Support

Compatible with:

* Nginx
* Traefik
* Cloudflare Tunnel

### 🔄 REST API

Generate speech programmatically.

Endpoints:

* /generate
* /clone
* /health

### 📦 Batch Generation

Generate multiple audio files in a single request.

### 🚀 Streaming Audio Generation

Play generated audio while synthesis is still running.

### 🎯 Speaker Management

* Save Speakers
* Rename Speakers
* Delete Speakers
* Speaker Library

### 🔍 Advanced Search

Search generated audio and saved speakers.

### 🌙 Modern UI

Built using:

* Gradio
* Responsive Layout
* Dark Mode
* Mobile Friendly Interface

## 🖥 Recommended Hardware

### Production

* NVIDIA RTX A6000 48GB
* CUDA 12+
* 16+ CPU Cores
* 64GB RAM
* Ubuntu 22.04

### Minimum

* RTX 3090 24GB
* 32GB RAM

## 📈 Performance (RTX A6000)

Expected:

* 10–20 concurrent users
* FP16 inference
* Fast multilingual generation
* Low latency voice cloning

## ⚠ Disclaimer

This project must not be used for unauthorized voice impersonation, fraud, scams, or illegal activities. Users are responsible for complying with applicable laws and regulations.


---

# 📜 License

This project uses OmniVoice.

Users must not use this software for unauthorized voice impersonation, fraud, scams, or illegal activities.

