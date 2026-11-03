import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
app = Flask(__name__)

SYSTEM_PROMPT = """
คุณคือ JES AI ผู้ช่วยอัจฉริยะส่วนตัว พูดภาษาไทยอย่างสุภาพ ชัดเจน และเป็นมิตร
ช่วยคิด วิเคราะห์ อธิบาย เขียนเอกสาร สร้างคอนเทนต์ และช่วยงานทั่วไป
หากข้อมูลไม่แน่ใจ ให้บอกตรง ๆ และอย่าสร้างข้อเท็จจริงขึ้นเอง
ตอบเป็นหัวข้อหรือขั้นตอนเมื่อเหมาะสม
"""

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        return jsonify({"error": "ยังไม่ได้ตั้งค่า GEMINI_API_KEY กรุณาทำตามคู่มือใน README"}), 400

    data = request.get_json(silent=True) or {}
    messages = data.get("messages", [])
    if not isinstance(messages, list) or not messages:
        return jsonify({"error": "กรุณาพิมพ์ข้อความก่อนส่ง"}), 400

    # ส่งบทสนทนาล่าสุดไปให้โมเดล เพื่อให้ต่อเนื่องในแต่ละรอบ
    transcript = []
    for item in messages[-20:]:
        role = "ผู้ใช้" if item.get("role") == "user" else "JES AI"
        content = str(item.get("content", ""))[:12000]
        if content.strip():
            transcript.append(f"{role}: {content}")

    prompt = SYSTEM_PROMPT + "\n\nบทสนทนา:\n" + "\n".join(transcript) + "\n\nJES AI:"
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite"),
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.7)
        )
        answer = (response.text or "").strip()
        if not answer:
            answer = "ขออภัย ระบบยังไม่สามารถสร้างคำตอบได้ ลองถามอีกครั้งนะครับ"
        return jsonify({"reply": answer})
    except Exception as exc:
        # ไม่ส่งรายละเอียดลับหรือ API key กลับไปยังหน้าเว็บ
        print("Gemini API error:", repr(exc))
        return jsonify({"error": "เชื่อมต่อ AI ไม่สำเร็จ กรุณาตรวจสอบ API Key, อินเทอร์เน็ต และโควตา Gemini"}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
