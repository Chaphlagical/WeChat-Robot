# WeChat Robot

This is a multifunction WeChat Robot based on wxpy. 

## Installation

* **Python 3.x**
* **pyecharts**
* **jieba**

## Introdution

### 1. WeChat Terminal

Using python operation system library os, you can control your computer through WeChat on your phone

#### Activate: 

```
cmd on
```

#### Inactivate:

```
cmd off
```

To prevent causing chaos, command terminal only available for the chats that has been activated.

#### Show the activated chats:

```
cmd list
```

After activating, you can control your computer through WeChat.

## 2. Turing Robot

Based on Turing Robot API (http://www.turingapi.com/), you can turn your WeChat to a chatting robot.

#### Activate: 

```
turing on
```

#### Inactivate:

```
turing off
```

To prevent causing chaos, Turing Robot only available for the chats that has been activated.

#### Show the activated chats:

```
turling list
```

When someone talk to you or @you in a group, the robot will reply auto automatically.

## 3. Analysis friend circle

You can analysis your friend circle by some keywords.

### Analysis your friends:

```
analysis friends
```

or

```
friends analysis
```

The result will be saved in:

* ./data/user/user_friends_data.md
* ./data/user/avatar
* ./data/user/Graph/China.html
* ./data/user/Graph/Gender.html
* ./data/user/Graph/Signature.html
* ./data/user/Graph/province.html (The province most of your friends come from)

### Analysis your groups:

If you want to analysis the specific group, you can post:

```
analysis [-group_name]
```

If you want to analysis all the groups, you can post:

```
analysis all group
```

The result will be saved in:

- ./data/group/[group_name]/group_members_data.md
- ./data/group/[group_name]/avatar
- ./data/group/[group_name]/Graph/Relationship.html

## Solution

### 1.  Sometimes you may not be able to download file named after  Chinese characters. 

Open file " ../dist-packages/urllib3/fields.py"

Find: 

```python
value = email.utils.encode_rfc2231(value, 'utf-8')
value = '%s*=%s' % (name, value)
```

Edit the second line to:

```python
value = '%s="%s"' % (name, value.encode('utf-8'))
```

