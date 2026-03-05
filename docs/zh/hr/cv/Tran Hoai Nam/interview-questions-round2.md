# 二面問題 — Tran Hoai Nam（Technical Lead）

> 面試官：Ryan
> 日期：2026-03-__
> 總時間：~50 分鐘（9 題 + 候選人提問）

---

## 一面摘要與二面重點

| 一面觀察 | 二面驗證方向 |
|----------|-------------|
| Solo dev 心態，產品多為小規模 | 能否帶領團隊做大規模系統 |
| 技術深度不算特別強 | 面對複雜技術挑戰的應對方式 |
| 專案管理能力突出（8分） | 如何將 PM 能力轉化為 Tech Lead 價值 |
| 商業思維好，先想 business fit | 技術決策是否能兼顧長期架構 |
| 目前 gap time，非急找工作 | 對 Jarvis 的投入意願與長期規劃 |

---

## 一、Leadership（2 題，10 min）

### L1

🇹🇼 你在 HpTek 基本上是 Solo Builder，從架構到部署都自己來。如果今天你要把這套系統交給一個 5 人團隊來維護和擴展，你會怎麼拆分職責？你覺得最大的挑戰是什麼？

🇺🇸 At HpTek you've been essentially a Solo Builder — handling everything from architecture to deployment. If you had to hand this system over to a 5-person team to maintain and scale, how would you divide responsibilities? What do you think would be the biggest challenge?

🇻🇳 Ở HpTek, anh về cơ bản là Solo Builder — tự xử lý mọi thứ từ kiến trúc đến triển khai. Nếu anh phải chuyển giao hệ thống này cho một team 5 người để duy trì và mở rộng, anh sẽ phân chia trách nhiệm như thế nào? Anh nghĩ thách thức lớn nhất là gì?

---

### L2

🇹🇼 你在 FPT 帶過中小型團隊。當你同時管理資深和初階工程師時，你怎麼分配 code review 和技術決策的權限？你有沒有遇過資深工程師不認同你的技術方向的情況？

🇺🇸 At FPT you managed small to mid-sized teams. When managing both senior and junior engineers, how did you distribute code review and technical decision-making authority? Did you ever face a situation where a senior engineer disagreed with your technical direction?

🇻🇳 Ở FPT anh quản lý các team vừa và nhỏ. Khi quản lý cả senior và junior engineer, anh phân chia quyền code review và quyết định kỹ thuật như thế nào? Anh có từng gặp trường hợp senior engineer không đồng ý với hướng kỹ thuật của anh không?

---

## 二、專案開發構想（3 題，15 min）

### P1

🇹🇼 你的物流平台 Quanlylogi 目前年營收 $4M+。如果今天要把這個平台的流量擴大 10 倍，你的架構會需要做哪些改變？你會怎麼規劃這個技術遷移？

🇺🇸 Your logistics platform Quanlylogi currently generates $4M+ annual revenue. If you needed to scale traffic by 10x, what architectural changes would be required? How would you plan this technical migration?

🇻🇳 Nền tảng logistics Quanlylogi hiện đạt doanh thu hàng năm $4M+. Nếu cần mở rộng lưu lượng gấp 10 lần, kiến trúc cần thay đổi gì? Anh sẽ lên kế hoạch di chuyển kỹ thuật này như thế nào?

---

### P2

🇹🇼 一面提到你傾向先考慮 business fit，再考慮 scale。但如果你加入一個需要從第一天就設計成可擴展架構的專案，你會怎麼平衡「先求有」和「架構品質」？

🇺🇸 In the first interview, it was noted that you tend to prioritize business fit before scale. But if you joined a project that needed scalable architecture from day one, how would you balance "ship fast" with "architectural quality"?

🇻🇳 Trong vòng phỏng vấn đầu, có ghi nhận anh thường ưu tiên business fit trước khi nghĩ đến scale. Nhưng nếu anh tham gia một dự án cần kiến trúc có thể mở rộng ngay từ ngày đầu, anh sẽ cân bằng "ship nhanh" và "chất lượng kiến trúc" như thế nào?

---

### P3

🇹🇼 你在 HpTek 做的 B2B 物流平台，需要整合金融服務（保險、PVOIL、支付）。這種多方整合的系統，你是怎麼設計 API 和資料流的？遇到第三方 API 不穩定時你怎麼處理？

