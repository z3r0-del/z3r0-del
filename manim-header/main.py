from manim import *
import random
import numpy as np

config.pixel_width = 1500
config.pixel_height = 356
config.frame_width = 16
config.frame_height = 4


class Template(Scene):
    def construct(self):

        def make_random_plot(seed, color):
            rng = np.random.default_rng(seed)
            a, b, c = rng.uniform(0.5, 2, 3)

            def func(t):
                x = t
                y = a * np.sin(b * t + c)
                return np.array([x, y, 0])

            return ParametricFunction(
                func,
                t_range=[-9, 9, 0.1],
                color=color,
                stroke_width=1.5,
                stroke_opacity=0.25,
            )

        background_plots = VGroup(
            *[
                make_random_plot(
                    seed=i,
                    color=random.choice([BLUE_D, PURPLE_D, TEAL_D, GREEN_D]),
                )
                for i in range(5)
            ]
        )

        for i, plot in enumerate(background_plots):
            plot.shift(UP * (i - 2) * 0.3)

        background_plots.set_z_index(-10)

        for plot in background_plots:
            plot.add_updater(lambda m, dt: m.shift(RIGHT * dt * 0.1))

        self.add(background_plots)

        translations = [
            "Welcome to my",
            "Willkommen auf meinem",
            "Bienvenido a mi",
            "Bienvenue dans mon",
            "καλως ηρθες στο δικο μου",
            "欢迎来到我的",
            "ようこそ、私へ",
            "добро пожаловать в мой",
            "मेरे में स्वागत है",
        ]

        skill_files = [
            "../imgs/git-original.svg",
            "../imgs/bash-original.svg",
            "../imgs/css3-original.svg",
            "../imgs/apple-original.svg",
            "../imgs/html5-original.svg",
            "../imgs/linux-original.svg",
            "../imgs/python-original.svg",
            "../imgs/javascript-original.svg",
        ]

        logo = SVGMobject("../manim-header/imgs/GitHub_Lockup_White_Clearspace.svg")
        logo.set(height=1.2)
        logo.to_edge(RIGHT, buff=1.5)
        logo.set_z_index(0)

        skills = VGroup(*[SVGMobject(f) for f in skill_files])
        for icon in skills:
            icon.set(height=0.4)
        skills.arrange(RIGHT, buff=0.3)
        skills.move_to(ORIGIN)
        skills.to_edge(DOWN, buff=0.5)
        skills.set_z_index(0)

        skills_bg = SurroundingRectangle(
            skills,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0.8,
            buff=0.2,
            corner_radius=0.15,
        )
        skills_bg.set_z_index(-1)

        text = Text(translations[0], font_size=36, font="Noto Sans")
        text.next_to(logo, LEFT, buff=0.5)
        text.set_z_index(0)

        cursor = Rectangle(
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=1.0,
            height=0.4,
            width=0.05,
        )
        cursor.move_to(text[0])
        cursor.set_z_index(0)

        self.play(
            TypeWithCursor(text, cursor),
            FadeIn(logo),
            FadeIn(skills_bg),
            FadeIn(skills, shift=UP * 0.2),
        )
        self.play(Blink(cursor, blinks=2))
        self.wait(0.2)

        rest = translations[1:]
        random.shuffle(rest)

        for translation in rest:
            self.play(UntypeWithCursor(text, cursor))
            new_text = Text(translation, font_size=36, font="Noto Sans")
            new_text.next_to(logo, LEFT, buff=0.5)
            new_text.set_z_index(0)
            self.play(TypeWithCursor(new_text, cursor), run_time=0.8)
            text = new_text
            self.play(Blink(cursor, blinks=2))
            self.wait(0.25)

        self.wait()
