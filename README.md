# JES AI — Local Web App

โปรแกรมผู้ช่วย AI ภาษาไทย ทำงานบนคอมพิวเตอร์ผ่านเว็บเบราว์เซอร์ โดยใช้ Gemini API

## สิ่งที่ต้องมี
- Windows 10/11 หรือ macOS/Linux
- Python 3.10 ขึ้นไป
- อินเทอร์เน็ต
- Gemini API Key จาก https://aistudio.google.com/app/apikey

## วิธีติดตั้งบน Windows
1. ติดตั้ง Python จาก https://www.python.org/downloads/ และเลือก Add Python to PATH
2. แตกไฟล์ ZIP นี้
3. ดับเบิลคลิก `start_windows.bat`
4. เมื่อไฟล์ `.env` เปิดขึ้น ให้วาง API Key หลัง `GEMINI_API_KEY=`
5. บันทึกไฟล์ แล้วรัน `start_windows.bat` อีกครั้ง
6. เปิดเบราว์เซอร์ไปที่ http://127.0.0.1:5000

## วิธีติดตั้งบน macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```
แก้ไฟล์ `.env` เพื่อใส่ API Key แล้วรัน:
```bash
python app.py
```
เปิด http://127.0.0.1:5000

## ความปลอดภัย
- อย่าแชร์ไฟล์ `.env` หรือ API Key ให้ผู้อื่น
- อย่าอัปโหลด `.env` ขึ้น GitHub
- รุ่นเริ่มต้นนี้เหมาะสำหรับใช้งานส่วนตัวบนเครื่อง ไม่ควรเปิดสู่สาธารณะโดยไม่มีระบบล็อกอินและการจำกัดการใช้งาน

## หมายเหตุเรื่องค่าใช้จ่าย
ตัวโปรแกรมและไลบรารีเป็นซอฟต์แวร์ที่ใช้ฟรี แต่การเรียก Gemini API มีโควตาและข้อกำหนดตามบัญชี/ภูมิภาค/รุ่นโมเดล โปรดตรวจสอบหน้า Pricing และ Usage ของ Google ก่อนใช้งานจริง

## ติดตั้งเป็นแอป (PWA)
เมื่อ JES AI ถูกนำขึ้นโฮสต์ที่รองรับ HTTPS แล้ว:
- Android/Chrome: เปิดเว็บไซต์ > เมนู > Install app / Add to Home screen
- iPhone/Safari: เปิดเว็บไซต์ > Share > Add to Home Screen

หมายเหตุ: การติดตั้ง PWA ต้องใช้ HTTPS หรือ localhost


## Deploy on Render
This project includes `render.yaml` for Render Blueprint deployment.
1. Push the complete project folder contents to a GitHub repository.
2. In Render, choose New > Blueprint and connect that repository.
3. Enter your Gemini API key as the `GEMINI_API_KEY` secret when prompted.
4. Deploy. Keep the API key out of GitHub.
