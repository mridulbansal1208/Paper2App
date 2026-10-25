# 📐 Paper2App: Napkin Sketch to Live Prototype

An automated design-to-code tool powered by **Gemma 4** open-weights multimodal intelligence via the Gemini API.

---

## 🚀 Overview
**Paper2App** eliminates the manual bottleneck of converting physical whiteboard and paper brainstorms into functional code. By combining visual spatial reasoning with OCR, it transforms napkin sketches into:

1. **Interactive Prototypes:** Responsive mobile UI mockups styled with Tailwind CSS.
2. **Semantic Inventory:** Structural component breakdown and interaction mapping.
3. **Automated UX/Accessibility Audits:** Ergonomic evaluations (thumb-zone reachability, touch target dimensions, edge cases).

---

## 🛠️ Tech Stack
- **AI Model:** Gemma 4 Multimodal (`gemma-4-26b-a4b-it`)
- **API Runtime:** Google GenAI SDK (Gemini API)
- **Frontend:** Streamlit
- **Styling Engine:** Tailwind CSS
- **Image Preprocessing:** Pillow (PIL)

---

## 💡 How It Works
1. **Visual Ingestion:** Upload any phone photo of a sketch, whiteboard, or wireframe.
2. **Multimodal Disambiguation:** Gemma 4 parses spatial geometry and handwritten instructions, distinguishing UI text from design notes (e.g., recognizing that *"controls opacity"* is a functional slider spec rather than a text header).
3. **Code & Audit Generation:** Synthesizes responsive Tailwind CSS and highlights usability risks in a single inference pass.

---

## 📦 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/paper2app.git
cd paper2app

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set your Gemini API key
set GEMINI_API_KEY=your-gemini-api-key (in windows command prompt)

### 4. Run the Application
streamlit run hacktober.py
