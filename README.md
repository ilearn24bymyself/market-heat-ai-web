# 台股資金動能分析 PRO - 雲端網頁版 (Streamlit)

原本的 05 版是一個 Flask 工具，現在已升級為 **05-1 雲端強化版**。本工具可以自動聚合各大財經媒體的新聞，並生成適合 AI 分析的指令，幫助交易者快速掌握資金流向。

## 🚀 核心功能
- **即時新聞聚合**：整合 Yahoo 股市、鉅亨網、經濟日報、MoneyDJ、玩股網等 5 大來源。
- **AI 指令生成**：預設專業的系統提示詞，一鍵生成包含即時新聞內容的 Markdown 指令。
- **互動式儀表板**：直觀顯示新聞標題、來源與摘要，支援關鍵字過濾。
- **雲端相容性**：專為 Streamlit Cloud 設計，免伺服器維護，隨點隨用。

## 📂 資料夾結構 (05-1 版)
- `streamlit_app.py`: Web 主程式，處理 UI 與 Prompt 拼接。
- `scrapers.py`: 核心爬蟲引擎，負責抓取各大媒體 RSS 或 API。
- `requirements.txt`: 雲端環境依賴檔。
- `run_streamlit.bat`: 本地測試腳本。

## 🛠️ 下一次開發/修改指南

### 1. 調整 AI 提示詞 (System Prompt)
若您想要改變 AI 分析的角度（例如增加個股籌碼分析、或是要求簡短一點），可以直接在 `streamlit_app.py` 的 `system_prompt_template` 變數中修改。

### 2. 增加新聞來源
在 `scrapers.py` 中新增一個 `scrape_xxx()` 函數，並將其加入 `get_all_news()` 的列表中即可。

## 📝 部署紀錄 (2026-04-20)
1. **GitHub 倉庫**: 建議建立新倉庫 `market-heat-ai-web`。
2. **分支**: `main`
3. **平台**: Streamlit Community Cloud
4. **注意事項**: 
   - 由於涉及即時抓取，請確保 Streamlit Cloud 下載了所有依賴（bs4, feedparser）。
   - 若網站載入過慢，可檢查個別爬蟲的 Timeout 設定。
