#!/usr/bin/env python
# coding: utf-8

# In[1]:


f'{17.489:.2f}' # 소수점 자릿수 포맷팅(반올림 적용)


# In[2]:


f'{10:d}' # 정수 포맷팅


# In[3]:


f'{65:c}{97:c}' # 정수 문자 코드를 그에 대응하는 문자로 표현


# In[4]:


f'{"hello":s} {7}'


# In[6]:


from decimal import Decimal

f'{Decimal("100000000000000.0"):.3f}'


# In[7]:


f'[{27:10d}]'


# In[8]:


f'[{3.5:10f}]'


# In[9]:


f'[{"hello":10}]'


# In[10]:


f'[{27:^7d}]'


# In[13]:


f'[{"27":^7s}]'


# In[14]:


# 기호가 포함된 양수를 포맷팅하기

f'[{27:+10d}]'


# In[15]:


f'[{27:+010d}]'


# In[17]:


print(f'{27:d}\n{27: d}\n{-27: d}')


# In[18]:


f'{123456789:,d}'


# In[19]:


f'{12346.78:,.2f}'


# In[20]:


'{:.2f}'.format(17.489)


# In[21]:


'{} {}'.format('Amanda', 'Cyan')


# In[22]:


'{0}, {0}, {1}'.format('Happy', 'Birthday')


# In[23]:


'{first} {last}'.format(first='Amanda', last='Gray')


# In[25]:


s1 = 'happy'
s2 = 'birthday'

s1 += ' ' + s2

s1


# In[26]:


symbol = '>'

symbol *= 5

symbol


# In[27]:


'happy birthday'.capitalize()


# In[28]:


'strings: a deeper look'.title()


# In[29]:


ord("A")


# In[30]:


ord("a")


# In[31]:


# 부분 문자열 찾기

sentence = 'to be or not to be that is the question'

sentence.count('to')


# In[32]:


sentence.count('to', 12)


# In[33]:


sentence.count(' ')


# In[34]:


sentence[25]


# In[35]:


sentence.rindex('be')


# In[37]:


sentence.startswith('to')


# In[38]:


sentence.startswith('be')


# In[39]:


values = '1\t2\t3\t4\t5'

values.replace('\t', ',')


# In[40]:


letters = 'A, B, C, D'

letters.split(',')


# In[41]:


letters.split(', ', 2) # rsplit 메서드 : 뒤에서부터 시작해 문자열을 나눈다


# In[42]:


letters_list = ['A', 'B', 'C', 'D']

','.join(letters_list) # 인자로 받은 문자열을 하나로 만든다


# In[43]:


','.join([str(i) for i in range(10)])


# In[44]:


'Amanda: 89, 97, 92'.partition(': ')


# In[45]:


'76'.isalnum()


# In[47]:


'-27'.isdigit()


# In[48]:


file_path = r'C:\MyFolder\MySubFolder\MyFile.txt'


# In[49]:


file_path


# In[50]:


import re

pattern = '02215'

'Match' if re.fullmatch(pattern, '02215') else 'No match'


# In[51]:


'Match' if re.fullmatch(pattern, '51120') else 'No match'


# In[52]:


'Valid' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Invalid' # * : 0번 또는 그 이상 반복되는 것


# In[53]:


'Valid' if re.fullmatch('[A-Z][a-z]*', 'eva') else 'Invalid'


# In[54]:


'Match' if re.fullmatch('[^a-z]', 'A') else 'No match'


# In[55]:


'Match' if re.fullmatch('[^a-z]', 'a') else 'No match'


# In[56]:


'Match' if re.fullmatch('[*+$]', '*') else 'No match'


# In[2]:


import re
'Match' if re.fullmatch('labell?ed', 'labelled') else 'No match'


# In[3]:


'Match' if re.fullmatch('labell?ed', 'labeled') else 'No match'


# In[4]:


'Match' if re.fullmatch('labell?ed', 'labellled') else 'No match'


# In[5]:


# l? : 남아있는 글자 ed의 바로 앞에 l이 오지 않거나 한번만 와야한다는 의미


