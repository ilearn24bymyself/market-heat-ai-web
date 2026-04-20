# 開發與部署日誌 - 05-1 網頁版 (2026-04-20)

## ✅ 今日完成功能
1.  **專案解耦與轉移**：
    - 將原有的 `05_Market_Heat_AI` (Flask) 邏輯抽離，於 `05-1_Market_Heat_Web` 建立全新的 Streamlit 專案。
2.  **爬蟲引擎最佳化 (scrapers.py)**：
    - 修復並優化了 5 個新聞來源的抓取邏輯。
    - 統一新聞輸出格式 (Title, Source, Summary, Link)。
3.  **網頁儀表板建置 (streamlit_app.py)**：
    - 實作了互動式側邊欄，允許使用者自定義 AI 系統提示詞。
    - 整合了 `st.code` 區塊，方便使用者一鍵複製龐大的 AI 提示詞。
    - 使用 `st.dataframe` 展示原始新聞數據，供使用者參考。
4.  **雲端部署準備**：
    - 建立了 `requirements.txt` 以支援 Streamlit Cloud 的自動環境建置。
    - 提供了 `run_streamlit.bat` 供使用者在 Windows 本地快速測試。

## 🛠️ 下一次開發方向
- **AI 整合**：如果使用者願意在 Streamlit 秘密設定中提供 API Key，可以直接在網頁上調用 ChatGPT API 進行自動總結，不必再手動複製貼上。
- **情感分析**：在爬蟲階段加入關鍵字情感分析 (Sentiment Analysis)，為新聞自動標註多空屬性。
