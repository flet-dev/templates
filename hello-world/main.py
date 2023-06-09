import flet as ft


def main(page: ft.Page):
    page.add(ft.Text("Hello, {{template_name}}!"))


ft.app(main)
