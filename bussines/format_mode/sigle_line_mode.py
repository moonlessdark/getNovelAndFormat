# encoding:utf-8
import re

from bussines.format_mode.common import format_common
from template.rexp_template import template


class formatByLine:
    """
    只在每一行的末尾检测是否有换行的标识符，如果有。保持不变，如果没有，就将下一行的文案去除左侧的换行符
    """

    def __init__(self):
        self.m = format_common()

    def split_by_line_feed(self, content: str, text_title_name: str) -> list:
        """
        按照换行符进行数组切割
        :return:
        """

        f_list = self.m.format_end_2_start_double_quotation_mark(content=content, text_title_name=text_title_name)

        content_list = []
        for line in range(len(f_list)):
            content_list_all = f_list[line].split("\n")
            for i in range(len(content_list_all)):
                if content_list_all[i] != "":
                    content_list.append(content_list_all[i])
        return content_list

    def format_end_str(self, content_list: list) -> list:
        """
        检查每一行的结束是否有结束符号
        :param content_list:
        :return:
        """
        start_wrap_character = template.wrap_character_by_line.value
        result_list: list = []
        temp_str: str = ""  # 用于存放临时字符的
        for line in content_list:
            if any(wrap_str in line[-1:] for wrap_str in start_wrap_character):
                if self.m.check_line_tips(temp_str + line):
                    r_list = format_common().line_feed_format(temp_str + line)
                    for s in range(len(r_list)):
                        result_list.append(r_list[s])
                        temp_str = ""
                else:
                    temp_str = temp_str + line
            else:
                temp_str = temp_str + line
        if temp_str != "":
            # 避免出现漏网之鱼
            result_list.append(temp_str)
        return result_list
