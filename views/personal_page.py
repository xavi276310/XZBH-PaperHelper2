from html import escape
from urllib.parse import urlencode

import streamlit as st
import streamlit.components.v1 as components
from config import AUTHOR_IMAGE


VIDEOS = [
    ('模块融合实践 · 视频一', 'BV1zg4y1C7oP'),
    ('模块融合实践 · 视频二', 'BV1Kw411G7Rw'),
]


def show_bilibili_video(title, bvid):
    """Show an official Bilibili preview; clicking it opens the original video."""
    video_url = f'https://www.bilibili.com/video/{bvid}/'
    player_url = 'https://player.bilibili.com/player.html?' + urlencode({
        'isOutside': 'true', 'bvid': bvid, 'p': 1, 'autoplay': 0,
    })
    label = escape(f'在 B 站观看：{title}', quote=True)
    preview = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><style>
body {{margin:0;font-family:system-ui,sans-serif;background:transparent;}}
.preview {{position:relative;aspect-ratio:16/9;overflow:hidden;border-radius:14px;background:#0a1024;box-shadow:inset 0 0 0 1px rgba(174,148,247,.22);}}
iframe {{position:absolute;inset:0;width:100%;height:100%;border:0;pointer-events:none;}}
.open-video {{position:absolute;inset:0;display:flex;align-items:flex-end;justify-content:flex-end;
  padding:14px;box-sizing:border-box;text-decoration:none;
  background:linear-gradient(transparent 65%,rgba(0,0,0,.48));}}
.open-video:focus-visible {{outline:3px solid #bda7fb;outline-offset:-4px;}}
.badge {{padding:8px 12px;border-radius:9px;border:1px solid rgba(193,165,255,.5);background:linear-gradient(115deg,rgba(103,76,177,.96),rgba(51,64,110,.96));color:#fff;font-size:13px;font-weight:600;}}
.open-video:hover .badge {{filter:brightness(1.2);box-shadow:0 4px 20px rgba(150,111,239,.3);}}
.hint {{margin:8px 0 0;color:#a3accb;font-size:12px;line-height:1.5;}}
</style></head><body>
<div class="preview">
  <iframe src="{escape(player_url, quote=True)}" title="{escape(title, quote=True)}的视频预览"
    loading="lazy" tabindex="-1" aria-hidden="true" referrerpolicy="strict-origin-when-cross-origin"></iframe>
  <a class="open-video" href="{video_url}" target="_blank" rel="noopener noreferrer" aria-label="{label}">
    <span class="badge">点击在 B 站观看 ↗</span>
  </a>
</div>
</body></html>'''
    # Scrolling preserves the full preview on both wide desktop and narrow screens.
    components.html(preview, height=310, scrolling=True)
    st.link_button('在 B 站观看 ↗', video_url, use_container_width=True)


def show_personal_page():
    st.markdown('<div class="eyebrow">关于作者</div>', unsafe_allow_html=True)
    st.title('你好，我是箫张跋扈')
    st.write('分享深度学习、模型模块与学术写作的实践经验。')
    st.markdown('我将常用的学术写作提示词整理成这个工具，希望帮你更快地组织问题、优化表达，把更多精力放在研究本身。')
    st.link_button('访问我的 B 站空间 ↗', 'https://space.bilibili.com/478113245', type='primary')
    st.divider()
    st.subheader('视频与学习资源')
    st.write('精选模块融合实践视频，点击视频预览或下方按钮即可前往 B 站观看。')
    for column, (title, bvid) in zip(st.columns(2), VIDEOS):
        with column:
            with st.container(border=True):
                st.markdown(f'#### {title}')
                show_bilibili_video(title, bvid)
    st.caption('若视频预览未能加载，可直接点击“在 B 站观看”按钮。')
    st.divider()
    st.subheader('了解更多')
    st.write('欢迎通过下方图片了解更多课程与学习资料，也可以先从公开分享的视频开始。')
    if AUTHOR_IMAGE.is_file():
        image_col, _ = st.columns([2, 1])
        with image_col:
            st.image(str(AUTHOR_IMAGE), use_container_width=True, caption='课程与学习资料')
    else:
        st.info('更多内容可前往上方 B 站空间查看。')
