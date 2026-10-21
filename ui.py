import json
import streamlit as st
import streamlit.components.v1 as components


def load_css():
    st.markdown('''<style>
:root {
    color-scheme: dark;
    --ink: #eef0ff;
    --muted: #a3accb;
    --line: rgba(162, 164, 227, .17);
    --violet: #a78bfa;
    --cyan: #86e4e9;
}
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse at 85% 2%, rgba(94, 54, 180, .21), transparent 46%),
        radial-gradient(ellipse at 9% 64%, rgba(26, 101, 129, .10), transparent 43%),
        #070a17;
    color: var(--ink);
    isolation: isolate;
}
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: -1;
    opacity: .45;
    background-image:
        radial-gradient(1px 1px at 23px 41px, #adbfec 95%, transparent),
        radial-gradient(1px 1px at 131px 107px, #bfb1f5 95%, transparent),
        radial-gradient(1px 1px at 79px 183px, #84c5df 95%, transparent);
    background-size: 229px 263px, 307px 337px, 419px 383px;
}
[data-testid="stAppViewContainer"]::after {
    content: "";
    position: fixed;
    width: 620px;
    height: 620px;
    right: -280px;
    top: -340px;
    border: 1px solid rgba(178, 157, 250, .15);
    border-radius: 50%;
    box-shadow: 0 0 0 64px rgba(163, 133, 245, .025),
                0 0 0 128px rgba(132, 176, 238, .018);
    pointer-events: none;
    z-index: -1;
}
[data-testid="stHeader"] {
    background: rgba(7, 10, 23, .80);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(151, 153, 220, .06);
}
.block-container {
    max-width: 1240px;
    padding-top: 3.1rem;
    padding-bottom: 3rem;
}
h1 {
    font-size: clamp(2rem, 3.2vw, 2.9rem) !important;
    line-height: 1.35 !important;
    letter-spacing: -.035em;
    font-weight: 750 !important;
    background: linear-gradient(110deg, #ffffff 10%, #dfd5ff 58%, #9bdfe6 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    padding-bottom: .65rem !important;
}
h2, h3, h4 {color: #edf0ff !important; letter-spacing: -.015em;}
h3 {font-size: 1.25rem !important; font-weight: 650 !important;}
p, li {line-height: 1.85;}
.eyebrow {
    display: inline-block;
    color: #c4b5fd;
    font-size: .77rem;
    font-weight: 600;
    letter-spacing: .12em;
    padding: .36rem .85rem;
    margin-bottom: 1.05rem;
    background: rgba(133, 100, 218, .10);
    border: 1px solid rgba(174, 148, 247, .23);
    border-radius: 999px;
    box-shadow: inset 0 1px 0 rgba(226, 216, 255, .04);
}
.eyebrow::before {content: "✦"; color: #91dfe6; margin-right: .55rem;}
[data-testid="stSidebar"] {
    background: linear-gradient(175deg, #101326 0%, #0a0d1b 80%);
    border-right: 1px solid var(--line);
}
[data-testid="stSidebar"] h3 {font-size: 1.2rem !important;}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: .48rem .2rem;
    border-radius: 10px;
    transition: background .2s ease;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: rgba(150, 124, 227, .08);
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
    background: linear-gradient(90deg, rgba(146, 110, 242, .17), rgba(126, 172, 230, .04));
}
[data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] p {
    color: var(--muted) !important;
    font-size: .80rem;
    line-height: 1.8;
}
[data-testid="stWidgetLabel"] p {color: #c6cce4; font-size: .86rem;}
[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: var(--line) !important;
    border-radius: 18px !important;
}
[data-testid="stVerticalBlockBorderWrapper"][height],
[data-testid="stVerticalBlockBorderWrapper"]:has(> div > [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"] > [data-testid="stTextArea"]),
[data-testid="stVerticalBlockBorderWrapper"]:has(> div > [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"] h4) {
    background: linear-gradient(145deg, rgba(28, 32, 57, .86), rgba(14, 18, 37, .93));
    box-shadow: inset 0 1px 0 rgba(228, 222, 255, .035), 0 18px 60px rgba(0, 0, 0, .15);
}
[data-testid="stExpander"] details {
    border: 1px solid var(--line);
    border-radius: 12px;
    background: rgba(22, 27, 48, .65);
}
[data-testid="stExpander"] summary {color: #bcc5e7;}
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
    color: #e0e6fa !important;
    caret-color: #bba7ff;
    background: #0d1227 !important;
}
[data-testid="stTextArea"] textarea {
    line-height: 1.95;
    font-size: .95rem;
    padding: 1.1rem;
    font-family: inherit;
}
[data-testid="stTextInput"] input::placeholder {color: #8290b4;}
[data-testid="stTextInput"] [data-baseweb="input"],
[data-testid="stTextArea"] [data-baseweb="textarea"],
[data-testid="stSelectbox"] [data-baseweb="select"] > div {
    border-color: rgba(156, 160, 219, .22) !important;
    background-color: #0d1227 !important;
    border-radius: 11px;
    color: #e0e6fa;
}
[data-baseweb="popover"] [role="listbox"] {
    background: #151a30 !important;
    color: #e0e6fa !important;
}
[data-testid="stButton"] button,
[data-testid="stDownloadButton"] button,
[data-testid="stLinkButton"] a {
    min-height: 2.7rem;
    border-radius: 11px;
    border: 1px solid rgba(157, 155, 218, .21);
    color: #d7ddf6;
    background: rgba(28, 33, 59, .70);
    transition: border-color .2s ease, background .2s ease, box-shadow .2s ease, transform .2s ease;
}
[data-testid="stButton"] button {text-align: left;}
[data-testid="stButton"] button:hover,
[data-testid="stDownloadButton"] button:hover,
[data-testid="stLinkButton"] a:hover {
    color: #fff;
    border-color: rgba(179, 148, 255, .62);
    background: rgba(62, 48, 101, .65);
    box-shadow: 0 4px 22px rgba(127, 88, 220, .13);
    transform: translateY(-1px);
}
button[kind="primary"], a[kind="primary"],
[data-testid="stBaseButton-primary"], [data-testid="stBaseLinkButton-primary"] {
    color: #fff !important;
    border-color: rgba(190, 162, 255, .55) !important;
    background: linear-gradient(115deg, #6550b5, #4b3a8c 75%, #354f79) !important;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, .10), 0 5px 24px rgba(101, 69, 189, .15);
}
button:focus-visible, a:focus-visible {
    outline: 2px solid #a99af5 !important;
    outline-offset: 3px;
}
hr {
    margin: 1.8rem 0 !important;
    border: 0 !important;
    height: 1px;
    background: linear-gradient(90deg, rgba(146, 122, 213, .32), rgba(128, 171, 218, .10), transparent);
}
[data-testid="stAlert"] {
    border: 1px solid rgba(129, 173, 232, .18);
    border-radius: 12px;
}
[data-testid="stImage"] img {border-radius: 14px;}
* {scrollbar-width: thin; scrollbar-color: #424164 transparent;}
*::-webkit-scrollbar {width: 6px; height: 6px;}
*::-webkit-scrollbar-thumb {background: #424164; border-radius: 9px;}
::selection {background: rgba(151, 119, 243, .40); color: white;}
@media (max-width: 700px) {
    .block-container {padding-top: 4rem; padding-left: 1.1rem; padding-right: 1.1rem;}
    h1 {font-size: 1.9rem !important;}
    .eyebrow {font-size: .7rem; letter-spacing: .07em;}
    [data-testid="stAppViewContainer"]::after {opacity: .4;}
}
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {animation: none !important; transition: none !important; scroll-behavior: auto !important;}
}
</style>''', unsafe_allow_html=True)


