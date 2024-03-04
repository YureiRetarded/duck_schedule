import datetime
import flet as ft


def main(page: ft.Page):
    page.title = "Duck schedule"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.START

    dates_works = [datetime.datetime.now()]
    schedule = list()
    schedule_rows = []

    def change_date(e):
        dates_works.clear()
        dates_works.append(date_picker.value)
        create_schedule()

    def check_day(variant):
        match variant:
            case 1:
                return [ft.colors.GREEN, ft.colors.GREEN, ft.colors.GREEN, ft.colors.RED, ft.colors.RED, ft.colors.RED,
                        ft.colors.RED, ft.colors.GREEN]
            case 2:
                return [ft.colors.GREEN]
            case 3:
                return [ft.colors.GREEN, ft.colors.GREEN, ft.colors.GREEN, ft.colors.GREEN, ft.colors.GREEN,
                        ft.colors.GREEN, ft.colors.GREEN, ft.colors.RED]
            case 4:
                return [ft.colors.RED, ft.colors.RED, ft.colors.RED, ft.colors.GREEN, ft.colors.GREEN, ft.colors.GREEN,
                        ft.colors.GREEN,
                        ft.colors.RED]
            case 5:
                return [ft.colors.RED, ft.colors.RED, ft.colors.RED, ft.colors.GREEN, ft.colors.GREEN, ft.colors.GREEN,
                        ft.colors.GREEN,
                        ft.colors.GREEN, ]
            case _:
                return [ft.colors.PINK]

    def create_schedule():
        n = 0
        # 1 - Day work
        # 2 - Weekend all day and night
        # 3 - First 21 Hour Weekend 3 Night work
        # 4 - First 9 hour night work 12 relax 3 night work
        # 5 - First 9 hour work then relax
        while n < 30:
            schedule.append(
                [
                    dates_works[0].day,
                    dates_works[0].month,
                    dates_works[0].year,
                    1
                ])
            dates_works[0] += datetime.timedelta(days=1)
            schedule.append(
                [
                    dates_works[0].day,
                    dates_works[0].month,
                    dates_works[0].year,
                    1
                ])
            dates_works[0] += datetime.timedelta(days=1)
            schedule.append(
                [
                    dates_works[0].day,
                    dates_works[0].month,
                    dates_works[0].year,
                    2
                ])
            dates_works[0] += datetime.timedelta(days=1)
            schedule.append(
                [
                    dates_works[0].day,
                    dates_works[0].month,
                    dates_works[0].year,
                    3
                ])
            dates_works[0] += datetime.timedelta(days=1)
            schedule.append(
                [
                    dates_works[0].day,
                    dates_works[0].month,
                    dates_works[0].year,
                    4
                ])
            dates_works[0] += datetime.timedelta(days=1)
            schedule.append(
                [
                    dates_works[0].day,
                    dates_works[0].month,
                    dates_works[0].year,
                    5
                ])
            dates_works[0] += datetime.timedelta(days=1)
            schedule.append(
                [
                    dates_works[0].day,
                    dates_works[0].month,
                    dates_works[0].year,
                    2
                ])
            dates_works[0] += datetime.timedelta(days=1)
            schedule.append(
                [
                    dates_works[0].day,
                    dates_works[0].month,
                    dates_works[0].year,
                    2
                ])
            dates_works[0] += datetime.timedelta(days=1)
            n += 1
        create_schuelde_rows()

    def create_schuelde_rows():
        for day in schedule:
            schedule_rows.append(
                ft.Row([
                    ft.Container(
                        content=ft.Text(str(f"{day[0]}.{day[1]}.{day[2]}"), size=30),
                        gradient=ft.LinearGradient(
                            colors=check_day(day[3])
                        ),
                        expand=True,
                        height=50,
                        border_radius=10,
                        margin=5,
                        alignment=ft.alignment.center
                    ),
                ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        for row in schedule_rows:
            page.add(row)

    date_picker = ft.DatePicker(
        on_change=change_date,
    )

    page.overlay.append(date_picker)

    date_button = ft.ElevatedButton(
        "Выбери ближайшую первую дневную смену!",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
    )
    page.add(
        ft.Row(
            [
                date_button,
            ],
            height=70,
            alignment=ft.MainAxisAlignment.CENTER
        ),
    )
    page.scroll = True


ft.app(target=main, assets_dir='assets')