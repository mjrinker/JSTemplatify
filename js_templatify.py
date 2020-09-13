import sublime
import sublime_plugin
import re


SETTINGS_FILE = "JSTemplatify.sublime-settings"


def js_templatify(string):
    string_quote = ''
    expressions_count = 0
    strings_count = 0
    within_expression = False
    string_template = '`'
    for c, char in enumerate(string):
        if string_quote == '' and char in ["'", '"', '`']:
            if c == 0 or (string[c - 1] != '\\') or (c > 1 and  string[c - 1] == '\\' and string[c - 2] == '\\'):
                string_quote = char
                strings_count += 1
                continue
        if string_quote and char == string_quote:
            if c == 0 or (string[c - 1] != '\\') or (c > 1 and  string[c - 1] == '\\' and string[c - 2] == '\\'):
                string_quote = ''
                continue

        if string_quote:
            string_template += char
        elif expressions_count == 0 and strings_count == 0:
            within_expression = True
            expressions_count += 1
            string_template += '${' + char
        elif char == '+':
            if within_expression:
                within_expression = False
                string_template += '}'
            else:
                within_expression = True
                expressions_count += 1
                string_template += '${'
        elif not re.match(r'\s', char):
            string_template += char

    if expressions_count == 0:
        return string

    if within_expression:
        within_expression = False
        string_template += '}'
    string_template += '`'
    return string_template


def run_on_selections(view, edit, func):
    settings = sublime.load_settings(SETTINGS_FILE)
    for s in view.sel():
        region = s if s else view.word(s)

        text = view.substr(region)
        # Preserve leading and trailing whitespace
        leading = text[:len(text)-len(text.lstrip())]
        trailing = text[len(text.rstrip()):]
        new_text = leading + func(text.strip()) + trailing
        if new_text != text:
            view.replace(edit, region, new_text)


class JsTemplatify(sublime_plugin.TextCommand):
    def run(self, edit):
        run_on_selections(self.view, edit, js_templatify)
