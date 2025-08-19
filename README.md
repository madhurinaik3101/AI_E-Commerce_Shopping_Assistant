# AI-E-Commerce-Shopping-Assistant

## Table of Contents

- [Overview](#overview)
- [Situation](#situation)
- [Task](#task)
- [Action](#action)
- [Result](#results)    
- [Technologies Used](#technologies-used)  

## Overview

Ms.Worldwide is a personalized, multi-turn AI shopping assistant that helps customers discover and purchase makeup, shoes, clothes, and electronics with context-aware, relevant recommendations. Unlike typical assistants that give generic, impersonal responses, Ms.Worldwide retains conversation context and interacts naturally, acting like a trusted shopping companion.

Built using LLaMA-4 Maverick-17B-128F-Instruct-FP8 and deployed with the Azure AI Foundry Python SDK, this project showcases LLM evaluation, prompt engineering, and scalable enterprise AI deployment.

## Situation

I was inspired by Amazon’s Rufus, which makes online shopping smoother, but I wanted something even smarter: a personal assistant that could help me find the best options across the web, without being overwhelming, generic, or context-losing. I envisioned Ms.Worldwide as a virtual shopping companion that talks to me like my “inner shopping friend” — personalized, attentive, and helpful — instead of being a frustrating, one-size-fits-all assistant.

## Task 

Develop a multi-turn AI assistant that empowers customers to make informed purchasing decisions across makeup, shoes, clothing, and electronics, while ensuring cost efficiency and scalability for enterprise use.

## Action

1. Benchmarked GPT-4o against LLaMA-4 Maverick-17B-128F-Instruct-FP8, comparing latency, cost, and contextual accuracy.
2. Selected LLaMA for its faster response times and lower cost, making it better suited for high-volume retail use cases.
3. Developed the assistant in Azure Cloud Shell using the Azure AI Foundry SDK with secure project-based inference.
4. Grounded the assistant with a system prompt:
“You are a Sales AI assistant that helps customers buy makeup, shoes, clothes, and electronics.”
5. Implemented conversation history retention to enable natural, multi-turn dialogues.


## Result

1. Delivered a Customer-Facing AI E-commerce Shopping Assistant that provides end-to-end personalized, friendly, and data-driven shopping recommendations instead of generic answers.
2. Achieved **~30% faster responses** and **~25% lower operational cost**, making the Assistant practical for small-to-large enterprise e-commerce platforms.


---

## Technologies Used

1. Language Model: LLaMA-4 Maverick-17B-128F-Instruct-FP8
2. Cloud AI Platform: Azure AI Foundry
3. Python SDKs:
    a. azure-ai-inference (Model Inference API)
    b. azure-ai-projects
    c. azure-core (optional if using credentials)
    d. python-dotenv (environment variable management)
4. Development Environment: Azure Cloud Shell / Local Python
5. Version Control & Hosting: Git & GitHub

--
