@echo off
chcp 65001
echo 正在啟動 台股資金動能分析 PRO [本地測試]...
pip install -r requirements.txt
streamlit run streamlit_app.py
pause
