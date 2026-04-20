import streamlit as st
import pandas as pd
from scrapers import get_all_news
import time

# --- Page Config ---
st.set_page_config(page_title="台股資金動能分析 PRO", layout="wide")

# --- Custom Styling ---
st.markdown("""
<style>
    .main { background-color: #0d1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #238636; color: white; border: none; }
    .stButton>button:hover { background-color: #2ea043; border: none; }
    .news-card { border-radius: 10px; padding: 15px; margin-bottom: 10px; background-color: #161b22; border: 1px solid #30363d; }
    .source-tag { background: #1f6feb; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8rem; margin-right: 10px; }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("🛠️ 設定")
system_prompt_template = st.sidebar.text_area("AI 系統提示詞 (System Prompt)", height=300, value="""你是一位精準的「台灣股市動能交易與籌碼分析師」。
請仔細閱讀我提供的【今日台股重點新聞列表】。
你的任務是「找出目前資金、新聞與散戶正在瘋狂湧入的族群與個股熱點」。我不看未來價值，我只要看當下市場的資金動能往哪裡擠。

請幫我整理成一個極簡的 markdown 表格，方便我快速閱讀。
表格必須包含以下五個欄位：
1. 股票名稱/代號
2. 漲跌表現 (如果有提到)
3. 新聞多空摘要 (重點節錄即可)
4. 所屬熱門族群 (如：矽光子、散熱、機器人)
5. 參考新聞連結

請列出前 10-15 檔最熱門個股。
並在表格下方，用 100 字簡短總結今天「資金流向的共識」。
""")

st.sidebar.markdown("---")
st.sidebar.info("本工具會從 Yahoo、鉅亨網、經濟日報等來源即時抓取新聞，並生成適合 AI (ChatGPT/Claude) 分析的指令。")

# --- Main Logic ---
st.title("🔥 台股資金動能 AI 分析助手")
st.markdown("本工具會自動聚合各大財經媒體新聞，幫助您找出當下的資金熱點。")

if st.button("🚀 即時抓取新聞並生成 AI 指令"):
    with st.spinner("正在搜尋各大財經媒體..."):
        news_list = get_all_news()
        
    if not news_list:
        st.error("暫時無法取得新聞，請稍後再試。")
    else:
        st.success(f"成功抓取 {len(news_list)} 則最新新聞！")
        
        # 1. Generate Prompt
        formatted_news = ""
        for i, n in enumerate(news_list, 1):
            formatted_news += f"{i}. [{n['source']}] {n['title']}\n"
            if n.get('summary'): formatted_news += f"   摘要：{n['summary']}\n"
            if n.get('link'): formatted_news += f"   連結：{n['link']}\n"
            formatted_news += "\n"
            
        final_prompt = system_prompt_template + "\n【今日台股重點新聞列表】\n" + formatted_news
        
        # 2. Display Prompt Area
        st.subheader("📋 生成的 AI 指令 (請點擊右上角複製)")
        st.code(final_prompt, language="markdown")
        
        # 3. Display News Table
        st.subheader("📰 原始新聞來源清單")
        df = pd.DataFrame(news_list)
        st.dataframe(df[['source', 'title', 'link']], use_container_width=True)
        
        # 4. Success Toast
        st.toast("指令已生成，請複製到 ChatGPT/Claude 進行分析！")

else:
    # Initial state
    st.write("點擊上方按鈕開始抓取今日即時數據。")
    
    # Showcase sources
    cols = st.columns(5)
    sources = ["Yahoo股市", "鉅亨網", "經濟日報", "MoneyDJ", "玩股網"]
    for i, s in enumerate(sources):
        cols[i].metric(s, "Online", delta_color="normal")

st.markdown("---")
st.caption("由 AI 輔助開發 · 專為台股動能交易者設計")