🇺🇸 Your B2B logistics platform at HpTek integrates financial services (insurance, PVOIL, payments). For this kind of multi-party integration system, how did you design the APIs and data flow? How do you handle unstable third-party APIs?

🇻🇳 Nền tảng logistics B2B ở HpTek tích hợp các dịch vụ tài chính (bảo hiểm, PVOIL, thanh toán). Với hệ thống tích hợp đa bên như vậy, anh thiết kế API và luồng dữ liệu như thế nào? Khi API bên thứ ba không ổn định, anh xử lý ra sao?

---

## 三、團隊管理風格（2 題，10 min）

### M1

🇹🇼 一面評估提到你的技術深度可能不是最強，當團隊成員提出很深的技術問題時，你會怎麼應對？你覺得 Tech Lead 一定要是團隊裡技術最強的人嗎？

🇺🇸 The first interview noted that your technical depth may not be the strongest. When team members raise deep technical questions, how do you handle it? Do you think a Tech Lead must be the most technically skilled person on the team?

🇻🇳 Vòng phỏng vấn đầu ghi nhận chiều sâu kỹ thuật của anh có thể chưa phải mạnh nhất. Khi thành viên trong team đặt ra câu hỏi kỹ thuật sâu, anh xử lý thế nào? Anh có nghĩ Tech Lead nhất thiết phải là người giỏi kỹ thuật nhất trong team không?

---

### M2

🇹🇼 你習慣一個人從頭做到尾，這是很強的能力。但帶團隊時，你怎麼克制自己不要「乾脆我自己來做比較快」的衝動？你有什麼具體方法來 delegate？

🇺🇸 You're used to building everything end-to-end yourself — that's a strong ability. But when leading a team, how do you resist the urge to think "it's faster if I just do it myself"? What specific methods do you use to delegate?

🇻🇳 Anh quen tự làm mọi thứ từ đầu đến cuối — đó là năng lực rất mạnh. Nhưng khi lead team, anh kiềm chế thôi thúc "thôi mình tự làm cho nhanh" như thế nào? Anh có phương pháp cụ thể nào để delegate không?

---

## 四、文化契合度（2 題，10 min）

### C1

🇹🇼 你在 HpTek 已經有自己的事業，也拿過 Zeroth.ai 和 VSV Capital 的投資。是什麼讓你考慮加入 Jarvis 而不是繼續自己做？你對下一份工作最看重什麼？

🇺🇸 You already have your own business at HpTek and have secured funding from Zeroth.ai and VSV Capital. What makes you consider joining Jarvis instead of continuing on your own? What do you value most in your next role?

🇻🇳 Anh đã có sự nghiệp riêng ở HpTek và đã nhận đầu tư từ Zeroth.ai và VSV Capital. Điều gì khiến anh cân nhắc gia nhập Jarvis thay vì tiếp tục tự làm? Anh coi trọng điều gì nhất trong công việc tiếp theo?

---

### C2

🇹🇼 Jarvis 是 AI 原生研發公司，我們用 AI Agent 驅動開發流程——從規劃、寫 code、測試到部署都有 AI 參與。以你在 AI 領域的經驗（GANs、Emotion Recognition），你會怎麼把 AI 融入日常開發工作流程，而不只是做 AI 產品？

🇺🇸 Jarvis is an AI-native development company — we use AI Agents to drive the development process, from planning to coding, testing, and deployment. With your AI experience (GANs, Emotion Recognition), how would you integrate AI into daily development workflows, beyond just building AI products?

🇻🇳 Jarvis là công ty phát triển AI-native — chúng tôi dùng AI Agent để thúc đẩy quy trình phát triển, từ lên kế hoạch, viết code, testing đến deployment. Với kinh nghiệm AI của anh (GANs, Emotion Recognition), anh sẽ tích hợp AI vào quy trình phát triển hàng ngày như thế nào, không chỉ là xây dựng sản phẩm AI?

---

## 面試節奏

| 區塊 | 題數 | 時間 |
|------|------|------|
| Leadership | 2 | 10 min |
| 專案構想 | 3 | 15 min |
| 管理風格 | 2 | 10 min |
| 文化契合 | 2 | 10 min |
| **候選人提問** | — | **5 min** |
| **合計** | **9 題** | **~50 min** |