def copy_button(content):
    # JSON serialization keeps quotes/newlines valid; escape HTML script terminators.
    payload = json.dumps(content, ensure_ascii=True).replace('<', r'\u003c').replace('>', r'\u003e').replace('&', r'\u0026')
    template = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><style>
    body {margin:0; font-family:system-ui,sans-serif; background:transparent; color-scheme:dark;}
    button {width:100%;padding:13px;border:1px solid rgba(195,172,255,.5);border-radius:11px;background:linear-gradient(115deg,#6d56bd,#493989 72%,#354e77);color:#fff;font-size:14px;font-weight:600;cursor:pointer;box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 5px 22px rgba(96,66,173,.2);transition:filter .2s,box-shadow .2s;}
    button:hover {filter:brightness(1.15);box-shadow:0 7px 28px rgba(138,98,230,.3);} button:focus-visible {outline:2px solid #bfaaff;outline-offset:2px;}
    #status {font-size:12px;color:#a3accb;margin-top:7px;line-height:1.5;}
    </style><button id="copy" type="button">复制提示词</button><div id="status" role="status" aria-live="polite"></div><script>
    const text = __PAYLOAD__;
    const button = document.getElementById('copy');
    const status = document.getElementById('status');
    function legacyCopy() {
      const area = document.createElement('textarea'); area.value = text;
      area.style.position = 'fixed'; area.style.left = '-9999px'; document.body.appendChild(area);
      area.select(); let copied = false;
      try {copied = document.execCommand('copy');} finally {area.remove();}
      return copied;
    }
    button.addEventListener('click', async () => {
      let copied = false;
      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(text); copied = true;
        } else {copied = legacyCopy();}
      } catch (error) {try {copied = legacyCopy();} catch (ignored) {copied = false;}}
      button.textContent = copied ? '已复制 ✓' : '复制未完成';
      status.textContent = copied ? '可以粘贴到你使用的 AI 工具中。' : '请在上方文本框全选复制，或下载 TXT。';
      setTimeout(() => {button.textContent = '复制提示词';}, 2400);
    });</script></html>'''
    components.html(template.replace('__PAYLOAD__', payload), height=92)
