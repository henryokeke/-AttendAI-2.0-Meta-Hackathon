# AttendAI 2.0 - Meta Global AI Developer Hackathon
> Built NEW between Oct 26 - Nov 4, 2025 for Meta Global AI Developer Hackathon

### [Live Demo] | [Video Demo (2 min)] | Public Repo

**Tagline:** No more fake attendance. Real students, real data.

### The Problem
In rural schools in Anambra where we (Elites Team) taught 200+ students, attendance is faked by proxy - one student marks for 5 friends. Lecturers have no real data.

### The Solution
AttendAI 2.0 - An AI attendance system with:
1.  **Anti-Proxy:** Liveness detection + Voice Print + Device/Location check
2.  **Smart Analytics:** Llama-powered insights - "Who is at-risk? Why is Friday low?"
3.  **Voice Support:** Mark attendance by saying "I dey here" in Igbo, Pidgin, English - works offline

### 🆕 What We Built DURING This Hackathon (Oct 26 - Nov 4)
To comply with "New Work Only" rule, ALL of this was built fresh during the hackathon:
- [ ] New FastAPI backend with Llama 3 integration
- [ ] Liveness check model (anti-photo spoofing)
- [ ] Voice verification with Whisper + Llama
- [ ] Analytics dashboard with Llama summarization
- [ ] PWA for low-network classrooms

*All commits in this repo are from the hackathon period. Previous AttendAI v1 was not reused.*

### Tech Stack
- **AI:** Llama 3.2 (via Fireworks AI / Baseten), Whisper
- **Backend:** Python FastAPI, Supabase
- **Frontend:** React PWA
- **Infra:** Modal for deployment

### Architecture
[Student Phone] -> Face Liveness + Voice -> FastAPI -> Llama Verification -> Supabase -> Lecturer Dashboard

### How to Run Locally
```bash
git clone https://github.com/your-username/AttendAI-2.0-Meta-Hackathon
pip install -r requirements.txt
uvicorn main:app --reload
