# Multilingual-voice-cloner

A production-ready web interface for OmniVoice running on NVIDIA GPUs with Gradio.

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
