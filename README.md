# 🤖 Simple WhatsApp Bot to-my-phone (Archived)

![Status](https://img.shields.io/badge/Status-Abandoned-red?style=flat-square)
![Reason](https://img.shields.io/badge/Reason-Cost%20Constraints-orange?style=flat-square)
![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)

A mini-project aimed at building a lightweight WhatsApp automation bot to-my-phone. This repository is **archived and no longer actively maintained**.

---

## 📌 Project Overview

The objective was to build a functional, straightforward WhatsApp bot capable of handling automated responses and user queries. 

While the core logic was right, the project was sunset after evaluating the long-term infrastructure and API messaging costs required to keep it live (NOT FREE ANYMORE).

---

## 🚫 Why Was This Project Discontinued?

Maintaining a production-ready WhatsApp bot requires third-party API services (such as the Meta WhatsApp Business API or paid gateway proxies). 

- **Commercial/Paid APIs:** Essential features like official API access, webhook hosting, and high-volume message delivery require paid subscriptions.
- **Sustainability:** As an exploratory side project, continuing to pay monthly API/hosting fees was not financially practical.
- **Free Tier Limitations:** Free alternatives or unofficial scraping wrappers proved either unstable or violated platform terms of service.

Rather than maintaining a broken or costly demo, the decision was made to halt development and archive the code.

---

## 🧠 Key Takeaways & Lessons Learned

Despite being discontinued, this project provided valuable practical experience:

1. **API Cost Modeling:** Understood the financial realities of building on top of proprietary ecosystem APIs (Meta / WhatsApp).
2. **Third-Party Integration:** Gained experience handling webhook payloads, authentication headers, and request routing.
3. **Architecture Decisions:** Learned when to pivot or cut losses when infrastructure requirements exceed initial budget constraints.

---

## 🛠️ Built With

- **Python** (Core backend logic)
- **Flask**
- **Twilio WhatsApp API**