# In[6]:


'Match' if re.fullmatch(r'\d{3,}', '123') else 'No match'


# In[7]:


'Match' if re.fullmatch(r'\d{3,}', '12345678') else 'No match'


# In[8]:


'Match' if re.fullmatch(r'\d{3,}', '12') else 'No match'


# In[9]:


'Match' if re.fullmatch(r'\d{3,6}', '123') else 'No match'


# In[10]:


'Match' if re.fullmatch(r'\d{3,6}', '1234567890') else 'No match'


# In[11]:


re.sub(r'\t', ',', '1\t2\t3\t4')


# In[12]:


re.sub(r'\t', ',', '1\t2\t3\t4', count=2) # count : 최대 교체 횟수 지정


# In[13]:


re.split(r',\s*', '1, 2, 3,4, 5,6,7,8') # * 없거나 하나 이상 등장. 공백 문자 클래스


# In[14]:


re.split(r',\s*', '1, 2, 3,4, 5,6,7,8', maxsplit=3)


# In[1]:


import re

result = re.search('Python', 'Python is fun') # 정규 표현식에 매칭되는 첫 번째 부분 문자열을 찾는다.


# In[2]:


result.group() if result else 'not found' # match 객체의 group 메서드: 매칭된 부분 문자열 반환


# In[3]:


result2 = re.search('fun!', 'Python is fun') # 문자열 패턴에 매칭되는 것이 없으면 None을 반환

result2.group() if result2 else 'not found'


# In[4]:


result3 = re.search('Sam', 'SAM WHITE', flags=re.IGNORECASE) # 정규 표현식의 매칭 방식을 바꾼다(본 예문은 대소문자 구별하지 않음)

result3.group() if result3 else 'not found'


# In[5]:


result = re.search('^Python', 'Python is fun') # 정규 표현식이 문자열의 첫 부분에 매칭해야 된다

result.group() if result else 'not found'


# In[6]:


result = re.search('^fun', 'Python is fun')

result.group() if result else 'not found'


# In[7]:


result = re.search('Python$', 'Python is fun')

result.group() if result else 'not found'


# In[8]:


result = re.search('fun$', 'Python is fun')

result.group() if result else 'not found'


# In[3]:


import re
contact = 'Wally White, Home:555-555-1234, Work:555-555-4321'

re.findall(r'\d{3}-\d{3}-\d{4}', contact)


# In[5]:


for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact): # findall 함수이나 match 객체를 필요할 때마다 만들어내는 자연 이터러블 반환
    print(phone.group())


# In[14]:


text = 'Charlie Cyan, e-mail: demol@deitel.com'

pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{3})'

result = re.search(pattern, text) # match 함수는 text 문자열이 전체 패턴에 일치하는 경우에만 match 객체를 반환


# In[16]:


result.groups()


# In[17]:


result.group()


# In[18]:


result.group(1)


# In[19]:


result.group(2)


# In[20]:


import pandas as pd

zips = pd.Series({'Boston' : '02215', 'Miami' : '3310'})

zips


# In[21]:


zips.str.match(r'\d{5}')


# In[22]:


cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])

cities


# In[23]:


cities.str.contains(r'[A-Z]{2}')


# In[24]:


cities.str.match(r'[A-Z]{2}')


# In[25]:


contacts = [['Mike Green', 'demol@deitel.com', '5555555555'],
           ['Sue Brown', 'demo2@deitel.com', '5555551234']]


contactsdf = pd.DataFrame(contacts, columns=['Name', 'Email', 'Phone'])

contactsdf


# In[26]:


#전화번호를 맵핑하기

import re

def get_formatted_phone(value):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value) # 10개의 연속된 숫자를 매칭
    return '-'.join(result.groups()) if result else value


# In[27]:


a = '5555555555'

result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', a)


# In[28]:


result.groups()


# In[29]:


formatted_phone = contactsdf['Phone'].map(get_formatted_phone)

formatted_phone


# In[30]:


contactsdf['Phone'] = formatted_phone

contactsdf

