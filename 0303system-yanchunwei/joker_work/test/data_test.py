
text_list=[]

def get_data(data,n):
    '''处理字符串'''
    if len(data)<=n:
        text_list.append(data)
    else:
        text=data[:n]
        text_left=data[n:]
        text_list.append(text)
        get_data(text_left,n)

    return text_list


# s1='所经历的ijiooiej2到家了可为了使额空间诶上课开放日卫生间口腔科额UI日客人会计师为日多付撒翁认识人若所无所所所所所所'
# print(len(s1))
# print(get_data(s1,60))
s2='诶上课开放日卫生间口腔科额UI日客人会计师为日多付撒翁认识人若所无所所所所所所 ,time: 20 。'
print(len(s2))
print(get_data(s2,60))