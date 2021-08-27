
import dash_core_components as dcc
import dash_html_components as html


# Dash Bootstrap components
import dash_bootstrap_components as dbc

#Alternative 1
MAIN_COLOR_SELECTOR = "#6C7BC4"
#Alternative 2
MAIN_COLOR_SELECTOR = "#7484d4"

#Ideal
#MAIN_COLOR_SELECTOR = "#E6F0FF"


landingPage_title=["Welcome", "to the Bogotá tourist information system"]
landingPage_subtitle=["In this site you will find the main data on the tourist demand of Bogotá"]
landingPage = dbc.Container(
    children=[
    dbc.Row(children=[
        dbc.Col(
            html.Div(id="landing-text",
            children=[html.Div(
                id="landing-title",
                children=[
                    html.Span(html.H1(landingPage_title[0], className="landing-title-bold")),
                    html.Span(html.H1(landingPage_title[1], className="landing-title"))
                ],
                style={"marginLeft": "10%", "marginRight": "10%"},
            ),
            html.Div(
                id="landing-subtitle",
                children=[
                    html.Span(html.P(landingPage_subtitle[0], className="landing-subtitle")),
                ],
                style={"marginLeft": "10%", "marginRight": "10%"},
            )
            ],
            #className="container-fluid main-banner row-full",
            className="container-fluid landing-banner row-full",
            style={'backgroundImage': '''url("https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/landing-image.png")'''}                        
            #style={'background-image': '''url("assets/landing-image.png")'''}                        
            ),            
            width=12,
        ),
    ]
    ),

    ],
    fluid=True,
)

#--------Viajeros layouts------------



viajerosOpt1_title=["Meet", "THE TRAVELERS",\
    "who visit Bogotá city"]

viajerosOpt1_main_selector = ["National Travelers",\
     "International Travelers", "Both"]    

viajerosOpt1_main_selector_label = "Interact with each of the filters and discover the information of your interest"
    
viajerosOpt1_main_board_title = "General Information"

viajerosOpt1_main_board_menu1 = {'label': 'Año', 'options':[2020, 2019]}
#This function makes it possible to visualize the options properly
viajerosOpt1_main_board_menu1['options'] = list(map(lambda x: dbc.DropdownMenuItem(x), viajerosOpt1_main_board_menu1['options']))

viajerosOpt1_main_board_menu2 = {'label': 'Mes', 'options':["Enero", "Febrero"]}
#This function makes it possible to visualize the options properly
viajerosOpt1_main_board_menu2['options'] = list(map(lambda x: dbc.DropdownMenuItem(x), viajerosOpt1_main_board_menu2['options']))

viajerosOpt1_main_board_labels = ["Total travelers", "Travelers gender", "Origin",\
    "Education level", "Age"]


