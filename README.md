# CircGen-AI: The Logisime Code Generator

**CircGen-AI** is a project dedicated to fine-tuning a large language model (LLM) to automatically generate digital logic circuit files (`.circ`) for Logisim Evolution from plain English descriptions. The ultimate goal is to create an intelligent agent capable of assisting with digital logic design tasks.

## Project Goal

The primary objective is to take a natural language prompt, such as "Create a 4-bit full adder", and have the AI generate a complete, functional, and valid `.circ` file that can be opened and simulated in Logisim Evolution.

## Core Technologies

- **Model**: `google/gemma-2b-it`
- **Technique**: Instruction Fine-Tuning with LoRA
- **Platform**: Hugging Face Ecosystem (`transformers`, `peft`, `datasets`)
- **Environment**: Google Colab

## Project Status: 🚀 Phase 1 - Setup

This section will be updated as the project progresses.

- [x] Repository created and structured.
- [ ] Initial dataset created with a single AND gate.
- [ ] Fine-tuning pipeline built and tested in Colab.
- [ ] First model adapters saved to Hugging Face Hub.

## Roadmap (August 2025)

- **Week 1: Build the Greenhouse.**

  - [ ] Set up the full end-to-end fine-tuning pipeline with a single data point.

- **Week 2: Expand the Diet.**

  - [ ] Collect data for all basic combinational logic gates (AND, OR, NOT, MUX).
  - [ ] Re-train and evaluate the model's ability to generate these components.

- **Week 3: Getting More Complex.**

- [ ] Add arithmetic and memory circuits (Adders, Flip-Flops) to the dataset.

- **Week 4: The ALU Challenge.**

- [ ] Attempt to generate a complete 1-bit ALU and then an 8-bit ALU.

## How to Use

(This section will be filled out later once the first model is trained and available on the Hugging Face Hub.)

1. Load the fine-tuned model from the Hub.
2. Provide a prompt describing the desired circuit.
3. Save the generated XML output as a .circ file.
4. Open and test the file in Logisim Evolution.

---
Building with ❤️ and contribution is most welcomed...
