__author__ = "Samuel Amogbonjaye"



from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import font

# from fontTopLevel import *

class pyPROApp:
    def __init__(self, master):
        global dictDesignWindowPropCollect
        dictDesignWindowPropCollect = {}  #### Dictionary to collect properties of the design window
        self.implementFont_determine = 0    ### Variable that works in conjunction with implementFont command
        self.dictCountFont = {}     ### Dicitonary to store font instances for design window widgets
        self.implementImage_determine = 0   ### Variable that works in conjunction with implementImage command
        self.dictCountImage = {}         ### Dictionary to store PhotoImage instances for design window
        self.count_image_instances = 1
        self.commands_all = {}      ### Dictionary to store commands for all widgets

        self.styleWidgetConfigLabel = ttk.Style()       ###ttk.Style for Main and WidgetToplevel widgets
        self.clickWidgetConfig = 0  # Variable that determines if WidgetConfig Window has been opened earlier

        self.numberFont_2 = 1  ###### Variable for New Font Name
        self.isFontToplevel = 0  #### Variable to determine whether FontToplevel is opened

        self.iswinConfigToplevel = 0    ### Variable to determine wheter winConfigToplevel is opned earlier


        global screen_width, screen_height
        self.master = master
        screen_width = windowPRO.winfo_screenwidth()
        screen_height = windowPRO.winfo_screenheight()

    ### Parameters for Title of Design Window
        dictDesignWindowPropCollect["title"] = f"windowDesign.title('Design Window')"
        
    ### Parameters for Geometry of Design Window
        global new_value_width
        new_value_width = int(screen_width / 2)
        global new_value_height
        new_value_height = int(screen_height / 1.57)
        global new_value_position_x
        new_value_position_x = int(screen_width / 4.5)
        global new_value_position_y
        new_value_position_y = int(screen_height / 3.36)
        dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry('{new_value_width}x{new_value_height}+" \
                                                  f"{new_value_position_x}+{new_value_position_y}')"

        ######## Main Window
        windowPRO.title("BuildIt")
        windowPRO.geometry(
            "%dx%d+%d+%d" % (screen_width / 2, screen_height / 8, screen_width / 4.5, (screen_height / 20) - 20))

        ####### Main Menu Widget
        Menu_main = Menu(master)

        ### comms for Code Gen
        def comm4compile_text():
            codeGen = CodeGenerate()
            codeGen.compile2Text()

        def comm4compile_python():
            codeGen2 = CodeGenerate()
            codeGen2.compile2PythonFile()

        command4Code_Gen = Menu()
        command4Code_Gen.add_command(label = "To Python File", command = comm4compile_python)
        command4Code_Gen.add_command(label="To pyPRO's NotePad", command = comm4compile_text)


        ### comms for Beautify
        cascade_change_theme = Menu()
        cascade_change_theme.add_command(label="alt", command=lambda: self.styleWidgetConfigLabel.theme_use("alt"))
        cascade_change_theme.add_command(label="clam", command=lambda: self.styleWidgetConfigLabel.theme_use("clam"))
        cascade_change_theme.add_command(label = "classic", command = lambda: self.styleWidgetConfigLabel.theme_use("classic"))
        cascade_change_theme.add_command(label = "default", command = lambda: self.styleWidgetConfigLabel.theme_use("default"))
        cascade_change_theme.add_command(label="vista", command=lambda: self.styleWidgetConfigLabel.theme_use("vista"))
        cascade_change_theme.add_command(label="winnative", command=lambda: self.styleWidgetConfigLabel.theme_use("winnative"))
        cascade_change_theme.add_command(label="xpnative", command=lambda: self.styleWidgetConfigLabel.theme_use("xpnative"))

        command4Beautify = Menu()
        command4Beautify.add_separator()
        command4Beautify.add_command(label = "Default Theme", command=lambda: self.styleWidgetConfigLabel.theme_use("vista"))
        command4Beautify.add_cascade(label = "Change Theme", menu = cascade_change_theme)
        command4Beautify.add_separator()

        ### comms for Window Setup
        def command4winConfig():
            global winsetupObject
            winsetupObject = DesignWindowSetup()
        command4Window = Menu()
        command4Window.add_command(label = "Window Setup", command = command4winConfig)


        Menu_main.add_cascade(label="Code Gen", menu=command4Code_Gen)  ### CodeGen cass
        Menu_main.add_cascade(label="Beautify", menu = command4Beautify) ### Beautify cass
        Menu_main.add_cascade(label="Edit")
        Menu_main.add_cascade(label="Window", menu = command4Window)
        master.config(menu=Menu_main)  ##### Configure main menu widget to window

        self.toplevel4WidgetToolkit()  #####Run Widget Toolkit Toplevel

    def toplevel4WidgetToolkit(self):  ####### Creates Wigets Toolkit Window and All Inside It
        ####### Top level for Widget Toolkit
        toplevelWidgetToolkit = Toplevel(self.master)
        toplevelWidgetToolkit.transient(self.master)
        toplevelWidgetToolkit.geometry("%dx%d+%d+%d" % (207, screen_height/1.105, screen_width/168, screen_height/35))
        toplevelWidgetToolkit.title("Widgets Toolkit")
        toplevelWidgetToolkit.resizable(False, True)
        print(toplevelWidgetToolkit.winfo_screenwidth())
        ####### Scrollbar for Main Widgets
        scrollbarWidgetToolkit = ttk.Scrollbar(toplevelWidgetToolkit, )
        scrollbarWidgetToolkit.pack(side=RIGHT, fill=Y)

        ####### Canvas for Widget Toolkit
        canvasWidgetToolkit = Canvas(toplevelWidgetToolkit, highlightthickness=0,
                                     yscrollcommand=scrollbarWidgetToolkit.set, width=207,
                                     height=screen_height/1.105)
        canvasWidgetToolkit.pack(side=LEFT, )

        ####### Frame to contain all Main Widgets
        frameWidgetToolkit = ttk.Frame(canvasWidgetToolkit)
        frameWidgetToolkit.pack()
        # n, ne, e, se, s, sw, w, nw, or center
        canvasWidgetToolkit.create_window((0, 0), window=frameWidgetToolkit, anchor=NW)

        scrollbarWidgetToolkit.config(
            command=canvasWidgetToolkit.yview)  #### Set scrollbarWidgetToolkit for canvasWidgetToolkit

        toplevelWidgetToolkit.bind("<Configure>", lambda event: canvasWidgetToolkit.config(
            scrollregion=canvasWidgetToolkit.bbox(ALL)))  #### Bind Scroll region to Configure Event

        ######### Widgets Placement for the Widget Toolkit

        ### All Main Widgets Here

        # Label  for Tk Widgets
        label_tk_widgets = ttk.Label(frameWidgetToolkit, text="tk Widgets", font=("Onyx", 15, "bold"))
        label_tk_widgets.pack(anchor=N, pady=5)

        # Main Button Widget
        self.widget_button = ttk.Button(frameWidgetToolkit, text="Button", style="main.TButton",
                                        command=lambda: self.determineButton("button"))
        self.widget_button.pack(anchor=W, )

        # Main Checkbutton Widget
        widget_checkbutton = ttk.Button(frameWidgetToolkit, text="Checkbutton", style="main.TButton",
                                        command=lambda: self.determineCheckbutton("checkbutton"))
        widget_checkbutton.pack(anchor=W, )

        # Main Entry Widget
        widget_entry = ttk.Button(frameWidgetToolkit, text="Entry", style="main.TButton",
                                  command=lambda: self.determineEntry("entry"))
        widget_entry.pack(anchor=W, )

        # Main Label Widget
        widget_label = ttk.Button(frameWidgetToolkit, text="Label", style="main.TButton",
                                  command=lambda: self.determineLabel("label"))
        widget_label.pack(anchor=W, )

        # Main Listbox Widget
        widget_listbox = ttk.Button(frameWidgetToolkit, text="Listbox", style="main.TButton",
                                    command=lambda: self.determineListbox("listbox"))
        widget_listbox.pack(anchor=W)

        # Main Menu Widget
        widget_menu = ttk.Button(frameWidgetToolkit, text="Menu", style="main.TButton", command=self.mainMenu)
        widget_menu.pack(anchor=W)

        # Main Menubutton Widget
        widget_menubutton = ttk.Button(frameWidgetToolkit, text="Menubutton", style="main.TButton",
                                       command=lambda: self.determineMenubutton("menubutton"))
        widget_menubutton.pack(anchor=W)

        # Main Message Widget
        widget_message = ttk.Button(frameWidgetToolkit, text="Message", style="main.TButton",
                                    command=lambda: self.determineMessage("message"))
        widget_message.pack(anchor=W)

        # Main OptionMenu Widget
        widget_optionmenu = ttk.Button(frameWidgetToolkit, text="OptionMenu", style="main.TButton",
                                       command=lambda: self.mainOptionMenu("optionmenu"))
        widget_optionmenu.pack(anchor=W)

        # Main Radiobutton Widget
        widget_radiobutton = ttk.Button(frameWidgetToolkit, text="Radiobutton", style="main.TButton",
                                        command=lambda: self.determineRadiobutton("radiobutton"))
        widget_radiobutton.pack(anchor=W, )

        # Main Scale - Horizontal
        widget_scalehorizontal = ttk.Button(frameWidgetToolkit, text="Scale - Horizontal", style="main.TButton",
                                            command=lambda: self.determineScale("scale_horizontal"))
        widget_scalehorizontal.pack(anchor=W, )

        # Main Scale - Vertical
        widget_scalevertical = ttk.Button(frameWidgetToolkit, text="Scale - Vertical", style="main.TButton",
                                          command=lambda: self.determineScale("scale_vertical"))
        widget_scalevertical.pack(anchor=W, )

        # Main Scrollbar - Horizontal
        widget_scrollbar = ttk.Button(frameWidgetToolkit, text="Scrollbar - Horizontal", style="main.TButton",
                                      command=lambda: self.determineScrollbar("scrollbar"))
        widget_scrollbar.pack(anchor=W)

        # Main Scrollbar - Vertical
        widget_scrollbar = ttk.Button(frameWidgetToolkit, text="Scrollbar - Vertical", style="main.TButton",
                                      command=lambda: self.determineScrollbar("scrollbar"))
        widget_scrollbar.pack(anchor=W)

        # Main Spinbox Widget
        widget_spinbox = ttk.Button(frameWidgetToolkit, text="Spinbox", style="main.TButton",
                                    command=lambda: self.determineSpinbox("spinbox"))
        widget_spinbox.pack(anchor=W, )

        # Main Text Widget
        widget_text = ttk.Button(frameWidgetToolkit, text="Text", style="main.TButton",
                                 command=lambda: self.determineText("text"))
        widget_text.pack(anchor=W, )

        # Label for Tk Containers
        label_tk_containers = ttk.Label(frameWidgetToolkit, text="tk Containers", font=("Onyx", 15, "bold"))
        label_tk_containers.pack(anchor=N, pady=5)

        # Main Frame Contain
        widget_frame = ttk.Button(frameWidgetToolkit, text="Frame", style="main.TButton",
                                  command=lambda: self.determineFrame("frame"))
        widget_frame.pack(anchor=W, )

        # Main LabelFrame Contain
        widget_labelframe = ttk.Button(frameWidgetToolkit, text="LabelFrame", style="main.TButton",
                                       command=lambda: self.determineLabelFrame("labelframe"))
        widget_labelframe.pack(anchor=W, )

        # Main PanedWindow Contain
        widget_panedwindow = ttk.Button(frameWidgetToolkit, text="PanedWindow", style="main.TButton",
                                        command=lambda: self.determinePanedWindow("panedwindow"))
        widget_panedwindow.pack(anchor=W, )

        # Main Toplevel Contain
        widget_toplevel = ttk.Button(frameWidgetToolkit, text="Toplevel", style="main.TButton",
                                     command=lambda: self.determineToplevel("toplevel"))
        widget_toplevel.pack(anchor=W, )

        # Styling for Main Buttons
        style_main_buttons = ttk.Style()
        style_main_buttons.configure("main.TButton", width=30, anchor=W, )

    def toplevel4WidgetConfig(self):  ############ Contains Attributes available in all Widgets Classes

        self.clickWidgetConfig = 1  #### Variable that determines if WidgetConfig Window has been opened earlier

        ###### Top level for Widgets Config toplevel
        self.toplevelWidgetConfig = Toplevel(self.master, name = "!toplevel_attr_editor")
        self.toplevelWidgetConfig.transient(self.master)
        self.toplevelWidgetConfig.title("Widgets Config")
        self.toplevelWidgetConfig.geometry(
            "%dx%d+%d+%d" % (280, screen_height/1.105, screen_width-300, screen_height/35))
        self.toplevelWidgetConfig.resizable(False, True)

        ### Canvas for Widget Config Toplevel
        canvasWidgetConfig = Canvas(self.toplevelWidgetConfig, width=265, height=screen_height/1.1052,
                                    highlightthickness=0)
        canvasWidgetConfig.pack(side=LEFT)

        ### Frame to host All Widgets in Widget Config Toplevel
        self.frameWidgetConfig = ttk.Frame(canvasWidgetConfig)
        self.frameWidgetConfig.pack(fill = BOTH, expand = 1)

        ### Scrollbar to scroll Frame and hence all Widgets inside it
        scrollbarWidgetConfig = ttk.Scrollbar(self.toplevelWidgetConfig, orient=VERTICAL, command=canvasWidgetConfig.yview)
        scrollbarWidgetConfig.pack(side=RIGHT, fill=Y)

        canvasWidgetConfig.create_window((0, 0), window=self.frameWidgetConfig,
                                         anchor=NW)  ### Canvas Window to host self.frameWidgetConfig

        canvasWidgetConfig.config(
            yscrollcommand=scrollbarWidgetConfig.set)  ###### Set scrollbarWidgetConfig to canvasWidgetConfig

        self.toplevelWidgetConfig.bind("<Configure>", lambda event: canvasWidgetConfig.config(
            scrollregion=canvasWidgetConfig.bbox(ALL)))  #### Bind Scroll region to Configure Event

        # ATTRIBUTES DISPLAY AND EDIT
        ### Edit Attributes Label section
        label4edit_attributes = ttk.Label(self.frameWidgetConfig, text="Edit Attributes", font=("Onyx", 15, "bold"))
        label4edit_attributes.grid(row=100, column=1, sticky=N, columnspan=2, pady=5)

        ### Widget Variable Section
        label4widget_variable = ttk.Label(self.frameWidgetConfig, text="Widget\nVariable", style="widgetconfig.TLabel")
        label4widget_variable.grid(row=101, column=1, sticky=W)
        frame4widget_variable = ttk.Frame(self.frameWidgetConfig)
        frame4widget_variable.grid(row=101, column=2)
        self.entry4widget_variable = Entry(frame4widget_variable, relief=FLAT, disabledbackground = "white")
        self.entry4widget_variable.pack(side=LEFT, padx=3)

        blank_label4command = ttk.Label(frame4widget_variable, text="", anchor=W, width=3)
        blank_label4command.pack(side=LEFT)

        ### activebackground Sec
        def color4activebackground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4activebackground.delete(0, END)
            windowObject.entry4activebackground.insert(END, color)

        self.label4activebackground = ttk.Label(self.frameWidgetConfig, text="active\nbackground",
                                                style="widgetconfig.TLabel")
        self.label4activebackground.grid(sticky=W, row=105, column=1)
        self.frame4activebackground = ttk.Frame(self.frameWidgetConfig)
        self.frame4activebackground.grid(row=105, column=2)
        self.entry4activebackground = Entry(self.frame4activebackground, relief=FLAT)
        self.entry4activebackground.pack(side=LEFT, padx=3)
        button4activebackground = ttk.Button(self.frame4activebackground, text=">>", style="moreOptions.TButton",
                                             command = color4activebackground)
        button4activebackground.pack(side=LEFT)

        ### activeforeground Sec
        def color4activeforeground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4activeforeground.delete(0, END)
            windowObject.entry4activeforeground.insert(END, color)

        self.label4activeforeground = ttk.Label(self.frameWidgetConfig, text="active\nforeground",
                                                style="widgetconfig.TLabel")
        self.label4activeforeground.grid(sticky=W, row=110, column=1)
        self.frame4activeforeground = ttk.Frame(self.frameWidgetConfig)
        self.frame4activeforeground.grid(row=110, column=2)
        self.entry4activeforeground = Entry(self.frame4activeforeground, )
        self.entry4activeforeground.pack(side=LEFT, padx=3)
        button4activeforeground = ttk.Button(self.frame4activeforeground, text=">>", style="moreOptions.TButton",
                                             command = color4activeforeground)
        button4activeforeground.pack(side=LEFT)

        ### activestyle Sec
        activestyles = ("dotbox", "none", "underline")
        self.label4activestyle = ttk.Label(self.frameWidgetConfig, text="active\nstyle", style="widgetconfig.TLabel")
        self.label4activestyle.grid(sticky=W, row=120, column=1)
        self.combo4activestyle = ttk.Combobox(self.frameWidgetConfig, values=activestyles)
        self.combo4activestyle.grid(row=120, column=2, ipadx=5)

        ### anchor Sec
        anchors = ("nw", "n", "ne", "w", "center", "e", "sw", "s", "se")
        self.label4anchor = ttk.Label(self.frameWidgetConfig, text="anchor", style="widgetconfig.TLabel")
        self.label4anchor.grid(sticky=W, row=200, column=1)
        self.combo4anchor = ttk.Combobox(self.frameWidgetConfig, values = anchors)
        self.combo4anchor.grid(row=200, column=2, ipadx=5)

        ### aspect Sec
        def command4aspect(new_value):
            new_value = self.int_aspect.get()
            windowObject.int_aspect.set(new_value)

        self.int_aspect = IntVar(value = 100)
        self.label4aspect = ttk.Label(self.frameWidgetConfig, text = "aspect", style = "widgetconfig.TLabel")
        self.label4aspect.grid(sticky = W, row = 250, column = 1)
        self.frame4aspect = Frame(self.frameWidgetConfig, )
        self.frame4aspect.grid(sticky = W, row = 250, column = 2, padx = 25)
        self.label24aspect = Label(self.frame4aspect, text = self.int_aspect.get(), textvariable = self.int_aspect)
        self.label24aspect.pack()
        self.scale4aspect = ttk.Scale(self.frame4aspect, from_ = 1, to = 1000, orient = HORIZONTAL,
                                            variable = self.int_aspect, command = command4aspect)
        self.scale4aspect.pack()

        ### autoseparators
        self.bool_autoseparators = BooleanVar()
        self.bool_autoseparators.set(True)
        self.label4autoseparators = ttk.Label(self.frameWidgetConfig, text="auto\nseparators",
                                               style="widgetconfig.TLabel")
        self.label4autoseparators.grid(sticky=W, row=260, column=1)
        self.frame4autoseparators = ttk.Frame(self.frameWidgetConfig)
        self.frame4autoseparators.grid(row=260, column=2)
        radioTrue4autoseparators = ttk.Radiobutton(self.frame4autoseparators, text="True",
                                                    variable=self.bool_autoseparators, value=True)
        radioTrue4autoseparators.grid(sticky=W, row=1, column=1, padx=20)
        radioFalse4autoseparators = ttk.Radiobutton(self.frame4autoseparators, text="False",
                                                     variable=self.bool_autoseparators, value=False)
        radioFalse4autoseparators.grid(sticky=E, row=1, column=2, padx=20)

        ### background Sec
        def color4background():
            color = colorchooser.askcolor()[1]
            windowObject.entry4background.delete(0, END)
            windowObject.entry4background.insert(END, color)

        self.label4background = ttk.Label(self.frameWidgetConfig, text="background", style="widgetconfig.TLabel")
        self.label4background.grid(sticky=W, row=300, column=1)
        self.frame4background = ttk.Frame(self.frameWidgetConfig)
        self.frame4background.grid(row=300, column=2)
        self.entry4background = Entry(self.frame4background, relief=FLAT)
        self.entry4background.pack(side=LEFT, padx=3)
        button4background = ttk.Button(self.frame4background, text=">>", style="moreOptions.TButton",
                                       command = color4background)
        button4background.pack(side=LEFT)

        ### bitmap Sec
        bitmaps = ("error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question",
                   "warning")
        self.label4bitmap = ttk.Label(self.frameWidgetConfig, text="bitmap", style="widgetconfig.TLabel")
        self.label4bitmap.grid(sticky=W, row=400, column=1)
        self.combo4bitmap = ttk.Combobox(self.frameWidgetConfig, values = bitmaps)
        self.combo4bitmap.grid(row=400, column=2, ipadx=5)

        ### blockcursor Sec
        self.bool_blockcursor = BooleanVar()
        self.bool_blockcursor.set(True)
        self.label4blockcursor = ttk.Label(self.frameWidgetConfig, text="blockcursor",
                                              style="widgetconfig.TLabel")
        self.label4blockcursor.grid(sticky=W, row=410, column=1)
        self.frame4blockcursor = ttk.Frame(self.frameWidgetConfig)
        self.frame4blockcursor.grid(row=410, column=2)
        radioTrue4blockcursor = ttk.Radiobutton(self.frame4blockcursor, text="True",
                                                   variable=self.bool_blockcursor, value=True)
        radioTrue4blockcursor.grid(sticky=W, row=1, column=1, padx=20)
        radioFalse4blockcursor = ttk.Radiobutton(self.frame4blockcursor, text="False",
                                                    variable=self.bool_blockcursor, value=False)
        radioFalse4blockcursor.grid(sticky=E, row=1, column=2, padx=20)

        ### borderwidth Sec
        # self.int_borderwidth = IntVar()
        # self.int_borderwidth.set("")
        self.label4borderwidth = ttk.Label(self.frameWidgetConfig, text="borderwidth", style="widgetconfig.TLabel")
        self.label4borderwidth.grid(sticky=W, row=500, column=1)
        self.spinbox4borderwidth = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=200, increment=2, width=10, wrap=True)
                                               # textvariable = self.int_borderwidth)
        self.spinbox4borderwidth.grid(row=500, column=2)

        ### buttonbackground Sec
        def color4buttonbackground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4buttonbackground.delete(0, END)
            windowObject.entry4buttonbackground.insert(END, color)

        self.label4buttonbackground = ttk.Label(self.frameWidgetConfig, text="button\nbackground", style="widgetconfig.TLabel")
        self.label4buttonbackground.grid(sticky=W, row=505, column=1)
        self.frame4buttonbackground = ttk.Frame(self.frameWidgetConfig)
        self.frame4buttonbackground.grid(row=505, column=2)
        self.entry4buttonbackground = Entry(self.frame4buttonbackground, relief=FLAT)
        self.entry4buttonbackground.pack(side=LEFT, padx=3)
        button4buttonbackground = ttk.Button(self.frame4buttonbackground, text=">>", style="moreOptions.TButton",
                                             command = color4buttonbackground)
        button4buttonbackground.pack(side=LEFT)

        ### buttoncursor Sec
        buttoncursors = ( "arrow", "based_arrow_down", "based_arrow_up", "boat", "bogosity", "bottom_left_corner",
                          "bottom_right_corner", "bottom_side", "bottom_tee", "box_spiral", "center_ptr", "circle",
                          "clock", "coffee_mug", "cross",
        "cross_reverse", "crosshair", "diamond_cross", "dot", "dotbox", "double_arrow", "draft_large", "draft_small",
        "draped_box", "exchange", "fleur", "gobbler", "gumby", "hand1", "hand2", "heart", "icon", "iron_cross",
        "left_ptr", "left_side", "left_tee", "leftbutton", "ll_angle", "lr_angle", "man", "middlebutton", "mouse",
        "pencil", "pirate", "plus", "question_arrow", "right_ptr", "right_side", "right_tee", "rightbutton",
        "rtl_logo", "sailboat", "sb_down_arrow", "sb_h_double_arrow", "sb_left_arrow", "sb_right_arrow", "sb_up_arrow",
        "sb_v_double_arrow", "shuttle", "sizing", "spider", "spraycan", "star", "target", "tcross", "top_left_arrow",
        "top_left_corner", "top_right_corner", "top_side", "top_tee", "trek", "ul_angle", "umbrella", "ur_angle",
        "watch", "xterm", "X_cursor")
        self.label4buttoncursor = ttk.Label(self.frameWidgetConfig, text="button\ncursor", style="widgetconfig.TLabel")
        self.label4buttoncursor.grid(sticky=W, row=510, column=1)
        self.combo4buttoncursor = ttk.Combobox(self.frameWidgetConfig, values=buttoncursors)
        self.combo4buttoncursor.grid(row=510, column=2, ipadx=5)

        ### buttondownrelief Sec
        buttondownreliefs = ("flat", "raised", "sunken", "groove", "ridge", "solid")
        self.label4buttondownrelief = ttk.Label(self.frameWidgetConfig, text="buttondown\nrelief", style="widgetconfig.TLabel")
        self.label4buttondownrelief.grid(sticky=W, row=515, column=1)
        self.combo4buttondownrelief = ttk.Combobox(self.frameWidgetConfig, values=buttondownreliefs)
        self.combo4buttondownrelief.grid(row=515, column=2, ipadx=5)

        ### buttonuprelief Sec
        buttonupreliefs = ("flat", "raised", "sunken", "groove", "ridge", "solid")
        self.label4buttonuprelief = ttk.Label(self.frameWidgetConfig, text="buttonup\nrelief", style="widgetconfig.TLabel")
        self.label4buttonuprelief.grid(sticky=W, row=520, column=1)
        self.combo4buttonuprelief = ttk.Combobox(self.frameWidgetConfig, values=buttonupreliefs)
        self.combo4buttonuprelief.grid(row=520, column=2, ipadx=5)

        ### command Sec
        self.label4command = ttk.Label(self.frameWidgetConfig, text="command", style="widgetconfig.TLabel")
        self.label4command.grid(sticky=W, row=600, column=1)
        self.frame4command = ttk.Frame(self.frameWidgetConfig)
        self.frame4command.grid(row=600, column=2)
        self.entry4command = Entry(self.frame4command, relief=FLAT, )
        self.entry4command.pack(side=LEFT, padx=3)
        blank_label4command = ttk.Label(self.frame4command, text="", anchor=W, width=3)
        blank_label4command.pack(side=LEFT)

        ### compound Sec
        compounds = ("bottom", "center", "left", "right", "top")
        self.label4compound = ttk.Label(self.frameWidgetConfig, text="compound", style="widgetconfig.TLabel")
        self.label4compound.grid(sticky=W, row=610, column=1)
        self.combo4compound = ttk.Combobox(self.frameWidgetConfig, values = compounds)
        self.combo4compound.grid(row=610, column=2, ipadx=5)

        ### Cursor Sec
        cursors = ("arrow", "based_arrow_down", "based_arrow_up", "boat", "bogosity", "bottom_left_corner", "bottom_right_corner",
         "bottom_side", "bottom_tee", "box_spiral", "center_ptr", "circle", "clock", "coffee_mug", "cross",
         "cross_reverse", "crosshair", "diamond_cross", "dot", "dotbox", "double_arrow", "draft_large", "draft_small",
         "draped_box", "exchange", "fleur", "gobbler", "gumby", "hand1", "hand2", "heart", "icon", "iron_cross",
         "left_ptr", "left_side", "left_tee", "leftbutton", "ll_angle", "lr_angle", "man", "middlebutton", "mouse",
         "pencil", "pirate", "plus", "question_arrow", "right_ptr", "right_side", "right_tee", "rightbutton",
         "rtl_logo", "sailboat", "sb_down_arrow", "sb_h_double_arrow", "sb_left_arrow", "sb_right_arrow", "sb_up_arrow",
         "sb_v_double_arrow", "shuttle", "sizing", "spider", "spraycan", "star", "target", "tcross", "top_left_arrow",
         "top_left_corner", "top_right_corner", "top_side", "top_tee", "trek", "ul_angle", "umbrella", "ur_angle",
         "watch", "xterm", "X_cursor")
        self.label4cursor = ttk.Label(self.frameWidgetConfig, text="cursor", style="widgetconfig.TLabel")
        self.label4cursor.grid(sticky=W, row=700, column=1)
        self.combo4cursor = ttk.Combobox(self.frameWidgetConfig, values = cursors)
        self.combo4cursor.grid(row=700, column=2, ipadx=5)

        ### digits Sec
        # self.int_digits = IntVar(value = "")
        self.label4digits = ttk.Label(self.frameWidgetConfig, text="digits",
                                                  style="widgetconfig.TLabel")
        self.label4digits.grid(sticky=W, row=701, column=1)
        self.spinbox4digits = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=17, increment=1, width=10, wrap=True)
                                                      # textvariable = self.int_digits)
        self.spinbox4digits.grid(row=701, column=2)

        ### direction Sec
        directions = ("above", "below", "left", "right")
        self.label4direction = ttk.Label(self.frameWidgetConfig, text="direction", style="widgetconfig.TLabel")
        self.label4direction.grid(sticky=W, row=705, column=1)
        self.combo4direction = ttk.Combobox(self.frameWidgetConfig, values=directions)
        self.combo4direction.grid(row=705, column=2, ipadx=5)

        ### disabledbackground Sec
        def color4disabledbackground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4disabledbackground.delete(0, END)
            windowObject.entry4disabledbackground.insert(END, color)

        self.label4disabledbackground = ttk.Label(self.frameWidgetConfig, text="disabled\nbackground",
                                                  style="widgetconfig.TLabel")
        self.label4disabledbackground.grid(sticky=W, row=710, column=1)
        self.frame4disabledbackground = ttk.Frame(self.frameWidgetConfig)
        self.frame4disabledbackground.grid(row=710, column=2)
        self.entry4disabledbackground = Entry(self.frame4disabledbackground, relief=FLAT)
        self.entry4disabledbackground.pack(side=LEFT, padx=3)
        button4disabledbackground = ttk.Button(self.frame4disabledbackground, text=">>", style="moreOptions.TButton",
                                               command = color4disabledbackground)
        button4disabledbackground.pack(side=LEFT)

        ### disabledforeground
        def color4disabledforeground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4disabledforeground.delete(0, END)
            windowObject.entry4disabledforeground.insert(END,color)

        self.label4disabledforeground = ttk.Label(self.frameWidgetConfig, text="disabled\nforeground",
                                                  style="widgetconfig.TLabel")
        self.label4disabledforeground.grid(sticky=W, row=800, column=1)
        self.frame4disabledforeground = ttk.Frame(self.frameWidgetConfig)
        self.frame4disabledforeground.grid(row=800, column=2)
        self.entry4disabledforeground = Entry(self.frame4disabledforeground, relief=FLAT)
        self.entry4disabledforeground.pack(side=LEFT, padx=3)
        button4disabledforeground = ttk.Button(self.frame4disabledforeground, text=">>", style="moreOptions.TButton",
                                               command = color4disabledforeground)
        button4disabledforeground.pack(side=LEFT)

        ### exportselection
        self.bool_exportselection = BooleanVar()
        self.bool_exportselection.set(1)
        self.label4exportselection = ttk.Label(self.frameWidgetConfig, text="export\nselection",
                                               style="widgetconfig.TLabel")
        self.label4exportselection.grid(sticky=W, row=810, column=1)
        self.frame4exportselection = ttk.Frame(self.frameWidgetConfig)
        self.frame4exportselection.grid(row=810, column=2)
        radioTrue4exportselection = ttk.Radiobutton(self.frame4exportselection, text="True",
                                                    variable=self.bool_exportselection, value=True)
        radioTrue4exportselection.grid(sticky=W, row=1, column=1, padx=20)
        radioFalse4exportselection = ttk.Radiobutton(self.frame4exportselection, text="False",
                                                     variable=self.bool_exportselection, value=False)
        radioFalse4exportselection.grid(sticky=E, row=1, column=2, padx=20)

        ### font Sec
        self.label4font = ttk.Label(self.frameWidgetConfig, text="font", style="widgetconfig.TLabel")
        self.label4font.grid(sticky=W, row=900, column=1)
        self.frame4font = ttk.Frame(self.frameWidgetConfig)
        self.frame4font.grid(row=900, column=2, )
        self.entry4font = Entry(self.frame4font, relief=FLAT)
        self.entry4font.pack(side=LEFT, padx=3)
        button4font = ttk.Button(self.frame4font, text=">>", style="moreOptions.TButton",
                                 command=self.executeFontToplevel)
        button4font.pack(side=LEFT)

        ### foreground Sec
        def color4foreground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4foreground.delete(0, END)
            windowObject.entry4foreground.insert(END,color)
        self.label4foreground = ttk.Label(self.frameWidgetConfig, text="foreground", style="widgetconfig.TLabel")
        self.label4foreground.grid(sticky=W, row=1000, column=1)
        self.frame4foreground = ttk.Frame(self.frameWidgetConfig)
        self.frame4foreground.grid(row=1000, column=2)
        self.entry4foreground = Entry(self.frame4foreground, relief=FLAT)
        self.entry4foreground.pack(side=LEFT, padx=3)
        button4foreground = ttk.Button(self.frame4foreground, text=">>", style="moreOptions.TButton",
                                       command = color4foreground)
        button4foreground.pack(side=LEFT)

        ### format Sec
        self.label4format = ttk.Label(self.frameWidgetConfig, text="format", style="widgetconfig.TLabel")
        self.label4format.grid(sticky=W, row=1010, column=1)
        self.frame4format = ttk.Frame(self.frameWidgetConfig)
        self.frame4format.grid(row=1010, column=2)
        self.entry4format = Entry(self.frame4format, relief=FLAT)
        self.entry4format.pack(side=LEFT, padx=3)
        blank_label4format = ttk.Label(self.frame4format, text="", anchor=W, width=3)
        blank_label4format.pack(side=LEFT)

        ### from_ Sec
        # self.int_from_ = IntVar()
        self.label4from_ = ttk.Label(self.frameWidgetConfig, text="from_", style="widgetconfig.TLabel")
        self.label4from_.grid(sticky=W, row=1020, column=1)
        self.frame4from_ = ttk.Frame(self.frameWidgetConfig)
        self.frame4from_.grid(row=1020, column=2)
        self.entry4from_ = Entry(self.frame4from_, relief=FLAT,)
                                 # textvariable = self.int_from_)
        self.entry4from_.pack(side=LEFT, padx=3)
        blank_label4from_ = ttk.Label(self.frame4from_, text="", anchor=W, width=3)
        blank_label4from_.pack(side=LEFT)

        ### handlepad
        # self.int_handlepad = IntVar()
        # self.int_handlepad.set(8)
        self.label4handlepad = ttk.Label(self.frameWidgetConfig, text="handlepad", style="widgetconfig.TLabel")
        self.label4handlepad.grid(sticky=W, row=1030, column=1)
        self.spinbox4handlepad = ttk.Spinbox(self.frameWidgetConfig, from_=1, increment=1, to=50, width=10, wrap=True,)
                                             # textvariable = self.int_handlepad)
        self.spinbox4handlepad.insert(END, 8)
        self.spinbox4handlepad.grid(row=1030, column=2)

        ### handlesize
        # self.int_handlesize = IntVar(value = 8)
        self.label4handlesize = ttk.Label(self.frameWidgetConfig, text="handlesize", style="widgetconfig.TLabel")
        self.label4handlesize.grid(sticky=W, row=1040, column=1)
        self.spinbox4handlesize = ttk.Spinbox(self.frameWidgetConfig, from_=1, increment=1, to=50, width=10, wrap=True,)
                                              # textvariable = self.int_handlesize)
        self.spinbox4handlesize.insert(END, 8)
        self.spinbox4handlesize.grid(row=1040, column=2)

        ### height Sec
        self.label4height = ttk.Label(self.frameWidgetConfig, text="height", style="widgetconfig.TLabel")
        self.label4height.grid(sticky=W, row=1100, column=1)
        self.spinbox4height = ttk.Spinbox(self.frameWidgetConfig, from_=1, increment = 5, to = self.label4height.winfo_screenheight(), width=10, wrap = True)
        self.spinbox4height.grid(row=1100, column=2)

        ### highlightbackground Sec
        def color4highlightbackground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4highlightbackground.delete(0, END)
            windowObject.entry4highlightbackground.insert(END,color)

        self.label4highlightbackground = ttk.Label(self.frameWidgetConfig, text="highlight\nbackground",
                                                   style="widgetconfig.TLabel", )
        self.label4highlightbackground.grid(sticky=W, row=1200, column=1)
        self.frame4highlightbackground = ttk.Frame(self.frameWidgetConfig)
        self.frame4highlightbackground.grid(row=1200, column=2)
        self.entry4highlightbackground = Entry(self.frame4highlightbackground, relief=FLAT)
        self.entry4highlightbackground.pack(side=LEFT, padx=3)
        button4highlightbackground = ttk.Button(self.frame4highlightbackground, text=">>", style="moreOptions.TButton",
                                                command = color4highlightbackground)
        button4highlightbackground.pack(side=LEFT)

        ### highlightcolor Sec
        def color4highlightcolor():
            color = colorchooser.askcolor()[1]
            windowObject.entry4highlightcolor.delete(0, END)
            windowObject.entry4highlightcolor.insert(END,color)

        self.label4highlightcolor = ttk.Label(self.frameWidgetConfig, text="highlight\ncolor",
                                              style="widgetconfig.TLabel")
        self.label4highlightcolor.grid(sticky=W, row=1300, column=1)
        self.frame4highlightcolor = ttk.Frame(self.frameWidgetConfig)
        self.frame4highlightcolor.grid(row=1300, column=2)
        self.entry4highlightcolor = Entry(self.frame4highlightcolor, relief=FLAT)
        self.entry4highlightcolor.pack(side=LEFT, padx=3)
        button4highlightcolor = ttk.Button(self.frame4highlightcolor, text=">>", style="moreOptions.TButton",
                                           command = color4highlightcolor)
        button4highlightcolor.pack(side=LEFT)

        ### highlightthickness Sec
        # self.int_highlightthickness = IntVar()
        self.label4highlightthickness = ttk.Label(self.frameWidgetConfig, text="highlight\nthickness",
                                                  style="widgetconfig.TLabel")
        self.label4highlightthickness.grid(sticky=W, row=1400, column=1)
        self.spinbox4highlightthickness = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=50, increment=2, width=10,
                                                      wrap=True,)
                                                                # textvariable = self.int_highlightthickness)
        self.spinbox4highlightthickness.grid(row=1400, column=2)

        ### image Sec
        # def command4scale_imagewidth(value):
        #     value = float(value)
        #     value = int(value)
        #     windowObject.dictCountImage[f"Image{windowObject.count_image_instances-1}"].config(width = value, height = value)
        # def command4scale_imageheight():
        #     pass

        def filedialog4image():
            file_get = filedialog.askopenfile(filetypes = [("Portable Network Graphics (PNG)", "*png")])

            try:
                file_get.name
            # label_adjustimagewidth = ttk.Label(self.frameWidgetConfig, text = "adjust\nimage\nwidth",
            #                                    style = "widgetconfig.TLabel")
            # label_adjustimagewidth.grid(row = 1406, column = 1)
            # scale_imagewidth = ttk.Scale(self.frameWidgetConfig, from_ = 0, to = 999, command = command4scale_imagewidth)
            # scale_imagewidth.grid(row = 1406, column = 2,)
            #
            # label_adjustimageheight = ttk.Label(self.frameWidgetConfig, text="adjust\nimage\nheight",
            #                                     style="widgetconfig.TLabel")
            # label_adjustimageheight.grid(row=1407, column=1)
            # scale_imageheight = ttk.Scale(self.frameWidgetConfig, from_ = 0, to = 999)
            # scale_imageheight.grid(row = 1407, column = 2)
            except:
                pass
            else:
                windowObject.dictCountImage[f"Image{windowObject.count_image_instances}"] = PhotoImage(master = windowDesign,
                                                file = file_get.name, name = f"image_{windowObject.count_image_instances}")
                print(file_get.name)
                windowObject.entry4image.delete(0, END)
                windowObject.entry4image.insert(END, f"image_{windowObject.count_image_instances}")


                windowObject.implementImage_determine = 22
            # except:
            #     pass
            # arrangeObject.refreshAttributes()
            # windowObject.count_image_instances += 1

        self.label4image = ttk.Label(self.frameWidgetConfig, text="image", style="widgetconfig.TLabel")
        self.label4image.grid(sticky=W, row=1405, column=1)
        self.frame4image = ttk.Frame(self.frameWidgetConfig)
        self.frame4image.grid(row=1405, column=2)
        self.entry4image = Entry(self.frame4image, relief=FLAT)
        self.entry4image.pack(side=LEFT, padx=3)
        button4image = ttk.Button(self.frame4image, text=">>", style="moreOptions.TButton", command = filedialog4image)
        button4image.pack(side=LEFT)

        ### inactiveselectbackground Sec
        def color4inactiveselectbackground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4inactiveselectbackground.delete(0, END)
            windowObject.entry4inactiveselectbackground.insert(END,color)

        self.label4inactiveselectbackground = ttk.Label(self.frameWidgetConfig, text="inactive\nselect\nbackground",
                                                        style="widgetconfig.TLabel")
        self.label4inactiveselectbackground.grid(sticky=W, row=1409, column=1)
        self.frame4inactiveselectbackground = ttk.Frame(self.frameWidgetConfig)
        self.frame4inactiveselectbackground.grid(row=1409, column=2)
        self.entry4inactiveselectbackground = Entry(self.frame4inactiveselectbackground, relief=FLAT)
        self.entry4inactiveselectbackground.pack(side=LEFT, padx=3)
        button4inactiveselectbackground = ttk.Button(self.frame4inactiveselectbackground, text=">>",
                                                style="moreOptions.TButton", command = color4inactiveselectbackground)
        button4inactiveselectbackground.pack(side=LEFT)


        ### increment Sec
        # self.int_increment = IntVar()
        self.label4increment = ttk.Label(self.frameWidgetConfig, text="increment", style="widgetconfig.TLabel")
        self.label4increment.grid(sticky=W, row=1411, column=1)
        self.frame4increment = ttk.Frame(self.frameWidgetConfig)
        self.frame4increment.grid(row=1411, column=2)
        self.entry4increment = Entry(self.frame4increment, relief=FLAT, )
                                     # textvariable = self.int_increment)
        self.entry4increment.pack(side=LEFT, padx=3)
        button4increment = ttk.Button(self.frame4increment, text=">>", style="moreOptions.TButton")
        button4increment.pack(side=LEFT)

        ### indicatoron Sec
        self.bool_indicatoron = BooleanVar()
        self.bool_indicatoron.set(1)
        self.label4indicatoron = ttk.Label(self.frameWidgetConfig, text="indicatoron", style="widgetconfig.TLabel")
        self.label4indicatoron.grid(sticky=W, row=1412, column=1)
        self.frame4indicatoron = ttk.Frame(self.frameWidgetConfig)
        self.frame4indicatoron.grid(row=1412, column=2)
        radioTrue4indicatoron = ttk.Radiobutton(self.frame4indicatoron, text="True", variable=self.bool_indicatoron,
                                              value=True)
        radioTrue4indicatoron.grid(sticky=W, row=1, column=1, padx=20)
        radioFalse4indicatoron = ttk.Radiobutton(self.frame4indicatoron, text="False", variable=self.bool_indicatoron,
                                               value=False)
        radioFalse4indicatoron.grid(sticky=E, row=1, column=2, padx=20)

        ### insertbackground Sec
        def color4insertbackground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4insertbackground.delete(0, END)
            windowObject.entry4insertbackground.insert(END, color)

        self.label4insertbackground = ttk.Label(self.frameWidgetConfig, text="insert\nbackground",
                                                style="widgetconfig.TLabel")
        self.label4insertbackground.grid(sticky=W, row=1415, column=1)
        self.frame4insertbackground = ttk.Frame(self.frameWidgetConfig)
        self.frame4insertbackground.grid(row=1415, column=2)
        self.entry4insertbackground = Entry(self.frame4insertbackground, relief=FLAT)
        self.entry4insertbackground.pack(side=LEFT, padx=3)
        button4insertbackground = ttk.Button(self.frame4insertbackground, text=">>", style="moreOptions.TButton",
                                             command = color4insertbackground)
        button4insertbackground.pack(side=LEFT)

        ### insertborderwidth Sec
        # self.int_insertborderwidth = IntVar()
        self.label4insertborderwidth = ttk.Label(self.frameWidgetConfig, text="insert\nborderwidth",
                                                 style="widgetconfig.TLabel")
        self.label4insertborderwidth.grid(sticky=W, row=1420, column=1)
        self.spinbox4insertborderwidth = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=50, increment=2, width=10,
                                                     wrap=True,)
                                                     # textvariable = self.int_insertborderwidth)
        self.spinbox4insertborderwidth.grid(row=1420, column=2)

        ### insertofftime Sec
        # self.int_insertofftime = IntVar()
        self.label4insertofftime = ttk.Label(self.frameWidgetConfig, text="insert\nofftime",
                                             style="widgetconfig.TLabel")
        self.label4insertofftime.grid(sticky=W, row=1425, column=1)
        self.spinbox4insertofftime = ttk.Spinbox(self.frameWidgetConfig, from_=0, to=3000, increment=100, width=10,
                                                 wrap=True,)
                                                 # textvariable = self.int_insertofftime)
        self.spinbox4insertofftime.grid(row=1425, column=2)

        ### insertontime Sec
        # self.int_insertontime = IntVar()
        self.label4insertontime = ttk.Label(self.frameWidgetConfig, text="insert\nontime", style="widgetconfig.TLabel")
        self.label4insertontime.grid(sticky=W, row=1430, column=1)
        self.spinbox4insertontime = ttk.Spinbox(self.frameWidgetConfig, from_=0, to=3000, increment=100, width=10,
                                                wrap=True,)
                                                # textvariable = self.int_insertontime)
        self.spinbox4insertontime.grid(row=1430, column=2)

        ### insertunfocussed
        insertunfocusseds = ("hollow", "solid", "none")
        self.label4insertunfoccussed = ttk.Label(self.frameWidgetConfig, text="insert\nunfocussed",
                                                 style="widgetconfig.TLabel")
        self.label4insertunfoccussed.grid(sticky=W, row=1431, column=1)
        self.combo4insertunfoccussed = ttk.Combobox(self.frameWidgetConfig, values=insertunfocusseds)
        self.combo4insertunfoccussed.grid(row=1431, column=2, ipadx=5)

        ### insertwidth Sec
        # self.int_insertwidth = IntVar()
        self.label4insertwidth = ttk.Label(self.frameWidgetConfig, text="insert\nwidth", style="widgetconfig.TLabel")
        self.label4insertwidth.grid(sticky=W, row=1435, column=1)
        self.spinbox4insertwidth = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=50, increment=2, width=10, wrap=True)
                                               # textvariable = self.int_insertwidth)
        self.spinbox4insertwidth.grid(row=1435, column=2)

        ### invalidcommand Sec
        self.label4invalidcommand = ttk.Label(self.frameWidgetConfig, text="invalid\ncommand",
                                                   style="widgetconfig.TLabel", )
        self.label4invalidcommand.grid(sticky=W, row=1450, column=1)
        self.frame4invalidcommand = ttk.Frame(self.frameWidgetConfig)
        self.frame4invalidcommand.grid(row=1450, column=2)
        self.entry4invalidcommand = Entry(self.frame4invalidcommand, relief=FLAT)
        self.entry4invalidcommand.pack(side=LEFT, padx=3)
        button4invalidcommand = ttk.Button(self.frame4invalidcommand, text=">>", style="moreOptions.TButton")
        button4invalidcommand.pack(side=LEFT)

        ### Justify Sec
        justifys = ("left", "center", "right")
        self.label4justify = ttk.Label(self.frameWidgetConfig, text="justify", style="widgetconfig.TLabel")
        self.label4justify.grid(sticky=W, row=1460, column=1)
        self.combo4justify = ttk.Combobox(self.frameWidgetConfig, values = justifys)
        self.combo4justify.grid(row=1460, column=2, ipadx=5)

        ### label Sec
        self.label4label = ttk.Label(self.frameWidgetConfig, text="label", style="widgetconfig.TLabel")
        self.label4label.grid(sticky=W, row=1470, column=1)
        self.frame4label = ttk.Frame(self.frameWidgetConfig)
        self.frame4label.grid(row=1470, column=2)
        self.entry4label = Entry(self.frame4label, relief=FLAT)
        self.entry4label.pack(side=LEFT, padx=3)
        blank_label4label = ttk.Label(self.frame4label, text="", anchor=W, width=3)
        blank_label4label.pack(side=LEFT)

        ### labelanchor Sec
        labelanchors = ("nw", "n", "ne", "en", "e", "es", "wn", "w", "ws", "sw", "s", "se")
        self.label4labelanchor = ttk.Label(self.frameWidgetConfig, text="labelanchor", style="widgetconfig.TLabel")
        self.label4labelanchor.grid(sticky=W, row=1501, column=1)
        self.combo4labelanchor = ttk.Combobox(self.frameWidgetConfig, values=labelanchors)
        self.combo4labelanchor.grid(row=1501, column=2, ipadx=5)

        ### labelwidget Sec
        self.label4labelwidget = ttk.Label(self.frameWidgetConfig, text="labelwidget", style="widgetconfig.TLabel")
        self.label4labelwidget.grid(sticky=W, row=1502, column=1)
        self.frame4labelwidget = ttk.Frame(self.frameWidgetConfig)
        self.frame4labelwidget.grid(row=1502, column=2)
        self.entry4labelwidget = Entry(self.frame4labelwidget, relief=FLAT)
        self.entry4labelwidget.pack(side=LEFT, padx=3)
        blank_label4labelwidget = ttk.Label(self.frame4labelwidget, text="", anchor=W, width=3)
        blank_label4labelwidget.pack(side=LEFT)

        ### length Sec
        self.label4length = ttk.Label(self.frameWidgetConfig, text="length", style="widgetconfig.TLabel")
        self.label4length.grid(sticky=W, row=1503, column=1)
        self.spinbox4length = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=300, increment=2, width=10, wrap=True)
        self.spinbox4length.grid(row=1503, column=2)

        ### listvariable Sec
        self.label4listvariable = ttk.Label(self.frameWidgetConfig, text="list\nvariable",
                                              style="widgetconfig.TLabel", )
        self.label4listvariable.grid(sticky=W, row=1504, column=1)
        self.frame4listvariable = ttk.Frame(self.frameWidgetConfig)
        self.frame4listvariable.grid(row=1504, column=2)
        self.entry4listvariable = Entry(self.frame4listvariable, relief=FLAT)
        self.entry4listvariable.pack(side=LEFT, padx=3)
        button4listvariable = ttk.Button(self.frame4listvariable, text=">>", style="moreOptions.TButton")
        button4listvariable.pack(side=LEFT)

        ### maxundo
        # self.int_maxundo = IntVar()
        self.label4maxundo = ttk.Label(self.frameWidgetConfig, text="maxundo", style="widgetconfig.TLabel")
        self.label4maxundo.grid(sticky=W, row=1505, column=1)
        self.frame4maxundo = ttk.Frame(self.frameWidgetConfig)
        self.frame4maxundo.grid(row=1505, column=2)
        self.entry4maxundo = Entry(self.frame4maxundo, relief=FLAT,)
                                   # textvariable = self.int_maxundo)
        self.entry4maxundo.pack(side=LEFT, padx=3)
        blank_label4maxundo = ttk.Label(self.frame4maxundo, text="", anchor=W, width=3)
        blank_label4maxundo.pack(side=LEFT)

        ### menu Sec
        self.label4menu = ttk.Label(self.frameWidgetConfig, text="menu",
                                            style="widgetconfig.TLabel", )
        self.label4menu.grid(sticky=W, row=1506, column=1)
        self.frame4menu = ttk.Frame(self.frameWidgetConfig)
        self.frame4menu.grid(row=1506, column=2)
        self.entry4menu = Entry(self.frame4menu, relief=FLAT)
        self.entry4menu.pack(side=LEFT, padx=3)
        button4menu = ttk.Button(self.frame4menu, text=">>", style="moreOptions.TButton")
        button4menu.pack(side=LEFT)

        ### offrelief Sec
        offreliefs = ("flat", "raised", "sunken", "groove", "ridge", "solid")
        self.label4offrelief = ttk.Label(self.frameWidgetConfig, text="offrelief", style="widgetconfig.TLabel")
        self.label4offrelief.grid(sticky=W, row=1507, column=1)
        self.combo4offrelief = ttk.Combobox(self.frameWidgetConfig, values=offreliefs)
        self.combo4offrelief.grid(row=1507, column=2, ipadx=5)

        ### opaqueresize Sec
        self.bool_opaqueresize = BooleanVar()
        self.bool_opaqueresize.set(1)
        self.label4opaqueresize = ttk.Label(self.frameWidgetConfig, text="opaque\nresize", style="widgetconfig.TLabel")
        self.label4opaqueresize.grid(sticky=W, row=1508, column=1)
        self.frame4opaqueresize = ttk.Frame(self.frameWidgetConfig)
        self.frame4opaqueresize.grid(row=1508, column=2)
        radioTrue4opaqueresize = ttk.Radiobutton(self.frame4opaqueresize, text="True", variable=self.bool_opaqueresize,
                                              value=True)
        radioTrue4opaqueresize.grid(sticky=W, row=1, column=1, padx=20)
        radioFalse4opaqueresize = ttk.Radiobutton(self.frame4opaqueresize, text="False", variable=self.bool_opaqueresize,
                                               value=False)
        radioFalse4opaqueresize.grid(sticky=E, row=1, column=2, padx=20)

        ### orient Sec
        orient = ("horizontal", "vertical")
        self.label4orient = label4cursor = ttk.Label(self.frameWidgetConfig, text="orient", style="widgetconfig.TLabel")
        self.label4orient.grid(sticky=W, row=1510, column=1)
        self.combo4orient = ttk.Combobox(self.frameWidgetConfig, values = orient)
        self.combo4orient.grid(row=1510, column=2, ipadx=5)

        ### overrelief Sec
        overreliefs = ("flat", "raised", "sunken", "groove", "ridge", "solid")
        self.label4overrelief = ttk.Label(self.frameWidgetConfig, text="overrelief", style="widgetconfig.TLabel")
        self.label4overrelief.grid(sticky=W, row=1515, column=1)
        self.combo4overrelief = ttk.Combobox(self.frameWidgetConfig, values = overreliefs)
        self.combo4overrelief.grid(row=1515, column=2, ipadx=5)

        ### padx Sec
        # self.int_padx = IntVar()
        self.label4padx = ttk.Label(self.frameWidgetConfig, text="padx", style="widgetconfig.TLabel")
        self.label4padx.grid(sticky=W, row=1600, column=1)
        self.spinbox4padx = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=50, increment=2, width=10, wrap=True)
                                        # textvariable = self.int_padx)
        self.spinbox4padx.grid(row=1600, column=2)

        ### pady Sec
        # self.int_pady = IntVar()
        self.label4pady = ttk.Label(self.frameWidgetConfig, text="pady", style="widgetconfig.TLabel")
        self.label4pady.grid(sticky=W, row=1700, column=1)
        self.spinbox4pady = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=50, increment=2, width=10, wrap=True,)
                                        # textvariable = self.int_pady)
        self.spinbox4pady.grid(row=1700, column=2)

        ### readonlybackground
        def color4readonlybackground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4readonlybackground.delete(0, END)
            windowObject.entry4readonlybackground.insert(END,color)

        self.label4readonlybackground = ttk.Label(self.frameWidgetConfig, text="readonly\nbackground",
                                                style="widgetconfig.TLabel")
        self.label4readonlybackground.grid(sticky=W, row=1710, column=1)
        self.frame4readonlybackground = ttk.Frame(self.frameWidgetConfig)
        self.frame4readonlybackground.grid(row=1710, column=2)
        self.entry4readonlybackground = Entry(self.frame4readonlybackground, relief=FLAT)
        self.entry4readonlybackground.pack(side=LEFT, padx=3)
        button4readonlybackground = ttk.Button(self.frame4readonlybackground, text=">>", style="moreOptions.TButton",
                                               command = color4readonlybackground)
        button4readonlybackground.pack(side=LEFT)

        ### relief Sec
        reliefs = ("flat", "raised", "sunken", "groove", "ridge", "solid")
        self.label4relief = ttk.Label(self.frameWidgetConfig, text="relief", style="widgetconfig.TLabel")
        self.label4relief.grid(sticky=W, row=1800, column=1)
        self.combo4relief = ttk.Combobox(self.frameWidgetConfig, values = reliefs)
        self.combo4relief.grid(row=1800, column=2, ipadx=5)

        ### repeatdelay Sec
        # self.int_repeatdelay = IntVar()
        self.label4repeatdelay = ttk.Label(self.frameWidgetConfig, text="repeat\ndelay", style="widgetconfig.TLabel")
        self.label4repeatdelay.grid(sticky=W, row=1815, column=1)
        self.spinbox4repeatdelay = ttk.Spinbox(self.frameWidgetConfig, from_=0, to=3000, increment=100, width=10,
                                               wrap=True,)
                                               # textvariable = self.int_repeatdelay)
        self.spinbox4repeatdelay.grid(row=1815, column=2)

        ### repeatinterval
        # self.int_repeatinterval = IntVar()
        self.label4repeatinterval = ttk.Label(self.frameWidgetConfig, text="repeat\ninterval",
                                              style="widgetconfig.TLabel")
        self.label4repeatinterval.grid(sticky=W, row=1820, column=1)
        self.spinbox4repeatinterval = ttk.Spinbox(self.frameWidgetConfig, from_=0, to=3000, increment=100, width=10,
                                                  wrap=True,)
                                                  # textvariable = self.int_repeatinterval)
        self.spinbox4repeatinterval.grid(row=1820, column=2)

        ### resolution
        # self.int_resolution = IntVar()
        self.label4resolution = ttk.Label(self.frameWidgetConfig, text="resolution",
                                                  style="widgetconfig.TLabel")
        self.label4resolution.grid(sticky=W, row=1821, column=1)
        self.frame4resolution = ttk.Frame(self.frameWidgetConfig)
        self.frame4resolution.grid(row=1821, column=2)
        self.entry4resolution = Entry(self.frame4resolution, relief=FLAT,)
                                      # textvariable = self.int_resolution)
        self.entry4resolution.pack(side=LEFT, padx=3)
        blank_label4resolution = ttk.Label(self.frame4resolution, text="", anchor=W, width=3)
        blank_label4resolution.pack(side=LEFT)

        ### sashcursor
        sashcursors = (
        "arrow", "based_arrow_down", "based_arrow_up", "boat", "bogosity", "bottom_left_corner", "bottom_right_corner",
        "bottom_side", "bottom_tee", "box_spiral", "center_ptr", "circle", "clock", "coffee_mug", "cross",
        "cross_reverse", "crosshair", "diamond_cross", "dot", "dotbox", "double_arrow", "draft_large", "draft_small",
        "draped_box", "exchange", "fleur", "gobbler", "gumby", "hand1", "hand2", "heart", "icon", "iron_cross",
        "left_ptr", "left_side", "left_tee", "leftbutton", "ll_angle", "lr_angle", "man", "middlebutton", "mouse",
        "pencil", "pirate", "plus", "question_arrow", "right_ptr", "right_side", "right_tee", "rightbutton",
        "rtl_logo", "sailboat", "sb_down_arrow", "sb_h_double_arrow", "sb_left_arrow", "sb_right_arrow", "sb_up_arrow",
        "sb_v_double_arrow", "shuttle", "sizing", "spider", "spraycan", "star", "target", "tcross", "top_left_arrow",
        "top_left_corner", "top_right_corner", "top_side", "top_tee", "trek", "ul_angle", "umbrella", "ur_angle",
        "watch", "xterm", "X_cursor")
        self.label4sashcursor = ttk.Label(self.frameWidgetConfig, text="sash\ncursor", style="widgetconfig.TLabel")
        self.label4sashcursor.grid(sticky=W, row=1822, column=1)
        self.combo4sashcursor = ttk.Combobox(self.frameWidgetConfig, values=sashcursors)
        self.combo4sashcursor.grid(row=1822, column=2, ipadx=5)

        ### sashpad Sec
        def command4sashpad(new_value):
            new_value = self.int_sashpad.get()
            windowObject.int_sashpad.set(new_value)

        self.int_sashpad = IntVar(value = 0,)
        self.label4sashpad = ttk.Label(self.frameWidgetConfig, text = "sash\npad", style = "widgetconfig.TLabel")
        self.label4sashpad.grid(sticky = W, row = 1823, column = 1)
        self.frame4sashpad = Frame(self.frameWidgetConfig, )
        self.frame4sashpad.grid(sticky = W, row = 1823, column = 2, padx = 25)
        self.label24sashpad = Label(self.frame4sashpad, textvariable = self.int_sashpad)
        self.label24sashpad.pack()
        self.scale4sashpad = ttk.Scale(self.frame4sashpad, from_ = 1, to = 50,
                                            variable = self.int_sashpad, command = command4sashpad)
        self.scale4sashpad.pack()

        ### sashrelief Sec
        sashreliefs = ("flat", "raised", "sunken", "groove", "ridge", "solid")
        self.label4sashrelief = ttk.Label(self.frameWidgetConfig, text="sash\nrelief", style="widgetconfig.TLabel")
        self.label4sashrelief.grid(sticky=W, row=1824, column=1)
        self.combo4sashrelief = ttk.Combobox(self.frameWidgetConfig, values=sashreliefs)
        self.combo4sashrelief.grid(row=1824, column=2, ipadx=5)

        ### sashwidth Sec
        def command4sashwidth(new_value):
            new_value = self.int_sashwidth.get()
            windowObject.int_sashwidth.set(new_value)

        self.int_sashwidth = IntVar(value = 3)
        self.label4sashwidth = ttk.Label(self.frameWidgetConfig, text = "sash\nwidth", style = "widgetconfig.TLabel")
        self.label4sashwidth.grid(sticky = W, row = 1825, column = 1)
        self.frame4sashwidth = Frame(self.frameWidgetConfig, )
        self.frame4sashwidth.grid(sticky = W, row = 1825, column = 2, padx = 25)
        self.label24sashwidth = Label(self.frame4sashwidth, textvariable = self.int_sashwidth)
        self.label24sashwidth.pack()
        self.scale4sashwidth = ttk.Scale(self.frame4sashwidth, from_ = 1, to = 50,
                                            variable = self.int_sashwidth, command = command4sashwidth)
        self.scale4sashwidth.pack()

        ### showhandle Sec
        self.bool_showhandle = BooleanVar()
        self.bool_showhandle.set(True)
        self.label4showhandle = ttk.Label(self.frameWidgetConfig, text="show\nhandle", style="widgetconfig.TLabel")
        self.label4showhandle.grid(sticky=W, row=1826, column=1)
        self.frame4showhandle = ttk.Frame(self.frameWidgetConfig)
        self.frame4showhandle.grid(row=1826, column=2)
        radioTrue4showhandle = ttk.Radiobutton(self.frame4showhandle, text="True", variable=self.bool_showhandle,
                                                 value=True)
        radioTrue4showhandle.grid(sticky=W, row=1, column=1, padx=20)
        radioFalse4showhandle = ttk.Radiobutton(self.frame4showhandle, text="False",
                                                  variable=self.bool_showhandle,
                                                  value=False)
        radioFalse4showhandle.grid(sticky=E, row=1, column=2, padx=20)


        ### selectbackground Sec
        def color4selectbackground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4selectbackground.delete(0, END)
            windowObject.entry4selectbackground.insert(END,color)
        self.label4selectbackground = ttk.Label(self.frameWidgetConfig, text="select\nbackground",
                                                style="widgetconfig.TLabel")
        self.label4selectbackground.grid(sticky=W, row=1828, column=1)
        self.frame4selectbackground = ttk.Frame(self.frameWidgetConfig)
        self.frame4selectbackground.grid(row=1828, column=2)
        self.entry4selectbackground = Entry(self.frame4selectbackground, relief=FLAT)
        self.entry4selectbackground.pack(side=LEFT, padx=3)
        button4selectbackground = ttk.Button(self.frame4selectbackground, text=">>", style="moreOptions.TButton",
                                             command = color4selectbackground)
        button4selectbackground.pack(side=LEFT)

        ### selectborderwidth Sec
        # self.int_selectborderwidth = IntVar()
        self.label4selectborderwidth = ttk.Label(self.frameWidgetConfig, text="select\nborderwidth",
                                                 style="widgetconfig.TLabel")
        self.label4selectborderwidth.grid(sticky=W, row=1830, column=1)
        self.spinbox4selectborderwidth = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=50, increment=2, width=10,
                                                     wrap=True,)
                                                     # textvariable = self.int_selectborderwidth)
        self.spinbox4selectborderwidth.grid(row=1830, column=2)

        ### selectcolor Sec
        def color4selectcolor():
            color = colorchooser.askcolor()[1]
            windowObject.entry4selectcolor.delete(0, END)
            windowObject.entry4selectcolor.insert(END,color)
        self.label4selectcolor = ttk.Label(self.frameWidgetConfig, text="selectcolor",
                                      style="widgetconfig.TLabel")
        self.label4selectcolor.grid(sticky=W, row=1831, column=1)
        self.frame4selectcolor = ttk.Frame(self.frameWidgetConfig)
        self.frame4selectcolor.grid(row=1831, column=2)
        self.entry4selectcolor = Entry(self.frame4selectcolor, relief=FLAT)
        self.entry4selectcolor.pack(side=LEFT, padx=3)
        button4selectcolor = ttk.Button(self.frame4selectcolor, text=">>", style="moreOptions.TButton",
                                        command = color4selectcolor)
        button4selectcolor.pack(side=LEFT)

        ### selectforeground Sec
        def color4selectforeground():
            color = colorchooser.askcolor()[1]
            windowObject.entry4selectforeground.delete(0, END)
            windowObject.entry4selectforeground.insert(END,color)
        self.label4selectforeground = ttk.Label(self.frameWidgetConfig, text="select\nforeground",
                                                style="widgetconfig.TLabel")
        self.label4selectforeground.grid(sticky=W, row=1835, column=1)
        self.frame4selectforeground = ttk.Frame(self.frameWidgetConfig)
        self.frame4selectforeground.grid(row=1835, column=2)
        self.entry4selectforeground = Entry(self.frame4selectforeground, relief=FLAT)
        self.entry4selectforeground.pack(side=LEFT, padx=3)
        button4selectforeground = ttk.Button(self.frame4selectforeground, text=">>", style="moreOptions.TButton",
                                             command = color4selectforeground)
        button4selectforeground.pack(side=LEFT)

        ### selectimage Sec
        self.label4selectimage = ttk.Label(self.frameWidgetConfig, text="selectimage", style="widgetconfig.TLabel")
        self.label4selectimage.grid(sticky=W, row=1836, column=1)
        self.frame4selectimage = ttk.Frame(self.frameWidgetConfig)
        self.frame4selectimage.grid(row=1836, column=2)
        self.entry4selectimage = Entry(self.frame4selectimage, relief=FLAT)
        self.entry4selectimage.pack(side=LEFT, padx=3)
        button4selectimage = ttk.Button(self.frame4selectimage, text=">>", style="moreOptions.TButton")
        button4selectimage.pack(side=LEFT)

        ### selectmode Sec
        selectmodes = ("browse", "single", "multiple", "extended")
        self.label4selectmode = ttk.Label(self.frameWidgetConfig, text="select\nmode", style="widgetconfig.TLabel")
        self.label4selectmode.grid(sticky=W, row=1837, column=1)
        self.combo4selectmode = ttk.Combobox(self.frameWidgetConfig, values = selectmodes)
        self.combo4selectmode.grid(row=1837, column=2, ipadx=5)

        ### show Sec
        self.label4show = ttk.Label(self.frameWidgetConfig, text="show", style="widgetconfig.TLabel")
        self.label4show.grid(sticky=W, row=1838, column=1)
        self.frame4show = ttk.Frame(self.frameWidgetConfig)
        self.frame4show.grid(row=1838, column=2)
        self.entry4show = Entry(self.frame4show, relief=FLAT)
        self.entry4show.pack(side=LEFT, padx=3)
        button4show = ttk.Button(self.frame4show, text=">>", style="moreOptions.TButton")
        button4show.pack(side=LEFT)

        ### showvalue Sec
        self.bool_showvalue = BooleanVar()
        self.bool_showvalue.set(1)
        self.label4showvalue = ttk.Label(self.frameWidgetConfig, text="showvalue", style="widgetconfig.TLabel")
        self.label4showvalue.grid(sticky=W, row=1839, column=1)
        self.frame4showvalue = ttk.Frame(self.frameWidgetConfig)
        self.frame4showvalue.grid(row=1839, column=2)
        radioTrue4showvalue = ttk.Radiobutton(self.frame4showvalue, text="True", variable=self.bool_showvalue,
                                              value=True)
        radioTrue4showvalue.grid(sticky=W, row=1, column=1, padx=20)
        radioFalse4showvalue = ttk.Radiobutton(self.frame4showvalue, text="False", variable=self.bool_showvalue,
                                               value=False)
        radioFalse4showvalue.grid(sticky=E, row=1, column=2, padx=20)

        ### sliderlength Sec
        def command4sliderlength(new_value):
            new_value = self.int_sliderlength.get()
            windowObject.int_sliderlength.set(new_value)

        self.int_sliderlength = IntVar(value = 30)
        self.label4sliderlength = ttk.Label(self.frameWidgetConfig, text = "slider\nlength", style = "widgetconfig.TLabel")
        self.label4sliderlength.grid(sticky = W, row = 1840, column = 1)
        self.frame4sliderlength = Frame(self.frameWidgetConfig, )
        self.frame4sliderlength.grid(sticky = W, row = 1840, column = 2, padx = 25)
        self.label24sliderlength = Label(self.frame4sliderlength, text = self.int_sliderlength.get())
        self.label24sliderlength.pack()
        self.scale4sliderlength = ttk.Scale(self.frame4sliderlength, from_ = 1, to = 500,
                                            variable = self.int_sliderlength, command = command4sliderlength)
        self.scale4sliderlength.pack()

        ### sliderrelief Sec
        sliderreliefs = ("flat", "raised", "sunken", "groove", "ridge", "solid")
        self.label4sliderrelief = ttk.Label(self.frameWidgetConfig, text="slider\nrelief", style="widgetconfig.TLabel")
        self.label4sliderrelief.grid(sticky=W, row=1841, column=1)
        self.combo4sliderrelief = ttk.Combobox(self.frameWidgetConfig, values=sliderreliefs)
        self.combo4sliderrelief.grid(row=1841, column=2, ipadx=5)

        ### spacing1 Sec
        # self.int_spacing1 = IntVar()
        self.label4spacing1 = ttk.Label(self.frameWidgetConfig, text="spacing1",
                                                 style="widgetconfig.TLabel")
        self.label4spacing1.grid(sticky=W, row=1843, column=1)
        self.spinbox4spacing1 = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=50, increment=2, width=10,
                                                     wrap=True)
                                            # textvariable = self.int_spacing1)
        self.spinbox4spacing1.grid(row=1843, column=2)

        ### spacing2 Sec
        # self.int_spacing2 = IntVar()
        self.label4spacing2 = ttk.Label(self.frameWidgetConfig, text="spacing2",
                                        style="widgetconfig.TLabel")
        self.label4spacing2.grid(sticky=W, row=1844, column=1)
        self.spinbox4spacing2 = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=50, increment=2, width=10,
                                            wrap=True,)
                                            # textvariable = self.int_spacing2)
        self.spinbox4spacing2.grid(row=1844, column=2)

        ### spacing3 Sec
        # self.int_spacing3 = IntVar()
        self.label4spacing3 = ttk.Label(self.frameWidgetConfig, text="spacing3",
                                        style="widgetconfig.TLabel")
        self.label4spacing3.grid(sticky=W, row=1845, column=1)
        self.spinbox4spacing3 = ttk.Spinbox(self.frameWidgetConfig, from_=1, to=50, increment=2, width=10,
                                            wrap=True,)
                                            # textvariable = self.int_spacing3)
        self.spinbox4spacing3.grid(row=1845, column=2)

        ### state Sec
        states = ("active", "disabled", "normal")
        self.label4state = ttk.Label(self.frameWidgetConfig, text="state", style="widgetconfig.TLabel")
        self.label4state.grid(sticky=W, row=1848, column=1)
        self.combo4state = ttk.Combobox(self.frameWidgetConfig, values = states)
        self.combo4state.grid(row=1848, column=2, ipadx=5)

        ### tabs Sec
        self.label4tabs = ttk.Label(self.frameWidgetConfig, text="tabs", style="widgetconfig.TLabel")
        self.label4tabs.grid(sticky=W, row=1850, column=1)
        self.frame4tabs = ttk.Frame(self.frameWidgetConfig)
        self.frame4tabs.grid(row=1850, column=2)
        self.entry4tabs = Entry(self.frame4tabs, relief=FLAT, )
        self.entry4tabs.pack(side=LEFT, padx=3)
        blank_label4tabs = ttk.Label(self.frame4tabs, text="", anchor=W, width=3)
        blank_label4tabs.pack(side=LEFT)

        ### takefocus Sec
        self.bool_takefocus = BooleanVar()
        self.bool_takefocus.set(1)
        self.label4takefocus = ttk.Label(self.frameWidgetConfig, text="takefocus", style="widgetconfig.TLabel")
        self.label4takefocus.grid(sticky=W, row=1900, column=1)
        self.frame4takefocus = ttk.Frame(self.frameWidgetConfig)
        self.frame4takefocus.grid(row=1900, column=2)
        radioTrue4takefocus = ttk.Radiobutton(self.frame4takefocus, text="True", variable=self.bool_takefocus, value=True)
        radioTrue4takefocus.grid(sticky=W, row=1, column=1, padx=20)
        radioFalse4takefocus = ttk.Radiobutton(self.frame4takefocus, text="False", variable=self.bool_takefocus, value=False)
        radioFalse4takefocus.grid(sticky=E, row=1, column=2, padx=20)

        ### text Sec
        self.label4text = ttk.Label(self.frameWidgetConfig, text="text", style="widgetconfig.TLabel")
        self.label4text.grid(sticky=W, row=2000, column=1)
        self.frame4text = ttk.Label(self.frameWidgetConfig)
        self.frame4text.grid(row=2000, column=2)
        self.entry4text = Entry(self.frame4text,  relief = FLAT)
        self.entry4text.grid(row=1, column=1, padx = 3 )
        button4text = ttk.Button(self.frame4text, text = ">>", style = "moreOptions.TButton")
        button4text.grid(row = 1, column = 2,)
        xscrollbar4text = ttk.Scrollbar(self.frame4text, orient=HORIZONTAL, command=self.entry4text.xview)
        xscrollbar4text.grid(sticky=EW, row=2, column=1, )
        self.entry4text.config(xscrollcommand=xscrollbar4text.set)

        ### textvariable Sec
        self.label4textvariable = ttk.Label(self.frameWidgetConfig, text="text\nvariable", style="widgetconfig.TLabel")
        self.label4textvariable.grid(sticky=W, row=2005, column=1)
        self.frame4textvariable = ttk.Frame(self.frameWidgetConfig)
        self.frame4textvariable.grid(row=2005, column=2)
        self.entrytextvariable = Entry(self.frame4textvariable, relief=FLAT, )
        self.entrytextvariable.pack(side=LEFT, padx=3)
        blank_label4textvariable = ttk.Label(self.frame4textvariable, text="", anchor=W, width=3)
        blank_label4textvariable.pack(side=LEFT)

        ### tickinterval Sec
        # self.int_tickinterval = IntVar()
        self.label4tickinterval = ttk.Label(self.frameWidgetConfig, text="tick\ninterval",
                                          style="widgetconfig.TLabel")
        self.label4tickinterval.grid(sticky=W, row=2006, column=1)
        self.frame4tickinterval = ttk.Frame(self.frameWidgetConfig)
        self.frame4tickinterval.grid(row=2006, column=2)
        self.entry4tickinterval = Entry(self.frame4tickinterval, relief=FLAT,)
                                        # textvariable = self.int_tickinterval)
        self.entry4tickinterval.pack(side=LEFT, padx=3)
        blank_label4tickinterval = ttk.Label(self.frame4tickinterval, text="", anchor=W, width=3)
        blank_label4tickinterval.pack(side=LEFT)

        ### to Sec
        # self.int_to = IntVar()
        self.label4to = ttk.Label(self.frameWidgetConfig, text="to", style="widgetconfig.TLabel")
        self.label4to.grid(sticky=W, row=2011, column=1)
        self.frame4to = ttk.Frame(self.frameWidgetConfig)
        self.frame4to.grid(row=2011, column=2)
        self.entry4to = Entry(self.frame4to, relief=FLAT, )
                              # textvariable = self.int_to)
        self.entry4to.pack(side=LEFT, padx=3)
        blank_label4to = ttk.Label(self.frame4to, text="", anchor=W, width=3)
        blank_label4to.pack(side=LEFT)

        ### troughcolor Sec
        def color4troughcolor():
            color = colorchooser.askcolor()[1]
            windowObject.entry4troughcolor.delete(0, END)
            windowObject.entry4troughcolor.insert(END,color)
        self.label4troughcolor = ttk.Label(self.frameWidgetConfig, text="trough\ncolor",
                                                style="widgetconfig.TLabel")
        self.label4troughcolor.grid(sticky=W, row=2012, column=1)
        self.frame4troughcolor = ttk.Frame(self.frameWidgetConfig)
        self.frame4troughcolor.grid(row=2012, column=2)
        self.entry4troughcolor = Entry(self.frame4troughcolor, relief=FLAT)
        self.entry4troughcolor.pack(side=LEFT, padx=3)
        button4troughcolor = ttk.Button(self.frame4troughcolor, text=">>", style="moreOptions.TButton",
                                        command = color4troughcolor)
        button4troughcolor.pack(side=LEFT)

        ### underline Sec
        # self.int_underline = IntVar()
        self.label4underline = ttk.Label(self.frameWidgetConfig, text="underline", style="widgetconfig.TLabel")
        self.label4underline.grid(sticky=W, row=2013, column=1)
        self.frame4underline = ttk.Frame(self.frameWidgetConfig)
        self.frame4underline.grid(row=2013, column=2)
        self.entry4underline = Entry(self.frame4underline, relief=FLAT, )
                                     # textvariable = self.int_underline)
        self.entry4underline.pack(side=LEFT, padx=3)
        blank_label4underline = ttk.Label(self.frame4underline, text="", anchor=W, width=3)
        blank_label4underline.pack(side=LEFT)

        ### undo
        self.bool_undo = BooleanVar()
        self.bool_undo.set(1)
        self.label4undo = ttk.Label(self.frameWidgetConfig, text="undo", style="widgetconfig.TLabel")
        self.label4undo.grid(sticky=W, row=2015, column=1)
        self.frame4undo = ttk.Frame(self.frameWidgetConfig)
        self.frame4undo.grid(row=2015, column=2)
        radioTrue4undo = ttk.Radiobutton(self.frame4undo, text="True", variable=self.bool_undo,
                                              value=True)
        radioTrue4undo.grid(sticky=W, row=1, column=1, padx=20)
        radioFalse4undo = ttk.Radiobutton(self.frame4undo, text="False", variable=self.bool_undo,
                                               value=False)
        radioFalse4undo.grid(sticky=E, row=1, column=2, padx=20)

        ### validate Sec
        validates = ("all", "focus", "focusin", "focusout", "key", "none")
        self.label4validate = ttk.Label(self.frameWidgetConfig, text="validate", style="widgetconfig.TLabel")
        self.label4validate.grid(sticky=W, row=2016, column=1)
        self.combo4validate = ttk.Combobox(self.frameWidgetConfig, values=validates)
        self.combo4validate.grid(row=2016, column=2, ipadx=5)

        ###validatecommand Sec
        self.label4validatecommand = ttk.Label(self.frameWidgetConfig, text="validate\ncommand",
                                               style="widgetconfig.TLabel")
        self.label4validatecommand.grid(sticky=W, row=2017, column=1)
        self.frame4validatecommand = ttk.Frame(self.frameWidgetConfig)
        self.frame4validatecommand.grid(row=2017, column=2)
        self.entry4validatecommand = Entry(self.frame4validatecommand, relief=FLAT, )
        self.entry4validatecommand.pack(side=LEFT, padx=3)
        blank_label4validatecommand = ttk.Label(self.frame4validatecommand, text="", anchor=W, width=3)
        blank_label4validatecommand.pack(side=LEFT)

        ### value Sec
        # self.int_value = IntVar()
        self.label4value = ttk.Label(self.frameWidgetConfig, text="value", style="widgetconfig.TLabel")
        self.label4value.grid(sticky=W, row=2018, column=1)
        self.frame4value = ttk.Frame(self.frameWidgetConfig)
        self.frame4value.grid(row=2018, column=2)
        self.entry4value = Entry(self.frame4value, relief=FLAT,)
                                 # textvariable = self.int_value)
        self.entry4value.pack(side=LEFT, padx=3)
        blank_label4value = ttk.Label(self.frame4value, text="", anchor=W, width=3)
        blank_label4value.pack(side=LEFT)

        ### value(s) Sec
        self.label4values = ttk.Label(self.frameWidgetConfig, text="value(s)", style="widgetconfig.TLabel")
        self.label4values.grid(sticky=W, row=2019, column=1)
        self.frame4values = ttk.Frame(self.frameWidgetConfig)
        self.frame4values.grid(row=2019, column=2)
        self.entry4values = Entry(self.frame4values, relief=FLAT)
        self.entry4values.pack(side=LEFT, padx=3)
        button4values = ttk.Button(self.frame4values, text=">>", style="moreOptions.TButton")
        button4values.pack(side=LEFT)

        ### variable Sec
        self.label4variable = ttk.Label(self.frameWidgetConfig, text="variable", style="widgetconfig.TLabel")
        self.label4variable.grid(sticky=W, row=2020, column=1)
        self.frame4variable = ttk.Frame(self.frameWidgetConfig)
        self.frame4variable.grid(row=2020, column=2)
        self.entry4variable = Entry(self.frame4variable, relief=FLAT, )
        self.entry4variable.pack(side=LEFT, padx=3)
        blank_label4variable = ttk.Label(self.frame4variable, text="", anchor=W, width=3)
        blank_label4variable.pack(side=LEFT)

        ### width Sec
        self.label4width = ttk.Label(self.frameWidgetConfig, text="width", style="widgetconfig.TLabel")
        self.label4width.grid(sticky=W, row=2100, column=1)
        self.spinbox4width = ttk.Spinbox(self.frameWidgetConfig, from_=1, increment = 5, to=self.label4width.winfo_screenwidth(), width = 10, wrap = True)
        self.spinbox4width.grid(row=2100, column=2)

        ### wrap Sec
        self.bool_wrap = BooleanVar()
        self.bool_wrap.set(1)
        self.label4wrap = ttk.Label(self.frameWidgetConfig, text="wrap", style="widgetconfig.TLabel")
        self.label4wrap.grid(sticky=W, row=2105, column=1)
        self.frame4wrap = ttk.Frame(self.frameWidgetConfig)
        self.frame4wrap.grid(row=2105, column=2)
        radioTrue4wrap = ttk.Radiobutton(self.frame4wrap, text="True", variable=self.bool_wrap,
                                              value=True)
        radioTrue4wrap.grid(sticky=W, row=1, column=1, padx=20)
        radioFalse4wrap = ttk.Radiobutton(self.frame4wrap, text="False", variable=self.bool_wrap,
                                               value=False)
        radioFalse4wrap.grid(sticky=E, row=1, column=2, padx=20)

        ### wrap (for Text) Sec
        wraps = ("char", "word", "none")
        self.label4wrap_Text = ttk.Label(self.frameWidgetConfig, text="wrap", style="widgetconfig.TLabel")
        self.label4wrap_Text.grid(sticky=W, row=2110, column=1)
        self.combo4wrap_Text = ttk.Combobox(self.frameWidgetConfig, values=wraps)
        self.combo4wrap_Text.grid(row=2110, column=2, ipadx=5)

        ### wraplength Sec
        # self.int_wraplength = IntVar()
        self.label4wraplength = ttk.Label(self.frameWidgetConfig, text="wraplength", style="widgetconfig.TLabel")
        self.label4wraplength.grid(sticky=W, row=2200, column=1)
        self.frame4wraplength = ttk.Frame(self.frameWidgetConfig)
        self.frame4wraplength.grid(row=2200, column=2)
        self.entry4wraplength = Entry(self.frame4wraplength, relief=FLAT,)
                                      # textvariable = self.int_wraplength)
        self.entry4wraplength.pack(side=LEFT, padx=3)
        blank_label4wraplength = ttk.Label(self.frame4wraplength, text="", anchor=W, width=3)
        blank_label4wraplength.pack(side=LEFT)

        ### xscrollcommand Sec
        self.label4xscrollcommand = ttk.Label(self.frameWidgetConfig, text="xscroll\ncommand",
                                              style="widgetconfig.TLabel")
        self.label4xscrollcommand.grid(sticky=W, row=2300, column=1)
        self.frame4xscrollcommand = ttk.Frame(self.frameWidgetConfig)
        self.frame4xscrollcommand.grid(row=2300, column=2)
        self.entry4xscrollcommand = Entry(self.frame4xscrollcommand, relief=FLAT, )
        self.entry4xscrollcommand.pack(side=LEFT, padx=3)
        blank_label4xscrollcommand = ttk.Label(self.frame4xscrollcommand, text="", anchor=W, width=3)
        blank_label4xscrollcommand.pack(side=LEFT)

        ### yscrollcommand Sec
        self.label4yscrollcommand = ttk.Label(self.frameWidgetConfig, text="yscroll\ncommand",
                                              style="widgetconfig.TLabel")
        self.label4yscrollcommand.grid(sticky=W, row=2400, column=1)
        self.frame4yscrollcommand = ttk.Frame(self.frameWidgetConfig)
        self.frame4yscrollcommand.grid(row=2400, column=2)
        self.entry4yscrollcommand = Entry(self.frame4yscrollcommand, relief=FLAT, )
        self.entry4yscrollcommand.pack(side=LEFT, padx=3)
        blank_label4yscrollcommand = ttk.Label(self.frame4yscrollcommand, text="", anchor=W, width=3)
        blank_label4yscrollcommand.pack(side=LEFT)

        ### Listbox Section to add
        # self.frame4AllListConfig = ttk.Frame(self.frameWidgetConfig)
        # self.frame4AllListConfig.grid(row = 2500, column=1, columnspan=2)
        # ttk.Label(self.frame4AllListConfig, text = "").grid()
        # ttk.Label(self.frame4AllListConfig, text = "").grid()
        #
        # frameListAdd = ttk.Frame(self.frame4AllListConfig)
        # frameListAdd.grid(row=10, column=1, columnspan=2)
        # labelListAdd = ttk.Label(frameListAdd, text="Add List", font=("Courier", 20, "bold"))
        # labelListAdd.pack(side=LEFT, anchor=W)
        # buttonListAdd = ttk.Button(frameListAdd, text="+")
        # buttonListAdd.pack(side=RIGHT, anchor=E)
        #
        # ### List for label, frame and entry variables of the listss
        # self.list_label_list = ["label4List_{x}" for x in range(0, 100)]
        # self.list_frame_list = ["frame4List_{x}" for x in range(0, 100)]
        # self.list_entry_list = ["entry4List_{x}" for x in range(0, 100)]
        # self.row_list = 12  ## Variable for grid of new toggled list
        # self.list_id = 2  ## Variable that toogles list label number
        #
        # def addList():      ### Command for + button
        #     windowObject.list_label_list[windowObject.list_id] = ttk.Label(self.frame4AllListConfig, text=f"List_{windowObject.list_id}",
        #                                                       style="widgetconfig.TLabel")
        #     windowObject.list_label_list[windowObject.list_id].grid(sticky=W, row=windowObject.row_list, column=1)
        #     windowObject.list_frame_list[windowObject.list_id] = ttk.Frame(self.frame4AllListConfig)
        #     windowObject.list_frame_list[windowObject.list_id].grid(row=windowObject.row_list, column=2)
        #     windowObject.list_entry_list[windowObject.list_id] = Entry(windowObject.list_frame_list[windowObject.list_id], relief=FLAT)
        #     windowObject.list_entry_list[windowObject.list_id].pack(side=LEFT, padx=3, pady = 3)
        #
        #     windowObject.row_list += 1
        #     windowObject.list_id += 1
        #
        # buttonListAdd.config(command = addList)
        #
        # self.list_label_list[1] = ttk.Label(self.frame4AllListConfig, text="List_1", style="widgetconfig.TLabel")
        # self.list_label_list[1].grid(sticky=W, row=11, column=1)
        #
        # self.list_frame_list[1] = ttk.Frame(self.frame4AllListConfig)
        # self.list_frame_list[1].grid(row=11, column=2)
        #
        # self.list_entry_list[1] = Entry(self.list_frame_list[1], relief=FLAT)
        # self.list_entry_list[1].pack(side=LEFT, padx=3, pady = 3)
        #
        # button4values = ttk.Button(self.frame4AllListConfig, text=">>", style="moreOptions.TButton",
        #                            command = arrangeObject.createList)
        # button4values.grid(row = 150, column = 2, sticky = E)

        ### PanedWindow Section to add
        self.frame4AllPaneConfig = ttk.Frame(self.frameWidgetConfig)
        self.frame4AllPaneConfig.grid(row = 2600, column=1, columnspan=2)

        ttk.Label(self.frame4AllPaneConfig, text = "").grid()
        ttk.Label(self.frame4AllPaneConfig, text = "").grid()

        framePaneAdd = ttk.Frame(self.frame4AllPaneConfig)
        framePaneAdd.grid(row=10, column=1, columnspan=2)
        labelPaneAdd = ttk.Label(framePaneAdd, text="Add Pane", font=("Courier", 20, "bold"))
        labelPaneAdd.pack(side=LEFT, anchor=W)
        buttonPaneAdd = ttk.Button(framePaneAdd, text="+")
        buttonPaneAdd.pack(side=RIGHT, anchor=E)

            ### List for label, frame and entry variables of the panes
        self.pane_label_list = ["label4Pane_{x}" for x in range(0, 100)]
        self.pane_frame_list = ["frame4Pane_{x}" for x in range(0, 100)]
        self.pane_entry_list = ["entry4Pane_{x}" for x in range(0, 100)]
        self.row_pane = 12     ## Variable for grid of new toggled pane
        self.pane_id = 2        ## Variable that toogles pane label number

        def addPane():      ### Command for + button
            windowObject.pane_label_list[windowObject.pane_id] = ttk.Label(self.frame4AllPaneConfig, text=f"Pane_{windowObject.pane_id}",
                                                              style="widgetconfig.TLabel")
            windowObject.pane_label_list[windowObject.pane_id].grid(sticky=W, row=windowObject.row_pane, column=1)
            windowObject.pane_frame_list[windowObject.pane_id] = ttk.Frame(self.frame4AllPaneConfig)
            windowObject.pane_frame_list[windowObject.pane_id].grid(row=windowObject.row_pane, column=2)
            windowObject.pane_entry_list[windowObject.pane_id] = Entry(windowObject.pane_frame_list[windowObject.pane_id], relief=FLAT)
            windowObject.pane_entry_list[windowObject.pane_id].pack(side=LEFT, padx=3, pady = 3)

            windowObject.row_pane += 1
            windowObject.pane_id += 1

        buttonPaneAdd.config(command = addPane)

        self.pane_label_list[1] = ttk.Label(self.frame4AllPaneConfig, text="Pane_1", style="widgetconfig.TLabel")
        self.pane_label_list[1].grid(sticky=W, row=11, column=1)

        self.pane_frame_list[1] = ttk.Frame(self.frame4AllPaneConfig)
        self.pane_frame_list[1].grid(row=11, column=2)

        self.pane_entry_list[1] = Entry(self.pane_frame_list[1], relief=FLAT)
        self.pane_entry_list[1].pack(side=LEFT, padx=3, pady = 3)

        button4values = ttk.Button(self.frame4AllPaneConfig, text=">>", style="moreOptions.TButton",
                                   command = arrangeObject.createPane)
        button4values.grid(row = 150, column = 2, sticky = E)


        ##### Styling for Wiget Config Label & Button
        self.styleWidgetConfigLabel.configure("widgetconfig.TLabel", font=("Courier New", 10), padding=3, anchor=W)
        self.styleWidgetConfigLabel.configure("moreOptions.TButton", width=3, anchor=W)

    def widgetTreeview(self):
        self.tree4Widget = ttk.Treeview(windowPRO, )
        self.tree4Widget.pack(side = LEFT, fill=BOTH, expand = 1)
        scroll4Widgettree = ttk.Scrollbar(orient = "vertical", command = self.tree4Widget.yview)
        scroll4Widgettree.pack(side = RIGHT, fill = Y)
        self.tree4Widget["yscrollcommand"] = scroll4Widgettree.set
        self.tree4Widget.insert("", END, iid="Design Window", text="Design Window", open = True)

    ##### Method to validate whether WidgetConfig Toplevel currently exits.
    def validateWidgetConfigTopLevelState(self):
        if self.clickWidgetConfig == 0:  # If NOT exists,
            self.toplevel4WidgetConfig()  # new Toplevel for Widget is created
        elif self.clickWidgetConfig == 1:  # If exists:
            self.toplevelWidgetConfig.destroy()  # Current Toplevel is destroyed
            self.toplevel4WidgetConfig()  # New Toplevel for Widget is created

    ########## Command for Main tk Widgets
    def determineButton(self, widget_value):
        global iswidget
        iswidget = widget_value

    def mainButton(self):
        self.validateWidgetConfigTopLevelState()
        ### Removal of Unavailable Attributes for this Widget
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineCheckbutton(self, widget_value):
        global iswidget
        iswidget = widget_value

    def mainCheckbutton(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineEntry(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainEntry(self):
        self.validateWidgetConfigTopLevelState()

        self.combo4state.config(values = ("active", "disabled", "normal", "readonly"))  ### Add 'readonly' to state
        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4height.destroy()
        self.spinbox4height.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    ### Addition of Attributes

    def determineLabel(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainLabel(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineListbox(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainListbox(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()


    def mainMenu(self):
        self.validateWidgetConfigTopLevelState()

    ### Removal of Unavailable Attributes for this Widget

    def determineMenubutton(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainMenubutton(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()


    def determineMessage(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainMessage(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def mainOptionMenu(self, widget_value):
        self.validateWidgetConfigTopLevelState()

        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

        ### Removal of Unavailable Attributes for this Widget
        self.validateWidgetConfigTopLevelState()
        self.label4activebackground.destroy()
        self.label4highlightthickness.destroy()
        self.frame4activebackground.destroy()
        self.spinbox4highlightthickness.destroy()
        self.label4activeforeground.destroy()
        self.label4highlightcolor.destroy()
        self.frame4activeforeground.destroy()
        self.frame4highlightcolor.destroy()
        self.label4anchor.destroy()
        self.label4highlightbackground.destroy()
        self.combo4anchor.destroy()
        self.frame4highlightbackground.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4foreground.destroy()
        self.frame4foreground.destroy()
        self.label4font.destroy()
        self.frame4font.destroy()
        self.label4justify.destroy()
        self.combo4justify.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4relief.destroy()
        self.combo4relief.destroy()
        self.label4takefocus.destroy()
        self.frame4takefocus.destroy()
        self.label4height.destroy()
        self.spinbox4height.destroy()
        self.label4cursor.destroy()
        self.combo4cursor.destroy()
        self.label4borderwidth.destroy()
        self.spinbox4borderwidth.destroy()
        self.label4width.destroy()
        self.spinbox4width.destroy()
        self.label4background.destroy()
        self.frame4background.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineRadiobutton(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainRadiobutton(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavialable Attributes for this widget
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineScale(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainScale(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4justify.destroy()  # Remove Justify Attribute
        self.combo4justify.destroy()
        self.label4height.destroy()  # Remove Height Attribute
        self.spinbox4height.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineScrollbar(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainScrollbar(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4font.destroy()
        self.frame4font.destroy()
        self.label4foreground.destroy()  # Remove Foreground Label Attribute
        self.frame4foreground.destroy()
        self.label4height.destroy()
        self.spinbox4height.destroy()
        self.label4justify.destroy()
        self.combo4justify.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineSpinbox(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainSpinbox(self):
        self.validateWidgetConfigTopLevelState()

        self.combo4state.config(values=("active", "disabled", "normal", "readonly"))    ### Add 'readonly' to state
        ### Removal of Unavailable Attributes for this Widget
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4height.destroy()
        self.spinbox4height.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineText(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainText(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4justify.destroy()  # Remove Justify Attribute
        self.combo4justify.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    ###### Command for Main tk Containers
    def determineFrame(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainFrame(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4font.destroy()  # Remove Font  Attribute
        self.frame4font.destroy()
        self.label4foreground.destroy()  # Remove Foreground Label Attribute
        self.frame4foreground.destroy()
        self.label4justify.destroy()  # Remove Justify Attribute
        self.combo4justify.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determineLabelFrame(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainLabelFrame(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4justify.destroy()  # Remove Justify Attribute
        self.combo4justify.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()

    def determinePanedWindow(self, widget_value):
        global iswidget
        iswidget = widget_value  ### Determines Widget to display on the design window

    def mainPanedWindow(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4font.destroy()
        self.frame4font.destroy()
        self.label4foreground.destroy()
        self.frame4foreground.destroy()
        self.label4highlightbackground.destroy()
        self.frame4highlightbackground.destroy()
        self.label4highlightcolor.destroy()
        self.frame4highlightcolor.destroy()
        self.label4highlightthickness.destroy()
        self.spinbox4highlightthickness.destroy()
        self.label4justify.destroy()
        self.combo4justify.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4padx.destroy()
        self.spinbox4padx.destroy()
        self.label4pady.destroy()
        self.spinbox4pady.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4takefocus.destroy()
        self.frame4takefocus.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()

    def determineToplevel(self, widget_value):
        global iswidget
        iswidget = widget_value     ### Widget Deteminant

    def mainToplevel(self):
        self.validateWidgetConfigTopLevelState()

        ### Removal of Unavailable Attributes for this Widget
        self.label4activebackground.destroy()
        self.frame4activebackground.destroy()
        self.label4activeforeground.destroy()
        self.frame4activeforeground.destroy()
        self.label4anchor.destroy()
        self.combo4anchor.destroy()
        self.label4bitmap.destroy()
        self.combo4bitmap.destroy()
        self.label4command.destroy()
        self.frame4command.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledforeground.destroy()
        self.frame4disabledforeground.destroy()
        self.label4foreground.destroy()
        self.frame4foreground.destroy()
        self.label4font.destroy()
        self.frame4font.destroy()
        self.label4justify.destroy()
        self.combo4justify.destroy()
        self.label4state.destroy()
        self.combo4state.destroy()
        self.label4text.destroy()
        self.frame4text.destroy()
        self.label4textvariable.destroy()
        self.frame4textvariable.destroy()
        self.label4underline.destroy()
        self.frame4underline.destroy()
        self.label4wraplength.destroy()
        self.frame4wraplength.destroy()
        self.label4compound.destroy()
        self.combo4compound.destroy()
        self.label4disabledbackground.destroy()
        self.frame4disabledbackground.destroy()
        self.label4from_.destroy()
        self.frame4from_.destroy()
        self.label4image.destroy()
        self.frame4image.destroy()
        self.label4insertbackground.destroy()
        self.frame4insertbackground.destroy()
        self.label4insertborderwidth.destroy()
        self.spinbox4insertborderwidth.destroy()
        self.label4insertofftime.destroy()
        self.spinbox4insertofftime.destroy()
        self.label4insertontime.destroy()
        self.spinbox4insertontime.destroy()
        self.label4insertwidth.destroy()
        self.spinbox4insertwidth.destroy()
        self.label4orient.destroy()
        self.combo4orient.destroy()
        self.label4overrelief.destroy()
        self.combo4overrelief.destroy()
        self.label4repeatdelay.destroy()
        self.spinbox4repeatdelay.destroy()
        self.label4repeatinterval.destroy()
        self.spinbox4repeatinterval.destroy()
        self.label4selectbackground.destroy()
        self.frame4selectbackground.destroy()
        self.label4selectborderwidth.destroy()
        self.spinbox4selectborderwidth.destroy()
        self.label4selectforeground.destroy()
        self.frame4selectforeground.destroy()
        self.label4to.destroy()
        self.frame4to.destroy()
        self.label4variable.destroy()
        self.frame4variable.destroy()
        self.label4xscrollcommand.destroy()
        self.frame4xscrollcommand.destroy()
        self.label4yscrollcommand.destroy()
        self.frame4yscrollcommand.destroy()
        self.label4selectcolor.destroy()
        self.frame4selectcolor.destroy()
        self.label4selectmode.destroy()
        self.combo4selectmode.destroy()
        self.label4exportselection.destroy()
        self.frame4exportselection.destroy()
        self.label4readonlybackground.destroy()
        self.frame4readonlybackground.destroy()
        self.label4show.destroy()
        self.frame4show.destroy()
        self.label4validate.destroy()
        self.combo4validate.destroy()
        self.label4validatecommand.destroy()
        self.frame4validatecommand.destroy()
        self.label4invalidcommand.destroy()
        self.frame4invalidcommand.destroy()
        self.label4activestyle.destroy()
        self.combo4activestyle.destroy()
        self.label4listvariable.destroy()
        self.frame4listvariable.destroy()
        self.label4direction.destroy()
        self.combo4direction.destroy()
        self.label4indicatoron.destroy()
        self.frame4indicatoron.destroy()
        self.label4menu.destroy()
        self.frame4menu.destroy()
        self.label4offrelief.destroy()
        self.combo4offrelief.destroy()
        self.label4selectimage.destroy()
        self.frame4selectimage.destroy()
        self.label4aspect.destroy()
        self.frame4aspect.destroy()
        self.label4value.destroy()
        self.frame4value.destroy()
        self.label4buttonbackground.destroy()
        self.frame4buttonbackground.destroy()
        self.label4buttoncursor.destroy()
        self.combo4buttoncursor.destroy()
        self.label4buttondownrelief.destroy()
        self.combo4buttondownrelief.destroy()
        self.label4buttonuprelief.destroy()
        self.combo4buttonuprelief.destroy()
        self.label4increment.destroy()
        self.frame4increment.destroy()
        self.label4wrap.destroy()
        self.frame4wrap.destroy()
        self.label4format.destroy()
        self.frame4format.destroy()
        self.label4values.destroy()
        self.frame4values.destroy()
        self.label4labelanchor.destroy()
        self.combo4labelanchor.destroy()
        self.label4labelwidget.destroy()
        self.entry4labelwidget.destroy()
        self.label4autoseparators.destroy()
        self.frame4autoseparators.destroy()
        self.label4blockcursor.destroy()
        self.frame4blockcursor.destroy()
        self.label4inactiveselectbackground.destroy()
        self.frame4inactiveselectbackground.destroy()
        self.label4insertunfoccussed.destroy()
        self.combo4insertunfoccussed.destroy()
        self.label4maxundo.destroy()
        self.frame4maxundo.destroy()
        self.label4undo.destroy()
        self.frame4undo.destroy()
        self.label4tabs.destroy()
        self.frame4tabs.destroy()
        self.label4wrap_Text.destroy()
        self.combo4wrap_Text.destroy()
        self.label4spacing1.destroy()
        self.spinbox4spacing1.destroy()
        self.label4spacing2.destroy()
        self.spinbox4spacing2.destroy()
        self.label4spacing3.destroy()
        self.spinbox4spacing3.destroy()
        self.label4digits.destroy()
        self.spinbox4digits.destroy()
        self.label4label.destroy()
        self.frame4label.destroy()
        self.label4resolution.destroy()
        self.frame4resolution.destroy()
        self.label4showvalue.destroy()
        self.frame4showvalue.destroy()
        self.label4sliderlength.destroy()
        self.frame4sliderlength.destroy()
        self.label4sliderrelief.destroy()
        self.combo4sliderrelief.destroy()
        self.label4tickinterval.destroy()
        self.frame4tickinterval.destroy()
        self.label4troughcolor.destroy()
        self.frame4troughcolor.destroy()
        self.label4handlepad.destroy()
        self.spinbox4handlepad.destroy()
        self.label4handlesize.destroy()
        self.spinbox4handlesize.destroy()
        self.label4opaqueresize.destroy()
        self.frame4opaqueresize.destroy()
        self.label4sashcursor.destroy()
        self.combo4sashcursor.destroy()
        self.label4sashpad.destroy()
        self.frame4sashpad.destroy()
        self.label4sashrelief.destroy()
        self.combo4sashrelief.destroy()
        self.label4sashwidth.destroy()
        self.frame4sashwidth.destroy()
        self.label4showhandle.destroy()
        self.frame4showhandle.destroy()
        self.label4length.destroy()
        self.spinbox4length.destroy()
        self.frame4AllPaneConfig.destroy()


    ###### Commands for >> Font Buttons
    def executeFontToplevel(self):
        self.numberFont_2
        self.isFontToplevel

        global fontObject

        if self.isFontToplevel == 0:
            fontObject = ChooseFont(self.numberFont_2,
                                    self.toplevelWidgetConfig,)  #### Creates font Object and passes in the CHANGED new font name
        elif self.isFontToplevel == 1:
            fontObject.toplevel4Font.destroy()
            fontObject = ChooseFont(self.numberFont_2,
                                    self.toplevelWidgetConfig,)  #### Creates font Object and passes in the CHANGED new font name
        if self.entry4font.get() == "":
            self.entry4font.insert(0, fontObject.fontNameVariable)
        elif self.entry4font.get() != "":
            self.entry4font.delete(0, END)
            self.entry4font.insert(0, fontObject.fontNameVariable)

        self.numberFont_2 += 1
        self.isFontToplevel = 1


class ChooseFont:
    def __init__(self, numberFont_1, master):

        self.toplevel4Font = Toplevel(master)

        self.toplevel4Font.resizable(False, False)
        self.fontScreenWidth = self.toplevel4Font.winfo_screenwidth()
        fontScreenHeight = self.toplevel4Font.winfo_screenheight()
        self.toplevel4Font.transient()
        self.toplevel4Font.geometry("%dx%d+%d+%d" % (self.fontScreenWidth/2.973, 445, self.fontScreenWidth/3, fontScreenHeight/2.5))
        # global selectedFont

        self.numberFont_1 = numberFont_1     #### Variable that determines new Font Name
        self.fontNameVariable = "font_{}".format(self.numberFont_1)     ###### Variable for Font Names
        self.dictFontSettings = {"name": self.fontNameVariable, "family": "Segoe UI", "size": 9}

        self.sampleFont = font.Font(family = "Arial", size= 8)
        windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"] = font.Font(root = windowDesign, **self.dictFontSettings) #### Font object for selected font in Font Window

        self.fontWidgets()    ######## Display Font Toplevel Widgets


    def applyFont(self,):
        # global selectedFont

        getFontFamily = self.comboFontFamily.get()
        self.dictFontSettings["family"] = getFontFamily
        self.sampleFont.config(family = getFontFamily)
        
        getFontSize = int(self.spinboxSize.get())
        self.dictFontSettings["size"] = getFontSize
        self.sampleFont.config(size = getFontSize)

        self.text4Preview.tag_config("tagPreviewText", font = self.sampleFont)
        self.groupStyle = (self.checkVariable1.get(), self.checkVariable2.get(), self.checkVariable3.get(), self.checkVariable4.get())  ##### Tuple that commulates responses from check boxes

        def iterateStyle():
            if fontObject.groupStyle[0] == 1:
                self.sampleFont.config(weight = font.BOLD)
            if fontObject.groupStyle[0] == 0:
                self.sampleFont.config(weight = font.NORMAL)
            if fontObject.groupStyle[1] == 1:
                self.sampleFont.config(slant = font.ITALIC)
            if fontObject.groupStyle[1] == 0:
                self.sampleFont.config(slant = font.ROMAN)
            if fontObject.groupStyle[2] == 1:
                self.sampleFont.config(overstrike = 1)
            if fontObject.groupStyle[2] == 0:
                self.sampleFont.config(overstrike = 0)
            if fontObject.groupStyle[3] == 1:
                self.sampleFont.config(underline = 1)
            if fontObject.groupStyle[3] == 0:
                self.sampleFont.config(underline = 0)
        self.toplevel4Font.after(1, iterateStyle)


    def applyFont_WidgetEvent(self, event):
        self.applyFont()

    def fontWidgets(self):
        ###### Font Family Sec
            ### Label for font family
        labelFontFamily = ttk.Label(self.toplevel4Font, text = "font family:",)
        labelFontFamily.grid(row = 1, column = 1, sticky = N, padx = 20, pady = 10)
            ### Combobox for font family
        get_families = font.families()   ##### Get all Available Font Families
        self.comboFontFamily = ttk.Combobox(self.toplevel4Font, values = get_families, )
        self.comboFontFamily.grid(row = 2, column = 1, sticky = W, padx = 20, pady = 10)
        self.comboFontFamily.set("Segoe UI")

        ###### Font Size Sec
            ### Label font size
        labelFontSize = ttk.Label(self.toplevel4Font, text = "font size:")
        labelFontSize.grid(row = 3, column = 1, sticky = N, padx = 20, pady = 10)
            ### Spinbox
        ##size_var = IntVar()
        ##size_var.initialize (8)
        self.spinboxSize = ttk.Spinbox(self.toplevel4Font, from_ = 8, to = 98, increment = 3, wrap = True, command = self.applyFont)
        self.spinboxSize.grid(row = 4, column = 1, sticky = W, padx = 20, pady = 10)
        self.spinboxSize.set(9)

        Label(self.toplevel4Font, ).grid(row = 5, column = 1)   ####### Spacing Label
        Label(self.toplevel4Font, ).grid(row = 6, column = 1)

        ###### Separator - Horizontal Sec
        seperatorFontHorizontal = ttk.Separator(self.toplevel4Font, orient = HORIZONTAL,  )
        seperatorFontHorizontal.grid(row = 7, column = 1, columnspan = 4, sticky = EW, )

        ###### Separator - Vertical Sec
        separatorFontVertical = ttk.Separator(self.toplevel4Font, orient = VERTICAL)
        separatorFontVertical.grid(row = 1, column = 2, rowspan = 6, sticky = NS, )

        ###### Preview Section
            ### Label for Preview
        labelPreview = ttk.Label(self.toplevel4Font, text = "Preview: ")
        labelPreview.grid(sticky = N, row = 8, column = 0, columnspan = 5, pady = 10)
            ### Text for Preview
        self.text4Preview = Text(self.toplevel4Font, width = int(self.fontScreenWidth/24)+1, height = 10, relief = FLAT, wrap = WORD)
        self.text4Preview.grid(sticky = W, row = 9, column = 0, columnspan = 5, pady = 5)
        self.text4Preview.insert(END, "abcABC")
        self.text4Preview.tag_add("tagPreviewText", 1.0, END)
        self.text4Preview.tag_config("tagPreviewText", font = self.sampleFont,
                                     justify = CENTER, spacing1 = 10)
        self.text4Preview["state"] = "disabled"

        ###### Font Styling Section
            ### Label for font styling
        labelFontStyle = ttk.Label(self.toplevel4Font, text = "font styling:")
        labelFontStyle.grid(row = 1, column = 3, sticky = N, padx = 40, pady = 10)
            ### Check button to select styling
        self.checkVariable1 = IntVar()
        checkFontStyle1 = ttk.Checkbutton(self.toplevel4Font, text = "Bold", variable = self.checkVariable1, command = self.applyFont)
        checkFontStyle1.grid(row = 2, column = 3, sticky = W, padx = 30)
        self.checkVariable2 = IntVar()
        checkFontStyle2 = ttk.Checkbutton(self.toplevel4Font, text = "Italic", variable = self.checkVariable2, command = self.applyFont)
        checkFontStyle2.grid(row = 3, column = 3, sticky = W, padx = 30)
        self.checkVariable3 = IntVar()
        checkFontStyle3 = ttk.Checkbutton(self.toplevel4Font, text = "Overstrike", variable = self.checkVariable3, command = self.applyFont)
        checkFontStyle3.grid(row = 4, column = 3, sticky = W, padx = 30)
        self.checkVariable4 = IntVar()
        checkFontStyle4 = ttk.Checkbutton(self.toplevel4Font, text = "Underline", variable = self.checkVariable4, command = self.applyFont)
        checkFontStyle4.grid(row = 5, column = 3, sticky = W, padx = 30)

        ####### apply Font Button
        def implementFont():
            try:
                self.sampleFont.config(family = fontObject.comboFontFamily.get())
                self.sampleFont.config(size = fontObject.spinboxSize.get())
                windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(family=fontObject.comboFontFamily.get())
                windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(size=fontObject.spinboxSize.get())
                if fontObject.groupStyle[0] == 1:
                    self.dictFontSettings["weight"] = "bold"
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(weight = font.BOLD)
                if fontObject.groupStyle[0] == 0:
                    self.dictFontSettings["weight"] = "normal"
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(weight = font.NORMAL)
                if fontObject.groupStyle[1] == 1:
                    self.dictFontSettings["slant"] = "italic"
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(slant = font.ITALIC)
                if fontObject.groupStyle[1] == 0:
                    self.dictFontSettings["slant"] = "roman"
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(slant = font.ROMAN)
                if fontObject.groupStyle[2] == 1:
                    self.dictFontSettings["overstrike"] = 1
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(overstrike = 1)
                if fontObject.groupStyle[2] == 0:
                    self.dictFontSettings["overstrike"] = 0
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(overstrike = 0)
                if fontObject.groupStyle[3] == 1:
                    self.dictFontSettings["underline"] = 1
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(underline = 1)
                if fontObject.groupStyle[3] == 0:
                    self.dictFontSettings["underline"] = 0
                    windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(underline = 0)

                windowObject.implementFont_determine = 22
                arrangeObject.refreshAttributes()
                windowObject.implementFont_determine = 0
            except AttributeError:
                pass
        
        def resetFont():
            fontObject.sampleFont.config(family = "Segoe UI", size = 9, weight = font.NORMAL, slant = font.ROMAN,
                                         overstrike = 0, underline = 0)
            windowObject.dictCountFont[f"selectedFont{self.numberFont_1}"].config(family = "Segoe UI", size = 9,
                                                weight = font.NORMAL, slant = font.ROMAN, overstrike = 0, underline = 0)
            fontObject.comboFontFamily.set("Segoe UI")
            fontObject.spinboxSize.set(9)
            self.checkVariable1.set(0)
            self.checkVariable2.set(0)
            self.checkVariable3.set(0)
            self.checkVariable4.set(0)

        def closeFont():
            fontObject.toplevel4Font.destroy()

        buttonResetFont = ttk.Button(self.toplevel4Font, text="Reset Font", command=resetFont)
        buttonResetFont.grid(row=11, column=1, sticky = W)

        buttonApplyFont = ttk.Button(self.toplevel4Font, text = "Apply Font", command = implementFont)
        buttonApplyFont.grid(row = 11, columnspan = 5)

        buttonCloseFont = ttk.Button(self.toplevel4Font, text = "Close", command = closeFont)
        buttonCloseFont.grid(row = 11, column = 4, sticky = W)

        ###### Styling for All Font Labels
        style4LabelFontStyling = ttk.Style()
        style4LabelFontStyling.configure("TLabel", font = ("Segoe UI", 9, "bold", "italic"))

        ###### Event Handlers
        self.comboFontFamily.bind("<<ComboboxSelected>>", self.applyFont_WidgetEvent)    ####### Combobox Event
        self.spinboxSize.bind("<Return>", self.applyFont_WidgetEvent)              ####### Spinbox Event for Enter Key
        self.comboFontFamily.bind("<Return>", self.applyFont_WidgetEvent)                ####### Combobox Event for Enter Key

global winConfigStart
winConfigStart = [0]
class DesignWindowSetup:
    global winConfigStart
    def __init__(self):
        if windowObject.iswinConfigToplevel == 0:
            winConfigStart[0] = (Toplevel(master = windowPRO))
            self.winConfig(winConfigStart[0])
        elif windowObject.iswinConfigToplevel == 1:
            winConfigStart[0].destroy()
            winConfigStart[0] = Toplevel(master = windowPRO)
            self.winConfig(winConfigStart[0])
        self.exitDesignWindowSetup()

    def winConfig(self,  get_toplevel_winconfig):
        self.toplevel4winConfig = get_toplevel_winconfig
        self.toplevel4winConfig.geometry("%dx%d+%d+%d" % (620, 535,
                                                          windowPRO.winfo_screenwidth()/4, windowPRO.winfo_screenheight()/5))
        global iswinConfigToplevel
        windowObject.iswinConfigToplevel = 1
        self.placeWidgetsDesign()

    def placeWidgetsDesign(self):
        ### Parameter Assignment for windowDesign geometry meth
        global new_value_width
        new_value_width = int(screen_width / 2)
        global new_value_height
        new_value_height = int(screen_height / 1.57)
        global new_value_position_x
        new_value_position_x = int(screen_width / 4.5)
        global new_value_position_y
        new_value_position_y = int(screen_height / 3.36)
        dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry({new_value_width}x{new_value_height}+" \
                                                  f"{new_value_position_x}+{new_value_position_y})"

        ### Parameter Assignment for windowDesign resizable meth
        global new_resizable_width
        new_resizable_width = True
        global new_resizable_height
        new_resizable_height = True
        dictDesignWindowPropCollect["resizable"] = f"windowDesign.resizable(width = {new_resizable_width}, " \
                                                   f"height = {new_resizable_height})"

        ### Parameter Assignment for windowDesign overrideredirect
        global new_overrideredirect
        new_overrideredirect = False

        ### Parameter Assignment for maxsize
        global new_maxsize_width
        new_maxsize_width = int(windowPRO.winfo_screenwidth() / 2)
        global new_maxsize_height
        new_maxsize_height = int(windowPRO.winfo_screenheight() / 1.57)

        ### Parameter Assignment for minsize
        global new_minsize_width
        new_minsize_width = int(windowPRO.winfo_screenwidth() / 2)
        global new_minsize_height
        new_minsize_height = int(windowPRO.winfo_screenheight() / 1.57)

        ### main toplevel title
        label4designconfig = ttk.Label(self.toplevel4winConfig, text = "Configure Your GUI Window To Your Taste",
                                       font = ("Courier", 15, "bold"), background = "grey", anchor = CENTER)
        label4designconfig.grid(row = 10, column = 0, columnspan = 9, ipadx = 75)

        Label(self.toplevel4winConfig, text = "").grid(row = 12)

        ### title
        dictDesignWindowPropCollect["title"] = f"windowDesign.title('Design Window')"
        def command4title():
            variable4title = entry4title.get()
            windowDesign.title(variable4title)
            dictDesignWindowPropCollect["title"] = f"windowDesign.title('{variable4title}')"
            
        frame4title_iconphoto = ttk.Frame(self.toplevel4winConfig)
        frame4title_iconphoto.grid(row = 20, column = 0, columnspan = 8)
        label4title = ttk.Label(frame4title_iconphoto, text = "title")
        label4title.grid(row = 20, column = 1, padx = 20)
        entry4title = ttk.Entry(master = frame4title_iconphoto)
        entry4title.grid(row = 20, column = 2,)
        button4title = ttk.Button(frame4title_iconphoto, text=">>", width=3, command = command4title)
        button4title.grid(row=20, column=3, padx=2)

        Label(frame4title_iconphoto, text = "").grid(row = 20, column = 4, padx = 40)

        ### photo
        def command4photo():
            file = filedialog.askopenfile("r", filetypes = [("Portable Network Graphics (PNG)", "*png")])
            value_image = PhotoImage(master = windowDesign, file = file.name)
            windowDesign.iconphoto(False, value_image)
            entry4photo.delete(0,END)
            entry4photo.insert(0, file.name)
            entry4photo["state"] = "readonly"
            dictDesignWindowPropCollect["iconphoto"] = f"PhotoImage(master = windowDesign, file = '{file.name}')"
            dictDesignWindowPropCollect["iconphoto2"] = f"windowDesign.iconphoto(False, IconPhoto)"
            
        label4photo = ttk.Label(frame4title_iconphoto, text = "icon photo")
        label4photo.grid(row = 20, column = 5, padx = 20)
        entry4photo = ttk.Entry(frame4title_iconphoto)
        entry4photo.grid(row = 20, column = 6)
        scroll4photo = ttk.Scrollbar(frame4title_iconphoto, orient = "horizontal", command = entry4photo.xview)
        scroll4photo.grid(row = 21, column = 6, ipadx = 40)
        entry4photo.config(xscrollcommand = scroll4photo.set)
        button4photo = ttk.Button(frame4title_iconphoto, text = ">>", width = 3, command = command4photo)
        button4photo.grid(row = 20, column = 7, padx = 2)

        Label(self.toplevel4winConfig, text = "").grid(row = 27)
        label4geometry = ttk.Label(self.toplevel4winConfig, text = "Geometry (Window Dimensions)",
                                   font = ("Calisto MT", 12, "bold"))
        label4geometry.grid(row = 30, column = 0, columnspan = 2)

        ### geometry width
        def command4width(new_value):
            global new_value_width
            new_value_width = int(float(new_value))
            windowDesign.geometry(
                "%dx%d+%d+%d" % (new_value_width, new_value_height, new_value_position_x,  new_value_position_y))
            label24width.config(text = new_value_width)
            dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry({new_value_width}, {new_value_height}, " \
                                                      f"{new_value_position_x}, {new_value_position_y})"
        label4width = ttk.Label(self.toplevel4winConfig, text = "width")
        label4width.grid(row = 40, column = 1)
        int_width = IntVar(value = windowPRO.winfo_screenwidth()/2)
        frame4width = ttk.Frame(self.toplevel4winConfig)
        frame4width.grid(row = 40, column = 2)
        label24width = ttk.Label(frame4width, text = int_width.get())
        label24width.pack()
        scale4width = ttk.Scale(frame4width, variable = int_width, from_ = 50,
                                to = windowPRO.winfo_screenwidth(), command = command4width)
        scale4width.pack()

        ### geometry height
        def command4height(new_value):
            global new_value_height
            new_value_height = int(float(new_value))
            windowDesign.geometry(
                "%dx%d+%d+%d" % (new_value_width, new_value_height, new_value_position_x,  new_value_position_y))
            label24height.config(text = new_value_height)
            dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry({new_value_width}, {new_value_height}, " \
                                                      f"{new_value_position_x}, {new_value_position_y})"
        label4height = ttk.Label(self.toplevel4winConfig, text = "height")
        label4height.grid(row = 50, column = 1)
        int_height = IntVar(value = windowPRO.winfo_screenheight()/1.57)
        frame4height = ttk.Frame(self.toplevel4winConfig)
        frame4height.grid(row = 50, column = 2)
        label24height = ttk.Label(frame4height, text = int_height.get())
        label24height.pack()
        scale4height = ttk.Scale(frame4height, variable = int_height, from_ = 50,
                                 to = windowPRO.winfo_screenheight(), command = command4height)
        scale4height.pack()

        ### position_x relative to screen
        def command4position_x(new_value):
            global new_value_position_x
            new_value_position_x = int(float(new_value))
            windowDesign.geometry(
                "%dx%d+%d+%d" % (new_value_width, new_value_height, new_value_position_x, new_value_position_y))
            label24position_x.config(text = new_value_position_x)
            dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry({new_value_width}, {new_value_height}, " \
                                                      f"{new_value_position_x}, {new_value_position_y})"
        label4position_x = ttk.Label(self.toplevel4winConfig, text = "x position of Design Window")
        label4position_x.grid(row = 60, column = 1)
        int_position_x = IntVar(value = windowPRO.winfo_screenwidth()/4.5)
        frame4position_x = ttk.Frame(self.toplevel4winConfig)
        frame4position_x.grid(row = 60, column = 2)
        label24position_x = ttk.Label(frame4position_x, text = int_position_x.get())
        label24position_x.pack()
        scale4position_x = ttk.Scale(frame4position_x, variable = int_position_x, from_ = 0,
                                     to = windowPRO.winfo_screenwidth()-50, command = command4position_x)
        scale4position_x.pack()

        ### position_y relative to screen
        def command4position_y(new_value):
            global new_value_position_y
            new_value_position_y = int(float(new_value))
            windowDesign.geometry(
                "%dx%d+%d+%d" % (new_value_width, new_value_height, new_value_position_x, new_value_position_y))
            label24position_y.config(text = new_value_position_y)
            dictDesignWindowPropCollect["geometry"] = f"windowDesign.geometry('{new_value_width}, {new_value_height}, " \
                                                      f"{new_value_position_x}, {new_value_position_y}')"
        label4position_y = ttk.Label(self.toplevel4winConfig, text = "y position of Design Window")
        label4position_y.grid(row = 70, column = 1)
        int_position_y = IntVar(value = windowPRO.winfo_screenheight() / 3.36)
        frame4position_y = ttk.Frame(self.toplevel4winConfig)
        frame4position_y.grid(row = 70, column = 2)
        label24position_y = ttk.Label(frame4position_y, text = int_position_y.get())
        label24position_y.pack()
        scale4position_y = ttk.Scale(frame4position_y, variable = int_position_y, from_ = 0,
                                     to = windowPRO.winfo_screenheight()-50, command = command4position_y)
        scale4position_y.pack()

        ### Window Properties Section Label
        Label(self.toplevel4winConfig, text="").grid(row=71)
        label4geometry = ttk.Label(self.toplevel4winConfig, text="Window Properties",
                                   font=("Calisto MT", 12, "bold"))
        label4geometry.grid(row=72, column=0, columnspan=2, sticky = W)

        ### is resizable_width
        def command4resizable_width():
            global new_resizable_width
            new_resizable_width = bool_resizable_width.get()
            windowDesign.resizable(width = new_resizable_width, height = new_resizable_height)
            dictDesignWindowPropCollect["resizable"] = f"windowDesign.resizable(width = {new_resizable_width}, " \
                                                             f"height = {new_resizable_height})"
        label4resizable_width = ttk.Label(self.toplevel4winConfig, text = "Is width resizable?")
        label4resizable_width.grid(row = 80, column = 1)
        bool_resizable_width = BooleanVar(value = True)
        frame4resizable_width = ttk.Frame(self.toplevel4winConfig)
        frame4resizable_width.grid(row = 80, column = 2)
        radioTrue4resizable_width = ttk.Radiobutton(frame4resizable_width, variable = bool_resizable_width, text = "Yes",
                                                    value = True, command = command4resizable_width)
        radioTrue4resizable_width.pack(side = LEFT, padx = 20)
        radioFalse4resizable_width = ttk.Radiobutton(frame4resizable_width, variable = bool_resizable_width, text = "No",
                                                     value = False, command = command4resizable_width)
        radioFalse4resizable_width.pack(side = RIGHT)

        ### is resizable height
        def command4resizable_height():
            global new_resizable_height
            new_resizable_height = bool_resizable_height.get()
            windowDesign.resizable(width = new_resizable_width, height = new_resizable_height)
            dictDesignWindowPropCollect["resizable"] = f"windowDesign.resizable(width = {new_resizable_width}, " \
                                                             f"height = {new_resizable_height})"
        label4resizable_height = ttk.Label(self.toplevel4winConfig, text="Is height resizable?")
        label4resizable_height.grid(row=90, column=1)
        bool_resizable_height = BooleanVar(value=True)
        frame4resizable_height = ttk.Frame(self.toplevel4winConfig)
        frame4resizable_height.grid(row=90, column=2)
        radioTrue4resizable_height = ttk.Radiobutton(frame4resizable_height, variable=bool_resizable_height, text="Yes",
                                                    value=True, command = command4resizable_height)
        radioTrue4resizable_height.pack(side=LEFT, padx=20)
        radioFalse4resizable_height = ttk.Radiobutton(frame4resizable_height, variable=bool_resizable_height, text="No",
                                                     value=False, command = command4resizable_height)
        radioFalse4resizable_height.pack(side=RIGHT)

        ### override redirect flag
        def command4overrideredirect():
            global new_overrideredirect
            new_overrideredirect = bool_overrideredirect.get()
            windowDesign.overrideredirect(new_overrideredirect)
            dictDesignWindowPropCollect["overrideredirect"] = f"windowDesign.overrideredirect({new_overrideredirect})"
        label4overrideredirect = ttk.Label(self.toplevel4winConfig, text = "Set the override redirect flag?")
        label4overrideredirect.grid(row = 100, column = 1)
        bool_overrideredirect = BooleanVar(value = False)
        frame4overrideredirect = ttk.Frame(self.toplevel4winConfig)
        frame4overrideredirect.grid(row = 100, column =2)
        radioTrue4overrideredirect = ttk.Radiobutton(frame4overrideredirect, variable = bool_overrideredirect,
                                                     text="Yes", value = True, command = command4overrideredirect)
        radioTrue4overrideredirect.pack(side = LEFT, padx = 20)
        radioFalse4overrideredirect = ttk.Radiobutton(frame4overrideredirect, variable = bool_overrideredirect,
                                                      text = "No", value = False, command = command4overrideredirect)
        radioFalse4overrideredirect.pack(side = RIGHT)

        ### maxsize
        def command4maxsize():
            new_maxsize_width = entry4maxsize_width.get()
            new_maxsize_height = entry4maxsize_height.get()
            windowDesign.maxsize(width = new_maxsize_width, height = new_maxsize_height)
            dictDesignWindowPropCollect["maxsize"] = f"windowDesign.maxsize(width = {new_maxsize_width}, " \
                                                     f"height = {new_maxsize_height})"
        label4maxsize = ttk.Label(self.toplevel4winConfig, text = "Maximum size for the window")
        label4maxsize.grid(row = 110, column = 1)
        frame4maxsize = ttk.Frame(self.toplevel4winConfig)
        frame4maxsize.grid(row = 110, column = 2)
        label4maxsize_width = ttk.Label(frame4maxsize, text = "width:", font = ("TkDefaultFont", 9, "bold"))
        label4maxsize_width.grid(row = 1, column = 1)
        entry4maxsize_width = ttk.Entry(frame4maxsize, width = 7)
        entry4maxsize_width.grid(row = 2, column = 1, padx = 5)
        label4maxsize_height = ttk.Label(frame4maxsize, text = "height:", font = ("TkDefaultFont", 9, "bold"))
        label4maxsize_height.grid(row=1, column=2)
        entry4maxsize_height = ttk.Entry(frame4maxsize, width = 7)
        entry4maxsize_height.grid(row=2, column=2)
        button4maxsize = ttk.Button(frame4maxsize, width = 3, text = ">>", command = command4maxsize)
        button4maxsize.grid(row = 1, rowspan = 2, column = 3, padx = 10)

        ### minsize
        def command4minsize():
            new_minsize_width = entry4minsize_width.get()
            new_minsize_height = entry4minsize_height.get()
            windowDesign.minsize(width = new_minsize_width, height = new_minsize_height)
            dictDesignWindowPropCollect["minsize"] = f"windowDesign.minsize(width = {new_minsize_width}, " \
                                                     f"height = {new_minsize_height})"
        label4minsize = ttk.Label(self.toplevel4winConfig, text="Minimum size for the window")
        label4minsize.grid(row=120, column=1)
        frame4minsize = ttk.Frame(self.toplevel4winConfig)
        frame4minsize.grid(row=120, column=2)
        label4minsize_width = ttk.Label(frame4minsize, text="width:", font = ("TkDefaultFont", 9, "bold"))
        label4minsize_width.grid(row=1, column=1)
        entry4minsize_width = ttk.Entry(frame4minsize, width=7)
        entry4minsize_width.grid(row=2, column=1, padx=5)
        label4minsize_height = ttk.Label(frame4minsize, text="height:", font = ("TkDefaultFont", 9, "bold"))
        label4minsize_height.grid(row=1, column=2)
        entry4minsize_height = ttk.Entry(frame4minsize, width=7)
        entry4minsize_height.grid(row=2, column=2)
        button4minsize = ttk.Button(frame4minsize, width=3, text=">>", command = command4minsize)
        button4minsize.grid(row=1, rowspan=2, column=3, padx = 10)
        
        def command4okay_button():
            print(dictDesignWindowPropCollect)
            self.toplevel4winConfig.destroy()
        button4okay = ttk.Button(self.toplevel4winConfig, text = "Okay", command = command4okay_button)
        button4okay.grid(row = 130, column = 7)

    def exitDesignWindowSetup(self):
        pass

        

    # def destroy(self):
    #     self.toplevel4winConfig.destroy()

    
class WidgetArrange:
    def __init__(self):
        global iswidget
        iswidget = 0  ### Variable to determine type of Widget to place on Design Window

        ###  Variables to count type of Widget placed on Design Window
        self.widget_button = 1
        self.widget_checkbutton = 1
        self.widget_entry = 1
        self.widget_label = 1
        self.widget_listbox = 1
        self.widget_menu = 1
        self.widget_menubutton = 1
        self.widget_message = 1
        self.widget_optionmenu = 1
        self.widget_scale = 1
        self.widget_scrollbar = 1
        self.widget_spinbox = 1
        self.widget_text = 1
        self.widget_radiobutton = 1
        self.widget_frame = 1
        self.widget_labelframe = 1
        self.widget_panedwindow = 1
        self.widget_toplevel = 1

        ### Variable List to hold handle Widgets that have been added to the Listbox
        self.list_widget_lists = []  ###

        ### Variable List to hold handle Widgets that have been paned to the PanedWindow
        self.dict_widget_panes = {} ###

        ### Dictionary that contains ATTRIBUTES and VALUES of a widget to be displayed
        self.dictCountWidget = {}

        ### Dictionary that contains place layout configurations of all the widgets
        self.dictLayoutConfig = {}

    def focusWidgetTree(self, event):

        self.focus_get = windowObject.tree4Widget.focus()
        
    def createList(self):

        for gg in windowObject.list_entry_list:
            try:
                gg.get()
                self.dictCountWidget[arrangeObject.focus_get].insert(END, gg.get())

            except:
                pass

            else:
                if gg.get() in self.list_widget_lists:
                    pass
                else:
                    self.list_widget_lists.append(gg.get())

    def createPane(self):

        for gg in windowObject.pane_entry_list:
            try:
                gg.get()
                self.dictCountWidget[gg.get()].lift(self.dictCountWidget[arrangeObject.focus_get])
                self.dictCountWidget[arrangeObject.focus_get].add(self.dictCountWidget[gg.get()])

            except:
                pass

            else:
                list_panes = list(self.dict_widget_panes.values())
                print(list_panes)
                if gg.get() in list_panes:
                    pass
                else:
                    self.dict_widget_panes[gg.get()] = arrangeObject.focus_get


    def motionRelease(self,event):
        global iswidget
        iswidget = None
        try:
            self.focus_get = event.widget.widgetName
            try:
                windowObject.tree4Widget.selection_set(self.focus_get)
            except:
                if self.focus_get.startswith("FramePW"):
                    self.focus_get = event.widget.children["!panedwindow"].widgetName
                    windowObject.tree4Widget.selection_set(self.focus_get)

            event.widget.focus()
            windowObject.tree4Widget.focus(self.focus_get)

            if self.focus_get.startswith("Button"):
                windowObject.determineButton(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                     "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainButton()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k,v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:

                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0,v[1])
                        except:
                            eval(f"windowObject.bool_{k}.set(v[1])")


            elif self.focus_get.startswith("Checkbutton"):
                windowObject.determineCheckbutton(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                     "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainCheckbutton()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))

                    for k,v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0,str(v[1]))
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")


            elif self.focus_get.startswith("Entry"):
                windowObject.determineEntry(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                     "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainEntry()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))

                    for k,v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0,v[1])
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("LabelFrame"):
                windowObject.determineLabelFrame(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainLabelFrame()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    print(dictAttributeCollect)
                    for k,v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0)
                            dictAttributeCollect[k][0].insert(0,v[1])
                        except:
                            eval(f"windowObject.bool_{k}.set(v[1])")
                            
                            
            elif self.focus_get.startswith("Label"):
                windowObject.determineLabel(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                     "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainLabel()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))

                    for k,v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0,v[1])
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Listbox"):
                windowObject.determineListbox(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                     "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainListbox()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))

                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, v[1])
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Menubutton"):
                windowObject.determineMenubutton(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainMenubutton()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))

                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, v[1])
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Message"):
                windowObject.determineMessage(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainMessage()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    print(dictAttributeCollect)
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            try:
                                dictAttributeCollect[k][0].delete(0, END)
                                dictAttributeCollect[k][0].insert(0, v[1])
                            except AttributeError:
                                eval(f"windowObject.bool_{k}.set(v[1])")
                        except:
                            eval(f"windowObject.int_{k}.set(v[1])")

            elif self.focus_get.startswith("Radiobutton"):
                windowObject.determineRadiobutton(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainRadiobutton()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, str(v[1]))
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Scale"):
                windowObject.determineScale(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}

                if event.widget.winfo_name() == "!scale_h":
                    windowObject.spinbox4width.insert(END, int(res["height"])-70)
                elif event.widget.winfo_name() == "!scale_v":
                    windowObject.spinbox4width.insert(END, int(res["width"])-70)
                windowObject.mainScale()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    print(dictAttributeCollect)
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            try:
                                dictAttributeCollect[k][0].delete(0, END)
                                dictAttributeCollect[k][0].insert(0, v[1])
                            except AttributeError:
                                eval(f"windowObject.bool_{k}.set(v[1])")
                        except:
                            eval(f"windowObject.int_{k}.set(v[1])")

            elif self.focus_get.startswith("Spinbox"):
                windowObject.determineSpinbox(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, str(v[1]))
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Text"):
                windowObject.determineText(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainText()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, str(v[1]))
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("Frame"):
                windowObject.determineFrame(None)
                res = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[self.focus_get] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                windowObject.mainFrame()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            dictAttributeCollect[k][0].delete(0, END)
                            dictAttributeCollect[k][0].insert(0, str(v[1]))
                        except AttributeError:
                            eval(f"windowObject.bool_{k}.set(v[1])")

            elif self.focus_get.startswith("PanedWindow"):

                self.dictCountWidget[event.widget.master.widgetName].config(borderwidth = 2, relief = "solid")

                windowObject.determinePanedWindow(None)
                res = self.dictCountWidget[event.widget.master.widgetName].place_info()
                res_sub = self.dictCountWidget[self.focus_get].place_info()
                self.dictLayoutConfig[event.widget.master.widgetName] = {"x": res["x"], "y": res["y"], "width": res["width"],
                                                         "height": res["height"], "anchor": res["anchor"]}
                self.dictLayoutConfig[self.focus_get] = {"relwidth": res_sub["relwidth"], "relheight": res_sub["relheight"],
                                                        "anchor": res_sub["anchor"]}
                windowObject.mainPanedWindow()
                windowObject.entry4widget_variable.insert(0, self.focus_get)
                if self.focus_get in dictAttributeEditorUpdate:
                    dictAttributeCollect = dict(sorted(dictAttributeEditorUpdate[self.focus_get].items()))
                    for k, v in zip(dictAttributeCollect.keys(), dictAttributeCollect.values()):
                        try:
                            try:
                                dictAttributeCollect[k][0].delete(0, END)
                                dictAttributeCollect[k][0].insert(0, v[1])
                            except AttributeError:
                                eval(f"windowObject.bool_{k}.set(v[1])")
                        except:
                            eval(f"windowObject.int_{k}.set(v[1])")



        except AttributeError:
            pass


    # def release(self, event):
    #     try:
    #         res = self.dictCountWidget[self.identifier].place_info()
    #         print(self.identifier, res)
    #     except AttributeError:
    #         pass

    def refreshAttributes(self):

        try:
            if arrangeObject.focus_get.startswith("Button") == True:
                # self.dictCountWidget[arrangeObject.focus_get].focus()
                # print(arrangeObject.focus_get)
                DragDropResizeWidget.__bases__ = (Button,)

                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]

                listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("default"); listAttr.remove("fg");
                listAttr.remove("height"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground, windowObject.entry4activeforeground,
                           windowObject.combo4anchor,
                           windowObject.entry4background, windowObject.combo4bitmap, windowObject.spinbox4borderwidth,
                           windowObject.entry4command, windowObject.combo4compound,
                           windowObject.combo4cursor, windowObject.entry4disabledforeground,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4image, windowObject.combo4justify,
                           windowObject.combo4overrelief, windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief, windowObject.spinbox4repeatdelay, windowObject.spinbox4repeatinterval,
                           windowObject.combo4state, windowObject.bool_takefocus, windowObject.entry4text,
                           windowObject.entrytextvariable,
                           windowObject.entry4underline, windowObject.entry4wraplength]
                for i,j in zip(listAttr, listVal):

                    if i == "command":
                        if (i == "command") & (j.get() == ""):
                            windowObject.commands_all[arrangeObject.focus_get] = None
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                        else:
                            windowObject.commands_all[arrangeObject.focus_get] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j,j.get()]

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "image") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                    
                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                                
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                                windowObject.implementFont_determine = 0

                            if windowObject.implementImage_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                                arrangeObject.dictCountWidget[arrangeObject.focus_get].image = j.get()

                                windowObject.implementImage_determine = 0
                                windowObject.count_image_instances += 1
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                try:
                    del dict_[arrangeObject.focus_get]["command"]
                except KeyError:
                    pass

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)
                # print(dict_)
                # print(dictAttributeCollect)
                # print(dictAttributeEditorUpdate)

            elif arrangeObject.focus_get.startswith("Checkbutton") == True:
                DragDropResizeWidget.__bases__ = (Checkbutton,)

                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("offvalue"); listAttr.remove("onvalue");
                listAttr.remove("tristateimage"); listAttr.remove("tristatevalue"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground, windowObject.entry4activeforeground,
                           windowObject.combo4anchor,
                           windowObject.entry4background, windowObject.combo4bitmap, windowObject.spinbox4borderwidth,
                           windowObject.entry4command, windowObject.combo4compound,
                           windowObject.combo4cursor, windowObject.entry4disabledforeground,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4image, windowObject.bool_indicatoron,
                           windowObject.combo4justify, windowObject.combo4offrelief,
                           windowObject.combo4overrelief, windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief, windowObject.entry4selectcolor, windowObject.entry4selectimage,
                           windowObject.combo4state, windowObject.bool_takefocus, windowObject.entry4text,
                           windowObject.entrytextvariable, windowObject.entry4underline, windowObject.entry4variable,
                           windowObject.entry4wraplength]

                for i, j in zip(listAttr, listVal):
                    if i == "command":
                        if (i == "command") & (j.get() == ""):
                            windowObject.commands_all[arrangeObject.focus_get] = None
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                        else:
                            windowObject.commands_all[arrangeObject.focus_get] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "image") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            if windowObject.implementImage_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                arrangeObject.dictCountWidget[arrangeObject.focus_get].image = j.get()

                                windowObject.implementImage_determine = 0
                                windowObject.count_image_instances += 1
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                try:
                    del dict_[arrangeObject.focus_get]["command"]
                except KeyError:
                    pass
                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Entry") == True:
                DragDropResizeWidget.__bases__ = (Entry,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("fg");  listAttr.remove("invcmd");
                listAttr.remove("vcmd"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4background, windowObject.spinbox4borderwidth, windowObject.combo4cursor,
                           windowObject.entry4disabledbackground, windowObject.entry4disabledforeground,
                           windowObject.bool_exportselection, windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4insertbackground,
                           windowObject.spinbox4insertborderwidth, windowObject.spinbox4insertofftime,
                           windowObject.spinbox4insertontime, windowObject.spinbox4insertwidth,
                           windowObject.entry4invalidcommand, windowObject.combo4justify,
                           windowObject.entry4readonlybackground, windowObject.combo4relief,
                           windowObject.entry4selectbackground, windowObject.spinbox4selectborderwidth,
                           windowObject.entry4selectforeground, windowObject.entry4show, windowObject.combo4state,
                           windowObject.bool_takefocus, windowObject.entrytextvariable, windowObject.combo4validate,
                           windowObject.entry4validatecommand, windowObject.entry4xscrollcommand]
                for i,j in zip(listAttr,listVal):

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("LabelFrame") == True:
                DragDropResizeWidget.__bases__ = (LabelFrame,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("class");  listAttr.remove("colormap");
                listAttr.remove("container"); listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("visual"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4background, windowObject.spinbox4borderwidth, windowObject.combo4cursor,
                           windowObject.entry4font, windowObject.entry4foreground, windowObject.entry4highlightbackground,
                           windowObject.entry4highlightcolor, windowObject.spinbox4highlightthickness,
                           windowObject.combo4labelanchor, windowObject.entry4labelwidget,
                           windowObject.spinbox4padx, windowObject.spinbox4pady, windowObject.combo4relief,
                           windowObject.bool_takefocus, windowObject.entry4text]

                for i,j in zip(listAttr, listVal):
                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                
                windowPRO.after(40, self.refreshAttributes)


            elif arrangeObject.focus_get.startswith("Label") == True:
                DragDropResizeWidget.__bases__ = (Label,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground, windowObject.entry4activeforeground,
                           windowObject.combo4anchor,
                           windowObject.entry4background, windowObject.combo4bitmap, windowObject.spinbox4borderwidth,
                           windowObject.combo4compound,
                           windowObject.combo4cursor, windowObject.entry4disabledforeground,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4image, windowObject.combo4justify,
                           windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief,
                           windowObject.combo4state, windowObject.bool_takefocus, windowObject.entry4text,
                           windowObject.entrytextvariable,
                           windowObject.entry4underline, windowObject.entry4wraplength]

                for i, j in zip(listAttr, listVal):

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "image") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0

                            if windowObject.implementImage_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                arrangeObject.dictCountWidget[arrangeObject.focus_get].image = j.get()
                                windowObject.implementImage_determine = 0
                                windowObject.count_image_instances += 1
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Listbox") == True:
                DragDropResizeWidget.__bases__ = (Listbox,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("setgrid"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.combo4activestyle, windowObject.entry4background,
                           windowObject.spinbox4borderwidth, windowObject.combo4cursor,
                           windowObject.entry4disabledforeground,
                           windowObject.bool_exportselection, windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness,
                           windowObject.combo4justify, windowObject.entry4listvariable, windowObject.combo4relief,
                           windowObject.entry4selectbackground, windowObject.spinbox4selectborderwidth,
                           windowObject.entry4selectforeground, windowObject.combo4selectmode, windowObject.combo4state,
                           windowObject.bool_takefocus, windowObject.entry4xscrollcommand,
                           windowObject.entry4yscrollcommand]

                for i,j in zip(listAttr,listVal):

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Menubutton") == True:
                DragDropResizeWidget.__bases__ = (Menubutton,)
                self.dictCountWidget[arrangeObject.focus_get].focus()
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground, windowObject.entry4activeforeground,
                           windowObject.combo4anchor,
                           windowObject.entry4background, windowObject.combo4bitmap, windowObject.spinbox4borderwidth,
                           windowObject.combo4compound, windowObject.combo4cursor,
                           windowObject.combo4direction, windowObject.entry4disabledforeground,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4image,
                           windowObject.bool_indicatoron, windowObject.combo4justify, windowObject.entry4menu,
                           windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief, windowObject.combo4state, windowObject.bool_takefocus,
                           windowObject.entry4text, windowObject.entrytextvariable,
                           windowObject.entry4underline, windowObject.entry4wraplength]

                for i,j in zip(listAttr, listVal):

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "image") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0

                            if windowObject.implementImage_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                arrangeObject.dictCountWidget[arrangeObject.focus_get].image = j.get()
                                windowObject.implementImage_determine = 0
                                windowObject.count_image_instances += 1
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Message") == True:
                DragDropResizeWidget.__bases__ = (Message,)
                self.dictCountWidget[arrangeObject.focus_get].focus()

                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("fg"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.combo4anchor, windowObject.int_aspect,
                           windowObject.entry4background, windowObject.spinbox4borderwidth,
                           windowObject.combo4cursor,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.combo4justify,
                           windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief,  windowObject.bool_takefocus,
                           windowObject.entry4text, windowObject.entrytextvariable, ]

                for i,j in zip(listAttr, listVal):
                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Radiobutton") == True:
                DragDropResizeWidget.__bases__ = (Radiobutton,)
                self.dictCountWidget[arrangeObject.focus_get].focus()
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("fg"); listAttr.remove("height");
                listAttr.remove("tristateimage"); listAttr.remove("tristatevalue"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground, windowObject.entry4activeforeground,
                           windowObject.combo4anchor,
                           windowObject.entry4background, windowObject.combo4bitmap, windowObject.spinbox4borderwidth,
                           windowObject.entry4command, windowObject.combo4compound,
                           windowObject.combo4cursor, windowObject.entry4disabledforeground,
                           windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4image,
                           windowObject.bool_indicatoron,
                           windowObject.combo4justify, windowObject.combo4offrelief,
                           windowObject.combo4overrelief, windowObject.spinbox4padx, windowObject.spinbox4pady,
                           windowObject.combo4relief, windowObject.entry4selectcolor, windowObject.entry4selectimage,
                           windowObject.combo4state, windowObject.bool_takefocus, windowObject.entry4text,
                           windowObject.entrytextvariable, windowObject.entry4underline, windowObject.entry4value,
                           windowObject.entry4variable, windowObject.entry4wraplength]

                for i,j in zip(listAttr, listVal):
                    if i == "command":
                        if (i == "command") & (j.get() == ""):
                            windowObject.commands_all[arrangeObject.focus_get] = None
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                        else:
                            windowObject.commands_all[arrangeObject.focus_get] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "image") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "text") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0

                            if windowObject.implementImage_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                arrangeObject.dictCountWidget[arrangeObject.focus_get].image = j.get()
                                windowObject.implementImage_determine = 0
                                windowObject.count_image_instances += 1
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                try:
                    del dict_[arrangeObject.focus_get]["command"]
                except KeyError:
                    pass
                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Scale") == True:
            # self.dictCountWidget[arrangeObject.focus_get].focus()
            # print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bigincrement"), listAttr.remove("bd"); listAttr.remove("bg"); listAttr.remove("fg");
                listAttr.remove("length"); listAttr.remove("orient"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground,
                           windowObject.entry4background, windowObject.spinbox4borderwidth,
                           windowObject.entry4command,
                           windowObject.combo4cursor, windowObject.spinbox4digits,
                           windowObject.entry4font, windowObject.entry4foreground, windowObject.entry4from_,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4label,
                           windowObject.combo4relief, windowObject.spinbox4repeatdelay, windowObject.spinbox4repeatinterval,
                           windowObject.entry4resolution, windowObject.bool_showvalue, windowObject.int_sliderlength,
                           windowObject.combo4sliderrelief,
                           windowObject.combo4state, windowObject.bool_takefocus, windowObject.entry4tickinterval,
                           windowObject.entry4to, windowObject.entry4troughcolor, windowObject.entry4variable]
                for i,j in zip(listAttr, listVal):
                    if i == "command":
                        if (i == "command") & (j.get() == ""):
                            windowObject.commands_all[arrangeObject.focus_get] = None
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                        else:
                            windowObject.commands_all[arrangeObject.focus_get] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    if (i == "label") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = ""
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                try:
                    del dict_[arrangeObject.focus_get]["command"]
                except KeyError:
                    pass
                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Spinbox") == True:
                DragDropResizeWidget.__bases__ = (Spinbox,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("fg");  listAttr.remove("invcmd");
                listAttr.remove("vcmd"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4activebackground,windowObject.entry4background,
                           windowObject.spinbox4borderwidth, windowObject.entry4buttonbackground,
                           windowObject.combo4buttoncursor, windowObject.combo4buttondownrelief,
                           windowObject.combo4buttonuprelief, windowObject.entry4command,windowObject.combo4cursor,
                           windowObject.entry4disabledbackground, windowObject.entry4disabledforeground,
                           windowObject.bool_exportselection, windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4format, windowObject.entry4from_,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4increment,
                           windowObject.entry4insertbackground,
                           windowObject.spinbox4insertborderwidth, windowObject.spinbox4insertofftime,
                           windowObject.spinbox4insertontime, windowObject.spinbox4insertwidth,
                           windowObject.entry4invalidcommand, windowObject.combo4justify,
                           windowObject.entry4readonlybackground, windowObject.combo4relief,
                           windowObject.spinbox4repeatdelay, windowObject.spinbox4repeatinterval,
                           windowObject.entry4selectbackground, windowObject.spinbox4selectborderwidth,
                           windowObject.entry4selectforeground, windowObject.combo4state,
                           windowObject.bool_takefocus, windowObject.entrytextvariable, windowObject.entry4to,
                           windowObject.combo4validate, windowObject.entry4validatecommand,
                           windowObject.entry4values, windowObject.bool_wrap, windowObject.entry4xscrollcommand]
                for i,j in zip(listAttr,listVal):
                    if i == "command":
                        if (i == "command") & (j.get() == ""):
                            windowObject.commands_all[arrangeObject.focus_get] = None
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]
                        else:
                            windowObject.commands_all[arrangeObject.focus_get] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                try:
                    del dict_[arrangeObject.focus_get]["command"]
                except KeyError:
                    pass
                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Text") == True:
                DragDropResizeWidget.__bases__ = (Text,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("endline"); listAttr.remove("fg");
                listAttr.remove("height"); listAttr.remove("setgrid"); listAttr.remove("startline");
                listAttr.remove("tabstyle"); listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.bool_autoseparators, windowObject.entry4background, windowObject.bool_blockcursor,
                           windowObject.spinbox4borderwidth, windowObject.combo4cursor,
                           windowObject.bool_exportselection, windowObject.entry4font, windowObject.entry4foreground,
                           windowObject.entry4highlightbackground, windowObject.entry4highlightcolor,
                           windowObject.spinbox4highlightthickness, windowObject.entry4inactiveselectbackground,
                           windowObject.entry4insertbackground,
                           windowObject.spinbox4insertborderwidth, windowObject.spinbox4insertofftime,
                           windowObject.spinbox4insertontime, windowObject.combo4insertunfoccussed,
                           windowObject.spinbox4insertwidth, windowObject.entry4maxundo, windowObject.spinbox4padx,
                           windowObject.spinbox4pady, windowObject.combo4relief,
                           windowObject.entry4selectbackground, windowObject.spinbox4selectborderwidth,
                           windowObject.entry4selectforeground, windowObject.spinbox4spacing1, windowObject.spinbox4spacing2,
                           windowObject.spinbox4spacing3, windowObject.combo4state, windowObject.entry4tabs,
                           windowObject.bool_takefocus, windowObject.bool_undo, windowObject.combo4wrap_Text,
                           windowObject.entry4xscrollcommand, windowObject.entry4yscrollcommand]
                for i,j in zip(listAttr,listVal):

                    if (i == "font") & (j.get() == ""):
                        dict_[arrangeObject.focus_get][i] = "TkDefaultFont"
                        dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, ""]

                    elif j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            if windowObject.implementFont_determine == 22:
                                dict_[arrangeObject.focus_get][i] = j.get()
                                windowObject.implementFont_determine = 0
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(1000, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("Frame") == True:
                DragDropResizeWidget.__bases__ = (Frame,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("class");  listAttr.remove("colormap");
                listAttr.remove("container"); listAttr.remove("height"); listAttr.remove("visual");
                listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4background, windowObject.spinbox4borderwidth,
                           windowObject.combo4cursor, windowObject.entry4highlightbackground,
                           windowObject.entry4highlightcolor, windowObject.spinbox4highlightthickness,
                           windowObject.spinbox4padx, windowObject.spinbox4pady, windowObject.combo4relief,
                           windowObject.bool_takefocus]

                for i,j in zip(listAttr, listVal):

                    if j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)

            elif arrangeObject.focus_get.startswith("PanedWindow") == True:
                DragDropResizeWidget.__bases__ = (Frame,)

                #print(arrangeObject.focus_get)
                listAttr = [x for x in self.dictCountWidget[arrangeObject.focus_get].keys()]
                listAttr.remove("bd"); listAttr.remove("bg");  listAttr.remove("height");
                listAttr.remove("proxybackground"); listAttr.remove("proxyborderwidth"); listAttr.remove("proxyrelief");
                listAttr.remove("width")
                listAttr.sort()
                listVal = [windowObject.entry4background, windowObject.spinbox4borderwidth, windowObject.combo4cursor,
                           windowObject.spinbox4handlepad, windowObject.spinbox4handlesize,
                           windowObject.bool_opaqueresize, windowObject.combo4orient,
                           windowObject.combo4relief, windowObject.combo4sashcursor, windowObject.int_sashpad,
                           windowObject.combo4sashrelief, windowObject.int_sashwidth, windowObject.bool_showhandle]

                for i,j in zip(listAttr, listVal):

                    if j.get() == "":
                        continue
                    else:
                        try:
                            try:
                                assert type(j.get()) is bool
                                dict_[arrangeObject.focus_get][i] = j.get()
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]
                                
                            except:
                                j_int = int(j.get())
                                dict_[arrangeObject.focus_get][i] = j_int
                                dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j_int]
                        except:
                            dict_[arrangeObject.focus_get][i] = j.get()
                            dictAttributeEditorUpdate[arrangeObject.focus_get][i] = [j, j.get()]

                self.dictCountWidget[arrangeObject.focus_get].config(**dict_[arrangeObject.focus_get])
                windowPRO.after(40, self.refreshAttributes)



        except (AttributeError, TclError,):
            # print("okay")
            windowPRO.after(10, self.refreshAttributes)


    def executeWidgetsOnDesignWindow(self, event):
        global iswidget

        try:
            if event.widget.widgetName.startswith("PanedWindow"):
                self.dictCountWidget[event.widget.master.widgetName].config(borderwidth = 2, relief = SOLID)
            elif event.widget.widgetName.startswith("FramePW"):
                self.dictCountWidget[event.widget.widgetName].config(borderwidth=2, relief=SOLID)

        except:
             for ii in self.dictCountWidget:
                 if ii.startswith("FramePW"):
                     self.dictCountWidget[ii].config(borderwidth = 0, relief = SOLID)

        if iswidget == "button":

            dict_[list_button[self.widget_button]] = {"text": f"Button{self.widget_button}"}
            dictAttributeEditorUpdate[list_button[self.widget_button]] = {}     ### Initiate storage of Attributes for every widget

            if str(event.widget) == ".":
                self.dictLayoutConfig[list_button[self.widget_button]] = {"x": event.x, "y": event.y, "width": 70,
                                                                          "height": 30, "anchor": "nw"}
            elif str(event.widget).startswith(".!scale") == True:
                self.dictLayoutConfig[list_button[self.widget_button]] = {"x": event.widget.winfo_x() + event.x,
                                                    "y": event.widget.winfo_y() + event.y, "width": 70, "height": 30,
                                                                          "anchor": "nw"}
            elif str(event.widget).startswith(".!dragdropresizewidget") == True:
                self.dictLayoutConfig[list_button[self.widget_button]] = {"x": event.widget.winfo_x() + event.x,
                                                                          "y": event.widget.winfo_y() + event.y,
                                                                          "width": 70, "height": 30, "anchor": "nw"}

            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Button{self.widget_button}",
                                            text=f"Button{self.widget_button}")
            windowObject.tree4Widget.selection_set(f"Button{self.widget_button}")
            windowObject.tree4Widget.focus(f"Button{self.widget_button}")
            DragDropResizeWidget.__bases__ = (Button,)
            self.dictCountWidget[f"Button{self.widget_button}"] = DragDropResizeWidget(windowDesign,
                                                                         **dict_[list_button[self.widget_button]])
            self.dictCountWidget[f"Button{self.widget_button}"].place(**self.dictLayoutConfig[list_button[self.widget_button]])
            self.dictCountWidget[f"Button{self.widget_button}"].focus()

            self.dictCountWidget[f"Button{self.widget_button}"].widgetName = f"Button{self.widget_button}"
            windowObject.mainButton()
            windowObject.entry4text.delete(0, END)
            windowObject.entry4text.insert(0, f"Button{self.widget_button}")
            windowObject.entry4widget_variable.insert(END, f"Button{self.widget_button}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_button += 1


        elif iswidget == "checkbutton":
            dict_[list_checkbutton[self.widget_checkbutton]] = {"text": f"Checkbutton{self.widget_checkbutton}"}
            dictAttributeEditorUpdate[
                list_checkbutton[self.widget_checkbutton]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_checkbutton[self.widget_checkbutton]] = {"x": event.x, "y": event.y, "width": 100,
                                                                            "height": 30, "anchor": "nw"}

            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Checkbutton{self.widget_checkbutton}",
                                            text=f"Checkbutton{self.widget_checkbutton}")
            windowObject.tree4Widget.selection_set(f"Checkbutton{self.widget_checkbutton}")
            windowObject.tree4Widget.focus(f"Checkbutton{self.widget_checkbutton}")
            DragDropResizeWidget.__bases__ = (Checkbutton,)
            self.dictCountWidget[f"Checkbutton{self.widget_checkbutton}"] = DragDropResizeWidget(windowDesign,
                                                                                        **dict_[list_checkbutton[self.widget_checkbutton]])
            self.dictCountWidget[f"Checkbutton{self.widget_checkbutton}"].place(**self.dictLayoutConfig[list_checkbutton[self.widget_checkbutton]])
            self.dictCountWidget[f"Checkbutton{self.widget_checkbutton}"].focus()

            self.dictCountWidget[f"Checkbutton{self.widget_checkbutton}"].widgetName = f"Checkbutton{self.widget_checkbutton}"
            windowObject.mainCheckbutton()
            windowObject.entry4text.insert(0, f"Checkbutton{self.widget_checkbutton}")
            windowObject.entry4widget_variable.insert(END, f"Checkbutton{self.widget_checkbutton}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_checkbutton += 1

        elif iswidget == "entry":
            dict_[list_entry[self.widget_entry]] = {}
            dictAttributeEditorUpdate[
                list_entry[self.widget_entry]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_entry[self.widget_entry]] = {"x": event.x, "y": event.y, "width": 100,
                                                                    "height": 20, "anchor": "nw"}
            windowObject.tree4Widget.insert("Design Window", index = END, iid = f"Entry{self.widget_entry}",
                                            text = f"Entry{self.widget_entry}")
            windowObject.tree4Widget.selection_set(f"Entry{self.widget_entry}")
            windowObject.tree4Widget.focus(f"Entry{self.widget_entry}")
            DragDropResizeWidget.__bases__ = (Entry,)
            self.dictCountWidget[f"Entry{self.widget_entry}"] = DragDropResizeWidget(windowDesign, **dict_[list_entry[
                                                                                            self.widget_entry]])
            self.dictCountWidget[f"Entry{self.widget_entry}"].place(**self.dictLayoutConfig[list_entry[self.widget_entry]])
            self.dictCountWidget[f"Entry{self.widget_entry}"].focus()

            self.dictCountWidget[f"Entry{self.widget_entry}"].widgetName = f"Entry{self.widget_entry}"
            windowObject.mainEntry()
            windowObject.entry4widget_variable.insert(END, f"Entry{self.widget_entry}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_entry += 1

        elif iswidget == "label":
            dict_[list_label[self.widget_label]] = {"text": f"Label{self.widget_label}"}
            dictAttributeEditorUpdate[
                list_label[self.widget_label]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_label[self.widget_label]] = {"x": event.x, "y": event.y, "width": 70,
                                                                    "height": 30, "anchor": "nw"}
            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Label{self.widget_label}",
                                            text=f"Label{self.widget_label}")
            windowObject.tree4Widget.selection_set(f"Label{self.widget_label}")
            windowObject.tree4Widget.focus(f"Label{self.widget_label}")
            DragDropResizeWidget.__bases__ = (Label,)
            self.dictCountWidget[f"Label{self.widget_label}"] = DragDropResizeWidget(windowDesign, **dict_[list_label[
                self.widget_label]])
            self.dictCountWidget[f"Label{self.widget_label}"].place(**self.dictLayoutConfig[list_label[self.widget_label]])
            self.dictCountWidget[f"Label{self.widget_label}"].focus()

            self.dictCountWidget[f"Label{self.widget_label}"].widgetName = f"Label{self.widget_label}"
            windowObject.mainLabel()
            windowObject.entry4text.insert(0, f"Label{self.widget_label}")
            windowObject.entry4widget_variable.insert(END, f"Label{self.widget_label}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_label += 1

        elif iswidget == "listbox":
            dict_[list_listbox[self.widget_listbox]] = {}
            dictAttributeEditorUpdate[
                list_listbox[self.widget_listbox]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_listbox[self.widget_listbox]] = {"x": event.x, "y": event.y, "width": 120,
                                                                        "height": 150, "anchor": "nw"}
            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Listbox{self.widget_listbox}",
                                            text=f"Listbox{self.widget_listbox}")
            windowObject.tree4Widget.selection_set(f"Listbox{self.widget_listbox}")
            windowObject.tree4Widget.focus(f"Listbox{self.widget_listbox}")
            DragDropResizeWidget.__bases__ = (Listbox,)
            self.dictCountWidget[f"Listbox{self.widget_listbox}"] = DragDropResizeWidget(windowDesign,
                                                                            **dict_[list_listbox[self.widget_listbox]])
            self.dictCountWidget[f"Listbox{self.widget_listbox}"].place(**self.dictLayoutConfig[list_listbox[self.widget_listbox]])
            self.dictCountWidget[f"Listbox{self.widget_listbox}"].focus()

            self.dictCountWidget[f"Listbox{self.widget_listbox}"].widgetName = f"Listbox{self.widget_label}"
            windowObject.mainListbox()
            windowObject.entry4widget_variable.insert(END, f"Listbox{self.widget_listbox}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_listbox += 1

        elif iswidget == "menubutton":
            dict_[list_menubutton[self.widget_menubutton]] = {"text": f"Menubutton{self.widget_menubutton}"}
            dictAttributeEditorUpdate[
                list_menubutton[self.widget_menubutton]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_menubutton[self.widget_menubutton]] = {"x": event.x, "y": event.y, "width": 110,
                                                                              "height": 30, "anchor": "nw"}
            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Menubutton{self.widget_menubutton}",
                                            text=f"Menubutton{self.widget_menubutton}")
            windowObject.tree4Widget.selection_set(f"Menubutton{self.widget_menubutton}")
            windowObject.tree4Widget.focus(f"Menubutton{self.widget_menubutton}")
            DragDropResizeWidget.__bases__ = (Menubutton,)
            self.dictCountWidget[f"Menubutton{self.widget_menubutton}"] = DragDropResizeWidget(windowDesign,
                                                                    **dict_[list_menubutton[self.widget_menubutton]])
            self.dictCountWidget[f"Menubutton{self.widget_menubutton}"].place(**self.dictLayoutConfig[list_menubutton[self.widget_menubutton]])
            self.dictCountWidget[f"Menubutton{self.widget_menubutton}"].focus()

            self.dictCountWidget[f"Menubutton{self.widget_menubutton}"].widgetName = f"Menubutton{self.widget_menubutton}"
            windowObject.mainMenubutton()
            windowObject.entry4text.insert(0, f"Menubutton{self.widget_menubutton}")
            windowObject.entry4widget_variable.insert(END, f"Menubutton{self.widget_menubutton}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_menubutton += 1

        elif iswidget == "message":
            dict_[list_message[self.widget_message]] = {"text": f"Message{self.widget_message}"}
            dictAttributeEditorUpdate[
                list_message[self.widget_message]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_message[self.widget_message]] = {"x": event.x, "y": event.y, "width": 100,
                                                                        "height": 30, "anchor": "nw"}

            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Message{self.widget_message}",
                                            text=f"Message{self.widget_message}")
            windowObject.tree4Widget.selection_set(f"Message{self.widget_message}")
            windowObject.tree4Widget.focus(f"Message{self.widget_message}")
            DragDropResizeWidget.__bases__ = (Message,)
            self.dictCountWidget[f"Message{self.widget_message}"] = DragDropResizeWidget(windowDesign,
                                                                        **dict_[list_message[self.widget_message]])
            self.dictCountWidget[f"Message{self.widget_message}"].place(**self.dictLayoutConfig[list_message[self.widget_message]])
            self.dictCountWidget[f"Message{self.widget_message}"].focus()

            self.dictCountWidget[f"Message{self.widget_message}"].widgetName = f"Message{self.widget_message}"
            windowObject.mainMessage()
            windowObject.entry4text.insert(0, f"Message{self.widget_message}")
            windowObject.entry4widget_variable.insert(END, f"Message{self.widget_message}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_message += 1

        elif iswidget == "radiobutton":
            dict_[list_radiobutton[self.widget_radiobutton]] = {"text": f"Radiobutton{self.widget_radiobutton}"}
            dictAttributeEditorUpdate[
                list_radiobutton[self.widget_radiobutton]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_radiobutton[self.widget_radiobutton]] = {"x": event.x, "y": event.y, "width": 100,
                                                                        "height": 30, "anchor": "nw"}

            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Radiobutton{self.widget_radiobutton}",
                                            text=f"Radiobutton{self.widget_radiobutton}")
            windowObject.tree4Widget.selection_set(f"Radiobutton{self.widget_radiobutton}")
            windowObject.tree4Widget.focus(f"Radiobutton{self.widget_radiobutton}")
            DragDropResizeWidget.__bases__ = (Radiobutton,)
            self.dictCountWidget[f"Radiobutton{self.widget_radiobutton}"] = DragDropResizeWidget(windowDesign,
                                                                                         **dict_[list_radiobutton[
                                                                                             self.widget_radiobutton]])
            self.dictCountWidget[f"Radiobutton{self.widget_radiobutton}"].place(
                **self.dictLayoutConfig[list_radiobutton[self.widget_radiobutton]])
            self.dictCountWidget[f"Radiobutton{self.widget_radiobutton}"].focus()

            self.dictCountWidget[f"Radiobutton{self.widget_radiobutton}"].widgetName = f"Radiobutton{self.widget_radiobutton}"
            windowObject.mainRadiobutton()
            windowObject.entry4text.insert(0, f"Radiobutton{self.widget_radiobutton}")
            windowObject.entry4widget_variable.insert(END, f"Radiobutton{self.widget_radiobutton}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_radiobutton += 1

        elif iswidget == "scale_horizontal":
            dict_[list_scale[self.widget_scale]] = {"label": f"Scale{self.widget_scale}", "orient": "horizontal"}
            dictAttributeEditorUpdate[
                list_scale[self.widget_scale]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_scale[self.widget_scale]] = {"x": event.x, "y": event.y, "width": 60,
                                                                        "height": 50, "anchor": "nw"}

            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Scale{self.widget_scale}",
                                            text=f"Scale{self.widget_scale}")
            windowObject.tree4Widget.selection_set(f"Scale{self.widget_scale}")
            windowObject.tree4Widget.focus(f"Scale{self.widget_scale}")
            self.dictCountWidget[f"Scale{self.widget_scale}"] = Scale_H(windowDesign, **dict_[list_scale[
                                                                                             self.widget_scale]])
            self.dictCountWidget[f"Scale{self.widget_scale}"].place(
                **self.dictLayoutConfig[list_scale[self.widget_scale]])
            self.dictCountWidget[f"Scale{self.widget_scale}"].focus()

            self.dictCountWidget[f"Scale{self.widget_scale}"].widgetName = f"Scale{self.widget_scale}"
            windowObject.mainScale()
            windowObject.entry4label.insert(0, f"Scale{self.widget_scale}")
            windowObject.entry4widget_variable.insert(END, f"Scale{self.widget_scale}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_scale += 1

        elif iswidget == "scale_vertical":
            dict_[list_scale[self.widget_scale]] = {"label": f"Scale{self.widget_scale}", "orient": "vertical"}
            dictAttributeEditorUpdate[
                list_scale[self.widget_scale]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_scale[self.widget_scale]] = {"x": event.x, "y": event.y, "width": 60,
                                                                        "height": 100, "anchor": "nw"}

            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Scale{self.widget_scale}",
                                            text=f"Scale{self.widget_scale}")
            windowObject.tree4Widget.selection_set(f"Scale{self.widget_scale}")
            windowObject.tree4Widget.focus(f"Scale{self.widget_scale}")

            self.dictCountWidget[f"Scale{self.widget_scale}"] = Scale_V(windowDesign, **dict_[list_scale[
                                                                                             self.widget_scale]])
            self.dictCountWidget[f"Scale{self.widget_scale}"].place(
                **self.dictLayoutConfig[list_scale[self.widget_scale]])
            self.dictCountWidget[f"Scale{self.widget_scale}"].focus()

            self.dictCountWidget[f"Scale{self.widget_scale}"].widgetName = f"Scale{self.widget_scale}"
            windowObject.mainScale()
            windowObject.entry4label.insert(0, f"Scale{self.widget_scale}")
            windowObject.entry4widget_variable.insert(END, f"Scale{self.widget_scale}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_scale += 1

        elif iswidget == "spinbox":
            dict_[list_spinbox[self.widget_spinbox]] = {}
            dictAttributeEditorUpdate[
                list_spinbox[self.widget_spinbox]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_spinbox[self.widget_spinbox]] = {"x": event.x, "y": event.y, "width": 150,
                                                                        "height": 20, "anchor": "nw"}
            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Spinbox{self.widget_spinbox}",
                                            text=f"Spinbox{self.widget_spinbox}")
            windowObject.tree4Widget.selection_set(f"Spinbox{self.widget_spinbox}")
            windowObject.tree4Widget.focus(f"Spinbox{self.widget_spinbox}")
            DragDropResizeWidget.__bases__ = (Spinbox,)
            self.dictCountWidget[f"Spinbox{self.widget_spinbox}"] = DragDropResizeWidget(windowDesign,
                                                                                         **dict_[list_spinbox[
                                                                                             self.widget_spinbox]])
            self.dictCountWidget[f"Spinbox{self.widget_spinbox}"].place(
                **self.dictLayoutConfig[list_spinbox[self.widget_spinbox]])
            self.dictCountWidget[f"Spinbox{self.widget_spinbox}"].focus()

            self.dictCountWidget[f"Spinbox{self.widget_spinbox}"].widgetName = f"Spinbox{self.widget_spinbox}"
            windowObject.mainSpinbox()
            windowObject.entry4widget_variable.insert(END, f"Spinbox{self.widget_spinbox}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_spinbox += 1

        elif iswidget == "text":
            dict_[list_text[self.widget_text]] = {}
            dictAttributeEditorUpdate[
                list_text[self.widget_text]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_text[self.widget_text]] = {"x": event.x, "y": event.y, "width": 300,
                                                                  "height": 300, "anchor": "nw"}
            windowObject.tree4Widget.insert("Design Window", index = END, iid = f"Text{self.widget_text}",
                                            text = f"Text{self.widget_text}")
            windowObject.tree4Widget.selection_set(f"Text{self.widget_text}")
            windowObject.tree4Widget.focus(f"Text{self.widget_text}")
            DragDropResizeWidget.__bases__ = (Text,)
            self.dictCountWidget[f"Text{self.widget_text}"] = DragDropResizeWidget(windowDesign, **dict_[list_text[
                                                                                            self.widget_text]])
            self.dictCountWidget[f"Text{self.widget_text}"].place(**self.dictLayoutConfig[list_text[self.widget_text]])
            self.dictCountWidget[f"Text{self.widget_text}"].focus()

            self.dictCountWidget[f"Text{self.widget_text}"].widgetName = f"Text{self.widget_text}"
            windowObject.mainText()
            windowObject.entry4widget_variable.insert(END, f"Text{self.widget_text}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_text += 1

        elif iswidget == "frame":
            dict_[list_frame[self.widget_frame]] = {"borderwidth": 2, "relief": "solid"}
            dictAttributeEditorUpdate[
                list_frame[self.widget_frame]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_frame[self.widget_frame]] = {"x": event.x, "y": event.y, "width": 200,
                                                                        "height": 200, "anchor": "nw"}

            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"Frame{self.widget_frame}",
                                            text=f"Frame{self.widget_frame}")
            windowObject.tree4Widget.selection_set(f"Frame{self.widget_frame}")
            windowObject.tree4Widget.focus(f"Frame{self.widget_frame}")
            DragDropResizeWidget.__bases__ = (Frame,)
            self.dictCountWidget[f"Frame{self.widget_frame}"] = DragDropResizeWidget(windowDesign,
                                                                                         **dict_[list_frame[
                                                                                             self.widget_frame]])
            self.dictCountWidget[f"Frame{self.widget_frame}"].place(
                **self.dictLayoutConfig[list_frame[self.widget_frame]])
            self.dictCountWidget[f"Frame{self.widget_frame}"].focus()

            self.dictCountWidget[f"Frame{self.widget_frame}"].widgetName = f"Frame{self.widget_frame}"
            windowObject.mainFrame()
            windowObject.spinbox4borderwidth.insert(END, 2)
            windowObject.combo4relief.insert(END, "solid")
            windowObject.entry4widget_variable.insert(END, f"Frame{self.widget_frame}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_frame += 1

        elif iswidget == "labelframe":
            dict_[list_labelframe[self.widget_labelframe]] = {"text": f"LabelFrame{self.widget_labelframe}"}
            dictAttributeEditorUpdate[
                list_labelframe[self.widget_labelframe]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_labelframe[self.widget_labelframe]] = {"x": event.x, "y": event.y, "width": 200,
                                                                        "height": 200, "anchor": "nw"}

            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"LabelFrame{self.widget_labelframe}",
                                            text=f"LabelFrame{self.widget_labelframe}")
            windowObject.tree4Widget.selection_set(f"LabelFrame{self.widget_labelframe}")
            windowObject.tree4Widget.focus(f"LabelFrame{self.widget_labelframe}")
            DragDropResizeWidget.__bases__ = (LabelFrame,)
            self.dictCountWidget[f"LabelFrame{self.widget_labelframe}"] = DragDropResizeWidget(windowDesign,
                                                                                         **dict_[list_labelframe[
                                                                                             self.widget_labelframe]])
            self.dictCountWidget[f"LabelFrame{self.widget_labelframe}"].place(
                **self.dictLayoutConfig[list_labelframe[self.widget_labelframe]])
            self.dictCountWidget[f"LabelFrame{self.widget_labelframe}"].focus()

            self.dictCountWidget[f"LabelFrame{self.widget_labelframe}"].widgetName = f"LabelFrame{self.widget_labelframe}"
            windowObject.mainLabelFrame()
            windowObject.entry4text.insert(0, f"LabelFrame{self.widget_labelframe}")
            windowObject.entry4widget_variable.insert(END, f"LabelFrame{self.widget_labelframe}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_labelframe += 1

        elif iswidget == "panedwindow":
            dict_[f"FramePW{self.widget_panedwindow}"] = {"borderwidth": 2, "relief": "solid"}
            dict_[list_panedwindow[self.widget_panedwindow]] = {"background": "grey"}
            dictAttributeEditorUpdate[
                list_panedwindow[self.widget_panedwindow]] = {}  ### Initiate storage of Attributes for every widget
            self.dictLayoutConfig[list_framepw[self.widget_panedwindow]] = {"x": event.x, "y": event.y, "width": 200,
                                                                        "height": 200, "anchor": "nw"}
            self.dictLayoutConfig[list_panedwindow[self.widget_panedwindow]] = {"relwidth": 0.8, "relheight": 1}

            windowObject.tree4Widget.insert("Design Window", index=END, iid=f"PanedWindow{self.widget_panedwindow}",
                                            text=f"PanedWindow{self.widget_panedwindow}")
            windowObject.tree4Widget.selection_set(f"PanedWindow{self.widget_panedwindow}")
            windowObject.tree4Widget.focus(f"PanedWindow{self.widget_panedwindow}")
            DragDropResizeWidget.__bases__ = (Frame,)
            self.dictCountWidget[f"FramePW{self.widget_panedwindow}"] = DragDropResizeWidget(windowDesign,
                                                                        **dict_[f"FramePW{self.widget_panedwindow}"])

            self.dictCountWidget[f"FramePW{self.widget_panedwindow}"].place(
                **self.dictLayoutConfig[list_framepw[self.widget_panedwindow]])

            self.dictCountWidget[f"PanedWindow{self.widget_panedwindow}"] = PanedWindow(
                            self.dictCountWidget[f"FramePW{self.widget_panedwindow}"],
                                                                                         **dict_[list_panedwindow[
                                                                                             self.widget_panedwindow]])
            self.dictCountWidget[f"PanedWindow{self.widget_panedwindow}"].place(relwidth = 0.8, relheight = 1)

            self.dictCountWidget[f"PanedWindow{self.widget_panedwindow}"].focus()

            self.dictCountWidget[f"FramePW{self.widget_panedwindow}"].widgetName = f"FramePW{self.widget_panedwindow}"
            self.dictCountWidget[f"PanedWindow{self.widget_panedwindow}"].widgetName = f"PanedWindow{self.widget_panedwindow}"
            windowObject.mainPanedWindow()
            windowObject.entry4background.insert(0, "grey")
            windowObject.entry4widget_variable.insert(END, f"PanedWindow{self.widget_panedwindow}")
            windowObject.entry4widget_variable["state"] = "disabled"
            iswidget = 0
            self.widget_panedwindow += 1


class CodeGenerate:
    def __init__(self):
        self.compile2Shell()
        


    def compile2Text(self):
        toplevel4Text = Toplevel(master = windowPRO, name = "toplevel_textbox")
        toplevel4Text.geometry = ("400x400+500+500")
        toplevel4Text.resizable(False, False)

        def copy_gen_codes():
            windowPRO.clipboard_clear()
            windowPRO.clipboard_append(self.string_final_codes)
            label_copy = Label(toplevel4Text, text = "Copied Successfully", font = ("Segoe UI", 10, "bold"))
            label_copy.pack(fill = X, )

        menu4copy = Menu(tearoff = False)
        menu4copy.add_command(label = "Copy", command = copy_gen_codes)
        toplevel4Text.config(menu = menu4copy)

        scroll4CompileText = Scrollbar(master=toplevel4Text, orient="vertical", )
        scroll4CompileText.pack(side=RIGHT, fill=Y)

        text4CompileText = Text(master = toplevel4Text, yscrollcommand = scroll4CompileText.set)
        text4CompileText.insert(END, self.string_final_codes)
        text4CompileText.config(state = "disabled")
        text4CompileText.pack()
        scroll4CompileText.config(command = text4CompileText.yview)




    def compile2PythonFile(self):
        file_gen_code = filedialog.asksaveasfile("w", filetypes = [("Python file","*.py")], defaultextension = ".py")
        print(file_gen_code)
        file_open = open(file_gen_code.name, "w")
        file_open.write(self.string_final_codes)
        file_open.close()


    def compile2Shell(self):
        string_command_all = ""
        string_font_all = ""
        string_image_all = ""
        string_button_all = ""
        string_checkbutton_all = ""
        string_entry_all = ""
        string_frame_all = ""
        string_labelframe_all = ""
        string_label_all = ""
        string_listbox_all = ""
        string_menubutton_all = ""
        string_message_all = ""
        string_radiobutton_all = ""
        string_scale_all = ""
        string_spinbox_all = ""
        string_text_all = ""
        string_framepw_all = ""
        string_panedwindow_all = ""
        string_panes = ""
        ### Run main window and its properties
        string_window_prop = ""
        string_iconphoto = ""
        string_header = "from tkinter import *\nfrom tkinter import font \n\nwindowDesign = Tk()"
        string_commands = ''
        string_mainloop = "windowDesign.mainloop()"
        for k,v in zip(dictDesignWindowPropCollect.keys(), dictDesignWindowPropCollect.values()):
            if k == "iconphoto":
                string_iconphoto = f"IconPhoto = {v})"
                continue
            string_window_prop = string_window_prop + v + "\n"
        string_all_header = string_header+"\n"+string_iconphoto+"\n"+string_window_prop

        ##### Commands Output section for Design window widgets
        for com in windowObject.commands_all:
            string_commands = ""
            if windowObject.commands_all[com] == None:
                continue
            else:
                com_value = windowObject.commands_all[com]
                string_commands = string_commands + f"def {com_value}():      # Command for {com}" + "\n"
                string_commands = string_commands + "    pass"
            string_command_all = string_command_all + string_commands

        for i,j,k in zip(arrangeObject.dictCountWidget.keys(), dict_.items(), arrangeObject.dictLayoutConfig.items()):
            new_dict_main = {}
            new_dict_layout = {}
            if i.startswith("FramePW")|i.startswith("PanedWindow"):
                continue;

            else:
                string_font_button = ""
                string_image_button = ""
                if i.startswith("Button"):

                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_button = string_font_button + f"{n} = font.Font(name = '{font_name}', " \
                                                            f"family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_button

                    widget_image = j["image"]
                    for im in windowObject.dictCountImage:
                        if widget_image == windowObject.dictCountImage[im].name:
                            image_name = windowObject.dictCountImage[im].name
                            image_file = windowObject.dictCountImage[im].cget("file")
                            string_image_button = f"{im} = PhotoImage(name = '{image_name}', file = '{image_file}')\n"
                        else:
                            pass
                    string_image_all = string_image_all + string_image_button

                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Button("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    if windowObject.commands_all[i] == None:
                        widgetStr = widgetStr + f")"
                    else:
                        widgetStr = widgetStr + f"command = {windowObject.commands_all[i]})"

                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                      f"anchor = '{k['anchor']}')"
                    widgetStr = f"{i} = {widgetStr}\n"
                    string_button_all = string_button_all + widgetStr


                if i.startswith("Checkbutton"):
                    string_font_checkbutton = ""
                    string_image_checkbutton = ""
                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_checkbutton = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_checkbutton
                    widget_image = j["image"]
                    for im in windowObject.dictCountImage:
                        if widget_image == windowObject.dictCountImage[im].name:
                            image_name = windowObject.dictCountImage[im].name
                            image_file = windowObject.dictCountImage[im].cget("file")
                            string_image_checkbutton = f"{im} = PhotoImage(name = '{image_name}', file = '{image_file}')\n"
                        else:
                            pass
                    string_image_all = string_image_all + string_image_checkbutton

                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Checkbutton("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    if windowObject.commands_all[i] == None:
                        widgetStr = widgetStr + f")"
                    else:
                        widgetStr = widgetStr + f"command = {windowObject.commands_all[i]})"

                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                          f"anchor = '{k['anchor']}')"
                    widgetStr = f"{i} = {widgetStr}\n"
                    string_checkbutton_all = string_checkbutton_all + widgetStr


                if i.startswith("Entry"):
                    string_font_entry = ""
                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_entry = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_entry
                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Entry("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    widgetStr = widgetStr + ")"
                    widgetStr = f"{i} = {widgetStr}"
                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                          f"anchor = '{k['anchor']}')\n"
                    string_entry_all = string_entry_all + widgetStr

                if i.startswith("Frame"):

                    j = dict(sorted(j[1].items()))
                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Frame("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    widgetStr = widgetStr + ")"
                    widgetStr = f"{i} = {widgetStr}"
                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                          f"anchor = '{k['anchor']}')\n"
                    string_frame_all = string_frame_all + widgetStr
                    

                if i.startswith("LabelFrame"):
                    string_font_labelframe = ""
                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_labelframe = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_labelframe
                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"LabelFrame("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    widgetStr = widgetStr + ")"

                    widgetStr = f"{i} = {widgetStr}"
                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}," \
                          f"anchor = '{k['anchor']}')\n"
                    string_labelframe_all = string_labelframe_all + widgetStr
                
                if i.startswith("Label"):
                    string_font_label = ""
                    string_image_label = ""
                    try:
                        j = dict(sorted(j[1].items()))
                        widget_font = j["font"]
                        for n in windowObject.dictCountFont:
                            if widget_font == windowObject.dictCountFont[n].name:
                                font_name = windowObject.dictCountFont[n].name
                                actual = windowObject.dictCountFont[n].actual()
                                string_font_label = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                      f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                      f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                      f"overstrike = {actual['overstrike']})\n"
                            else:
                                pass
                        string_font_all = string_font_all + string_font_label
                        widget_image = j["image"]
                        for im in windowObject.dictCountImage:
                            if widget_image == windowObject.dictCountImage[im].name:
                                image_name = windowObject.dictCountImage[im].name
                                image_file = windowObject.dictCountImage[im].cget("file")
                                string_image_label = f"{im} = PhotoImage(name = '{image_name}', file = '{image_file}')\n"
                            else:
                                pass
                        string_image_all = string_image_all + string_image_label

                        k = arrangeObject.dictLayoutConfig[i]
                        widgetStr = f"Label("
                        for jj in j:
                            dd = jj.replace("'", "")
                            dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                            widgetStr = widgetStr + dd
                        widgetStr = widgetStr + ")"
                        widgetStr = f"{i} = {widgetStr}"
                        widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, "\
                              f"anchor = '{k['anchor']}')\n"
                        string_label_all = string_label_all + widgetStr
                    except KeyError:
                        pass

                if i.startswith("Listbox"):
                    string_font_listbox = ""
                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_listbox = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_listbox
                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Listbox("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    widgetStr = widgetStr + ")"
                    widgetStr = f"{i} = {widgetStr}"
                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                          f"anchor = '{k['anchor']}')\n"
                    string_listbox_all = string_listbox_all + widgetStr

                if i.startswith("Menubutton"):
                    string_font_menubutton = ""
                    string_image_menubutton = ""
                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_menubutton = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                        widget_image = j["image"]
                    string_font_all = string_font_all + string_font_menubutton
                    for im in windowObject.dictCountImage:
                        if widget_image == windowObject.dictCountImage[im].name:
                            image_name = windowObject.dictCountImage[im].name
                            image_file = windowObject.dictCountImage[im].cget("file")
                            string_image_menubutton = f"{im} = PhotoImage(name = '{image_name}', file = '{image_file}')\n"
                        else:
                            pass
                    string_image_all = string_image_all + string_image_menubutton
                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Menubutton("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    widgetStr = widgetStr + ")"
                    widgetStr = f"{i} = {widgetStr}"
                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                          f"anchor = '{k['anchor']}')\n"
                    string_menubutton_all = string_menubutton_all + widgetStr

                if i.startswith("Message"):
                    string_font_message = ""
                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_message = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_message
                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Message("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    widgetStr = widgetStr + ")"
                    widgetStr = f"{i} = {widgetStr}"
                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                          f"anchor = '{k['anchor']}')\n"
                    string_message_all = string_message_all + widgetStr

                if i.startswith("Radiobutton"):
                    string_font_radiobutton = ""
                    string_image_radiobutton = ""
                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_radiobutton = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_radiobutton
                    widget_image = j["image"]
                    for im in windowObject.dictCountImage:
                        if widget_image == windowObject.dictCountImage[im].name:
                            image_name = windowObject.dictCountImage[im].name
                            image_file = windowObject.dictCountImage[im].cget("file")
                            string_image_radiobutton = f"{im} = PhotoImage(name = '{image_name}', file = '{image_file}')\n"
                        else:
                            pass
                    string_image_all = string_image_all + string_image_radiobutton

                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Radiobutton("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    if windowObject.commands_all[i] == None:
                        widgetStr = widgetStr + f")"
                    else:
                        widgetStr = widgetStr + f"command = {windowObject.commands_all[i]})"

                    widgetStr = f"{i} = {widgetStr}"
                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                          f"anchor = '{k['anchor']}')\n"
                    string_radiobutton_all = string_radiobutton_all + widgetStr

                if i.startswith("Scale"):
                    string_font_scale = ""
                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_scale = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_scale
                    k = arrangeObject.dictLayoutConfig[i]
                    if j["orient"] == "vertical":
                        k_width = int(k["width"])-70
                        widgetStr = f"Scale("
                        for jj in j:
                            dd = jj.replace("'", "")
                            dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                            widgetStr = widgetStr + dd
                        if windowObject.commands_all[i] == None:
                            widgetStr = widgetStr + f" width = {k_width})"
                        else:
                            widgetStr = widgetStr + f"width = {k_width}, command = {windowObject.commands_all[i]})"

                        widgetStr = f"{i} = {widgetStr}"
                        widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, anchor = '{k['anchor']}')\n"
                        string_scale_all = string_scale_all + widgetStr

                    elif j["orient"] == "horizontal":
                        k_height = int(k["height"])-70
                        widgetStr = f"Scale("
                        for jj in j:
                            dd = jj.replace("'", "")
                            dd = f"{dd} = {j[jj], }".replace("(","").replace(")"," ")
                            widgetStr = widgetStr + dd
                        if windowObject.commands_all[i] == None:
                            widgetStr = widgetStr + f" width = {k_height})"
                        else:
                            widgetStr = widgetStr + f"width = {k_height}, command = {windowObject.commands_all[i]})"

                        widgetStr = f"{i} = {widgetStr}"
                        widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, width = {k['width']}, anchor = '{k['anchor']}')\n"
                        string_scale_all = string_scale_all + widgetStr

                if i.startswith("Spinbox"):
                    string_font_spinbox = ""
                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_spinbox = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_spinbox
                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Spinbox("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    if windowObject.commands_all[i] == None:
                        widgetStr = widgetStr + f")"
                    else:
                        widgetStr = widgetStr + f"command = {windowObject.commands_all[i]})"

                    widgetStr = f"{i} = {widgetStr}"
                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                          f"anchor = '{k['anchor']}')\n"
                    string_scale_all = string_scale_all + widgetStr

                if i.startswith("Text"):
                    string_font_text = ""
                    j = dict(sorted(j[1].items()))
                    widget_font = j["font"]
                    for n in windowObject.dictCountFont:
                        if widget_font == windowObject.dictCountFont[n].name:
                            font_name = windowObject.dictCountFont[n].name
                            actual = windowObject.dictCountFont[n].actual()
                            string_font_text = f"{n} = font.Font(name = '{font_name}', family = '{actual['family']}', " \
                                  f"size = {actual['size']}, weight = '{actual['weight']}', " \
                                  f"slant = '{actual['slant']}', underline = {actual['underline']}, " \
                                  f"overstrike = {actual['overstrike']})\n"
                        else:
                            pass
                    string_font_all = string_font_all + string_font_text
                    k = arrangeObject.dictLayoutConfig[i]
                    widgetStr = f"Text("
                    for jj in j:
                        dd = jj.replace("'", "")
                        dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                        widgetStr = widgetStr + dd
                    widgetStr = widgetStr + ")"
                    widgetStr = f"{i} = {widgetStr}"
                    widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                          f"anchor = '{k['anchor']}')\n"
                    string_text_all = string_text_all + widgetStr

        for i, j, k in zip(arrangeObject.dictCountWidget.keys(), dict_.items(), arrangeObject.dictLayoutConfig.items()):
            if i.startswith("FramePW"):
                j = dict(sorted(j[1].items()))
                k = arrangeObject.dictLayoutConfig[i]
                widgetStr = f"Frame("
                for jj in j:
                    dd = jj.replace("'", "")
                    dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                    widgetStr = widgetStr + dd
                widgetStr = widgetStr + ")"
                widgetStr = f"{i} = {widgetStr}"
                widgetStr = widgetStr + f"\n{i}.place(x = {k['x']}, y = {k['y']}, height = {k['height']}, width = {k['width']}, " \
                      f"anchor = '{k['anchor']}')\n"
                masterPW = i
                string_framepw_all = string_framepw_all + widgetStr

            elif i.startswith("PanedWindow"):
                j = dict(sorted(j[1].items()))
                widgetStr = f"PanedWindow({masterPW}, "
                for jj in j:
                    dd = jj.replace("'", "")
                    dd = f"{dd} = {j[jj], }".replace("(", "").replace(")", " ")
                    widgetStr = widgetStr + dd
                widgetStr = widgetStr + ")"

                widgetStr = f"{i} = {widgetStr}"
                widgetStr = widgetStr + f"\n{i}.place(relheight = 1, relwidth = 0.8)\n"
                for ke,val in zip(arrangeObject.dict_widget_panes.keys(), arrangeObject.dict_widget_panes.values()):
                    print(arrangeObject.dict_widget_panes)
                    string_panes = string_panes + f"{ke}.lift()\n"
                    string_panes = string_panes + f"{val}.add({ke})\n"
                string_panedwindow_all = string_panedwindow_all + widgetStr


        self.string_final_codes = string_all_header + "\n" + string_command_all + "\n" + string_font_all + string_image_all + \
        string_button_all + string_checkbutton_all + string_entry_all + string_frame_all + string_labelframe_all + \
        string_label_all + string_listbox_all + string_menubutton_all + string_message_all + string_radiobutton_all + \
        string_scale_all + string_spinbox_all + string_text_all + string_framepw_all + string_panedwindow_all + \
        string_panes + "\n" + string_mainloop



class DragDropResizeWidget(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Motion>", self.motion1Both)

    def cursorChange(self, event):
        self["cursor"] = windowObject.combo4cursor.get()

    def startDrag(self, event):
        self.start_drag_x = event.x
        self.start_drag_y = event.y

    def motionDrag(self, event):
        self["cursor"] = "bogosity"
        self.place_configure(anchor="nw")
        new_x = (self.winfo_x() + event.x) - self.start_drag_x
        new_y = (self.winfo_y() + event.y) - self.start_drag_y
        self.place(x=new_x, y=new_y)

    def motion1Both(self, event):
        self.xx = self.winfo_x() + int(self.place_info()["width"])
        self.yy = self.winfo_y() + int(self.place_info()["height"])
        self.ttx = event.x + self.winfo_x()
        self.tty = event.y + self.winfo_y()

        if ((self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)) & (
                (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
            self["cursor"] = "bottom_right_corner"
            self.bind("<Button1-Motion>", self.motionBottomRight)

        elif ((self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                self.winfo_x() == self.ttx - 3)) & (
                (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
            self["cursor"] = "bottom_left_corner"
            self.bind("<Button1-Motion>", self.motionBottomLeft)

        elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                self.winfo_y() == self.tty - 3)) & (
                (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                self.winfo_x() == self.ttx - 3)):
            self["cursor"] = "top_left_corner"
            self.bind("<Button1-Motion>", self.motionTopLeft)

        elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                self.winfo_y() == self.tty - 3)) & (
                (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)):
            self["cursor"] = "top_right_corner"
            self.bind("<Button1-Motion>", self.motionTopRight)

        elif (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3):
            self["cursor"] = "right_side"
            self.bind("<Button1-Motion>", self.motionRight)

        elif (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3):
            self["cursor"] = "bottom_side"
            self.bind("<Button1-Motion>", self.motionBottom)

        elif (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (self.winfo_x() == self.ttx - 3):
            self["cursor"] = "left_side"
            self.bind("<Button1-Motion>", self.motionLeft)

        elif (self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (self.winfo_y() == self.tty - 3):
            self["cursor"] = "top_side"
            self.bind("<Button1-Motion>", self.motionTop)


        else:
            self["cursor"] = windowObject.combo4cursor.get()
            self.bind("<Button-1>", self.startDrag)
            self.bind("<Button1-Motion>", self.motionDrag)
            self.bind("<ButtonRelease-1>", self.cursorChange)

    def motionTop(self, event):
        self.place_configure(x=self.winfo_x(), y=(self.winfo_y() + int(self.place_info()["height"])), anchor="sw")
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self.place_configure(height=new_height)

    def motionBottom(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self.place_configure(height=new_height)

    def motionLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = (0 - event.x) + int(self.place_info()["width"])
        self.place_configure(width=new_width)

    def motionRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        self.place_configure(width=new_width)

    def motionTopLeft(self, event):
        self.place_configure(x=self.winfo_x() + int(self.place_info()["width"]),
                             y=self.winfo_y() + int(self.place_info()["height"]), anchor="se")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = 0 - event.y + int(self.place_info()["height"])
        self.place_configure(width=new_width, height=new_height)

    def motionTopRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y() + int(self.place_info()["height"]), anchor="sw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self.place_configure(width=new_width, height=new_height)

    def motionBottomLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self.place_configure(width=new_width, height=new_height)

    def motionBottomRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self.place_configure(width=new_width, height=new_height)


class Scale_H(Scale):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Motion>", self.motion1Both)

    def cursorChange(self, event):
        self["cursor"] = windowObject.combo4cursor.get()


    def startDrag(self, event):

        self.start_drag_x = event.x
        self.start_drag_y = event.y

    def motionDrag(self, event):
        self["cursor"] = "bogosity"
        self.place_configure(anchor="nw")
        new_x = (self.winfo_x() + event.x) - self.start_drag_x
        new_y = (self.winfo_y() + event.y) - self.start_drag_y
        self.place(x=new_x, y=new_y)

    def motion1Both(self, event):

        if self.identify(event.x, event.y) == "":
            self.xx = self.winfo_x() + int(self.place_info()["width"])
            self.yy = self.winfo_y() + int(self.place_info()["height"])
            self.ttx = event.x + self.winfo_x()
            self.tty = event.y + self.winfo_y()

            if ((self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)) & (
                    (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
                self["cursor"] = "bottom_right_corner"
                self.bind("<Button1-Motion>", self.motionBottomRight)

            elif ((self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                    self.winfo_x() == self.ttx - 3)) & (
                    (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
                self["cursor"] = "bottom_left_corner"
                self.bind("<Button1-Motion>", self.motionBottomLeft)

            elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                    self.winfo_y() == self.tty - 3)) & (
                    (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                    self.winfo_x() == self.ttx - 3)):
                self["cursor"] = "top_left_corner"
                self.bind("<Button1-Motion>", self.motionTopLeft)

            elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                    self.winfo_y() == self.tty - 3)) & (
                    (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)):
                self["cursor"] = "top_right_corner"
                self.bind("<Button1-Motion>", self.motionTopRight)

            elif (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3):
                self["cursor"] = "right_side"
                self.bind("<Button1-Motion>", self.motionRight)

            elif (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3):
                self["cursor"] = "bottom_side"
                self.bind("<Button1-Motion>", self.motionBottom)

            elif (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (self.winfo_x() == self.ttx - 3):
                self["cursor"] = "left_side"
                self.bind("<Button1-Motion>", self.motionLeft)

            elif (self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (self.winfo_y() == self.tty - 3):
                self["cursor"] = "top_side"
                self.bind("<Button1-Motion>", self.motionTop)


            else:
                self["cursor"] = windowObject.combo4cursor.get()
                self.bind("<Button-1>", self.startDrag)
                self.bind("<Button1-Motion>", self.motionDrag)
                self.bind("<ButtonRelease-1>", self.cursorChange)

        else:
            self.bind("<Button1-Motion>", lambda x: None)

    def motionTop(self, event):
        self.place_configure(x=self.winfo_x(), y=(self.winfo_y() + int(self.place_info()["height"])), anchor="sw")
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(height=new_height)

    def motionBottom(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(height=new_height)

    def motionLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = (0 - event.x) + int(self.place_info()["width"])
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width)

    def motionRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width)

    def motionTopLeft(self, event):
        self.place_configure(x=self.winfo_x() + int(self.place_info()["width"]),
                             y=self.winfo_y() + int(self.place_info()["height"]), anchor="se")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = 0 - event.y + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width, height=new_height)

    def motionTopRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y() + int(self.place_info()["height"]), anchor="sw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width, height=new_height)

    def motionBottomLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width, height=new_height)

    def motionBottomRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["height"]) - 33)
        self.place_configure(width=new_width, height=new_height)


class Scale_V(Scale):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Motion>", self.motion1Both)

    def cursorChange(self, event):
        self["cursor"] = windowObject.combo4cursor.get()

    def startDrag(self, event):

        self.start_drag_x = event.x
        self.start_drag_y = event.y

    def motionDrag(self, event):
        self["cursor"] = "bogosity"
        self.place_configure(anchor="nw")
        new_x = (self.winfo_x() + event.x) - self.start_drag_x
        new_y = (self.winfo_y() + event.y) - self.start_drag_y
        self.place(x=new_x, y=new_y)

    def motion1Both(self, event):

        if self.identify(event.x, event.y) == "":
            self.xx = self.winfo_x() + int(self.place_info()["width"])
            self.yy = self.winfo_y() + int(self.place_info()["height"])
            self.ttx = event.x + self.winfo_x()
            self.tty = event.y + self.winfo_y()

            if ((self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)) & (
                    (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
                self["cursor"] = "bottom_right_corner"
                self.bind("<Button1-Motion>", self.motionBottomRight)

            elif ((self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                    self.winfo_x() == self.ttx - 3)) & (
                    (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3)):
                self["cursor"] = "bottom_left_corner"
                self.bind("<Button1-Motion>", self.motionBottomLeft)

            elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                    self.winfo_y() == self.tty - 3)) & (
                    (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (
                    self.winfo_x() == self.ttx - 3)):
                self["cursor"] = "top_left_corner"
                self.bind("<Button1-Motion>", self.motionTopLeft)

            elif ((self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (
                    self.winfo_y() == self.tty - 3)) & (
                    (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3)):
                self["cursor"] = "top_right_corner"
                self.bind("<Button1-Motion>", self.motionTopRight)

            elif (self.ttx == self.xx - 1) | (self.ttx == self.xx - 2) | (self.ttx == self.xx - 3):
                self["cursor"] = "right_side"
                self.bind("<Button1-Motion>", self.motionRight)

            elif (self.tty == self.yy - 1) | (self.tty == self.yy - 2) | (self.tty == self.yy - 3):
                self["cursor"] = "bottom_side"
                self.bind("<Button1-Motion>", self.motionBottom)

            elif (self.winfo_x() == self.ttx - 1) | (self.winfo_x() == self.ttx - 2) | (self.winfo_x() == self.ttx - 3):
                self["cursor"] = "left_side"
                self.bind("<Button1-Motion>", self.motionLeft)

            elif (self.winfo_y() == self.tty - 1) | (self.winfo_y() == self.tty - 2) | (self.winfo_y() == self.tty - 3):
                self["cursor"] = "top_side"
                self.bind("<Button1-Motion>", self.motionTop)


            else:
                self["cursor"] = windowObject.combo4cursor.get()
                self.bind("<Button-1>", self.startDrag)
                self.bind("<Button1-Motion>", self.motionDrag)
                self.bind("<ButtonRelease-1>", self.cursorChange)

        else:
            self.bind("<Button1-Motion>", lambda x: None)

    def motionTop(self, event):
        self.place_configure(x=self.winfo_x(), y=(self.winfo_y() + int(self.place_info()["height"])), anchor="sw")
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(height=new_height)

    def motionBottom(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(height=new_height)

    def motionLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = (0 - event.x) + int(self.place_info()["width"])
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width)

    def motionRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width)

    def motionTopLeft(self, event):
        self.place_configure(x=self.winfo_x() + int(self.place_info()["width"]),
                             y=self.winfo_y() + int(self.place_info()["height"]), anchor="se")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = 0 - event.y + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width, height=new_height)

    def motionTopRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y() + int(self.place_info()["height"]), anchor="sw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = (0 - event.y) + int(self.place_info()["height"])
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width, height=new_height)

    def motionBottomLeft(self, event):
        self.place_configure(x=(self.winfo_x() + int(self.place_info()["width"])), y=self.winfo_y(), anchor="ne")
        new_width = 0 - event.x + int(self.place_info()["width"])
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width, height=new_height)

    def motionBottomRight(self, event):
        self.place_configure(x=self.winfo_x(), y=self.winfo_y(), anchor="nw")
        new_width = int(self.place_info()["width"]) + (event.x - int(self.place_info()["width"]))
        new_height = int(self.place_info()["height"]) + (event.y - int(self.place_info()["height"]))
        self["width"] = 0.9 * (int(self.place_info()["width"]) - 43)
        self.place_configure(width=new_width, height=new_height)

windowPRO = Tk()  ######## Creates Main Window



windowObject = pyPROApp(windowPRO)  ####### Instance Object for pyPROApp class
windowObject.widgetTreeview()

##### Lists of widget control variables names
list_button = [f"Button{x}" for x in range(0,1000)]    #### list to contain widget control variables names for Button
list_checkbutton = [f"Checkbutton{x}" for x in range(0,1000)]   #### list to contain widget control variables names for Checkbutton
list_entry = [f"Entry{x}" for x in range(0,1000)]
list_label = [f"Label{x}" for x in range(0,1000)]
list_listbox = [f"Listbox{x}" for x in range(0,1000)]
list_menubutton = [f"Menubutton{x}" for x in range (0,1000)]
list_message = [f"Message{x}" for x in range (0,1000)]
list_radiobutton = [f"Radiobutton{x}" for x in range(0,1000)]
list_scale = [f"Scale{x}" for x in range(0,1000)]
list_scrollbar = [f"Scrollbar{x}" for x in range (0, 1000)]
list_spinbox = [f"Spinbox{x}" for x in range(0,1000)]
list_text = [f"Text{x}" for x in range(0,1000)]
list_frame = [f"Frame{x}" for x in range(0,1000)]
list_labelframe = [f"LabelFrame{x}" for x in range(0,1000)]
list_framepw = [f"FramePW{x}" for x in range(0,1000)]
list_panedwindow = [f"PanedWindow{x}" for x in range(0,1000)]

dict_ = {}                                      #### Dictionary to hold attributes for control variables
dictAttributeEditorUpdate = {}                  #### Dictionary to update Attribute Editor for any selected widget
# dictAttributeCollect = {}                       #### Dictionary to collect attributes to display in Attribute Editor


arrangeObject = WidgetArrange()  ####### Instance Object for WidgetArrange class
arrangeObject.refreshAttributes()


####### Design Window - To Work On
windowDesign = Tk()
windowDesign.title("Design Window")
windowDesign.geometry("%dx%d+%d+%d" % (screen_width / 2, screen_height / 1.57, screen_width / 4.5, screen_height / 3.36))


### Events For Design Window
windowDesign.bind("<Button-1>", arrangeObject.executeWidgetsOnDesignWindow)
windowObject.tree4Widget.bind("<<TreeviewSelect>>", arrangeObject.focusWidgetTree)  ### Event for Widget Tree
windowDesign.bind_all("<ButtonRelease-1>", arrangeObject.motionRelease)

implementFont_determine = None    ### Variable that determines whether to run implementFont command
windowPRO.mainloop()