viajerosOpt1 = dbc.Container(
    children=[
    #---Main banner
    dbc.Row(children=[        
        dbc.Col(
            html.Div(
            children=[html.Div(
                children=[
                    html.Span(html.H1(viajerosOpt1_title[0], className="main-title")),
                    html.Span(html.H1(viajerosOpt1_title[1], className="main-title-bold")),
                    html.Span(html.H1(viajerosOpt1_title[2], className="main-title"))
                ],
                style={"marginLeft": "10%", "marginRight": "10%"},                
            ),
            ],
            className="container-fluid main-banner row-full",
            style={'backgroundImage': '''url("https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-opt1-main.jpg")''',\
                'backgroundPosition': "center"}, 
            #style={'background-image': '''url("assets/viajeros-opt1-main.jpg")'''}                                    
            ),            
            width=12,
        ),
    ]
    ),
    dbc.Row([
        dbc.Col(
            html.Div([
                #Botón Nacionales
                dbc.Button(viajerosOpt1_main_selector[0],\
                    id="viajeros-selector-nacionales-opt1", \
                    className="main-primary-selector-subpage btn-block"),                    
            ], style={'textAlign' : "center"}),
            width=3,
        ),
        dbc.Col(
            html.Div([
                #Botón Internacionales
                dbc.Button(viajerosOpt1_main_selector[1],\
                    id="viajeros-selector-internacionales-opt1", \
                    className="main-primary-selector-subpage btn-block"),                    
            ], style={'textAlign' : "center"}),
            width=3,
        ),
        dbc.Col(
            html.Div([
                #Botón Ambos
                dbc.Button(viajerosOpt1_main_selector[2],\
                    id="viajeros-selector-nacionales-opt1", \
                    className="main-primary-selector-subpage btn-block"),                    
            ], style={'textAlign' : "center"}),
            width=3,
        ),         
    ],
    justify="center",
    ),

    dbc.Row([
        dbc.Col(
            #Mensaje bajo los selectores principales
            html.Div(html.P(viajerosOpt1_main_selector_label), \
                style={'fontSize':"20px", 'textAlign' : "center", "marginBottom": "2.5rem"}),
        ),
    ],
    justify="center",
    ),
    html.Div(id="viajerosOpt1-main-board",children=[
        dbc.Card(
            dbc.CardBody(children=[
               dbc.Row([
                   dbc.Col(
                       [
                           html.Div([
                               html.H3(viajerosOpt1_main_board_title, \
                                   className="main-board-title-subpage"),
                                dbc.DropdownMenu(
                                    #Menu Año primer tablero
                                    viajerosOpt1_main_board_menu1["options"], label=viajerosOpt1_main_board_menu1["label"]\
                                        , color=MAIN_COLOR_SELECTOR, bs_size="lg", className="m-1 board-menu-subpage",\
                                        id="viajerosOpt1-main-board-menu-año",
                                ),
                                dbc.DropdownMenu(
                                    #Menu Mes segundo tablero
                                    viajerosOpt1_main_board_menu2["options"], label=viajerosOpt1_main_board_menu2["label"]\
                                    , color=MAIN_COLOR_SELECTOR, bs_size="lg", className="m-1 board-menu-subpage",\
                                    id="viajerosOpt1-main-board-menu-mes",
                                ),
                            ],
                            className="main-board-header",
                           )
                       ],
                       width=12,
                   ),                                      
               ],

               ),
               dbc.Row([
                   dbc.Col([
                       html.Div([
                           html.Div([
                                html.Img(
                                    src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-board-logo1.png",
                                    style={"width": "6rem", "height": "6rem", "marginRight" : "1rem"}                                    
                                ),  
                                #This element gotta be reached using a call back with the id to load content
                                #That text is burned
                                html.Span(html.P("23M", id="viajerosOpt1-main-board-content-cantidad"), className="main-board-content-big"),

                            ],
                            className="main-board-container-standard-h",
                            style={'borderRight': "4px solid var(--third-color-contrast)"}
                           ),
                       ],
                       
                       )
                    ],
                    style={"marginTop": "3rem"},
                    md={"size": 4},
                   ),
                   dbc.Col([
                       html.Div([
                           html.Div([
                                html.Div([
                                    html.Img(
                                        src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-genero-hombre.png",
                                        style={"width": "6rem", "height": "6rem", "marginRight" : "1rem"}                                    
                                    ),  

                                    html.Div([
                                        #This element gotta be reached using a call back with the id to load content
                                        #That text is burned                                        
                                        html.P("32%", id="viajerosOpt1-main-board-content-genero-hombre", className="main-board-content-big"),                                     
                                        #Burnt label
                                        html.P("Men", className="main-board-subtitle")
                                    ],
                                    )
                                ],
                                style={"display": "flex", "justifyContent" : "center"}

                                ),
                                html.Div([
                                    html.Img(
                                        src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-genero-mujer.png",
                                        style={"width": "6rem", "height": "6rem", "marginRight" : "1rem"}                                    
                                    ),  

                                    html.Div([
                                        #This element gotta be reached using a call back with the id to load content
                                        #That text is burned                                        
                                        html.P("68%", id="viajerosOpt1-main-board-content-genero-hombre", className="main-board-content-big"),                                     
                                        #Burnt label
                                        html.P("Women", className="main-board-subtitle")
                                    ],
                                    )
                                ],
                                className="main-board-container-standard-h",

                                ),                         

                            ],
                            style={"display": "flex", "justifyContent" : "space-around"}
                           ),

                       ],
                       
                       )
                    ],
                    style={"marginTop": "3rem"},
                    md={"size": 6},
                   ),

               ],
                justify="center",

               ),
               dbc.Row([
                   dbc.Col([
                       html.Div(
                           html.P(viajerosOpt1_main_board_labels[0], className="main-board-label"),
                           style={'textAlign': "right", 'marginTop': "0.5rem"}
                       )
                   ],
                   md={"size": 4},
                   ),
                   dbc.Col([
                       html.Div(
                           html.P(viajerosOpt1_main_board_labels[1], className="main-board-label"),
                           style={'textAlign': "right", 'marginTop': "0.5rem"}
                       )
                   ],
                   md={"size": 6},
                   ),              
               ], 
               
               ),
               dbc.Row([
                   dbc.Col([
                       html.Div([
                            html.Img(
                                src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-origin.png",
                                style={"width": "6rem", "height": "6rem", "marginRight" : "1rem"}                                    
                            ),       
                            #This element gotta be reached using a call back with the id to load content
                            #That text is burned                                        
                            html.P("Valle del Cauca", id="viajerosOpt1-main-board-content-origin", className="main-board-content-small"),                                     
                       ],
                       className="main-board-container-standard-v",
                       style={'borderRight': "4px solid var(--third-color-contrast)"}              
                       ),
                   ],
                   md={"size": 4},
                   ),
                   dbc.Col([
                       html.Div([
                            html.Img(
                                src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-education.png",
                                style={"width": "6rem", "height": "6rem", "marginRight" : "1rem"}                                    
                            ),       
                            #This element gotta be reached using a call back with the id to load content
                            #That text is burned                                        
                            html.P("Undergraduate degree", id="viajerosOpt1-main-board-content-education", className="main-board-content-small"),                                     
                       ],
                       className="main-board-container-standard-v",
                       style={'borderRight': "4px solid var(--third-color-contrast)"}              
                       ),
                   ],
                   md={"size": 4},
                   ),
                   dbc.Col([
                       html.Div([
                            html.Img(
                                src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-age.png",
                                style={"width": "6rem", "height": "6rem", "marginRight" : "1rem"}                                    
                            ),       
                            #This element gotta be reached using a call back with the id to load content
                            #That text is burned                                        
                            html.P("18-30 years", id="viajerosOpt1-main-board-content-age", className="main-board-content-small"),                                     
                       ],
                       className="main-board-container-standard-v",
                       ),
                   ],
                   md={"size": 4},
                   ),
               ],
                justify="center",
               ),
               dbc.Row([
                   dbc.Col([
                       html.Div(
                           html.P(viajerosOpt1_main_board_labels[2], className="main-board-label"),
                           style={'textAlign': "center"}
                       )
                   ],
                   md={"size": 4},
                   ),
                   dbc.Col([
                       html.Div(
                           html.P(viajerosOpt1_main_board_labels[3], className="main-board-label"),
                           style={'textAlign': "center"}
                       )
                   ],
                   md={"size": 4},
                   ),
                   dbc.Col([
                       html.Div(
                           html.P(viajerosOpt1_main_board_labels[3], className="main-board-label"),
                           style={'textAlign': "center"}
                       )
                   ],
                   md={"size": 4},
                   ),                   
               ],               
               ),


            ]
            ),
            className="mb-3 main-board-subpage",
        ),
    ]),


    ],
    fluid=True,
)

