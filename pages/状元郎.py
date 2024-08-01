'''我的主页'''
import streamlit as st
from PIL import Image, ImageFilter
from matplotlib import pyplot 

page = st.sidebar.radio('我的首页', ['我的兴趣推荐','人民的图片处理工具','人民的智能词典','人民的留言区', '人民的其他网站'])

def page_1():
    '''我的兴趣推荐'''
    with open('2.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format = 'audio/mp3', start_time = 0)
    st.write(':green[我的武侠梦]')
    st.text('每个人心中都有一个江湖，像这样')
    st.image('1.jpg')
    st.text('这样')
    st.image('2.jpg')
    st.text('或是这样')
    st.image('3.jpg')
    st.text('或许是身着飘逸的长衫，手持三尺青锋，在山林间快意恩仇。我身轻如燕，能飞檐走壁，穿梭于山川湖泊之间。')
    st.text('心怀正义，路见不平定会拔刀相助，拯救弱小于危难之中。')
    st.text('也或许是梦想着能与志同道合的侠客们结伴而行，共闯天涯。在桃花盛开的山谷中饮酒论剑，切磋武艺，')
    st.text('交流着对江湖道义的理解。在月黑风高的夜晚，潜伏在恶势力的巢穴外，等待时机，一举将其铲除，还世间一个太平。')
    st.image('4.jpg')
    st.text('谁不是渴望练就一身绝世武功，如凌波微步，能在敌人的攻击下轻松闪避；又如降龙十八掌，掌风所至，石破天')
    st.text('惊，让邪恶之徒闻风丧胆。用武功，保护无辜百姓免受欺凌，让正义的光芒照亮每一个黑暗的角落。')
    st.image('5.jpg')
    st.text('一柄剑，一壶酒，畅游江湖是多少男儿的英雄梦啊。从金庸武侠到古龙世界，一个又一个的故事令我们感动，一')
    st.text('场又一场兄弟情令我们向往。')
    st.image('6.jpg')
    st.text('虽是幻想，但牵人心弦。虽是虚构却动人真情。在这世间于心里，保存着一股正义，一抹义气，这边是武侠，便')
    st.text('是牵动无数男儿的武侠世界，又何尝不是一种品味呢？')
    st.image('7.jpg')
    with open('1.mp4', 'rb') as f:
        mymp4 = f.read()
    st.video(mymp4)
    st.write(':red[此致每一个拥有武侠梦的英雄男儿]')
            
    
def page_2():
    '''人民的图片处理工具'''
    st.write('图片换色小程序')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpeg', 'jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, taba, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['原图', '灰度图', '紫红', '偏蓝', '暗紫','青色', '浮雕', '轮廓'])
        with tab1:
            st.image(img)
        with taba:
            imgw = img.convert('L') # 转换为灰度图
            st.image(imgw)


        with tab2:
            st.image(img_change(img,0, 2, 1))
        with tab3:
            st.image(img_change(img,1, 2, 0))
        with tab4:
            st.image(img_change(img,1, 0, 2))
        with tab5:
            st.image(img_change(img,1, 0, 0))
        with tab6:
            a = img.filter(ImageFilter.EMBOSS)
            st.image(a)
        with tab7:
            a = img.filter(ImageFilter.CONTOUR)
            st.image(a)
        
def page_3():
    '''人民的智能词典'''
    st.snow()
    st.write('智慧词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        word_list = f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')
    word_dict = {}
    for i in word_list:
        word_dict[i[1]] = [int(i[0]), i[2]]
        
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
        
    word = st.text_input('请输入要查询的单词')

    if word in word_dict:
        st.write(word_dict[word])
        n = word_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询技术', times_dict[n])
        if word =='python':
            st.code('''
                    #恭喜你触发彩蛋， 这是一行python代码
                    print('hello word')''')
        if word =='history':
            st.code('''
                    #恭喜你触发彩蛋， 这是中国历史朝代歌
                    ''')
            with open('2.mp4', 'rb') as f:
                mwmp4 = f.read()
            st.video(mwmp4)
            
        
def page_4():
    '''人民的留言区'''
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '状元郎（作者）':
            with st.chat_message('🐉'):
                st.write(i[1],':',i[2])
        elif i[1] == '林黛秀':
            with st.chat_message('🐇'):
                st.write(i[1],':',i[2])
        elif i[1] == i[1]:
            with st.chat_message('👲'):
                st.write(i[1], ':',i[2])
                
    name = st.selectbox('我是......', ['状元郎（作者）', '林黛秀',st.text_input('你是谁?')])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
    with open('leave_messages.txt', 'w', encoding='utf-8') as f:
        message = ''
        for i in messages_list:
            message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
        message = message[:-1]
        f.write(message)
        
def page_5():
    go = st.selectbox('选择想要查看的网页', ['百度', 'bilibili', '抖音'])
    if go == '百度':
        st.link_button('跳转到'+go, 'https://www.baidu.com/')
    elif go == 'bilibili':
        st.link_button('跳转到'+go, 'https://www.bilibili.com/')
    elif go == '抖音':
        st.link_button('跳转到'+go, 'https://www.douyin.com/downloadpage/app')
        

def img_change(img, rc, bc, gc):
    '''图片处理'''
    width,height = img.size
    image_arry = img.load()
    for x in range(width):
        for y in range(height):
            r = image_arry[x, y][rc]
            g = image_arry[x, y][gc]
            b = image_arry[x, y][bc]
            image_arry[x, y] = (r, b, g)
    return img

if page=='我的兴趣推荐':
    page_1()
elif page=='人民的图片处理工具':
    page_2()
elif page=='人民的智能词典':
    page_3()
elif page=='人民的留言区':
    page_4()
elif page=='人民的其他网站':
    page_5()