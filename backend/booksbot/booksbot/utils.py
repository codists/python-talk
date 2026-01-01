"""
Manning 出版社作者格式类型：
1.单个作者："Taehun Kim"
2.使用逗号分隔的多个作者："Benjamin Tan Wei Hao, Shanoop Padmanabhan, and Varun Mallya"
3.包含 HTML 标签的作者："Constantin Gonciulea and Charlee Stefanski<br><i>Foreword by Heather Higgins<\u002fi>"
4.使用 ...with...and...连接的作者："Jungjun Hur and Younghee Song"
5.包含附加信息的作者： "Edward Raff, Drew Farris and Stella Biderman for Booz Allen Hamilton"

"""
import re
from html import unescape


def extract_authors(authorship_display: str):
    # 处理转义符,如 <\u002fi> 其实是 </i>
    s = unescape(authorship_display)

    # 移除 HTML 标签
    s = re.sub(r'<[^>]+>', '', s)

    # 移除 Forward
    s = re.sub(r'Forewords? by.*$', '', s, flags=re.IGNORECASE)

    # 移除组织名
    s = re.sub(r'\s+for\s+.*$', '', s, flags=re.IGNORECASE)

    # 移除普通分隔符
    s = s.replace(' and ', ', ')
    s = s.replace(' with ', ', ')

    # 切割成列表
    authors = [a.strip() for a in s.split(',') if a.strip()]

    return authors


# if __name__ == '__main__':
#     data = [
#         "Reuven M. Lerner",
#         "Taehun Kim",
#         "Val Andrei Fajardo",
#         "Benjamin Tan Wei Hao, Shanoop Padmanabhan, and Varun Mallya",
#         "Luis G. Serrano",
#         "Noah Flynn",
#         "Aneev Kochakadan",
#         "Tomasz Lelek and Artur Skowroński",
#         "Roberto Infante",
#         "Sebastian Raschka",
#         "Luca Antiga, Eli Stevens, Howard Huang, Thomas Viehmann",
#         "Nicole Koenigstein<br><i>Foreword by Luis Serrano</i>",
#         "Wei-Meng Lee",
#         "Pekka Enberg",
#         "José Haro Peralta<br><i>Foreword by Dan Barahona</i>",
#         "Alessandro Negro with Vlastimil Kus, Giuseppe Futia and Fabio Montagna<br><i>Forewords by Maxime Labonne, Khalifeh AlJadda</i>",
#         "Will Kurt",
#         "Rush Shahani",
#         "Jungjun Hur and Younghee Song",
#         "Mariia Mykhailova",
#         "François Chollet and Matthew Watson",
#         "Justin Mitchel",
#         "Tyler Suard",
#         "Tomaž Bratanič and Oskar Hane<br><i>Foreword by Paco Nathan</i>",
#         "Ashish Ranjan Jha",
#         "Sebastian Raschka and Abhinav Kimothi",
#         "Edward Raff, Drew Farris and Stella Biderman for Booz Allen Hamilton",
#         "Emmanuel Maggiori",
#         "Abhinav Kimothi",
#         "Gianluigi Mucciolo",
#         "Gianluigi Mucciolo",
#         "Gianluigi Mucciolo",
#         "Gianluigi Mucciolo",
#         "Gianluigi Mucciolo",
#         "Vaibhav Verdhan<br><i>Foreword by Ravi Gopalakrishnan</i>",
#         "Constantin Gonciulea and Charlee Stefanski<br><i>Foreword by Heather Higgins</i>",
#         "Immanuel Trummer",
#         "Christopher Kardell and Mark Brouwer",
#         "Rob Reider and Alexander Michalka",
#         "Mona Khalil<br><i>Foreword by Barry McCardel</i>"
#     ]
#     for name in data:
#         result = extract_authors(name)
#         print(result)
#     print(unescape("Constantin Gonciulea and Charlee Stefanski<br><i>Foreword by Heather Higgins<\u002fi>"))
