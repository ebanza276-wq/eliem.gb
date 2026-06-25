import flet as ft
import flet_video as ftv

def main(page: ft.Page):
    page.title = "Publications"
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 390
    page.window.height = 844
    page.window.resizable = False
    page.window.center()
    # 🔥 IMPORTANT (supprime tous les espaces)
    page.padding = 0
    page.spacing = 0
    selected_index = 0
    video_url = None
    stories = []
    explore_tab = "découvrir"
    publications = [
        {   "etat":1,
            "id":1,
            "creator_nom":"Alice Martin",
            "avatar":"https://i.pravatar.cc/100?img=1",
            "contenu":"https://picsum.photos/1080/1080?3",
            "description":"Motivation 💪🔥 #motivation",
            "profil":[
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://picsum.photos/1080/1080",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://picsum.photos/1080/1080?4",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
            ],
            "likes":12,
            "comments":20,
            "shares":10,
        },
        {   "etat":0,
            "id":2,
            "creator_nom":"Alice Martin",
            "avatar":"https://i.pravatar.cc/100?img=1",
            "contenu": """
Chaque petit pas compte.

Ne compare pas ton chapitre 1 au chapitre 20 de quelqu'un d'autre.
Continue d'avancer, même lentement.

#mindset #motivation #developpementpersonnel
""",
            #"description":"Motivation 💪🔥",
            "profil":[
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"Engagé pour une Europe forte, verte et souveraine. Ensemble, construisons l’avenir durable de notre continent. 🇫🇷🇪🇺",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://picsum.photos/1080/1080?4",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
            ],
            "likes":12,
            "comments":20,
            "shares":10,
        },
        {   "etat":1,
            "id":3,
            "creator_nom":"Alice Martin",
            "avatar":"https://i.pravatar.cc/100?img=1",
            "contenu":"https://www.w3schools.com/html/mov_bbb.mp4",
            "description":"Motivation 💪🔥",
            "profil":[
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"Engagé pour une Europe forte, verte et souveraine. Ensemble, construisons l’avenir durable de notre continent. 🇫🇷🇪🇺",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://picsum.photos/1080/1080?4",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
            ],
            "likes":12,
            "comments":20,
            "shares":10,
        },
        {   "etat":0,
            "id":3,
            "creator_nom":"bella",
            "avatar":"https://picsum.photos/id/64/200/200",
            "contenu":"https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500",
            "description": """
Il y a des personnes qui n’ont pas besoin de parler fort pour être remarquées. Leur présence suffit. Entre douceur et confiance, ce portrait capture un instant simple mais puissant, celui où l’on est pleinement soi-même, sans filtre ni artifice. ✨ 
            #portrait #naturel #beauté #authenticité #lifestyle #confidence #photography
""",
            "profil":[
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
                {
                    "nom":"Alice Martin",
                    "avatar":"https://i.pravatar.cc/100?img=1",
                    "contenu":"https://picsum.photos/1080/1080?4",
                    "description":"Motivation 💪🔥",
                    "likes":12,
                    "comments":20,
                    "shares":10,
                },
            ],
            "likes":12,
            "comments":20,
            "shares":10,
        },
    ]
    videos = [
        {"creator_nom": "Bianca Herrera", "contenu": "https://www.w3schools.com/html/mov_bbb.mp4", "likes": "36.6K", "medias": "104", "videos": "9"},
        {"creator_nom": "Lovina", "contenu": "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4", "likes": "12.4K", "medias": "45", "videos": "2"}
    ]
    decouvrir_data = [
        {
            "nom": "Bianca Herrera",
            "username": "@biancaherrera",
            "avatar": "https://picsum.photos/100/100?img=10",
            "cover": "https://picsum.photos/400/600?img=15",
            "large": True
        },
        {
            "nom": "Lovina",
            "username": "@lovina",
            "avatar": "https://picsum.photos/100/100?img=11",
            "cover": "https://picsum.photos/400/600?img=16",
            "large": False
        }
    ]
    recommandes_data = [
        {"avatar": "https://picsum.photos/600/400?img=21", "nom": "Aria Sky", "username": "@ariasky"},
        {"avatar": "https://picsum.photos/600/400?img=22", "nom": "Eva Moon", "username": "@evamoon"}
    ]
    historique_recherche = [
        {"nom": "gina", "username": "@your.fav.bunny", "avatar": "https://picsum.photos/100/100?img=30"},
        {"nom": "Emjayplays", "username": "@emjayplays", "avatar": "https://picsum.photos/100/100?img=31"},
        {"nom": "Ava Skye", "username": "@avaskyee", "avatar": "https://picsum.photos/100/100?img=32"}
    ]
    def story(s):
        return ft.Column(
            horizontal_alignment="center",
            controls=[
                ft.Container(
                    padding=3,
                    border=ft.border.Border(
                    top=ft.BorderSide(3, "pink"),
                    bottom=ft.BorderSide(3, "pink"),
                    left=ft.BorderSide(3, "pink"),
                    right=ft.BorderSide(3, "pink"),
                    ),
                    border_radius=50,
                    content=ft.CircleAvatar(
                        foreground_image_src=s["avatar"],
                        radius=30
                    ),
                    #on_click=lambda e: page.run_task(on_avatar_click, e, s)
                    #on_click=lambda e: on_avatar_click(e, s),
                ),
                ft.Text(s["nom"], size=12)
            ]
        )
    def hashtags(txt):
        spans = []
        for mot in txt.split():
            color = "blue" if mot.startswith("#") else "white"
            spans.append(
                ft.TextSpan(text=mot + " ", style=ft.TextStyle(color=color))
            )
        return ft.Text(spans=spans)
    def item_recent(user):
        return ft.Container(
        padding=12,
        border_radius=12,
        bgcolor="#1E1E1E",
        content=ft.Row(
            controls=[
                ft.CircleAvatar(
                    radius=22,
                    foreground_image_src=user["avatar"],
                ),

                ft.Column(
                    spacing=2,
                    expand=True,
                    controls=[
                        ft.Text(
                            user["nom"],
                            color="white",
                            weight=ft.FontWeight.W_600,
                        ),
                        ft.Text(
                            f"@{user['username']}",
                            color="grey",
                            size=12,
                        ),
                    ],
                ),

                ft.Icon(
                    ft.Icons.CHEVRON_RIGHT,
                    color="grey",
                ),
            ],
        ),
    )
    def video_preview(url):
        def play_video(e):
            nonlocal video_url
            video_url = url
            page.go("/video_message")

        return ft.Container(
            content=ft.Stack(
                alignment=ft.Alignment.CENTER,
                controls=[
                    ft.Image(src="https://picsum.photos/1080/1080?video", width=float("inf"), border_radius=12, height=300, fit="cover"),  
                    ft.IconButton(  
                        icon=ft.Icons.PLAY_CIRCLE_FILL,  
                        icon_size=60,  
                        icon_color="#00AFF0",
                        on_click=play_video  
                    )
                ]
            )
        )
    async def open_drawer(e):
        await page.show_drawer()
    def debloquer(p):
        p["etat"]=1
        update_page()
    def publication(p):
        liked = False

        like_count = ft.Text(str(p["likes"]), weight="bold")
        comm_count=ft.Text("12", weight="bold")
        part_count=ft.Text("12", weight="bold")
        like_icon = ft.IconButton(icon=ft.Icons.FAVORITE_BORDER)
        def toggle_like(e):
            nonlocal liked
            if liked:
                like_icon.icon = ft.Icons.FAVORITE_BORDER
                like_icon.icon_color = "white"
                like_count.value = str(int(like_count.value) - 1)
            else:
                like_icon.icon = ft.Icons.FAVORITE
                like_icon.icon_color = "red"
                like_count.value = str(int(like_count.value) + 1)

            liked = not liked
            page.update()

        like_icon.on_click = toggle_like
        contenu = p["contenu"]
        etat = p["etat"]

        if etat == 1:
            if contenu.endswith(".mp4"):
                media = video_preview(contenu)
            elif contenu.startswith("https"):
                media = ft.Container(
                content=ft.Image(
                src=contenu,
                width=float("inf"),
                height=350,
                fit="cover", # Version propre avec l'énumération Flet
                ),
                border_radius=20,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS, # 🔥 Obligatoire pour couper l'image aux angles
                )

            else:
                media = ft.Container(
                content=hashtags(contenu)
                )
        else:
            media = ft.Container(  
                height=320,  
                border_radius=12,  
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,  
                content=ft.Stack(  
                    controls=[  
                        ft.Image(  
                            src="https://picsum.photos/1080/1080?blur",  
                            fit="cover",  
                            width=float("inf"),  
                            height=320,
                            #blur=ft.Blur(15, 15, ft.BlurTileMode.CLAMP) # Effet flouté
                        ),  
                        ft.Container(bgcolor=ft.Colors.with_opacity(0.75, "black"), expand=True),  
                        ft.Container(  
                            alignment=ft.Alignment.CENTER,  
                            content=ft.Column(  
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
                                alignment=ft.MainAxisAlignment.CENTER,  
                                controls=[  
                                    ft.Container(  
                                        padding=12,  
                                        bgcolor=ft.Colors.with_opacity(0.75, "black"),  
                                        border_radius=50,  
                                        content=ft.Icon(ft.Icons.LOCK_OUTLINED, color="#00AFF0", size=30),  
                                    ),  
                                    ft.Text("Contenu Premium", size=18, weight=ft.FontWeight.BOLD, color="white"),  
                                    ft.Text("Abonnez-vous pour débloquer", size=12, color="white70"),  
                                    ft.Container(height=5),  
                                    ft.FilledButton(  
                                        "Débloquer (4.99€)",  
                                        #icon=ft.Icons.STAR_PURPLE_554,  
                                        style=ft.ButtonStyle(  
                                            bgcolor="#00AFF0",  
                                            color="white",  
                                            shape=ft.RoundedRectangleBorder(radius=20),  
                                        ),  
                                        height=40,  
                                        on_click=lambda e: debloquer(p)
                                    ),  
                                ],  
                            ),  
                        ),  
                    ]  
                ),  
            )  
        return ft.Container(
        #bgcolor=CARD_BG,
        border_radius=15,
        padding=15,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Row(
                            [
                                ft.CircleAvatar(
                                    radius=18,
                                    foreground_image_src=p["avatar"],
                                ),
                                ft.Text(
                                    p["creator_nom"],
                                    color="white",
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ]
                        ),
                        ft.Icon(
                            ft.Icons.MORE_HORIZ,
                            #color=TEXT_GRAY,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                *[ [hashtags(p["description"])] if p.get("description") else [] ][0],
                media,
                ft.Row(
                    [
                        like_icon,
                        ft.IconButton(
                            icon=ft.Icons.CHAT_BUBBLE_OUTLINE,
                            #icon_color=TEXT_GRAY,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.MONETIZATION_ON_OUTLINED,
                            #icon_color=PINK,
                        ),
                        ft.Column(expand=True)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                [
                    like_count,
                    ft.Text("likes"),
                    comm_count,
                    ft.Text("comments"),
                ],
                spacing=5,
            )
            ]
        ),
    )

    # EXCLUSIVE CONTENT
    exclusive_title = ft.Container(
        content=ft.Text(
            "EXCLUSIVE CONTENT",
            #color=TEXT_GRAY,
            weight=ft.FontWeight.BOLD,
        ),
        padding=ft.Padding.symmetric(horizontal=15),
    )
    
    page.drawer = ft.NavigationDrawer(
    bgcolor="#121212",
    controls=[
        ft.Container(
            padding=20,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.CircleAvatar(
                        radius=40,
                        foreground_image_src="https://i.pravatar.cc/150?img=1"
                    ),
                    ft.Text(
                        "@alicemartin",
                        size=18,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(
                        "Créatrice de contenu",
                        color="grey"
                    ),
                ]
            )
        ),

        ft.Divider(color="#222"),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.PERSON, color="#00AFF0"),
            title=ft.Text("Mon profil"),
        ),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.BOOKMARK_BORDER, color="#00AFF0"),
            title=ft.Text("Collections"),
        ),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.ACCOUNT_BALANCE, color="#00AFF0"),
            title=ft.Text("Devenir Createur"),
        ),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.LANGUAGE, color="#00AFF0"),
            title=ft.Text("Language"),
        ),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.QUESTION_MARK, color="#00AFF0"),
            title=ft.Text("Help"),
        ),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.SETTINGS, color="#00AFF0"),
            title=ft.Text("Paramètres"),
        ),

        ft.Divider(color="#222"),

        ft.ListTile(
            leading=ft.Icon(ft.Icons.LOGOUT, color="red"),
            title=ft.Text("Déconnexion"),
        ),
    ],
)
    header = ft.AppBar(
        leading=ft.IconButton(icon=ft.Icons.MENU, icon_color="white",on_click=open_drawer,),
        title=ft.Text("SocialFlow", size=22, weight=ft.FontWeight.BOLD, font_family="sans-serif"),
        center_title=True,
        bgcolor="#121212",
        elevation=2,
        actions=[
            ft.IconButton(icon=ft.Icons.NOTIFICATIONS_NONE, icon_color="white"),
            ft.Container(
                content=ft.Icon(ft.Icons.PERSON, color="white", size=16),
                bgcolor="purple",
                shape=ft.BoxShape.CIRCLE,
                margin=ft.Margin.only(right=15),
                padding=6
            )
        ]
    )
    posts_column = ft.Column(scroll="auto")
    def page_accueil():
        if stories:
            section_stories = ft.Container(
            padding=ft.Padding.only(top=5, bottom=5),
            bgcolor="#121212",
            content=ft.Row(
                controls=[
                    ft.Container(width=5),
                    *[story(s) for s in stories]
                ],
                scroll=ft.ScrollMode.AUTO
            )
        )
        else:
            section_stories = None

        controls = [header]

        if section_stories:
            controls.append(section_stories)

            controls.append(
            ft.Container(
                height=1,
                bgcolor=ft.Colors.GREY_800
            )
        )

        controls.extend(
        [publication(p) for p in publications]
    )

        posts_column.controls = controls

        return ft.Container(
        expand=True,
        padding=0,
        margin=0,
        content=posts_column
    )
    def build_explore_tabs():
        def set_tab(tab_name):
            nonlocal explore_tab
            explore_tab = tab_name
            update_page()

        def tab_style(target_tab):
            is_active = explore_tab == target_tab
            return ft.TextStyle(
                color="white" if is_active else "grey600",
                weight=ft.FontWeight.BOLD if is_active else ft.FontWeight.NORMAL,
                size=18 if is_active else 16
            )

        return ft.Container(
            padding=ft.Padding.only(top=15, bottom=15, left=10, right=10),
            bgcolor="#000000",
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.TextButton(
                        content=ft.Text("Découvrir", style=tab_style("découvrir")),
                        on_click=lambda _: set_tab("découvrir")
                    ),
                    ft.Text("|", color="grey800", size=14),
                    ft.TextButton(
                        content=ft.Text("Vidéo", style=tab_style("vidéo")),
                        on_click=lambda _: set_tab("vidéo")
                    ),
                    ft.Text("|", color="grey800", size=14),
                    ft.TextButton(
                        content=ft.Text("Rechercher", style=tab_style("rechercher")),
                        on_click=lambda _: set_tab("rechercher")
                    ),
                ]
            )
        )
    def view_decouvrir():
        def creator_card(c):
            return ft.Container(
            width=185,
            height=320,
            border_radius=24,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            border=ft.Border.all(1, "#2A2A2A"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color="#00000060",
            ),
            content=ft.Stack(
                controls=[
                    ft.Image(
                        src=c["cover"],
                        fit="cover",
                        expand=True,
                    ),

                    ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.Alignment.TOP_CENTER,
                            end=ft.Alignment.BOTTOM_CENTER,
                            colors=[
                                ft.Colors.TRANSPARENT,
                                "#000000DD",
                            ],
                        )
                    ),

                    ft.Container(
                        padding=15,
                        alignment=ft.Alignment.BOTTOM_LEFT,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.END,
                            spacing=8,
                            controls=[

                                ft.Row(
                                    spacing=8,
                                    controls=[
                                        ft.Stack(
                                            controls=[
                                                ft.CircleAvatar(
                                                    foreground_image_src=c["avatar"],
                                                    radius=18,
                                                ),
                                                ft.Container(
                                                    width=10,
                                                    height=10,
                                                    bgcolor="#00FF66",
                                                    border_radius=10,
                                                    right=0,
                                                    bottom=0,
                                                    border=ft.Border.all(
                                                        2,
                                                        "black",
                                                    ),
                                                ),
                                            ]
                                        ),

                                        ft.Column(
                                            spacing=0,
                                            controls=[
                                                ft.Text(
                                                    c["nom"],
                                                    color="white",
                                                    size=13,
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                                ft.Text(
                                                    c["username"],
                                                    color="white70",
                                                    size=11,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),

                                ft.Row(
                                    spacing=10,
                                    controls=[
                                        ft.Icon(
                                            ft.Icons.FAVORITE,
                                            color="red",
                                            size=14,
                                        ),
                                        ft.Text(
                                            "24K",
                                            color="white70",
                                            size=11,
                                        ),
                                        ft.Icon(
                                            ft.Icons.VIDEOCAM,
                                            color="white70",
                                            size=14,
                                        ),
                                        ft.Text(
                                            "128",
                                            color="white70",
                                            size=11,
                                        ),
                                    ],
                                ),

                                ft.Container(
                                    bgcolor="#FF2D55",
                                    border_radius=20,
                                    padding=ft.Padding.symmetric(
                                        horizontal=12,
                                        vertical=6,
                                    ),
                                    content=ft.Text(
                                        "Suivre",
                                        color="white",
                                        size=11,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ),
                            ],
                        ),
                    ),
                ]
            ),
        )
        def top_creator_item(c):
            return ft.Container(
            padding=10,
            border_radius=15,
            bgcolor="#111111",
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        spacing=10,
                        controls=[
                            ft.CircleAvatar(
                                foreground_image_src=c["avatar"],
                                radius=22,
                            ),
                            ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(
                                        c["nom"],
                                        color="white",
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        c["username"],
                                        color="white60",
                                        size=12,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    ft.TextButton(
                        "Suivre",
                        style=ft.ButtonStyle(
                            color="white",
                            bgcolor="#FF2D55",
                        ),
                    ),
                ],
            ),
        )
        recommended_section = ft.Column(
        spacing=10,
        controls=[
            ft.Text(
                "Créateurs recommandés",
                color="white",
                size=18,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Row(
                scroll=ft.ScrollMode.AUTO,
                spacing=10,
                controls=[
                    ft.Container(
                        width=300,
                        height=160,
                        border_radius=20,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        content=ft.Stack(
                            controls=[
                                ft.Image(
                                    src=r["avatar"],
                                    fit="cover",
                                    expand=True,
                                ),
                                ft.Container(
                                    gradient=ft.LinearGradient(
                                        begin=ft.Alignment.TOP_CENTER,
                                        end=ft.Alignment.BOTTOM_CENTER,
                                        colors=[
                                            ft.Colors.TRANSPARENT,
                                            "#000000CC",
                                        ],
                                    )
                                ),
                                ft.Container(
                                    alignment=ft.Alignment.BOTTOM_LEFT,
                                    padding=15,
                                    content=ft.Text(
                                        r["nom"],
                                        color="white",
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ),
                            ]
                        ),
                    )
                    for r in recommandes_data
                ],
            ),
        ],
        )
        top_section = ft.Column(
        spacing=10,
        controls=[
            ft.Text(
                "🏆 Top créateurs",
                color="white",
                size=18,
                weight=ft.FontWeight.BOLD,
            ),
            *[top_creator_item(c) for c in decouvrir_data],
        ],
        )
        creator_grid = ft.Row(
        scroll=ft.ScrollMode.AUTO,
        spacing=12,
        controls=[creator_card(c) for c in decouvrir_data],
        )
        return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=15,
        controls=[

            # Bannière tendance
            ft.Container(
                margin=10,
                height=190,
                border_radius=25,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                content=ft.Stack(
                    controls=[
                        ft.Image(
                            src="https://picsum.photos/900/500?blur=1",
                            fit="cover",
                            expand=True,
                        ),
                        ft.Container(
                            gradient=ft.LinearGradient(
                                begin=ft.Alignment.TOP_CENTER,
                                end=ft.Alignment.BOTTOM_CENTER,
                                colors=[
                                    ft.Colors.TRANSPARENT,
                                    "#000000EE",
                                ],
                            )
                        ),
                        ft.Container(
                            padding=20,
                            alignment=ft.Alignment.BOTTOM_LEFT,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.END,
                                spacing=5,
                                controls=[
                                    ft.Text(
                                        "🔥 Tendances du jour",
                                        color="white",
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        "Découvrez les créateurs les plus populaires",
                                        color="white70",
                                        size=13,
                                    ),
                                ],
                            ),
                        ),
                    ]
                ),
            ),
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=10),
                content=ft.Text(
                    "Créateurs populaires",
                    color="white",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
            creator_grid,
            ft.Container(
                padding=10,
                content=recommended_section,
            ),

            ft.Container(
                padding=10,
                content=top_section,
            ),

            ft.Container(height=30),
        ],
    )
    def view_video():
        return ft.PageView(
            horizontal=False,
            expand=True,
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Stack(
                        controls=[
                            ftv.Video(
                                playlist=[ftv.VideoMedia(v["contenu"])],
                                autoplay=True,
                                expand=True,
                                show_controls=False,
                            ),
                            # Dégradé supérieur pour masquer la barre d'onglets proprement
                            ft.Container(
                                top=0, left=0, right=0, height=80,
                                gradient=ft.LinearGradient(
                                    begin=ft.Alignment.TOP_CENTER,
                                    end=ft.Alignment.BOTTOM_CENTER,
                                    colors=[ft.Colors.BLACK54, ft.Colors.TRANSPARENT]
                                )
                            ),
                            # Infos en overlay inférieur
                            ft.Container(
                                bottom=20,
                                left=15,
                                right=15,
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=ft.CrossAxisAlignment.END,
                                    controls=[
                                        ft.Row(
                                            spacing=10,
                                            controls=[
                                                ft.CircleAvatar(foreground_image_src="https://picsum.photos/100/100?img=10", radius=20),
                                                ft.Column(
                                                    spacing=2,
                                                    controls=[
                                                        ft.Text(v["creator_nom"], color="white", weight="bold", size=15),
                                                        ft.Row(
                                                            spacing=10,
                                                            controls=[
                                                                ft.Row([ft.Icon(ft.Icons.IMAGE_OUTLINED, size=14, color="white70"), ft.Text(v["medias"], color="white70", size=12)]),
                                                                ft.Row([ft.Icon(ft.Icons.VIDEOCAM_OUTLINED, size=14, color="white70"), ft.Text(v["videos"], color="white70", size=12)]),
                                                                ft.Row([ft.Icon(ft.Icons.FAVORITE_ROUNDED, size=14, color="white70"), ft.Text(v["likes"], color="white70", size=12)]),
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.IconButton(icon=ft.Icons.PERSON_ADD_ROUNDED, icon_color="white", icon_size=24)
                                    ]
                                )
                            )
                        ]
                    )
                ) for v in videos
            ]
        )
    def view_rechercher():
        return ft.Container(
        padding=20,
        expand=True,
        content=ft.Column(
            spacing=15,
            controls=[
                ft.Text(
                    "Recherche",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),

                ft.TextField(
                    hint_text="Rechercher des créateurs...",
                    prefix_icon=ft.Icons.SEARCH,
                    bgcolor="#1E1E1E",
                    border_radius=20,
                    border_color=ft.Colors.TRANSPARENT,
                    focused_border_color="#3A3A3A",
                    cursor_color="white",
                    text_style=ft.TextStyle(color="white"),
                    hint_style=ft.TextStyle(color="#888888"),
                    filled=True,
                    content_padding=15,
                    width=float("inf"),
                ),

                ft.Container(height=10),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            "Récemment consultés",
                            color="white",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.TextButton(
                            "Tout voir",
                            style=ft.ButtonStyle(
                                color="#00BFFF"
                            ),
                        ),
                    ],
                ),

                ft.Divider(color="#2A2A2A", height=1),

                # Liste des créateurs récents
                ft.Column(
                    spacing=10,
                    controls=[
                        item_recent(u)
                        for u in historique_recherche
                    ],
                ),

                ft.Container(height=10),

                ft.FilledButton(
                    "Voir plus",
                    width=float("inf"),
                    style=ft.ButtonStyle(
                        bgcolor="#2A2A2A",
                        color="white",
                        shape=ft.RoundedRectangleBorder(radius=12),
                    ),
                ),
            ],
        ),
    )
    def page_explore():
        if explore_tab == "découvrir":
           sub_content = view_decouvrir()
        elif explore_tab == "vidéo":
           sub_content = view_video()
        else:
           sub_content = view_rechercher()

        return ft.Column(
        spacing=0,
        controls=[
            build_explore_tabs(),
            ft.Container(content=sub_content, expand=True)
        ],
        expand=True
    )
    def set_index(i):
        nonlocal selected_index
        selected_index = i
        update_page()
    def update_page():
        if selected_index == 0:
            contenu.content = page_accueil()
        elif selected_index == 1:
            contenu.content = page_explore()
        elif selected_index == 2:
            contenu.content = ft.Text("plus")
        elif selected_index == 4:
            contenu.content = ft.Text("Send")
        elif selected_index == 5:
            contenu.content = ft.Text("Send")

        page.update()
    nav_bar = ft.Container(
    content=ft.Row(
        [
            ft.IconButton(
                icon=ft.Icons.HOME,
                icon_color="white",
                on_click=lambda e: set_index(0)
            ),
            ft.IconButton(
                icon=ft.Icons.EXPLORE,
                icon_color="white",
                on_click=lambda e: set_index(1)
            ),
            ft.IconButton(
                icon=ft.Icons.ADD_BOX_OUTLINED,
                icon_color="white",
                on_click=lambda e: set_index(2)
            ),
            ft.IconButton(
                icon=ft.Icons.CHAT,
                icon_color="white",
                on_click=lambda e: set_index(4)
            ),
            ft.IconButton(ft.Icons.PERSON_OUTLINE, icon_color="white",on_click=lambda e: set_index(5)),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
    ),
    padding=ft.Padding.only(top=10, bottom=20),
    bgcolor="#121212",
    border=ft.Border.only(
        top=ft.BorderSide(1, "#222222")
    ),
)
    page.navigation_bar = nav_bar
    def route_change(e):
        if page.route.startswith("/video"):
            page.views.append(
            ft.View(
            route=page.route,
            appbar=ft.AppBar(title=ft.Text("Lecture vidéo")),
            padding=0,
            controls=[
                ftv.Video(
                    playlist=[
                        ftv.VideoMedia(video_url)
                    ],
                    autoplay=True,
                    expand=True,
                    show_controls=True
                )
            ]
        )
    )
    page.on_route_change = route_change
    #page.on_view_pop = view_pop
    contenu = ft.Container(expand=True, content=page_accueil())
    page.add(contenu)
ft.app(target=main)
